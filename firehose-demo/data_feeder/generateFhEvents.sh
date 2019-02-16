#!/bin/bash

#Usage: 
function usage()
{
    echo -e "Usage: $0 <firehose_delivery stream name>"
}

DS_NAME=$1

payload='{"Data":"{\"First_Name\":\"Quick Brown Fox\",\"Last_Name\":\"Name Me\"}"}'

echo "Writing $payload to firehose"
aws firehose put-record --delivery-stream-name $DS_NAME --record="$payload"
