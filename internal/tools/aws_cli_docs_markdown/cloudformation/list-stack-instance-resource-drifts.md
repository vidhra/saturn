# list-stack-instance-resource-driftsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-instance-resource-drifts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-stack-instance-resource-drifts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# list-stack-instance-resource-drifts

## Description

Returns drift information for resources in a stack instance.

### Note

`ListStackInstanceResourceDrifts` returns drift information for the most recent drift detection operation. If an operation is in progress, it may only return partial results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListStackInstanceResourceDrifts)

## Synopsis

```
list-stack-instance-resource-drifts
--stack-set-name <value>
[--next-token <value>]
[--max-results <value>]
[--stack-instance-resource-drift-statuses <value>]
--stack-instance-account <value>
--stack-instance-region <value>
--operation-id <value>
[--call-as <value>]
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

`--stack-set-name` (string)

The name or unique ID of the stack set that you want to list drifted resources for.

`--next-token` (string)

If the previous paginated request didnât return all of the remaining results, the response objectâs `NextToken` parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request objectâs `NextToken` parameter. If there are no remaining results, the previous response objectâs `NextToken` parameter is set to `null` .

`--max-results` (integer)

The maximum number of results to be returned with a single call. If the number of available results exceeds this maximum, the response includes a `NextToken` value that you can assign to the `NextToken` request parameter to get the next set of results.

`--stack-instance-resource-drift-statuses` (list)

The resource drift status of the stack instance.

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

`--stack-instance-account` (string)

The name of the Amazon Web Services account that you want to list resource drifts for.

`--stack-instance-region` (string)

The name of the Region where you want to list resource drifts.

`--operation-id` (string)

The unique ID of the drift operation.

`--call-as` (string)

[Service-managed permissions] Specifies whether you are acting as an account administrator in the organizationâs management account or as a delegated administrator in a member account.

By default, `SELF` is specified. Use `SELF` for stack sets with self-managed permissions.

- If you are signed in to the management account, specify `SELF` .
- If you are signed in to a delegated administrator account, specify `DELEGATED_ADMIN` . Your Amazon Web Services account must be registered as a delegated administrator in the management account. For more information, see [Register a delegated administrator](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacksets-orgs-delegated-admin.html) in the *CloudFormation User Guide* .

Possible values:

- `SELF`
- `DELEGATED_ADMIN`

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

## Output

Summaries -> (list)

A list of `StackInstanceResourceDriftsSummary` structures that contain information about the specified stack instances.

(structure)

The structure containing summary information about resource drifts for a stack instance.

StackId -> (string)

The ID of the stack instance.

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

Type of resource. For more information, see [Amazon Web Services resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the *CloudFormation User Guide* .

PropertyDifferences -> (list)

Status of the actual configuration of the resource compared to its expected configuration. These will be present only for resources whose `StackInstanceResourceDriftStatus` is `MODIFIED` .

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

The drift status of the resource in a stack instance.

- `DELETED` : The resource differs from its expected template configuration in that the resource has been deleted.
- `MODIFIED` : One or more resource properties differ from their expected template values.
- `IN_SYNC` : The resourceâs actual configuration matches its expected template configuration.
- `NOT_CHECKED` : CloudFormation doesnât currently return this value.

Timestamp -> (timestamp)

Time at which the stack instance drift detection operation was initiated.

NextToken -> (string)

If the previous paginated request didnât return all of the remaining results, the response objectâs `NextToken` parameter value is set to a token. To retrieve the next set of results, call this action again and assign that token to the request objectâs `NextToken` parameter. If there are no remaining results, the previous response objectâs `NextToken` parameter is set to `null` .