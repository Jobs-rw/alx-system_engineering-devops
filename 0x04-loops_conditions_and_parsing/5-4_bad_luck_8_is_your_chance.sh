#!/usr/bin/env bash
"""this will print 10 times on 4th and 8th will bad luck and good luck"""

i=1

while [ $i -le 10 ]
do
    if [ $i -eq 4 ]; then
        echo "bad luck"
    elif [ $i -eq 8 ]; then
        echo "good luck"
    else
        echo "Best School"
    fi

    ((i += 1))
done
