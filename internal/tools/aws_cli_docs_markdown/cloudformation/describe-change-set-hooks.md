# describe-change-set-hooksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-change-set-hooks.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-change-set-hooks.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# describe-change-set-hooks

## Description

Returns hook-related information for the change set and a list of changes that CloudFormation makes when you run the change set.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/DescribeChangeSetHooks)

## Synopsis

```
describe-change-set-hooks
--change-set-name <value>
[--stack-name <value>]
[--next-token <value>]
[--logical-resource-id <value>]
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

`--change-set-name` (string)

The name or Amazon Resource Name (ARN) of the change set that you want to describe.

`--stack-name` (string)

If you specified the name of a change set, specify the stack name or stack ID (ARN) of the change set you want to describe.

`--next-token` (string)

A string, provided by the `DescribeChangeSetHooks` response output, that identifies the next page of information that you want to retrieve.

`--logical-resource-id` (string)

If specified, lists only the Hooks related to the specified `LogicalResourceId` .

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

ChangeSetId -> (string)

The change set identifier (stack ID).

ChangeSetName -> (string)

The change set name.

Hooks -> (list)

List of hook objects.

(structure)

Specifies the resource, the hook, and the hook version to be invoked.

InvocationPoint -> (string)

Specifies the points in provisioning logic where a hook is invoked.

FailureMode -> (string)

Specify the hook failure mode for non-compliant resources in the followings ways.

- `FAIL` Stops provisioning resources.
- `WARN` Allows provisioning to continue with a warning message.

TypeName -> (string)

The unique name for your hook. Specifies a three-part namespace for your hook, with a recommended pattern of `Organization::Service::Hook` .

### Note

The following organization namespaces are reserved and canât be used in your hook type names:

- `Alexa`
- `AMZN`
- `Amazon`
- `ASK`
- `AWS`
- `Custom`
- `Dev`

TypeVersionId -> (string)

The version ID of the type specified.

TypeConfigurationVersionId -> (string)

The version ID of the type configuration.

TargetDetails -> (structure)

Specifies details about the target that the hook will run against.

TargetType -> (string)

The name of the type.

ResourceTargetDetails -> (structure)

Required if `TargetType` is `RESOURCE` .

LogicalResourceId -> (string)

The resourceâs logical ID, which is defined in the stackâs template.

ResourceType -> (string)

The type of CloudFormation resource, such as `AWS::S3::Bucket` .

ResourceAction -> (string)

Specifies the action of the resource.

Status -> (string)

Provides the status of the change set hook.

NextToken -> (string)

Pagination token, `null` or empty if no more results.

StackId -> (string)

The stack identifier (stack ID).

StackName -> (string)

The stack name.