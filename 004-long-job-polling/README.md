## Long job checking Lambda
This tidbit contains an example lambda and state machine (step function) that can be used to check on the status of a long running job or process. This is useful if the long running job takes a fairly long time to complete, and an action needs to be performed once the job has completed. The step function triggers a lambda
every 5 mins. The lambda is responsible for checking whether the long job has completed. The state machine will keep checking until either the job has completed, or a configurable timeout to stop the checks has been reached (default of 30mins)

## Deploy
Use the provided Makefile and run
```Make
make deploy STACK_NAME=<name to give the Cloudformation stack> DEPLOY_BUCKET=<An S3 bucket that CloudFormation can use to store packaged lambda code>
```

## Dependencies
* AWS SAM Cli version 0.52 or above
* Docker (to run tests)
