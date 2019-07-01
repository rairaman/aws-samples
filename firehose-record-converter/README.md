# Firehose Record Conversion
Creates a Firehose Delivery Stream with Firehose Record Conversion (JSON to Parquet/ORC) enabled.

## Deploy
Use the provided Makefile to deploy:

1. A set of Glue resources that defines the schema of the JSON input into the firehose. This sample assumes the input JSON format is similar to the below:
```
{
    "First_Name":"Hello",
    "Last_Name":"World"
}
```
2. A Firehose delivery stream with data conversion enabled. The delivery stream needs to be provided with the Glue Database Name, Glue Table Name containing the input JSON schema, and an IAM role that enables it to access those Glue resources

```Make
make glue-resources GLUE_STACK_NAME=<Name of Cloud Formation stack to deploy in>	
					GLUE_DB_NAME=<Name of the glue database where the target input schema will reside>
					GLUE_TABLE_NAME=<Name of the Glue table defining the input schema to convert>

make deploy-firehose STACK_NAME=<Name of Cloud Formation stack to deploy in>				
						FH_DEL_STR_NAME=<Name of the firehose delivery stream>
						GLUE_TABLE_NAME=<Name of the Glue table defining the input schema to convert>
						GLUE_DB_NAME=<Name of the glue database where the target input schema resides>
						GLUE_INT_ROLE=<The IAM role that firehose uses to query the glue schema>
```

## Dependencies
- None