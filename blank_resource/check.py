#!/usr/bin/env python


import os, sys
import json
from . import common


def check_(stdin):
    config, source_config = common.parse_input(stdin)
    if config.get('version'):
        return []
    else:
        return [{"ref": "fake"}]

def main():
    version = check_(sys.stdin)
    print(json.dumps({'version': {'version': version}}))
