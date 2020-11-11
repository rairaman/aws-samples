#!/bin/bash

golden_ami_name=$1

if [ -z $golden_ami_name ]; then
    echo "AMI Name must be provided as first argument"
    echo "Usage: store_golden_ami_id <AMI Name>"
    exit 1
fi

echo "Retrieving AMI Id for $golden_ami_name"
golden_ami_id=`aws ec2 describe-images --filters "Name=name,Values=$golden_ami_name" --query "Images[0].ImageId" --output text`

aws ssm put-parameter --name '/ami/golden/base/latest' \
    --description 'ID of the AMI used as a base for other applications' \
    --type 'String' \
    --value "$golden_ami_id" \
    --overwrite
