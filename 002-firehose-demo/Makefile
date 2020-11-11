
# Usage:
# make kinesis-firehose DEPLOY_BUCKET=<S3 bucket where lambda code is deployed by CloudFormation>
#						FH_STACK_NAME=<Name of Cloud Formation stack to deploy in>
#						FRIENDLY_FH_NAME=<Friendly name to give the firehose delivery stream>
kinesis-firehose:
	aws cloudformation package --template-file deploy-firehose.yml \
		--s3-bucket $(DEPLOY_BUCKET) \
		--output-template-file packaged-template.yml 

	aws cloudformation deploy \
		--template-file  packaged-template.yml \
		--stack-name $(FH_STACK_NAME) \
		--parameter-overrides FirehoseDeliveryStreamName=$(FRIENDLY_FH_NAME) \
		--capabilities CAPABILITY_NAMED_IAM