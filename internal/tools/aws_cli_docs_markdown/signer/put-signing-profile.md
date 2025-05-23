# put-signing-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/put-signing-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/put-signing-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [signer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/signer/index.html#cli-aws-signer) ]

# put-signing-profile

## Description

Creates a signing profile. A signing profile is a code-signing template that can be used to carry out a pre-defined signing job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/signer-2017-08-25/PutSigningProfile)

## Synopsis

```
put-signing-profile
--profile-name <value>
[--signing-material <value>]
[--signature-validity-period <value>]
--platform-id <value>
[--overrides <value>]
[--signing-parameters <value>]
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

`--profile-name` (string)

The name of the signing profile to be created.

`--signing-material` (structure)

The AWS Certificate Manager certificate that will be used to sign code with the new signing profile.

certificateArn -> (string)

The Amazon Resource Name (ARN) of the certificates that is used to sign your code.

Shorthand Syntax:

```
certificateArn=string
```

JSON Syntax:

```
{
  "certificateArn": "string"
}
```

`--signature-validity-period` (structure)

The default validity period override for any signature generated using this signing profile. If unspecified, the default is 135 months.

value -> (integer)

The numerical value of the time unit for signature validity.

type -> (string)

The time unit for signature validity.

Shorthand Syntax:

```
value=integer,type=string
```

JSON Syntax:

```
{
  "value": integer,
  "type": "DAYS"|"MONTHS"|"YEARS"
}
```

`--platform-id` (string)

The ID of the signing platform to be created.

`--overrides` (structure)

A subfield of `platform` . This specifies any different configuration options that you want to apply to the chosen platform (such as a different `hash-algorithm` or `signing-algorithm` ).

signingConfiguration -> (structure)

A signing configuration that overrides the default encryption or hash algorithm of a signing job.

encryptionAlgorithm -> (string)

A specified override of the default encryption algorithm that is used in a code-signing job.

hashAlgorithm -> (string)

A specified override of the default hash algorithm that is used in a code-signing job.

signingImageFormat -> (string)

A signed image is a JSON object. When overriding the default signing platform configuration, a customer can select either of two signing formats, `JSONEmbedded` or `JSONDetached` . (A third format value, `JSON` , is reserved for future use.) With `JSONEmbedded` , the signing image has the payload embedded in it. With `JSONDetached` , the payload is not be embedded in the signing image.

Shorthand Syntax:

```
signingConfiguration={encryptionAlgorithm=string,hashAlgorithm=string},signingImageFormat=string
```

JSON Syntax:

```
{
  "signingConfiguration": {
    "encryptionAlgorithm": "RSA"|"ECDSA",
    "hashAlgorithm": "SHA1"|"SHA256"
  },
  "signingImageFormat": "JSON"|"JSONEmbedded"|"JSONDetached"
}
```

`--signing-parameters` (map)

Map of key-value pairs for signing. These can include any information that you want to use during signing.

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

`--tags` (map)

Tags to be associated with the signing profile that is being created.

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

**To create a signing profile**

The following `put-signing-profile` example creates a signing profile using the specified certificate and platform.

```
aws signer put-signing-profile \
    --profile-name MyProfile6 \
    --signing-material certificateArn=arn:aws:acm:us-west-2:123456789012:certificate/6a55389b-306b-4e8c-a95c-0123456789abc \
    --platform AmazonFreeRTOS-TI-CC3220SF
```

Output:

```
{
    "arn": "arn:aws:signer:us-west-2:123456789012:/signing-profiles/MyProfile6"
}
```

## Output

arn -> (string)

The Amazon Resource Name (ARN) of the signing profile created.

profileVersion -> (string)

The version of the signing profile being created.

profileVersionArn -> (string)

The signing profile ARN, including the profile version.