# invoke-data-automation-asyncÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-data-automation-runtime/invoke-data-automation-async.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-data-automation-runtime/invoke-data-automation-async.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-data-automation-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-data-automation-runtime/index.html#cli-aws-bedrock-data-automation-runtime) ]

# invoke-data-automation-async

## Description

Async API: Invoke data automation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync)

## Synopsis

```
invoke-data-automation-async
[--client-token <value>]
--input-configuration <value>
--output-configuration <value>
[--data-automation-configuration <value>]
[--encryption-configuration <value>]
[--notification-configuration <value>]
[--blueprints <value>]
--data-automation-profile-arn <value>
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

`--client-token` (string)

Idempotency token.

`--input-configuration` (structure)

Input configuration.

s3Uri -> (string)

S3 uri.

assetProcessingConfiguration -> (structure)

Asset processing configuration

video -> (structure)

Video asset processing configuration

segmentConfiguration -> (tagged union structure)

Delimits the segment of the input that will be processed

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `timestampSegment`.

timestampSegment -> (structure)

Timestamp segment

startTimeMillis -> (long)

Start timestamp in milliseconds

endTimeMillis -> (long)

End timestamp in milliseconds

JSON Syntax:

```
{
  "s3Uri": "string",
  "assetProcessingConfiguration": {
    "video": {
      "segmentConfiguration": {
        "timestampSegment": {
          "startTimeMillis": long,
          "endTimeMillis": long
        }
      }
    }
  }
}
```

`--output-configuration` (structure)

Output configuration.

s3Uri -> (string)

S3 uri.

Shorthand Syntax:

```
s3Uri=string
```

JSON Syntax:

```
{
  "s3Uri": "string"
}
```

`--data-automation-configuration` (structure)

Data automation configuration.

dataAutomationProjectArn -> (string)

Data automation project arn.

stage -> (string)

Data automation stage.

Shorthand Syntax:

```
dataAutomationProjectArn=string,stage=string
```

JSON Syntax:

```
{
  "dataAutomationProjectArn": "string",
  "stage": "LIVE"|"DEVELOPMENT"
}
```

`--encryption-configuration` (structure)

Encryption configuration.

kmsKeyId -> (string)

Customer KMS key used for encryption

kmsEncryptionContext -> (map)

KMS encryption context.

key -> (string)

Excryption context key.

value -> (string)

Encryption context value.

Shorthand Syntax:

```
kmsKeyId=string,kmsEncryptionContext={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "kmsKeyId": "string",
  "kmsEncryptionContext": {"string": "string"
    ...}
}
```

`--notification-configuration` (structure)

Notification configuration.

eventBridgeConfiguration -> (structure)

Event bridge configuration.

eventBridgeEnabled -> (boolean)

Event bridge flag.

Shorthand Syntax:

```
eventBridgeConfiguration={eventBridgeEnabled=boolean}
```

JSON Syntax:

```
{
  "eventBridgeConfiguration": {
    "eventBridgeEnabled": true|false
  }
}
```

`--blueprints` (list)

Blueprint list.

(structure)

Blueprint.

blueprintArn -> (string)

Arn of blueprint.

version -> (string)

Version of blueprint.

stage -> (string)

Stage of blueprint.

Shorthand Syntax:

```
blueprintArn=string,version=string,stage=string ...
```

JSON Syntax:

```
[
  {
    "blueprintArn": "string",
    "version": "string",
    "stage": "DEVELOPMENT"|"LIVE"
  }
  ...
]
```

`--data-automation-profile-arn` (string)

Data automation profile ARN

`--tags` (list)

List of tags.

(structure)

Key value pair of a tag

key -> (string)

Defines the context of the tag.

value -> (string)

Defines the value within the context. e.g. <key=reason, value=training>.

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

## Output

invocationArn -> (string)

ARN of the automation job