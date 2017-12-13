# @auther 宋疆疆 
# @since 2017/12/11.

import json
from GitBean import GitBean
import Util
import subprocess
import os


def main(file_path):
    with open(file_path, "r") as f:
        gits = json.load(f, object_hook=GitBean.parse)

    for git in gits:
        if os.path.exists(os.getcwd() + git.path):
            ret = update(git)
            if ret != 0:
                msg = 'Fail: ' + str(ret) + ', ' + git.name + ' update, ' + git.uri
                raise Exception(msg)

            Util.cprint('Success ' + git.name + ' update ' + git.uri)

            ret = rebase(git)
            if ret != 0:
                msg = 'Fail: ' + str(ret) + ', ' + git.name + ' rebase, ' + git.uri
                raise Exception(msg)

            Util.cprint('Success ' + git.name + ' rebase ' + git.uri)
        else:
            ret = clone(git)
            if ret != 0:
                msg = 'Fail: ' + str(ret) + ', ' + git.name + ' clone, ' + git.uri
                raise Exception(msg)

            Util.cprint('Success ' + git.name + ' clone ' + git.uri)

    return 0


def clone(git):
    obj = subprocess.Popen(['git', 'clone', git.uri, os.getcwd() + git.path, '-b', git.branch], stdout=subprocess.PIPE)
    obj.wait()
    ret = obj.returncode
    return ret


def update(git):
    obj = subprocess.Popen(['git', 'remote', 'update'], stdout=subprocess.PIPE, cwd=os.getcwd() + git.path)
    obj.wait()
    ret = obj.returncode
    return ret


def rebase(git):
    obj = subprocess.Popen(['git', 'rebase', 'origin/' + git.branch], stdout=subprocess.PIPE, cwd=os.getcwd() + git.path)
    obj.wait()
    ret = obj.returncode
    return ret
