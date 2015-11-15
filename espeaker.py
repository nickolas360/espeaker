#!/usr/bin/env python3
# Copyright (C) 2015 nickolas360 (https://github.com/nickolas360)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from pyrcb import IRCBot
from getpass import getpass
from xml.sax.saxutils import escape
import conf
import socket
import sys
import threading

usage = "Usage: espeaker <port> <irc-host> <irc-port> <nickname> <channel>"

ssml_template = """
<voice name="{0}">
    <prosody pitch="{1}">
        {2}
    </prosody>
</voice>
"""


class ESpeaker(IRCBot):
    def __init__(self, *args, **kwargs):
        super(ESpeaker, self).__init__(*args, **kwargs)
        self.clients = []

    def start_server(self, port):
        s = socket.socket()
        try:
            s.bind(("", port))
            s.listen(5)
            while True:
                client, address = s.accept()
                client.sendall(conf.connect_message.encode("utf8"))
                self.clients.append(client)
        finally:
            s.shutdown(socket.SHUT_RDWR)
            s.close()

    def broadcast(self, message):
        disconnected = []
        for client in self.clients:
            try:
                client.sendall(message)
            except (ConnectionError, TimeoutError):
                disconnected.append(client)
        for client in disconnected:
            self.clients.remove(client)

    def on_message(self, message, nickname, channel, is_query):
        if is_query:
            return
        voice, pitch = conf.voices[nickname]
        ssml_data = ssml_template.format(voice, pitch, escape(message))
        self.broadcast(ssml_data.encode("utf8"))
        print("<{0}> {1}".format(nickname, message))


def main():
    if len(sys.argv[1:]) != 5:
        print(usage)
        return

    port, irc_host, irc_port, nickname, channel = sys.argv[1:]
    port, irc_port = int(port), int(irc_port)

    print("Password (empty for none): ", end="", file=sys.stderr, flush=True)
    password = getpass("") if sys.stdin.isatty() else input()

    bot = ESpeaker(debug_print=True)
    bot.connect(irc_host, irc_port)
    threading.Thread(target=bot.start_server, args=[port], daemon=True).start()

    if password:
        bot.password(password)
    bot.register(nickname)
    bot.join(channel)
    bot.listen()
    print("Disconnected from server.")

if __name__ == "__main__":
    main()
