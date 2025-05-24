# create-usage-limitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/create-usage-limit.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/create-usage-limit.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift-serverless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-serverless/index.html#cli-aws-redshift-serverless) ]

# create-usage-limit

## Description

Creates a usage limit for a specified Amazon Redshift Serverless usage type. The usage limit is identified by the returned usage limit identifier.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-serverless-2021-04-21/CreateUsageLimit)

## Synopsis

```
create-usage-limit
--amount <value>
[--breach-action <value>]
[--period <value>]
--resource-arn <value>
--usage-type <value>
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

`--amount` (long)

The limit amount. If time-based, this amount is in Redshift Processing Units (RPU) consumed per hour. If data-based, this amount is in terabytes (TB) of data transferred between Regions in cross-account sharing. The value must be a positive number.

`--breach-action` (string)

The action that Amazon Redshift Serverless takes when the limit is reached. The default is log.

Possible values:

- `log`
- `emit-metric`
- `deactivate`

`--period` (string)

The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly.

Possible values:

- `daily`
- `weekly`
- `monthly`

`--resource-arn` (string)

The Amazon Resource Name (ARN) of the Amazon Redshift Serverless resource to create the usage limit for.

`--usage-type` (string)

The type of Amazon Redshift Serverless usage to create a usage limit for.

Possible values:

- `serverless-compute`
- `cross-region-datasharing`

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

usageLimit -> (structure)

The returned usage limit object.

amount -> (long)

The limit amount. If time-based, this amount is in RPUs consumed per hour. If data-based, this amount is in terabytes (TB). The value must be a positive number.

breachAction -> (string)

The action that Amazon Redshift Serverless takes when the limit is reached.

period -> (string)

The time period that the amount applies to. A weekly period begins on Sunday. The default is monthly.

resourceArn -> (string)

The Amazon Resource Name (ARN) that identifies the Amazon Redshift Serverless resource.

usageLimitArn -> (string)

The Amazon Resource Name (ARN) of the resource associated with the usage limit.

usageLimitId -> (string)

The identifier of the usage limit.

usageType -> (string)

The Amazon Redshift Serverless feature to limit.