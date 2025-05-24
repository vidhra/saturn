# describe-event-detailsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-details.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-details.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [health](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/index.html#cli-aws-health) ]

# describe-event-details

## Description

Returns detailed information about one or more specified events. Information includes standard event data (Amazon Web Services Region, service, and so on, as returned by [DescribeEvents](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEvents.html) ), a detailed event description, and possible additional metadata that depends upon the nature of the event. Affected entities are not included. To retrieve the entities, use the [DescribeAffectedEntities](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeAffectedEntities.html) operation.

If a specified event canât be retrieved, an error message is returned for that event.

### Note

This operation supports resource-level permissions. You can use this operation to allow or deny access to specific Health events. For more information, see [Resource- and action-based conditions](https://docs.aws.amazon.com/health/latest/ug/security_iam_id-based-policy-examples.html#resource-action-based-conditions) in the *Health User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/health-2016-08-04/DescribeEventDetails)

## Synopsis

```
describe-event-details
--event-arns <value>
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

`--event-arns` (list)

A list of event ARNs (unique identifiers). For example: `"arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-CDE456", "arn:aws:health:us-west-1::event/EBS/AWS_EBS_LOST_VOLUME/AWS_EBS_LOST_VOLUME_CHI789_JKL101"`

(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list information about an AWS Health event**

The following `describe-event-details` example lists information about the specified AWS Health event.

```
aws health describe-event-details \
    --event-arns "arn:aws:health:us-east-1::event/EC2/AWS_EC2_OPERATIONAL_ISSUE/AWS_EC2_OPERATIONAL_ISSUE_VKTXI_EXAMPLE111" \
    --region us-east-1
```

Output:

```
{
    "successfulSet": [
        {
            "event": {
                "arn": "arn:aws:health:us-east-1::event/EC2/AWS_EC2_OPERATIONAL_ISSUE/AWS_EC2_OPERATIONAL_ISSUE_VKTXI_EXAMPLE111",
                "service": "EC2",
                "eventTypeCode": "AWS_EC2_OPERATIONAL_ISSUE",
                "eventTypeCategory": "issue",
                "region": "us-east-1",
                "startTime": 1587462325.096,
                "endTime": 1587464204.774,
                "lastUpdatedTime": 1587464204.865,
                "statusCode": "closed"
            },
            "eventDescription": {
                "latestDescription": "[RESOLVED] Increased API Error Rates and Latencies\n\n[02:45 AM PDT] We are investigating increased API error rates and latencies in the US-EAST-1 Region.\n\n[03:16 AM PDT] Between 2:10 AM and 2:59 AM PDT we experienced increased API error rates and latencies in the US-EAST-1 Region. The issue has been resolved and the service is operating normally."
            }
        }
    ],
    "failedSet": []
}
```

For more information, see [Event details pane](https://docs.aws.amazon.com/health/latest/ug/getting-started-phd.html#event-details) in the *AWS Health User Guide*.

## Output

successfulSet -> (list)

Information about the events that could be retrieved.

(structure)

Detailed information about an event. A combination of an [Event](https://docs.aws.amazon.com/health/latest/APIReference/API_Event.html) object, an [EventDescription](https://docs.aws.amazon.com/health/latest/APIReference/API_EventDescription.html) object, and additional metadata about the event. Returned by the [DescribeEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html) operation.

event -> (structure)

Summary information about the event.

arn -> (string)

The unique identifier for the event. The event ARN has the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-details.html#id1)arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` format.

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

The most recent description of the event.

latestDescription -> (string)

The most recent description of the event.

eventMetadata -> (map)

Additional metadata about the event.

key -> (string)

value -> (string)

failedSet -> (list)

Error messages for any events that could not be retrieved.

(structure)

Error information returned when a [DescribeEventDetails](https://docs.aws.amazon.com/health/latest/APIReference/API_DescribeEventDetails.html) operation canât find a specified event.

eventArn -> (string)

The unique identifier for the event. The event ARN has the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/health/describe-event-details.html#id3)arn:aws:health:*event-region* ::event/*SERVICE* /*EVENT_TYPE_CODE* /*EVENT_TYPE_PLUS_ID* `` format.

For example, an event ARN might look like the following:

`arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`

errorName -> (string)

The name of the error.

errorMessage -> (string)

A message that describes the error.