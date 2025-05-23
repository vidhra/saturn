# put-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [events](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/index.html#cli-aws-events) ]

# put-events

## Description

Sends custom events to Amazon EventBridge so that they can be matched to rules.

You can batch multiple event entries into one request for efficiency. However, the total entry size must be less than 256KB. You can calculate the entry size before you send the events. For more information, see [Calculating PutEvents event entry size](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-putevents.html#eb-putevent-size) in the * *Amazon EventBridge User Guide* * .

PutEvents accepts the data in JSON format. For the JSON number (integer) data type, the constraints are: a minimum value of -9,223,372,036,854,775,808 and a maximum value of 9,223,372,036,854,775,807.

### Note

PutEvents will only process nested JSON up to 1000 levels deep.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/eventbridge-2015-10-07/PutEvents)

## Synopsis

```
put-events
--entries <value>
[--endpoint-id <value>]
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

`--entries` (list)

The entry that defines an event in your system. You can specify several parameters for the entry such as the source and type of the event, resources associated with the event, and so on.

(structure)

Represents an event to be submitted.

Time -> (timestamp)

The time stamp of the event, per [RFC3339](https://www.rfc-editor.org/rfc/rfc3339.txt) . If no time stamp is provided, the time stamp of the [PutEvents](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_PutEvents.html) call is used.

Source -> (string)

The source of the event.

### Note

`Detail` , `DetailType` , and `Source` are required for EventBridge to successfully send an event to an event bus. If you include event entries in a request that do not include each of those properties, EventBridge fails that entry. If you submit a request in which *none* of the entries have each of these properties, EventBridge fails the entire request.

Resources -> (list)

Amazon Web Services resources, identified by Amazon Resource Name (ARN), which the event primarily concerns. Any number, including zero, may be present.

(string)

DetailType -> (string)

Free-form string, with a maximum of 128 characters, used to decide what fields to expect in the event detail.

### Note

`Detail` , `DetailType` , and `Source` are required for EventBridge to successfully send an event to an event bus. If you include event entries in a request that do not include each of those properties, EventBridge fails that entry. If you submit a request in which *none* of the entries have each of these properties, EventBridge fails the entire request.

Detail -> (string)

A valid JSON object. There is no other schema imposed. The JSON object may contain fields and nested sub-objects.

### Note

`Detail` , `DetailType` , and `Source` are required for EventBridge to successfully send an event to an event bus. If you include event entries in a request that do not include each of those properties, EventBridge fails that entry. If you submit a request in which *none* of the entries have each of these properties, EventBridge fails the entire request.

EventBusName -> (string)

The name or ARN of the event bus to receive the event. Only the rules that are associated with this event bus are used to match the event. If you omit this, the default event bus is used.

### Note

If youâre using a global endpoint with a custom bus, you can enter either the name or Amazon Resource Name (ARN) of the event bus in either the primary or secondary Region here. EventBridge then determines the corresponding event bus in the other Region based on the endpoint referenced by the `EndpointId` . Specifying the event bus ARN is preferred.

TraceHeader -> (string)

An X-Ray trace header, which is an http header (X-Amzn-Trace-Id) that contains the trace-id associated with the event.

To learn more about X-Ray trace headers, see [Tracing header](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html#xray-concepts-tracingheader) in the X-Ray Developer Guide.

Shorthand Syntax:

```
Time=timestamp,Source=string,Resources=string,string,DetailType=string,Detail=string,EventBusName=string,TraceHeader=string ...
```

JSON Syntax:

```
[
  {
    "Time": timestamp,
    "Source": "string",
    "Resources": ["string", ...],
    "DetailType": "string",
    "Detail": "string",
    "EventBusName": "string",
    "TraceHeader": "string"
  }
  ...
]
```

`--endpoint-id` (string)

The URL subdomain of the endpoint. For example, if the URL for Endpoint is [https://abcde.veo.endpoints.event.amazonaws.com](https://abcde.veo.endpoints.event.amazonaws.com), then the EndpointId is `abcde.veo` .

### Warning

When using Java, you must include `auth-crt` on the class path.

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

**To send a custom event to CloudWatch Events**

This example sends a custom event to CloudWatch Events. The event is contained within the putevents.json file:

```
aws events put-events --entries file://putevents.json
```

Here are the contents of the putevents.json file:

```
[
  {
    "Source": "com.mycompany.myapp",
    "Detail": "{ \"key1\": \"value1\", \"key2\": \"value2\" }",
    "Resources": [
      "resource1",
      "resource2"
    ],
    "DetailType": "myDetailType"
  },
  {
    "Source": "com.mycompany.myapp",
    "Detail": "{ \"key1\": \"value3\", \"key2\": \"value4\" }",
    "Resources": [
      "resource1",
      "resource2"
    ],
    "DetailType": "myDetailType"
   }
]
```

## Output

FailedEntryCount -> (integer)

The number of failed entries.

Entries -> (list)

The successfully and unsuccessfully ingested events results. If the ingestion was successful, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.

For each record, the index of the response element is the same as the index in the request array.

(structure)

Represents the results of an event submitted to an event bus.

If the submission was successful, the entry has the event ID in it. Otherwise, you can use the error code and error message to identify the problem with the entry.

For information about the errors that are common to all actions, see [Common Errors](https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html) .

EventId -> (string)

The ID of the event.

ErrorCode -> (string)

The error code that indicates why the event submission failed.

Retryable errors include:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-events.html#id1)[InternalFailure](https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html) ``   The request processing has failed because of an unknown error, exception or failure.
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-events.html#id3)[ThrottlingException](https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html) ``   The request was denied due to request throttling.

Non-retryable errors include:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/put-events.html#id5)[AccessDeniedException](https://docs.aws.amazon.com/eventbridge/latest/APIReference/CommonErrors.html) ``   You do not have sufficient access to perform this action.
- `InvalidAccountIdException`   The account ID provided is not valid.
- `InvalidArgument`   A specified parameter is not valid.
- `MalformedDetail`   The JSON provided is not valid.
- `RedactionFailure`   Redacting the CloudTrail event failed.
- `NotAuthorizedForSourceException`   You do not have permissions to publish events with this source onto this event bus.
- `NotAuthorizedForDetailTypeException`   You do not have permissions to publish events with this detail type onto this event bus.

ErrorMessage -> (string)

The error message that explains why the event submission failed.