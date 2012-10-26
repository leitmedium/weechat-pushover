weechat-pushover
================

Weechat plugin to send notifications about query messages and channel hilights to your iPhone or Android via pushover.net.

## Installation and Configuration

In order to use the plugin you need to take the following steps:

1. Register an account at http://pushover.net
2. Create a new application at https://pushover.net/apps/build
3. Note the "token" for your new application (referenced as TOKEN later on)
4. From the Dashboard at https://pushover.net note your "User key" (referenced as USERKEY later on)
5. Install the pushover app on your iPhone/Android and login
6. put "pushover.py" to ~/.weechat/python
7. start the plugin with "/python load pushover.py"
8. Set user key and token by doing
9. /set plugins.var.python.pushover.user USERKEY
10. /set plugins.var.python.pushover.token TOKEN 

## Todo

1. Get rid of curl dependency and use python itself to do the http call (non-blocking).
2. Make it configurable to notify about current window or not.
3. Make it configurable to notify only while being in away mode.
4. Make it configurable to send more details (e.g. local timestamp).

## Security

Due to the architecture used, this plugin does not use end-to-end-encryption. It mostly relies on SSL traffic encryption. Check official pushover FAQ for reference: https://pushover.net/faq#security-encryption

## License

The script is derived from other scripts (see pushover.py for history). It is released under the GPL v2. See LICENSE file for details.

## Author

Author: Caspar Clemens Mierau <ccm@screenage.de>

