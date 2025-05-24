# start-importÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/start-import.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/start-import.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudtrail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudtrail/index.html#cli-aws-cloudtrail) ]

# start-import

## Description

Starts an import of logged trail events from a source S3 bucket to a destination event data store. By default, CloudTrail only imports events contained in the S3 bucketâs `CloudTrail` prefix and the prefixes inside the `CloudTrail` prefix, and does not check prefixes for other Amazon Web Services services. If you want to import CloudTrail events contained in another prefix, you must include the prefix in the `S3LocationUri` . For more considerations about importing trail events, see [Considerations for copying trail events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-copy-trail-to-lake.html#cloudtrail-trail-copy-considerations) in the *CloudTrail User Guide* .

When you start a new import, the `Destinations` and `ImportSource` parameters are required. Before starting a new import, disable any access control lists (ACLs) attached to the source S3 bucket. For more information about disabling ACLs, see [Controlling ownership of objects and disabling ACLs for your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) .

When you retry an import, the `ImportID` parameter is required.

### Note

If the destination event data store is for an organization, you must use the management account to import trail events. You cannot use the delegated administrator account for the organization.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudtrail-2013-11-01/StartImport)

## Synopsis

```
start-import
[--destinations <value>]
[--import-source <value>]
[--start-event-time <value>]
[--end-event-time <value>]
[--import-id <value>]
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

`--destinations` (list)

The ARN of the destination event data store. Use this parameter for a new import.

(string)

Syntax:

```
"string" "string" ...
```

`--import-source` (structure)

The source S3 bucket for the import. Use this parameter for a new import.

S3 -> (structure)

The source S3 bucket.

S3LocationUri -> (string)

The URI for the source S3 bucket.

S3BucketRegion -> (string)

The Region associated with the source S3 bucket.

S3BucketAccessRoleArn -> (string)

The IAM ARN role used to access the source S3 bucket.

Shorthand Syntax:

```
S3={S3LocationUri=string,S3BucketRegion=string,S3BucketAccessRoleArn=string}
```

JSON Syntax:

```
{
  "S3": {
    "S3LocationUri": "string",
    "S3BucketRegion": "string",
    "S3BucketAccessRoleArn": "string"
  }
}
```

`--start-event-time` (timestamp)

Use with `EndEventTime` to bound a `StartImport` request, and limit imported trail events to only those events logged within a specified time period. When you specify a time range, CloudTrail checks the prefix and log file names to verify the names contain a date between the specified `StartEventTime` and `EndEventTime` before attempting to import events.

`--end-event-time` (timestamp)

Use with `StartEventTime` to bound a `StartImport` request, and limit imported trail events to only those events logged within a specified time period. When you specify a time range, CloudTrail checks the prefix and log file names to verify the names contain a date between the specified `StartEventTime` and `EndEventTime` before attempting to import events.

`--import-id` (string)

The ID of the import. Use this parameter when you are retrying an import.

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

ImportId -> (string)

The ID of the import.

Destinations -> (list)

The ARN of the destination event data store.

(string)

ImportSource -> (structure)

The source S3 bucket for the import.

S3 -> (structure)

The source S3 bucket.

S3LocationUri -> (string)

The URI for the source S3 bucket.

S3BucketRegion -> (string)

The Region associated with the source S3 bucket.

S3BucketAccessRoleArn -> (string)

The IAM ARN role used to access the source S3 bucket.

StartEventTime -> (timestamp)

Used with `EndEventTime` to bound a `StartImport` request, and limit imported trail events to only those events logged within a specified time period.

EndEventTime -> (timestamp)

Used with `StartEventTime` to bound a `StartImport` request, and limit imported trail events to only those events logged within a specified time period.

ImportStatus -> (string)

Shows the status of the import after a `StartImport` request. An import finishes with a status of `COMPLETED` if there were no failures, or `FAILED` if there were failures.

CreatedTimestamp -> (timestamp)

The timestamp for the importâs creation.

UpdatedTimestamp -> (timestamp)

The timestamp of the importâs last update, if applicable.