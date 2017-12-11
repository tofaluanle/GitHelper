# @auther 宋疆疆 
# @since 2017/12/11.

import Util
import subprocess
import shutil
import sys


def main(manifestUri):
    shutil.copytree(sys.path[0], '.githelper/python')

    ret = clone(manifestUri)
    if ret != 0:
        Util.cprint('manifest clone ' + manifestUri + ' fail: ' + str(ret))
        return ret

    Util.cprint('manifest clone ' + manifestUri + ' success')

    return 0


def clone(git):
    obj = subprocess.Popen(['git', 'clone', git, '.githelper/manifest'], stdout=subprocess.PIPE)
    obj.wait()
    ret = obj.returncode
    return ret
