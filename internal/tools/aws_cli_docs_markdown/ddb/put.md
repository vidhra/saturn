# putÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ddb/put.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ddb/put.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ddb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ddb/index.html#cli-aws-ddb) ]

# put

## Description

`put` puts one or more items into a table.

## Synopsis

```
put
<table-name>
<items>
[--condition <value> [<value>...]]
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

`items` (string)

One or more items to put into the table, in YAML format.

`--condition` (string)

A condition that must be satisfied in order for a conditional `put` operation to succeed.

For more information, see [Comparison Operator and Function Reference](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html) in the *Amazon DynamoDB Developer Guide*

For CLI specific syntax see [aws help ddb-expressions](https://docs.aws.amazon.com/cli/latest/topic/ddb-expressions.html)

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

**To add an item to a table**

This example adds a new item to the *MusicCollection* table.

Command:

```
aws ddb put MusicCollection '{Artist: "No One You Know", SongTitle: "Call Me Today", AlbumTitle: "Somewhat Famous"}'
```

**To add items to a table from a file**

This example adds two new items from a file to the *MusicCollection* table.

Command:

```
aws ddb put MusicCollection file://items.json
```

The items to add to the table are in a JSON file, `items.json`. Here are the
contents of that file:

```
[
    {
        "Artist": "No One You Know",
        "SongTitle": "Call Me Today",
        "AlbumTitle": "Somewhat Famous"
    },
    {
        "Artist": "No One You Know",
        "SongTitle": "Scared of My Shadow",
        "AlbumTitle": "Blue Sky Blues"
    }
]
```

**To add items to a table from stdin**

This example adds a new item to the *MusicCollection* table by reading it from
stdin.

Command:

```
echo '{Artist: "No One You Know", SongTitle: "Call Me Today"}' \
    | aws ddb put MusicCollection -
```

**Conditional Expressions**

This example shows how to perform a one-line conditional operation.
This put call to the table *MusicCollection* table will only succeed if the
artist âObscure Indie Bandâ does not exist in the table.

Command:

```
aws ddb put MusicCollection '{Artist: "Obscure Indie Band", SongTitle: "Atlas"}' \
    --condition 'attribute_not_exists(Artist)'
```

If the key already exists, you should see:

Output:

```
A client error (ConditionalCheckFailedException) occurred when calling the PutItem operation: The conditional request failed
```