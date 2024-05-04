#!/bin/bash
#display all methods accpeted by server URL
curl -i --no-progress-meter "$1" | grep 'Allow:' | cut -d ":" -f 2 | cut -c 2-
