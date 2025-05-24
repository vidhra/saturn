# execute-gremlin-profile-queryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/execute-gremlin-profile-query.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/execute-gremlin-profile-query.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptunedata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/index.html#cli-aws-neptunedata) ]

# execute-gremlin-profile-query

## Description

Executes a Gremlin Profile query, which runs a specified traversal, collects various metrics about the run, and produces a profile report as output. See [Gremlin profile API in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html) for details.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:ReadDataViaQuery](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#readdataviaquery) IAM action in that cluster.

Note that the [neptune-db:QueryLanguage:Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys) IAM condition key can be used in the policy document to restrict the use of Gremlin queries (see [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html) ).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptunedata-2023-08-01/ExecuteGremlinProfileQuery)

## Synopsis

```
execute-gremlin-profile-query
--gremlin-query <value>
[--results | --no-results]
[--chop <value>]
[--serializer <value>]
[--index-ops | --no-index-ops]
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

`--gremlin-query` (string)

The Gremlin query string to profile.

`--results` | `--no-results` (boolean)

If this flag is set to `TRUE` , the query results are gathered and displayed as part of the profile report. If `FALSE` , only the result count is displayed.

`--chop` (integer)

If non-zero, causes the results string to be truncated at that number of characters. If set to zero, the string contains all the results.

`--serializer` (string)

If non-null, the gathered results are returned in a serialized response message in the format specified by this parameter. See [Gremlin profile API in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html) for more information.

`--index-ops` | `--no-index-ops` (boolean)

If this flag is set to `TRUE` , the results include a detailed report of all index operations that took place during query execution and serialization.

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

output -> (blob)

A text blob containing the Gremlin Profile result. See [Gremlin profile API in Neptune](https://docs.aws.amazon.com/neptune/latest/userguide/gremlin-profile-api.html) for details.