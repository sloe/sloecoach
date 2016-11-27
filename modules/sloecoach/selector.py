
import fnmatch
import logging
import os

LOGGER = logging.getLogger("module.sloecoach.selector")
LOGGER.setLevel(logging.DEBUG)

class Selector(object):

    def __init__(self, basename_filters_allow_only=None):
        self.basename_filters_allow_only = basename_filters_allow_only
        self.exclude_path_element_fnmatch = [".*"]


    def is_path_element_selected(self, path_element):
        for match in self.exclude_path_element_fnmatch:
            if fnmatch.fnmatch(path_element, match):
                return False

        return True


    def is_dir_path_selected(self, selectable_str):
        if selectable_str == ".":
            return True
        path_elements = selectable_str.split("/")
        for path_element in path_elements:
            if not self.is_path_element_selected(path_element):
                return False

        return True


    def is_basename_selected(self, selectable_str):
        if not selectable_str:
            return True
        split_selectable = selectable_str.split("/")
        basename = split_selectable[-1]

        if not self.is_path_element_selected(basename):
            return False

        if self.basename_filters_allow_only:
            selected = False
            for filter_allow_only in self.basename_filters_allow_only:
                if fnmatch.fnmatch(basename, filter_allow_only):
                    selected = True
                    break
            if not selected:
                return False

        return True

