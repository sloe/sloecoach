
import exceptions
import fnmatch
import itertools
import logging
import operator
import os

from gluon.storage import Storage
import yapsy.PluginManager

LOGGER = logging.getLogger("module.sloecoach.plugins")
LOGGER.setLevel(logging.DEBUG)


class PluginNotFound(exceptions.LookupError):
    pass


class PluginManager(object):
    instance = None
    plugin_manager = yapsy.PluginManager.PluginManager()

    def __init__(self):
        self.by_type = Storage()
        self.yapsy_manager = yapsy.PluginManager.PluginManager()


    def load_path(self, dir_path):
        self.yapsy_manager.setPluginPlaces([dir_path])
        self.yapsy_manager.collectPlugins()
        for plugin in self.yapsy_manager.getAllPlugins():
            record = Storage()
            record.plugin_type = plugin.plugin_object.TYPE
            if not record.plugin_type:
                LOGGER.warn("Plugin %s missing TYPE element, ignoring", plugin.name)
            record.merit = plugin.plugin_object.MERIT
            record.metadata = Storage(plugin.plugin_object.METADATA)
            record.plugin = plugin
            record.plugin_obj = plugin.plugin_object

            if record.plugin_type not in self.by_type:
                self.by_type[record.plugin_type] = []

            self.by_type[record.plugin_type].append(record)
        pass


    def select_multiple_plugins(self, plugin_type, selector_fn):
        selected = []
        plugins_for_type = []
        for key in sorted(self.by_type.keys()):
            if fnmatch.fnmatch(key, plugin_type):
                plugins_for_type += self.by_type[key]

        for plugin_for_type in plugins_for_type:
            if not selector_fn or selector_fn(plugin_for_type):
                selected.append(plugin_for_type)

        return selected


    def select_plugin(self, plugin_type, selector_fn, error_message):
        selected = self.select_multiple_plugins(plugin_type, selector_fn)
        if not selected:
            raise PluginNotFound("Plugin type %s not found: %s", plugin_type, error_message)

        sorted_selected = sorted(selected, key=operator.attrgetter("merit"), reverse=True)
        return sorted_selected[0]


    def select_plugin_object(self, plugin_type, selector_fn, error_message):
        plugin = self.select_plugin(plugin_type, selector_fn, error_message)
        return plugin.plugin_obj


    def load_standard_paths(self):
        local_dir = os.path.join(os.path.dirname(__file__))
        self.load_path(local_dir)


PluginManager.instance = PluginManager()
PluginManager.instance.load_standard_paths()
