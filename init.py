# @auther 宋疆疆 
# @since 2017/12/11.

import Util
import subprocess
import shutil
import sys
import os

PATH = os.getcwd() + '/.githelper/manifest'


def main(manifestUri, branch):
    # shutil.copytree(sys.path[0], '.githelper/python')

    if os.path.exists(PATH):
        update()
        reset(branch)
    else:
        clone(manifestUri, branch)

    return 0


def clone(git, branch):
    Util.cprint('exec: git clone ' + git + ' .githelper/manifest -b ' + branch)
    obj = subprocess.Popen(['git', 'clone', git, '.githelper/manifest', '-b', branch], stdout=subprocess.PIPE)
    obj.wait()
    ret = obj.returncode
    if ret != 0:
        msg = 'Fail: ' + str(ret) + ', ' + 'manifest clone, ' + git
        raise Exception(msg)

    Util.cprint('Success manifest clone , ' + git)
    return ret


def update():
    Util.cprint('path: ' + PATH)
    Util.cprint('exec: git remote update')
    obj = subprocess.Popen(['git', 'remote', 'update'], stdout=subprocess.PIPE, cwd=PATH)
    obj.wait()
    ret = obj.returncode
    if ret != 0:
        msg = 'Fail: ' + str(ret) + ', ' + 'manifest update'
        raise Exception(msg)

    Util.cprint('Success manifest update')
    return ret


def reset(branch):
    Util.cprint('path: ' + PATH)
    Util.cprint('exec: git checkout origin/' + branch + ' -B ' + branch)
    obj = subprocess.Popen(['git', 'checkout', 'origin/' + branch, '-B', branch], stdout=subprocess.PIPE, cwd=PATH)
    obj.wait()
    ret = obj.returncode
    if ret != 0:
        msg = 'Fail: ' + str(ret) + ', ' + 'manifest checkout -B ' + branch
        raise Exception(msg)

    Util.cprint('Success manifest checkout -B ' + branch)
    return ret
