# update-report-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-report-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/update-report-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codebuild](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codebuild/index.html#cli-aws-codebuild) ]

# update-report-group

## Description

Updates a report group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codebuild-2016-10-06/UpdateReportGroup)

## Synopsis

```
update-report-group
--arn <value>
[--export-config <value>]
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

`--arn` (string)

The ARN of the report group to update.

`--export-config` (structure)

Used to specify an updated export type. Valid values are:

- `S3` : The report results are exported to an S3 bucket.
- `NO_EXPORT` : The report results are not exported.

exportConfigType -> (string)

The export configuration type. Valid values are:

- `S3` : The report results are exported to an S3 bucket.
- `NO_EXPORT` : The report results are not exported.

s3Destination -> (structure)

A `S3ReportExportConfig` object that contains information about the S3 bucket where the run of a report is exported.

bucket -> (string)

The name of the S3 bucket where the raw data of a report are exported.

bucketOwner -> (string)

The Amazon Web Services account identifier of the owner of the Amazon S3 bucket. This allows report data to be exported to an Amazon S3 bucket that is owned by an account other than the account running the build.

path -> (string)

The path to the exported reportâs raw data results.

packaging -> (string)

The type of build output artifact to create. Valid values include:

- `NONE` : CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified.
- `ZIP` : CodeBuild creates a ZIP file with the raw data in the output bucket.

encryptionKey -> (string)

The encryption key for the reportâs encrypted raw data.

encryptionDisabled -> (boolean)

A boolean value that specifies if the results of a report are encrypted.

Shorthand Syntax:

```
exportConfigType=string,s3Destination={bucket=string,bucketOwner=string,path=string,packaging=string,encryptionKey=string,encryptionDisabled=boolean}
```

JSON Syntax:

```
{
  "exportConfigType": "S3"|"NO_EXPORT",
  "s3Destination": {
    "bucket": "string",
    "bucketOwner": "string",
    "path": "string",
    "packaging": "ZIP"|"NONE",
    "encryptionKey": "string",
    "encryptionDisabled": true|false
  }
}
```

`--tags` (list)

An updated list of tag key and value pairs associated with this report group.

These tags are available for use by Amazon Web Services services that support CodeBuild report group tags.

(structure)

A tag, consisting of a key and a value.

This tag is available for use by Amazon Web Services services that support tags in CodeBuild.

key -> (string)

The tagâs key.

value -> (string)

The tagâs value.

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update a report group in AWS CodeBuild.**

The following `update-report-group` example changes the export type of the report group to âNO_EXPORTâ.

```
aws codebuild update-report-group \
    --arn arn:aws:codebuild:<region-ID>:<user-ID>:report-group/cli-created-report-group \
    --export-config="exportConfigType=NO_EXPORT"
```

Output:

```
{
    "reportGroup": {
        "arn": "arn:aws:codebuild:<region-ID>:<user-ID>:report-group/cli-created-report-group",
        "name": "cli-created-report-group",
        "type": "TEST",
        "exportConfig": {
            "exportConfigType": "NO_EXPORT"
        },
        "created": 1602020686.009,
        "lastModified": 1602021033.454,
        "tags": []
    }
}
```

For more information, see [Working with report groups](https://docs.aws.amazon.com/codebuild/latest/userguide/test-report-group.html) in the *AWS CodeBuild User Guide*.

## Output

reportGroup -> (structure)

Information about the updated report group.

arn -> (string)

The ARN of the `ReportGroup` .

name -> (string)

The name of the `ReportGroup` .

type -> (string)

The type of the `ReportGroup` . This can be one of the following values:

CODE_COVERAGE

The report group contains code coverage reports.

TEST

The report group contains test reports.

exportConfig -> (structure)

Information about the destination where the raw data of this `ReportGroup` is exported.

exportConfigType -> (string)

The export configuration type. Valid values are:

- `S3` : The report results are exported to an S3 bucket.
- `NO_EXPORT` : The report results are not exported.

s3Destination -> (structure)

A `S3ReportExportConfig` object that contains information about the S3 bucket where the run of a report is exported.

bucket -> (string)

The name of the S3 bucket where the raw data of a report are exported.

bucketOwner -> (string)

The Amazon Web Services account identifier of the owner of the Amazon S3 bucket. This allows report data to be exported to an Amazon S3 bucket that is owned by an account other than the account running the build.

path -> (string)

The path to the exported reportâs raw data results.

packaging -> (string)

The type of build output artifact to create. Valid values include:

- `NONE` : CodeBuild creates the raw data in the output bucket. This is the default if packaging is not specified.
- `ZIP` : CodeBuild creates a ZIP file with the raw data in the output bucket.

encryptionKey -> (string)

The encryption key for the reportâs encrypted raw data.

encryptionDisabled -> (boolean)

A boolean value that specifies if the results of a report are encrypted.

created -> (timestamp)

The date and time this `ReportGroup` was created.

lastModified -> (timestamp)

The date and time this `ReportGroup` was last modified.

tags -> (list)

A list of tag key and value pairs associated with this report group.

These tags are available for use by Amazon Web Services services that support CodeBuild report group tags.

(structure)

A tag, consisting of a key and a value.

This tag is available for use by Amazon Web Services services that support tags in CodeBuild.

key -> (string)

The tagâs key.

value -> (string)

The tagâs value.

status -> (string)

The status of the report group. This property is read-only.

This can be one of the following values:

ACTIVE

The report group is active.

DELETING

The report group is in the process of being deleted.