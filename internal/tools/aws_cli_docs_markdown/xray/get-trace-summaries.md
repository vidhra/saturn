# get-trace-summariesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-trace-summaries.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-trace-summaries.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [xray](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/index.html#cli-aws-xray) ]

# get-trace-summaries

## Description

Retrieves IDs and annotations for traces available for a specified time frame using an optional filter. To get the full traces, pass the trace IDs to `BatchGetTraces` .

A filter expression can target traced requests that hit specific service nodes or edges, have errors, or come from a known user. For example, the following filter expression targets traces that pass through `api.example.com` :

`service("api.example.com")`

This filter expression finds traces that have an annotation named `account` with the value `12345` :

`annotation.account = "12345"`

For a full list of indexed fields and keywords that you can use in filter expressions, see [Use filter expressions](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray-interface-console.html#xray-console-filters) in the *Amazon Web Services X-Ray Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetTraceSummaries)

`get-trace-summaries` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `TraceSummaries`

## Synopsis

```
get-trace-summaries
--start-time <value>
--end-time <value>
[--time-range-type <value>]
[--sampling | --no-sampling]
[--sampling-strategy <value>]
[--filter-expression <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--start-time` (timestamp)

The start of the time frame for which to retrieve traces.

`--end-time` (timestamp)

The end of the time frame for which to retrieve traces.

`--time-range-type` (string)

Query trace summaries by TraceId (trace start time), Event (trace update time), or Service (trace segment end time).

Possible values:

- `TraceId`
- `Event`
- `Service`

`--sampling` | `--no-sampling` (boolean)

Set to `true` to get summaries for only a subset of available traces.

`--sampling-strategy` (structure)

A parameter to indicate whether to enable sampling on trace summaries. Input parameters are Name and Value.

Name -> (string)

The name of a sampling rule.

Value -> (double)

The value of a sampling rule.

Shorthand Syntax:

```
Name=string,Value=double
```

JSON Syntax:

```
{
  "Name": "PartialScan"|"FixedRate",
  "Value": double
}
```

`--filter-expression` (string)

Specify a filter expression to retrieve trace summaries for services or requests that meet certain requirements.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

**To get a trace summary**

The following `get-trace-summaries` example retrieves IDs and metadata for traces available within a specified time frame.

```
aws xray get-trace-summaries \
    --start-time 1568835392.0 \
    --end-time 1568835446.0
```

Output:

```
[
    "http://scorekeep-env-1.123456789.us-east-2.elasticbeanstalk.com/api/move/VSAE93HF/GSSD2NTB/DP0PCC09",
    "http://scorekeep-env-1.123456789.us-east-2.elasticbeanstalk.com/api/move/GCQ2B35P/FREELDFT/4LRE643M",
    "http://scorekeep-env-1.123456789.us-east-2.elasticbeanstalk.com/api/game/VSAE93HF/GSSD2NTB/starttime/1568835513",
    "http://scorekeep-env-1.123456789.us-east-2.elasticbeanstalk.com/api/move/4MQNA5NN/L99KK2RF/null"
]
```

For more information, see [Using the AWS X-Ray API with the AWS CLI](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-tutorial.html) in the *AWS X-Ray Developer Guide*.

## Output

TraceSummaries -> (list)

Trace IDs and annotations for traces that were found in the specified time frame.

(structure)

Metadata generated from the segment documents in a trace.

Id -> (string)

The unique identifier for the request that generated the traceâs segments and subsegments.

StartTime -> (timestamp)

The start time of a trace, based on the earliest trace segment start time.

Duration -> (double)

The length of time in seconds between the start time of the root segment and the end time of the last segment that completed.

ResponseTime -> (double)

The length of time in seconds between the start and end times of the root segment. If the service performs work asynchronously, the response time measures the time before the response is sent to the user, while the duration measures the amount of time before the last traced activity completes.

HasFault -> (boolean)

The root segment document has a 500 series error.

HasError -> (boolean)

The root segment document has a 400 series error.

HasThrottle -> (boolean)

One or more of the segment documents has a 429 throttling error.

IsPartial -> (boolean)

One or more of the segment documents is in progress.

Http -> (structure)

Information about the HTTP request served by the trace.

HttpURL -> (string)

The request URL.

HttpStatus -> (integer)

The response status.

HttpMethod -> (string)

The request method.

UserAgent -> (string)

The requestâs user agent string.

ClientIp -> (string)

The IP address of the requestor.

Annotations -> (map)

Annotations from the traceâs segment documents.

key -> (string)

value -> (list)

(structure)

Information about a segment annotation.

AnnotationValue -> (structure)

Values of the annotation.

NumberValue -> (double)

Value for a Number annotation.

BooleanValue -> (boolean)

Value for a Boolean annotation.

StringValue -> (string)

Value for a String annotation.

ServiceIds -> (list)

Services to which the annotation applies.

(structure)

Name -> (string)

Names -> (list)

(string)

AccountId -> (string)

Type -> (string)

Users -> (list)

Users from the traceâs segment documents.

(structure)

Information about a user recorded in segment documents.

UserName -> (string)

The userâs name.

ServiceIds -> (list)

Services that the userâs request hit.

(structure)

Name -> (string)

Names -> (list)

(string)

AccountId -> (string)

Type -> (string)

ServiceIds -> (list)

Service IDs from the traceâs segment documents.

(structure)

Name -> (string)

Names -> (list)

(string)

AccountId -> (string)

Type -> (string)

ResourceARNs -> (list)

A list of resource ARNs for any resource corresponding to the trace segments.

(structure)

A list of resources ARNs corresponding to the segments in a trace.

ARN -> (string)

The ARN of a corresponding resource.

InstanceIds -> (list)

A list of EC2 instance IDs for any instance corresponding to the trace segments.

(structure)

A list of EC2 instance IDs corresponding to the segments in a trace.

Id -> (string)

The ID of a corresponding EC2 instance.

AvailabilityZones -> (list)

A list of Availability Zones for any zone corresponding to the trace segments.

(structure)

A list of Availability Zones corresponding to the segments in a trace.

Name -> (string)

The name of a corresponding Availability Zone.

EntryPoint -> (structure)

The root of a trace.

Name -> (string)

Names -> (list)

(string)

AccountId -> (string)

Type -> (string)

FaultRootCauses -> (list)

A collection of FaultRootCause structures corresponding to the trace segments.

(structure)

The root cause information for a trace summary fault.

Services -> (list)

A list of corresponding services. A service identifies a segment and it contains a name, account ID, type, and inferred flag.

(structure)

A collection of fields identifying the services in a trace summary fault.

Name -> (string)

The service name.

Names -> (list)

A collection of associated service names.

(string)

Type -> (string)

The type associated to the service.

AccountId -> (string)

The account ID associated to the service.

EntityPath -> (list)

The path of root cause entities found on the service.

(structure)

A collection of segments and corresponding subsegments associated to a trace summary fault error.

Name -> (string)

The name of the entity.

Exceptions -> (list)

The types and messages of the exceptions.

(structure)

The exception associated with a root cause.

Name -> (string)

The name of the exception.

Message -> (string)

The message of the exception.

Remote -> (boolean)

A flag that denotes a remote subsegment.

Inferred -> (boolean)

A Boolean value indicating if the service is inferred from the trace.

ClientImpacting -> (boolean)

A flag that denotes that the root cause impacts the trace client.

ErrorRootCauses -> (list)

A collection of ErrorRootCause structures corresponding to the trace segments.

(structure)

The root cause of a trace summary error.

Services -> (list)

A list of services corresponding to an error. A service identifies a segment and it contains a name, account ID, type, and inferred flag.

(structure)

A collection of fields identifying the services in a trace summary error.

Name -> (string)

The service name.

Names -> (list)

A collection of associated service names.

(string)

Type -> (string)

The type associated to the service.

AccountId -> (string)

The account ID associated to the service.

EntityPath -> (list)

The path of root cause entities found on the service.

(structure)

A collection of segments and corresponding subsegments associated to a trace summary error.

Name -> (string)

The name of the entity.

Exceptions -> (list)

The types and messages of the exceptions.

(structure)

The exception associated with a root cause.

Name -> (string)

The name of the exception.

Message -> (string)

The message of the exception.

Remote -> (boolean)

A flag that denotes a remote subsegment.

Inferred -> (boolean)

A Boolean value indicating if the service is inferred from the trace.

ClientImpacting -> (boolean)

A flag that denotes that the root cause impacts the trace client.

ResponseTimeRootCauses -> (list)

A collection of ResponseTimeRootCause structures corresponding to the trace segments.

(structure)

The root cause information for a response time warning.

Services -> (list)

A list of corresponding services. A service identifies a segment and contains a name, account ID, type, and inferred flag.

(structure)

A collection of fields identifying the service in a response time warning.

Name -> (string)

The service name.

Names -> (list)

A collection of associated service names.

(string)

Type -> (string)

The type associated to the service.

AccountId -> (string)

The account ID associated to the service.

EntityPath -> (list)

The path of root cause entities found on the service.

(structure)

A collection of segments and corresponding subsegments associated to a response time warning.

Name -> (string)

The name of the entity.

Coverage -> (double)

The type and messages of the exceptions.

Remote -> (boolean)

A flag that denotes a remote subsegment.

Inferred -> (boolean)

A Boolean value indicating if the service is inferred from the trace.

ClientImpacting -> (boolean)

A flag that denotes that the root cause impacts the trace client.

Revision -> (integer)

The revision number of a trace.

MatchedEventTime -> (timestamp)

The matched time stamp of a defined event.

ApproximateTime -> (timestamp)

The start time of this page of results.

TracesProcessedCount -> (long)

The total number of traces processed, including traces that did not match the specified filter expression.

NextToken -> (string)

If the requested time frame contained more than one page of results, you can use this token to retrieve the next page. The first page contains the most recent results, closest to the end of the time frame.