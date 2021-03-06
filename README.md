espeaker
========

Version 0.2.1

**espeaker** is an IRC bot which allows users to listen to IRC with the
text-to-speech program [espeak]. It converts IRC messages into SSML data that
can be piped to and read by espeak. Users can be given unique voices.

[espeak]: https://en.wikipedia.org/wiki/ESpeak

espeaker runs over a network socket, allowing people to connect to it and pipe
the data to espeak. Use the command ``nc <espeaker-host> <espeaker-port> |
espeak -m`` to connect and listen to espeaker. Option ``-m`` enables SSML
support in espeak.

Edit ``conf.py`` to give users espeak voices. See ``espeak --voices`` and
``espeak --voices=variant`` to see what voices and variants you can use.

Usage
-----

``espeaker <port> <irc-host> <irc-port> [--ssl] <nickname> <channel>``

``<port>`` is the port the espeaker server should run on, not the port of the
IRC server (which is ``<irc-port>``).

Use ``--ssl`` to connect to the IRC server with SSL/TLS.

espeaker will ask for a NickServ password when started. Supply an empty
password if you don't want to use one.

What's new
----------

Version 0.2.1:

* Fixed a minor error in conf.py.

Version 0.2.0:

* Switched to pyrcb2.

Dependencies
------------

* Python ≥ 3.5
* [pyrcb2](https://pypi.python.org/pypi/pyrcb2) ≥ 0.1.2
