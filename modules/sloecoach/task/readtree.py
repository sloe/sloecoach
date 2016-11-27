
import logging
import os

import sloecoach.selector

LOGGER = logging.getLogger("module.sloecoach.task.readtree")
LOGGER.setLevel(logging.DEBUG)

def readtree(db, spec):
    import sloecoach.db.file

    fs_tree_root = os.path.normpath(spec.metadata_root_path)
    selector = spec.selector or sloecoach.selector.Selector(metafile_filter=spec.selector)

    for dirpath, dirnames, filenames in os.walk(fs_tree_root):

        # Apply selector to current directory
        dir_path = os.path.join(fs_tree_root, dirpath)
        dir_subpath = os.path.relpath(dirpath, fs_tree_root)
        if selector.is_dir_path_selected(dir_subpath):
            for filename in filenames:
                # Apply selector to current file
                if selector.is_basename_selected(filename):
                    sloecoach.db.file.update_from_file(fs_tree_root, dir_subpath, filename)

