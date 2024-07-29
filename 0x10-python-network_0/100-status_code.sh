#!/bin/bash
# Sends a GET request to a given URL and display the response status code.
curl -sLw "%{http_code}" -o /dev/null "$1"
