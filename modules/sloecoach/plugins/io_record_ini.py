
import sloecoach.iplugin

import ConfigParser
import logging

LOGGER = logging.getLogger("module.sloecoach.plugins.io_record_ini")
LOGGER.setLevel(logging.DEBUG)

class IoRecordIni(sloecoach.iplugin.IPlugin):
    METADATA = dict(
        format_names=["INI file"],
        read_extensions=[".ini"],
        write_extensions=[".ini"]
    )
    TYPE="io_record"

    @staticmethod
    def io_record_read_fp(ini_fp):
        parser = ConfigParser.RawConfigParser()
        parser.readfp(ini_fp)
        ini_data = {}
        for section in parser.sections():
            ini_data[section] = {}
            for item_name, value in parser.items(section):
                if value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                ini_data[section][item_name] = value

        return ini_data

    @classmethod
    def io_record_read_file(cls, filepath):
        with open(filepath) as fp:
            ini_data = cls.io_record_read_fp(fp)

        return ini_data
