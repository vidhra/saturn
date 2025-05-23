# get-export-snapshot-recordsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-export-snapshot-records.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-export-snapshot-records.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-export-snapshot-records

## Description

Returns all export snapshot records created as a result of the `export snapshot` operation.

An export snapshot record can be used to create a new Amazon EC2 instance and its related resources with the [CreateCloudFormationStack](https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_CreateCloudFormationStack.html) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetExportSnapshotRecords)

`get-export-snapshot-records` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `exportSnapshotRecords`

## Synopsis

```
get-export-snapshot-records
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

exportSnapshotRecords -> (list)

A list of objects describing the export snapshot records.

(structure)

Describes an export snapshot record.

name -> (string)

The export snapshot record name.

arn -> (string)

The Amazon Resource Name (ARN) of the export snapshot record.

createdAt -> (timestamp)

The date when the export snapshot record was created.

location -> (structure)

The AWS Region and Availability Zone where the export snapshot record is located.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

resourceType -> (string)

The Lightsail resource type (`ExportSnapshotRecord` ).

state -> (string)

The state of the export snapshot record.

sourceInfo -> (structure)

A list of objects describing the source of the export snapshot record.

resourceType -> (string)

The Lightsail resource type (`InstanceSnapshot` or `DiskSnapshot` ).

createdAt -> (timestamp)

The date when the source instance or disk snapshot was created.

name -> (string)

The name of the source instance or disk snapshot.

arn -> (string)

The Amazon Resource Name (ARN) of the source instance or disk snapshot.

fromResourceName -> (string)

The name of the snapshotâs source instance or disk.

fromResourceArn -> (string)

The Amazon Resource Name (ARN) of the snapshotâs source instance or disk.

instanceSnapshotInfo -> (structure)

A list of objects describing an instance snapshot.

fromBundleId -> (string)

The bundle ID from which the source instance was created (`micro_x_x` ).

fromBlueprintId -> (string)

The blueprint ID from which the source instance (`amazon_linux_2023` ).

fromDiskInfo -> (list)

A list of objects describing the disks that were attached to the source instance.

(structure)

Describes a disk.

name -> (string)

The disk name.

path -> (string)

The disk path.

sizeInGb -> (integer)

The size of the disk in GB (`32` ).

isSystemDisk -> (boolean)

A Boolean value indicating whether this disk is a system disk (has an operating system loaded on it).

diskSnapshotInfo -> (structure)

A list of objects describing a disk snapshot.

sizeInGb -> (integer)

The size of the disk in GB (`32` ).

destinationInfo -> (structure)

A list of objects describing the destination of the export snapshot record.

id -> (string)

The ID of the resource created at the destination.

service -> (string)

The destination service of the record.

nextPageToken -> (string)

The token to advance to the next page of results from your request.

A next page token is not returned if there are no more results to display.

To get the next page of results, perform another `GetExportSnapshotRecords` request and specify the next page token using the `pageToken` parameter.