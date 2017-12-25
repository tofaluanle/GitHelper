# @auther 宋疆疆 
# @since 2017/12/11.

import sys
import os
import sync
import init
import forall
import Util
import Config

print(sys.argv[1:])

subModule = sys.argv[1]
if subModule == 'sync':
    if len(sys.argv) <= 2:
        sync.main(Config.MAINFEST_PATH)
    else:
        sync.main(sys.argv[2])
elif subModule == 'init':
    if len(sys.argv) < 3:
        init.main('', 'develop')
    elif len(sys.argv) == 3:
        init.main(sys.argv[2], 'develop')
    else:
        init.main(sys.argv[2], sys.argv[3])
elif subModule == 'forall':
    forall.main()
else:
    Util.cprint("just support command [init, sync, forall]")
