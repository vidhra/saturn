# create-commandÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-command.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-command.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# create-command

## Description

Creates a command. A command contains reusable configurations that can be applied before they are sent to the devices.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateCommand)

## Synopsis

```
create-command
--command-id <value>
[--namespace <value>]
[--display-name <value>]
[--description <value>]
[--payload <value>]
[--mandatory-parameters <value>]
[--role-arn <value>]
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

`--command-id` (string)

A unique identifier for the command. We recommend using UUID. Alpha-numeric characters, hyphens, and underscores are valid for use here.

`--namespace` (string)

The namespace of the command. The MQTT reserved topics and validations will be used for command executions according to the namespace setting.

Possible values:

- `AWS-IoT`
- `AWS-IoT-FleetWise`

`--display-name` (string)

The user-friendly name in the console for the command. This name doesnât have to be unique. You can update the user-friendly name after you define it.

`--description` (string)

A short text decription of the command.

`--payload` (structure)

The payload object for the command. You must specify this information when using the `AWS-IoT` namespace.

You can upload a static payload file from your local storage that contains the instructions for the device to process. The payload file can use any format. To make sure that the device correctly interprets the payload, we recommend you to specify the payload content type.

content -> (blob)

The static payload file for the command.

contentType -> (string)

The content type that specifies the format type of the payload file. This field must use a type/subtype format, such as `application/json` . For information about various content types, see [Common MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/MIME_types/Common_types) .

Shorthand Syntax:

```
content=blob,contentType=string
```

JSON Syntax:

```
{
  "content": blob,
  "contentType": "string"
}
```

`--mandatory-parameters` (list)

A list of parameters that are required by the `StartCommandExecution` API. These parameters need to be specified only when using the `AWS-IoT-FleetWise` namespace. You can either specify them here or when running the command using the `StartCommandExecution` API.

(structure)

A map of key-value pairs that describe the command.

name -> (string)

The name of a specific parameter used in a command and command execution.

value -> (structure)

The value used to describe the command. When you assign a value to a parameter, it will override any default value that you had already specified.

S -> (string)

An attribute of type String. For example:

`"S": "Hello"`

B -> (boolean)

An attribute of type Boolean. For example:

`"BOOL": true`

I -> (integer)

An attribute of type Integer (Thirty-Two Bits).

L -> (long)

An attribute of type Long.

D -> (double)

An attribute of type Double (Sixty-Four Bits).

BIN -> (blob)

An attribute of type Binary. For example:

`"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`

UL -> (string)

An attribute of type unsigned long.

defaultValue -> (structure)

The default value used to describe the command. This is the value assumed by the parameter if no other value is assigned to it.

S -> (string)

An attribute of type String. For example:

`"S": "Hello"`

B -> (boolean)

An attribute of type Boolean. For example:

`"BOOL": true`

I -> (integer)

An attribute of type Integer (Thirty-Two Bits).

L -> (long)

An attribute of type Long.

D -> (double)

An attribute of type Double (Sixty-Four Bits).

BIN -> (blob)

An attribute of type Binary. For example:

`"B": "dGhpcyB0ZXh0IGlzIGJhc2U2NC1lbmNvZGVk"`

UL -> (string)

An attribute of type unsigned long.

description -> (string)

The description of the command parameter.

Shorthand Syntax:

```
name=string,value={S=string,B=boolean,I=integer,L=long,D=double,BIN=blob,UL=string},defaultValue={S=string,B=boolean,I=integer,L=long,D=double,BIN=blob,UL=string},description=string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "value": {
      "S": "string",
      "B": true|false,
      "I": integer,
      "L": long,
      "D": double,
      "BIN": blob,
      "UL": "string"
    },
    "defaultValue": {
      "S": "string",
      "B": true|false,
      "I": integer,
      "L": long,
      "D": double,
      "BIN": blob,
      "UL": "string"
    },
    "description": "string"
  }
  ...
]
```

`--role-arn` (string)

The IAM role that you must provide when using the `AWS-IoT-FleetWise` namespace. The role grants IoT Device Management the permission to access IoT FleetWise resources for generating the payload for the command. This field is not required when you use the `AWS-IoT` namespace.

`--tags` (list)

Name-value pairs that are used as metadata to manage a command.

(structure)

A set of key/value pairs that are used to manage the resource.

Key -> (string)

The tagâs key.

Value -> (string)

The tagâs value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

commandId -> (string)

The unique identifier for the command.

commandArn -> (string)

The Amazon Resource Number (ARN) of the command. For example, `arn:aws:iot:<region>:<accountid>:command/<commandId>`