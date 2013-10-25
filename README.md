lethe
=====

Secure one-time messaging service for the privacy conscious user.  Designed to be deployed over anonymity networks such as Tor and I2P.

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

That's it.

Limitations
=====
Due to our philosophy of keeping data off the disk, restarting the lethe service will lead to complete information loss.

This is unfortunately an unavoidable design decision.  Beore making a lethe service public, ensure the stability of your host!

Contributions are welcomed.  Submit pull requests, issues, and feel free to contact us through GitHub.
