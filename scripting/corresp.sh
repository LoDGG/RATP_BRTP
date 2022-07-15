#!/bin/bash
count=0
nl='
'
while read l; 
do
    if [[ `echo ${l} | cut -c1` = '"' ]]
    then
        NAME=$(echo $l)
    elif [[  $l != *$'\n'* ]]
    then
            echo $l,$NAME\)
    fi

done <"../corresp.txt"


