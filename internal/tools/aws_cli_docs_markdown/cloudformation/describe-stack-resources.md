# describe-stack-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# describe-stack-resources

## Description

Returns Amazon Web Services resource descriptions for running and deleted stacks. If `StackName` is specified, all the associated resources that are part of the stack are returned. If `PhysicalResourceId` is specified, the associated resources of the stack that the resource belongs to are returned.

### Note

Only the first 100 resources will be returned. If your stack has more resources than this, you should use `ListStackResources` instead.

For deleted stacks, `DescribeStackResources` returns resource information for up to 90 days after the stack has been deleted.

You must specify either `StackName` or `PhysicalResourceId` , but not both. In addition, you can specify `LogicalResourceId` to filter the returned result. For more information about resources, the `LogicalResourceId` and `PhysicalResourceId` , see the [CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/) .

### Note

A `ValidationError` is returned if you specify both `StackName` and `PhysicalResourceId` in the same request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackResources)

## Synopsis

```
describe-stack-resources
[--stack-name <value>]
[--logical-resource-id <value>]
[--physical-resource-id <value>]
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

`--stack-name` (string)

The name or the unique stack ID that is associated with the stack, which arenât always interchangeable:

- Running stacks: You can specify either the stackâs name or its unique stack ID.
- Deleted stacks: You must specify the unique stack ID.

Required: Conditional. If you donât specify `StackName` , you must specify `PhysicalResourceId` .

`--logical-resource-id` (string)

The logical name of the resource as specified in the template.

`--physical-resource-id` (string)

The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.

For example, for an Amazon Elastic Compute Cloud (EC2) instance, `PhysicalResourceId` corresponds to the `InstanceId` . You can pass the EC2 `InstanceId` to `DescribeStackResources` to find which stack the instance belongs to and what other resources are part of the stack.

Required: Conditional. If you donât specify `PhysicalResourceId` , you must specify `StackName` .

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

**To get information about a stack resource**

The following `describe-stack-resources` example displays details for the resources in the specified stack.

```
aws cloudformation describe-stack-resources \
    --stack-name my-stack
```

Output:

```
{
    "StackResources": [
        {
            "StackName": "my-stack",
            "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204",
            "LogicalResourceId": "bucket",
            "PhysicalResourceId": "my-stack-bucket-1vc62xmplgguf",
            "ResourceType": "AWS::S3::Bucket",
            "Timestamp": "2019-10-02T04:34:11.345Z",
            "ResourceStatus": "CREATE_COMPLETE",
            "DriftInformation": {
                "StackResourceDriftStatus": "IN_SYNC"
            }
        },
        {
            "StackName": "my-stack",
            "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204",
            "LogicalResourceId": "function",
            "PhysicalResourceId": "my-function-SEZV4XMPL4S5",
            "ResourceType": "AWS::Lambda::Function",
            "Timestamp": "2019-10-02T05:34:27.989Z",
            "ResourceStatus": "UPDATE_COMPLETE",
            "DriftInformation": {
                "StackResourceDriftStatus": "IN_SYNC"
            }
        },
        {
            "StackName": "my-stack",
            "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204",
            "LogicalResourceId": "functionRole",
            "PhysicalResourceId": "my-functionRole-HIZXMPLEOM9E",
            "ResourceType": "AWS::IAM::Role",
            "Timestamp": "2019-10-02T04:34:06.350Z",
            "ResourceStatus": "CREATE_COMPLETE",
            "DriftInformation": {
                "StackResourceDriftStatus": "IN_SYNC"
            }
        }
    ]
}
```

## Output

StackResources -> (list)

A list of `StackResource` structures.

(structure)

The StackResource data type.

StackName -> (string)

The name associated with the stack.

StackId -> (string)

Unique identifier of the stack.

LogicalResourceId -> (string)

The logical name of the resource specified in the template.

PhysicalResourceId -> (string)

The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.

ResourceType -> (string)

Type of resource. For more information, see [Amazon Web Services resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the *CloudFormation User Guide* .

Timestamp -> (timestamp)

Time the status was updated.

ResourceStatus -> (string)

Current status of the resource.

ResourceStatusReason -> (string)

Success/failure message associated with the resource.

Description -> (string)

User defined description associated with the resource.

DriftInformation -> (structure)

Information about whether the resourceâs actual configuration differs, or has *drifted* , from its expected configuration, as defined in the stack template and any values specified as template parameters. For more information, see [Detect unmanaged configuration changes to stacks and resources with drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) .

StackResourceDriftStatus -> (string)

Status of the resourceâs actual configuration compared to its expected configuration

- `DELETED` : The resource differs from its expected configuration in that it has been deleted.
- `MODIFIED` : The resource differs from its expected configuration.
- `NOT_CHECKED` : CloudFormation has not checked if the resource differs from its expected configuration. Any resources that do not currently support drift detection have a status of `NOT_CHECKED` . For more information, see [Resource type support for imports and drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) .
- `IN_SYNC` : The resourceâs actual configuration matches its expected configuration.

LastCheckTimestamp -> (timestamp)

When CloudFormation last checked if the resource had drifted from its expected configuration.

ModuleInfo -> (structure)

Contains information about the module from which the resource was created, if the resource was created from a module included in the stack template.

TypeHierarchy -> (string)

A concatenated list of the module type or types containing the resource. Module types are listed starting with the inner-most nested module, and separated by `/` .

In the following example, the resource was created from a module of type `AWS::First::Example::MODULE` , thatâs nested inside a parent module of type `AWS::Second::Example::MODULE` .

`AWS::First::Example::MODULE/AWS::Second::Example::MODULE`

LogicalIdHierarchy -> (string)

A concatenated list of the logical IDs of the module or modules containing the resource. Modules are listed starting with the inner-most nested module, and separated by `/` .

In the following example, the resource was created from a module, `moduleA` , thatâs nested inside a parent module, `moduleB` .

`moduleA/moduleB`

For more information, see [Reference module resources in CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/module-ref-resources.html) in the *CloudFormation User Guide* .