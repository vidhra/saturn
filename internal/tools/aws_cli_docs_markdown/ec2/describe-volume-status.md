# describe-volume-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volume-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-volume-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-volume-status

## Description

Describes the status of the specified volumes. Volume status provides the result of the checks performed on your volumes to determine events that can impair the performance of your volumes. The performance of a volume can be affected if an issue occurs on the volumeâs underlying host. If the volumeâs underlying host experiences a power outage or system issue, after the system is restored, there could be data inconsistencies on the volume. Volume events notify you if this occurs. Volume actions notify you if any action needs to be taken in response to the event.

The `DescribeVolumeStatus` operation provides the following information about the specified volumes:

*Status* : Reflects the current status of the volume. The possible values are `ok` , `impaired` , `warning` , or `insufficient-data` . If all checks pass, the overall status of the volume is `ok` . If the check fails, the overall status is `impaired` . If the status is `insufficient-data` , then the checks might still be taking place on your volume at the time. We recommend that you retry the request. For more information about volume status, see [Monitor the status of your volumes](https://docs.aws.amazon.com/ebs/latest/userguide/monitoring-volume-status.html) in the *Amazon EBS User Guide* .

*Events* : Reflect the cause of a volume status and might require you to take action. For example, if your volume returns an `impaired` status, then the volume event might be `potential-data-inconsistency` . This means that your volume has been affected by an issue with the underlying host, has all I/O operations disabled, and might have inconsistent data.

*Actions* : Reflect the actions you might have to take in response to an event. For example, if the status of the volume is `impaired` and the volume event shows `potential-data-inconsistency` , then the action shows `enable-volume-io` . This means that you may want to enable the I/O operations for the volume by calling the  EnableVolumeIO action and then check the volume for data consistency.

Volume status is based on the volume status checks, and does not reflect the volume state. Therefore, volume status does not indicate volumes in the `error` state (for example, when a volume is incapable of accepting I/O.)

### Note

The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVolumeStatus)

`describe-volume-status` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `VolumeStatuses`

## Synopsis

```
describe-volume-status
[--volume-ids <value>]
[--dry-run | --no-dry-run]
[--filters <value>]
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

`--volume-ids` (list)

The IDs of the volumes.

Default: Describes all your volumes.

(string)

Syntax:

```
"string" "string" ...
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--filters` (list)

The filters.

- `action.code` - The action code for the event (for example, `enable-volume-io` ).
- `action.description` - A description of the action.
- `action.event-id` - The event ID associated with the action.
- `availability-zone` - The Availability Zone of the instance.
- `event.description` - A description of the event.
- `event.event-id` - The event ID.
- `event.event-type` - The event type (for `io-enabled` : `passed` | `failed` ; for `io-performance` : `io-performance:degraded` | `io-performance:severely-degraded` | `io-performance:stalled` ).
- `event.not-after` - The latest end time for the event.
- `event.not-before` - The earliest start time for the event.
- `volume-status.details-name` - The cause for `volume-status.status` (`io-enabled` | `io-performance` ).
- `volume-status.details-status` - The status of `volume-status.details-name` (for `io-enabled` : `passed` | `failed` ; for `io-performance` : `normal` | `degraded` | `severely-degraded` | `stalled` ).
- `volume-status.status` - The status of the volume (`ok` | `impaired` | `warning` | `insufficient-data` ).

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To describe the status of a single volume**

This example command describes the status for the volume `vol-1234567890abcdef0`.

Command:

```
aws ec2 describe-volume-status --volume-ids vol-1234567890abcdef0
```

Output:

```
{
    "VolumeStatuses": [
        {
            "VolumeStatus": {
                "Status": "ok",
                "Details": [
                    {
                        "Status": "passed",
                        "Name": "io-enabled"
                    },
                    {
                        "Status": "not-applicable",
                        "Name": "io-performance"
                    }
                ]
            },
            "AvailabilityZone": "us-east-1a",
            "VolumeId": "vol-1234567890abcdef0",
            "Actions": [],
            "Events": []
        }
    ]
}
```

**To describe the status of impaired volumes**

This example command describes the status for all volumes that are impaired. In this example output, there are no impaired volumes.

Command:

```
aws ec2 describe-volume-status --filters Name=volume-status.status,Values=impaired
```

Output:

```
{
    "VolumeStatuses": []
}
```

If you have a volume with a failed status check (status is impaired), see [Working with an Impaired Volume](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-volume-status.html#work_volumes_impaired) in the *Amazon EC2 User Guide*.

## Output

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.

VolumeStatuses -> (list)

Information about the status of the volumes.

(structure)

Describes the volume status.

Actions -> (list)

The details of the operation.

(structure)

Describes a volume status operation code.

Code -> (string)

The code identifying the operation, for example, `enable-volume-io` .

Description -> (string)

A description of the operation.

EventId -> (string)

The ID of the event associated with this operation.

EventType -> (string)

The event type associated with this operation.

AvailabilityZone -> (string)

The Availability Zone of the volume.

OutpostArn -> (string)

The Amazon Resource Name (ARN) of the Outpost.

Events -> (list)

A list of events associated with the volume.

(structure)

Describes a volume status event.

Description -> (string)

A description of the event.

EventId -> (string)

The ID of this event.

EventType -> (string)

The type of this event.

NotAfter -> (timestamp)

The latest end time of the event.

NotBefore -> (timestamp)

The earliest start time of the event.

InstanceId -> (string)

The ID of the instance associated with the event.

VolumeId -> (string)

The volume ID.

VolumeStatus -> (structure)

The volume status.

Details -> (list)

The details of the volume status.

(structure)

Describes a volume status.

Name -> (string)

The name of the volume status.

Status -> (string)

The intended status of the volume status.

Status -> (string)

The status of the volume.

AttachmentStatuses -> (list)

Information about the instances to which the volume is attached.

(structure)

Information about the instances to which the volume is attached.

IoPerformance -> (string)

The maximum IOPS supported by the attached instance.

InstanceId -> (string)

The ID of the attached instance.

AvailabilityZoneId -> (string)

The ID of the Availability Zone.