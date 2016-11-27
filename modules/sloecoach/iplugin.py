
import logging

import yapsy.IPlugin

LOGGER = logging.getLogger("module.sloecoach.iplugin")
LOGGER.setLevel(logging.DEBUG)

class IPlugin(yapsy.IPlugin.IPlugin):
    MERIT = 1.0
