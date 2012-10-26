# Author: Caspar Clemens Mierau <ccm@screenage.de>
# Homepage: https://github.com/leitmedium/weechat-pushover
# Derived from: notifo
#   Author: ochameau <poirot.alex AT gmail DOT com>
#   Homepage: https://github.com/ochameau/weechat-notifo
# An from: notify
#   Author: lavaramano <lavaramano AT gmail DOT com>
#   Improved by: BaSh - <bash.lnx AT gmail DOT com>
#   Ported to Weechat 0.3.0 by: Sharn - <sharntehnub AT gmail DOT com)
# And from: notifo_notify
#   Author: SAEKI Yoshiyasu <laclef_yoshiyasu@yahoo.co.jp>
#   Homepage: http://bitbucket.org/laclefyoshi/weechat/
#
# This plugin sends push notifications to your iPhone or Android smartphone
# by using pushover.net. In order to use it, please follow these steps:
#
# 1. Register an account at http://pushover.net
# 2. Create a new application at https://pushover.net/apps/build
# 3. Note the "token" for your new application (referenced as TOKEN later on)
# 4. From the Dashboard at https://pushover.net note your "User key" (referenced as USERKEY later on)
# 5. Install the pushover app on your iPhone/Android and login
# 6. put "pushover.py" to ~/.weechat/python
# 7. start the plugin with "/python load pushover.py"
# 8. Set user key and token by doing
# 9. /set plugins.var.python.pushover.user USERKEY
# 10. /set plugins.var.python.pushover.token TOKEN 
#
# On security: This plugin does not use end-to-end-encryption. Please see
# the security related FAQ at pushover.net for details
#
# Requires Weechat 0.3.0, curl
# Released under GNU GPL v2, see LICENSE file for details
#
# 2012-10-26, au <poirot.alex@gmail.com>:
#     version 0.1: merge notify.py and notifo_notify.py in order to avoid
#                  sending notifications when channel or private buffer is
#                  already opened

import weechat, string, os, urllib

weechat.register("pushover", "Caspar Clemens Mierau <ccm@screenage.de>", "0.1", "GPL", "pushover: Send push notifications to you iPhone/Android about your private message and highligts.", "", "")

settings = {
    "user": "",
    "token": "",
}

for option, default_value in settings.items():
    if weechat.config_get_plugin(option) == "":
        weechat.prnt("", weechat.prefix("error") + "pushover: Please set option: %s" % option)
        weechat.prnt("", "pushover: /set plugins.var.python.pushover.%s STRING" % option)

# Hook privmsg/hilights
weechat.hook_print("", "irc_privmsg", "", 1, "notify_show", "")

# Functions
def notify_show(data, bufferp, uber_empty, tagsn, isdisplayed,
        ishilight, prefix, message):

    #if ((bufferp == weechat.current_buffer()) & (weechat.config_get_plugin("show_active_buffer")!="1")):  
    #    pass

    if weechat.buffer_get_string(bufferp, "localvar_type") == "private":
        show_notification(prefix, message)

    elif ishilight == "1":
        buffer = (weechat.buffer_get_string(bufferp, "short_name") or
                weechat.buffer_get_string(bufferp, "name"))
        show_notification(buffer, prefix + ": " + message)

    return weechat.WEECHAT_RC_OK

def show_notification(chan, message):
    PUSHOVER_USER = weechat.config_get_plugin("user")
    PUSHOVER_API_SECRET = weechat.config_get_plugin("token")
    if PUSHOVER_USER != "" and PUSHOVER_API_SECRET != "":
        message = urllib.quote_plus(message)
        os.system("curl -s -d token=" + PUSHOVER_API_SECRET + " -d user=" + PUSHOVER_USER + " -d message=" + message + " -d title='weechat: " + chan + "' https://api.pushover.net/1/messages.json")

# vim: autoindent expandtab smarttab shiftwidth=4
