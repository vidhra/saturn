# selectÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ddb/select.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ddb/select.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ddb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ddb/index.html#cli-aws-ddb) ]

# select

## Description

`select` searches a table or index.

Under the hood, this operation will use `query` if `--key-condition` is specified, or `scan` otherwise.

Only `yaml` output is supported for this operation.

## Synopsis

```
select
<table-name>
[--index-name <value>]
[--projection <value> [<value>...]]
[--filter <value> [<value>...]]
[--key-condition <value> [<value>...]]
[--attributes <value>]
[--consistent-read | --no-consistent-read]
[--return-consumed-capacity | --no-return-consumed-capacity]
[--starting-token <value>]
[--max-items <value>]
[--page-size <value>]
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

`table_name` (string)

The name of your DynamoDB table.

`--index-name` (string)

The name of a secondary index to scan. This index can be any local secondary index or global secondary index.

`--projection` (string)

A string that identifies one or more attributes to retrieve from the specified table or index. These attributes can include scalars, sets, or elements of a JSON document. The attributes in the expression must be separated by commas. If any of the requested attributes are not found, they will not appear in the result.

For more information, see [Accessing Item Attributes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ProjectionExpressions.html) in the *Amazon DynamoDB Developer Guide* .

For CLI specific syntax see [aws help ddb-expressions](https://docs.aws.amazon.com/cli/latest/topic/ddb-expressions.html)

`--filter` (string)

A string that contains conditions that DynamoDB applies after the operation, but before the data is returned to you. Items that do not satisfy the `--filter` criteria are not returned.

### Note

A `--filter` is applied after the items have already been read; the process of filtering does not consume any additional read capacity units.

For more information, see [Filter Expressions](http://docs.aws.amazon.com/amazondynamodb/latest/developerguide/QueryAndScan.html#FilteringResults) in the *Amazon DynamoDB Developer Guide* .

For CLI specific syntax see [aws help ddb-expressions](https://docs.aws.amazon.com/cli/latest/topic/ddb-expressions.html)

`--key-condition` (string)

The condition that specifies the key value(s) for items to be retrieved. Must perform an equality test on a single partition key value.

The condition can optionally perform one of several comparison tests on a single sort key value. This allows `select` to retrieve one item with a given partition key value and sort key value, or several items that have the same partition key value but different sort key values.

The partition key equality test must be specified in the following format:

`partitionKeyName = :partitionkeyval`

If you also want to provide a condition for the sort key, it must be combined using `AND` with the condition for the sort key.

Valid comparisons for the sort key condition are as follows:

- `sortKeyName = :sortkeyval` - true if the sort key value is equal to `:sortkeyval` .
- `sortKeyName < :sortkeyval` - true if the sort key value is less than `:sortkeyval` .
- `sortKeyName <= :sortkeyval` - true if the sort key value is less than or equal to `:sortkeyval` .
- `sortKeyName > :sortkeyval` - true if the sort key value is greater than `:sortkeyval` .
- `sortKeyName >= :sortkeyval` - true if the sort key value is greater than or equal to `:sortkeyval` .
- `sortKeyName BETWEEN :sortkeyval1 AND :sortkeyval2` - true if the sort key value is greater than or equal to `:sortkeyval1` , and less than or equal to `:sortkeyval2` .
- `begins_with(sortKeyName, :sortkeyval)` - true if the sort key value begins with a particular operand. (You cannot use this function with a sort key that is of type Number.) Note that the function name `begins_with` is case-sensitive.

For CLI specific syntax see [aws help ddb-expressions](https://docs.aws.amazon.com/cli/latest/topic/ddb-expressions.html)

`--attributes` (string)

The attributes to be returned in the result. You can retrieve all item attributes, specific item attributes, the count of matching items, or in the case of an index, some or all of the attributes projected into the index.

- `ALL` - Returns all of the item attributes from the specified table or index. If you query a local secondary index, then for each matching item in the index DynamoDB will fetch the entire item from the parent table. If the index is configured to project all item attributes, then all of the data can be obtained from the local secondary index, and no fetching is required.
- `ALL_PROJECTED` - Allowed only when querying an index. Retrieves all attributes that have been projected into the index. If the index is configured to project all attributes, this return value is equivalent to specifying `ALL`.
- `COUNT` - Returns the number of matching items, rather than the matching items themselves.

`--consistent-read` | `--no-consistent-read` (boolean)

Determines the read consistency model: If set to `--consistent-read` , then the operation uses strongly consistent reads; otherwise, the operation uses eventually consistent reads. Strongly consistent reads are not supported on global secondary indexes. If you query a global secondary index with `--consistent-read` , you will receive a `ValidationException` .

`--return-consumed-capacity` | `--no-return-consumed-capacity` (boolean)

Will include the aggregate `ConsumedCapacity` for the operation. If `--index-name` is also specified, then the `ConsumedCapacity` for each table and secondary index that was accessed will be returned.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To scan an entire table**

This example scans the entire *MusicCollection* table, and then narrows the
results to songs by the artist âNo One You Knowâ. For each item, only the album
title and song title are returned.

Command:

```
aws ddb select MusicCollection --projection 'SongTitle, AlbumTitle' \
    --filter 'Artist = "No One You Know"'
```

Output:

```
Count: 2
Items:
- SongTitle: "Call Me Today"
  AlbumTitle: "Somewhat Famous"
- SongTitle: "Scared of My Shadow"
  AlbumTitle: "Blue Sky Blues"
ScannedCount: 3
```

**To query for specific primary keys**

This example queries items in the *MusicCollection* table. The table has a
hash-and-range primary key (*Artist* and *SongTitle*), but this query only
specifies the hash key value. It returns song titles by the artist named âNo
One You Knowâ.

Command:

```
aws ddb select MusicCollection --projection SongTitle \
    --key-condition 'Artist = "No One You Know"'
```

Output:

```
Count: 2
Items:
- SongTitle: "Call Me Today"
- SongTitle: "Scared of My Shadow"
ScannedCount: 2
```