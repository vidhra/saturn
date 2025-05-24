# list-security-control-definitionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-security-control-definitions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/list-security-control-definitions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securityhub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html#cli-aws-securityhub) ]

# list-security-control-definitions

## Description

Lists all of the security controls that apply to a specified standard.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/ListSecurityControlDefinitions)

`list-security-control-definitions` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `SecurityControlDefinitions`

## Synopsis

```
list-security-control-definitions
[--standards-arn <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--standards-arn` (string)

The Amazon Resource Name (ARN) of the standard that you want to view controls for.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**Example 1: To list all available security controls**

The following `list-security-control-definitions` example lists the available security controls across all Security Hub standards. This example limits the results to three controls.

```
aws securityhub list-security-control-definitions \
    --max-items 3
```

Output:

```
{
    "SecurityControlDefinitions": [
        {
            "SecurityControlId": "ACM.1",
            "Title": "Imported and ACM-issued certificates should be renewed after a specified time period",
            "Description": "This control checks whether an AWS Certificate Manager (ACM) certificate is renewed within the specified time period. It checks both imported certificates and certificates provided by ACM. The control fails if the certificate isn't renewed within the specified time period. Unless you provide a custom parameter value for the renewal period, Security Hub uses a default value of 30 days.",
            "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/ACM.1/remediation",
            "SeverityRating": "MEDIUM",
            "CurrentRegionAvailability": "AVAILABLE",
            "CustomizableProperties": [
                "Parameters"
            ]
        },
        {
            "SecurityControlId": "ACM.2",
            "Title": "RSA certificates managed by ACM should use a key length of at least 2,048 bits",
            "Description": "This control checks whether RSA certificates managed by AWS Certificate Manager use a key length of at least 2,048 bits. The control fails if the key length is smaller than 2,048 bits.",
            "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/ACM.2/remediation",
            "SeverityRating": "HIGH",
            "CurrentRegionAvailability": "AVAILABLE",
            "CustomizableProperties": []
        },
        {
            "SecurityControlId": "APIGateway.1",
            "Title": "API Gateway REST and WebSocket API execution logging should be enabled",
            "Description": "This control checks whether all stages of an Amazon API Gateway REST or WebSocket API have logging enabled. The control fails if the 'loggingLevel' isn't 'ERROR' or 'INFO' for all stages of the API. Unless you provide custom parameter values to indicate that a specific log type should be enabled, Security Hub produces a passed finding if the logging level is either 'ERROR' or 'INFO'.",
            "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/APIGateway.1/remediation",
            "SeverityRating": "MEDIUM",
            "CurrentRegionAvailability": "AVAILABLE",
            "CustomizableProperties": [
                "Parameters"
            ]
        }
    ],
    "NextToken": "U2FsdGVkX1/UprCPzxVbkDeHikDXbDxfgJZ1w2RG1XWsFPTMTIQPVE0m/FduIGxS7ObRtAbaUt/8/RCQcg2PU0YXI20hH/GrhoOTgv+TSm0qvQVFhkJepWmqh+NYawjocVBeos6xzn/8qnbF9IuwGg=="
}
```

For more information, see [Viewing details for a standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-view-controls.html) in the *AWS Security Hub User Guide*.

**Example 2: To list available security controls for a specific standard**

The following `list-security-control-definitions` example lists the available security controls for the CIS AWS Foundations Benchmark v1.4.0. This example limits the results to three controls.

```
aws securityhub list-security-control-definitions \
    --standards-arn "arn:aws:securityhub:us-east-1::standards/cis-aws-foundations-benchmark/v/1.4.0" \
    --max-items 3
```

Output:

```
{
    "SecurityControlDefinitions": [
        {
            "SecurityControlId": "CloudTrail.1",
            "Title": "CloudTrail should be enabled and configured with at least one multi-Region trail that includes read and write management events",
            "Description": "This AWS control checks that there is at least one multi-region AWS CloudTrail trail includes read and write management events.",
            "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/CloudTrail.1/remediation",
            "SeverityRating": "HIGH",
            "CurrentRegionAvailability": "AVAILABLE",
            "CustomizableProperties": []
        },
        {
            "SecurityControlId": "CloudTrail.2",
            "Title": "CloudTrail should have encryption at-rest enabled",
            "Description": "This AWS control checks whether AWS CloudTrail is configured to use the server side encryption (SSE) AWS Key Management Service (AWS KMS) customer master key (CMK) encryption. The check will pass if the KmsKeyId is defined.",
            "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/CloudTrail.2/remediation",
            "SeverityRating": "MEDIUM",
            "CurrentRegionAvailability": "AVAILABLE",
            "CustomizableProperties": []
        },
        {
            "SecurityControlId": "CloudTrail.4",
            "Title": "CloudTrail log file validation should be enabled",
            "Description": "This AWS control checks whether CloudTrail log file validation is enabled.",
            "RemediationUrl": "https://docs.aws.amazon.com/console/securityhub/CloudTrail.4/remediation",
            "SeverityRating": "MEDIUM",
            "CurrentRegionAvailability": "AVAILABLE",
            "CustomizableProperties": []
        }
    ],
    "NextToken": "eyJOZXh0VG9rZW4iOiBudWxsLCAiYm90b190cnVuY2F0ZV9hbW91bnQiOiAzfQ=="
}
```

For more information, see [Viewing details for a standard](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-view-controls.html) in the *AWS Security Hub User Guide*.

## Output

SecurityControlDefinitions -> (list)

An array of controls that apply to the specified standard.

(structure)

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

NextToken -> (string)

A pagination parameter thatâs included in the response only if it was included in the request.