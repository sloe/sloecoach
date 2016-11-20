
import logging
import os

LOGGER = logging.getLogger(__file__)

def readtree(db, spec):
    fs_tree_root = os.path.normpath(spec.stack_row.f_infopath)
    selector = spec.selector

    for dirpath, dirnames, filenames in os.walk(fs_tree_root):

        # Apply selector to current directory
        dir_path = os.path.join(fs_tree_root, dirpath)
        dir_subpath = os.path.relpath(fs_tree_root, dirpath)
        if not selector or selector.select_on_dir_subpath(dir_subpath):
            for filename in filenames:
                # Apply selector to current file
                file_path = os.path.join(fs_tree_root, dirpath, filename)
                if not selector or selector_select_on_file_subpath(file_subpath):
                    pass
