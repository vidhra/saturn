# get-security-control-definitionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-security-control-definition.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-security-control-definition.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securityhub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html#cli-aws-securityhub) ]

# get-security-control-definition

## Description

Retrieves the definition of a security control. The definition includes the control title, description, Region availability, parameter definitions, and other details.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetSecurityControlDefinition)

## Synopsis

```
get-security-control-definition
--security-control-id <value>
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

The ID of the security control to retrieve the definition for. This field doesnât accept an Amazon Resource Name (ARN).

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

**To get security control definition details**

The following `get-security-control-definition` example retrieves definition details for a Security Hub security control. Details include the control title, description, Region availability, parameters, and other information.

```
aws securityhub get-security-control-definition \
    --security-control-id ACM.1
```

Output:

```
{
    "SecurityControlDefinition": {
        "SecurityControlId": "ACM.1",
        "Title": "Imported and ACM-issued certificates should be renewed after a specified time period",
        "Description": "This control checks whether an AWS Certificate Manager (ACM) certificate is renewed within the specified time period. It checks both imported certificates and certificates provided by ACM. The control fails if the certificate isn't renewed within the specified time period. Unless you provide a custom parameter value for the renewal period, Security Hub uses a default value of 30 days.",
        "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/ACM.1/remediation",
        "SeverityRating": "MEDIUM",
        "CurrentRegionAvailability": "AVAILABLE",
        "ParameterDefinitions": {
            "daysToExpiration": {
                "Description": "Number of days within which the ACM certificate must be renewed",
                "ConfigurationOptions": {
                    "Integer": {
                        "DefaultValue": 30,
                        "Min": 14,
                        "Max": 365
                    }
                }
            }
        }
    }
}
```

For more information, see [Custom control parameters](https://docs.aws.amazon.com/securityhub/latest/userguide/custom-control-parameters.html) in the *AWS Security Hub User Guide*.

## Output

SecurityControlDefinition -> (structure)

Provides metadata for a security control, including its unique standard-agnostic identifier, title, description, severity, availability in Amazon Web Services Regions, and a link to remediation steps.

SecurityControlId -> (string)

The unique identifier of a security control across standards. Values for this field typically consist of an Amazon Web Services service name and a number (for example, APIGateway.3). This parameter differs from `SecurityControlArn` , which is a unique Amazon Resource Name (ARN) assigned to a control. The ARN references the security control ID (for example, arn:aws:securityhub:eu-central-1:123456789012:security-control/APIGateway.3).

Title -> (string)

The title of a security control.

Description -> (string)

The description of a security control across standards. This typically summarizes how Security Hub evaluates the control and the conditions under which it produces a failed finding. This parameter doesnât reference a specific standard.

RemediationUrl -> (string)

A link to Security Hub documentation that explains how to remediate a failed finding for a security control.

SeverityRating -> (string)

The severity of a security control. For more information about how Security Hub determines control severity, see [Assigning severity to control findings](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#control-findings-severity) in the *Security Hub User Guide* .

CurrentRegionAvailability -> (string)

Specifies whether a security control is available in the current Amazon Web Services Region.

CustomizableProperties -> (list)

Security control properties that you can customize. Currently, only parameter customization is supported for select controls. An empty array is returned for controls that donât support custom properties.

(string)

ParameterDefinitions -> (map)

An object that provides a security control parameter name, description, and the options for customizing it. This object is excluded for a control that doesnât support custom parameters.

key -> (string)

value -> (structure)

An object that describes a security control parameter and the options for customizing it.

Description -> (string)

Description of a control parameter.

ConfigurationOptions -> (tagged union structure)

The options for customizing a control parameter. Customization options vary based on the data type of the parameter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Integer`, `IntegerList`, `Double`, `String`, `StringList`, `Boolean`, `Enum`, `EnumList`.

Integer -> (structure)

The options for customizing a security control parameter that is an integer.

DefaultValue -> (integer)

The Security Hub default value for a control parameter that is an integer.

Min -> (integer)

The minimum valid value for a control parameter that is an integer.

Max -> (integer)

The maximum valid value for a control parameter that is an integer.

IntegerList -> (structure)

The options for customizing a security control parameter that is a list of integers.

DefaultValue -> (list)

The Security Hub default value for a control parameter that is a list of integers.

(integer)

Min -> (integer)

The minimum valid value for a control parameter that is a list of integers.

Max -> (integer)

The maximum valid value for a control parameter that is a list of integers.

MaxItems -> (integer)

The maximum number of list items that an interger list control parameter can accept.

Double -> (structure)

The options for customizing a security control parameter that is a double.

DefaultValue -> (double)

The Security Hub default value for a control parameter that is a double.

Min -> (double)

The minimum valid value for a control parameter that is a double.

Max -> (double)

The maximum valid value for a control parameter that is a double.

String -> (structure)

The options for customizing a security control parameter that is a string data type.

DefaultValue -> (string)

The Security Hub default value for a control parameter that is a string.

Re2Expression -> (string)

An RE2 regular expression that Security Hub uses to validate a user-provided control parameter string.

ExpressionDescription -> (string)

The description of the RE2 regular expression.

StringList -> (structure)

The options for customizing a security control parameter that is a list of strings.

DefaultValue -> (list)

The Security Hub default value for a control parameter that is a list of strings.

(string)

Re2Expression -> (string)

An RE2 regular expression that Security Hub uses to validate a user-provided list of strings for a control parameter.

MaxItems -> (integer)

The maximum number of list items that a string list control parameter can accept.

ExpressionDescription -> (string)

The description of the RE2 regular expression.

Boolean -> (structure)

The options for customizing a security control parameter that is a boolean. For a boolean parameter, the options are `true` and `false` .

DefaultValue -> (boolean)

The Security Hub default value for a boolean parameter.

Enum -> (structure)

The options for customizing a security control parameter that is an enum.

DefaultValue -> (string)

The Security Hub default value for a control parameter that is an enum.

AllowedValues -> (list)

The valid values for a control parameter that is an enum.

(string)

EnumList -> (structure)

The options for customizing a security control parameter that is a list of enums.

DefaultValue -> (list)

The Security Hub default value for a control parameter that is a list of enums.

(string)

MaxItems -> (integer)

The maximum number of list items that an enum list control parameter can accept.

AllowedValues -> (list)

The valid values for a control parameter that is a list of enums.

(string)