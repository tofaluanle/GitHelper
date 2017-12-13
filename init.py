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
        ret = update()
        if ret != 0:
            msg = 'Fail: ' + str(ret) + ', ' + 'manifest update, ' + manifestUri
            raise Exception(msg)

        Util.cprint('Success manifest update ' + manifestUri)

        ret = reset(branch)
        if ret != 0:
            msg = 'Fail: ' + str(ret) + ', ' + 'manifest reset, ' + manifestUri
            raise Exception(msg)

        Util.cprint('Success manifest reset ' + manifestUri)

    else:
        ret = clone(manifestUri, branch)
        if ret != 0:
            msg = 'Fail: ' + str(ret) + ', ' + 'manifest clone, ' + manifestUri
            raise Exception(msg)

        Util.cprint('Success manifest clone , ' + manifestUri)

    return 0


def clone(git, branch):
    obj = subprocess.Popen(['git', 'clone', git, '.githelper/manifest', '-b', branch], stdout=subprocess.PIPE)
    obj.wait()
    ret = obj.returncode
    return ret


def update():
    obj = subprocess.Popen(['git', 'remote', 'update'], stdout=subprocess.PIPE, cwd=PATH)
    obj.wait()
    ret = obj.returncode
    return ret


def reset(branch):
    obj = subprocess.Popen(['git', 'reset', '--hard', 'origin/' + branch], stdout=subprocess.PIPE, cwd=PATH)
    obj.wait()
    ret = obj.returncode
    return ret
