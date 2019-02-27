PKG_DIR=panda-layer/python/lib/python3.7/site-packages
LAYER_STACK_NAME=demo-panda-layer
LAMBDA_STACK_NAME=demo-panda-lambda

clean:
	rm -rf $(PKG_DIR)
	rm -rf packaged-template.yml

compile-panda: clean
	mkdir -p $(PKG_DIR)
	docker run --rm -u 1000:1000 -v "$(PWD)":/tmp -w /tmp lambci/lambda:build-python3.7 pip install -r requirements.txt --no-deps -t $(PKG_DIR)

#Usage: make deploy-panda-layer DEPLOY_BUCKET=<Bucket where Cloud formation can store package items>
deploy-panda-layer:
	aws cloudformation package --template-file deploy-panda-layer.yaml \
		--s3-bucket $(DEPLOY_BUCKET) \
		--output-template-file packaged-template.yml 

	aws cloudformation deploy \
		--template-file  packaged-template.yml \
		--stack-name $(LAYER_STACK_NAME) \
		--no-fail-on-empty-changeset \
		--capabilities CAPABILITY_NAMED_IAM

#Usage: make deploy-lambda-demo DEPLOY_BUCKET=<Bucket where Cloud formation can store package items>
#					PD_LY_ARN=<ARN of the layer containing the python library required>			
deploy-lambda-demo:
	aws cloudformation package --template-file deploy-lambda.yaml \
		--s3-bucket $(DEPLOY_BUCKET) \
		--output-template-file packaged-template.yml 

	aws cloudformation deploy \
		--template-file  packaged-template.yml \
		--stack-name $(LAMBDA_STACK_NAME) \
		--parameter-overrides PandaLayerArn=$(PD_LY_ARN) \
		--no-fail-on-empty-changeset \
		--capabilities CAPABILITY_NAMED_IAM