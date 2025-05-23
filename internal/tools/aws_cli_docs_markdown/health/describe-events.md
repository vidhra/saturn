# describe-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/index.html#cli-aws-health) ]

# describe-events

## Description

Returns information about events that meet the specified filter criteria. Events are returned in a summary form and do not include the detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the [DescribeEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html) and [DescribeAffectedEntities](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html) operations.

If no filter criteria are specified, all events are returned. Results are sorted by `lastModifiedTime` , starting with the most recent event.

### Note

- When you call the `DescribeEvents` operation and specify an entity for the `entityValues` parameter, Health might return public events that arenât specific to that resource. For example, if you call `DescribeEvents` and specify an ID for an Amazon Elastic Compute Cloud (Amazon EC2) instance, Health might return events that arenât specific to that resource or service. To get events that are specific to a service, use the `services` parameter in the `filter` object. For more information, see [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html) .
- This API operation uses pagination. Specify the `nextToken` parameter in the next request to return more results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEvents)

`describe-events` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `events`

## Synopsis

```
describe-events
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

eventArns -> (list)

A list of event ARNs (unique identifiers). For example: `"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`

(string)

eventTypeCodes -> (list)

A list of unique identifiers for event types. For example, `"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED".`

(string)

services -> (list)

The Amazon Web Services services associated with the event. For example, `EC2` , `RDS` .

(string)

regions -> (list)

A list of Amazon Web Services Regions.

(string)

availabilityZones -> (list)

A list of Amazon Web Services Availability Zones.

(string)

startTimes -> (list)

A list of dates and times that the event began.

(structure)

A range of dates and times that is used by the [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html) and [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html) objects. If `from` is set and `to` is set: match items where the timestamp (`startTime` , `endTime` , or `lastUpdatedTime` ) is between `from` and `to` inclusive. If `from` is set and `to` is not set: match items where the timestamp value is equal to or after `from` . If `from` is not set and `to` is set: match items where the timestamp value is equal to or before `to` .

from -> (timestamp)

The starting date and time of a time range.

to -> (timestamp)

The ending date and time of a time range.

endTimes -> (list)

A list of dates and times that the event ended.

(structure)

A range of dates and times that is used by the [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html) and [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html) objects. If `from` is set and `to` is set: match items where the timestamp (`startTime` , `endTime` , or `lastUpdatedTime` ) is between `from` and `to` inclusive. If `from` is set and `to` is not set: match items where the timestamp value is equal to or after `from` . If `from` is not set and `to` is set: match items where the timestamp value is equal to or before `to` .

from -> (timestamp)

The starting date and time of a time range.

to -> (timestamp)

The ending date and time of a time range.

lastUpdatedTimes -> (list)

A list of dates and times that the event was last updated.

(structure)

A range of dates and times that is used by the [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html) and [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html) objects. If `from` is set and `to` is set: match items where the timestamp (`startTime` , `endTime` , or `lastUpdatedTime` ) is between `from` and `to` inclusive. If `from` is set and `to` is not set: match items where the timestamp value is equal to or after `from` . If `from` is not set and `to` is set: match items where the timestamp value is equal to or before `to` .

from -> (timestamp)

The starting date and time of a time range.

to -> (timestamp)

The ending date and time of a time range.

entityArns -> (list)

A list of entity ARNs (unique identifiers).

(string)

entityValues -> (list)

A list of entity identifiers, such as EC2 instance IDs (`i-34ab692e` ) or EBS volumes (`vol-426ab23e` ).

(string)

eventTypeCategories -> (list)

A list of event type category codes. Possible values are `issue` , `accountNotification` , or `scheduledChange` . Currently, the `investigation` value isnât supported at this time.

(string)

tags -> (list)

A map of entity tags attached to the affected entity.

### Note

Currently, the `tags` property isnât supported.

(map)

key -> (string)

value -> (string)

eventStatusCodes -> (list)

A list of event status codes.

(string)

Shorthand Syntax:

```
eventArns=string,string,eventTypeCodes=string,string,services=string,string,regions=string,string,availabilityZones=string,string,startTimes=[{from=timestamp,to=timestamp},{from=timestamp,to=timestamp}],endTimes=[{from=timestamp,to=timestamp},{from=timestamp,to=timestamp}],lastUpdatedTimes=[{from=timestamp,to=timestamp},{from=timestamp,to=timestamp}],entityArns=string,string,entityValues=string,string,eventTypeCategories=string,string,tags=[{KeyName1=string,KeyName2=string},{KeyName1=string,KeyName2=string}],eventStatusCodes=string,string
```

JSON Syntax:

```
{
  "eventArns": ["string", ...],
  "eventTypeCodes": ["string", ...],
  "services": ["string", ...],
  "regions": ["string", ...],
  "availabilityZones": ["string", ...],
  "startTimes": [
    {
      "from": timestamp,
      "to": timestamp
    }
    ...
  ],
  "endTimes": [
    {
      "from": timestamp,
      "to": timestamp
    }
    ...
  ],
  "lastUpdatedTimes": [
    {
      "from": timestamp,
      "to": timestamp
    }
    ...
  ],
  "entityArns": ["string", ...],
  "entityValues": ["string", ...],
  "eventTypeCategories": ["issue"|"accountNotification"|"scheduledChange"|"investigation", ...],
  "tags": [
    {"string": "string"
      ...}
    ...
  ],
  "eventStatusCodes": ["open"|"closed"|"upcoming", ...]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To list AWS Health events**

The following `describe-events` example lists recent AWS Health events.

```
aws health describe-events \
    --region us-east-1
```

Output:

```
{
    "events": [
        {
            "arn": "arn:aws:health:us-west-1::event/ECS/AWS_ECS_OPERATIONAL_ISSUE/AWS_ECS_OPERATIONAL_ISSUE_KWQPY_EXAMPLE111",
            "service": "ECS",
            "eventTypeCode": "AWS_ECS_OPERATIONAL_ISSUE",
            "eventTypeCategory": "issue",
            "region": "us-west-1",
            "startTime": 1589077890.53,
            "endTime": 1589086345.597,
            "lastUpdatedTime": 1589086345.905,
            "statusCode": "closed",
            "eventScopeCode": "PUBLIC"
        },
        {
            "arn": "arn:aws:health:global::event/BILLING/AWS_BILLING_NOTIFICATION/AWS_BILLING_NOTIFICATION_6ce1d874-e995-40e2-99cd-EXAMPLE1118b",
            "service": "BILLING",
            "eventTypeCode": "AWS_BILLING_NOTIFICATION",
            "eventTypeCategory": "accountNotification",
            "region": "global",
            "startTime": 1588356000.0,
            "lastUpdatedTime": 1588356524.358,
            "statusCode": "open",
            "eventScopeCode": "ACCOUNT_SPECIFIC"
        },
        {
            "arn": "arn:aws:health:us-west-2::event/CLOUDFORMATION/AWS_CLOUDFORMATION_OPERATIONAL_ISSUE/AWS_CLOUDFORMATION_OPERATIONAL_ISSUE_OHTWY_EXAMPLE111",
            "service": "CLOUDFORMATION",
            "eventTypeCode": "AWS_CLOUDFORMATION_OPERATIONAL_ISSUE",
            "eventTypeCategory": "issue",
            "region": "us-west-2",
            "startTime": 1588279630.761,
            "endTime": 1588284650.0,
            "lastUpdatedTime": 1588284691.941,
            "statusCode": "closed",
            "eventScopeCode": "PUBLIC"
        },
        {
            "arn": "arn:aws:health:ap-northeast-1::event/LAMBDA/AWS_LAMBDA_OPERATIONAL_ISSUE/AWS_LAMBDA_OPERATIONAL_ISSUE_JZDND_EXAMPLE111",
            "service": "LAMBDA",
            "eventTypeCode": "AWS_LAMBDA_OPERATIONAL_ISSUE",
            "eventTypeCategory": "issue",
            "region": "ap-northeast-1",
            "startTime": 1587379534.08,
            "endTime": 1587391771.0,
            "lastUpdatedTime": 1587395689.316,
            "statusCode": "closed",
            "eventScopeCode": "PUBLIC"
        },
        {
            "arn": "arn:aws:health:us-east-1::event/EC2/AWS_EC2_OPERATIONAL_ISSUE/AWS_EC2_OPERATIONAL_ISSUE_COBXJ_EXAMPLE111",
            "service": "EC2",
            "eventTypeCode": "AWS_EC2_OPERATIONAL_ISSUE",
            "eventTypeCategory": "issue",
            "region": "us-east-1",
            "startTime": 1586473044.284,
            "endTime": 1586479706.091,
            "lastUpdatedTime": 1586479706.153,
            "statusCode": "closed",
            "eventScopeCode": "PUBLIC"
        },
        {
            "arn": "arn:aws:health:global::event/SECURITY/AWS_SECURITY_NOTIFICATION/AWS_SECURITY_NOTIFICATION_42007387-8129-42da-8c88-EXAMPLE11139",
            "service": "SECURITY",
            "eventTypeCode": "AWS_SECURITY_NOTIFICATION",
            "eventTypeCategory": "accountNotification",
            "region": "global",
            "startTime": 1585674000.0,
            "lastUpdatedTime": 1585674004.132,
            "statusCode": "open",
            "eventScopeCode": "PUBLIC"
        },
        {
            "arn": "arn:aws:health:global::event/CLOUDFRONT/AWS_CLOUDFRONT_OPERATIONAL_ISSUE/AWS_CLOUDFRONT_OPERATIONAL_ISSUE_FRQXG_EXAMPLE111",
            "service": "CLOUDFRONT",
            "eventTypeCode": "AWS_CLOUDFRONT_OPERATIONAL_ISSUE",
            "eventTypeCategory": "issue",
            "region": "global",
            "startTime": 1585610898.589,
            "endTime": 1585617671.0,
            "lastUpdatedTime": 1585620638.869,
            "statusCode": "closed",
            "eventScopeCode": "PUBLIC"
        },
        {
            "arn": "arn:aws:health:us-east-1::event/SES/AWS_SES_OPERATIONAL_ISSUE/AWS_SES_OPERATIONAL_ISSUE_URNDF_EXAMPLE111",
            "service": "SES",
            "eventTypeCode": "AWS_SES_OPERATIONAL_ISSUE",
            "eventTypeCategory": "issue",
            "region": "us-east-1",
            "startTime": 1585342008.46,
            "endTime": 1585344017.0,
            "lastUpdatedTime": 1585344355.989,
            "statusCode": "closed",
            "eventScopeCode": "PUBLIC"
        },
        {
            "arn": "arn:aws:health:global::event/IAM/AWS_IAM_OPERATIONAL_NOTIFICATION/AWS_IAM_OPERATIONAL_NOTIFICATION_b6771c34-6ecd-4aea-9d3e-EXAMPLE1117e",
            "service": "IAM",
            "eventTypeCode": "AWS_IAM_OPERATIONAL_NOTIFICATION",
            "eventTypeCategory": "accountNotification",
            "region": "global",
            "startTime": 1584978300.0,
            "lastUpdatedTime": 1584978553.572,
            "statusCode": "open",
            "eventScopeCode": "ACCOUNT_SPECIFIC"
        },
        {
            "arn": "arn:aws:health:ap-southeast-2::event/EC2/AWS_EC2_OPERATIONAL_ISSUE/AWS_EC2_OPERATIONAL_ISSUE_HNGHE_EXAMPLE111",
            "service": "EC2",
            "eventTypeCode": "AWS_EC2_OPERATIONAL_ISSUE",
            "eventTypeCategory": "issue",
            "region": "ap-southeast-2",
            "startTime": 1583881487.483,
            "endTime": 1583885056.785,
            "lastUpdatedTime": 1583885057.052,
            "statusCode": "closed",
            "eventScopeCode": "PUBLIC"
        }
    ]
}
```

For more information, see [Getting started with the AWS Personal Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-phd.html) in the *AWS Health User Guide*.

**Example 2: To list AWS Health events by service and event status code**

The following `describe-events` example lists AWS Health events for Amazon Elastic Compute Cloud (Amazon EC2) where the event status is closed.

```
aws health describe-events \
    --filter "services=EC2,eventStatusCodes=closed"
```

Output:

```
{
    "events": [
        {
            "arn": "arn:aws:health:us-east-1::event/EC2/AWS_EC2_OPERATIONAL_ISSUE/AWS_EC2_OPERATIONAL_ISSUE_VKTXI_EXAMPLE111",
            "service": "EC2",
            "eventTypeCode": "AWS_EC2_OPERATIONAL_ISSUE",
            "eventTypeCategory": "issue",
            "region": "us-east-1",
            "startTime": 1587462325.096,
            "endTime": 1587464204.774,
            "lastUpdatedTime": 1587464204.865,
            "statusCode": "closed",
            "eventScopeCode": "PUBLIC"
        },
        {
            "arn": "arn:aws:health:us-east-1::event/EC2/AWS_EC2_OPERATIONAL_ISSUE/AWS_EC2_OPERATIONAL_ISSUE_COBXJ_EXAMPLE111",
            "service": "EC2",
            "eventTypeCode": "AWS_EC2_OPERATIONAL_ISSUE",
            "eventTypeCategory": "issue",
            "region": "us-east-1",
            "startTime": 1586473044.284,
            "endTime": 1586479706.091,
            "lastUpdatedTime": 1586479706.153,
            "statusCode": "closed",
            "eventScopeCode": "PUBLIC"
        },
        {
            "arn": "arn:aws:health:ap-southeast-2::event/EC2/AWS_EC2_OPERATIONAL_ISSUE/AWS_EC2_OPERATIONAL_ISSUE_HNGHE_EXAMPLE111",
            "service": "EC2",
            "eventTypeCode": "AWS_EC2_OPERATIONAL_ISSUE",
            "eventTypeCategory": "issue",
            "region": "ap-southeast-2",
            "startTime": 1583881487.483,
            "endTime": 1583885056.785,
            "lastUpdatedTime": 1583885057.052,
            "statusCode": "closed",
            "eventScopeCode": "PUBLIC"
        }
    ]
}
```

For more information, see [Getting started with the AWS Personal Health Dashboard](https://docs.aws.amazon.com/health/latest/ug/getting-started-phd.html) in the *AWS Health User Guide*.

## Output

events -> (list)

The events that match the specified filter criteria.

(structure)

Summary information about an Health event.

Health events can be public or account-specific:

- *Public events* might be service events that are not specific to an Amazon Web Services account. For example, if there is an issue with an Amazon Web Services Region, Health provides information about the event, even if you donât use services or resources in that Region.
- *Account-specific* events are specific to either your Amazon Web Services account or an account in your organization. For example, if thereâs an issue with Amazon Elastic Compute Cloud in a Region that you use, Health provides information about the event and the affected resources in the account.

You can determine if an event is public or account-specific by using the `eventScopeCode` parameter. For more information, see [eventScopeCode](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html#AWSHealth-Type-Event-eventScopeCode) .

arn -> (string)

The unique identifier for the event. The event ARN has the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-events.html#id1)arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` format.

For example, an event ARN might look like the following:

`arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`

service -> (string)

The Amazon Web Services service that is affected by the event. For example, `EC2` , `RDS` .

eventTypeCode -> (string)

The unique identifier for the event type. The format is `AWS_*SERVICE* _*DESCRIPTION* `` ; for example, ``AWS_EC2_SYSTEM_MAINTENANCE_EVENT` .

eventTypeCategory -> (string)

A list of event type category codes. Possible values are `issue` , `accountNotification` , or `scheduledChange` . Currently, the `investigation` value isnât supported at this time.

region -> (string)

The Amazon Web Services Region name of the event.

availabilityZone -> (string)

The Amazon Web Services Availability Zone of the event. For example, us-east-1a.

startTime -> (timestamp)

The date and time that the event began.

endTime -> (timestamp)

The date and time that the event ended.

lastUpdatedTime -> (timestamp)

The most recent date and time that the event was updated.

statusCode -> (string)

The most recent status of the event. Possible values are `open` , `closed` , and `upcoming` .

eventScopeCode -> (string)

This parameter specifies if the Health event is a public Amazon Web Services service event or an account-specific event.

- If the `eventScopeCode` value is `PUBLIC` , then the `affectedAccounts` value is always empty.
- If the `eventScopeCode` value is `ACCOUNT_SPECIFIC` , then the `affectedAccounts` value lists the affected Amazon Web Services accounts in your organization. For example, if an event affects a service such as Amazon Elastic Compute Cloud and you have Amazon Web Services accounts that use that service, those account IDs appear in the response.
- If the `eventScopeCode` value is `NONE` , then the `eventArn` that you specified in the request is invalid or doesnât exist.

nextToken -> (string)

If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.