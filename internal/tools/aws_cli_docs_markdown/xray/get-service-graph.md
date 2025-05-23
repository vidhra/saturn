# get-service-graphÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-service-graph.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-service-graph.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [xray](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/index.html#cli-aws-xray) ]

# get-service-graph

## Description

Retrieves a document that describes services that process incoming requests, and downstream services that they call as a result. Root services process incoming requests and make calls to downstream services. Root services are applications that use the [Amazon Web Services X-Ray SDK](https://docs.aws.amazon.com/xray/index.html) . Downstream services can be other applications, Amazon Web Services resources, HTTP web APIs, or SQL databases.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetServiceGraph)

`get-service-graph` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Services`

## Synopsis

```
get-service-graph
--start-time <value>
--end-time <value>
[--group-name <value>]
[--group-arn <value>]
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

The start of the time frame for which to generate a graph.

`--end-time` (timestamp)

The end of the timeframe for which to generate a graph.

`--group-name` (string)

The name of a group based on which you want to generate a graph.

`--group-arn` (string)

The Amazon Resource Name (ARN) of a group based on which you want to generate a graph.

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

**To get a service graph**

The following example displays a document within a specified time period that describes services processing incoming requests, and the downstream services that they call as a result.:

```
aws xray get-service-graph \
    --start-time 1568835392.0
    --end-time 1568835446.0
```

Output:

```
{
    "Services": [
        {
            "ReferenceId": 0,
            "Name": "Scorekeep",
            "Names": [
                "Scorekeep"
            ],
            "Root": true,
            "Type": "AWS::ElasticBeanstalk::Environment",
            "State": "active",
            "StartTime": 1568835392.0,
            "EndTime": 1568835446.0,
            "Edges": [
                {
                    "ReferenceId": 1,
                    "StartTime": 1568835392.0,
                    "EndTime": 1568835446.0,
                    "SummaryStatistics": {
                        "OkCount": 14,
                        "ErrorStatistics": {
                            "ThrottleCount": 0,
                            "OtherCount": 0,
                            "TotalCount": 0
                        },
                        "FaultStatistics": {
                            "OtherCount": 0,
                            "TotalCount": 0
                        },
                        "TotalCount": 14,
                        "TotalResponseTime": 0.13
                    },
                    "ResponseTimeHistogram": [
                        {
                            "Value": 0.008,
                            "Count": 1
                        },
                        {
                            "Value": 0.005,
                            "Count": 7
                        },
                        {
                            "Value": 0.009,
                            "Count": 1
                        },
                        {
                            "Value": 0.021,
                            "Count": 1
                        },
                        {
                            "Value": 0.038,
                            "Count": 1
                        },
                        {
                            "Value": 0.007,
                            "Count": 1
                        },
                        {
                            "Value": 0.006,
                            "Count": 2
                        }
                    ],
                    "Aliases": []
                },

                ... TRUNCATED FOR BREVITY ...

            ]
        }
    ],
    "StartTime": 1568835392.0,
    "EndTime": 1568835446.0,
    "ContainsOldGroupVersions": false
}
```

For more information, see [Using the AWS X-Ray API with the AWS CLI](https://docs.aws.amazon.com/xray/latest/devguide/xray-api-tutorial.html) in the *AWS X-Ray Developer Guide*.

## Output

StartTime -> (timestamp)

The start of the time frame for which the graph was generated.

EndTime -> (timestamp)

The end of the time frame for which the graph was generated.

Services -> (list)

The services that have processed a traced request during the specified time frame.

(structure)

Information about an application that processed requests, users that made requests, or downstream services, resources, and applications that an application used.

ReferenceId -> (integer)

Identifier for the service. Unique within the service map.

Name -> (string)

The canonical name of the service.

Names -> (list)

A list of names for the service, including the canonical name.

(string)

Root -> (boolean)

Indicates that the service was the first service to process a request.

AccountId -> (string)

Identifier of the Amazon Web Services account in which the service runs.

Type -> (string)

The type of service.

- Amazon Web Services Resource - The type of an Amazon Web Services resource. For example, `AWS::EC2::Instance` for an application running on Amazon EC2 or `AWS::DynamoDB::Table` for an Amazon DynamoDB table that the application used.
- Amazon Web Services Service - The type of an Amazon Web Services service. For example, `AWS::DynamoDB` for downstream calls to Amazon DynamoDB that didnât target a specific table.
- `client` - Represents the clients that sent requests to a root service.
- `remote` - A downstream service of indeterminate type.

State -> (string)

The serviceâs state.

StartTime -> (timestamp)

The start time of the first segment that the service generated.

EndTime -> (timestamp)

The end time of the last segment that the service generated.

Edges -> (list)

Connections to downstream services.

(structure)

Information about a connection between two services. An edge can be a synchronous connection, such as typical call between client and service, or an asynchronous link, such as a Lambda function which retrieves an event from an SNS queue.

ReferenceId -> (integer)

Identifier of the edge. Unique within a service map.

StartTime -> (timestamp)

The start time of the first segment on the edge.

EndTime -> (timestamp)

The end time of the last segment on the edge.

SummaryStatistics -> (structure)

Response statistics for segments on the edge.

OkCount -> (long)

The number of requests that completed with a 2xx Success status code.

ErrorStatistics -> (structure)

Information about requests that failed with a 4xx Client Error status code.

ThrottleCount -> (long)

The number of requests that failed with a 429 throttling status code.

OtherCount -> (long)

The number of requests that failed with untracked 4xx Client Error status codes.

TotalCount -> (long)

The total number of requests that failed with a 4xx Client Error status code.

FaultStatistics -> (structure)

Information about requests that failed with a 5xx Server Error status code.

OtherCount -> (long)

The number of requests that failed with untracked 5xx Server Error status codes.

TotalCount -> (long)

The total number of requests that failed with a 5xx Server Error status code.

TotalCount -> (long)

The total number of completed requests.

TotalResponseTime -> (double)

The aggregate response time of completed requests.

ResponseTimeHistogram -> (list)

A histogram that maps the spread of client response times on an edge. Only populated for synchronous edges.

(structure)

An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value -> (double)

The value of the entry.

Count -> (integer)

The prevalence of the entry.

Aliases -> (list)

Aliases for the edge.

(structure)

An alias for an edge.

Name -> (string)

The canonical name of the alias.

Names -> (list)

A list of names for the alias, including the canonical name.

(string)

Type -> (string)

The type of the alias.

EdgeType -> (string)

Describes an asynchronous connection, with a value of `link` .

ReceivedEventAgeHistogram -> (list)

A histogram that maps the spread of event age when received by consumers. Age is calculated each time an event is received. Only populated when *EdgeType* is `link` .

(structure)

An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value -> (double)

The value of the entry.

Count -> (integer)

The prevalence of the entry.

SummaryStatistics -> (structure)

Aggregated statistics for the service.

OkCount -> (long)

The number of requests that completed with a 2xx Success status code.

ErrorStatistics -> (structure)

Information about requests that failed with a 4xx Client Error status code.

ThrottleCount -> (long)

The number of requests that failed with a 429 throttling status code.

OtherCount -> (long)

The number of requests that failed with untracked 4xx Client Error status codes.

TotalCount -> (long)

The total number of requests that failed with a 4xx Client Error status code.

FaultStatistics -> (structure)

Information about requests that failed with a 5xx Server Error status code.

OtherCount -> (long)

The number of requests that failed with untracked 5xx Server Error status codes.

TotalCount -> (long)

The total number of requests that failed with a 5xx Server Error status code.

TotalCount -> (long)

The total number of completed requests.

TotalResponseTime -> (double)

The aggregate response time of completed requests.

DurationHistogram -> (list)

A histogram that maps the spread of service durations.

(structure)

An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value -> (double)

The value of the entry.

Count -> (integer)

The prevalence of the entry.

ResponseTimeHistogram -> (list)

A histogram that maps the spread of service response times.

(structure)

An entry in a histogram for a statistic. A histogram maps the range of observed values on the X axis, and the prevalence of each value on the Y axis.

Value -> (double)

The value of the entry.

Count -> (integer)

The prevalence of the entry.

ContainsOldGroupVersions -> (boolean)

A flag indicating whether the groupâs filter expression has been consistent, or if the returned service graph may show traces from an older version of the groupâs filter expression.

NextToken -> (string)

Pagination token.