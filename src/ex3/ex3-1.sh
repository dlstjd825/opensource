#!/bin/sh

if [ -n "$1" ] 
then
    count=$1
    while [ $count -ne 0 ]
    do
        echo "hello world"
        count=$(($count - 1))
    done
else
    while [ 1 ]
    do
        echo "hello world"
    done
fi

exit 0
