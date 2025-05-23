# execute-queryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/execute-query.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/execute-query.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune-graph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/index.html#cli-aws-neptune-graph) ]

# execute-query

## Description

Execute an openCypher query.

When invoking this operation in a Neptune Analytics cluster, the IAM user or role making the request must have a policy attached that allows one of the following IAM actions in that cluster, depending on the query:

- neptune-graph:ReadDataViaQuery
- neptune-graph:WriteDataViaQuery
- neptune-graph:DeleteDataViaQuery

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-graph-2023-11-29/ExecuteQuery)

`execute-query` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
execute-query
--graph-identifier <value>
--query-string <value>
--language <value>
[--parameters <value>]
[--plan-cache <value>]
[--explain-mode <value>]
[--query-timeout-milliseconds <value>]
<outfile>
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

`--graph-identifier` (string)

The unique identifier of the Neptune Analytics graph.

`--query-string` (string)

The query string to be executed.

`--language` (string)

The query language the query is written in. Currently only openCypher is supported.

Possible values:

- `OPEN_CYPHER`

`--parameters` (map)

The data parameters the query can use in JSON format. For example: {ânameâ: âjohnâ, âageâ: 20}. (optional)

key -> (string)

value -> (document)

JSON Syntax:

```
{"string": {...}
  ...}
```

`--plan-cache` (string)

Query plan cache is a feature that saves the query plan and reuses it on successive executions of the same query. This reduces query latency, and works for both `READ` and `UPDATE` queries. The plan cache is an LRU cache with a 5 minute TTL and a capacity of 1000.

Possible values:

- `ENABLED`
- `DISABLED`
- `AUTO`

`--explain-mode` (string)

The explain mode parameter returns a query explain instead of the actual query results. A query explain can be used to gather insights about the query execution such as planning decisions, time spent on each operator, solutions flowing etc.

Possible values:

- `STATIC`
- `DETAILS`

`--query-timeout-milliseconds` (integer)

Specifies the query timeout duration, in milliseconds. (optional)

`outfile` (string)
Filename where the content will be saved

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

payload -> (streaming blob)

The query results.