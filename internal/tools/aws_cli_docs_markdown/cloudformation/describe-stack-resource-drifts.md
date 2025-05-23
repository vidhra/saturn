# describe-stack-resource-driftsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resource-drifts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stack-resource-drifts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# describe-stack-resource-drifts

## Description

Returns drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects configuration drift.

For a given stack, there will be one `StackResourceDrift` for each stack resource that has been checked for drift. Resources that havenât yet been checked for drift arenât included. Resources that donât currently support drift detection arenât checked, and so not included. For a list of resources that support drift detection, see [Resource type support for imports and drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) .

Use  DetectStackResourceDrift to detect drift on individual resources, or  DetectStackDrift to detect drift on all supported resources for a given stack.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeStackResourceDrifts)

## Synopsis

```
describe-stack-resource-drifts
--stack-name <value>
[--stack-resource-drift-status-filters <value>]
[--next-token <value>]
[--max-results <value>]
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

The name of the stack for which you want drift information.

`--stack-resource-drift-status-filters` (list)

The resource drift status values to use as filters for the resource drift results returned.

- `DELETED` : The resource differs from its expected template configuration in that the resource has been deleted.
- `MODIFIED` : One or more resource properties differ from their expected template values.
- `IN_SYNC` : The resourceâs actual configuration matches its expected template configuration.
- `NOT_CHECKED` : CloudFormation doesnât currently return this value.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  IN_SYNC
  MODIFIED
  DELETED
  NOT_CHECKED
```

`--next-token` (string)

A string that identifies the next page of stack resource drift results.

`--max-results` (integer)

The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a `NextToken` value that you can assign to the `NextToken` request parameter to get the next set of results.

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

**To get information about resources that drifted from the stack definition**

The following command displays information about drifted resources for the specified stack. To initiate drift detection, use the `detect-stack-drift` command.:

```
aws cloudformation describe-stack-resource-drifts \
    --stack-name my-stack
```

The output shows an AWS Lambda function that was modified out-of-band:

```
{
    "StackResourceDrifts": [
        {
            "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/my-stack/d0a825a0-e4cd-xmpl-b9fb-061c69e99204",
            "LogicalResourceId": "function",
            "PhysicalResourceId": "my-function-SEZV4XMPL4S5",
            "ResourceType": "AWS::Lambda::Function",
            "ExpectedProperties": "{\"Description\":\"Write a file to S3.\",\"Environment\":{\"Variables\":{\"bucket\":\"my-stack-bucket-1vc62xmplgguf\"}},\"Handler\":\"index.handler\",\"MemorySize\":128,\"Role\":\"arn:aws:iam::123456789012:role/my-functionRole-HIZXMPLEOM9E\",\"Runtime\":\"nodejs10.x\",\"Tags\":[{\"Key\":\"lambda:createdBy\",\"Value\":\"SAM\"}],\"Timeout\":900,\"TracingConfig\":{\"Mode\":\"Active\"}}",
            "ActualProperties": "{\"Description\":\"Write a file to S3.\",\"Environment\":{\"Variables\":{\"bucket\":\"my-stack-bucket-1vc62xmplgguf\"}},\"Handler\":\"index.handler\",\"MemorySize\":256,\"Role\":\"arn:aws:iam::123456789012:role/my-functionRole-HIZXMPLEOM9E\",\"Runtime\":\"nodejs10.x\",\"Tags\":[{\"Key\":\"lambda:createdBy\",\"Value\":\"SAM\"}],\"Timeout\":22,\"TracingConfig\":{\"Mode\":\"Active\"}}",
            "PropertyDifferences": [
                {
                    "PropertyPath": "/MemorySize",
                    "ExpectedValue": "128",
                    "ActualValue": "256",
                    "DifferenceType": "NOT_EQUAL"
                },
                {
                    "PropertyPath": "/Timeout",
                    "ExpectedValue": "900",
                    "ActualValue": "22",
                    "DifferenceType": "NOT_EQUAL"
                }
            ],
            "StackResourceDriftStatus": "MODIFIED",
            "Timestamp": "2019-10-02T05:54:44.064Z"
        }
    ]
}
```

## Output

StackResourceDrifts -> (list)

Drift information for the resources that have been checked for drift in the specified stack. This includes actual and expected configuration values for resources where CloudFormation detects drift.

For a given stack, there will be one `StackResourceDrift` for each stack resource that has been checked for drift. Resources that havenât yet been checked for drift arenât included. Resources that do not currently support drift detection arenât checked, and so not included. For a list of resources that support drift detection, see [Resource type support for imports and drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) .

(structure)

Contains the drift information for a resource that has been checked for drift. This includes actual and expected property values for resources in which CloudFormation has detected drift. Only resource properties explicitly defined in the stack template are checked for drift. For more information, see [Detect unmanaged configuration changes to stacks and resources with drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) .

Resources that donât currently support drift detection canât be checked. For a list of resources that support drift detection, see [Resource type support for imports and drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/resource-import-supported-resources.html) .

Use  DetectStackResourceDrift to detect drift on individual resources, or  DetectStackDrift to detect drift on all resources in a given stack that support drift detection.

StackId -> (string)

The ID of the stack.

LogicalResourceId -> (string)

The logical name of the resource specified in the template.

PhysicalResourceId -> (string)

The name or unique identifier that corresponds to a physical instance ID of a resource supported by CloudFormation.

PhysicalResourceIdContext -> (list)

Context information that enables CloudFormation to uniquely identify a resource. CloudFormation uses context key-value pairs in cases where a resourceâs logical and physical IDs arenât enough to uniquely identify that resource. Each context key-value pair specifies a unique resource that contains the targeted resource.

(structure)

Context information that enables CloudFormation to uniquely identify a resource. CloudFormation uses context key-value pairs in cases where a resourceâs logical and physical IDs arenât enough to uniquely identify that resource. Each context key-value pair specifies a resource that contains the targeted resource.

Key -> (string)

The resource context key.

Value -> (string)

The resource context value.

ResourceType -> (string)

The type of the resource.

ExpectedProperties -> (string)

A JSON structure containing the expected property values of the stack resource, as defined in the stack template and any values specified as template parameters.

For resources whose `StackResourceDriftStatus` is `DELETED` , this structure will not be present.

ActualProperties -> (string)

A JSON structure containing the actual property values of the stack resource.

For resources whose `StackResourceDriftStatus` is `DELETED` , this structure will not be present.

PropertyDifferences -> (list)

A collection of the resource properties whose actual values differ from their expected values. These will be present only for resources whose `StackResourceDriftStatus` is `MODIFIED` .

(structure)

Information about a resource property whose actual value differs from its expected value, as defined in the stack template and any values specified as template parameters. These will be present only for resources whose `StackResourceDriftStatus` is `MODIFIED` . For more information, see [Detect unmanaged configuration changes to stacks and resources with drift detection](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html) .

PropertyPath -> (string)

The fully-qualified path to the resource property.

ExpectedValue -> (string)

The expected property value of the resource property, as defined in the stack template and any values specified as template parameters.

ActualValue -> (string)

The actual property value of the resource property.

DifferenceType -> (string)

The type of property difference.

- `ADD` : A value has been added to a resource property thatâs an array or list data type.
- `REMOVE` : The property has been removed from the current resource configuration.
- `NOT_EQUAL` : The current property value differs from its expected value (as defined in the stack template and any values specified as template parameters).

StackResourceDriftStatus -> (string)

Status of the resourceâs actual configuration compared to its expected configuration.

- `DELETED` : The resource differs from its expected template configuration because the resource has been deleted.
- `MODIFIED` : One or more resource properties differ from their expected values (as defined in the stack template and any values specified as template parameters).
- `IN_SYNC` : The resourceâs actual configuration matches its expected template configuration.
- `NOT_CHECKED` : CloudFormation does not currently return this value.

Timestamp -> (timestamp)

Time at which CloudFormation performed drift detection on the stack resource.

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

NextToken -> (string)

If the request doesnât return all the remaining results, `NextToken` is set to a token. To retrieve the next set of results, call `DescribeStackResourceDrifts` again and assign that token to the request objectâs `NextToken` parameter. If the request returns all results, `NextToken` is set to `null` .