#!/bin/bash
rm -f 

filename='.env'
if [ -f “$filename” ]; then
rm .env
echo "Existing $filename is removed"

echo "ULOBA_USERNAME=$ULOBA_USERNAME" > .env
echo "ULOBA_PASSWORD=$Uloba986" > .env
echo "new $filename is created and populated"