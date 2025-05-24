# search-channelsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/search-channels.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/search-channels.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-messaging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/index.html#cli-aws-chime-sdk-messaging) ]

# search-channels

## Description

Allows the `ChimeBearer` to search channels by channel members. Users or bots can search across the channels that they belong to. Users in the `AppInstanceAdmin` role can search across all channels.

The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-messaging-2021-05-15/SearchChannels)

## Synopsis

```
search-channels
[--chime-bearer <value>]
--fields <value>
[--max-results <value>]
[--next-token <value>]
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

`--chime-bearer` (string)

The `AppInstanceUserArn` of the user making the API call.

`--fields` (list)

A list of the `Field` objects in the channel being searched.

(structure)

A `Field` of the channel that you want to search.

Key -> (string)

An `enum` value that indicates the key to search the channel on. `MEMBERS` allows you to search channels based on memberships. You can use it with the `EQUALS` operator to get channels whose memberships are equal to the specified values, and with the `INCLUDES` operator to get channels whose memberships include the specified values.

Values -> (list)

The values that you want to search for, a list of strings. The values must be `AppInstanceUserArns` specified as a list of strings.

### Note

This operation isnât supported for `AppInstanceUsers` with large number of memberships.

(string)

Operator -> (string)

The operator used to compare field values, currently `EQUALS` or `INCLUDES` . Use the `EQUALS` operator to find channels whose memberships equal the specified values. Use the `INCLUDES` operator to find channels whose memberships include the specified values.

Shorthand Syntax:

```
Key=string,Values=string,string,Operator=string ...
```

JSON Syntax:

```
[
  {
    "Key": "MEMBERS",
    "Values": ["string", ...],
    "Operator": "EQUALS"|"INCLUDES"
  }
  ...
]
```

`--max-results` (integer)

The maximum number of channels that you want returned.

`--next-token` (string)

The token returned from previous API requests until the number of channels is reached.

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

Channels -> (list)

A list of the channels in the request.

(structure)

Summary of the details of a `Channel` .

Name -> (string)

The name of the channel.

ChannelArn -> (string)

The ARN of the channel.

Mode -> (string)

The mode of the channel.

Privacy -> (string)

The privacy setting of the channel.

Metadata -> (string)

The metadata of the channel.

LastMessageTimestamp -> (timestamp)

The time at which the last persistent message visible to the caller in a channel was sent.

NextToken -> (string)

The token returned from previous API responses until the number of channels is reached.