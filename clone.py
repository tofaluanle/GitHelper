# @auther 宋疆疆 
# @since 2017/12/11.

import json
from GitBean import GitBean
import Util
import subprocess


def main(file_path):
    with open(file_path, "r") as f:
        gits = json.load(f, object_hook=GitBean.parse)

    for git in gits:
        ret = clone(git)
        if ret != 0:
            Util.cprint(git.name + ' clone ' + git.uri + ' fail: ' + str(ret))
            return ret

        Util.cprint(git.name + ' clone ' + git.uri + ' success')

    return 0


def clone(git):
    obj = subprocess.Popen(['git', 'clone', git.uri, git.path, '-b', git.branch], stdout=subprocess.PIPE)
    obj.wait()
    ret = obj.returncode
    return ret

