#!/bin/bash
#Bash script that sends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -s -X POST -d "@$2" -H "Content-type: application/json" "$1"
