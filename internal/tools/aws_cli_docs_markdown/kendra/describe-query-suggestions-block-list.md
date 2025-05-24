# describe-query-suggestions-block-listÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-query-suggestions-block-list.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/describe-query-suggestions-block-list.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# describe-query-suggestions-block-list

## Description

Gets information about a block list used for query suggestions for an index.

This is used to check the current settings that are applied to a block list.

`DescribeQuerySuggestionsBlockList` is currently not supported in the Amazon Web Services GovCloud (US-West) region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/DescribeQuerySuggestionsBlockList)

## Synopsis

```
describe-query-suggestions-block-list
--index-id <value>
--id <value>
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

`--index-id` (string)

The identifier of the index for the block list.

`--id` (string)

The identifier of the block list you want to get information on.

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

IndexId -> (string)

The identifier of the index for the block list.

Id -> (string)

The identifier of the block list.

Name -> (string)

The name of the block list.

Description -> (string)

The description for the block list.

Status -> (string)

The current status of the block list. When the value is `ACTIVE` , the block list is ready for use.

ErrorMessage -> (string)

The error message containing details if there are issues processing the block list.

CreatedAt -> (timestamp)

The Unix timestamp when a block list for query suggestions was created.

UpdatedAt -> (timestamp)

The Unix timestamp when a block list for query suggestions was last updated.

SourceS3Path -> (structure)

Shows the current S3 path to your block list text file in your S3 bucket.

Each block word or phrase should be on a separate line in a text file.

For information on the current quota limits for block lists, see [Quotas for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html) .

Bucket -> (string)

The name of the S3 bucket that contains the file.

Key -> (string)

The name of the file.

ItemCount -> (integer)

The current number of valid, non-empty words or phrases in the block list text file.

FileSizeBytes -> (long)

The current size of the block list text file in S3.

RoleArn -> (string)

The IAM (Identity and Access Management) role used by Amazon Kendra to access the block list text file in S3.

The role needs S3 read permissions to your file in S3 and needs to give STS (Security Token Service) assume role permissions to Amazon Kendra.