# @auther 宋疆疆 
# @since 2017/12/11.

import sys
import os
import sync
import init

subModule = sys.argv[1]
if subModule == 'sync':
    if len(sys.argv) <= 2:
        sync.main(os.getcwd() + '/.githelper/manifest/manifest.json')
    else:
        sync.main(sys.argv[2])
elif subModule == 'init':
    if len(sys.argv) > 2:
        init.main(sys.argv[2], 'develop')
    else:
        init.main(sys.argv[2], sys.argv[3])
