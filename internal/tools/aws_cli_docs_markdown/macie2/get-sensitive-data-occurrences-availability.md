# get-sensitive-data-occurrences-availabilityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-sensitive-data-occurrences-availability.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-sensitive-data-occurrences-availability.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [macie2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/index.html#cli-aws-macie2) ]

# get-sensitive-data-occurrences-availability

## Description

Checks whether occurrences of sensitive data can be retrieved for a finding.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/macie2-2020-01-01/GetSensitiveDataOccurrencesAvailability)

## Synopsis

```
get-sensitive-data-occurrences-availability
--finding-id <value>
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

`--finding-id` (string)

The unique identifier for the finding.

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

code -> (string)

Specifies whether occurrences of sensitive data can be retrieved for the finding. Possible values are: AVAILABLE, the sensitive data can be retrieved; and, UNAVAILABLE, the sensitive data canât be retrieved. If this value is UNAVAILABLE, the reasons array indicates why the data canât be retrieved.

reasons -> (list)

Specifies why occurrences of sensitive data canât be retrieved for the finding. Possible values are:

- ACCOUNT_NOT_IN_ORGANIZATION - The affected account isnât currently part of your organization. Or the account is part of your organization but Macie isnât currently enabled for the account. Youâre not allowed to access the affected S3 object by using Macie.
- INVALID_CLASSIFICATION_RESULT - There isnât a corresponding sensitive data discovery result for the finding. Or the corresponding sensitive data discovery result isnât available in the current Amazon Web Services Region, is malformed or corrupted, or uses an unsupported storage format. Macie canât verify the location of the sensitive data to retrieve.
- INVALID_RESULT_SIGNATURE - The corresponding sensitive data discovery result is stored in an S3 object that wasnât signed by Macie. Macie canât verify the integrity and authenticity of the sensitive data discovery result. Therefore, Macie canât verify the location of the sensitive data to retrieve.
- MEMBER_ROLE_TOO_PERMISSIVE - The trust or permissions policy for the IAM role in the affected member account doesnât meet Macie requirements for restricting access to the role. Or the roleâs trust policy doesnât specify the correct external ID for your organization. Macie canât assume the role to retrieve the sensitive data.
- MISSING_GET_MEMBER_PERMISSION - Youâre not allowed to retrieve information about the association between your account and the affected account. Macie canât determine whether youâre allowed to access the affected S3 object as the delegated Macie administrator for the affected account.
- OBJECT_EXCEEDS_SIZE_QUOTA - The storage size of the affected S3 object exceeds the size quota for retrieving occurrences of sensitive data from this type of file.
- OBJECT_UNAVAILABLE - The affected S3 object isnât available. The object was renamed, moved, deleted, or changed after Macie created the finding. Or the object is encrypted with an KMS key that isnât available. For example, the key is disabled, is scheduled for deletion, or was deleted.
- RESULT_NOT_SIGNED - The corresponding sensitive data discovery result is stored in an S3 object that hasnât been signed. Macie canât verify the integrity and authenticity of the sensitive data discovery result. Therefore, Macie canât verify the location of the sensitive data to retrieve.
- ROLE_TOO_PERMISSIVE - Your account is configured to retrieve occurrences of sensitive data by using an IAM role whose trust or permissions policy doesnât meet Macie requirements for restricting access to the role. Macie canât assume the role to retrieve the sensitive data.
- UNSUPPORTED_FINDING_TYPE - The specified finding isnât a sensitive data finding.
- UNSUPPORTED_OBJECT_TYPE - The affected S3 object uses a file or storage format that Macie doesnât support for retrieving occurrences of sensitive data.

This value is null if sensitive data can be retrieved for the finding.

(string)

Specifies why occurrences of sensitive data canât be retrieved for a finding. Possible values are: