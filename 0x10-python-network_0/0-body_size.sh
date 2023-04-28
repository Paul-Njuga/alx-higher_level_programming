#!/bin/bash
# Takes in a URL, sends request, displays response body size
curl -sI "$1" | awk '/Content-Legnth/ { print $2 }'
