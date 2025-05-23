# list-hook-resultsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-hook-results.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/list-hook-results.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# list-hook-results

## Description

Returns summaries of invoked Hooks when a change set or Cloud Control API operation target is provided.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/ListHookResults)

## Synopsis

```
list-hook-results
--target-type <value>
--target-id <value>
[--next-token <value>]
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

`--target-type` (string)

The type of operation being targeted by the Hook.

Possible values:

- `CHANGE_SET`
- `STACK`
- `RESOURCE`
- `CLOUD_CONTROL`

`--target-id` (string)

The logical ID of the target the operation is acting on by the Hook. If the target is a change set, itâs the ARN of the change set.

If the target is a Cloud Control API operation, this will be the `HookRequestToken` returned by the Cloud Control API operation request. For more information on the `HookRequestToken` , see [ProgressEvent](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ProgressEvent.html) .

`--next-token` (string)

A string that identifies the next page of events that you want to retrieve.

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

TargetType -> (string)

The type of operation being targeted by the Hook.

TargetId -> (string)

The logical ID of the target the operation is acting on by the Hook. If the target is a change set, itâs the ARN of the change set.

If the target is a Cloud Control API operation, this will be the `HooksRequestToken` returned by the Cloud Control API operation request. For more information on the `HooksRequestToken` , see [ProgressEvent](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_ProgressEvent.html) .

HookResults -> (list)

A list of `HookResultSummary` structures that provides the status and Hook status reason for each Hook invocation for the specified target.

(structure)

Describes a Hook invocation, its status, and the reason for its status.

InvocationPoint -> (string)

The exact point in the provisioning logic where the Hook runs.

FailureMode -> (string)

The failure mode of the invocation. The following are potential modes:

- `FAIL` : If the hook invocation returns a failure, then the requested target operation should fail.
- `WARN` : If the hook invocation returns a failure, then the requested target operation should warn.

TypeName -> (string)

The type name of the Hook being invoked.

TypeVersionId -> (string)

The version of the Hook being invoked.

TypeConfigurationVersionId -> (string)

The version of the Hook type configuration.

Status -> (string)

The state of the Hook invocation.

HookStatusReason -> (string)

A description of the Hook results status. For example, if the Hook result is in a `FAILED` state, this may contain additional information for the `FAILED` state.

NextToken -> (string)

Pagination token, `null` or empty if no more results.