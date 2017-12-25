# @auther 宋疆疆 
# @since 2017/12/11.

import sys
import sync
import init
import forall
import Util

subModule = sys.argv[1]
if subModule == 'init':
    init.main()
elif subModule == 'sync':
    sync.main()
elif subModule == 'forall':
    forall.main()
else:
    Util.cprint("just support command [init, sync, forall]")
