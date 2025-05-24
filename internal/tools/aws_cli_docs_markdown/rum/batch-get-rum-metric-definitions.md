# batch-get-rum-metric-definitionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/batch-get-rum-metric-definitions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/batch-get-rum-metric-definitions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rum](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/index.html#cli-aws-rum) ]

# batch-get-rum-metric-definitions

## Description

Retrieves the list of metrics and dimensions that a RUM app monitor is sending to a single destination.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rum-2018-05-10/BatchGetRumMetricDefinitions)

`batch-get-rum-metric-definitions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `MetricDefinitions`

## Synopsis

```
batch-get-rum-metric-definitions
--app-monitor-name <value>
--destination <value>
[--destination-arn <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

The name of the CloudWatch RUM app monitor that is sending the metrics.

`--destination` (string)

The type of destination that you want to view metrics for. Valid values are `CloudWatch` and `Evidently` .

Possible values:

- `CloudWatch`
- `Evidently`

`--destination-arn` (string)

This parameter is required if `Destination` is `Evidently` . If `Destination` is `CloudWatch` , do not use this parameter.

This parameter specifies the ARN of the Evidently experiment that corresponds to the destination.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

MetricDefinitions -> (list)

An array of structures that display information about the metrics that are sent by the specified app monitor to the specified destination.

(structure)

A structure that displays the definition of one extended metric that RUM sends to CloudWatch or CloudWatch Evidently. For more information, see [Additional metrics that you can send to CloudWatch and CloudWatch Evidently](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM-vended-metrics.html) .

DimensionKeys -> (map)

This field is a map of field paths to dimension names. It defines the dimensions to associate with this metric in CloudWatch The value of this field is used only if the metric destination is `CloudWatch` . If the metric destination is `Evidently` , the value of `DimensionKeys` is ignored.

key -> (string)

value -> (string)

EventPattern -> (string)

The pattern that defines the metric. RUM checks events that happen in a userâs session against the pattern, and events that match the pattern are sent to the metric destination.

If the metrics destination is `CloudWatch` and the event also matches a value in `DimensionKeys` , then the metric is published with the specified dimensions.

MetricDefinitionId -> (string)

The ID of this metric definition.

Name -> (string)

The name of the metric that is defined in this structure.

Namespace -> (string)

If this metric definition is for a custom metric instead of an extended metric, this field displays the metric namespace that the custom metric is published to.

UnitLabel -> (string)

Use this field only if you are sending this metric to CloudWatch. It defines the CloudWatch metric unit that this metric is measured in.

ValueKey -> (string)

The field within the event object that the metric value is sourced from.

NextToken -> (string)

A token that you can use in a subsequent operation to retrieve the next set of results.