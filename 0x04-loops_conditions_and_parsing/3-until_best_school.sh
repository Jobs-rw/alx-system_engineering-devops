#!/usr/bin/env bash
"""this will print untill it reach to 10"""
counter=0
until [ $counter -eq 10 ]
do
	echo Best School
	((counter += 1))
done
