#!/bin/bash
# Script sends a JSON POST request to a URL first argument, displays the body of response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
