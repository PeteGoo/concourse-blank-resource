#!/usr/bin/env python


import os, sys
import json
from . import common

check_url = os.environ["CHECK_URL"]


def check_(stdin):
    config, source_config = common.parse_input(stdin)
    slack_trigger = slack.SlackTrigger(source_config)
    return slack_trigger.check_for_messages(config)

def main():
    version = check_(sys.stdin)
    print(json.dumps({'version': {'version': version}}))
