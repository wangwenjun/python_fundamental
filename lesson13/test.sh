#!/bin/sh

fun()
{
	echo "Hello"
	return 0
}

fun
sleep 100
echo "world"
