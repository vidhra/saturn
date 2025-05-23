# create-resourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/create-resource.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/create-resource.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudcontrol](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/index.html#cli-aws-cloudcontrol) ]

# create-resource

## Description

Creates the specified resource. For more information, see [Creating a resource](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-create.html) in the *Amazon Web Services Cloud Control API User Guide* .

After you have initiated a resource creation request, you can monitor the progress of your request by calling [GetResourceRequestStatus](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html) using the `RequestToken` of the `ProgressEvent` type returned by `CreateResource` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudcontrol-2021-09-30/CreateResource)

## Synopsis

```
create-resource
--type-name <value>
[--type-version-id <value>]
[--role-arn <value>]
[--client-token <value>]
--desired-state <value>
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

`--type-name` (string)

The name of the resource type.

`--type-version-id` (string)

For private resource types, the type version to use in this resource operation. If you do not specify a resource version, CloudFormation uses the default version.

`--role-arn` (string)

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role for Cloud Control API to use when performing this resource operation. The role specified must have the permissions required for this operation. The necessary permissions for each event handler are defined in the `` [handlers](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html#schema-properties-handlers) `` section of the [resource type definition schema](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-schema.html) .

If you do not specify a role, Cloud Control API uses a temporary session created using your Amazon Web Services user credentials.

For more information, see [Specifying credentials](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-permissions) in the *Amazon Web Services Cloud Control API User Guide* .

`--client-token` (string)

A unique identifier to ensure the idempotency of the resource request. As a best practice, specify this token to ensure idempotency, so that Amazon Web Services Cloud Control API can accurately distinguish between request retries and new resource requests. You might retry a resource request to ensure that it was successfully received.

A client token is valid for 36 hours once used. After that, a resource request with the same client token is treated as a new request.

If you do not specify a client token, one is generated for inclusion in the request.

For more information, see [Ensuring resource operation requests are unique](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations.html#resource-operations-idempotency) in the *Amazon Web Services Cloud Control API User Guide* .

`--desired-state` (string)

Structured data format representing the desired state of the resource, consisting of that resourceâs properties and their desired values.

### Note

Cloud Control API currently supports JSON as a structured data format.

Specify the desired state as one of the following:

- A JSON blob
- A local path containing the desired state in JSON data format

For more information, see [Composing the desired state of the resource](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-create.html#resource-operations-create-desiredstate) in the *Amazon Web Services Cloud Control API User Guide* .

For more information about the properties of a specific resource, refer to the related topic for the resource in the [Resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the *CloudFormation Users Guide* .

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

**To create a resource**

The following `create-resource` example creates an AWS::Kinesis::Stream resource, named ResourceExample, with a retention period of 168 hours and a shard count of three.

```
aws cloudcontrol create-resource \
    --type-name AWS::Kinesis::Stream \
    --desired-state "{\"Name\": \"ResourceExample\",\"RetentionPeriodHours\":168, \"ShardCount\":3}"
```

Output:

```
{
    "ProgressEvent": {
        "EventTime": 1632506656.706,
        "TypeName": "AWS::Kinesis::Stream",
        "OperationStatus": "IN_PROGRESS",
        "Operation": "CREATE",
        "Identifier": "ResourceExample",
        "RequestToken": "20999d87-e304-4725-ad84-832dcbfd7fc5"
    }
}
```

For more information, see [Creating a resource](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-create.html) in the *Cloud Control API User Guide*.

## Output

ProgressEvent -> (structure)

Represents the current status of the resource creation request.

After you have initiated a resource creation request, you can monitor the progress of your request by calling [GetResourceRequestStatus](https://docs.aws.amazon.com/cloudcontrolapi/latest/APIReference/API_GetResourceRequestStatus.html) using the `RequestToken` of the `ProgressEvent` returned by `CreateResource` .

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