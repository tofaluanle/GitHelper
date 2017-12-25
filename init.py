# @auther 宋疆疆 
# @since 2017/12/11.

import Util
import os
import sys
import Config


def main():
    if len(sys.argv) < 3:
        branch = 'develop'
    elif len(sys.argv) == 3:
        manifestUri=sys.argv[2]
        branch = 'develop'
    else:
        manifestUri = sys.argv[2]
        branch = sys.argv[3]

    if os.path.exists(Config.MAINFEST_DIR):
        Util.execCmd(['git', 'remote', 'update'], Config.MAINFEST_DIR)
        Util.execCmd(['git', 'checkout', 'origin/' + branch, '-B', branch], Config.MAINFEST_DIR)
    else:
        Util.execCmd(['git', 'clone', manifestUri, '.githelper/manifest', '-b', branch])

    return 0
