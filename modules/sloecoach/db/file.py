
import logging
import os

import sloecoach.inireader

LOGGER = logging.getLogger(__file__)
LOGGER.setLevel(logging.DEBUG)


def update_from_file(dir_path, dir_subpath, filename):
    LOGGER.info("Updating from file %s|%s|%s", dir_path, dir_subpath, filename)

    full_path = os.path.normpath(os.path.join(dir_path, dir_subpath, filename))

    file_ext = os.path.splitext(filename)[1].lower()

    if file_ext == ".ini":
        ini_data = sloecoach.inireader.read_ini_file(full_path)
    else:
        LOGGER.warning("Ignoring file with unknown extension %s", file_ext)
    pass