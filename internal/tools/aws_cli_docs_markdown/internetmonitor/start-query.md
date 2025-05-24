# start-queryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/start-query.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/start-query.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [internetmonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/index.html#cli-aws-internetmonitor) ]

# start-query

## Description

Start a query to return data for a specific query type for the Amazon CloudWatch Internet Monitor query interface. Specify a time period for the data that you want returned by using `StartTime` and `EndTime` . You filter the query results to return by providing parameters that you specify with `FilterParameters` .

For more information about using the query interface, including examples, see [Using the Amazon CloudWatch Internet Monitor query interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html) in the Amazon CloudWatch Internet Monitor User Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/internetmonitor-2021-06-03/StartQuery)

## Synopsis

```
start-query
--monitor-name <value>
--start-time <value>
--end-time <value>
--query-type <value>
[--filter-parameters <value>]
[--linked-account-id <value>]
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

`--monitor-name` (string)

The name of the monitor to query.

`--start-time` (timestamp)

The timestamp that is the beginning of the period that you want to retrieve data for with your query.

`--end-time` (timestamp)

The timestamp that is the end of the period that you want to retrieve data for with your query.

`--query-type` (string)

The type of query to run. The following are the three types of queries that you can run using the Internet Monitor query interface:

- `MEASUREMENTS` : Provides availability score, performance score, total traffic, and round-trip times, at 5 minute intervals.
- `TOP_LOCATIONS` : Provides availability score, performance score, total traffic, and time to first byte (TTFB) information, for the top location and ASN combinations that youâre monitoring, by traffic volume.
- `TOP_LOCATION_DETAILS` : Provides TTFB for Amazon CloudFront, your current configuration, and the best performing EC2 configuration, at 1 hour intervals.
- `OVERALL_TRAFFIC_SUGGESTIONS` : Provides TTFB, using a 30-day weighted average, for all traffic in each Amazon Web Services location that is monitored.
- `OVERALL_TRAFFIC_SUGGESTIONS_DETAILS` : Provides TTFB, using a 30-day weighted average, for each top location, for a proposed Amazon Web Services location. Must provide an Amazon Web Services location to search.
- `ROUTING_SUGGESTIONS` : Provides the predicted average round-trip time (RTT) from an IP prefix toward an Amazon Web Services location for a DNS resolver. The RTT is calculated at one hour intervals, over a one hour period.

For lists of the fields returned with each query type and more information about how each type of query is performed, see [Using the Amazon CloudWatch Internet Monitor query interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html) in the Amazon CloudWatch Internet Monitor User Guide.

Possible values:

- `MEASUREMENTS`
- `TOP_LOCATIONS`
- `TOP_LOCATION_DETAILS`
- `OVERALL_TRAFFIC_SUGGESTIONS`
- `OVERALL_TRAFFIC_SUGGESTIONS_DETAILS`
- `ROUTING_SUGGESTIONS`

`--filter-parameters` (list)

The `FilterParameters` field that you use with Amazon CloudWatch Internet Monitor queries is a string the defines how you want a query to be filtered. The filter parameters that you can specify depend on the query type, since each query type returns a different set of Internet Monitor data.

For more information about specifying filter parameters, see [Using the Amazon CloudWatch Internet Monitor query interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html) in the Amazon CloudWatch Internet Monitor User Guide.

(structure)

A filter that you use with the results of a Amazon CloudWatch Internet Monitor query that you created and ran. The query sets up a repository of data that is a subset of your applicationâs Internet Monitor data. `FilterParameter` is a string that defines how you want to filter the repository of data to return a set of results, based on your criteria.

The filter parameters that you can specify depend on the query type that you used to create the repository, since each query type returns a different set of Internet Monitor data.

For each filter, you specify a field (such as `city` ), an operator (such as `not_equals` , and a value or array of values (such as `["Seattle", "Redmond"]` ). Separate values in the array with commas.

For more information about specifying filter parameters, see [Using the Amazon CloudWatch Internet Monitor query interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html) in the Amazon CloudWatch Internet Monitor User Guide.

Field -> (string)

A data field that you want to filter, to further scope your applicationâs Internet Monitor data in a repository that you created by running a query. A field might be `city` , for example. The field must be one of the fields that was returned by the specific query that you used to create the repository.

Operator -> (string)

The operator to use with the filter field and a value, such as `not_equals` .

Values -> (list)

One or more values to be used, together with the specified operator, to filter data for a query. For example, you could specify an array of values such as `["Seattle", "Redmond"]` . Values in the array are separated by commas.

(string)

Shorthand Syntax:

```
Field=string,Operator=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Field": "string",
    "Operator": "EQUALS"|"NOT_EQUALS",
    "Values": ["string", ...]
  }
  ...
]
```

`--linked-account-id` (string)

The account ID for an account that youâve set up cross-account sharing for in Amazon CloudWatch Internet Monitor. You configure cross-account sharing by using Amazon CloudWatch Observability Access Manager. For more information, see [Internet Monitor cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cwim-cross-account.html) in the Amazon CloudWatch Internet Monitor User Guide.

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

QueryId -> (string)

The internally-generated identifier of a specific query.