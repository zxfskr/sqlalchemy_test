#!/bin/bash

#mysql check
# set -e

timeout 1 bash -c 'cat < /dev/null > /dev/tcp/db/3306'

while [ $? -ne 0 ] ;
do 
    echo "mysql not ready";
    sleep 15s ;
    timeout 1 bash -c 'cat < /dev/null > /dev/tcp/db/3306'
done

echo "mysql start";
