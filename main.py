# @auther 宋疆疆 
# @since 2017/12/11.

import sys
import os
import clone
import init

subModule = sys.argv[1]
if subModule == 'clone':
    if len(sys.argv) <= 2:
        clone.main(os.getcwd() + '/.githelper/manifest/manifest.json')
    else:
        clone.main(sys.argv[2])
elif subModule == 'init':
    init.main(sys.argv[2])
