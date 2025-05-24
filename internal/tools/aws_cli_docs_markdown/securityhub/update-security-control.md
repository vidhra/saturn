# update-security-controlÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-security-control.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/update-security-control.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securityhub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html#cli-aws-securityhub) ]

# update-security-control

## Description

Updates the properties of a security control.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/UpdateSecurityControl)

## Synopsis

```
update-security-control
--security-control-id <value>
--parameters <value>
[--last-update-reason <value>]
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

`--security-control-id` (string)

The Amazon Resource Name (ARN) or ID of the control to update.

`--parameters` (map)

An object that specifies which security control parameters to update.

key -> (string)

value -> (structure)

An object that provides the current value of a security control parameter and identifies whether it has been customized.

ValueType -> (string)

Identifies whether a control parameter uses a custom user-defined value or subscribes to the default Security Hub behavior.

When `ValueType` is set equal to `DEFAULT` , the default behavior can be a specific Security Hub default value, or the default behavior can be to ignore a specific parameter. When `ValueType` is set equal to `DEFAULT` , Security Hub ignores user-provided input for the `Value` field.

When `ValueType` is set equal to `CUSTOM` , the `Value` field canât be empty.

Value -> (tagged union structure)

The current value of a control parameter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Integer`, `IntegerList`, `Double`, `String`, `StringList`, `Boolean`, `Enum`, `EnumList`.

Integer -> (integer)

A control parameter that is an integer.

IntegerList -> (list)

A control parameter that is a list of integers.

(integer)

Double -> (double)

A control parameter that is a double.

String -> (string)

A control parameter that is a string.

StringList -> (list)

A control parameter that is a list of strings.

(string)

Boolean -> (boolean)

A control parameter that is a boolean.

Enum -> (string)

A control parameter that is an enum.

EnumList -> (list)

A control parameter that is a list of enums.

(string)

Shorthand Syntax:

```
KeyName1=ValueType=string,Value={Integer=integer,IntegerList=[integer,integer],Double=double,String=string,StringList=[string,string],Boolean=boolean,Enum=string,EnumList=[string,string]},KeyName2=ValueType=string,Value={Integer=integer,IntegerList=[integer,integer],Double=double,String=string,StringList=[string,string],Boolean=boolean,Enum=string,EnumList=[string,string]}
```

JSON Syntax:

```
{"string": {
      "ValueType": "DEFAULT"|"CUSTOM",
      "Value": {
        "Integer": integer,
        "IntegerList": [integer, ...],
        "Double": double,
        "String": "string",
        "StringList": ["string", ...],
        "Boolean": true|false,
        "Enum": "string",
        "EnumList": ["string", ...]
      }
    }
  ...}
```

`--last-update-reason` (string)

The most recent reason for updating the properties of the security control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.

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

**To update security control properties**

The following `update-security-control` example specifies custom values for a Security Hub security control parameter.

```
aws securityhub update-security-control \
    --security-control-id ACM.1 \
    --parameters '{"daysToExpiration": {"ValueType": "CUSTOM", "Value": {"Integer": 15}}}' \
    --last-update-reason "Internal compliance requirement"
```

This command produces no output.

For more information, see [Custom control parameters](https://docs.aws.amazon.com/securityhub/latest/userguide/custom-control-parameters.html) in the *AWS Security Hub User Guide*.

## Output

None