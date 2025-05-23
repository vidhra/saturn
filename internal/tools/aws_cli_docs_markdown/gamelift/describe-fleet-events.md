# describe-fleet-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-fleet-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# describe-fleet-events

## Description

Retrieves entries from a fleetâs event log. Fleet events are initiated by changes in status, such as during fleet creation and termination, changes in capacity, etc. If a fleet has multiple locations, events are also initiated by changes to status and capacity in remote locations.

You can specify a time range to limit the result set. Use the pagination parameters to retrieve results as a set of sequential pages.

If successful, a collection of event log entries matching the request are returned.

**Learn more**

[Setting up Amazon GameLift fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeFleetEvents)

`describe-fleet-events` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Events`

## Synopsis

```
describe-fleet-events
--fleet-id <value>
[--start-time <value>]
[--end-time <value>]
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

`--fleet-id` (string)

A unique identifier for the fleet to get event logs for. You can use either the fleet ID or ARN value.

`--start-time` (timestamp)

The earliest date to retrieve event logs for. If no start time is specified, this call returns entries starting from when the fleet was created to the specified end time. Format is a number expressed in Unix time as milliseconds (ex: â1469498468.057â).

`--end-time` (timestamp)

The most recent date to retrieve event logs for. If no end time is specified, this call returns entries from the specified start time up to the present. Format is a number expressed in Unix time as milliseconds (ex: â1469498468.057â).

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

**To request events for a specified time span**

The following `describe-fleet-events` example diplays details of all fleet-related events that occurred during the specified time span.

```
aws gamelift describe-fleet-events \
    --fleet-id arn:aws:gamelift:us-west-2::fleet/fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --start-time 1579647600 \
    --end-time 1579649400 \
    --limit 5
```

Output:

```
{
    "Events": [
        {
            "EventId": "a37b6892-5d07-4d3b-8b47-80244ecf66b9",
            "ResourceId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "EventCode": "FLEET_STATE_ACTIVE",
            "Message": "Fleet fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 changed state to ACTIVE",
            "EventTime": 1579649342.191
        },
        {
            "EventId": "67da4ec9-92a3-4d95-886a-5d6772c24063",
            "ResourceId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "EventCode": "FLEET_STATE_ACTIVATING",
            "Message": "Fleet fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 changed state to ACTIVATING",
            "EventTime": 1579649321.427
        },
        {
            "EventId": "23813a46-a9e6-4a53-8847-f12e6a8381ac",
            "ResourceId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "EventCode": "FLEET_STATE_BUILDING",
            "Message": "Fleet fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 changed state to BUILDING",
            "EventTime": 1579649321.243
        },
        {
            "EventId": "3bf217d0-1d44-42f9-9202-433ed475d2e8",
            "ResourceId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "EventCode": "FLEET_STATE_VALIDATING",
            "Message": "Fleet fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 changed state to VALIDATING",
            "EventTime": 1579649197.449
        },
        {
            "EventId": "2ecd0130-5986-44eb-99a7-62df27741084",
            "ResourceId": "fleet-a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "EventCode": "FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND",
            "Message": "Failed to find a valid path",
            "EventTime": 1569319075.839,
            "PreSignedLogUrl": "https://gamelift-event-logs-prod-us-west-2.s3.us-west-2.amazonaws.com/logs/fleet-83422059-8329-42a2-a4d6-c4444386a6f8/events/2ecd0130-5986-44eb-99a7-62df27741084/FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND.txt?X-Amz-Security-Token=IQoJb3JpZ2luX2VjEB8aCXVzLXdlc3QtMiJHMEUCIHV5K%2FLPx8h310D%2FAvx0%2FZxsDy5XA3cJOwPdu3T0eBa%2FAiEA1yovokcZYy%2FV4CWW6l26aFyiSHO%2Bxz%2FBMAhEHYHMQNcqkQMImP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw3NDEwNjE1OTIxNzEiDI8rsZtzLzlwEDQhXSrlAtl5Ae%2Fgo6FCIzqXPbXfBOnSvFYqeDlriZarEpKqKrUt8mXQv9iqHResqCph9AKo49lwgSYTT2QoSxnrD7%2FUgv%2BZm2pVuczvuKtUA0fcx6s0GxpjIAzdIE%2F5P%2FB7B9M%2BVZ%2F9KF82hbJi0HTE6Y7BjKsEgFCvk4UXILhfjtan9iQl8%2F21ZTurAcJbm7Y5tuLF9SWSK3%2BEa7VXOcCK4D4O1sMjmdRm0q0CKZ%2FIaXoHkNvg0RVTa0hIqdvpaDQlsSBNdqTXbjHTu6fETE9Y9Ky%2BiJK5KiUG%2F59GjCpDcvS1FqKeLUEmKT7wysGmvjMc2n%2Fr%2F9VxQfte7w9srXwlLAQuwhiXAAyI5ICMZ5JvzjzQwTqD4CHTVKUUDwL%2BRZzbuuqkJObZml02CkRGp%2B74RTAzLbWptVqZTIfzctiCTmWxb%2FmKyELRYsVLrwNJ%2BGJ7%2BCrN0RC%2FjlgfLYIZyeAqjPgAu5HjgX%2BM7jCo9M7wBTrnAXKOFQuf9dvA84SuwXOJFp17LYGjrHMKv0qC3GfbTMrZ6kzeNV9awKCpXB2Gnx9z2KvIlJdqirWVpvHVGwKCmJBCesDzjJHrae3neogI1uW%2F9C6%2B4jIZPME3jXmZcEHqqw5uvAVF7aeIavtUZU8pxpDIWT0YE4p3Kriy2AA7ziCRKtVfjV839InyLk8LUjsioWK2qlpg2HXKFLpAXw1QsQyxYmFMB9sGKOUlbL7Jdkk%2BYUq8%2FDTlLxqj1S%2FiO4TI0Wo7ilAo%2FKKWWF4guuNDexj8EOOynSp1yImB%2BZf2Fua3O44W4eEXAMPLE33333&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20170621T231808Z&X-Amz-SignedHeaders=host&X-Amz-Expires=900&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20170621%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Signature=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
        }
    ],
    "NextToken": "eyJhd3NBY2NvdW50SWQiOnsicyI6IjMwMjc3NjAxNjM5OCJ9LCJidWlsZElkIjp7InMiOiJidWlsZC01NWYxZTZmMS1jY2FlLTQ3YTctOWI5ZS1iYjFkYTQwMjEXAMPLE2"
}
```

For more information, see [Debug GameLift Fleet Issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html) in the *Amazon GameLift Developer Guide*.

## Output

Events -> (list)

A collection of objects containing event log entries for the specified fleet.

(structure)

Log entry describing an event that involves Amazon GameLift resources (such as a fleet). In addition to tracking activity, event codes and messages can provide additional information for troubleshooting and debugging problems.

EventId -> (string)

A unique identifier for a fleet event.

ResourceId -> (string)

A unique identifier for an event resource, such as a fleet ID.

EventCode -> (string)

The type of event being logged.

**Fleet state transition events:**

- FLEET_CREATED â A fleet resource was successfully created with a status of `NEW` . Event messaging includes the fleet ID.
- FLEET_STATE_DOWNLOADING â Fleet status changed from `NEW` to `DOWNLOADING` . Amazon GameLift is downloading the compressed build and running install scripts.
- FLEET_STATE_VALIDATING â Fleet status changed from `DOWNLOADING` to `VALIDATING` . Amazon GameLift has successfully installed build and is now validating the build files.
- FLEET_STATE_BUILDING â Fleet status changed from `VALIDATING` to `BUILDING` . Amazon GameLift has successfully verified the build files and is now launching a fleet instance.
- FLEET_STATE_ACTIVATING â Fleet status changed from `BUILDING` to `ACTIVATING` . Amazon GameLift is launching a game server process on the fleet instance and is testing its connectivity with the Amazon GameLift service.
- FLEET_STATE_ACTIVE â The fleetâs status changed from `ACTIVATING` to `ACTIVE` . The fleet is now ready to host game sessions.
- FLEET_STATE_ERROR â The Fleetâs status changed to `ERROR` . Describe the fleet event message for more details.

**Fleet creation events (ordered by fleet creation activity):**

- FLEET_BINARY_DOWNLOAD_FAILED â The build failed to download to the fleet instance.
- FLEET_CREATION_EXTRACTING_BUILD â The game server build was successfully downloaded to an instance, and Amazon GameLiftis now extracting the build files from the uploaded build. Failure at this stage prevents a fleet from moving to ACTIVE status. Logs for this stage display a list of the files that are extracted and saved on the instance. Access the logs by using the URL in *PreSignedLogUrl* .
- FLEET_CREATION_RUNNING_INSTALLER â The game server build files were successfully extracted, and Amazon GameLift is now running the buildâs install script (if one is included). Failure in this stage prevents a fleet from moving to ACTIVE status. Logs for this stage list the installation steps and whether or not the install completed successfully. Access the logs by using the URL in *PreSignedLogUrl* .
- FLEET_CREATION_COMPLETED_INSTALLER â The game server build files were successfully installed and validation of the installation will begin soon.
- FLEET_CREATION_FAILED_INSTALLER â The installed failed while attempting to install the build files. This event indicates that the failure occurred before Amazon GameLift could start validation.
- FLEET_CREATION_VALIDATING_RUNTIME_CONFIG â The build process was successful, and the GameLift is now verifying that the game server launch paths, which are specified in the fleetâs runtime configuration, exist. If any listed launch path exists, Amazon GameLift tries to launch a game server process and waits for the process to report ready. Failures in this stage prevent a fleet from moving to `ACTIVE` status. Logs for this stage list the launch paths in the runtime configuration and indicate whether each is found. Access the logs by using the URL in *PreSignedLogUrl* .
- FLEET_VALIDATION_LAUNCH_PATH_NOT_FOUND â Validation of the runtime configuration failed because the executable specified in a launch path does not exist on the instance.
- FLEET_VALIDATION_EXECUTABLE_RUNTIME_FAILURE â Validation of the runtime configuration failed because the executable specified in a launch path failed to run on the fleet instance.
- FLEET_VALIDATION_TIMED_OUT â Validation of the fleet at the end of creation timed out. Try fleet creation again.
- FLEET_ACTIVATION_FAILED â The fleet failed to successfully complete one of the steps in the fleet activation process. This event code indicates that the game build was successfully downloaded to a fleet instance, built, and validated, but was not able to start a server process. For more information, see [Debug Fleet Creation Issues](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-creating-debug.html#fleets-creating-debug-creation) .
- FLEET_ACTIVATION_FAILED_NO_INSTANCES â Fleet creation was not able to obtain any instances based on the input fleet attributes. Try again at a different time or choose a different combination of fleet attributes such as fleet type, instance type, etc.
- FLEET_INITIALIZATION_FAILED â A generic exception occurred during fleet creation. Describe the fleet event message for more details.

**VPC peering events:**

- FLEET_VPC_PEERING_SUCCEEDED â A VPC peering connection has been established between the VPC for an Amazon GameLift fleet and a VPC in your Amazon Web Services account.
- FLEET_VPC_PEERING_FAILED â A requested VPC peering connection has failed. Event details and status information provide additional detail. A common reason for peering failure is that the two VPCs have overlapping CIDR blocks of IPv4 addresses. To resolve this, change the CIDR block for the VPC in your Amazon Web Services account. For more information on VPC peering failures, see [https://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html](https://docs.aws.amazon.com/AmazonVPC/latest/PeeringGuide/invalid-peering-configurations.html)
- FLEET_VPC_PEERING_DELETED â A VPC peering connection has been successfully deleted.

**Spot instance events:**

- INSTANCE_INTERRUPTED â A spot instance was interrupted by EC2 with a two-minute notification.
- INSTANCE_RECYCLED â A spot instance was determined to have a high risk of interruption and is scheduled to be recycled once it has no active game sessions.

**Server process events:**

- SERVER_PROCESS_INVALID_PATH â The game server executable or script could not be found based on the Fleet runtime configuration. Check that the launch path is correct based on the operating system of the Fleet.
- SERVER_PROCESS_SDK_INITIALIZATION_TIMEOUT â The server process did not call `InitSDK()` within the time expected (5 minutes). Check your game session log to see why `InitSDK()` was not called in time. This event is not emitted for managed container fleets and Anywhere fleets unless theyâre deployed with the Amazon GameLift Agent.
- SERVER_PROCESS_PROCESS_READY_TIMEOUT â The server process did not call `ProcessReady()` within the time expected (5 minutes) after calling `InitSDK()` . Check your game session log to see why `ProcessReady()` was not called in time.
- SERVER_PROCESS_CRASHED â The server process exited without calling `ProcessEnding()` . Check your game session log to see why `ProcessEnding()` was not called.
- SERVER_PROCESS_TERMINATED_UNHEALTHY â The server process did not report a valid health check for too long and was therefore terminated by GameLift. Check your game session log to see if the thread became stuck processing a synchronous task for too long.
- SERVER_PROCESS_FORCE_TERMINATED â The server process did not exit cleanly within the time expected after `OnProcessTerminate()` was sent. Check your game session log to see why termination took longer than expected.
- SERVER_PROCESS_PROCESS_EXIT_TIMEOUT â The server process did not exit cleanly within the time expected (30 seconds) after calling `ProcessEnding()` . Check your game session log to see why termination took longer than expected.

**Game session events:**

- GAME_SESSION_ACTIVATION_TIMEOUT â GameSession failed to activate within the expected time. Check your game session log to see why `ActivateGameSession()` took longer to complete than expected.

**Other fleet events:**

- FLEET_SCALING_EVENT â A change was made to the fleetâs capacity settings (desired instances, minimum/maximum scaling limits). Event messaging includes the new capacity settings.
- FLEET_NEW_GAME_SESSION_PROTECTION_POLICY_UPDATED â A change was made to the fleetâs game session protection policy setting. Event messaging includes both the old and new policy setting.
- FLEET_DELETED â A request to delete a fleet was initiated.
- GENERIC_EVENT â An unspecified event has occurred.

Message -> (string)

Additional information related to the event.

EventTime -> (timestamp)

Time stamp indicating when this event occurred. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

PreSignedLogUrl -> (string)

Location of stored logs with additional detail that is related to the event. This is useful for debugging issues. The URL is valid for 15 minutes. You can also access fleet creation logs through the Amazon GameLift console.

Count -> (long)

The number of times that this event occurred.

NextToken -> (string)

A token that indicates where to resume retrieving results on the next call to this operation. If no token is returned, these results represent the end of the list.