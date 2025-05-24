# get-event-actionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-event-action.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-event-action.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dataexchange](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/index.html#cli-aws-dataexchange) ]

# get-event-action

## Description

This operation retrieves information about an event action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dataexchange-2017-07-25/GetEventAction)

## Synopsis

```
get-event-action
--event-action-id <value>
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

`--event-action-id` (string)

The unique identifier for the event action.

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

Action -> (structure)

What occurs after a certain event.

ExportRevisionToS3 -> (structure)

Details for the export revision to Amazon S3 action.

Encryption -> (structure)

Encryption configuration for the auto export job.

KmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the AWS KMS key you want to use to encrypt the Amazon S3 objects. This parameter is required if you choose aws:kms as an encryption type.

Type -> (string)

The type of server side encryption used for encrypting the objects in Amazon S3.

RevisionDestination -> (structure)

A revision destination is the Amazon S3 bucket folder destination to where the export will be sent.

Bucket -> (string)

The Amazon S3 bucket that is the destination for the event action.

KeyPattern -> (string)

A string representing the pattern for generated names of the individual assets in the revision. For more information about key patterns, see [Key patterns when exporting revisions](https://docs.aws.amazon.com/data-exchange/latest/userguide/jobs.html#revision-export-keypatterns) .

Arn -> (string)

The ARN for the event action.

CreatedAt -> (timestamp)

The date and time that the event action was created, in ISO 8601 format.

Event -> (structure)

What occurs to start an action.

RevisionPublished -> (structure)

What occurs to start the revision publish action.

DataSetId -> (string)

The data set ID of the published revision.

Id -> (string)

The unique identifier for the event action.

UpdatedAt -> (timestamp)

The date and time that the event action was last updated, in ISO 8601 format.