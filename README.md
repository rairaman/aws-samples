# AWS Samples
Small tidbits of AWS code

## Samples
1. [API Gateway with Swagger definition](./001-apigw-swagger/README.md) - Two sample API endpoints, defined using the OpenApi specification. One of the endpoints has request payload validation built-in
2. [Firehose Demo](./002-firehose-demo/README.md) - Deploys a Kinesis Firehose Delivery Stream with a simple lambda transformer
3. [Firehose Record Converter](./003-firehose-record-converter/README.md) - Deploys Glue resources, a Kinesis Firehose Delivery Stream with record conversion enabled and a lambda that gets pedestrian count data from the City of Melbourne dataset at 15mins interval
4. [Long Job Poller](./004-long-job-polling/README.md) - A state machine that can be used to check for the completion of a long running job (via a lambda)
5. [Panda python data library as a layer](./006-panda-lambda-layer/README.md) - Deploys a lambda layer containing the python panda data manipulation library and a sample lambda referencing that library
