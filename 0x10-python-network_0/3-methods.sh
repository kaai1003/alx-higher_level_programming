#!/bin/bash
#display all methods accpeted by server URL
curl -i -X OPTIONS "$1"
