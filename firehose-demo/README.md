# Firehose Demo
Creates a Firehose delivery stream, with an S3 bucket as a destination. The Firehose delivery stream additionally has a lambda function that will process all incoming packetsand spit back the original data received.

### Deploy
The Firehose demo can be deployed using Make. The name of an existing S3 bucket needs to be passed, as well as a name for the stack and a friendly name for the Firehose delivery stream
```make
make kinesis-firehose DEPLOY_BUCKET=<bucket-name> FH_STACK_NAME=<stack-name> FRIENDLY_FH_NAME=<A friendly name for firehose delivery>
```

### Dependencies
- An S3 bucket used by CloudFormation to package lambdas
