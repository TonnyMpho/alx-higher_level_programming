#!/bin/bash
#Bash script that makes a request to 0.0.0.0:5000/catch_me
curl -s -X PUT -L --header "Origin: School" -d "user_id=98" "0.0.0.0:5000/catch_me"
