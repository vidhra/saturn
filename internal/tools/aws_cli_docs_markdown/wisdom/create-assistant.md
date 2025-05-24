# create-assistantÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wisdom/create-assistant.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wisdom/create-assistant.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wisdom](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wisdom/index.html#cli-aws-wisdom) ]

# create-assistant

## Description

Creates an Amazon Connect Wisdom assistant.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wisdom-2020-10-19/CreateAssistant)

## Synopsis

```
create-assistant
[--client-token <value>]
[--description <value>]
--name <value>
[--server-side-encryption-configuration <value>]
[--tags <value>]
--type <value>
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

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) .

`--description` (string)

The description of the assistant.

`--name` (string)

The name of the assistant.

`--server-side-encryption-configuration` (structure)

The configuration information for the customer managed key used for encryption.

The customer managed key must have a policy that allows `kms:CreateGrant` , `kms:DescribeKey` , and `kms:Decrypt/kms:GenerateDataKey` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow `kms:Decrypt` , `kms:GenerateDataKey*` , and `kms:DescribeKey` permissions to the `connect.amazonaws.com` service principal.

For more information about setting up a customer managed key for Wisdom, see [Enable Amazon Connect Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html) .

kmsKeyId -> (string)

The customer managed key used for encryption. For more information about setting up a customer managed key for Wisdom, see [Enable Amazon Connect Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html) . For information about valid ID values, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) .

Shorthand Syntax:

```
kmsKeyId=string
```

JSON Syntax:

```
{
  "kmsKeyId": "string"
}
```

`--tags` (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--type` (string)

The type of assistant.

Possible values:

- `AGENT`

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

assistant -> (structure)

Information about the assistant.

assistantArn -> (string)

The Amazon Resource Name (ARN) of the Wisdom assistant.

assistantId -> (string)

The identifier of the Wisdom assistant.

description -> (string)

The description.

integrationConfiguration -> (structure)

The configuration information for the Wisdom assistant integration.

topicIntegrationArn -> (string)

The Amazon Resource Name (ARN) of the integrated Amazon SNS topic used for streaming chat messages.

name -> (string)

The name.

serverSideEncryptionConfiguration -> (structure)

The configuration information for the customer managed key used for encryption.

This KMS key must have a policy that allows `kms:CreateGrant` , `kms:DescribeKey` , and `kms:Decrypt/kms:GenerateDataKey` permissions to the IAM identity using the key to invoke Wisdom. To use Wisdom with chat, the key policy must also allow `kms:Decrypt` , `kms:GenerateDataKey*` , and `kms:DescribeKey` permissions to the `connect.amazonaws.com` service principal.

For more information about setting up a customer managed key for Wisdom, see [Enable Amazon Connect Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html) .

kmsKeyId -> (string)

The customer managed key used for encryption. For more information about setting up a customer managed key for Wisdom, see [Enable Amazon Connect Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html) . For information about valid ID values, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) .

status -> (string)

The status of the assistant.

tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

type -> (string)

The type of assistant.