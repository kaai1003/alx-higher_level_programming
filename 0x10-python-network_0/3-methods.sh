#!/bin/bash
#display all methods accpeted by server URL
curl -X OPTIONS "$1" | grep 'Allow:'
