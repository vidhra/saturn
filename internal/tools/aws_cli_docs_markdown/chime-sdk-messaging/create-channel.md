# create-channelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/create-channel.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/create-channel.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-messaging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/index.html#cli-aws-chime-sdk-messaging) ]

# create-channel

## Description

Creates a channel to which you can add users and send messages.

**Restriction** : You canât change a channelâs privacy.

### Note

The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-messaging-2021-05-15/CreateChannel)

## Synopsis

```
create-channel
--app-instance-arn <value>
--name <value>
[--mode <value>]
[--privacy <value>]
[--metadata <value>]
[--client-request-token <value>]
[--tags <value>]
--chime-bearer <value>
[--channel-id <value>]
[--member-arns <value>]
[--moderator-arns <value>]
[--elastic-channel-configuration <value>]
[--expiration-settings <value>]
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

`--app-instance-arn` (string)

The ARN of the channel request.

`--name` (string)

The name of the channel.

`--mode` (string)

The channel mode: `UNRESTRICTED` or `RESTRICTED` . Administrators, moderators, and channel members can add themselves and other members to unrestricted channels. Only administrators and moderators can add members to restricted channels.

Possible values:

- `UNRESTRICTED`
- `RESTRICTED`

`--privacy` (string)

The channelâs privacy level: `PUBLIC` or `PRIVATE` . Private channels arenât discoverable by users outside the channel. Public channels are discoverable by anyone in the `AppInstance` .

Possible values:

- `PUBLIC`
- `PRIVATE`

`--metadata` (string)

The metadata of the creation request. Limited to 1KB and UTF-8.

`--client-request-token` (string)

The client token for the request. An `Idempotency` token.

`--tags` (list)

The tags for the creation request.

(structure)

A tag object containing a key-value pair.

Key -> (string)

The key in a tag.

Value -> (string)

The value in a tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--chime-bearer` (string)

The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.

`--channel-id` (string)

The ID of the channel in the request.

`--member-arns` (list)

The ARNs of the channel members in the request.

(string)

Syntax:

```
"string" "string" ...
```

`--moderator-arns` (list)

The ARNs of the channel moderators in the request.

(string)

Syntax:

```
"string" "string" ...
```

`--elastic-channel-configuration` (structure)

The attributes required to configure and create an elastic channel. An elastic channel can support a maximum of 1-million users, excluding moderators.

MaximumSubChannels -> (integer)

The maximum number of SubChannels that you want to allow in the elastic channel.

TargetMembershipsPerSubChannel -> (integer)

The maximum number of members allowed in a SubChannel.

MinimumMembershipPercentage -> (integer)

The minimum allowed percentage of TargetMembershipsPerSubChannel users. Ceil of the calculated value is used in balancing members among SubChannels of the elastic channel.

Shorthand Syntax:

```
MaximumSubChannels=integer,TargetMembershipsPerSubChannel=integer,MinimumMembershipPercentage=integer
```

JSON Syntax:

```
{
  "MaximumSubChannels": integer,
  "TargetMembershipsPerSubChannel": integer,
  "MinimumMembershipPercentage": integer
}
```

`--expiration-settings` (structure)

Settings that control the interval after which the channel is automatically deleted.

ExpirationDays -> (integer)

The period in days after which the system automatically deletes a channel.

ExpirationCriterion -> (string)

The conditions that must be met for a channel to expire.

Shorthand Syntax:

```
ExpirationDays=integer,ExpirationCriterion=string
```

JSON Syntax:

```
{
  "ExpirationDays": integer,
  "ExpirationCriterion": "CREATED_TIMESTAMP"|"LAST_MESSAGE_TIMESTAMP"
}
```

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

ChannelArn -> (string)

The ARN of the channel.