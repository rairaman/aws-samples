WEB_INFRA_STACK_NAME=020-web-infra
ENVIRONMENT_NAME=dev
VPC_ID := $(shell aws ssm get-parameter --name /base-infra/vpc/id --query "Parameter.Value" --output text)
PUBLIC_SUBNET_IDS := $(shell aws ssm get-parameter --name /base-infra/vpc/public-subnets --query "Parameter.Value" --output text)
PRIVATE_SUBNET_IDS := $(shell aws ssm get-parameter --name /base-infra/vpc/private-subnets --query "Parameter.Value" --output text)
WEB_APP_CODE_BKT_NAME := $(shell aws ssm get-parameter --name /base-infra/buckets/webappcode --query "Parameter.Value" --output text)

validate-web-infra:
	aws cloudformation validate-template \
		--template-body file://web_infra.yaml

deploy-web-infra:
	aws cloudformation deploy \
		--template-file web_infra.yaml \
		--stack-name $(ENVIRONMENT_NAME)-$(WEB_INFRA_STACK_NAME) \
		--capabilities CAPABILITY_NAMED_IAM \
		--no-fail-on-empty-changeset \
		--parameter-overrides VpcId=$(VPC_ID) \
							PrivateSubnets=$(PRIVATE_SUBNET_IDS) \
							PublicSubnets=$(PUBLIC_SUBNET_IDS)

upload-web-app:
	aws s3 sync ./web_app_code/ s3://$(WEB_APP_CODE_BKT_NAME)/web-app/

.PHONY: deploy-web-infra validate-web-infra upload-web-app