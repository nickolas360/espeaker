# To the extent possible under law, the author(s) have dedicated all
# copyright and neighboring rights to this software to the public domain
# worldwide. This software is distributed without any warranty. See
# <http://creativecommons.org/publicdomain/zero/1.0/> for a copy of the
# CC0 Public Domain Dedication.

from pyrcb2 import IDefaultDict

# Maps nicknames to tuples containing a voice name and a pitch.
voices = IDefaultDict(lambda: ("en-us", "70"), {
    "nickname1": ("en+f3", "65"),
    "nickname2": ("en-us+m5", "40"),
})

# Sent to users when they first connect to espeaker.
# XML comments are only spoken when running espeak without SSML (option -m).
connect_message = """\
<!-- If you can hear this, you are not running espeak correctly. -->
<!-- You must run espeak with option dash lowercase m. -->
"""
