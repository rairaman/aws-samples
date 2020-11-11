# Api Gateway with a Swagger/OpenAPI inline definition
This tidbit contains two example API endpoints backed by two lambda functions. 

* /pets : Get a json list of pets
* /addPet: Post a json payload in the following format
```json
{ "name" : "Yuri the Yak" }
```

The API itself is defined using the OpenApi 3.0.0 specification. The OpenApi specification is defined in a file called swagger.yaml. However, the contents of the swagger file is pulled into the SAM template using an include function. The Api specification also includes a jsonschema definition that validates the format of the payload passed to the `addPet` endpoint.

## Deploy
Use the provided Makefile to deploy the API endpoints and the lambda functions

```Makefile
make deploy-api-gw DEPLOY_BUCKET=<S3 bucket where the CloudFormation package command can upload its artefacts to>
				 STACK_NAME=<Name to give to the Cloud Formation stack>
```

## Dependencies
AWS SAM cli for local testing