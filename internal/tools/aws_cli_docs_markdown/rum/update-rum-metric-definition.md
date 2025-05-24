# update-rum-metric-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/update-rum-metric-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/update-rum-metric-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rum](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rum/index.html#cli-aws-rum) ]

# update-rum-metric-definition

## Description

Modifies one existing metric definition for CloudWatch RUM extended metrics. For more information about extended metrics, see [BatchCreateRumMetricsDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricsDefinitions.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rum-2018-05-10/UpdateRumMetricDefinition)

## Synopsis

```
update-rum-metric-definition
--app-monitor-name <value>
--destination <value>
[--destination-arn <value>]
--metric-definition <value>
--metric-definition-id <value>
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

The name of the CloudWatch RUM app monitor that sends these metrics.

`--destination` (string)

The destination to send the metrics to. Valid values are `CloudWatch` and `Evidently` . If you specify `Evidently` , you must also specify the ARN of the CloudWatchEvidently experiment that will receive the metrics and an IAM role that has permission to write to the experiment.

Possible values:

- `CloudWatch`
- `Evidently`

`--destination-arn` (string)

This parameter is required if `Destination` is `Evidently` . If `Destination` is `CloudWatch` , do not use this parameter.

This parameter specifies the ARN of the Evidently experiment that is to receive the metrics. You must have already defined this experiment as a valid destination. For more information, see [PutRumMetricsDestination](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_PutRumMetricsDestination.html) .

`--metric-definition` (structure)

A structure that contains the new definition that you want to use for this metric.

DimensionKeys -> (map)

Use this field only if you are sending the metric to CloudWatch.

This field is a map of field paths to dimension names. It defines the dimensions to associate with this metric in CloudWatch. For extended metrics, valid values for the entries in this field are the following:

- `"metadata.pageId": "PageId"`
- `"metadata.browserName": "BrowserName"`
- `"metadata.deviceType": "DeviceType"`
- `"metadata.osName": "OSName"`
- `"metadata.countryCode": "CountryCode"`
- `"event_details.fileType": "FileType"`

For both extended metrics and custom metrics, all dimensions listed in this field must also be included in `EventPattern` .

key -> (string)

value -> (string)

EventPattern -> (string)

The pattern that defines the metric, specified as a JSON object. RUM checks events that happen in a userâs session against the pattern, and events that match the pattern are sent to the metric destination.

When you define extended metrics, the metric definition is not valid if `EventPattern` is omitted.

Example event patterns:

- `'{ "event_type": ["com.amazon.rum.js_error_event"], "metadata": { "browserName": [ "Chrome", "Safari" ], } }'`
- `'{ "event_type": ["com.amazon.rum.performance_navigation_event"], "metadata": { "browserName": [ "Chrome", "Firefox" ] }, "event_details": { "duration": [{ "numeric": [ "<", 2000 ] }] } }'`
- `'{ "event_type": ["com.amazon.rum.performance_navigation_event"], "metadata": { "browserName": [ "Chrome", "Safari" ], "countryCode": [ "US" ] }, "event_details": { "duration": [{ "numeric": [ ">=", 2000, "<", 8000 ] }] } }'`

If the metrics destination is `CloudWatch` and the event also matches a value in `DimensionKeys` , then the metric is published with the specified dimensions.

Name -> (string)

The name for the metric that is defined in this structure. For custom metrics, you can specify any name that you like. For extended metrics, valid values are the following:

- `PerformanceNavigationDuration`
- `PerformanceResourceDuration`
- `NavigationSatisfiedTransaction`
- `NavigationToleratedTransaction`
- `NavigationFrustratedTransaction`
- `WebVitalsCumulativeLayoutShift`
- `WebVitalsFirstInputDelay`
- `WebVitalsLargestContentfulPaint`
- `JsErrorCount`
- `HttpErrorCount`
- `SessionCount`

Namespace -> (string)

If this structure is for a custom metric instead of an extended metrics, use this parameter to define the metric namespace for that custom metric. Do not specify this parameter if this structure is for an extended metric.

You cannot use any string that starts with `AWS/` for your namespace.

UnitLabel -> (string)

The CloudWatch metric unit to use for this metric. If you omit this field, the metric is recorded with no unit.

ValueKey -> (string)

The field within the event object that the metric value is sourced from.

If you omit this field, a hardcoded value of 1 is pushed as the metric value. This is useful if you want to count the number of events that the filter catches.

If this metric is sent to CloudWatch Evidently, this field will be passed to Evidently raw. Evidently will handle data extraction from the event.

Shorthand Syntax:

```
DimensionKeys={KeyName1=string,KeyName2=string},EventPattern=string,Name=string,Namespace=string,UnitLabel=string,ValueKey=string
```

JSON Syntax:

```
{
  "DimensionKeys": {"string": "string"
    ...},
  "EventPattern": "string",
  "Name": "string",
  "Namespace": "string",
  "UnitLabel": "string",
  "ValueKey": "string"
}
```

`--metric-definition-id` (string)

The ID of the metric definition to update.

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

None