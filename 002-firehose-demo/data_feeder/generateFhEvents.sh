#!/bin/bash

#Usage: 
function usage()
{
    echo -e "Usage: $0 <firehose_delivery stream name>"
}

if [ "$#" -ne 1 ]; then
    usage
    exit 1
fi

DS_NAME=$1

payload='{"Data":"{\"First_Name\":\"Quick Brown Fox\",\"Last_Name\":\"Name Me\"}\n"}'

echo "Writing $payload to firehose"
aws firehose put-record --delivery-stream-name $DS_NAME --record="$payload"
