
from collections import defaultdict
import logging
import os
import time

import sloecoach.selector

LOGGER = logging.getLogger("module.sloecoach.task.writetree")
LOGGER.setLevel(logging.DEBUG)

def writetree(db, cache, spec):

    LOGGER.info("Beginning write of tree %s", spec.name)
    start_time = time.clock()

    LOGGER.error("Not implemented")

    LOGGER.info("Completed write of tree %s in %.2f seconds", spec.name, time.clock() - start_time)

