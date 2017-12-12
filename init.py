# @auther 宋疆疆 
# @since 2017/12/11.

import Util
import subprocess
import shutil
import sys
import os

PATH = os.getcwd() + '/.githelper/manifest'

def main(manifestUri):
    # shutil.copytree(sys.path[0], '.githelper/python')

    if os.path.exists(PATH):
        ret = update()
        if ret != 0:
            raise Exception('manifest update ' + manifestUri + ' fail: ' + str(ret))

        Util.cprint('manifest update ' + manifestUri + ' success')

        ret = reset()
        if ret != 0:
            raise Exception('manifest reset ' + manifestUri + ' fail: ' + str(ret))

        Util.cprint('manifest reset ' + manifestUri + ' success')
        
    else:
        ret = clone(manifestUri)
        if ret != 0:
            raise Exception('manifest clone ' + manifestUri + ' fail: ' + str(ret))
    
        Util.cprint('manifest clone ' + manifestUri + ' success')

    return 0


def clone(git):
    obj = subprocess.Popen(['git', 'clone', git, '.githelper/manifest'], stdout=subprocess.PIPE)
    obj.wait()
    ret = obj.returncode
    return ret


def update():
    obj = subprocess.Popen(['git', 'remote', 'update'], stdout=subprocess.PIPE, cwd=PATH)
    obj.wait()
    ret = obj.returncode
    return ret


def reset():
    obj = subprocess.Popen(['git', 'reset', '--hard', 'origin/master'], stdout=subprocess.PIPE, cwd=PATH)
    obj.wait()
    ret = obj.returncode
    return ret
