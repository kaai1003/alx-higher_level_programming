#!/bin/bash
#display all methods accpeted by server URL
curl -i -X OPTIONS "$1" | grep 'Allow:' | cut -f2- 'd'
