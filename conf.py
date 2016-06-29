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

from pyrcb import IDefaultDict

# Maps nicknames to tuples containing a voice name and a pitch.
voices = IDefaultDict(lambda: ("en-us", "70"), {
    "nickname1": ("en-uk+f3", "65"),
    "nickname2": ("en-us+m5", "40"),
})

# Sent to users when they first connect to espeaker.
# XML comments are only spoken when running espeak without SSML (option -m).
connect_message = """
<!-- If you can hear this, you are not running espeak correctly. -->
<!-- You must run espeak with option dash lowercase m. -->
"""
