# Firehose Record Conversion
Uses a custom resource to make an API call to enable the Firehose Record Conversion (JSON to Parquet/ORC )
This directory contains an example custom resource built using code from [AWS Labs](https://github.com/awslabs/aws-cloudformation-templates/tree/master/community/custom_resources/python_custom_resource_helper)

## Deploy
Use the provided Makefile to deploy:

1. A set of Glue resources that defines the schema of the JSON input into the firehose. This sample assumes the input JSON format is:
```
{
    "First_Name":"Hello",
    "Last_Name":"World"
}
```
2. A lambda backed custom resource that makes updates the S3 destination of an existing Firehose delivery stream and enables Data Conversion. The custom resource needs to be provided with the Glue Database Name, Glue Table Name containing the input JSON schema, and an IAM role that enables it to access those Glue resources

```Make
make glue-resources DEPLOY_BUCKET=<S3 bucket where lambda code is deployed by CloudFomration>
					CUST_STACK_NAME=<Name of Cloud Formation stack to deploy in>
					FRIENDLY_FH_NAME=<Friendly name to give the firehose delivery stream>
					GLUE_DB_NAME=<Name of the glue database where the target input schema will reside>
					GLUE_TABLE_NAME=<Name of the Glue table defining the input schema to convert>

make update-firehose DEPLOY_BUCKET=<S3 bucket where lambda code is deployed by CloudFomration>
					CUST_STACK_NAME=<Name of Cloud Formation stack to deploy in>
					FH_ARN=<ARN of the Firehose delivery stream to update>
					FH_DEL_STR_NAME=<Name of the firehose delivery stream>
					GLUE_TABLE_NAME=<Name of the Glue table defining the input schema to convert>
					GLUE_DB_NAME=<Name of the glue database where the target input schema resides>
					GLUE_INT_ROLE=<The IAM role that firehose uses to query the glue schema>
```

## Dependencies
- An S3 bucket used by CloudFormation to package lambdas