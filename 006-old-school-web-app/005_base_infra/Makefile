BASE_VPC_STACK_NAME=005-base-vpc
WEB_BKT_STACK_NAME=005-web-app-code
ENVIRONMENT_NAME=dev

validate-infra:
	aws cloudformation validate-template \
		--template-body file://base_vpc.yaml

	aws cloudformation validate-template \
		--template-body file://web_app_code.yaml

deploy-base-infra:
	aws cloudformation deploy \
		--template-file base_vpc.yaml \
		--stack-name $(ENVIRONMENT_NAME)-$(BASE_VPC_STACK_NAME) \
		--capabilities CAPABILITY_NAMED_IAM \
		--no-fail-on-empty-changeset \
		--parameter-overrides EnvironmentName=$(ENVIRONMENT_NAME)

deploy-web-app-bucket:
	aws cloudformation deploy \
		--template-file web_app_code.yaml \
		--stack-name $(ENVIRONMENT_NAME)-$(WEB_BKT_STACK_NAME) \
		--no-fail-on-empty-changeset

.PHONY: deploy-base-infra validate-base-infra deploy-web-app-bucket