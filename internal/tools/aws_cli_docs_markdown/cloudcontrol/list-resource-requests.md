# list-resource-requestsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/list-resource-requests.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/list-resource-requests.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudcontrol](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudcontrol/index.html#cli-aws-cloudcontrol) ]

# list-resource-requests

## Description

Returns existing resource operation requests. This includes requests of all status types. For more information, see [Listing active resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html#resource-operations-manage-requests-list) in the *Amazon Web Services Cloud Control API User Guide* .

### Note

Resource operation requests expire after 7 days.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudcontrol-2021-09-30/ListResourceRequests)

`list-resource-requests` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ResourceRequestStatusSummaries`

## Synopsis

```
list-resource-requests
[--resource-request-status-filter <value>]
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

`--resource-request-status-filter` (structure)

The filter criteria to apply to the requests returned.

Operations -> (list)

The operation types to include in the filter.

(string)

OperationStatuses -> (list)

The operation statuses to include in the filter.

- `PENDING` : The operation has been requested, but not yet initiated.
- `IN_PROGRESS` : The operation is in progress.
- `SUCCESS` : The operation completed.
- `FAILED` : The operation failed.
- `CANCEL_IN_PROGRESS` : The operation is in the process of being canceled.
- `CANCEL_COMPLETE` : The operation has been canceled.

(string)

Shorthand Syntax:

```
Operations=string,string,OperationStatuses=string,string
```

JSON Syntax:

```
{
  "Operations": ["CREATE"|"DELETE"|"UPDATE", ...],
  "OperationStatuses": ["PENDING"|"IN_PROGRESS"|"SUCCESS"|"FAILED"|"CANCEL_IN_PROGRESS"|"CANCEL_COMPLETE", ...]
}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list the active resource operation requests**

The following `list-resource-requests` example lists the resource requests for CREATE and UPDATE operations that have failed in your AWS account.

```
aws cloudcontrol list-resource-requests \
    --resource-request-status-filter Operations=CREATE,OperationStatuses=FAILED
```

Output:

```
{
    "ResourceRequestStatusSummaries": [
        {
            "TypeName": "AWS::Kinesis::Stream",
            "Identifier": "Demo",
            "RequestToken": "e1a6b86e-46bd-41ac-bfba-633abcdfdbd7",
            "Operation": "CREATE",
            "OperationStatus": "FAILED",
            "EventTime": 1632950268.481,
            "StatusMessage": "Resource of type 'AWS::Kinesis::Stream' with identifier 'Demo' already exists.",
            "ErrorCode": "AlreadyExists"
        }
    ]
}
```

For more information, see [Managing resource operation requests](https://docs.aws.amazon.com/cloudcontrolapi/latest/userguide/resource-operations-manage-requests.html) in the *Cloud Control API User Guide*.

## Output

ResourceRequestStatusSummaries -> (list)

The requests that match the specified filter criteria.

(structure)

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

NextToken -> (string)

If the request doesnât return all of the remaining results, `NextToken` is set to a token. To retrieve the next set of results, call `ListResources` again and assign that token to the request objectâs `NextToken` parameter. If the request returns all results, `NextToken` is set to null.