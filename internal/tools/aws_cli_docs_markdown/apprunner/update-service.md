# update-serviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/update-service.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/update-service.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [apprunner](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/apprunner/index.html#cli-aws-apprunner) ]

# update-service

## Description

Update an App Runner service. You can update the source configuration and instance configuration of the service. You can also update the ARN of the auto scaling configuration resource thatâs associated with the service. However, you canât change the name or the encryption configuration of the service. These can be set only when you create the service.

To update the tags applied to your service, use the separate actions  TagResource and  UntagResource .

This is an asynchronous operation. On a successful call, you can use the returned `OperationId` and the  ListOperations call to track the operationâs progress.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/apprunner-2020-05-15/UpdateService)

## Synopsis

```
update-service
--service-arn <value>
[--source-configuration <value>]
[--instance-configuration <value>]
[--auto-scaling-configuration-arn <value>]
[--health-check-configuration <value>]
[--network-configuration <value>]
[--observability-configuration <value>]
[--cli-input-json | --cli-input-yaml]
[--generate-cli-skeleton <value>]
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

`--service-arn` (string)

The Amazon Resource Name (ARN) of the App Runner service that you want to update.

`--source-configuration` (structure)

The source configuration to apply to the App Runner service.

You can change the configuration of the code or image repository that the service uses. However, you canât switch from code to image or the other way around. This means that you must provide the same structure member of `SourceConfiguration` that you originally included when you created the service. Specifically, you can include either `CodeRepository` or `ImageRepository` . To update the source configuration, set the values to members of the structure that you include.

CodeRepository -> (structure)

The description of a source code repository.

You must provide either this member or `ImageRepository` (but not both).

RepositoryUrl -> (string)

The location of the repository that contains the source code.

SourceCodeVersion -> (structure)

The version that should be used within the source code repository.

Type -> (string)

The type of version identifier.

For a git-based repository, branches represent versions.

Value -> (string)

A source code version.

For a git-based repository, a branch name maps to a specific version. App Runner uses the most recent commit to the branch.

CodeConfiguration -> (structure)

Configuration for building and running the service from a source code repository.

### Note

`CodeConfiguration` is required only for `CreateService` request.

ConfigurationSource -> (string)

The source of the App Runner configuration. Values are interpreted as follows:

- `REPOSITORY` â App Runner reads configuration values from the `apprunner.yaml` file in the source code repository and ignores `CodeConfigurationValues` .
- `API` â App Runner uses configuration values provided in `CodeConfigurationValues` and ignores the `apprunner.yaml` file in the source code repository.

CodeConfigurationValues -> (structure)

The basic configuration for building and running the App Runner service. Use it to quickly launch an App Runner service without providing a `apprunner.yaml` file in the source code repository (or ignoring the file if it exists).

Runtime -> (string)

A runtime environment type for building and running an App Runner service. It represents a programming language runtime.

BuildCommand -> (string)

The command App Runner runs to build your application.

StartCommand -> (string)

The command App Runner runs to start your application.

Port -> (string)

The port that your application listens to in the container.

Default: `8080`

RuntimeEnvironmentVariables -> (map)

The environment variables that are available to your running App Runner service. An array of key-value pairs.

key -> (string)

value -> (string)

RuntimeEnvironmentSecrets -> (map)

An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

- If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Amazon Web Services Region as the service that youâre launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified.
- Currently, cross account referencing of Amazon Web Services Systems Manager Parameter Store parameter is not supported.

key -> (string)

value -> (string)

SourceDirectory -> (string)

The path of the directory that stores source code and configuration files. The build and start commands also execute from here. The path is absolute from root and, if not specified, defaults to the repository root.

ImageRepository -> (structure)

The description of a source image repository.

You must provide either this member or `CodeRepository` (but not both).

ImageIdentifier -> (string)

The identifier of an image.

For an image in Amazon Elastic Container Registry (Amazon ECR), this is an image name. For the image name format, see [Pulling an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide* .

ImageConfiguration -> (structure)

Configuration for running the identified image.

RuntimeEnvironmentVariables -> (map)

Environment variables that are available to your running App Runner service. An array of key-value pairs.

key -> (string)

value -> (string)

StartCommand -> (string)

An optional command that App Runner runs to start the application in the source image. If specified, this command overrides the Docker imageâs default start command.

Port -> (string)

The port that your application listens to in the container.

Default: `8080`

RuntimeEnvironmentSecrets -> (map)

An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

- If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Amazon Web Services Region as the service that youâre launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified.
- Currently, cross account referencing of Amazon Web Services Systems Manager Parameter Store parameter is not supported.

key -> (string)

value -> (string)

ImageRepositoryType -> (string)

The type of the image repository. This reflects the repository provider and whether the repository is private or public.

AutoDeploymentsEnabled -> (boolean)

If `true` , continuous integration from the source repository is enabled for the App Runner service. Each repository change (including any source code commit or new image version) starts a deployment.

Default: App Runner sets to `false` for a source image that uses an ECR Public repository or an ECR repository thatâs in an Amazon Web Services account other than the one that the service is in. App Runner sets to `true` in all other cases (which currently include a source code repository or a source image using a same-account ECR repository).

AuthenticationConfiguration -> (structure)

Describes the resources that are needed to authenticate access to some source repositories.

ConnectionArn -> (string)

The Amazon Resource Name (ARN) of the App Runner connection that enables the App Runner service to connect to a source repository. Itâs required for GitHub code repositories.

AccessRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that grants the App Runner service access to a source repository. Itâs required for ECR image repositories (but not for ECR Public repositories).

JSON Syntax:

```
{
  "CodeRepository": {
    "RepositoryUrl": "string",
    "SourceCodeVersion": {
      "Type": "BRANCH",
      "Value": "string"
    },
    "CodeConfiguration": {
      "ConfigurationSource": "REPOSITORY"|"API",
      "CodeConfigurationValues": {
        "Runtime": "PYTHON_3"|"NODEJS_12"|"NODEJS_14"|"CORRETTO_8"|"CORRETTO_11"|"NODEJS_16"|"GO_1"|"DOTNET_6"|"PHP_81"|"RUBY_31"|"PYTHON_311"|"NODEJS_18"|"NODEJS_22",
        "BuildCommand": "string",
        "StartCommand": "string",
        "Port": "string",
        "RuntimeEnvironmentVariables": {"string": "string"
          ...},
        "RuntimeEnvironmentSecrets": {"string": "string"
          ...}
      }
    },
    "SourceDirectory": "string"
  },
  "ImageRepository": {
    "ImageIdentifier": "string",
    "ImageConfiguration": {
      "RuntimeEnvironmentVariables": {"string": "string"
        ...},
      "StartCommand": "string",
      "Port": "string",
      "RuntimeEnvironmentSecrets": {"string": "string"
        ...}
    },
    "ImageRepositoryType": "ECR"|"ECR_PUBLIC"
  },
  "AutoDeploymentsEnabled": true|false,
  "AuthenticationConfiguration": {
    "ConnectionArn": "string",
    "AccessRoleArn": "string"
  }
}
```

`--instance-configuration` (structure)

The runtime configuration to apply to instances (scaling units) of your service.

Cpu -> (string)

The number of CPU units reserved for each instance of your App Runner service.

Default: `1 vCPU`

Memory -> (string)

The amount of memory, in MB or GB, reserved for each instance of your App Runner service.

Default: `2 GB`

InstanceRoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that provides permissions to your App Runner service. These are permissions that your code needs when it calls any Amazon Web Services APIs.

Shorthand Syntax:

```
Cpu=string,Memory=string,InstanceRoleArn=string
```

JSON Syntax:

```
{
  "Cpu": "string",
  "Memory": "string",
  "InstanceRoleArn": "string"
}
```

`--auto-scaling-configuration-arn` (string)

The Amazon Resource Name (ARN) of an App Runner automatic scaling configuration resource that you want to associate with the App Runner service.

`--health-check-configuration` (structure)

The settings for the health check that App Runner performs to monitor the health of the App Runner service.

Protocol -> (string)

The IP protocol that App Runner uses to perform health checks for your service.

If you set `Protocol` to `HTTP` , App Runner sends health check requests to the HTTP path specified by `Path` .

Default: `TCP`

Path -> (string)

The URL that health check requests are sent to.

`Path` is only applicable when you set `Protocol` to `HTTP` .

Default: `"/"`

Interval -> (integer)

The time interval, in seconds, between health checks.

Default: `5`

Timeout -> (integer)

The time, in seconds, to wait for a health check response before deciding it failed.

Default: `2`

HealthyThreshold -> (integer)

The number of consecutive checks that must succeed before App Runner decides that the service is healthy.

Default: `1`

UnhealthyThreshold -> (integer)

The number of consecutive checks that must fail before App Runner decides that the service is unhealthy.

Default: `5`

Shorthand Syntax:

```
Protocol=string,Path=string,Interval=integer,Timeout=integer,HealthyThreshold=integer,UnhealthyThreshold=integer
```

JSON Syntax:

```
{
  "Protocol": "TCP"|"HTTP",
  "Path": "string",
  "Interval": integer,
  "Timeout": integer,
  "HealthyThreshold": integer,
  "UnhealthyThreshold": integer
}
```

`--network-configuration` (structure)

Configuration settings related to network traffic of the web application that the App Runner service runs.

EgressConfiguration -> (structure)

Network configuration settings for outbound message traffic.

EgressType -> (string)

The type of egress configuration.

Set to `DEFAULT` for access to resources hosted on public networks.

Set to `VPC` to associate your service to a custom VPC specified by `VpcConnectorArn` .

VpcConnectorArn -> (string)

The Amazon Resource Name (ARN) of the App Runner VPC connector that you want to associate with your App Runner service. Only valid when `EgressType = VPC` .

IngressConfiguration -> (structure)

Network configuration settings for inbound message traffic.

IsPubliclyAccessible -> (boolean)

Specifies whether your App Runner service is publicly accessible. To make the service publicly accessible set it to `True` . To make the service privately accessible, from only within an Amazon VPC set it to `False` .

IpAddressType -> (string)

App Runner provides you with the option to choose between *Internet Protocol version 4 (IPv4)* and *dual stack* (IPv4 and IPv6) for your incoming public network configuration. This is an optional parameter. If you do not specify an `IpAddressType` , it defaults to select IPv4.

### Note

Currently, App Runner supports dual stack for only Public endpoint. Only IPv4 is supported for Private endpoint. If you update a service thatâs using dual-stack Public endpoint to a Private endpoint, your App Runner service will default to support only IPv4 for Private endpoint and fail to receive traffic originating from IPv6 endpoint.

Shorthand Syntax:

```
EgressConfiguration={EgressType=string,VpcConnectorArn=string},IngressConfiguration={IsPubliclyAccessible=boolean},IpAddressType=string
```

JSON Syntax:

```
{
  "EgressConfiguration": {
    "EgressType": "DEFAULT"|"VPC",
    "VpcConnectorArn": "string"
  },
  "IngressConfiguration": {
    "IsPubliclyAccessible": true|false
  },
  "IpAddressType": "IPV4"|"DUAL_STACK"
}
```

`--observability-configuration` (structure)

The observability configuration of your service.

ObservabilityEnabled -> (boolean)

When `true` , an observability configuration resource is associated with the service, and an `ObservabilityConfigurationArn` is specified.

ObservabilityConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the observability configuration that is associated with the service. Specified only when `ObservabilityEnabled` is `true` .

Specify an ARN with a name and a revision number to associate that revision. For example: `arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/3`

Specify just the name to associate the latest revision. For example: `arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing`

Shorthand Syntax:

```
ObservabilityEnabled=boolean,ObservabilityConfigurationArn=string
```

JSON Syntax:

```
{
  "ObservabilityEnabled": true|false,
  "ObservabilityConfigurationArn": "string"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string)
Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update memory size**

The following `update-service` example updates the memory size of instances (scaling units) of an App Runner service to 2048 MiB.

When the call succeeds, App Runner starts an asynchronous update process.
The `Service` structure thatâs returned by the call reflects the new memory value thatâs being applied by this call.

```
aws apprunner update-service \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa",
    "InstanceConfiguration": {
        "Memory": "4 GB"
    }
}
```

Output:

```
{
    "OperationId": "17fe9f55-7e91-4097-b243-fcabbb69a4cf",
    "Service": {
        "CreatedAt": "2020-11-20T19:05:25Z",
        "UpdatedAt": "2020-11-23T12:41:37Z",
        "ServiceArn": "arn:aws:apprunner:us-east-1:123456789012:service/python-app/8fe1e10304f84fd2b0df550fe98a71fa",
        "ServiceId": "8fe1e10304f84fd2b0df550fe98a71fa",
        "ServiceName": "python-app",
        "ServiceUrl": "psbqam834h.us-east-1.awsapprunner.com",
        "SourceConfiguration": {
            "AuthenticationConfiguration": {
                "ConnectionArn": "arn:aws:apprunner:us-east-1:123456789012:connection/my-github-connection/e7656250f67242d7819feade6800f59e"
            },
            "AutoDeploymentsEnabled": true,
            "CodeRepository": {
                "CodeConfiguration": {
                    "CodeConfigurationValues": {
                        "BuildCommand": "pip install -r requirements.txt",
                        "Port": "8080",
                        "Runtime": "PYTHON_3",
                        "RuntimeEnvironmentVariables": [
                            {
                                "NAME": "Jane"
                            }
                        ],
                        "StartCommand": "python server.py"
                    },
                    "ConfigurationSource": "Api"
                },
                "RepositoryUrl": "https://github.com/my-account/python-hello",
                "SourceCodeVersion": {
                    "Type": "BRANCH",
                    "Value": "main"
                }
            }
        },
        "Status": "OPERATION_IN_PROGRESS",
        "InstanceConfiguration": {
            "CPU": "1 vCPU",
            "Memory": "4 GB"
        }
    }
}
```

## Output

Service -> (structure)

A description of the App Runner service updated by this request. All configuration values in the returned `Service` structure reflect configuration changes that are being applied by this request.

ServiceName -> (string)

The customer-provided service name.

ServiceId -> (string)

An ID that App Runner generated for this service. Itâs unique within the Amazon Web Services Region.

ServiceArn -> (string)

The Amazon Resource Name (ARN) of this service.

ServiceUrl -> (string)

A subdomain URL that App Runner generated for this service. You can use this URL to access your service web application.

CreatedAt -> (timestamp)

The time when the App Runner service was created. Itâs in the Unix time stamp format.

UpdatedAt -> (timestamp)

The time when the App Runner service was last updated at. Itâs in the Unix time stamp format.

DeletedAt -> (timestamp)

The time when the App Runner service was deleted. Itâs in the Unix time stamp format.

Status -> (string)

The current state of the App Runner service. These particular values mean the following.

- `CREATE_FAILED` â The service failed to create. The failed service isnât usable, and still counts towards your service quota. To troubleshoot this failure, read the failure events and logs, change any parameters that need to be fixed, and rebuild your service using `UpdateService` .
- `DELETE_FAILED` â The service failed to delete and canât be successfully recovered. Retry the service deletion call to ensure that all related resources are removed.

SourceConfiguration -> (structure)

The source deployed to the App Runner service. It can be a code or an image repository.

CodeRepository -> (structure)

The description of a source code repository.

You must provide either this member or `ImageRepository` (but not both).

RepositoryUrl -> (string)

The location of the repository that contains the source code.

SourceCodeVersion -> (structure)

The version that should be used within the source code repository.

Type -> (string)

The type of version identifier.

For a git-based repository, branches represent versions.

Value -> (string)

A source code version.

For a git-based repository, a branch name maps to a specific version. App Runner uses the most recent commit to the branch.

CodeConfiguration -> (structure)

Configuration for building and running the service from a source code repository.

### Note

`CodeConfiguration` is required only for `CreateService` request.

ConfigurationSource -> (string)

The source of the App Runner configuration. Values are interpreted as follows:

- `REPOSITORY` â App Runner reads configuration values from the `apprunner.yaml` file in the source code repository and ignores `CodeConfigurationValues` .
- `API` â App Runner uses configuration values provided in `CodeConfigurationValues` and ignores the `apprunner.yaml` file in the source code repository.

CodeConfigurationValues -> (structure)

The basic configuration for building and running the App Runner service. Use it to quickly launch an App Runner service without providing a `apprunner.yaml` file in the source code repository (or ignoring the file if it exists).

Runtime -> (string)

A runtime environment type for building and running an App Runner service. It represents a programming language runtime.

BuildCommand -> (string)

The command App Runner runs to build your application.

StartCommand -> (string)

The command App Runner runs to start your application.

Port -> (string)

The port that your application listens to in the container.

Default: `8080`

RuntimeEnvironmentVariables -> (map)

The environment variables that are available to your running App Runner service. An array of key-value pairs.

key -> (string)

value -> (string)

RuntimeEnvironmentSecrets -> (map)

An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

- If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Amazon Web Services Region as the service that youâre launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified.
- Currently, cross account referencing of Amazon Web Services Systems Manager Parameter Store parameter is not supported.

key -> (string)

value -> (string)

SourceDirectory -> (string)

The path of the directory that stores source code and configuration files. The build and start commands also execute from here. The path is absolute from root and, if not specified, defaults to the repository root.

ImageRepository -> (structure)

The description of a source image repository.

You must provide either this member or `CodeRepository` (but not both).

ImageIdentifier -> (string)

The identifier of an image.

For an image in Amazon Elastic Container Registry (Amazon ECR), this is an image name. For the image name format, see [Pulling an image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-pull-ecr-image.html) in the *Amazon ECR User Guide* .

ImageConfiguration -> (structure)

Configuration for running the identified image.

RuntimeEnvironmentVariables -> (map)

Environment variables that are available to your running App Runner service. An array of key-value pairs.

key -> (string)

value -> (string)

StartCommand -> (string)

An optional command that App Runner runs to start the application in the source image. If specified, this command overrides the Docker imageâs default start command.

Port -> (string)

The port that your application listens to in the container.

Default: `8080`

RuntimeEnvironmentSecrets -> (map)

An array of key-value pairs representing the secrets and parameters that get referenced to your service as an environment variable. The supported values are either the full Amazon Resource Name (ARN) of the Secrets Manager secret or the full ARN of the parameter in the Amazon Web Services Systems Manager Parameter Store.

### Note

- If the Amazon Web Services Systems Manager Parameter Store parameter exists in the same Amazon Web Services Region as the service that youâre launching, you can use either the full ARN or name of the secret. If the parameter exists in a different Region, then the full ARN must be specified.
- Currently, cross account referencing of Amazon Web Services Systems Manager Parameter Store parameter is not supported.

key -> (string)

value -> (string)

ImageRepositoryType -> (string)

The type of the image repository. This reflects the repository provider and whether the repository is private or public.

AutoDeploymentsEnabled -> (boolean)

If `true` , continuous integration from the source repository is enabled for the App Runner service. Each repository change (including any source code commit or new image version) starts a deployment.

Default: App Runner sets to `false` for a source image that uses an ECR Public repository or an ECR repository thatâs in an Amazon Web Services account other than the one that the service is in. App Runner sets to `true` in all other cases (which currently include a source code repository or a source image using a same-account ECR repository).

AuthenticationConfiguration -> (structure)

Describes the resources that are needed to authenticate access to some source repositories.

ConnectionArn -> (string)

The Amazon Resource Name (ARN) of the App Runner connection that enables the App Runner service to connect to a source repository. Itâs required for GitHub code repositories.

AccessRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role that grants the App Runner service access to a source repository. Itâs required for ECR image repositories (but not for ECR Public repositories).

InstanceConfiguration -> (structure)

The runtime configuration of instances (scaling units) of this service.

Cpu -> (string)

The number of CPU units reserved for each instance of your App Runner service.

Default: `1 vCPU`

Memory -> (string)

The amount of memory, in MB or GB, reserved for each instance of your App Runner service.

Default: `2 GB`

InstanceRoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that provides permissions to your App Runner service. These are permissions that your code needs when it calls any Amazon Web Services APIs.

EncryptionConfiguration -> (structure)

The encryption key that App Runner uses to encrypt the service logs and the copy of the source repository that App Runner maintains for the service. It can be either a customer-provided encryption key or an Amazon Web Services managed key.

KmsKey -> (string)

The ARN of the KMS key thatâs used for encryption.

HealthCheckConfiguration -> (structure)

The settings for the health check that App Runner performs to monitor the health of this service.

Protocol -> (string)

The IP protocol that App Runner uses to perform health checks for your service.

If you set `Protocol` to `HTTP` , App Runner sends health check requests to the HTTP path specified by `Path` .

Default: `TCP`

Path -> (string)

The URL that health check requests are sent to.

`Path` is only applicable when you set `Protocol` to `HTTP` .

Default: `"/"`

Interval -> (integer)

The time interval, in seconds, between health checks.

Default: `5`

Timeout -> (integer)

The time, in seconds, to wait for a health check response before deciding it failed.

Default: `2`

HealthyThreshold -> (integer)

The number of consecutive checks that must succeed before App Runner decides that the service is healthy.

Default: `1`

UnhealthyThreshold -> (integer)

The number of consecutive checks that must fail before App Runner decides that the service is unhealthy.

Default: `5`

AutoScalingConfigurationSummary -> (structure)

Summary information for the App Runner automatic scaling configuration resource thatâs associated with this service.

AutoScalingConfigurationArn -> (string)

The Amazon Resource Name (ARN) of this auto scaling configuration.

AutoScalingConfigurationName -> (string)

The customer-provided auto scaling configuration name. It can be used in multiple revisions of a configuration.

AutoScalingConfigurationRevision -> (integer)

The revision of this auto scaling configuration. Itâs unique among all the active configurations (`"Status": "ACTIVE"` ) with the same `AutoScalingConfigurationName` .

Status -> (string)

The current state of the auto scaling configuration. If the status of a configuration revision is `INACTIVE` , it was deleted and canât be used. Inactive configuration revisions are permanently removed some time after they are deleted.

CreatedAt -> (timestamp)

The time when the auto scaling configuration was created. Itâs in Unix time stamp format.

HasAssociatedService -> (boolean)

Indicates if this auto scaling configuration has an App Runner service associated with it. A value of `true` indicates one or more services are associated. A value of `false` indicates no services are associated.

IsDefault -> (boolean)

Indicates if this auto scaling configuration should be used as the default for a new App Runner service that does not have an auto scaling configuration ARN specified during creation. Each account can have only one default `AutoScalingConfiguration` per region. The default `AutoScalingConfiguration` can be any revision under the same `AutoScalingConfigurationName` .

NetworkConfiguration -> (structure)

Configuration settings related to network traffic of the web application that this service runs.

EgressConfiguration -> (structure)

Network configuration settings for outbound message traffic.

EgressType -> (string)

The type of egress configuration.

Set to `DEFAULT` for access to resources hosted on public networks.

Set to `VPC` to associate your service to a custom VPC specified by `VpcConnectorArn` .

VpcConnectorArn -> (string)

The Amazon Resource Name (ARN) of the App Runner VPC connector that you want to associate with your App Runner service. Only valid when `EgressType = VPC` .

IngressConfiguration -> (structure)

Network configuration settings for inbound message traffic.

IsPubliclyAccessible -> (boolean)

Specifies whether your App Runner service is publicly accessible. To make the service publicly accessible set it to `True` . To make the service privately accessible, from only within an Amazon VPC set it to `False` .

IpAddressType -> (string)

App Runner provides you with the option to choose between *Internet Protocol version 4 (IPv4)* and *dual stack* (IPv4 and IPv6) for your incoming public network configuration. This is an optional parameter. If you do not specify an `IpAddressType` , it defaults to select IPv4.

### Note

Currently, App Runner supports dual stack for only Public endpoint. Only IPv4 is supported for Private endpoint. If you update a service thatâs using dual-stack Public endpoint to a Private endpoint, your App Runner service will default to support only IPv4 for Private endpoint and fail to receive traffic originating from IPv6 endpoint.

ObservabilityConfiguration -> (structure)

The observability configuration of this service.

ObservabilityEnabled -> (boolean)

When `true` , an observability configuration resource is associated with the service, and an `ObservabilityConfigurationArn` is specified.

ObservabilityConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the observability configuration that is associated with the service. Specified only when `ObservabilityEnabled` is `true` .

Specify an ARN with a name and a revision number to associate that revision. For example: `arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing/3`

Specify just the name to associate the latest revision. For example: `arn:aws:apprunner:us-east-1:123456789012:observabilityconfiguration/xray-tracing`

OperationId -> (string)

The unique ID of the asynchronous operation that this request started. You can use it combined with the  ListOperations call to track the operationâs progress.