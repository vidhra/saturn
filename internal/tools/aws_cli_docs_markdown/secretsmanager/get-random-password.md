# get-random-passwordÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/get-random-password.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/get-random-password.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [secretsmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/index.html#cli-aws-secretsmanager) ]

# get-random-password

## Description

Generates a random password. We recommend that you specify the maximum length and include every character type that the system you are generating a password for can support. By default, Secrets Manager uses uppercase and lowercase letters, numbers, and the following characters in passwords: `!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~`

Secrets Manager generates a CloudTrail log entry when you call this action.

**Required permissions:** `secretsmanager:GetRandomPassword` . For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/GetRandomPassword)

## Synopsis

```
get-random-password
[--password-length <value>]
[--exclude-characters <value>]
[--exclude-numbers | --no-exclude-numbers]
[--exclude-punctuation | --no-exclude-punctuation]
[--exclude-uppercase | --no-exclude-uppercase]
[--exclude-lowercase | --no-exclude-lowercase]
[--include-space | --no-include-space]
[--require-each-included-type | --no-require-each-included-type]
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

`--password-length` (long)

The length of the password. If you donât include this parameter, the default length is 32 characters.

`--exclude-characters` (string)

A string of the characters that you donât want in the password.

`--exclude-numbers` | `--no-exclude-numbers` (boolean)

Specifies whether to exclude numbers from the password. If you donât include this switch, the password can contain numbers.

`--exclude-punctuation` | `--no-exclude-punctuation` (boolean)

Specifies whether to exclude the following punctuation characters from the password: `! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~` . If you donât include this switch, the password can contain punctuation.

`--exclude-uppercase` | `--no-exclude-uppercase` (boolean)

Specifies whether to exclude uppercase letters from the password. If you donât include this switch, the password can contain uppercase letters.

`--exclude-lowercase` | `--no-exclude-lowercase` (boolean)

Specifies whether to exclude lowercase letters from the password. If you donât include this switch, the password can contain lowercase letters.

`--include-space` | `--no-include-space` (boolean)

Specifies whether to include the space character. If you include this switch, the password can contain space characters.

`--require-each-included-type` | `--no-require-each-included-type` (boolean)

Specifies whether to include at least one upper and lowercase letter, one number, and one punctuation. If you donât include this switch, the password contains at least one of every character type.

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

**To generate a random password**

The following `get-random-password` example generates a random password 20 characters long that includes at least one uppercase letter, lowercase letter, number, and punctuation.

```
aws secretsmanager get-random-password \
    --require-each-included-type \
    --password-length 20
```

Output:

```
{
    "RandomPassword": "EXAMPLE-PASSWORD"
}
```

For more information, see [Create and manage secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/managing-secrets.html) in the *Secrets Manager User Guide*.

## Output

RandomPassword -> (string)

A string with the password.