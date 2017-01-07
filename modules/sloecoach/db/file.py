
import logging
import os

import sloecoach.plugins

LOGGER = logging.getLogger("module.sloecoach.db.file")
LOGGER.setLevel(logging.DEBUG)


def update_from_file(db, dir_path, dir_subpath, filename):

    file_ext = os.path.splitext(filename)[1].lower()

    def __io_selector(plugin):
        return file_ext in plugin.metadata.read_extensions

    io_plugin_obj = sloecoach.plugins.PluginManager.instance.select_plugin_object("io_record", __io_selector, "loader for file extension %s" % file_ext)
    fingerprint = io_plugin_obj.io_record_read_file_fingerprint(dir_path, dir_subpath, filename)
    record = io_plugin_obj.io_record_read_file(dir_path, dir_subpath, filename)
    LOGGER.debug("Loaded %s/%s: %s", dir_subpath, filename, record)

    for obj_type_str, obj_data in record.iteritems():
        obj_type = obj_type_str.split("-")[0]

        def __db_selector(plugin):
            return obj_type in plugin.metadata.update_methods

        try:
            db_plugin = sloecoach.plugins.PluginManager.instance.select_plugin("db_record", __db_selector, "DB updater for object type %s" % obj_type)
        except sloecoach.plugins.PluginNotFound as e:
            LOGGER.warning("No plugin available to load object type %s", obj_type)
            continue

        update_method = db_plugin.metadata.update_methods[obj_type]

        obj_data.update(fingerprint)
        update_method(db_plugin.plugin_obj, db, obj_data, dir_subpath)
