# create-poolÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-pool.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/create-pool.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint-sms-voice-v2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-sms-voice-v2/index.html#cli-aws-pinpoint-sms-voice-v2) ]

# create-pool

## Description

Creates a new pool and associates the specified origination identity to the pool. A pool can include one or more phone numbers and SenderIds that are associated with your Amazon Web Services account.

The new pool inherits its configuration from the specified origination identity. This includes keywords, message type, opt-out list, two-way configuration, and self-managed opt-out configuration. Deletion protection isnât inherited from the origination identity and defaults to false.

If the origination identity is a phone number and is already associated with another pool, an error is returned. A sender ID can be associated with multiple pools.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-sms-voice-v2-2022-03-31/CreatePool)

## Synopsis

```
create-pool
--origination-identity <value>
--iso-country-code <value>
--message-type <value>
[--deletion-protection-enabled | --no-deletion-protection-enabled]
[--tags <value>]
[--client-token <value>]
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

`--origination-identity` (string)

The origination identity to use such as a PhoneNumberId, PhoneNumberArn, SenderId or SenderIdArn. You can use  DescribePhoneNumbers to find the values for PhoneNumberId and PhoneNumberArn while  DescribeSenderIds can be used to get the values for SenderId and SenderIdArn.

After the pool is created you can add more origination identities to the pool by using [AssociateOriginationIdentity](https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_AssociateOriginationIdentity.html) .

### Warning

If you are using a shared AWS End User Messaging SMS and Voice resource then you must use the full Amazon Resource Name(ARN).

`--iso-country-code` (string)

The new two-character code, in ISO 3166-1 alpha-2 format, for the country or region of the new pool.

`--message-type` (string)

The type of message. Valid values are TRANSACTIONAL for messages that are critical or time-sensitive and PROMOTIONAL for messages that arenât critical or time-sensitive. After the pool is created the MessageType canât be changed.

Possible values:

- `TRANSACTIONAL`
- `PROMOTIONAL`

`--deletion-protection-enabled` | `--no-deletion-protection-enabled` (boolean)

By default this is set to false. When set to true the pool canât be deleted. You can change this value using the  UpdatePool action.

`--tags` (list)

An array of tags (key and value pairs) associated with the pool.

(structure)

The list of tags to be added to the specified topic.

Key -> (string)

The key identifier, or name, of the tag.

Value -> (string)

The string value associated with the key of the tag.

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

`--client-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you donât specify a client token, a randomly generated token is used for the request to ensure idempotency.

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

PoolArn -> (string)

The Amazon Resource Name (ARN) for the pool.

PoolId -> (string)

The unique identifier for the pool.

Status -> (string)

The current status of the pool.

- CREATING: The pool is currently being created and isnât yet available for use.
- ACTIVE: The pool is active and available for use.
- DELETING: The pool is being deleted.

MessageType -> (string)

The type of message for the pool to use.

TwoWayEnabled -> (boolean)

By default this is set to false. When set to true you can receive incoming text messages from your end recipients.

TwoWayChannelArn -> (string)

The Amazon Resource Name (ARN) of the two way channel.

TwoWayChannelRole -> (string)

An optional IAM Role Arn for a service to assume, to be able to post inbound SMS messages.

SelfManagedOptOutsEnabled -> (boolean)

By default this is set to false. When an end recipient sends a message that begins with HELP or STOP to one of your dedicated numbers, AWS End User Messaging SMS and Voice automatically replies with a customizable message and adds the end recipient to the OptOutList. When set to true youâre responsible for responding to HELP and STOP requests. Youâre also responsible for tracking and honoring opt-out requests.

OptOutListName -> (string)

The name of the OptOutList associated with the pool.

SharedRoutesEnabled -> (boolean)

Indicates whether shared routes are enabled for the pool. Set to false and only origination identities in this pool are used to send messages.

DeletionProtectionEnabled -> (boolean)

When set to true deletion protection is enabled. By default this is set to false.

Tags -> (list)

An array of tags (key and value pairs) associated with the pool.

(structure)

The list of tags to be added to the specified topic.

Key -> (string)

The key identifier, or name, of the tag.

Value -> (string)

The string value associated with the key of the tag.

CreatedTimestamp -> (timestamp)

The time when the pool was created, in [UNIX epoch time](https://www.epochconverter.com/) format.