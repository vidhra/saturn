# get-resource-request-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/get-resource-request-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/get-resource-request-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudcontrol](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/index.html#cli-aws-cloudcontrol) ]

# get-resource-request-status

## Description

Returns the current status of a resource operation request. For more information, see [Tracking the progress of resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-track) in the *Amazon Web Services Cloud Control API User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudcontrol-2021-09-30/GetResourceRequestStatus)

## Synopsis

```
get-resource-request-status
--request-token <value>
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

`--request-token` (string)

A unique token used to track the progress of the resource operation request.

Request tokens are included in the `ProgressEvent` type returned by a resource operation request.

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

**To get the status information of a resource request**

The following `get-resource-request-status` example returns status information about the specified resource request.

```
aws cloudcontrol get-resource-request-status \
    --request-token "e1a6b86e-46bd-41ac-bfba-001234567890"
```

Output:

```
{
    "ProgressEvent": {
        "TypeName": "AWS::Kinesis::Stream",
        "Identifier": "Demo",
        "RequestToken": "e1a6b86e-46bd-41ac-bfba-001234567890",
        "Operation": "CREATE",
        "OperationStatus": "FAILED",
        "EventTime": 1632950268.481,
        "StatusMessage": "Resource of type 'AWS::Kinesis::Stream' with identifier 'Demo' already exists.",
        "ErrorCode": "AlreadyExists"
    }
}
```

For more information, see [Managing resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html) in the *Cloud Control API User Guide*.

## Output

ProgressEvent -> (structure)

Represents the current status of the resource operation request.

TypeName -> (string)

The name of the resource type used in the operation.

Identifier -> (string)

The primary identifier for the resource.

### Note

In some cases, the resource identifier may be available before the resource operation has reached a status of `SUCCESS` .

RequestToken -> (string)

The unique token representing this resource operation request.

Use the `RequestToken` with [GetResourceRequestStatus](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html) to return the current status of a resource operation request.

HooksRequestToken -> (string)

The unique token representing the Hooks operation for the request.

Operation -> (string)

The resource operation type.

OperationStatus -> (string)

The current status of the resource operation request.

- `PENDING` : The resource operation hasnât yet started.
- `IN_PROGRESS` : The resource operation is currently in progress.
- `SUCCESS` : The resource operation has successfully completed.
- `FAILED` : The resource operation has failed. Refer to the error code and status message for more information.
- `CANCEL_IN_PROGRESS` : The resource operation is in the process of being canceled.
- `CANCEL_COMPLETE` : The resource operation has been canceled.

EventTime -> (timestamp)

When the resource operation request was initiated.

ResourceModel -> (string)

A JSON string containing the resource model, consisting of each resource property and its current value.

StatusMessage -> (string)

Any message explaining the current status.

ErrorCode -> (string)

For requests with a status of `FAILED` , the associated error code.

For error code definitions, see [Handler error codes](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-test-contract-errors.html) in the *CloudFormation Command Line Interface User Guide for Extension Development* .

RetryAfter -> (timestamp)

When to next request the status of this resource operation request.

HooksProgressEvent -> (list)

Lists Hook invocations for the specified target in the request. This is a list since the same target can invoke multiple Hooks.

(structure)

Represents the current status of applicable Hooks for a resource operation request. It contains list of Hook invocation information for the resource specified in the request since the same target can invoke multiple Hooks. For more information, see [Managing resource operation requests with Amazon Web Services Cloud Control API](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html) .

HookTypeName -> (string)

The type name of the Hook being invoked.

HookTypeVersionId -> (string)

The type version of the Hook being invoked.

HookTypeArn -> (string)

The ARN of the Hook being invoked.

InvocationPoint -> (string)

States whether the Hook is invoked before or after resource provisioning.

HookStatus -> (string)

The status of the Hook invocation. The following are potential statuses:

- `HOOK_PENDING` : The Hook was added to the invocation plan, but not yet invoked.
- `HOOK_IN_PROGRESS` : The Hook was invoked, but hasnât completed.
- `HOOK_COMPLETE_SUCCEEDED` : The Hook invocation is complete with a successful result.
- `HOOK_COMPLETE_FAILED` : The Hook invocation is complete with a failed result.
- `HOOK_FAILED` : The Hook invocation didnât complete successfully.

HookEventTime -> (timestamp)

The time that the Hook invocation request initiated.

HookStatusMessage -> (string)

The message explaining the current Hook status.

FailureMode -> (string)

The failure mode of the invocation. The following are the potential statuses:

- `FAIL` : This will fail the Hook invocation and the request associated with it.
- `WARN` : This will fail the Hook invocation, but not the request associated with it.