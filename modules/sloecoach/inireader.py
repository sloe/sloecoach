
import ConfigParser
import logging

LOGGER = logging.getLogger(__file__)


def read_ini_fp(ini_fp):
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


def read_ini_file(filepath):

    with open(filepath) as fp:
        ini_data = read_ini_fp(fp)

    return ini_data

