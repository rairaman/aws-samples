
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

# Usage:
# make deploy-data-sourcer DEPLOY_BUCKET=<S3 bucket where lambda code is deployed by CloudFormation>
# 							DS_STACK_NAME=<Name of CloudFormation stack to deploy in>
deploy-data-sourcer:
	aws cloudformation package --template-file deploy-data-sourcer.yml \
		--s3-bucket $(DEPLOY_BUCKET) \
		--output-template-file packaged-template.yml 

	aws cloudformation deploy \
		--template-file packaged-template.yml \
		--stack-name $(DS_STACK_NAME) \
		--capabilities CAPABILITY_NAMED_IAM

#-e ./local-resources/test-event.json
# Usage:
# make run-local-data-sourcer FIREHOSE_NAME=<Name of the firehose stream the lambda function will write to>
run-local-data-sourcer:
	cp ./local-resources/env-vars-template.json ./local-resources/env-vars.json
	sed -i 's/FIREHOSE_ARN_REPLACE/$(FIREHOSE_NAME)/' ./local-resources/env-vars.json
	sam local invoke --no-event --env-vars ./local-resources/env-vars.json -t deploy-data-sourcer.yml
	rm ./local-resources/env-vars.json