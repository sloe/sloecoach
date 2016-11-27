
import logging
import os

import sloecoach.plugins

LOGGER = logging.getLogger("module.sloecoach.db.file")
LOGGER.setLevel(logging.DEBUG)


def update_from_file(dir_path, dir_subpath, filename):
    full_path = os.path.normpath(os.path.join(dir_path, dir_subpath, filename))

    file_ext = os.path.splitext(filename)[1].lower()

    def __selector(plugin):
        return file_ext in plugin.metadata.read_extensions

    io_plugin = sloecoach.plugins.PluginManager.instance.select_plugin_object("io_record", __selector, "loader for file extension %s" % file_ext)
    record = io_plugin.io_record_read_file(full_path)
    LOGGER.debug("Loaded %s/%s: %s", dir_subpath, filename, record)
