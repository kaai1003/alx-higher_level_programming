#!/bin/bash
#send GET request to URL and display body with header variable
#Usage: script_name URL
curl -s -H "X-School-User-Id: 98" "$1"
