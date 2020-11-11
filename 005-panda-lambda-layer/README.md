# Panda Lambda Layer
Contains two SAM (Serverless Application Model) resources, one that deploys a Lambda layer with the panda library and another one containing a lambda that references the panda layer

## Deploy
Use the provided makefile to first deploy the layer. The CloudFormation Stack outputs the ARN of the newly created layer. This ARN can then be used as an argument for the stack containing the lamdbda
```
make deploy-panda-layer DEPLOY_BUCKET=<s3_bucket_name_for_packages>

make deploy-lambda-demo DEPLOY_BUCKET=<s3_bucket_name_for_packages> PD_LY_ARN=<arn_of_panda_layer>
```

## Local Testing
The lambda can be tested locally as long as the dependent layers have been deployed. The layers will be downloaded and cached by the SAM CLI when the lambda is invoked locally.
```
make run-local PD_LY_ARN=<ARN of the layer containing the python library required>
```

## Dependencies
- An S3 bucket used by CloudFormation to package the lambda function as well as the lambda layer