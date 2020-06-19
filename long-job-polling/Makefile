

deploy:
	sam deploy --template-file deploy-long-job-poll.yaml \
		--s3-bucket $(DEPLOY_BUCKET) \
		--stack-name $(STACK_NAME) \
		--capabilities CAPABILITY_NAMED_IAM \
		--no-fail-on-empty-changeset