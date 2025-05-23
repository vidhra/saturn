# update-case-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcases/update-case-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcases/update-case-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connectcases](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connectcases/index.html#cli-aws-connectcases) ]

# update-case-rule

## Description

Updates a case rule. In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connectcases-2022-10-03/UpdateCaseRule)

## Synopsis

```
update-case-rule
--case-rule-id <value>
[--description <value>]
--domain-id <value>
[--name <value>]
[--rule <value>]
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

`--case-rule-id` (string)

Unique identifier of a case rule.

`--description` (string)

Description of a case rule.

`--domain-id` (string)

Unique identifier of a Cases domain.

`--name` (string)

Name of the case rule.

`--rule` (tagged union structure)

Represents what rule type should take place, under what conditions.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `required`.

required -> (structure)

Required rule type, used to indicate whether a field is required.

conditions -> (list)

List of conditions for the required rule; the first condition to evaluate to true dictates the value of the rule.

(tagged union structure)

Boolean condition for a rule. In the Amazon Connect admin website, case rules are known as *case field conditions* . For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `equalTo`, `notEqualTo`.

equalTo -> (structure)

Tests that operandOne is equal to operandTwo.

operandOne -> (tagged union structure)

Represents the left hand operand in the condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fieldId`.

fieldId -> (string)

The field ID that this operand should take the value of.

operandTwo -> (tagged union structure)

Represents the right hand operand in the condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `booleanValue`, `doubleValue`, `emptyValue`, `stringValue`.

booleanValue -> (boolean)

Boolean value type.

doubleValue -> (double)

Double value type.

emptyValue -> (structure)

Empty value type.

stringValue -> (string)

String value type.

result -> (boolean)

The value of the outer rule if the condition evaluates to true.

notEqualTo -> (structure)

Tests that operandOne is not equal to operandTwo.

operandOne -> (tagged union structure)

Represents the left hand operand in the condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fieldId`.

fieldId -> (string)

The field ID that this operand should take the value of.

operandTwo -> (tagged union structure)

Represents the right hand operand in the condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `booleanValue`, `doubleValue`, `emptyValue`, `stringValue`.

booleanValue -> (boolean)

Boolean value type.

doubleValue -> (double)

Double value type.

emptyValue -> (structure)

Empty value type.

stringValue -> (string)

String value type.

result -> (boolean)

The value of the outer rule if the condition evaluates to true.

defaultValue -> (boolean)

The value of the rule (that is, whether the field is required) should none of the conditions evaluate to true.

JSON Syntax:

```
{
  "required": {
    "conditions": [
      {
        "equalTo": {
          "operandOne": {
            "fieldId": "string"
          },
          "operandTwo": {
            "booleanValue": true|false,
            "doubleValue": double,
            "emptyValue": {

            },
            "stringValue": "string"
          },
          "result": true|false
        },
        "notEqualTo": {
          "operandOne": {
            "fieldId": "string"
          },
          "operandTwo": {
            "booleanValue": true|false,
            "doubleValue": double,
            "emptyValue": {

            },
            "stringValue": "string"
          },
          "result": true|false
        }
      }
      ...
    ],
    "defaultValue": true|false
  }
}
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

None