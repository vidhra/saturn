# list-channel-membershipsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/list-channel-memberships.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/list-channel-memberships.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime-sdk-messaging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime-sdk-messaging/index.html#cli-aws-chime-sdk-messaging) ]

# list-channel-memberships

## Description

Lists all channel memberships in a channel.

### Note

The `x-amz-chime-bearer` request header is mandatory. Use the ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call as the value in the header.

If you want to list the channels to which a specific app instance user belongs, see the [ListChannelMembershipsForAppInstanceUser](https://docs.aws.amazon.com/chime/latest/APIReference/API_messaging-chime_ListChannelMembershipsForAppInstanceUser.html) API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-sdk-messaging-2021-05-15/ListChannelMemberships)

## Synopsis

```
list-channel-memberships
--channel-arn <value>
[--type <value>]
[--max-results <value>]
[--next-token <value>]
--chime-bearer <value>
[--sub-channel-id <value>]
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

`--channel-arn` (string)

The maximum number of channel memberships that you want returned.

`--type` (string)

The membership type of a user, `DEFAULT` or `HIDDEN` . Default members are returned as part of `ListChannelMemberships` if no type is specified. Hidden members are only returned if the type filter in `ListChannelMemberships` equals `HIDDEN` .

Possible values:

- `DEFAULT`
- `HIDDEN`

`--max-results` (integer)

The maximum number of channel memberships that you want returned.

`--next-token` (string)

The token passed by previous API calls until all requested channel memberships are returned.

`--chime-bearer` (string)

The ARN of the `AppInstanceUser` or `AppInstanceBot` that makes the API call.

`--sub-channel-id` (string)

The ID of the SubChannel in the request.

### Note

Only required when listing a userâs memberships in a particular sub-channel of an elastic channel.

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

ChannelMemberships -> (list)

The information for the requested channel memberships.

(structure)

Summary of the details of a `ChannelMembership` .

Member -> (structure)

A memberâs summary data.

Arn -> (string)

The ARN in an Identity.

Name -> (string)

The name in an Identity.

NextToken -> (string)

The token passed by previous API calls until all requested channel memberships are returned.