#!/bin/bash
# ends a JSON POST request to a URL passed as the first argument, and displays the body of the response.
curl -sL -X PUT 0.0.0.0:5000/catch_me -d "user_id=98" -H "Origin: HolbertonSchool"
