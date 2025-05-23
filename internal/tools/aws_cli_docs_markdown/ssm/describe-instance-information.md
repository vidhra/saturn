# describe-instance-informationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-information.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-information.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# describe-instance-information

## Description

Provides information about one or more of your managed nodes, including the operating system platform, SSM Agent version, association status, and IP address. This operation does not return information for nodes that are either Stopped or Terminated.

If you specify one or more node IDs, the operation returns information for those managed nodes. If you donât specify node IDs, it returns information for all your managed nodes. If you specify a node ID that isnât valid or a node that you donât own, you receive an error.

### Note

The `IamRole` field returned for this API operation is the role assigned to an Amazon EC2 instance configured with a Systems Manager Quick Setup host management configuration or the role assigned to an on-premises managed node.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstanceInformation)

`describe-instance-information` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `InstanceInformationList`

## Synopsis

```
describe-instance-information
[--instance-information-filter-list <value>]
[--filters <value>]
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

`--instance-information-filter-list` (list)

This is a legacy method. We recommend that you donât use this method. Instead, use the `Filters` data type. `Filters` enables you to return node information by filtering based on tags applied to managed nodes.

### Note

Attempting to use `InstanceInformationFilterList` and `Filters` leads to an exception error.

(structure)

Describes a filter for a specific list of managed nodes. You can filter node information by using tags. You specify tags by using a key-value mapping.

Use this operation instead of the  DescribeInstanceInformationRequest$InstanceInformationFilterList method. The `InstanceInformationFilterList` method is a legacy method and doesnât support tags.

key -> (string)

The name of the filter.

valueSet -> (list)

The filter values.

(string)

Shorthand Syntax:

```
key=string,valueSet=string,string ...
```

JSON Syntax:

```
[
  {
    "key": "InstanceIds"|"AgentVersion"|"PingStatus"|"PlatformTypes"|"ActivationIds"|"IamRole"|"ResourceType"|"AssociationStatus",
    "valueSet": ["string", ...]
  }
  ...
]
```

`--filters` (list)

One or more filters. Use a filter to return a more specific list of managed nodes. You can filter based on tags applied to your managed nodes. Tag filters canât be combined with other filter types. Use this `Filters` data type instead of `InstanceInformationFilterList` , which is deprecated.

(structure)

The filters to describe or get information about your managed nodes.

Key -> (string)

The filter key name to describe your managed nodes.

Valid filter key values: ActivationIds | AgentVersion | AssociationStatus | IamRole | InstanceIds | PingStatus | PlatformTypes | ResourceType | SourceIds | SourceTypes | âtag-keyâ | âtag:`{keyname}`

- Valid values for the `AssociationStatus` filter key: Success | Pending | Failed
- Valid values for the `PingStatus` filter key: Online | ConnectionLost | Inactive (deprecated)
- Valid values for the `PlatformType` filter key: Windows | Linux | MacOS
- Valid values for the `ResourceType` filter key: EC2Instance | ManagedInstance
- Valid values for the `SourceType` filter key: AWS::EC2::Instance | AWS::SSM::ManagedInstance | AWS::IoT::Thing
- Valid tag examples: `Key=tag-key,Values=Purpose` | `Key=tag:Purpose,Values=Test` .

Values -> (list)

The filter values.

(string)

Shorthand Syntax:

```
Key=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Values": ["string", ...]
  }
  ...
]
```

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

**Example 1: To describe managed instance information**

The following `describe-instance-information` example retrieves details of each of your managed instances.

```
aws ssm describe-instance-information
```

**Example 2: To describe information about a specific managed instance**

The following `describe-instance-information` example shows details of the managed instance `i-028ea792daEXAMPLE`.

```
aws ssm describe-instance-information \
    --filters "Key=InstanceIds,Values=i-028ea792daEXAMPLE"
```

**Example 3: To describe information about managed instances with a specific tag key**

The following `describe-instance-information` example shows details for managed instances that have the tag key `DEV`.

```
aws ssm describe-instance-information \
    --filters "Key=tag-key,Values=DEV"
```

Output:

```
{
    "InstanceInformationList": [
        {
            "InstanceId": "i-028ea792daEXAMPLE",
            "PingStatus": "Online",
            "LastPingDateTime": 1582221233.421,
            "AgentVersion": "2.3.842.0",
            "IsLatestVersion": true,
            "PlatformType": "Linux",
            "PlatformName": "SLES",
            "PlatformVersion": "15.1",
            "ResourceType": "EC2Instance",
            "IPAddress": "192.0.2.0",
            "ComputerName": "ip-198.51.100.0.us-east-2.compute.internal",
            "AssociationStatus": "Success",
            "LastAssociationExecutionDate": 1582220806.0,
            "LastSuccessfulAssociationExecutionDate": 1582220806.0,
            "AssociationOverview": {
                "DetailedStatus": "Success",
                "InstanceAssociationStatusAggregatedCount": {
                    "Success": 2
                }
            }
        }
    ]
}
```

For more information, see [Managed Instances](https://docs.aws.amazon.com/systems-manager/latest/userguide/managed_instances.html) in the *AWS Systems Manager User Guide*.

## Output

InstanceInformationList -> (list)

The managed node information list.

(structure)

Describes a filter for a specific list of managed nodes.

InstanceId -> (string)

The managed node ID.

PingStatus -> (string)

Connection status of SSM Agent.

### Note

The status `Inactive` has been deprecated and is no longer in use.

LastPingDateTime -> (timestamp)

The date and time when the agent last pinged the Systems Manager service.

AgentVersion -> (string)

The version of SSM Agent running on your Linux managed node.

IsLatestVersion -> (boolean)

Indicates whether the latest version of SSM Agent is running on your Linux managed node. This field doesnât indicate whether or not the latest version is installed on Windows managed nodes, because some older versions of Windows Server use the EC2Config service to process Systems Manager requests.

PlatformType -> (string)

The operating system platform type.

PlatformName -> (string)

The name of the operating system platform running on your managed node.

PlatformVersion -> (string)

The version of the OS platform running on your managed node.

ActivationId -> (string)

The activation ID created by Amazon Web Services Systems Manager when the server or virtual machine (VM) was registered.

IamRole -> (string)

The role assigned to an Amazon EC2 instance configured with a Systems Manager Quick Setup host management configuration or the role assigned to an on-premises managed node.

This call doesnât return the IAM role for *unmanaged* Amazon EC2 instances (instances not configured for Systems Manager). To retrieve the role for an unmanaged instance, use the Amazon EC2 `DescribeInstances` operation. For information, see [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) in the *Amazon EC2 API Reference* or [describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html) in the *Amazon Web Services CLI Command Reference* .

RegistrationDate -> (timestamp)

The date the server or VM was registered with Amazon Web Services as a managed node.

ResourceType -> (string)

The type of instance. Instances are either EC2 instances or managed instances.

Name -> (string)

The name assigned to an on-premises server, edge device, or virtual machine (VM) when it is activated as a Systems Manager managed node. The name is specified as the `DefaultInstanceName` property using the  CreateActivation command. It is applied to the managed node by specifying the Activation Code and Activation ID when you install SSM Agent on the node, as explained in [How to install SSM Agent on hybrid Linux nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-ssm-agent-install-linux.html) and [How to install SSM Agent on hybrid Windows Server nodes](https://docs.aws.amazon.com/systems-manager/latest/userguide/hybrid-multicloud-ssm-agent-install-windows.html) . To retrieve the `Name` tag of an EC2 instance, use the Amazon EC2 `DescribeInstances` operation. For information, see [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) in the *Amazon EC2 API Reference* or [describe-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-instances.html) in the *Amazon Web Services CLI Command Reference* .

IPAddress -> (string)

The IP address of the managed node.

ComputerName -> (string)

The fully qualified host name of the managed node.

AssociationStatus -> (string)

The status of the association.

LastAssociationExecutionDate -> (timestamp)

The date the association was last run.

LastSuccessfulAssociationExecutionDate -> (timestamp)

The last date the association was successfully run.

AssociationOverview -> (structure)

Information about the association.

DetailedStatus -> (string)

Detailed status information about the aggregated associations.

InstanceAssociationStatusAggregatedCount -> (map)

The number of associations for the managed nodes.

key -> (string)

value -> (integer)

SourceId -> (string)

The ID of the source resource. For IoT Greengrass devices, `SourceId` is the Thing name.

SourceType -> (string)

The type of the source resource. For IoT Greengrass devices, `SourceType` is `AWS::IoT::Thing` .

NextToken -> (string)

The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.