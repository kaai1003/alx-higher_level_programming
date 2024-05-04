#!/bin/bash
#display all methods accpeted by server URL
curl -i "$1" | grep 'Allow:'
