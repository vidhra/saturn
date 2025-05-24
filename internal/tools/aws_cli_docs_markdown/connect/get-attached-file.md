# get-attached-fileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-attached-file.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/get-attached-file.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# get-attached-file

## Description

Provides a pre-signed URL for download of an approved attached file. This API also returns metadata about the attached file. It will only return a downloadURL if the status of the attached file is `APPROVED` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/GetAttachedFile)

## Synopsis

```
get-attached-file
--instance-id <value>
--file-id <value>
[--url-expiry-in-seconds <value>]
--associated-resource-arn <value>
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

`--instance-id` (string)

The unique identifier of the Amazon Connect instance.

`--file-id` (string)

The unique identifier of the attached file resource.

`--url-expiry-in-seconds` (integer)

Optional override for the expiry of the pre-signed S3 URL in seconds. The default value is 300.

`--associated-resource-arn` (string)

The resource to which the attached file is (being) uploaded to. The supported resources are [Cases](https://docs.aws.amazon.com/connect/latest/adminguide/cases.html) and [Email](https://docs.aws.amazon.com/connect/latest/adminguide/setup-email-channel.html) .

### Note

This value must be a valid ARN.

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

FileArn -> (string)

The unique identifier of the attached file resource (ARN).

FileId -> (string)

The unique identifier of the attached file resource.

CreationTime -> (string)

The time of Creation of the file resource as an ISO timestamp. Itâs specified in ISO 8601 format: `yyyy-MM-ddThh:mm:ss.SSSZ` . For example, `2024-05-03T02:41:28.172Z` .

FileStatus -> (string)

The current status of the attached file.

FileName -> (string)

A case-sensitive name of the attached file being uploaded.

FileSizeInBytes -> (long)

The size of the attached file in bytes.

AssociatedResourceArn -> (string)

The resource to which the attached file is (being) uploaded to. [Cases](https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateCase.html) are the only current supported resource.

FileUseCaseType -> (string)

The use case for the file.

CreatedBy -> (tagged union structure)

Represents the identity that created the file.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ConnectUserArn`, `AWSIdentityArn`.

ConnectUserArn -> (string)

An agent ARN representing a [connect user](https://docs.aws.amazon.com/service-authorization/latest/reference/list_amazonconnect.html#amazonconnect-resources-for-iam-policies) .

AWSIdentityArn -> (string)

STS or IAM ARN representing the identity of API Caller. SDK users cannot populate this and this value is calculated automatically if `ConnectUserArn` is not provided.

DownloadUrlMetadata -> (structure)

URL and expiry to be used when downloading the attached file.

Url -> (string)

A pre-signed URL that should be used to download the attached file.

UrlExpiry -> (string)

The expiration time of the URL in ISO timestamp. Itâs specified in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.

Tags -> (map)

The tags used to organize, track, or control access for this resource. For example, `{ "Tags": {"key1":"value1", "key2":"value2"} }` .

key -> (string)

value -> (string)