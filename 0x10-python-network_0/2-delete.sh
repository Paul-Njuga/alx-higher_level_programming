#!/bin/bash
# Sends DELETE request URL passed as 1st argument & displays response body
curl -s "$1" -X DELETE
