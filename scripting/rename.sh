#!/bin/bash
count=0
FILES="Lignes/*"
for f in $FILES
do
    while read l; 
    do
        if [[ ${#l} -ge 3  ]]
        then
            if [[ count -le 9 ]]
            then
                new=$(echo M0$count.txt)
                echo 0$count$l >> $new
            else 
                new=$(echo M$count.txt)
                echo $count$l >> $new 
            fi
        fi
    done <"$f"
    count=$(($count+1))
done

