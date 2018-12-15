# Usage:
# make update-firehose DEPLOY_BUCKET=<S3 bucket where lambda code is deployed by CloudFomration>
#						CUST_STACK_NAME=<Name of Cloud Formation stack to deploy in>
#						FH_ARN=<ARN of the Firehose delivery stream to update>
#						FH_DEL_STR_NAME=<Name of the firehose delivery stream>
#						GLUE_TABLE_NAME=<Name of the Glue table defining the input schema to convert>
#						GLUE_DB_NAME=<Name of the glue database where the target input schema resides>
#						GLUE_INT_ROLE=<The IAM role that firehose uses to query the glue schema>
update-firehose:
	aws cloudformation package --template-file deploy-custom-resource.yml \
		--s3-bucket $(DEPLOY_BUCKET) \
		--output-template-file packaged-template.yml 

	aws cloudformation deploy \
		--template-file  packaged-template.yml \
		--stack-name $(CUST_STACK_NAME) \
		--parameter-overrides FirehoseDeliveryArn=$(FH_ARN) \
								FireshoseDeliveryStreamName=$(FH_DEL_STR_NAME) \
								GlueTableName=$(GLUE_TABLE_NAME) \
								GlueDatabaseName=$(GLUE_DB_NAME) \
								GlueInteractionRole=$(GLUE_INT_ROLE) \
		--capabilities CAPABILITY_NAMED_IAM

# Usage:
# make glue-resources DEPLOY_BUCKET=<S3 bucket where lambda code is deployed by CloudFomration>
#						GLUE_STACK_NAME=<Name of Cloud Formation stack to deploy in>
#						FRIENDLY_FH_NAME=<Friendly name to give the firehose delivery stream>
#						GLUE_DB_NAME=<Name of the glue database where the target input schema will reside>
#						GLUE_TABLE_NAME=<Name of the Glue table defining the input schema to convert>
glue-resources:
	aws cloudformation deploy \
		--template-file deploy-glue-resources.yml \
		--stack-name $(GLUE_STACK_NAME) \
		--parameter-overrides FirehoseInputDbName=$(GLUE_DB_NAME) \
								FirehoseInputTableName=$(GLUE_TABLE_NAME) \
								FirehoseDeliveryArn=$(FIREHOSE_ARN) \
		--capabilities CAPABILITY_NAMED_IAM