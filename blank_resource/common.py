import re
import sys, json


def msg(msg):
    print(msg, file=sys.stderr)


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def validate_config_param(parent: dict, name, error):
    if not parent.get(name):
        eprint(error)
        return False
    else:
        return True



class SourceConfig:
    def __init__(self, source_config: dict):
        if (
                not validate_config_param(source_config, 'param1',
                                          '"param1" was not supplied in the source configuration. This is the first param')
                or not validate_config_param(source_config, 'param2',
                                          '"param2" was not supplied in the source configuration. This is the first param')
                or not validate_config_param(source_config, 'param3',
                                          '"param3" was not supplied in the source configuration. This is the first param')

        ):
            raise Exception('Invalid Source Configuration')

        self.__param1 = source_config['param1']
        self.__param2 = source_config['param2']
        self.__param3 = source_config['param3']

    @property
    def param1(self):
        return self.__param1

    @property
    def channel(self):
        return self.__param2

    @property
    def deploy_name(self):
        return self.__param3


def parse_input(stdin=sys.stdin) -> (dict, SourceConfig):
    input_doc = json.load(stdin)

    source_config = input_doc['source']

    return input_doc, SourceConfig(source_config)
