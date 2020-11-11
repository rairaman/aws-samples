# Firehose Record Conversion
Creates a Firehose Delivery Stream with Firehose Record Conversion (JSON to Parquet) enabled. There's also a stack containing a lambda that gets
the City of Melbourne pedestrian sensor count data at interval of 15 mins. The Lambda is configured to send the sensor count data to the Firehose
resource which converts the data to Parquet.

## Deploy
Use the provided Makefile to deploy:

1. A set of Glue resources that defines the schema of the JSON input into firehose, as well as an IAM role that allows Firehose to access the Glue resources
```Make
make glue-resources GLUE_STACK_NAME=<Name of Cloud Formation stack to deploy in>	
					GLUE_DB_NAME=<Name of the glue database where the target input schema will reside>
					GLUE_TABLE_NAME=<Name of the Glue table defining the input schema to convert>
```
2. A Firehose delivery stream with data conversion enabled. The delivery stream needs to be provided with the Glue Database Name, Glue Table Name containing the input JSON schema, and an IAM role that enables it to access those Glue resources

```Make
make deploy-firehose STACK_NAME=<Name of Cloud Formation stack to deploy in>				
						FH_DEL_STR_NAME=<Name of the firehose delivery stream>
						GLUE_TABLE_NAME=<Name of the Glue table defining the input schema to convert>
						GLUE_DB_NAME=<Name of the glue database where the target input schema resides>
						GLUE_INT_ROLE=<The IAM role that firehose uses to query the glue schema>
```
3. A lambda function that gets the City of Melbourne pedestrian sensor counts at 15 mins intervals

```Make
make deploy-data-sourcer DEPLOY_BUCKET=<S3 bucket where lambda code is deployed by CloudFormation>
						DS_STACK_NAME=<Name of CloudFormation stack to deploy in>
```
## Dependencies
- None