# tailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/tail.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/tail.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# tail

## Description

Tails the logs for a CloudWatch Logs group. By default, the command returns logs from all associated CloudWatch Logs streams during the past ten minutes. Note that there is no guarantee for exact timestamp ordering of logs.

## Synopsis

```
tail
group_name <value>
[--since <value>]
[--follow]
[--format <value>]
[--filter-pattern <value>]
[--log-stream-names <value> [<value>...]]
[--log-stream-name-prefix <value>]
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

`group_name` (string)
The name of the CloudWatch Logs group.

`--since` (string)
From what time to begin displaying logs. By default, logs will be displayed starting from ten minutes in the past. The value provided can be an ISO 8601 timestamp or a relative time. For relative times, provide a number and a single unit. Supported units include:

- `s` - seconds
- `m` - minutes
- `h` - hours
- `d` - days
- `w` - weeks

For example, a value of `5m` would indicate to display logs starting five minutes in the past. Note that multiple units are **not** supported (i.e. `5h30m`)

`--follow` (boolean)
Whether to continuously poll for new logs. By default, the command will exit once there are no more logs to display. To exit from this mode, use Control-C.

`--format` (string)
The format to display the logs. The following formats are supported:

- detailed - This the default format. It prints out the timestamp with millisecond precision and timezones, the log stream name, and the log message.
- short - A shortened format. It prints out the a shortened timestamp and the log message.
- json - Pretty print any messages that are entirely JSON.

`--filter-pattern` (string)
The filter pattern to use. See [Filter and Pattern Syntax](http://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) for details. If not provided, all the events are matched

`--log-stream-names` (string)
The list of stream names to filter logs by. This parameter cannot be specified when `--log-stream-name-prefix` is also specified.

`--log-stream-name-prefix` (string)
The prefix to filter logs by. Only events from log streams with names beginning with this prefix will be returned. This parameter cannot be specified when `log-stream-names` is also specified.

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