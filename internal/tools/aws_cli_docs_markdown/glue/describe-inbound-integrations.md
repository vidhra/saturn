# describe-inbound-integrationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/describe-inbound-integrations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/describe-inbound-integrations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# describe-inbound-integrations

## Description

Returns a list of inbound integrations for the specified integration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DescribeInboundIntegrations)

## Synopsis

```
describe-inbound-integrations
[--integration-arn <value>]
[--marker <value>]
[--max-records <value>]
[--target-arn <value>]
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

`--integration-arn` (string)

The Amazon Resource Name (ARN) of the integration.

`--marker` (string)

A token to specify where to start paginating. This is the marker from a previously truncated response.

`--max-records` (integer)

The total number of items to return in the output.

`--target-arn` (string)

The Amazon Resource Name (ARN) of the target resource in the integration.

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

InboundIntegrations -> (list)

A list of inbound integrations.

(structure)

A structure for an integration that writes data into a resource.

SourceArn -> (string)

The ARN of the source resource for the integration.

TargetArn -> (string)

The ARN of the target resource for the integration.

IntegrationArn -> (string)

The ARN of the zero-ETL integration.

Status -> (string)

The possible statuses are:

- CREATING: The integration is being created.
- ACTIVE: The integration creation succeeds.
- MODIFYING: The integration is being modified.
- FAILED: The integration creation fails.
- DELETING: The integration is deleted.
- SYNCING: The integration is synchronizing.
- NEEDS_ATTENTION: The integration needs attention, such as synchronization.

CreateTime -> (timestamp)

The time that the integration was created, in UTC.

IntegrationConfig -> (structure)

Properties associated with the integration.

RefreshInterval -> (string)

Specifies the frequency at which CDC (Change Data Capture) pulls or incremental loads should occur. This parameter provides flexibility to align the refresh rate with your specific data update patterns, system load considerations, and performance optimization goals. Time increment can be set from 15 minutes to 8640 minutes (six days). Currently supports creation of `RefreshInterval` only.

Errors -> (list)

A list of errors associated with the integration.

(structure)

An error associated with a zero-ETL integration.

ErrorCode -> (string)

The code associated with this error.

ErrorMessage -> (string)

A message describing the error.

Marker -> (string)

A value that indicates the starting point for the next set of response records in a subsequent request.