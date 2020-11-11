# Old School web application
Back in the day (circa 2012), deploying your web application directly on EC2 was quite popular. While you shouldn't even consider this sort of architecture for simple web applications these days (2020), doing so can teach you a lot about simple networking setup in an AWS VPC.

This repo contains artefacts that creates:
1. A CloudFormation template containing a simple 2-AZ VPC with a pair of public and a pair of private subnets, and NAT gateways
1. A CloudFormation template containing an S3 bucket to store application code
1. Scripts that create an Amazon Machine Image and store the ami id in an SSM parameter
1. A CloudFormation template containing an ELB, and an auto scaling group to host the application

## Prerequisites
1. Create a new or use an existing AWS IAM User with at least the following AWS Managed policies and one user managed policy:
    * AmazonEC2FullAccess Managed Policy
    * AmazonS3FullAccess Managed Policy
    * AmazonSSMFullAccess Managed Policy
    * AWSCloudFormationFullAccess Managed Policy
    * A user managed policy with the following permissions:
        1. iam:CreateRole
        1. iam:CreateInstanceProfile
        1. iam:GetRole
        1. iam:GetRolePolicy
        1. iam:PutRolePolicy
        1. iam:DeleteRole
        1. iam:DeleteInstanceProfile
        1. iam:DeleteRolePolicy
        1. iam:AddRoleToInstanceProfile
        1. iam:RemoveRoleFromInstanceProfile
        1. iam:PassRole
        1. iam:GetInstanceProfile
2. Install [Packer](https://learn.hashicorp.com/tutorials/packer/getting-started-install) for your operating system
3. Ensure that your system has [GNU Make](https://www.gnu.org/software/make/) installed

## Deployment instructions (provided templated VPC)
1. Start a terminal session and ensure that your session is configured to use the AWS IAM User created as part of the pre-requisites, or configured to use an IAM User or Role that has more permissions than described in the [prerequisites](#Prerequisites)
1. Change to the `005_base_infra` directory.
1. Run the `make deploy-base-infra` command and wait for the deployment to complete.
1. Run the `make deploy-web-app-bucket` command and wait for the deployment to complete.
1. Change to the `010_golden_ami` directory.
1. Run the `make golden-ami` command and wait for the AMI creation to complete.
1. Run the `make store-golden-ami-id simple_golden_ami` command.
1. Change to the `020_web_application` directory.
1. Run the `make upload-web-app` command and wait for all code files to the uploaded to S3.
1. Run the `make deploy-web-infra` command and wait for the deployment to complete.
1. Using the AWS Console, navigate to the EC2 page, and under Load Balancers, get the domain name of the Elastic Load Balancer created as part of the previous step
1. Use the domain name obtained in the previous step to get to the web application