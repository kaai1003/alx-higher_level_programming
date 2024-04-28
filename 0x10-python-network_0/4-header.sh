#!/bin/bash
#send GET request to URL and display body with header variable
curl -s -H "X-School-User-Id: 98" "$1"
