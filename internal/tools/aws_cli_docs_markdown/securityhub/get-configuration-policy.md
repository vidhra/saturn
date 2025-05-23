# get-configuration-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-configuration-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/get-configuration-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securityhub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html#cli-aws-securityhub) ]

# get-configuration-policy

## Description

Provides information about a configuration policy. Only the Security Hub delegated administrator can invoke this operation from the home Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/GetConfigurationPolicy)

## Synopsis

```
get-configuration-policy
--identifier <value>
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

`--identifier` (string)

The Amazon Resource Name (ARN) or universally unique identifier (UUID) of the configuration policy.

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

**To view configuration policy details**

The following `get-configuration-policy` example retrieves details about the specified configuration policy.

```
aws securityhub get-configuration-policy \
   --identifier "arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
```

Output:

```
{
    "Arn": "arn:aws:securityhub:eu-central-1:123456789012:configuration-policy/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
    "Id": "ce5ed1e7-9639-4e2f-9313-fa87fcef944b",
    "Name": "SampleConfigurationPolicy",
    "Description": "SampleDescription",
    "UpdatedAt": "2023-11-28T20:28:04.494000+00:00",
    "CreatedAt": "2023-11-28T20:28:04.494000+00:00",
    "ConfigurationPolicy": {
        "SecurityHub": {
            "ServiceEnabled": true,
            "EnabledStandardIdentifiers": [
                "arn:aws:securityhub:eu-central-1::standards/aws-foundational-security-best-practices/v/1.0.0",
                "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0"
            ],
            "SecurityControlsConfiguration": {
                "DisabledSecurityControlIdentifiers": [
                    "CloudTrail.2"
                ],
                "SecurityControlCustomParameters": [
                    {
                        "SecurityControlId": "ACM.1",
                        "Parameters": {
                            "daysToExpiration": {
                                "ValueType": "CUSTOM",
                                "Value": {
                                    "Integer": 15
                                }
                            }
                        }
                    }
                ]
            }
        }
    }
}
```

For more information, see [Viewing Security Hub configuration policies](https://docs.aws.amazon.com/securityhub/latest/userguide/view-policy.html) in the *AWS Security Hub User Guide*.

## Output

Arn -> (string)

The ARN of the configuration policy.

Id -> (string)

The UUID of the configuration policy.

Name -> (string)

The name of the configuration policy.

Description -> (string)

The description of the configuration policy.

UpdatedAt -> (timestamp)

The date and time, in UTC and ISO 8601 format, that the configuration policy was last updated.

CreatedAt -> (timestamp)

The date and time, in UTC and ISO 8601 format, that the configuration policy was created.

ConfigurationPolicy -> (tagged union structure)

An object that defines how Security Hub is configured. It includes whether Security Hub is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If the policy includes a list of security controls that are enabled, Security Hub disables all other controls (including newly released controls). If the policy includes a list of security controls that are disabled, Security Hub enables all other controls (including newly released controls).

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `SecurityHub`.

SecurityHub -> (structure)

The Amazon Web Services service that the configuration policy applies to.

ServiceEnabled -> (boolean)

Indicates whether Security Hub is enabled in the policy.

EnabledStandardIdentifiers -> (list)

A list that defines which security standards are enabled in the configuration policy.

(string)

SecurityControlsConfiguration -> (structure)

An object that defines which security controls are enabled in the configuration policy. The enablement status of a control is aligned across all of the enabled standards in an account.

EnabledSecurityControlIdentifiers -> (list)

A list of security controls that are enabled in the configuration policy. Security Hub disables all other controls (including newly released controls) other than the listed controls.

(string)

DisabledSecurityControlIdentifiers -> (list)

A list of security controls that are disabled in the configuration policy. Security Hub enables all other controls (including newly released controls) other than the listed controls.

(string)

SecurityControlCustomParameters -> (list)

A list of security controls and control parameter values that are included in a configuration policy.

(structure)

A list of security controls and control parameter values that are included in a configuration policy.

SecurityControlId -> (string)

The ID of the security control.

Parameters -> (map)

An object that specifies parameter values for a control in a configuration policy.

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