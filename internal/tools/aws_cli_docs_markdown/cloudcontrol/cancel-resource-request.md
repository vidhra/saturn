# cancel-resource-requestÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/cancel-resource-request.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/cancel-resource-request.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudcontrol](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/index.html#cli-aws-cloudcontrol) ]

# cancel-resource-request

## Description

Cancels the specified resource operation request. For more information, see [Canceling resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-cancel) in the *Amazon Web Services Cloud Control API User Guide* .

Only resource operations requests with a status of `PENDING` or `IN_PROGRESS` can be canceled.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudcontrol-2021-09-30/CancelResourceRequest)

## Synopsis

```
cancel-resource-request
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

The `RequestToken` of the `ProgressEvent` object returned by the resource operation request.

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

ProgressEvent -> (structure)

Represents the current status of a resource operation request. For more information, see [Managing resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html) in the *Amazon Web Services Cloud Control API User Guide* .

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