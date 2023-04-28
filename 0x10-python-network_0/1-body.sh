#!/bin/bash
# Takes in a URL, sends request, displays only body of 200 status code response
curl -s "$1" -X GET -L 
