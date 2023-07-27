#!/usr/bin/env bash
"""this will print 11 times 10 for Best School and 1 for Hi"""
counter=1

while [ $counter -le 10 ]
do
  if [ $counter -eq 9 ]
  then
    echo "Best School"
    echo "Hi"
  else
    echo "Best School"
  fi

  ((counter++))
done
