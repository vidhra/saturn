# list-harvest-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/list-harvest-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/list-harvest-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mediapackagev2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mediapackagev2/index.html#cli-aws-mediapackagev2) ]

# list-harvest-jobs

## Description

Retrieves a list of harvest jobs that match the specified criteria.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mediapackagev2-2022-12-25/ListHarvestJobs)

`list-harvest-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Items`

## Synopsis

```
list-harvest-jobs
--channel-group-name <value>
[--channel-name <value>]
[--origin-endpoint-name <value>]
[--status <value>]
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

`--channel-group-name` (string)

The name of the channel group to filter the harvest jobs by. If specified, only harvest jobs associated with channels in this group will be returned.

`--channel-name` (string)

The name of the channel to filter the harvest jobs by. If specified, only harvest jobs associated with this channel will be returned.

`--origin-endpoint-name` (string)

The name of the origin endpoint to filter the harvest jobs by. If specified, only harvest jobs associated with this origin endpoint will be returned.

`--status` (string)

The status to filter the harvest jobs by. If specified, only harvest jobs with this status will be returned.

Possible values:

- `QUEUED`
- `IN_PROGRESS`
- `CANCELLED`
- `COMPLETED`
- `FAILED`

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

Items -> (list)

An array of harvest job objects that match the specified criteria.

(structure)

Represents a harvest job resource in MediaPackage v2, which is used to export content from an origin endpoint to an S3 bucket.

ChannelGroupName -> (string)

The name of the channel group containing the channel associated with this harvest job.

ChannelName -> (string)

The name of the channel associated with this harvest job.

OriginEndpointName -> (string)

The name of the origin endpoint associated with this harvest job.

Destination -> (structure)

The S3 destination where the harvested content will be placed.

S3Destination -> (structure)

The configuration for exporting harvested content to an S3 bucket. This includes details such as the bucket name and destination path within the bucket.

BucketName -> (string)

The name of an S3 bucket within which harvested content will be exported.

DestinationPath -> (string)

The path within the specified S3 bucket where the harvested content will be placed.

HarvestJobName -> (string)

The name of the harvest job.

HarvestedManifests -> (structure)

A list of manifests that are being or have been harvested.

HlsManifests -> (list)

A list of harvested HLS manifests.

(structure)

Information about a harvested HLS manifest.

ManifestName -> (string)

The name of the harvested HLS manifest.

DashManifests -> (list)

A list of harvested DASH manifests.

(structure)

Information about a harvested DASH manifest.

ManifestName -> (string)

The name of the harvested DASH manifest.

LowLatencyHlsManifests -> (list)

A list of harvested Low-Latency HLS manifests.

(structure)

Information about a harvested Low-Latency HLS manifest.

ManifestName -> (string)

The name of the harvested Low-Latency HLS manifest.

Description -> (string)

An optional description of the harvest job.

ScheduleConfiguration -> (structure)

The configuration for when the harvest job is scheduled to run.

StartTime -> (timestamp)

The start time for the harvest job.

EndTime -> (timestamp)

The end time for the harvest job.

Arn -> (string)

The Amazon Resource Name (ARN) of the harvest job.

CreatedAt -> (timestamp)

The date and time when the harvest job was created.

ModifiedAt -> (timestamp)

The date and time when the harvest job was last modified.

Status -> (string)

The current status of the harvest job (e.g., QUEUED, IN_PROGRESS, CANCELLED, COMPLETED, FAILED).

ErrorMessage -> (string)

An error message if the harvest job encountered any issues.

ETag -> (string)

The current version of the harvest job. Used for concurrency control.

NextToken -> (string)

A token used for pagination. Include this value in subsequent requests to retrieve the next set of results. If null, there are no more results to retrieve.