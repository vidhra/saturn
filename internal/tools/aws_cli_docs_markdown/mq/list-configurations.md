# list-configurationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-configurations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/list-configurations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mq](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mq/index.html#cli-aws-mq) ]

# list-configurations

## Description

Returns a list of all configurations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mq-2017-11-27/ListConfigurations)

## Synopsis

```
list-configurations
[--max-results <value>]
[--next-token <value>]
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

`--max-results` (integer)

The maximum number of brokers that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.

`--next-token` (string)

The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.

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

Configurations -> (list)

The list of all revisions for the specified configuration.

(structure)

Returns information about all configurations.

Arn -> (string)

Required. The ARN of the configuration.

AuthenticationStrategy -> (string)

Optional. The authentication strategy associated with the configuration. The default is SIMPLE.

Created -> (timestamp)

Required. The date and time of the configuration revision.

Description -> (string)

Required. The description of the configuration.

EngineType -> (string)

Required. The type of broker engine. Currently, Amazon MQ supports ACTIVEMQ and RABBITMQ.

EngineVersion -> (string)

The broker engine version. Defaults to the latest available version for the specified broker engine type. For a list of supported engine versions, see the [ActiveMQ version management](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/activemq-version-management.html) and the [RabbitMQ version management](https://docs.aws.amazon.com//amazon-mq/latest/developer-guide/rabbitmq-version-management.html) sections in the Amazon MQ Developer Guide.

Id -> (string)

Required. The unique ID that Amazon MQ generates for the configuration.

LatestRevision -> (structure)

Required. The latest revision of the configuration.

Created -> (timestamp)

Required. The date and time of the configuration revision.

Description -> (string)

The description of the configuration revision.

Revision -> (integer)

Required. The revision number of the configuration.

Name -> (string)

Required. The name of the configuration. This value can contain only alphanumeric characters, dashes, periods, underscores, and tildes (- . _ ~). This value must be 1-150 characters long.

Tags -> (map)

The list of all tags associated with this configuration.

key -> (string)

value -> (string)

MaxResults -> (integer)

The maximum number of configurations that Amazon MQ can return per page (20 by default). This value must be an integer from 5 to 100.

NextToken -> (string)

The token that specifies the next page of results Amazon MQ should return. To request the first page, leave nextToken empty.