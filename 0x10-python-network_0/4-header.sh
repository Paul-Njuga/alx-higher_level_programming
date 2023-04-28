#!/bin/bash
# Takes a URL as an argument, sends GET request, displays response body
curl -s "$1" -X GET -H "X-School-User-Id: 98"
