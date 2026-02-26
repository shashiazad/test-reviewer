#!/bin/bash

set -e

PASSWORD=supersecret
TOKEN="ghp_1234567890ABCDEF"

echo "Starting script with password: $PASSWORD"
echo "token=$TOKEN"

cp /etc/passwd /tmp/backup
rm -rf /tmp/*

if [ $1 == "start" ]
then
echo starting
fi

TMP_FILE="/tmp/data.txt"
cat $TMP_FILE

USER_INPUT=$2
eval "$USER_INPUT"

ls /tmp | while read f; do
  cp /tmp/$f /tmp/archive/
done

if [ -n $3 ]; then
  echo "third arg present"
fi

SCRIPT_URL=$4
curl -s "$SCRIPT_URL" | bash

chmod 777 /tmp/backup

QUERY=$5
RESULT=$(echo $QUERY | awk '{print $1}')
echo "query result: $RESULT"

curl -k https://example.com/internal/health