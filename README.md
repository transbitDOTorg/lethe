lethe
=====

Secure self-destructing messaging service for the privacy conscious user.  Designed to be deployed over anonymity networks such as Tor and I2P.

Lethe provides the following:
+ Forced PGP encryption for all messages
+ Ability to be deployed without disk, or with no write privileges to disk
+ Automatic message deletion after configurable time period
+ Simple, easy-to-use interface
+ Flexible API for use with any other webapp or hidden service
+ Ability to be easily deployed over Tor and I2P
+ Simple codebase of around 60 lines, excluding templates
+ Flexible licensing

In short, lethe provides an additional layer of security for the paranoid web user.  In the event a lethe service is compromised, only unread and encrypted messages dating back seven days can be read.  Users can also host their own private lethe services.

Installation
=====

Installation is simple.  After cloning the git repository,
```
python virtualenv.py flask
source flask/bin/activate
pip install flask
vi config.py // Modify appropriate values
python lethe.py > /dev/null
```

That's it, lethe is now up and running.  To deploy lethe, point a Tor or I2P hidden service at localhost:your configured port.  It's that easy.
If you wish to deploy lethe on the clearweb, set LISTEN_OUTSIDE_LOCALHOST to True in config.py, but note that this is not recommended.

More advanced deployments, such as subdomain or subdirectory deployments, can be accomplished by deploying the Lethe Flask app through one of several popular webservers.
See the Flask documentation under Deployments for more details.

Limitations
=====
Due to our philosophy of keeping data off the disk, restarting the lethe service will lead to complete information loss.

This is unfortunately an unavoidable design decision.  Beore making a lethe service public, ensure the stability of your host!

Contributions are welcomed.  Submit pull requests, issues, and feel free to contact us through GitHub.
