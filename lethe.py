from flask import Flask, request, render_template, jsonify, abort, flash
from config import *
import uuid, time
from threading import Thread

lethe = Flask(__name__)

# Dirty global for message storage
lethe.lethe_messages = {}

# -----------------------------------
# Lethe Views and Routes
@lethe.route("/", methods=["GET", "POST"])
def post():
    if request.method == "POST":
        try:
            return_json = request.form.get("json", False)
            return post_message_response(request.form["secret"], return_json)
        except KeyError:
            abort(404)
    return render_template("post.html", action = "Post a message")

@lethe.route("/get/<string:secret_key>")
def get(secret_key):
    return render_template("get.html", secret = get_secret(secret_key), action = "Read Message")

@lethe.route("/get_json/<string:secret_key>")
def get_json(secret_key):
    return jsonify(secret = get_secret(secret_key))

# -----------------------------------
# Lethe controllers / utility methods
def post_message_response(secret, return_json):
    if len(lethe.lethe_messages) > MAX_MESSAGES:
        return render_template("post.html", action = "Error", error = "Maximum number of messages on server reached.  Try again later."), 500
    if not ("BEGIN PGP MESSAGE" in secret and "END PGP MESSAGE" in secret):
        return render_template("post.html", action = "Error", error = "Invalid PGP message.  Please click PGP in the header for a tutorial on using PGP."), 403
    secret_key = str(uuid.uuid4())
    lethe.lethe_messages[secret_key] = Message(secret, time.time())
    if return_json:
        return jsonify(secret_key = secret_key)
    return render_template("posted.html", secret_key = secret_key, EXPIRY = FORGET_AFTER_DAYS, action = "Message Posted")

def get_secret(secret_key):
    try:
        secret = lethe.lethe_messages[secret_key].secret
    except KeyError:
        abort(404)
    del lethe.lethe_messages[secret_key]
    return secret

# http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-email-support
def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target = f, args = args, kwargs = kwargs)
        thr.start()
    return wrapper

@async
def clean_garbage():
    while True:
        # @todo - More intelligence than a linear search
        sweep_time = time.time()
        for secret_key, message in lethe.lethe_messages.iteritems():
            if (sweep_time - message.timestamp) > (86400 * FORGET_AFTER_DAYS):
                del lethe.lethe_messages[secret_key]
        time.sleep(7200)

# -----------------------------------
# Lethe models
class Message(object):
    def __init__(self, secret, timestamp):
        self.secret = secret
        self.timestamp = timestamp

# -----------------------------------
if __name__ == "__main__":
    # Initiate old message garbage collector
    clean_garbage()
    if LISTEN_OUTSIDE_LOCALHOST:
        lethe.run(host="0.0.0.0", port = LETHE_PORT, debug = False)
    else:
        lethe.run(port = LETHE_PORT, debug = False)
