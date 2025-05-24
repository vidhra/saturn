# start-cache-reportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/start-cache-report.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/start-cache-report.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [storagegateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html#cli-aws-storagegateway) ]

# start-cache-report

## Description

Starts generating a report of the file metadata currently cached by an S3 File Gateway for a specific file share. You can use this report to identify and resolve issues if you have files failing upload from your gateway to Amazon S3. The report is a CSV file containing a list of files which match the set of filter parameters you specify in the request.

### Note

The **Files Failing Upload** flag is reset every 24 hours and during gateway reboot. If this report captures the files after the reset, but before they become flagged again, they will not be reported as **Files Failing Upload** .

The following requirements must be met to successfully generate a cache report:

- You must have permissions to list the entire Amazon S3 bucket associated with the specified file share.
- No other cache reports can currently be in-progress for the specified file share.
- There must be fewer than 10 existing cache reports for the specified file share.
- The gateway must be online and connected to Amazon Web Services.
- The root disk must have at least 20GB of free space when report generation starts.
- You must specify at least one value for `InclusionFilters` or `ExclusionFilters` in the request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/StartCacheReport)

## Synopsis

```
start-cache-report
--file-share-arn <value>
--role <value>
--location-arn <value>
--bucket-region <value>
[--vpc-endpoint-dns-name <value>]
[--inclusion-filters <value>]
[--exclusion-filters <value>]
--client-token <value>
[--tags <value>]
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

`--file-share-arn` (string)

The Amazon Resource Name (ARN) of the file share.

`--role` (string)

The ARN of the IAM role used when saving the cache report to Amazon S3.

`--location-arn` (string)

The ARN of the Amazon S3 bucket where you want to save the cache report.

### Note

We do not recommend saving the cache report to the same Amazon S3 bucket for which you are generating the report.

This field does not accept access point ARNs.

`--bucket-region` (string)

The Amazon Web Services Region of the Amazon S3 bucket where you want to save the cache report.

`--vpc-endpoint-dns-name` (string)

The DNS name of the VPC endpoint associated with the Amazon S3 where you want to save the cache report. Optional.

`--inclusion-filters` (list)

The list of filters and parameters that determine which files are included in the report. You must specify at least one value for `InclusionFilters` or `ExclusionFilters` in a `StartCacheReport` request.

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

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "UploadState"|"UploadFailureReason",
    "Values": ["string", ...]
  }
  ...
]
```

`--exclusion-filters` (list)

The list of filters and parameters that determine which files are excluded from the report. You must specify at least one value for `InclusionFilters` or `ExclusionFilters` in a `StartCacheReport` request.

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

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "UploadState"|"UploadFailureReason",
    "Values": ["string", ...]
  }
  ...
]
```

`--client-token` (string)

A unique identifier that you use to ensure idempotent report generation if you need to retry an unsuccessful `StartCacheReport` request. If you retry a request, use the same `ClientToken` you specified in the initial request.

`--tags` (list)

A list of up to 50 key/value tags that you can assign to the cache report. Using tags can help you categorize your reports and more easily locate them in search results.

(structure)

A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /.

Key -> (string)

Tag key. The key canât start with aws:.

Value -> (string)

Value of the tag key.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

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

CacheReportARN -> (string)

The Amazon Resource Name (ARN) of the cache report generated by the `StartCacheReport` request.