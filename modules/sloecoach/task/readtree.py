
from collections import defaultdict
import logging
import os
import time

import sloecoach.selector

LOGGER = logging.getLogger("module.sloecoach.task.readtree")
LOGGER.setLevel(logging.DEBUG)

def readtree(db, cache, spec):

    LOGGER.info("Beginning read of tree %s", spec.name)
    start_time = time.clock()
    import sloecoach.db.file

    fs_tree_root = spec.metadata_root_path
    selector = spec.selector or sloecoach.selector.Selector(metafile_filter=spec.selector)
    update_context = defaultdict(dict)

    for dirpath, dirnames, filenames in os.walk(fs_tree_root):

        # Apply selector to current directory
        dir_subpath = os.path.relpath(dirpath, fs_tree_root).replace("\\", "/")
        if selector.is_dir_path_selected(dir_subpath):
            for filename in filenames:
                # Apply selector to current file
                if selector.is_basename_selected(filename):
                    sloecoach.db.file.update_from_file(db, cache, update_context, fs_tree_root, dir_subpath, filename)

    LOGGER.info("Completed read of tree %s in %.2f seconds", spec.name, time.clock() - start_time)

