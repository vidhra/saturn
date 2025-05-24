# describe-instance-propertiesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-properties.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-properties.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# describe-instance-properties

## Description

An API operation used by the Systems Manager console to display information about Systems Manager managed nodes.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/DescribeInstanceProperties)

`describe-instance-properties` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `InstanceProperties`

## Synopsis

```
describe-instance-properties
[--instance-property-filter-list <value>]
[--filters-with-operator <value>]
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

`--instance-property-filter-list` (list)

An array of instance property filters.

(structure)

Describes a filter for a specific list of managed nodes. You can filter node information by using tags. You specify tags by using a key-value mapping.

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
    "key": "InstanceIds"|"AgentVersion"|"PingStatus"|"PlatformTypes"|"DocumentName"|"ActivationIds"|"IamRole"|"ResourceType"|"AssociationStatus",
    "valueSet": ["string", ...]
  }
  ...
]
```

`--filters-with-operator` (list)

The request filters to use with the operator.

(structure)

The filters to describe or get information about your managed nodes.

Key -> (string)

The filter key name to describe your managed nodes.

Values -> (list)

The filter key name to describe your managed nodes.

(string)

Operator -> (string)

The operator used by the filter call.

Shorthand Syntax:

```
Key=string,Values=string,string,Operator=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Values": ["string", ...],
    "Operator": "Equal"|"NotEqual"|"BeginWith"|"LessThan"|"GreaterThan"
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

## Output

InstanceProperties -> (list)

Properties for the managed instances.

(structure)

An object containing various properties of a managed node.

Name -> (string)

The value of the EC2 `Name` tag associated with the node. If a `Name` tag hasnât been applied to the node, this value is blank.

InstanceId -> (string)

The ID of the managed node.

InstanceType -> (string)

The instance type of the managed node. For example, t3.large.

InstanceRole -> (string)

The instance profile attached to the node. If an instance profile isnât attached to the node, this value is blank.

KeyName -> (string)

The name of the key pair associated with the node. If a key pair isntât associated with the node, this value is blank.

InstanceState -> (string)

The current state of the node.

Architecture -> (string)

The CPU architecture of the node. For example, `x86_64` .

IPAddress -> (string)

The public IPv4 address assigned to the node. If a public IPv4 address isnât assigned to the node, this value is blank.

LaunchTime -> (timestamp)

The timestamp for when the node was launched.

PingStatus -> (string)

Connection status of the SSM Agent on the managed node.

LastPingDateTime -> (timestamp)

The date and time when the SSM Agent last pinged the Systems Manager service.

AgentVersion -> (string)

The version of SSM Agent running on your managed node.

PlatformType -> (string)

The operating system platform type of the managed node. For example, Windows Server or Amazon Linux 2.

PlatformName -> (string)

The name of the operating system platform running on your managed node.

PlatformVersion -> (string)

The version of the OS platform running on your managed node.

ActivationId -> (string)

The activation ID created by Systems Manager when the server or virtual machine (VM) was registered

IamRole -> (string)

The IAM role used in the hybrid activation to register the node with Systems Manager.

RegistrationDate -> (timestamp)

The date the node was registered with Systems Manager.

ResourceType -> (string)

The type of managed node.

ComputerName -> (string)

The fully qualified host name of the managed node.

AssociationStatus -> (string)

The status of the State Manager association applied to the managed node.

LastAssociationExecutionDate -> (timestamp)

The date the association was last run.

LastSuccessfulAssociationExecutionDate -> (timestamp)

The last date the association was successfully run.

AssociationOverview -> (structure)

Status information about the aggregated associations.

DetailedStatus -> (string)

Detailed status information about the aggregated associations.

InstanceAssociationStatusAggregatedCount -> (map)

The number of associations for the managed nodes.

key -> (string)

value -> (integer)

SourceId -> (string)

The ID of the source resource.

SourceType -> (string)

The type of the source resource.

NextToken -> (string)

The token for the next set of properties to return. Use this token to get the next set of results.