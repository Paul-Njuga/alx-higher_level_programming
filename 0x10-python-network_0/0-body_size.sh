#!/bin/bash
# Takes in a URL, sends request, displays response body size
if [ "$1" ]; then
	curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
fi
