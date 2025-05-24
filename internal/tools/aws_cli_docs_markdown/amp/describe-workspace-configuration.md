# describe-workspace-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amp/describe-workspace-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amp/describe-workspace-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [amp](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amp/index.html#cli-aws-amp) ]

# describe-workspace-configuration

## Description

Use this operation to return information about the configuration of a workspace. The configuration details returned include workspace configuration status, label set limits, and retention period.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/amp-2020-08-01/DescribeWorkspaceConfiguration)

## Synopsis

```
describe-workspace-configuration
--workspace-id <value>
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

`--workspace-id` (string)

The ID of the workspace that you want to retrieve information for. To find the IDs of your workspaces, use the [ListWorkspaces](https://docs.aws.amazon.com/prometheus/latest/APIReference/API_ListWorkspaces.htm) operation.

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

workspaceConfiguration -> (structure)

This structure contains the information about the workspace configuration.

limitsPerLabelSet -> (list)

This is an array of structures, where each structure displays one label sets for the workspace and the limits for that label set.

(structure)

This structure defines one label set used to enforce ingestion limits for the workspace, and defines the limit for that label set.

A label set is a unique combination of label-value pairs. Use them to control time series ingestion limits and to monitor usage by specific label groups. Example label sets might be `team:finance` or `env:prod`

labelSet -> (map)

This defines one label set that will have an enforced ingestion limit.

Label values accept ASCII characters and must contain at least one character that isnât whitespace. ASCII control characters are not accepted. If the label name is metric name label `__*name* __` , then the *metric* part of the name must conform to the following pattern: `[a-zA-Z_:][a-zA-Z0-9_:]*`

key -> (string)

value -> (string)

limits -> (structure)

This structure contains the information about the limits that apply to time series that match this label set.

maxSeries -> (long)

The maximum number of active series that can be ingested that match this label set.

Setting this to 0 causes no label set limit to be enforced, but it does cause Amazon Managed Service for Prometheus to vend label set metrics to CloudWatch

retentionPeriodInDays -> (integer)

This field displays how many days that metrics are retained in the workspace.

status -> (structure)

This structure displays the current status of the workspace configuration, and might also contain a reason for that status.

statusCode -> (string)

The current status of the workspace configuration.

statusReason -> (string)

The reason for the current status, if a reason is available.