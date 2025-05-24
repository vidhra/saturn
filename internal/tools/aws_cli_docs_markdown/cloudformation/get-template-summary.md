# get-template-summaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/get-template-summary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/get-template-summary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# get-template-summary

## Description

Returns information about a new or existing template. The `GetTemplateSummary` action is useful for viewing parameter information, such as default parameter values and parameter types, before you create or update a stack or stack set.

You can use the `GetTemplateSummary` action when you submit a template, or you can get template information for a stack set, or a running or deleted stack.

For deleted stacks, `GetTemplateSummary` returns the template information for up to 90 days after the stack has been deleted. If the template doesnât exist, a `ValidationError` is returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/GetTemplateSummary)

## Synopsis

```
get-template-summary
[--template-body <value>]
[--template-url <value>]
[--stack-name <value>]
[--stack-set-name <value>]
[--call-as <value>]
[--template-summary-config <value>]
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

`--template-body` (string)

Structure containing the template body with a minimum length of 1 byte and a maximum length of 51,200 bytes.

Conditional: You must specify only one of the following parameters: `StackName` , `StackSetName` , `TemplateBody` , or `TemplateURL` .

`--template-url` (string)

The URL of a file containing the template body. The URL must point to a template (max size: 1 MB) thatâs located in an Amazon S3 bucket or a Systems Manager document. The location for an Amazon S3 bucket must start with `https://` .

Conditional: You must specify only one of the following parameters: `StackName` , `StackSetName` , `TemplateBody` , or `TemplateURL` .

`--stack-name` (string)

The name or the stack ID thatâs associated with the stack, which arenât always interchangeable. For running stacks, you can specify either the stackâs name or its unique stack ID. For deleted stack, you must specify the unique stack ID.

Conditional: You must specify only one of the following parameters: `StackName` , `StackSetName` , `TemplateBody` , or `TemplateURL` .

`--stack-set-name` (string)

The name or unique ID of the stack set from which the stack was created.

Conditional: You must specify only one of the following parameters: `StackName` , `StackSetName` , `TemplateBody` , or `TemplateURL` .

`--call-as` (string)

[Service-managed permissions] Specifies whether you are acting as an account administrator in the organizationâs management account or as a delegated administrator in a member account.

By default, `SELF` is specified. Use `SELF` for stack sets with self-managed permissions.

- If you are signed in to the management account, specify `SELF` .
- If you are signed in to a delegated administrator account, specify `DELEGATED_ADMIN` . Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the *CloudFormation User Guide* .

Possible values:

- `SELF`
- `DELEGATED_ADMIN`

`--template-summary-config` (structure)

Specifies options for the `GetTemplateSummary` API action.

TreatUnrecognizedResourceTypesAsWarnings -> (boolean)

If set to `True` , any unrecognized resource types generate warnings and not an error. Any unrecognized resource types are returned in the `Warnings` output parameter.

Shorthand Syntax:

```
TreatUnrecognizedResourceTypesAsWarnings=boolean
```

JSON Syntax:

```
{
  "TreatUnrecognizedResourceTypesAsWarnings": true|false
}
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

**To display a template summary**

The following command displays summary information about the resources and metadata for the specified template file.

```
aws cloudformation get-template-summary \
   --template-body file://template.yaml
```

Output:

```
{
    "Parameters": [],
    "Description": "A VPC and subnets.",
    "ResourceTypes": [
        "AWS::EC2::VPC",
        "AWS::EC2::Subnet",
        "AWS::EC2::Subnet",
        "AWS::EC2::RouteTable",
        "AWS::EC2::VPCEndpoint",
        "AWS::EC2::SubnetRouteTableAssociation",
        "AWS::EC2::SubnetRouteTableAssociation",
        "AWS::EC2::VPCEndpoint"
    ],
    "Version": "2010-09-09"
}
```

## Output

Parameters -> (list)

A list of parameter declarations that describe various properties for each parameter.

(structure)

The ParameterDeclaration data type.

ParameterKey -> (string)

The name thatâs associated with the parameter.

DefaultValue -> (string)

The default value of the parameter.

ParameterType -> (string)

The type of parameter.

NoEcho -> (boolean)

Flag that indicates whether the parameter value is shown as plain text in logs and in the Amazon Web Services Management Console.

Description -> (string)

The description thatâs associate with the parameter.

ParameterConstraints -> (structure)

The criteria that CloudFormation uses to validate parameter values.

AllowedValues -> (list)

A list of values that are permitted for a parameter.

(string)

Description -> (string)

The value thatâs defined in the `Description` property of the template.

Capabilities -> (list)

The capabilities found within the template. If your template contains IAM resources, you must specify the `CAPABILITY_IAM` or `CAPABILITY_NAMED_IAM` value for this parameter when you use the  CreateStack or  UpdateStack actions with your template; otherwise, those actions return an `InsufficientCapabilities` error.

For more information, see [Acknowledging IAM resources in CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html#using-iam-capabilities) .

(string)

CapabilitiesReason -> (string)

The list of resources that generated the values in the `Capabilities` response element.

ResourceTypes -> (list)

A list of all the template resource types that are defined in the template, such as `AWS::EC2::Instance` , `AWS::Dynamo::Table` , and `Custom::MyCustomInstance` .

(string)

Version -> (string)

The Amazon Web Services template format version, which identifies the capabilities of the template.

Metadata -> (string)

The value thatâs defined for the `Metadata` property of the template.

DeclaredTransforms -> (list)

A list of the transforms that are declared in the template.

(string)

ResourceIdentifierSummaries -> (list)

A list of resource identifier summaries that describe the target resources of an import operation and the properties you can provide during the import to identify the target resources. For example, `BucketName` is a possible identifier property for an `AWS::S3::Bucket` resource.

(structure)

Describes the target resources of a specific type in your import template (for example, all `AWS::S3::Bucket` resources) and the properties you can provide during the import to identify resources of that type.

ResourceType -> (string)

The template resource type of the target resources, such as `AWS::S3::Bucket` .

LogicalResourceIds -> (list)

The logical IDs of the target resources of the specified `ResourceType` , as defined in the import template.

(string)

ResourceIdentifiers -> (list)

The resource properties you can provide during the import to identify your target resources. For example, `BucketName` is a possible identifier property for `AWS::S3::Bucket` resources.

(string)

Warnings -> (structure)

An object containing any warnings returned.

UnrecognizedResourceTypes -> (list)

A list of all of the unrecognized resource types. This is only returned if the `TemplateSummaryConfig` parameter has the `TreatUnrecognizedResourceTypesAsWarning` configuration set to `True` .

(string)