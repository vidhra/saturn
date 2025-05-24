# describe-event-typesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-types.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-types.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/index.html#cli-aws-health) ]

# describe-event-types

## Description

Returns the event types that meet the specified filter criteria. You can use this API operation to find information about the Health event, such as the category, Amazon Web Services service, and event code. The metadata for each event appears in the [EventType](https://docs.aws.amazon.com/health/latest/APIReference/API_EventType.html) object.

If you donât specify a filter criteria, the API operation returns all event types, in no particular order.

### Note

This API operation uses pagination. Specify the `nextToken` parameter in the next request to return more results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventTypes)

`describe-event-types` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `eventTypes`

## Synopsis

```
describe-event-types
[--filter <value>]
[--locale <value>]
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

`--filter` (structure)

Values to narrow the results returned.

eventTypeCodes -> (list)

A list of event type codes.

(string)

services -> (list)

The Amazon Web Services services associated with the event. For example, `EC2` , `RDS` .

(string)

eventTypeCategories -> (list)

A list of event type category codes. Possible values are `issue` , `accountNotification` , or `scheduledChange` . Currently, the `investigation` value isnât supported at this time.

(string)

Shorthand Syntax:

```
eventTypeCodes=string,string,services=string,string,eventTypeCategories=string,string
```

JSON Syntax:

```
{
  "eventTypeCodes": ["string", ...],
  "services": ["string", ...],
  "eventTypeCategories": ["issue"|"accountNotification"|"scheduledChange"|"investigation", ...]
}
```

`--locale` (string)

The locale (language) to return information in. English (en) is the default and the only supported value at this time.

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

eventTypes -> (list)

A list of event types that match the filter criteria. Event types have a category (`issue` , `accountNotification` , or `scheduledChange` ), a service (for example, `EC2` , `RDS` , `DATAPIPELINE` , `BILLING` ), and a code (in the format `AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT` ).

(structure)

Contains the metadata about a type of event that is reported by Health. The `EventType` shows the category, service, and the event type code of the event. For example, an `issue` might be the category, `EC2` the service, and `AWS_EC2_SYSTEM_MAINTENANCE_EVENT` the event type code.

You can use the [DescribeEventTypes](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventTypes.html) API operation to return this information about an event.

You can also use the Amazon CloudWatch Events console to create a rule so that you can get notified or take action when Health delivers a specific event to your Amazon Web Services account. For more information, see [Monitor for Health events with Amazon CloudWatch Events](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) in the *Health User Guide* .

service -> (string)

The Amazon Web Services service that is affected by the event. For example, `EC2` , `RDS` .

code -> (string)

The unique identifier for the event type. The format is `AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT` .

category -> (string)

A list of event type category codes. Possible values are `issue` , `accountNotification` , or `scheduledChange` . Currently, the `investigation` value isnât supported at this time.

nextToken -> (string)

If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.