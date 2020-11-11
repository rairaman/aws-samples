VPC_ID := $(shell aws ssm get-parameter --name /base-infra/vpc/id --query "Parameter.Value" --output text)
PUBLIC_SUBNET_ID := $(shell aws ssm get-parameter --name /base-infra/vpc/public-subnets --query "Parameter.Value" --output text | cut -d , -f 1)
GOLDEN_AMI_NAME?=simple_golden_ami

golden-ami:
	packer build -var "golden_ami_name=$(GOLDEN_AMI_NAME)" \
		-var "vpc_id=$(VPC_ID)" \
		-var "subnet_id=$(PUBLIC_SUBNET_ID)" \
		golden_ami.json

store-golden-ami-id:
	./scripts/store_golden_ami_id.sh $(GOLDEN_AMI_NAME)

.PHONY: golden-ami store-golden-ami-id