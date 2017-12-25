# @auther 宋疆疆
# @since 2017/12/22.

from optparse import OptionParser
import Config
import json
from GitBean import GitBean
import Util
import subprocess
import os


def main():
    parser = OptionParser()

    parser.add_option(
        "-c",
        action="store_true",
        help="ex: -c git branch",
    )

    (options, args) = parser.parse_args()

    print(args)
    print(options)
    args.remove('forall')
    print(args)
    # for arg in args:
    #     print(arg.split(" "))


    if options.c:
        Util.cprint('exec: ' + ' '.join(args))

    with open(Config.MAINFEST_PATH, "r") as f:
        gits = json.load(f, object_hook=GitBean.parse)

    for git in gits:
        execCmd(git, args)


def execCmd(git, args):
    Util.cprint('path: ' + os.getcwd() + git.path)
    obj = subprocess.run(args, stdout=subprocess.PIPE, cwd=os.getcwd() + git.path)
    while obj.poll() is None:
        line = obj.stdout.readline()
        line = line.strip()
        if line:
            print(line)
    ret = obj.returncode
    if ret != 0:
        msg = 'Fail: ' + str(ret)
        raise Exception(msg)

    Util.cprint('Success ')
