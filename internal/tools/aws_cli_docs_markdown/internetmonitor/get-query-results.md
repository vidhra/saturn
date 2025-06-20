# get-query-resultsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/get-query-results.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/get-query-results.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [internetmonitor](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/internetmonitor/index.html#cli-aws-internetmonitor) ]

# get-query-results

## Description

Return the data for a query with the Amazon CloudWatch Internet Monitor query interface. Specify the query that you want to return results for by providing a `QueryId` and a monitor name.

For more information about using the query interface, including examples, see [Using the Amazon CloudWatch Internet Monitor query interface](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-view-cw-tools-cwim-query.html) in the Amazon CloudWatch Internet Monitor User Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/internetmonitor-2021-06-03/GetQueryResults)

## Synopsis

```
get-query-results
--monitor-name <value>
--query-id <value>
[--next-token <value>]
[--max-results <value>]
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

The name of the monitor to return data for.

`--query-id` (string)

The ID of the query that you want to return data results for. A `QueryId` is an internally-generated identifier for a specific query.

`--next-token` (string)

The token for the next set of results. You receive this token from a previous call.

`--max-results` (integer)

The number of query results that you want to return with this call.

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

Fields -> (list)

The fields that the query returns data for. Fields are name-data type pairs, such as `availability_score` -`float` .

(structure)

Defines a field to query for your applicationâs Amazon CloudWatch Internet Monitor data. You create a data repository by running a query of a specific type. Each `QueryType` includes a specific set of fields and datatypes to retrieve data for.

Name -> (string)

The name of a field to query your applicationâs Amazon CloudWatch Internet Monitor data for, such as `availability_score` .

Type -> (string)

The data type for a query field, which must correspond to the field youâre defining for `QueryField` . For example, if the query field name is `availability_score` , the data type is `float` .

Data -> (list)

The data results that the query returns. Data is returned in arrays, aligned with the `Fields` for the query, which creates a repository of Amazon CloudWatch Internet Monitor information for your application. Then, you can filter the information in the repository by using `FilterParameters` that you define.

(list)

(string)

NextToken -> (string)

The token for the next set of results. You receive this token from a previous call.