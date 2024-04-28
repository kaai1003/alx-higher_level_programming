#!/bin/bash
#send POST request to URL and pass some variable
curl -s -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" -X POST "$1"
