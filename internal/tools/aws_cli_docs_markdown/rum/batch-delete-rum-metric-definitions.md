# batch-delete-rum-metric-definitionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/batch-delete-rum-metric-definitions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/batch-delete-rum-metric-definitions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rum](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/index.html#cli-aws-rum) ]

# batch-delete-rum-metric-definitions

## Description

Removes the specified metrics from being sent to an extended metrics destination.

If some metric definition IDs specified in a `BatchDeleteRumMetricDefinitions` operations are not valid, those metric definitions fail and return errors, but all valid metric definition IDs in the same operation are still deleted.

The maximum number of metric definitions that you can specify in one `BatchDeleteRumMetricDefinitions` operation is 200.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rum-2018-05-10/BatchDeleteRumMetricDefinitions)

## Synopsis

```
batch-delete-rum-metric-definitions
--app-monitor-name <value>
--destination <value>
[--destination-arn <value>]
--metric-definition-ids <value>
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

`--app-monitor-name` (string)

The name of the CloudWatch RUM app monitor that is sending these metrics.

`--destination` (string)

Defines the destination where you want to stop sending the specified metrics. Valid values are `CloudWatch` and `Evidently` . If you specify `Evidently` , you must also specify the ARN of the CloudWatchEvidently experiment that is to be the destination and an IAM role that has permission to write to the experiment.

Possible values:

- `CloudWatch`
- `Evidently`

`--destination-arn` (string)

This parameter is required if `Destination` is `Evidently` . If `Destination` is `CloudWatch` , do not use this parameter.

This parameter specifies the ARN of the Evidently experiment that was receiving the metrics that are being deleted.

`--metric-definition-ids` (list)

An array of structures which define the metrics that you want to stop sending.

(string)

Syntax:

```
"string" "string" ...
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

## Output

Errors -> (list)

An array of error objects, if the operation caused any errors.

(structure)

A structure that defines one error caused by a [BatchCreateRumMetricsDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricsDefinitions.html) operation.

ErrorCode -> (string)

The error code.

ErrorMessage -> (string)

The error message for this metric definition.

MetricDefinitionId -> (string)

The ID of the metric definition that caused this error.

MetricDefinitionIds -> (list)

The IDs of the metric definitions that were deleted.

(string)