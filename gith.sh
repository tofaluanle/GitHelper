#!/usr/bin/env bash

rootDir=$(cd `dirname $0`; pwd)

python3 $rootDir/main.py $@

#case $1 in
#init)
#    python3 $rootDir/init.py $2
#    ;;
#sync)
#    if [ ! -n "$2" ] ;then
#        python3 $rootDir/sync.py pwd/.githelper/manifest/manifest.json
#    else
#        python3 $rootDir/sync.py $2
#    fi
#    ;;
#*)
#    echo wrong command
#    ;;
#esac
