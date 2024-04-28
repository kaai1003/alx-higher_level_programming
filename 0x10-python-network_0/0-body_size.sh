#!/bin/bash
#send request to URL and display size of body
curl -sI "$1" | grep -i "Content-Length" | cut -d " " -f 2
