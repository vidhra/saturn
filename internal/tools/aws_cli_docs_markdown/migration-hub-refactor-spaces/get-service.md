# get-serviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migration-hub-refactor-spaces/get-service.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migration-hub-refactor-spaces/get-service.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [migration-hub-refactor-spaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migration-hub-refactor-spaces/index.html#cli-aws-migration-hub-refactor-spaces) ]

# get-service

## Description

Gets an Amazon Web Services Migration Hub Refactor Spaces service.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/migration-hub-refactor-spaces-2021-10-26/GetService)

## Synopsis

```
get-service
--application-identifier <value>
--environment-identifier <value>
--service-identifier <value>
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

`--application-identifier` (string)

The ID of the application.

`--environment-identifier` (string)

The ID of the environment.

`--service-identifier` (string)

The ID of the service.

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

ApplicationId -> (string)

The ID of the application.

Arn -> (string)

The Amazon Resource Name (ARN) of the service.

CreatedByAccountId -> (string)

The Amazon Web Services account ID of the service creator.

CreatedTime -> (timestamp)

The timestamp of when the service is created.

Description -> (string)

The description of the service.

EndpointType -> (string)

The endpoint type of the service.

EnvironmentId -> (string)

The unique identifier of the environment.

Error -> (structure)

Any error associated with the service resource.

AccountId -> (string)

The Amazon Web Services account ID of the resource owner.

AdditionalDetails -> (map)

Additional details about the error.

key -> (string)

value -> (string)

Code -> (string)

The error code associated with the error.

Message -> (string)

The message associated with the error.

ResourceIdentifier -> (string)

The ID of the resource.

ResourceType -> (string)

The type of resource.

LambdaEndpoint -> (structure)

The configuration for the Lambda endpoint type.

The **Arn** is the Amazon Resource Name (ARN) of the Lambda function associated with this service.

Arn -> (string)

The Amazon Resource Name (ARN) of the Lambda endpoint.

LastUpdatedTime -> (timestamp)

A timestamp that indicates when the service was last updated.

Name -> (string)

The name of the service.

OwnerAccountId -> (string)

The Amazon Web Services account ID of the service owner.

ServiceId -> (string)

The unique identifier of the service.

State -> (string)

The current state of the service.

Tags -> (map)

The tags assigned to the service. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key-value pair.

key -> (string)

value -> (string)

UrlEndpoint -> (structure)

The configuration for the URL endpoint type.

The **Url** isthe URL of the endpoint type.

The **HealthUrl** is the health check URL of the endpoint type.

HealthUrl -> (string)

The health check URL of the URL endpoint type.

Url -> (string)

The HTTP URL endpoint.

VpcId -> (string)

The ID of the virtual private cloud (VPC).