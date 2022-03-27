#!/bin/sh

dir_path="C:/programming/atcoder/contest/ABC/*"
dirs=`find $dir_path  -maxdepth 0 -type d`

for dir in $dirs;
do
    echo $dir
    name=`basename $dir`
    # echo $name
    if [[ ${name} =~ ABC([0-9]+) ]]; then
        echo $name
        echo ${BASH_REMATCH[1]}
        mv $name ${BASH_REMATCH[1]}
    fi
done

#ABC186
#ABC