#!/bin/bash
min=40000
while ((1))
do
    var1="$(echo | python3 ../src/main.py)" && var2=$(echo "$var1" | tail -n 1)
    if [ $(($var2 - $min)) -le $((0)) ] 
    then
        min=$var2
        echo "$var1" >> history.txt
        echo "$var1"
    fi
done
