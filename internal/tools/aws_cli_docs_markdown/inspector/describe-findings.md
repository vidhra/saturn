# describe-findingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-findings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-findings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/index.html#cli-aws-inspector) ]

# describe-findings

## Description

Describes the findings that are specified by the ARNs of the findings.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeFindings)

## Synopsis

```
describe-findings
--finding-arns <value>
[--locale <value>]
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

`--finding-arns` (list)

The ARN that specifies the finding that you want to describe.

(string)

Syntax:

```
"string" "string" ...
```

`--locale` (string)

The locale into which you want to translate a finding description, recommendation, and the short description that identifies the finding.

Possible values:

- `EN_US`

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

**To describe findings**

The following `describe-findings` command describes the finding with the ARN of `arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4`:

```
aws inspector describe-findings --finding-arns arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4
```

Output:

```
{
      "failedItems": {},
      "findings": [
        {
              "arn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE/finding/0-HwPnsDm4",
              "assetAttributes": {
                "ipv4Addresses": [],
                "schemaVersion": 1
              },
              "assetType": "ec2-instance",
              "attributes": [],
              "confidence": 10,
              "createdAt": 1458680301.37,
              "description": "Amazon Inspector did not find any potential security issues during this assessment.",
              "indicatorOfCompromise": false,
              "numericSeverity": 0,
              "recommendation": "No remediation needed.",
              "schemaVersion": 1,
              "service": "Inspector",
              "serviceAttributes": {
                "assessmentRunArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE",
                "rulesPackageArn": "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP",
                "schemaVersion": 1
              },
              "severity": "Informational",
              "title": "No potential security issues found",
              "updatedAt": 1458680301.37,
              "userAttributes": []
        }
      ]
}
```

For more information, see [Amazon Inspector Findings](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_findings.html) in the *Amazon Inspector* guide.

## Output

findings -> (list)

Information about the finding.

(structure)

Contains information about an Amazon Inspector finding. This data type is used as the response element in the  DescribeFindings action.

arn -> (string)

The ARN that specifies the finding.

schemaVersion -> (integer)

The schema version of this data type.

service -> (string)

The data element is set to âInspectorâ.

serviceAttributes -> (structure)

This data type is used in the  Finding data type.

schemaVersion -> (integer)

The schema version of this data type.

assessmentRunArn -> (string)

The ARN of the assessment run during which the finding is generated.

rulesPackageArn -> (string)

The ARN of the rules package that is used to generate the finding.

assetType -> (string)

The type of the host from which the finding is generated.

assetAttributes -> (structure)

A collection of attributes of the host from which the finding is generated.

schemaVersion -> (integer)

The schema version of this data type.

agentId -> (string)

The ID of the agent that is installed on the EC2 instance where the finding is generated.

autoScalingGroup -> (string)

The Auto Scaling group of the EC2 instance where the finding is generated.

amiId -> (string)

The ID of the Amazon Machine Image (AMI) that is installed on the EC2 instance where the finding is generated.

hostname -> (string)

The hostname of the EC2 instance where the finding is generated.

ipv4Addresses -> (list)

The list of IP v4 addresses of the EC2 instance where the finding is generated.

(string)

tags -> (list)

The tags related to the EC2 instance where the finding is generated.

(structure)

A key and value pair. This data type is used as a request parameter in the  SetTagsForResource action and a response element in the  ListTagsForResource action.

key -> (string)

A tag key.

value -> (string)

A value assigned to a tag key.

networkInterfaces -> (list)

An array of the network interfaces interacting with the EC2 instance where the finding is generated.

(structure)

Contains information about the network interfaces interacting with an EC2 instance. This data type is used as one of the elements of the  AssetAttributes data type.

networkInterfaceId -> (string)

The ID of the network interface.

subnetId -> (string)

The ID of a subnet associated with the network interface.

vpcId -> (string)

The ID of a VPC associated with the network interface.

privateDnsName -> (string)

The name of a private DNS associated with the network interface.

privateIpAddress -> (string)

The private IP address associated with the network interface.

privateIpAddresses -> (list)

A list of the private IP addresses associated with the network interface. Includes the privateDnsName and privateIpAddress.

(structure)

Contains information about a private IP address associated with a network interface. This data type is used as a response element in the  DescribeFindings action.

privateDnsName -> (string)

The DNS name of the private IP address.

privateIpAddress -> (string)

The full IP address of the network inteface.

publicDnsName -> (string)

The name of a public DNS associated with the network interface.

publicIp -> (string)

The public IP address from which the network interface is reachable.

ipv6Addresses -> (list)

The IP addresses associated with the network interface.

(string)

securityGroups -> (list)

A list of the security groups associated with the network interface. Includes the groupId and groupName.

(structure)

Contains information about a security group associated with a network interface. This data type is used as one of the elements of the  NetworkInterface data type.

groupName -> (string)

The name of the security group.

groupId -> (string)

The ID of the security group.

id -> (string)

The ID of the finding.

title -> (string)

The name of the finding.

description -> (string)

The description of the finding.

recommendation -> (string)

The recommendation for the finding.

severity -> (string)

The finding severity. Values can be set to High, Medium, Low, and Informational.

numericSeverity -> (double)

The numeric value of the finding severity.

confidence -> (integer)

This data element is currently not used.

indicatorOfCompromise -> (boolean)

This data element is currently not used.

attributes -> (list)

The system-defined attributes for the finding.

(structure)

This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

key -> (string)

The attribute key.

value -> (string)

The value assigned to the attribute key.

userAttributes -> (list)

The user-defined attributes that are assigned to the finding.

(structure)

This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

key -> (string)

The attribute key.

value -> (string)

The value assigned to the attribute key.

createdAt -> (timestamp)

The time when the finding was generated.

updatedAt -> (timestamp)

The time when  AddAttributesToFindings is called.

failedItems -> (map)

Finding details that cannot be described. An error code is provided for each failed item.

key -> (string)

value -> (structure)

Includes details about the failed items.

failureCode -> (string)

The status code of a failed item.

retryable -> (boolean)

Indicates whether you can immediately retry a request for this item for a specified resource.