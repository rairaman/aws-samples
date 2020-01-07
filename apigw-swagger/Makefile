# Usage:
# make deploy-api-gw DEPLOY_BUCKET=<S3 bucket where the CloudFormation package command can upload its artefacts to>
#					 STACK_NAME=<Name to give to the Cloud Formation stack>
deploy-api-gw:
	aws cloudformation package --template-file deploy-api-gw.yaml \
		--s3-bucket $(DEPLOY_BUCKET) \
		--output-template-file packaged-template-api.yaml

	aws cloudformation deploy \
		--template-file  packaged-template-api.yaml \
		--stack-name $(STACK_NAME) \
		--capabilities CAPABILITY_NAMED_IAM \
		--no-fail-on-empty-changeset

# Usage:
# make run-local-lambda LAMBDA_FUNC_ID=<The logical resource name given to the lambda/serverless function in the CloudFormation template>
run-local-lambda:
	sam local invoke -t deploy-api-gw.yaml --no-event $(LAMBDA_FUNC_ID)

run-local-api: 
	sam local start-api -t deploy-api-gw.yaml

clean:
	rm packaged-template-api.yaml