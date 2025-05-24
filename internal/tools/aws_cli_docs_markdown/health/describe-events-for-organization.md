# describe-events-for-organizationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-events-for-organization.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-events-for-organization.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/index.html#cli-aws-health) ]

# describe-events-for-organization

## Description

Returns information about events across your organization in Organizations. You can use the``filters`` parameter to specify the events that you want to return. Events are returned in a summary form and donât include the affected accounts, detailed description, any additional metadata that depends on the event type, or any affected resources. To retrieve that information, use the following operations:

- [DescribeAffectedAccountsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedAccountsForOrganization.html)
- [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html)
- [DescribeAffectedEntitiesForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html)

If you donât specify a `filter` , the `DescribeEventsForOrganizations` returns all events across your organization. Results are sorted by `lastModifiedTime` , starting with the most recent event.

For more information about the different types of Health events, see [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html) .

Before you can call this operation, you must first enable Health to work with Organizations. To do this, call the [EnableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html) operation from your organizationâs management account.

### Note

This API operation uses pagination. Specify the `nextToken` parameter in the next request to return more results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventsForOrganization)

`describe-events-for-organization` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `events`

## Synopsis

```
describe-events-for-organization
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

A list of unique identifiers for event types. For example, `"AWS_EC2_SYSTEM_MAINTENANCE_EVENT","AWS_RDS_MAINTENANCE_SCHEDULED".`

(string)

awsAccountIds -> (list)

A list of 12-digit Amazon Web Services account numbers that contains the affected entities.

(string)

services -> (list)

The Amazon Web Services services associated with the event. For example, `EC2` , `RDS` .

(string)

regions -> (list)

A list of Amazon Web Services Regions.

(string)

startTime -> (structure)

A range of dates and times that is used by the [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html) and [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html) objects. If `from` is set and `to` is set: match items where the timestamp (`startTime` , `endTime` , or `lastUpdatedTime` ) is between `from` and `to` inclusive. If `from` is set and `to` is not set: match items where the timestamp value is equal to or after `from` . If `from` is not set and `to` is set: match items where the timestamp value is equal to or before `to` .

from -> (timestamp)

The starting date and time of a time range.

to -> (timestamp)

The ending date and time of a time range.

endTime -> (structure)

A range of dates and times that is used by the [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html) and [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html) objects. If `from` is set and `to` is set: match items where the timestamp (`startTime` , `endTime` , or `lastUpdatedTime` ) is between `from` and `to` inclusive. If `from` is set and `to` is not set: match items where the timestamp value is equal to or after `from` . If `from` is not set and `to` is set: match items where the timestamp value is equal to or before `to` .

from -> (timestamp)

The starting date and time of a time range.

to -> (timestamp)

The ending date and time of a time range.

lastUpdatedTime -> (structure)

A range of dates and times that is used by the [EventFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EventFilter.html) and [EntityFilter](https://docs.aws.amazon.com/health/latest/APIReference/API_EntityFilter.html) objects. If `from` is set and `to` is set: match items where the timestamp (`startTime` , `endTime` , or `lastUpdatedTime` ) is between `from` and `to` inclusive. If `from` is set and `to` is not set: match items where the timestamp value is equal to or after `from` . If `from` is not set and `to` is set: match items where the timestamp value is equal to or before `to` .

from -> (timestamp)

The starting date and time of a time range.

to -> (timestamp)

The ending date and time of a time range.

entityArns -> (list)

A list of entity ARNs (unique identifiers).

(string)

entityValues -> (list)

A list of entity identifiers, such as EC2 instance IDs (i-34ab692e) or EBS volumes (vol-426ab23e).

(string)

eventTypeCategories -> (list)

A list of event type category codes. Possible values are `issue` , `accountNotification` , or `scheduledChange` . Currently, the `investigation` value isnât supported at this time.

(string)

eventStatusCodes -> (list)

A list of event status codes.

(string)

Shorthand Syntax:

```
eventTypeCodes=string,string,awsAccountIds=string,string,services=string,string,regions=string,string,startTime={from=timestamp,to=timestamp},endTime={from=timestamp,to=timestamp},lastUpdatedTime={from=timestamp,to=timestamp},entityArns=string,string,entityValues=string,string,eventTypeCategories=string,string,eventStatusCodes=string,string
```

JSON Syntax:

```
{
  "eventTypeCodes": ["string", ...],
  "awsAccountIds": ["string", ...],
  "services": ["string", ...],
  "regions": ["string", ...],
  "startTime": {
    "from": timestamp,
    "to": timestamp
  },
  "endTime": {
    "from": timestamp,
    "to": timestamp
  },
  "lastUpdatedTime": {
    "from": timestamp,
    "to": timestamp
  },
  "entityArns": ["string", ...],
  "entityValues": ["string", ...],
  "eventTypeCategories": ["issue"|"accountNotification"|"scheduledChange"|"investigation", ...],
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

## Output

events -> (list)

The events that match the specified filter criteria.

(structure)

Summary information about an event, returned by the [DescribeEventsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventsForOrganization.html) operation.

arn -> (string)

The unique identifier for the event. The event ARN has the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-events-for-organization.html#id1)arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` format.

For example, an event ARN might look like the following:

`arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`

service -> (string)

The Amazon Web Services service that is affected by the event, such as EC2 and RDS.

eventTypeCode -> (string)

The unique identifier for the event type. The format is `AWS_SERVICE_DESCRIPTION` . For example, `AWS_EC2_SYSTEM_MAINTENANCE_EVENT` .

eventTypeCategory -> (string)

A list of event type category codes. Possible values are `issue` , `accountNotification` , or `scheduledChange` . Currently, the `investigation` value isnât supported at this time.

eventScopeCode -> (string)

This parameter specifies if the Health event is a public Amazon Web Services service event or an account-specific event.

- If the `eventScopeCode` value is `PUBLIC` , then the `affectedAccounts` value is always empty.
- If the `eventScopeCode` value is `ACCOUNT_SPECIFIC` , then the `affectedAccounts` value lists the affected Amazon Web Services accounts in your organization. For example, if an event affects a service such as Amazon Elastic Compute Cloud and you have Amazon Web Services accounts that use that service, those account IDs appear in the response.
- If the `eventScopeCode` value is `NONE` , then the `eventArn` that you specified in the request is invalid or doesnât exist.

region -> (string)

The Amazon Web Services Region name of the event.

startTime -> (timestamp)

The date and time that the event began.

endTime -> (timestamp)

The date and time that the event ended.

lastUpdatedTime -> (timestamp)

The most recent date and time that the event was updated.

statusCode -> (string)

The most recent status of the event. Possible values are `open` , `closed` , and `upcoming` .

nextToken -> (string)

If the results of a search are large, only a portion of the results are returned, and a `nextToken` pagination token is returned in the response. To retrieve the next batch of results, reissue the search request and include the returned token. When all results have been returned, the response does not contain a pagination token value.