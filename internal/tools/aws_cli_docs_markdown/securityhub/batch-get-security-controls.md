# batch-get-security-controlsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-security-controls.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-security-controls.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securityhub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html#cli-aws-securityhub) ]

# batch-get-security-controls

## Description

Provides details about a batch of security controls for the current Amazon Web Services account and Amazon Web Services Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchGetSecurityControls)

## Synopsis

```
batch-get-security-controls
--security-control-ids <value>
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

`--security-control-ids` (list)

A list of security controls (identified with `SecurityControlId` , `SecurityControlArn` , or a mix of both parameters). The security control ID or Amazon Resource Name (ARN) is the same across standards.

(string)

Syntax:

```
"string" "string" ...
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

**To get security control details**

The following `batch-get-security-controls` example gets details for the security controls ACM.1 and IAM.1 in the current AWS account and AWS Region.

```
aws securityhub batch-get-security-controls \
    --security-control-ids '["ACM.1", "IAM.1"]'
```

Output:

```
{
    "SecurityControls": [
        {
            "SecurityControlId": "ACM.1",
            "SecurityControlArn": "arn:aws:securityhub:us-east-2:123456789012:security-control/ACM.1",
            "Title": "Imported and ACM-issued certificates should be renewed after a specified time period",
            "Description": "This control checks whether an AWS Certificate Manager (ACM) certificate is renewed within the specified time period. It checks both imported certificates and certificates provided by ACM. The control fails if the certificate isn't renewed within the specified time period. Unless you provide a custom parameter value for the renewal period, Security Hub uses a default value of 30 days.",
            "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/ACM.1/remediation",
            "SeverityRating": "MEDIUM",
            "SecurityControlStatus": "ENABLED"
            "UpdateStatus": "READY",
            "Parameters": {
                "daysToExpiration": {
                    "ValueType": CUSTOM,
                    "Value": {
                        "Integer": 15
                    }
                }
            },
            "LastUpdateReason": "Updated control parameter"
        },
        {
            "SecurityControlId": "IAM.1",
            "SecurityControlArn": "arn:aws:securityhub:us-east-2:123456789012:security-control/IAM.1",
            "Title": "IAM policies should not allow full \"*\" administrative privileges",
            "Description": "This AWS control checks whether the default version of AWS Identity and Access Management (IAM) policies (also known as customer managed policies) do not have administrator access with a statement that has \"Effect\": \"Allow\" with \"Action\": \"*\" over \"Resource\": \"*\". It only checks for the Customer Managed Policies that you created, but not inline and AWS Managed Policies.",
            "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/IAM.1/remediation",
            "SeverityRating": "HIGH",
            "SecurityControlStatus": "ENABLED"
            "UpdateStatus": "READY",
            "Parameters": {}
        }
    ]
}
```

For more information, see [Viewing details for a control](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-control-details.html) in the *AWS Security Hub User Guide*.

## Output

SecurityControls -> (list)

An array that returns the identifier, Amazon Resource Name (ARN), and other details about a security control. The same information is returned whether the request includes `SecurityControlId` or `SecurityControlArn` .

(structure)

A security control in Security Hub describes a security best practice related to a specific resource.

SecurityControlId -> (string)

The unique identifier of a security control across standards. Values for this field typically consist of an Amazon Web Services service name and a number, such as APIGateway.3.

SecurityControlArn -> (string)

The Amazon Resource Name (ARN) for a security control across standards, such as `arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1` . This parameter doesnât mention a specific standard.

Title -> (string)

The title of a security control.

Description -> (string)

The description of a security control across standards. This typically summarizes how Security Hub evaluates the control and the conditions under which it produces a failed finding. This parameter doesnât reference a specific standard.

RemediationUrl -> (string)

A link to Security Hub documentation that explains how to remediate a failed finding for a security control.

SeverityRating -> (string)

The severity of a security control. For more information about how Security Hub determines control severity, see [Assigning severity to control findings](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-findings-create-update.html#control-findings-severity) in the *Security Hub User Guide* .

SecurityControlStatus -> (string)

The enablement status of a security control in a specific standard.

UpdateStatus -> (string)

Identifies whether customizable properties of a security control are reflected in Security Hub findings. A status of `READY` indicates that Security Hub uses the current control parameter values when running security checks of the control. A status of `UPDATING` indicates that all security checks might not use the current parameter values.

Parameters -> (map)

An object that identifies the name of a control parameter, its current value, and whether it has been customized.

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

LastUpdateReason -> (string)

The most recent reason for updating the customizable properties of a security control. This differs from the `UpdateReason` field of the ` `BatchUpdateStandardsControlAssociations` [https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations).html`__ API, which tracks the reason for updating the enablement status of a control. This field accepts alphanumeric characters in addition to white spaces, dashes, and underscores.

UnprocessedIds -> (list)

A security control (identified with `SecurityControlId` , `SecurityControlArn` , or a mix of both parameters) for which details cannot be returned.

(structure)

Provides details about a security control for which a response couldnât be returned.

SecurityControlId -> (string)

The control (identified with `SecurityControlId` , `SecurityControlArn` , or a mix of both parameters) for which a response couldnât be returned.

ErrorCode -> (string)

The error code for the unprocessed security control.

ErrorReason -> (string)

The reason why the security control was unprocessed.