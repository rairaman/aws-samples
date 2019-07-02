
# Usage:
# make glue-resources GLUE_STACK_NAME=<Name of Cloud Formation stack to deploy in>	
#						GLUE_DB_NAME=<Name of the glue database where the target input schema will reside>
#						GLUE_TABLE_NAME=<Name of the Glue table defining the input schema to convert>
glue-resources:
	aws cloudformation deploy \
		--template-file deploy-glue-resources.yml \
		--stack-name $(GLUE_STACK_NAME) \
		--parameter-overrides FirehoseInputDbName=$(GLUE_DB_NAME) \
								FirehoseInputTableName=$(GLUE_TABLE_NAME) \
		--capabilities CAPABILITY_NAMED_IAM

# Usage:
# make deploy-firehose FH_STACK_NAME=<Name of Cloud Formation stack to deploy in>				
#						FH_DEL_STR_NAME=<Name of the firehose delivery stream>
#						GLUE_TABLE_NAME=<Name of the Glue table defining the input schema to convert>
#						GLUE_DB_NAME=<Name of the glue database where the target input schema resides>
#						GLUE_INT_ROLE=<The IAM role that firehose uses to query the glue schema>
deploy-firehose:
	aws cloudformation deploy \
		--template-file deploy-firehose.yml \
		--stack-name $(FH_STACK_NAME) \
		--parameter-overrides FirehoseDeliveryStreamName=$(FH_DEL_STR_NAME) \
								GlueTableName=$(GLUE_TABLE_NAME) \
								GlueDatabaseName=$(GLUE_DB_NAME) \
								GlueInteractionRoleArn=$(GLUE_INT_ROLE) \
		--capabilities CAPABILITY_NAMED_IAM
