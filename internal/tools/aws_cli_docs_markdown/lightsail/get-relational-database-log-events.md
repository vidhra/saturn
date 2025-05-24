# get-relational-database-log-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-log-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-relational-database-log-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-relational-database-log-events

## Description

Returns a list of log events for a database in Amazon Lightsail.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetRelationalDatabaseLogEvents)

## Synopsis

```
get-relational-database-log-events
--relational-database-name <value>
--log-stream-name <value>
[--start-time <value>]
[--end-time <value>]
[--start-from-head | --no-start-from-head]
[--page-token <value>]
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

`--relational-database-name` (string)

The name of your database for which to get log events.

`--log-stream-name` (string)

The name of the log stream.

Use the `get relational database log streams` operation to get a list of available log streams.

`--start-time` (timestamp)

The start of the time interval from which to get log events.

Constraints:

- Specified in Coordinated Universal Time (UTC).
- Specified in the Unix time format. For example, if you wish to use a start time of October 1, 2018, at 8 PM UTC, then you input `1538424000` as the start time.

`--end-time` (timestamp)

The end of the time interval from which to get log events.

Constraints:

- Specified in Coordinated Universal Time (UTC).
- Specified in the Unix time format. For example, if you wish to use an end time of October 1, 2018, at 8 PM UTC, then you input `1538424000` as the end time.

`--start-from-head` | `--no-start-from-head` (boolean)

Parameter to specify if the log should start from head or tail. If `true` is specified, the log event starts from the head of the log. If `false` is specified, the log event starts from the tail of the log.

### Note

For PostgreSQL, the default value of `false` is the only option available.

`--page-token` (string)

The token to advance to the next or previous page of results from your request.

To get a page token, perform an initial `GetRelationalDatabaseLogEvents` request. If your results are paginated, the response will return a next forward token and/or next backward token that you can specify as the page token in a subsequent request.

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

**To get log events for a relational database**

The following `get-relational-database-log-events` example displays details about the specified log between `1570733176` and `1571597176` for relational database `Database1`. The information returned is configured to start from `head`.

We recommend that you use a unix time converter to identify the start and end times.

```
aws lightsail get-relational-database-log-events \
    --relational-database-name Database1 \
    --log-stream-name error \
    --start-from-head \
    --start-time 1570733176 \
    --end-time 1571597176
```

Output:

```
{
    "resourceLogEvents": [
        {
            "createdAt": 1570820267.0,
            "message": "2019-10-11 18:57:47 20969 [Warning] IP address '192.0.2.0' could not be resolved: Name or service not known"
        },
        {
            "createdAt": 1570860974.0,
            "message": "2019-10-12 06:16:14 20969 [Warning] IP address '8192.0.2.0' could not be resolved: Temporary failure in name resolution"
        },
        {
            "createdAt": 1570860977.0,
            "message": "2019-10-12 06:16:17 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution"
        },
        {
            "createdAt": 1570860979.0,
            "message": "2019-10-12 06:16:19 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution"
        },
        {
            "createdAt": 1570860981.0,
            "message": "2019-10-12 06:16:21 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution"
        },
        {
            "createdAt": 1570860982.0,
            "message": "2019-10-12 06:16:22 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution"
        },
        {
            "createdAt": 1570860984.0,
            "message": "2019-10-12 06:16:24 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution"
        },
        {
            "createdAt": 1570860986.0,
            "message": "2019-10-12 06:16:26 20969 [Warning] IP address '192.0.2.0' could not be resolved: Temporary failure in name resolution"
        },
        ...
        }
    ],
    "nextBackwardToken": "eEXAMPLEZXJUZXh0IjoiZnRWb3F3cUpRSlQ5NndMYThxelRUZlFhR3J6c2dKWEEvM2kvajZMZzVVVWpqRDN0YjFXTjNrak5pRk9iVFRZdjkwVGlpZGw5NFJGSFRQTEdJSjdpQnFCRk5CZFJlYTZaSXpScStuZjJEYXhqM2grUFVJOEpIYlU5YWJ2QitvQWN5cEFyVUo3VDk1QWY3bVF6MEwvcVovVldZdGc9Iiwibm9uY2UiOiJBNHpzdWMvUkZZKzRvUzhEIiwiY2lwaGVyIjoiQUVTL0dDTS9Ob1BhZGEXAMPLEQ==",
    "nextForwardToken": "eEXAMPLEZXJUZXh0IjoiT09Lb0Z6ZFRJbHhaNEQ5N2tPbkkwRmwwNUxPZjFTbFFwUklQbzlSaWgvMWVXbEk4aG56VHg4bW1Gb3grbDVodUVNZEdiZXN0TzVYcjlLK1FUdFB2RlJLS2FMcU05WkN3Rm1uVzBkOFpDR2g0b1BBVlg2NVFGNDNPazZzRXJieHRuU0xzdkRNTkFUMTZibU9HM2YyaGxiS0hUUDA9Iiwibm9uY2UiOiJFQmI4STQ3cU5aWXNXZ0g4IiwiY2lwaGVyIjoiQUVTL0dDTS9Ob1BhZGEXAMPLEQ=="
}
```

## Output

resourceLogEvents -> (list)

An object describing the result of your get relational database log events request.

(structure)

Describes a database log event.

createdAt -> (timestamp)

The timestamp when the database log event was created.

message -> (string)

The message of the database log event.

nextBackwardToken -> (string)

A token used for advancing to the previous page of results from your get relational database log events request.

nextForwardToken -> (string)

A token used for advancing to the next page of results from your get relational database log events request.