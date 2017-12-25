# @auther 宋疆疆 
# @since 2017/12/11.

import json
from GitBean import GitBean
import Util
import os
import Config
import sys


def main():
    if len(sys.argv) <= 2:
        file_path = Config.MAINFEST_PATH
    else:
        file_path = sys.argv[2]

    with open(file_path, "r") as f:
        gits = json.load(f, object_hook=GitBean.parse)

    for git in gits:
        if os.path.exists(os.getcwd() + git.path):
            Util.execCmd(['git', 'remote', 'update'], os.getcwd() + git.path)
            Util.execCmd(['git', 'merge', 'origin/' + git.branch], os.getcwd() + git.path)
        else:
            Util.execCmd(['git', 'clone', git.uri, os.getcwd() + git.path, '-b', git.branch])

    return 0
