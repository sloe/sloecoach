
import logging

import sloecoach.plugins

LOGGER = logging.getLogger("module.sloecoach.db.ensure_basis")
LOGGER.setLevel(logging.DEBUG)

def ensure_basis(db):

   def __selector(plugin):
      return hasattr(plugin.plugin_obj, "ensure_basis")

   ensure_plugins = sloecoach.plugins.PluginManager.instance.select_multiple_plugins("*", __selector)

   for ensure_plugin in ensure_plugins:
      ensure_plugin.plugin_obj.ensure_basis(db)
