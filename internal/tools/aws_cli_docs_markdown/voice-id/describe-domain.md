# describe-domainÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/voice-id/describe-domain.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/voice-id/describe-domain.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [voice-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/voice-id/index.html#cli-aws-voice-id) ]

# describe-domain

## Description

Describes the specified domain.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/voice-id-2021-09-27/DescribeDomain)

## Synopsis

```
describe-domain
--domain-id <value>
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

`--domain-id` (string)

The identifier of the domain that you are describing.

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

Domain -> (structure)

Information about the specified domain.

Arn -> (string)

The Amazon Resource Name (ARN) for the domain.

CreatedAt -> (timestamp)

The timestamp of when the domain was created.

Description -> (string)

The description of the domain.

DomainId -> (string)

The identifier of the domain.

DomainStatus -> (string)

The current status of the domain.

Name -> (string)

The name for the domain.

ServerSideEncryptionConfiguration -> (structure)

The server-side encryption configuration containing the KMS key identifier you want Voice ID to use to encrypt your data.

KmsKeyId -> (string)

The identifier of the KMS key to use to encrypt data stored by Voice ID. Voice ID doesnât support asymmetric customer managed keys.

ServerSideEncryptionUpdateDetails -> (structure)

Details about the most recent server-side encryption configuration update. When the server-side encryption configuration is changed, dependency on the old KMS key is removed through an asynchronous process. When this update is complete, the domainâs data can only be accessed using the new KMS key.

Message -> (string)

Message explaining the current UpdateStatus. When the UpdateStatus is FAILED, this message explains the cause of the failure.

OldKmsKeyId -> (string)

The previous KMS key ID the domain was encrypted with, before ServerSideEncryptionConfiguration was updated to a new KMS key ID.

UpdateStatus -> (string)

Status of the server-side encryption update. During an update, if there is an issue with the domainâs current or old KMS key ID, such as an inaccessible or disabled key, then the status is FAILED. In order to resolve this, the key needs to be made accessible, and then an UpdateDomain call with the existing server-side encryption configuration will re-attempt this update process.

UpdatedAt -> (timestamp)

The timestamp of when the domain was last update.

WatchlistDetails -> (structure)

The watchlist details of a domain. Contains the default watchlist ID of the domain.

DefaultWatchlistId -> (string)

The identifier of the default watchlist.