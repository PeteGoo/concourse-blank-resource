#!/usr/bin/env python


import sys
import json
from . import common


def in_(dest_dir, stdin):
    input_args = json.load(stdin)
    config = common.get_source_config(input_args)
    return "dunno"

def main():
    destdir = sys.argv[1]
    common.msg('Output directory: {}'.format(destdir))
    version = in_(destdir, sys.stdin)
    print(json.dumps({'version': {'version': version}}))
