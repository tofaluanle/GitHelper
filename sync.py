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
            update(git)
            merge(git)
        else:
            clone(git)

    return 0


def clone(git):
    Util.cprint('exec: git clone' + git.uri + ' ' + os.getcwd() + git.path + ' -b ' + git.branch)
    obj = subprocess.Popen(['git', 'clone', git.uri, os.getcwd() + git.path, '-b', git.branch], stdout=subprocess.PIPE)
    obj.wait()
    ret = obj.returncode
    if ret != 0:
        msg = 'Fail: ' + str(ret) + ', ' + git.name + ' clone, ' + git.uri
        raise Exception(msg)

    Util.cprint('Success ' + git.name + ' clone ' + git.uri)
    return ret


def update(git):
    Util.cprint('path: ' + os.getcwd() + git.path)
    Util.cprint('exec: git remote update')
    obj = subprocess.Popen(['git', 'remote', 'update'], stdout=subprocess.PIPE, cwd=os.getcwd() + git.path)
    obj.wait()
    ret = obj.returncode
    if ret != 0:
        msg = 'Fail: ' + str(ret) + ', ' + git.name + ' update, ' + git.uri
        raise Exception(msg)

    Util.cprint('Success ' + git.name + ' update ' + git.uri)
    return ret


def merge(git):
    Util.cprint('path: ' + os.getcwd() + git.path)
    Util.cprint('exec: git merge origin/' + git.branch)
    obj = subprocess.Popen(['git', 'merge', 'origin/' + git.branch], stdout=subprocess.PIPE, cwd=os.getcwd() + git.path)
    obj.wait()
    ret = obj.returncode
    if ret != 0:
        msg = 'Fail: ' + str(ret) + ', ' + git.name + ' merge, ' + git.uri
        raise Exception(msg)

    Util.cprint('Success ' + git.name + ' merge ' + git.uri)
    return ret
