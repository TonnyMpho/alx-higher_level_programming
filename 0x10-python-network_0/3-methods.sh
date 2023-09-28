#!/bin/bash
#Bash script that takes in a URL and displays all HTTP methods the server will accept.
curl -I -X OPTIONS -s "$1" | grep "Allow:" | sed 's/Allow: //'
