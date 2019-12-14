# AWS Samples
Small tidbits of AWS code

## Samples
1. [Firehose Demo](./firehose-demo/README.md) - Deploys a Kinesis Firehose Delivery Stream with a simple lambda transformer
2. [Firehose Record Converter](./firehose-record-converter/README.md) - Deploys Glue resources, a Kinesis Firehose Delivery Stream with record conversion enabled and a lambda that gets pedestrian count data from the City of Melbourne dataset at 15mins interval
3. [Panda python data library as a layer](./panda-lambda-layer/README.md) - Deploys a lambda layer containing the python panda data manipulation library and a sample lambda referencing that library