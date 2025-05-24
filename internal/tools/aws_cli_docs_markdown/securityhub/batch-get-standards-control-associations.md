# batch-get-standards-control-associationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-standards-control-associations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/batch-get-standards-control-associations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [securityhub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/securityhub/index.html#cli-aws-securityhub) ]

# batch-get-standards-control-associations

## Description

For a batch of security controls and standards, identifies whether each control is currently enabled or disabled in a standard.

Calls to this operation return a `RESOURCE_NOT_FOUND_EXCEPTION` error when the standard subscription for the association has a `NOT_READY_FOR_UPDATES` value for `StandardsControlsUpdatable` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/securityhub-2018-10-26/BatchGetStandardsControlAssociations)

## Synopsis

```
batch-get-standards-control-associations
--standards-control-association-ids <value>
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

`--standards-control-association-ids` (list)

An array with one or more objects that includes a security control (identified with `SecurityControlId` , `SecurityControlArn` , or a mix of both parameters) and the Amazon Resource Name (ARN) of a standard. This field is used to query the enablement status of a control in a specified standard. The security control ID or ARN is the same across standards.

(structure)

An array with one or more objects that includes a security control (identified with `SecurityControlId` , `SecurityControlArn` , or a mix of both parameters) and the Amazon Resource Name (ARN) of a standard. The security control ID or ARN is the same across standards.

SecurityControlId -> (string)

The unique identifier (identified with `SecurityControlId` , `SecurityControlArn` , or a mix of both parameters) of a security control across standards.

StandardsArn -> (string)

The ARN of a standard.

Shorthand Syntax:

```
SecurityControlId=string,StandardsArn=string ...
```

JSON Syntax:

```
[
  {
    "SecurityControlId": "string",
    "StandardsArn": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To get the enablement status of a control**

The following `batch-get-standards-control-associations` example identifies whether the specified controls are enabled in the specified standards.

```
aws securityhub batch-get-standards-control-associations \
    --standards-control-association-ids '[{"SecurityControlId": "Config.1","StandardsArn": "arn:aws:securityhub:us-east-1:123456789012:ruleset/cis-aws-foundations-benchmark/v/1.2.0"}, {"SecurityControlId": "IAM.6","StandardsArn": "arn:aws:securityhub:us-east-1:123456789012:standards/aws-foundational-security-best-practices/v/1.0.0"}]'
```

Output:

```
{
    "StandardsControlAssociationDetails": [
        {
            "StandardsArn": "arn:aws:securityhub:::ruleset/cis-aws-foundations-benchmark/v/1.2.0",
            "SecurityControlId": "Config.1",
            "SecurityControlArn": "arn:aws:securityhub:us-east-1:068873283051:security-control/Config.1",
            "AssociationStatus": "ENABLED",
            "RelatedRequirements": [
                "CIS AWS Foundations 2.5"
            ],
            "UpdatedAt": "2022-10-27T16:07:12.960000+00:00",
            "StandardsControlTitle": "Ensure AWS Config is enabled",
            "StandardsControlDescription": "AWS Config is a web service that performs configuration management of supported AWS resources within your account and delivers log files to you. The recorded information includes the configuration item (AWS resource), relationships between configuration items (AWS resources), and any configuration changes between resources. It is recommended to enable AWS Config in all regions.",
            "StandardsControlArns": [
                "arn:aws:securityhub:us-east-1:068873283051:control/cis-aws-foundations-benchmark/v/1.2.0/2.5"
            ]
        },
        {
            "StandardsArn": "arn:aws:securityhub:us-east-1::standards/aws-foundational-security-best-practices/v/1.0.0",
            "SecurityControlId": "IAM.6",
            "SecurityControlArn": "arn:aws:securityhub:us-east-1:068873283051:security-control/IAM.6",
            "AssociationStatus": "DISABLED",
            "RelatedRequirements": [],
            "UpdatedAt": "2022-11-22T21:30:35.080000+00:00",
            "UpdatedReason": "test",
            "StandardsControlTitle": "Hardware MFA should be enabled for the root user",
            "StandardsControlDescription": "This AWS control checks whether your AWS account is enabled to use a hardware multi-factor authentication (MFA) device to sign in with root user credentials.",
            "StandardsControlArns": [
                "arn:aws:securityhub:us-east-1:068873283051:control/aws-foundational-security-best-practices/v/1.0.0/IAM.6"
            ]
        }
    ]
}
```

For more information, see [Enabling and disabling controls in specific standards](https://docs.aws.amazon.com/securityhub/latest/userguide/controls-configure.html) in the *AWS Security Hub User Guide*.

## Output

StandardsControlAssociationDetails -> (list)

Provides the enablement status of a security control in a specified standard and other details for the control in relation to the specified standard.

(structure)

Provides details about a controlâs enablement status in a specified standard.

StandardsArn -> (string)

The Amazon Resource Name (ARN) of a security standard.

SecurityControlId -> (string)

The unique identifier of a security control across standards. Values for this field typically consist of an Amazon Web Services service name and a number, such as APIGateway.3.

SecurityControlArn -> (string)

The ARN of a security control across standards, such as `arn:aws:securityhub:eu-central-1:123456789012:security-control/S3.1` . This parameter doesnât mention a specific standard.

AssociationStatus -> (string)

Specifies whether a control is enabled or disabled in a specified standard.

RelatedRequirements -> (list)

The requirement that underlies a control in the compliance framework related to the standard.

(string)

UpdatedAt -> (timestamp)

The time at which the enablement status of the control in the specified standard was last updated.

UpdatedReason -> (string)

The reason for updating the enablement status of a control in a specified standard.

StandardsControlTitle -> (string)

The title of a control. This field may reference a specific standard.

StandardsControlDescription -> (string)

The description of a control. This typically summarizes how Security Hub evaluates the control and the conditions under which it produces a failed finding. This parameter may reference a specific standard.

StandardsControlArns -> (list)

Provides the input parameter that Security Hub uses to call the [UpdateStandardsControl](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateStandardsControl.html) API. This API can be used to enable or disable a control in a specified standard.

(string)

UnprocessedAssociations -> (list)

A security control (identified with `SecurityControlId` , `SecurityControlArn` , or a mix of both parameters) whose enablement status in a specified standard cannot be returned.

(structure)

Provides details about which controlâs enablement status couldnât be retrieved in a specified standard when calling [BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html) . This parameter also provides details about why the request was unprocessed.

StandardsControlAssociationId -> (structure)

An array with one or more objects that includes a security control (identified with `SecurityControlId` , `SecurityControlArn` , or a mix of both parameters) and the Amazon Resource Name (ARN) of a standard. This parameter shows the specific controls for which the enablement status couldnât be retrieved in specified standards when calling [BatchUpdateStandardsControlAssociations](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchUpdateStandardsControlAssociations.html) .

SecurityControlId -> (string)

The unique identifier (identified with `SecurityControlId` , `SecurityControlArn` , or a mix of both parameters) of a security control across standards.

StandardsArn -> (string)

The ARN of a standard.

ErrorCode -> (string)

The error code for the unprocessed standard and control association.

ErrorReason -> (string)

The reason why the standard and control association was unprocessed.