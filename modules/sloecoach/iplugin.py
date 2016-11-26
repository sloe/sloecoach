
import logging

import yapsy.IPlugin

LOGGER = logging.getLogger(__file__)
LOGGER.setLevel(logging.DEBUG)

class IPlugin(yapsy.IPlugin.IPlugin):
    MERIT = 1.0
