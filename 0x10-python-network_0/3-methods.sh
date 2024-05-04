#!/bin/bash
#display all methods accpeted by server URL
curl -i OPTIONS "$1" | grep 'Allow:'
