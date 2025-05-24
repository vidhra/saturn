# describe-event-details-for-organizationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-details-for-organization.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-details-for-organization.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/index.html#cli-aws-health) ]

# describe-event-details-for-organization

## Description

Returns detailed information about one or more specified events for one or more Amazon Web Services accounts in your organization. This information includes standard event data (such as the Amazon Web Services Region and service), an event description, and (depending on the event) possible metadata. This operation doesnât return affected entities, such as the resources related to the event. To return affected entities, use the [DescribeAffectedEntitiesForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html) operation.

### Note

Before you can call this operation, you must first enable Health to work with Organizations. To do this, call the [EnableHealthServiceAccessForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_EnableHealthServiceAccessForOrganization.html) operation from your organizationâs management account.

When you call the `DescribeEventDetailsForOrganization` operation, specify the `organizationEventDetailFilters` object in the request. Depending on the Health event type, note the following differences:

- To return event details for a public event, you must specify a null value for the `awsAccountId` parameter. If you specify an account ID for a public event, Health returns an error message because public events arenât specific to an account.
- To return event details for an event that is specific to an account in your organization, you must specify the `awsAccountId` parameter in the request. If you donât specify an account ID, Health returns an error message because the event is specific to an account in your organization.

For more information, see [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html) .

### Note

This operation doesnât support resource-level permissions. You canât use this operation to allow or deny access to specific Health events. For more information, see [Resource- and action-based conditions](https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions) in the *Health User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventDetailsForOrganization)

## Synopsis

```
describe-event-details-for-organization
--organization-event-detail-filters <value>
[--locale <value>]
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

`--organization-event-detail-filters` (list)

A set of JSON elements that includes the `awsAccountId` and the `eventArn` .

(structure)

The values used to filter results from the [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html) and [DescribeAffectedEntitiesForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntitiesForOrganization.html) operations.

eventArn -> (string)

The unique identifier for the event. The event ARN has the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-details-for-organization.html#id1)arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` format.

For example, an event ARN might look like the following:

`arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`

awsAccountId -> (string)

The 12-digit Amazon Web Services account numbers that contains the affected entities.

Shorthand Syntax:

```
eventArn=string,awsAccountId=string ...
```

JSON Syntax:

```
[
  {
    "eventArn": "string",
    "awsAccountId": "string"
  }
  ...
]
```

`--locale` (string)

The locale (language) to return information in. English (en) is the default and the only supported value at this time.

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

successfulSet -> (list)

Information about the events that could be retrieved.

(structure)

Detailed information about an event. A combination of an [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html) object, an [EventDescription](https://docs.aws.amazon.com/health/latest/APIReference/API_EventDescription.html) object, and additional metadata about the event. Returned by the [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html) operation.

awsAccountId -> (string)

The 12-digit Amazon Web Services account numbers that contains the affected entities.

event -> (structure)

Summary information about an Health event.

Health events can be public or account-specific:

- *Public events* might be service events that are not specific to an Amazon Web Services account. For example, if there is an issue with an Amazon Web Services Region, Health provides information about the event, even if you donât use services or resources in that Region.
- *Account-specific* events are specific to either your Amazon Web Services account or an account in your organization. For example, if thereâs an issue with Amazon Elastic Compute Cloud in a Region that you use, Health provides information about the event and the affected resources in the account.

You can determine if an event is public or account-specific by using the `eventScopeCode` parameter. For more information, see [eventScopeCode](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html#AWSHealth-Type-Event-eventScopeCode) .

arn -> (string)

The unique identifier for the event. The event ARN has the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-details-for-organization.html#id3)arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` format.

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

eventDescription -> (structure)

The detailed description of the event. Included in the information returned by the [DescribeEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html) operation.

latestDescription -> (string)

The most recent description of the event.

eventMetadata -> (map)

Additional metadata about the event.

key -> (string)

value -> (string)

failedSet -> (list)

Error messages for any events that could not be retrieved.

(structure)

Error information returned when a [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html) operation canât find a specified event.

awsAccountId -> (string)

Error information returned when a [DescribeEventDetailsForOrganization](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetailsForOrganization.html) operation canât find a specified event.

eventArn -> (string)

The unique identifier for the event. The event ARN has the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-details-for-organization.html#id5)arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` format.

For example, an event ARN might look like the following:

`arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`

errorName -> (string)

The name of the error.

errorMessage -> (string)

A message that describes the error.

If you call the `DescribeEventDetailsForOrganization` operation and receive one of the following errors, follow the recommendations in the message:

- We couldnât find a public event that matches your request. To find an event that is account specific, you must enter an Amazon Web Services account ID in the request.
- We couldnât find an account specific event for the specified Amazon Web Services account. To find an event that is public, you must enter a null value for the Amazon Web Services account ID in the request.
- Your Amazon Web Services account doesnât include the Amazon Web Services Support plan required to use the Health API. You must have either a Business, Enterprise On-Ramp, or Enterprise Support plan.