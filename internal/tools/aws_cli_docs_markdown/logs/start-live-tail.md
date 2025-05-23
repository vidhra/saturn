# start-live-tailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/start-live-tail.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/start-live-tail.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# start-live-tail

## Description

Starts a Live Tail streaming session for one or more log groups. A Live Tail session provides a near real-time streaming of log events as they are ingested into selected log groups. A session can go on for a maximum of 3 hours.

By default, this command start a native tailing session where recent log events appear from the bottom, the log events are output as-is in Plain text.  You can run this command with âmode interactive, which starts an interactive tailing session. Interactive tailing provides the ability to highlight up to 5 terms in your logs. The severity codes are highlighted by default. The logs are output in JSON format if possible, but can be toggled to Plain text if desired. Interactive experience is disabled if âcolor is set to off, or if the output doesnât allow for color.

You must have logs:StartLiveTail permission to perform this operation. If the log events matching the filters are more than 500 events per second, we sample the events to provide the real-time tailing experience.

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and start tailing on Log Group(s) present in the linked source accounts. For more information, see [https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html).

Live Tail sessions incur charges by session usage time, per minute. For pricing details, please refer to [https://aws.amazon.com/cloudwatch/pricing/](https://aws.amazon.com/cloudwatch/pricing/).

## Synopsis

```
start-live-tail
--log-group-identifiers <value> [<value>...]
[--log-stream-names <value> [<value>...]]
[--log-stream-name-prefixes <value> [<value>...]]
[--log-event-filter-pattern <value>]
[--mode <value>]
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

`--log-group-identifiers` (list)
The Log Group Identifiers are the ARNs for the CloudWatch Logs groups to tail. You can provide up to 10 Log Group Identifiers. Logs can be filtered by Log Stream(s) by providing âlog-stream-names or âlog-stream-name-prefixes. If more than one Log Group is provided âlog-stream-names and âlog-stream-name-prefixes is disabled. âlog-stream-names and âlog-stream-name-prefixes canât be provided simultaneously. Note - The Log Group ARN must be in the following format. Replace REGION and ACCOUNT_ID with your Region and account ID. `arn:aws:logs:REGION :ACCOUNT_ID :log-group:LOG_GROUP_NAME`. A `:*` after the ARN is prohibited.For more information about ARN format, see [CloudWatch Logs resources and operations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/iam-access-control-overview-cwl.html) .(string)

Syntax:

```
"string" "string" ...
```

`--log-stream-names` (list)
The list of stream names to filter logs by. This parameter cannot be specified when âlog-stream-name-prefixes are also specified. This parameter cannot be specified when multiple log-group-identifiers are specified(string)

Syntax:

```
"string" "string" ...
```

`--log-stream-name-prefixes` (list)
The prefix to filter logs by. Only events from log streams with names beginning with this prefix will be returned. This parameter cannot be specified when âlog-stream-names is also specified. This parameter cannot be specified when multiple log-group-identifiers are specified(string)

Syntax:

```
"string" "string" ...
```

`--log-event-filter-pattern` (string)
The filter pattern to use. See [Filter and Pattern Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/FilterAndPatternSyntax.html) for details. If not provided, all the events are matched. This option can be used to include or exclude log events patterns. Additionally, when multiple filter patterns are provided, they must be encapsulated by quotes.

`--mode` (string)
The command support the following modes:

- interative - Starts a Live Tail session in interactive mode. In an interactive session, you can highlight as many as five terms in the tailed logs. The severity codes are highlighted by default. Press h to enter the highlight mode and then type in the terms to be highlighted, one at a time, and press enter. Press c to clear the highlighted term(s). Press t to toggle formatting between JSON/Plain text. Press Esc to exit the Live Tail session. The interactive experience is disabled if you specify âcolor as off, or if coloring is not allowed by your output. Press up / down keys to scroll up or down between log events, use Ctrl + u / Ctrl + d to scroll faster. Press q to scroll to latest log events.
- print-only - Starts a LiveTail session in print-only mode. In print-only mode logs are tailed and are printed as-is. This mode can be used in conjunction with other shell commands.

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

The following command starts a Live Tail session on a log group named `my-logs`:

```
aws logs start-live-tail --log-group-identifiers arn:aws:logs:us-east-1:111111222222:log-group:my-logs
```

The following command starts a Live Tail session on a log group named `my-logs` in interactive mode:

```
aws logs start-live-tail --log-group-identifiers arn:aws:logs:us-east-1:111111222222:log-group:my-logs --mode interactive
```

In interactive mode you can highlight as many as five terms in the tailed logs. The severity codes are highlighted by default.
Press `h` to enter the highlight mode and then type in the terms to be highlighted, one at a time, and press enter. Press `c` to clear the highlighted term(s).
Press `t` to toggle formatting between JSON/Plain text. Press `Esc` to exit the Live Tail session.
Press `up` / `down` keys to scroll up or down between log events, use `Ctrl + u` / `Ctrl + d` to scroll faster. Press `q` to scroll to latest log events.