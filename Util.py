# @auther 宋疆疆 
# @since 2017/9/12.

import sys
import subprocess
import os


def cprint(msg):
    print("[ GH ] " + msg)
    sys.stdout.flush()


def execCmd(args, path=None):
    if path:
        cprint('Path: ' + path)
    else:
        cprint('Path: ' + os.getcwd())
    cprint('Exec: ' + ' '.join(args))

    if path:
        obj = subprocess.Popen(args, cwd=path)
    else:
        obj = subprocess.Popen(args)

    obj.wait()
    ret = obj.returncode
    if ret != 0:
        msg = 'Fail: ' + str(ret)
        raise Exception(msg)

    cprint('Success ')
