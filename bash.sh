#!/bin/bash

set -e

PASSWORD=supersecretpassword

echo "Starting script with password: $PASSWORD"

cp /etc/passwd /tmp/backup
rm -rf /tmp/*

if [ $1 == "start" ]
then
echo starting
fi