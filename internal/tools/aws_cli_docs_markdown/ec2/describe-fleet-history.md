# describe-fleet-historyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fleet-history.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-fleet-history.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-fleet-history

## Description

Describes the events for the specified EC2 Fleet during the specified time.

EC2 Fleet events are delayed by up to 30 seconds before they can be described. This ensures that you can query by the last evaluated time and not miss a recorded event. EC2 Fleet events are available for 48 hours.

For more information, see [Monitor fleet events using Amazon EventBridge](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/fleet-monitor.html) in the *Amazon EC2 User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeFleetHistory)

## Synopsis

```
describe-fleet-history
[--dry-run | --no-dry-run]
[--event-type <value>]
[--max-results <value>]
[--next-token <value>]
--fleet-id <value>
--start-time <value>
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--event-type` (string)

The type of events to describe. By default, all events are described.

Possible values:

- `instance-change`
- `fleet-change`
- `service-error`

`--max-results` (integer)

The maximum number of items to return for this request. To get the next page of items, make another request with the token returned in the output. For more information, see [Pagination](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Query-Requests.html#api-pagination) .

`--next-token` (string)

The token returned from a previous paginated request. Pagination continues from the end of the items returned by the previous request.

`--fleet-id` (string)

The ID of the EC2 Fleet.

`--start-time` (timestamp)

The start date and time for the events, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z).

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

**To describe EC2 Fleet history**

The following `describe-fleet-history` example returns the history for the specified EC2 Fleet starting at the specified time. The output is for an EC2 Fleet with two running instances.

```
aws ec2 describe-fleet-history \
    --fleet-id fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE \
    --start-time 2020-09-01T00:00:00Z
```

Output:

```
{
    "HistoryRecords": [
        {
            "EventInformation": {
                "EventSubType": "submitted"
            },
            "EventType": "fleetRequestChange",
            "Timestamp": "2020-09-01T18:26:05.000Z"
        },
        {
            "EventInformation": {
                "EventSubType": "active"
            },
            "EventType": "fleetRequestChange",
            "Timestamp": "2020-09-01T18:26:15.000Z"
        },
        {
            "EventInformation": {
                "EventDescription": "t2.small, ami-07c8bc5c1ce9598c3, ...",
                "EventSubType": "progress"
            },
            "EventType": "fleetRequestChange",
            "Timestamp": "2020-09-01T18:26:17.000Z"
        },
        {
            "EventInformation": {
                "EventDescription": "{\"instanceType\":\"t2.small\", ...}",
                "EventSubType": "launched",
                "InstanceId": "i-083a1c446e66085d2"
            },
            "EventType": "instanceChange",
            "Timestamp": "2020-09-01T18:26:17.000Z"
        },
        {
            "EventInformation": {
                "EventDescription": "{\"instanceType\":\"t2.small\", ...}",
                "EventSubType": "launched",
                "InstanceId": "i-090db02406cc3c2d6"
            },
            "EventType": "instanceChange",
            "Timestamp": "2020-09-01T18:26:17.000Z"
        }
    ],
    "LastEvaluatedTime": "2020-09-01T19:10:19.000Z",
    "FleetId": "fleet-12a34b55-67cd-8ef9-ba9b-9208dEXAMPLE",
    "StartTime": "2020-08-31T23:53:20.000Z"
}
```

For more information, see [Managing an EC2 Fleet](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/manage-ec2-fleet.html) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.

## Output

HistoryRecords -> (list)

Information about the events in the history of the EC2 Fleet.

(structure)

Describes an event in the history of an EC2 Fleet.

EventInformation -> (structure)

Information about the event.

EventDescription -> (string)

The description of the event.

EventSubType -> (string)

The event.

`error` events:

- `iamFleetRoleInvalid` - The EC2 Fleet or Spot Fleet does not have the required permissions either to launch or terminate an instance.
- `allLaunchSpecsTemporarilyBlacklisted` - None of the configurations are valid, and several attempts to launch instances have failed. For more information, see the description of the event.
- `spotInstanceCountLimitExceeded` - Youâve reached the limit on the number of Spot Instances that you can launch.
- `spotFleetRequestConfigurationInvalid` - The configuration is not valid. For more information, see the description of the event.

`fleetRequestChange` events:

- `active` - The EC2 Fleet or Spot Fleet request has been validated and Amazon EC2 is attempting to maintain the target number of running instances.
- `deleted` (EC2 Fleet) / `cancelled` (Spot Fleet) - The EC2 Fleet is deleted or the Spot Fleet request is canceled and has no running instances. The EC2 Fleet or Spot Fleet will be deleted two days after its instances are terminated.
- `deleted_running` (EC2 Fleet) / `cancelled_running` (Spot Fleet) - The EC2 Fleet is deleted or the Spot Fleet request is canceled and does not launch additional instances. Its existing instances continue to run until they are interrupted or terminated. The request remains in this state until all instances are interrupted or terminated.
- `deleted_terminating` (EC2 Fleet) / `cancelled_terminating` (Spot Fleet) - The EC2 Fleet is deleted or the Spot Fleet request is canceled and its instances are terminating. The request remains in this state until all instances are terminated.
- `expired` - The EC2 Fleet or Spot Fleet request has expired. If the request was created with `TerminateInstancesWithExpiration` set, a subsequent `terminated` event indicates that the instances are terminated.
- `modify_in_progress` - The EC2 Fleet or Spot Fleet request is being modified. The request remains in this state until the modification is fully processed.
- `modify_succeeded` - The EC2 Fleet or Spot Fleet request was modified.
- `submitted` - The EC2 Fleet or Spot Fleet request is being evaluated and Amazon EC2 is preparing to launch the target number of instances.
- `progress` - The EC2 Fleet or Spot Fleet request is in the process of being fulfilled.

`instanceChange` events:

- `launched` - A new instance was launched.
- `terminated` - An instance was terminated by the user.
- `termination_notified` - An instance termination notification was sent when a Spot Instance was terminated by Amazon EC2 during scale-down, when the target capacity of the fleet was modified down, for example, from a target capacity of 4 to a target capacity of 3.

`Information` events:

- `fleetProgressHalted` - The price in every launch specification is not valid because it is below the Spot price (all the launch specifications have produced `launchSpecUnusable` events). A launch specification might become valid if the Spot price changes.
- `launchSpecTemporarilyBlacklisted` - The configuration is not valid and several attempts to launch instances have failed. For more information, see the description of the event.
- `launchSpecUnusable` - The price specified in a launch specification is not valid because it is below the Spot price for the requested Spot pools. Note: Even if a fleet with the `maintain` request type is in the process of being canceled, it may still publish a `launchSpecUnusable` event. This does not mean that the canceled fleet is attempting to launch a new instance.
- `registerWithLoadBalancersFailed` - An attempt to register instances with load balancers failed. For more information, see the description of the event.

InstanceId -> (string)

The ID of the instance. This information is available only for `instanceChange` events.

EventType -> (string)

The event type.

Timestamp -> (timestamp)

The date and time of the event, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z).

LastEvaluatedTime -> (timestamp)

The last date and time for the events, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z). All records up to this time were retrieved.

If `nextToken` indicates that there are more items, this value is not present.

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.

FleetId -> (string)

The ID of the EC Fleet.

StartTime -> (timestamp)

The start date and time for the events, in UTC format (for example, *YYYY* -*MM* -*DD* T*HH* :*MM* :*SS* Z).