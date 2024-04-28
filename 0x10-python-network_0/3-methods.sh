#!/bin/bash
#display all methods accpeted by server URL
#Usage: script_name URL
curl -s -I -X OPTIONS "$1" | grep 'Allow:' | cut -f2- -d'
