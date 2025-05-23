# describe-cache-reportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-cache-report.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/describe-cache-report.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [storagegateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html#cli-aws-storagegateway) ]

# describe-cache-report

## Description

Returns information about the specified cache report, including completion status and generation progress.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/DescribeCacheReport)

## Synopsis

```
describe-cache-report
--cache-report-arn <value>
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

`--cache-report-arn` (string)

The Amazon Resource Name (ARN) of the cache report you want to describe.

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

CacheReportInfo -> (structure)

Contains all informational fields associated with a cache report. Includes name, ARN, tags, status, progress, filters, start time, and end time.

CacheReportARN -> (string)

The Amazon Resource Name (ARN) of the cache report you want to describe.

CacheReportStatus -> (string)

The status of the specified cache report.

ReportCompletionPercent -> (integer)

The percentage of the report generation process that has been completed at time of inquiry.

EndTime -> (timestamp)

The time at which the gateway stopped generating the cache report.

Role -> (string)

The ARN of the IAM role that an S3 File Gateway assumes when it accesses the underlying storage.

FileShareARN -> (string)

The Amazon Resource Name (ARN) of the file share.

LocationARN -> (string)

The ARN of the Amazon S3 bucket location where the cache report is saved.

StartTime -> (timestamp)

The time at which the gateway started generating the cache report.

InclusionFilters -> (list)

The list of filters and parameters that determine which files are included in the report.

(structure)

A list of filter parameters and associated values that determine which files are included or excluded from a cache report created by a `StartCacheReport` request. Multiple instances of the same filter parameter are combined with an OR operation, while different parameters are combined with an AND operation.

Name -> (string)

The parameter name for a filter that determines which files are included or excluded from a cache report.

**Valid Names:**

UploadFailureReason | UploadState

Values -> (list)

The parameter value for a filter that determines which files are included or excluded from a cache report.

**Valid ``UploadFailureReason`` Values:**

`InaccessibleStorageClass` | `InvalidObjectState` | `ObjectMissing` | `S3AccessDenied`

**Valid ``UploadState`` Values:**

`FailingUpload`

(string)

ExclusionFilters -> (list)

The list of filters and parameters that determine which files are excluded from the report.

(structure)

A list of filter parameters and associated values that determine which files are included or excluded from a cache report created by a `StartCacheReport` request. Multiple instances of the same filter parameter are combined with an OR operation, while different parameters are combined with an AND operation.

Name -> (string)

The parameter name for a filter that determines which files are included or excluded from a cache report.

**Valid Names:**

UploadFailureReason | UploadState

Values -> (list)

The parameter value for a filter that determines which files are included or excluded from a cache report.

**Valid ``UploadFailureReason`` Values:**

`InaccessibleStorageClass` | `InvalidObjectState` | `ObjectMissing` | `S3AccessDenied`

**Valid ``UploadState`` Values:**

`FailingUpload`

(string)

ReportName -> (string)

The file name of the completed cache report object stored in Amazon S3.

Tags -> (list)

The list of key/value tags associated with the report.

(structure)

A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /.

Key -> (string)

Tag key. The key canât start with aws:.

Value -> (string)

Value of the tag key.