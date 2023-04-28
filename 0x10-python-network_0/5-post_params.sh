#!/bin/bash
# Takes a URL as an argument, sends POST request, displays response body
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
