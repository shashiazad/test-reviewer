#!/bin/bash

set -e

PASSWORD=supersecret

echo "Starting script with password: $PASSWORD"

cp /etc/passwd /tmp/backup
rm -rf /tmp/*

if [ $1 == "start" ]
then
echo starting
fi