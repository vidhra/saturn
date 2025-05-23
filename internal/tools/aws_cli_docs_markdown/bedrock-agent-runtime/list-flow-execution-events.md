# list-flow-execution-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent-runtime/list-flow-execution-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent-runtime/list-flow-execution-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-agent-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent-runtime/index.html#cli-aws-bedrock-agent-runtime) ]

# list-flow-execution-events

## Description

Lists events that occurred during an asynchronous execution of a flow. Events provide detailed information about the execution progress, including node inputs and outputs, flow inputs and outputs, condition results, and failure events.

### Note

Asynchronous flows is in preview release for Amazon Bedrock and is subject to change.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agent-runtime-2023-07-26/ListFlowExecutionEvents)

`list-flow-execution-events` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

`list-flow-execution-events` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `flowExecutionEvents`

## Synopsis

```
list-flow-execution-events
--event-type <value>
--execution-identifier <value>
--flow-alias-identifier <value>
--flow-identifier <value>
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

`--event-type` (string)

The type of events to retrieve. Specify `Node` for node-level events or `Flow` for flow-level events.

Possible values:

- `Node`
- `Flow`

`--execution-identifier` (string)

The unique identifier of the async execution.

`--flow-alias-identifier` (string)

The unique identifier of the flow alias used for the execution.

`--flow-identifier` (string)

The unique identifier of the flow.

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

## Output

flowExecutionEvents -> (list)

A list of events that occurred during the async execution. Events can include node inputs and outputs, flow inputs and outputs, condition results, and failure events.

(tagged union structure)

Represents an event that occurred during an async execution. This is a union type that can contain one of several event types, such as node input and output events; flow input and output events; condition node result events, or failure events.

### Note

Asynchronous flows is in preview release for Amazon Bedrock and is subject to change.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `conditionResultEvent`, `flowFailureEvent`, `flowInputEvent`, `flowOutputEvent`, `nodeFailureEvent`, `nodeInputEvent`, `nodeOutputEvent`.

conditionResultEvent -> (structure)

Contains information about a condition evaluation result during the async execution. This event is generated when a condition node in the flow evaluates its conditions.

nodeName -> (string)

The name of the condition node that evaluated the conditions.

satisfiedConditions -> (list)

A list of conditions that were satisfied during the evaluation.

(structure)

Represents a condition that was satisfied during a condition node evaluation in a flowâs async execution.

### Note

Asynchronous flows is in preview release for Amazon Bedrock and is subject to change.

conditionName -> (string)

The name of the condition that was satisfied.

timestamp -> (timestamp)

The timestamp when the condition evaluation occurred.

flowFailureEvent -> (structure)

Contains information about a failure that occurred at the flow level during execution.

errorCode -> (string)

The error code that identifies the type of failure that occurred.

errorMessage -> (string)

A descriptive message that provides details about the failure.

timestamp -> (timestamp)

The timestamp when the failure occurred.

flowInputEvent -> (structure)

Contains information about the inputs provided to the flow at the start of execution.

fields -> (list)

A list of input fields provided to the flow.

(structure)

Represents an input field provided to a flow during an async execution.

### Note

Asynchronous flows is in preview release for Amazon Bedrock and is subject to change.

content -> (tagged union structure)

The content of the input field, which can contain text or structured data.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `document`.

document -> (document)

The document content of the field, which can contain text or structured data.

name -> (string)

The name of the input field as defined in the flowâs input schema.

nodeName -> (string)

The name of the node that receives the inputs.

timestamp -> (timestamp)

The timestamp when the inputs are provided.

flowOutputEvent -> (structure)

Contains information about the outputs produced by the flow at the end of execution.

fields -> (list)

A list of output fields produced by the flow.

(structure)

Represents an output field produced by a flow during an async execution.

### Note

Asynchronous flows is in preview release for Amazon Bedrock and is subject to change.

content -> (tagged union structure)

The content of the output field, which can contain text or structured data.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `document`.

document -> (document)

The document content of the field, which can contain text or structured data.

name -> (string)

The name of the output field as defined in the flowâs output schema.

nodeName -> (string)

The name of the node that produces the outputs.

timestamp -> (timestamp)

The timestamp when the outputs are produced.

nodeFailureEvent -> (structure)

Contains information about a failure that occurred at a specific node during execution.

errorCode -> (string)

The error code that identifies the type of failure that occurred at the node.

errorMessage -> (string)

A descriptive message that provides details about the node failure.

nodeName -> (string)

The name of the node where the failure occurred.

timestamp -> (timestamp)

The timestamp when the node failure occurred.

nodeInputEvent -> (structure)

Contains information about the inputs provided to a specific node during execution.

fields -> (list)

A list of input fields provided to the node.

(structure)

Represents an input field provided to a node during a flowâs async execution.

content -> (tagged union structure)

The content of the input field, which can contain text or structured data.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `document`.

document -> (document)

The document content of the field, which can contain text or structured data.

name -> (string)

The name of the input field as defined in the nodeâs input schema.

nodeName -> (string)

The name of the node that received the inputs.

timestamp -> (timestamp)

The timestamp when the inputs were provided to the node.

nodeOutputEvent -> (structure)

Contains information about the outputs produced by a specific node during execution.

fields -> (list)

A list of output fields produced by the node.

(structure)

Represents an output field produced by a node during a flowâs async execution.

### Note

Asynchronous flows is in preview release for Amazon Bedrock and is subject to change.

content -> (tagged union structure)

The content of the output field, which can contain text or structured data.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `document`.

document -> (document)

The document content of the field, which can contain text or structured data.

name -> (string)

The name of the output field as defined in the nodeâs output schema.

nodeName -> (string)

The name of the node that produced the outputs.

timestamp -> (timestamp)

The timestamp when the outputs were produced by the node.

nextToken -> (string)

A token to retrieve the next set of results. This value is returned if more results are available.