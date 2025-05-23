# get-ops-itemÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-ops-item.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-ops-item.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# get-ops-item

## Description

Get information about an OpsItem by using the ID. You must have permission in Identity and Access Management (IAM) to view information about an OpsItem. For more information, see [Set up OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-setup.html) in the *Amazon Web Services Systems Manager User Guide* .

Operations engineers and IT professionals use Amazon Web Services Systems Manager OpsCenter to view, investigate, and remediate operational issues impacting the performance and health of their Amazon Web Services resources. For more information, see [Amazon Web Services Systems Manager OpsCenter](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) in the *Amazon Web Services Systems Manager User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetOpsItem)

## Synopsis

```
get-ops-item
--ops-item-id <value>
[--ops-item-arn <value>]
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

`--ops-item-id` (string)

The ID of the OpsItem that you want to get.

`--ops-item-arn` (string)

The OpsItem Amazon Resource Name (ARN).

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

**To view information about an OpsItem**

The following `get-ops-item` example displays details about the specified OpsItem.

```
aws ssm get-ops-item \
    --ops-item-id oi-0b725EXAMPLE
```

Output:

```
{
    "OpsItem": {
        "CreatedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE",
        "CreatedTime": "2019-12-04T15:52:16.793000-08:00",
        "Description": "CloudWatch Event Rule SSMOpsItems-EC2-instance-terminated was triggered. Your EC2 instance has terminated. See below for more details.",
        "LastModifiedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE",
        "LastModifiedTime": "2019-12-04T15:52:16.793000-08:00",
        "Notifications": [],
        "RelatedOpsItems": [],
        "Status": "Open",
        "OpsItemId": "oi-0b725EXAMPLE",
        "Title": "EC2 instance terminated",
        "Source": "EC2",
        "OperationalData": {
            "/aws/automations": {
                "Value": "[ { \"automationType\": \"AWS:SSM:Automation\", \"automationId\": \"AWS-CreateManagedWindowsInstance\" }, { \"automationType\": \"AWS:SSM:Automation\", \"automationId\": \"AWS-CreateManagedLinuxInstance\" } ]",
                "Type": "SearchableString"
            },
            "/aws/dedup": {
                "Value": "{\"dedupString\":\"SSMOpsItems-EC2-instance-terminated\"}",
                "Type": "SearchableString"
            },
            "/aws/resources": {
                "Value": "[{\"arn\":\"arn:aws:ec2:us-east-2:111222333444:instance/i-05adec7e97EXAMPLE\"}]",
                "Type": "SearchableString"
            },
            "event-time": {
                "Value": "2019-12-04T23:52:16Z",
                "Type": "String"
            },
            "instance-state": {
                "Value": "terminated",
                "Type": "String"
            }
        },
        "Category": "Availability",
        "Severity": "4"
    }
}
```

For more information, see [Working with OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html) in the *AWS Systems Manager User Guide*.

## Output

OpsItem -> (structure)

The OpsItem.

CreatedBy -> (string)

The ARN of the Amazon Web Services account that created the OpsItem.

OpsItemType -> (string)

The type of OpsItem. Systems Manager supports the following types of OpsItems:

- `/aws/issue`   This type of OpsItem is used for default OpsItems created by OpsCenter.
- `/aws/changerequest`   This type of OpsItem is used by Change Manager for reviewing and approving or rejecting change requests.
- `/aws/insight`   This type of OpsItem is used by OpsCenter for aggregating and reporting on duplicate OpsItems.

CreatedTime -> (timestamp)

The date and time the OpsItem was created.

Description -> (string)

The OpsItem description.

LastModifiedBy -> (string)

The ARN of the Amazon Web Services account that last updated the OpsItem.

LastModifiedTime -> (timestamp)

The date and time the OpsItem was last updated.

Notifications -> (list)

The Amazon Resource Name (ARN) of an Amazon Simple Notification Service (Amazon SNS) topic where notifications are sent when this OpsItem is edited or changed.

(structure)

A notification about the OpsItem.

Arn -> (string)

The Amazon Resource Name (ARN) of an Amazon Simple Notification Service (Amazon SNS) topic where notifications are sent when this OpsItem is edited or changed.

Priority -> (integer)

The importance of this OpsItem in relation to other OpsItems in the system.

RelatedOpsItems -> (list)

One or more OpsItems that share something in common with the current OpsItem. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.

(structure)

An OpsItems that shares something in common with the current OpsItem. For example, related OpsItems can include OpsItems with similar error messages, impacted resources, or statuses for the impacted resource.

OpsItemId -> (string)

The ID of an OpsItem related to the current OpsItem.

Status -> (string)

The OpsItem status. For more information, see [Editing OpsItem details](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems-editing-details.html) in the *Amazon Web Services Systems Manager User Guide* .

OpsItemId -> (string)

The ID of the OpsItem.

Version -> (string)

The version of this OpsItem. Each time the OpsItem is edited the version number increments by one.

Title -> (string)

A short heading that describes the nature of the OpsItem and the impacted resource.

Source -> (string)

The origin of the OpsItem, such as Amazon EC2 or Systems Manager. The impacted resource is a subset of source.

OperationalData -> (map)

Operational data is custom data that provides useful reference details about the OpsItem. For example, you can specify log files, error strings, license keys, troubleshooting tips, or other relevant data. You enter operational data as key-value pairs. The key has a maximum length of 128 characters. The value has a maximum size of 20 KB.

### Warning

Operational data keys *canât* begin with the following: `amazon` , `aws` , `amzn` , `ssm` , `/amazon` , `/aws` , `/amzn` , `/ssm` .

You can choose to make the data searchable by other users in the account or you can restrict search access. Searchable data means that all users with access to the OpsItem Overview page (as provided by the  DescribeOpsItems API operation) can view and search on the specified data. Operational data that isnât searchable is only viewable by users who have access to the OpsItem (as provided by the  GetOpsItem API operation).

Use the `/aws/resources` key in OperationalData to specify a related resource in the request. Use the `/aws/automations` key in OperationalData to associate an Automation runbook with the OpsItem. To view Amazon Web Services CLI example commands that use these keys, see [Creating OpsItems manually](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-manually-create-OpsItems.html) in the *Amazon Web Services Systems Manager User Guide* .

key -> (string)

value -> (structure)

An object that defines the value of the key and its type in the OperationalData map.

Value -> (string)

The value of the OperationalData key.

Type -> (string)

The type of key-value pair. Valid types include `SearchableString` and `String` .

Category -> (string)

An OpsItem category. Category options include: Availability, Cost, Performance, Recovery, Security.

Severity -> (string)

The severity of the OpsItem. Severity options range from 1 to 4.

ActualStartTime -> (timestamp)

The time a runbook workflow started. Currently reported only for the OpsItem type `/aws/changerequest` .

ActualEndTime -> (timestamp)

The time a runbook workflow ended. Currently reported only for the OpsItem type `/aws/changerequest` .

PlannedStartTime -> (timestamp)

The time specified in a change request for a runbook workflow to start. Currently supported only for the OpsItem type `/aws/changerequest` .

PlannedEndTime -> (timestamp)

The time specified in a change request for a runbook workflow to end. Currently supported only for the OpsItem type `/aws/changerequest` .

OpsItemArn -> (string)

The OpsItem Amazon Resource Name (ARN).