# get-container-service-deploymentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-service-deployments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-container-service-deployments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-container-service-deployments

## Description

Returns the deployments for your Amazon Lightsail container service

A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service.

The deployments are ordered by version in ascending order. The newest version is listed at the top of the response.

### Note

A set number of deployments are kept before the oldest one is replaced with the newest one. For more information, see [Amazon Lightsail endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/lightsail.html) in the *Amazon Web Services General Reference* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetContainerServiceDeployments)

## Synopsis

```
get-container-service-deployments
--service-name <value>
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

`--service-name` (string)

The name of the container service for which to return deployments.

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

## Output

deployments -> (list)

An array of objects that describe deployments for a container service.

(structure)

Describes a container deployment configuration of an Amazon Lightsail container service.

A deployment specifies the settings, such as the ports and launch command, of containers that are deployed to your container service.

version -> (integer)

The version number of the deployment.

state -> (string)

The state of the deployment.

A deployment can be in one of the following states:

- `ACTIVATING` - The deployment is being created.
- `ACTIVE` - The deployment was successfully created, and itâs currently running on the container service. The container service can have only one deployment in an active state at a time.
- `INACTIVE` - The deployment was previously successfully created, but it is not currently running on the container service.
- `FAILED` - The deployment failed. Use the `GetContainerLog` action to view the log events for the containers in the deployment to try to determine the reason for the failure.

containers -> (map)

An object that describes the configuration for the containers of the deployment.

key -> (string)

value -> (structure)

Describes the settings of a container that will be launched, or that is launched, to an Amazon Lightsail container service.

image -> (string)

The name of the image used for the container.

Container images sourced from your Lightsail container service, that are registered and stored on your service, start with a colon (`:` ). For example, if your container service name is `container-service-1` , the container image label is `mystaticsite` , and you want to use the third (`3` ) version of the registered container image, then you should specify `:container-service-1.mystaticsite.3` . To use the latest version of a container image, specify `latest` instead of a version number (for example, `:container-service-1.mystaticsite.latest` ). Lightsail will automatically use the highest numbered version of the registered container image.

Container images sourced from a public registry like Docker Hub donât start with a colon. For example, `nginx:latest` or `nginx` .

command -> (list)

The launch command for the container.

(string)

environment -> (map)

The environment variables of the container.

key -> (string)

value -> (string)

ports -> (map)

The open firewall ports of the container.

key -> (string)

value -> (string)

publicEndpoint -> (structure)

An object that describes the endpoint of the deployment.

containerName -> (string)

The name of the container entry of the deployment that the endpoint configuration applies to.

containerPort -> (integer)

The port of the specified container to which traffic is forwarded to.

healthCheck -> (structure)

An object that describes the health check configuration of the container.

healthyThreshold -> (integer)

The number of consecutive health checks successes required before moving the container to the `Healthy` state. The default value is `2` .

unhealthyThreshold -> (integer)

The number of consecutive health check failures required before moving the container to the `Unhealthy` state. The default value is `2` .

timeoutSeconds -> (integer)

The amount of time, in seconds, during which no response means a failed health check. You can specify between 2 and 60 seconds. The default value is `2` .

intervalSeconds -> (integer)

The approximate interval, in seconds, between health checks of an individual container. You can specify between 5 and 300 seconds. The default value is `5` .

path -> (string)

The path on the container on which to perform the health check. The default value is `/` .

successCodes -> (string)

The HTTP codes to use when checking for a successful response from a container. You can specify values between `200` and `499` . You can specify multiple values (for example, `200,202` ) or a range of values (for example, `200-299` ).

createdAt -> (timestamp)

The timestamp when the deployment was created.