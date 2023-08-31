#!/bin/bash
# Takes in a URL, sends header request, displays response body size
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
