# deployÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/deploy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/deploy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ecs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/index.html#cli-aws-ecs) ]

# deploy

## Description

Deploys a new task definition to the specified ECS service. Only services that use CodeDeploy for deployments are supported. This command will register a new task definition, update the CodeDeploy appspec with the new task definition revision, create a CodeDeploy deployment, and wait for the deployment to successfully complete. This command will exit with a return code of 255 if the deployment does not succeed within 30 minutes by default or up to 10 minutes more than your deployment groupâs configured wait time (max of 6 hours).

## Synopsis

```
deploy
--service <value>
--task-definition <value>
--codedeploy-appspec <value>
[--cluster <value>]
[--codedeploy-application <value>]
[--codedeploy-deployment-group <value>]
[--debug]
[--endpoint-url <value>]
[--no-verify-ssl]
[--no-paginate]
[--output <value>]
[--query <value>]
[--profile <value>]
[--region <value>]
[--version <value>]
[--color <value>]
[--no-sign-request]
[--ca-bundle <value>]
[--cli-read-timeout <value>]
[--cli-connect-timeout <value>]
[--cli-binary-format <value>]
[--no-cli-pager]
[--cli-auto-prompt]
[--no-cli-auto-prompt]
```

## Options

`--service` (string)
The short name or full Amazon Resource Name (ARN) of the service to update

`--task-definition` (string)
The file path where your task definition file is located. The format of the file must be the same as the JSON output of:

```
aws ecs register-task-definition --generate-cli-skeleton
```

`--codedeploy-appspec` (string)
The file path where your AWS CodeDeploy appspec file is located. The appspec file may be in JSON or YAML format. The `TaskDefinition` property will be updated within the appspec with the newly registered task definition ARN, overwriting any placeholder values in the file.

`--cluster` (string)
The short name or full Amazon Resource Name (ARN) of the cluster that your service is running within. If you do not specify a cluster, the âdefaultâ cluster is assumed.

`--codedeploy-application` (string)
The name of the AWS CodeDeploy application to use for the deployment. The specified application must use the âECSâ compute platform. If you do not specify an application, the application name `AppECS-[CLUSTER_NAME]-[SERVICE_NAME]` is assumed.

`--codedeploy-deployment-group` (string)
The name of the AWS CodeDeploy deployment group to use for the deployment. The specified deployment group must be associated with the specified ECS service and cluster. If you do not specify a deployment group, the deployment group name `DgpECS-[CLUSTER_NAME]-[SERVICE_NAME]` is assumed.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override commandâs default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.