# @auther 宋疆疆
# @since 2017/12/22.

import Config
import json
from GitBean import GitBean
import Util
import os
import sys


def main():
    args = sys.argv[1:]
    args.remove('forall')

    if '-c' not in args:
        raise Exception("wrong command, example: -c git --version")

    args.remove('-c')

    with open(Config.MAINFEST_PATH, "r") as f:
        gits = json.load(f, object_hook=GitBean.parse)

    for git in gits:
        Util.execCmd(args, os.getcwd() + git.path)
