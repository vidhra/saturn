# showÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/history/show.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/history/show.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [history](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/history/index.html#cli-aws-history) ]

# show

## Description

Shows the various events related to running a specific CLI command. If this command is ran without any positional arguments, it will display the events for the last CLI command ran.

## Synopsis

```
show
command_id <value>
[--include <value> [<value>...]]
[--exclude <value> [<value>...]]
[--format <value>]
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

`command_id` (string)
The ID of the CLI command to show. If this positional argument is omitted, it will show the last the CLI command ran.

`--include` (string)
Specifies which events to **only** include when showing the CLI command. This argument is mutually exclusive with `--exclude`.

`--exclude` (string)
Specifies which events to exclude when showing the CLI command. This argument is mutually exclusive with `--include`.

`--format` (string)
Specifies which format to use in showing the events for the specified CLI command. The following formats are supported:

- detailed - This the default format. It prints out a detailed overview of the CLI command ran. It displays all of the key events in the command lifecycle where each important event has a title and its important values underneath. The events are ordered by timestamp and events of the same API call are associated together with the [`api_id`] notation where events that share the same `api_id` belong to the lifecycle of the same API call.

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