weechat-pushover
================

Weechat plugin to send notifications about query messages and channel hilights to your iPhone or Android via pushover.net.

## Installation and Configuration

In order to use the plugin you need to take the following steps:

1. Register an account at http://pushover.net
2. Create a new application at https://pushover.net/apps/build
3. Note the "token" for your new application (referenced as TOKEN later on)
4. From the Dashboard at https://pushover.net note your "User key" (referenced as USERKEY later on)
5. put "pushover.py" to ~/.weechat/python
6. start the plugin with "/python load pushover.py"
7. Set user key and token by doing
8. /set plugins.var.python.pushover.user USERKEY
9. /set plugins.var.python.pushover.token TOKEN 

## License

The script is derived from other scripts (see pushover.py for history). It is released under the GPL v2. See LICENSE file for details.

## Author

Author: Caspar Clemens Mierau <ccm@screenage.de>

