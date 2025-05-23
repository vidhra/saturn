# get-linked-whatsapp-business-accountÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/socialmessaging/get-linked-whatsapp-business-account.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/socialmessaging/get-linked-whatsapp-business-account.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [socialmessaging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/socialmessaging/index.html#cli-aws-socialmessaging) ]

# get-linked-whatsapp-business-account

## Description

Get the details of your linked WhatsApp Business Account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/socialmessaging-2024-01-01/GetLinkedWhatsAppBusinessAccount)

## Synopsis

```
get-linked-whatsapp-business-account
--id <value>
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

`--id` (string)

The unique identifier, from Amazon Web Services, of the linked WhatsApp Business Account. WABA identifiers are formatted as `waba-01234567890123456789012345678901` . Use [ListLinkedWhatsAppBusinessAccounts](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_ListLinkedWhatsAppBusinessAccounts.html) to list all WABAs and their details.

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

account -> (structure)

The details of the linked WhatsApp Business Account.

arn -> (string)

The ARN of the linked WhatsApp Business Account.

id -> (string)

The ID of the linked WhatsApp Business Account, formatted as `waba-01234567890123456789012345678901` .

wabaId -> (string)

The WhatsApp Business Account ID from meta.

registrationStatus -> (string)

The registration status of the linked WhatsApp Business Account.

linkDate -> (timestamp)

The date the WhatsApp Business Account was linked.

wabaName -> (string)

The name of the linked WhatsApp Business Account.

eventDestinations -> (list)

The event destinations for the linked WhatsApp Business Account.

(structure)

Contains information on the event destination.

eventDestinationArn -> (string)

The ARN of the event destination.

roleArn -> (string)

The Amazon Resource Name (ARN) of an Identity and Access Management role that is able to import phone numbers and write events.

phoneNumbers -> (list)

The phone numbers associated with the Linked WhatsApp Business Account.

(structure)

The details of a linked phone number.

arn -> (string)

The full Amazon Resource Name (ARN) for the phone number.

phoneNumber -> (string)

The phone number associated with the Linked WhatsApp Business Account.

phoneNumberId -> (string)

The phone number ID. Phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901` .

metaPhoneNumberId -> (string)

The phone number ID from Meta.

displayPhoneNumberName -> (string)

The display name for this phone number.

displayPhoneNumber -> (string)

The phone number that appears in the recipients display.

qualityRating -> (string)

The quality rating of the phone number. This is from Meta.