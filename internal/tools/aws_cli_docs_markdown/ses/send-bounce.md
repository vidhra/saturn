# send-bounceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-bounce.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-bounce.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html#cli-aws-ses) ]

# send-bounce

## Description

Generates and sends a bounce message to the sender of an email you received through Amazon SES. You can only use this operation on an email up to 24 hours after you receive it.

### Note

You cannot use this operation to send generic bounces for mail that was not received by Amazon SES.

For information about receiving email through Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html) .

You can execute this operation no more than once per second.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendBounce)

## Synopsis

```
send-bounce
--original-message-id <value>
--bounce-sender <value>
[--explanation <value>]
[--message-dsn <value>]
--bounced-recipient-info-list <value>
[--bounce-sender-arn <value>]
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

`--original-message-id` (string)

The message ID of the message to be bounced.

`--bounce-sender` (string)

The address to use in the âFromâ header of the bounce message. This must be an identity that you have verified with Amazon SES.

`--explanation` (string)

Human-readable text for the bounce message to explain the failure. If not specified, the text is auto-generated based on the bounced recipient information.

`--message-dsn` (structure)

Message-related DSN fields. If not specified, Amazon SES chooses the values.

ReportingMta -> (string)

The reporting MTA that attempted to deliver the message, formatted as specified in [RFC 3464](https://tools.ietf.org/html/rfc3464) (`mta-name-type; mta-name` ). The default value is `dns; inbound-smtp.[region].amazonaws.com` .

ArrivalDate -> (timestamp)

When the message was received by the reporting mail transfer agent (MTA), in [RFC 822](https://www.ietf.org/rfc/rfc0822.txt) date-time format.

ExtensionFields -> (list)

Additional X-headers to include in the DSN.

(structure)

Additional X-headers to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.

For information about receiving email through Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html) .

Name -> (string)

The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

Value -> (string)

The value of the header to add. Must contain 2048 characters or fewer, and must not contain newline characters (ârâ or ânâ).

Shorthand Syntax:

```
ReportingMta=string,ArrivalDate=timestamp,ExtensionFields=[{Name=string,Value=string},{Name=string,Value=string}]
```

JSON Syntax:

```
{
  "ReportingMta": "string",
  "ArrivalDate": timestamp,
  "ExtensionFields": [
    {
      "Name": "string",
      "Value": "string"
    }
    ...
  ]
}
```

`--bounced-recipient-info-list` (list)

A list of recipients of the bounced message, including the information required to create the Delivery Status Notifications (DSNs) for the recipients. You must specify at least one `BouncedRecipientInfo` in the list.

(structure)

Recipient-related information to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.

For information about receiving email through Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html) .

Recipient -> (string)

The email address of the recipient of the bounced email.

RecipientArn -> (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to receive email for the recipient of the bounced email. For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) .

BounceType -> (string)

The reason for the bounce. You must provide either this parameter or `RecipientDsnFields` .

RecipientDsnFields -> (structure)

Recipient-related DSN fields, most of which would normally be filled in automatically when provided with a `BounceType` . You must provide either this parameter or `BounceType` .

FinalRecipient -> (string)

The email address that the message was ultimately delivered to. This corresponds to the `Final-Recipient` in the DSN. If not specified, `FinalRecipient` is set to the `Recipient` specified in the `BouncedRecipientInfo` structure. Either `FinalRecipient` or the recipient in `BouncedRecipientInfo` must be a recipient of the original bounced message.

### Note

Do not prepend the `FinalRecipient` email address with `rfc 822;` , as described in [RFC 3798](https://tools.ietf.org/html/rfc3798) .

Action -> (string)

The action performed by the reporting mail transfer agent (MTA) as a result of its attempt to deliver the message to the recipient address. This is required by [RFC 3464](https://tools.ietf.org/html/rfc3464) .

RemoteMta -> (string)

The MTA to which the remote MTA attempted to deliver the message, formatted as specified in [RFC 3464](https://tools.ietf.org/html/rfc3464) (`mta-name-type; mta-name` ). This parameter typically applies only to propagating synchronous bounces.

Status -> (string)

The status code that indicates what went wrong. This is required by [RFC 3464](https://tools.ietf.org/html/rfc3464) .

DiagnosticCode -> (string)

An extended explanation of what went wrong; this is usually an SMTP response. See [RFC 3463](https://tools.ietf.org/html/rfc3463) for the correct formatting of this parameter.

LastAttemptDate -> (timestamp)

The time the final delivery attempt was made, in [RFC 822](https://www.ietf.org/rfc/rfc0822.txt) date-time format.

ExtensionFields -> (list)

Additional X-headers to include in the DSN.

(structure)

Additional X-headers to include in the Delivery Status Notification (DSN) when an email that Amazon SES receives on your behalf bounces.

For information about receiving email through Amazon SES, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email.html) .

Name -> (string)

The name of the header to add. Must be between 1 and 50 characters, inclusive, and consist of alphanumeric (a-z, A-Z, 0-9) characters and dashes only.

Value -> (string)

The value of the header to add. Must contain 2048 characters or fewer, and must not contain newline characters (ârâ or ânâ).

JSON Syntax:

```
[
  {
    "Recipient": "string",
    "RecipientArn": "string",
    "BounceType": "DoesNotExist"|"MessageTooLarge"|"ExceededQuota"|"ContentRejected"|"Undefined"|"TemporaryFailure",
    "RecipientDsnFields": {
      "FinalRecipient": "string",
      "Action": "failed"|"delayed"|"delivered"|"relayed"|"expanded",
      "RemoteMta": "string",
      "Status": "string",
      "DiagnosticCode": "string",
      "LastAttemptDate": timestamp,
      "ExtensionFields": [
        {
          "Name": "string",
          "Value": "string"
        }
        ...
      ]
    }
  }
  ...
]
```

`--bounce-sender-arn` (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the address in the âFromâ header of the bounce. For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) .

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

MessageId -> (string)

The message ID of the bounce message.