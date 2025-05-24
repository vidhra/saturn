# describe-configuration-templatesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-configuration-templates.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-configuration-templates.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# describe-configuration-templates

## Description

Use this operation to return the valid and default values that are used when creating delivery sources, delivery destinations, and deliveries. For more information about deliveries, see [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeConfigurationTemplates)

`describe-configuration-templates` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `configurationTemplates`

## Synopsis

```
describe-configuration-templates
[--service <value>]
[--log-types <value>]
[--resource-types <value>]
[--delivery-destination-types <value>]
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

`--service` (string)

Use this parameter to filter the response to include only the configuration templates that apply to the Amazon Web Services service that you specify here.

`--log-types` (list)

Use this parameter to filter the response to include only the configuration templates that apply to the log types that you specify here.

(string)

Syntax:

```
"string" "string" ...
```

`--resource-types` (list)

Use this parameter to filter the response to include only the configuration templates that apply to the resource types that you specify here.

(string)

Syntax:

```
"string" "string" ...
```

`--delivery-destination-types` (list)

Use this parameter to filter the response to include only the configuration templates that apply to the delivery destination types that you specify here.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  S3
  CWL
  FH
```

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

configurationTemplates -> (list)

An array of objects, where each object describes one configuration template that matches the filters that you specified in the request.

(structure)

A structure containing information about the deafult settings and available settings that you can use to configure a [delivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_Delivery.html) or a [delivery destination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeliveryDestination.html) .

service -> (string)

A string specifying which service this configuration template applies to. For more information about supported services see [Enable logging from Amazon Web Services services.](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.html) .

logType -> (string)

A string specifying which log type this configuration template applies to.

resourceType -> (string)

A string specifying which resource type this configuration template applies to.

deliveryDestinationType -> (string)

A string specifying which destination type this configuration template applies to.

defaultDeliveryConfigValues -> (structure)

A mapping that displays the default value of each property within a deliveryâs configuration, if it is not specified in the request.

recordFields -> (list)

The default record fields that will be delivered when a list of record fields is not provided in a [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) operation.

(string)

fieldDelimiter -> (string)

The default field delimiter that is used in a [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) operation when the field delimiter is not specified in that operation. The field delimiter is used only when the final output delivery is in `Plain` , `W3C` , or `Raw` format.

s3DeliveryConfiguration -> (structure)

The delivery parameters that are used when you create a delivery to a delivery destination that is an S3 Bucket.

suffixPath -> (string)

This string allows re-configuring the S3 object prefix to contain either static or variable sections. The valid variables to use in the suffix path will vary by each log source. To find the values supported for the suffix path for each log source, use the [DescribeConfigurationTemplates](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DescribeConfigurationTemplates.html) operation and check the `allowedSuffixPathFields` field in the response.

enableHiveCompatiblePath -> (boolean)

This parameter causes the S3 objects that contain delivered logs to use a prefix structure that allows for integration with Apache Hive.

allowedFields -> (list)

The allowed fields that a caller can use in the `recordFields` parameter of a [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) or [UpdateDeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html) operation.

(structure)

A structure that represents a valid record field header and whether it is mandatory.

name -> (string)

The name to use when specifying this record field in a [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) or [UpdateDeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html) operation.

mandatory -> (boolean)

If this is `true` , the record field must be present in the `recordFields` parameter provided to a [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) or [UpdateDeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html) operation.

allowedOutputFormats -> (list)

The list of delivery destination output formats that are supported by this log source.

(string)

allowedActionForAllowVendedLogsDeliveryForResource -> (string)

The action permissions that a caller needs to have to be able to successfully create a delivery source on the desired resource type when calling [PutDeliverySource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.html) .

allowedFieldDelimiters -> (list)

The valid values that a caller can use as field delimiters when calling [CreateDelivery](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.html) or [UpdateDeliveryConfiguration](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UpdateDeliveryConfiguration.html) on a delivery that delivers in `Plain` , `W3C` , or `Raw` format.

(string)

allowedSuffixPathFields -> (list)

The list of variable fields that can be used in the suffix path of a delivery that delivers to an S3 bucket.

(string)

nextToken -> (string)

The token for the next set of items to return. The token expires after 24 hours.