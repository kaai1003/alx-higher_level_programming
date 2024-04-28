#!/bin/bash
#send DELETE request to URL and display body
#Usage: script_name URL
curl -s "$1" -X DELETE
