# send-bulk-emailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/send-bulk-email.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/send-bulk-email.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# send-bulk-email

## Description

Composes an email message to multiple destinations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/SendBulkEmail)

## Synopsis

```
send-bulk-email
[--from-email-address <value>]
[--from-email-address-identity-arn <value>]
[--reply-to-addresses <value>]
[--feedback-forwarding-email-address <value>]
[--feedback-forwarding-email-address-identity-arn <value>]
[--default-email-tags <value>]
--default-content <value>
--bulk-email-entries <value>
[--configuration-set-name <value>]
[--endpoint-id <value>]
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

`--from-email-address` (string)

The email address to use as the âFromâ address for the email. The address that you specify has to be verified.

`--from-email-address-identity-arn` (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the `FromEmailAddress` parameter.

For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use sender@example.com, then you would specify the `FromEmailAddressIdentityArn` to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the `FromEmailAddress` to be [sender@example.com](mailto:sender%40example.com).

For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html) .

`--reply-to-addresses` (list)

The âReply-toâ email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.

(string)

Syntax:

```
"string" "string" ...
```

`--feedback-forwarding-email-address` (string)

The address that you want bounce and complaint notifications to be sent to.

`--feedback-forwarding-email-address-identity-arn` (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the `FeedbackForwardingEmailAddress` parameter.

For example, if the owner of example.com (which has ARN arn:aws:ses:us-east-1:123456789012:identity/example.com) attaches a policy to it that authorizes you to use feedback@example.com, then you would specify the `FeedbackForwardingEmailAddressIdentityArn` to be arn:aws:ses:us-east-1:123456789012:identity/example.com, and the `FeedbackForwardingEmailAddress` to be [feedback@example.com](mailto:feedback%40example.com).

For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/sending-authorization.html) .

`--default-email-tags` (list)

A list of tags, in the form of name/value pairs, to apply to an email that you send using the `SendEmail` operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.

(structure)

Contains the name and value of a tag that you apply to an email. You can use message tags when you publish email sending events.

Name -> (string)

The name of the message tag. The message tag name has to meet the following criteria:

- It can only contain ASCII letters (aâz, AâZ), numbers (0â9), underscores (_), or dashes (-).
- It can contain no more than 256 characters.

Value -> (string)

The value of the message tag. The message tag value has to meet the following criteria:

- It can only contain ASCII letters (aâz, AâZ), numbers (0â9), underscores (_), or dashes (-).
- It can contain no more than 256 characters.

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
  }
  ...
]
```

`--default-content` (structure)

An object that contains the body of the message. You can specify a template message.

Template -> (structure)

The template to use for the bulk email message.

TemplateName -> (string)

The name of the template. You will refer to this name when you send email using the `SendTemplatedEmail` or `SendBulkTemplatedEmail` operations.

TemplateArn -> (string)

The Amazon Resource Name (ARN) of the template.

TemplateContent -> (structure)

The content of the template.

### Note

Amazon SES supports only simple substitions when you send email using the `SendEmail` or `SendBulkEmail` operations and you provide the full template content in the request.

Subject -> (string)

The subject line of the email.

Text -> (string)

The email body that will be visible to recipients whose email clients do not display HTML.

Html -> (string)

The HTML body of the email.

TemplateData -> (string)

An object that defines the values to use for message variables in the template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the value to use for that variable.

Headers -> (list)

The list of message headers that will be added to the email message.

(structure)

Contains the name and value of a message header that you add to an email.

Name -> (string)

The name of the message header. The message header name has to meet the following criteria:

- Can contain any printable ASCII character (33 - 126) except for colon (:).
- Can contain no more than 126 characters.

Value -> (string)

The value of the message header. The message header value has to meet the following criteria:

- Can contain any printable ASCII character.
- Can contain no more than 870 characters.

Attachments -> (list)

The List of attachments to include in your email. All recipients will receive the same attachments.

(structure)

Contains metadata and attachment raw content.

RawContent -> (blob)

The raw data of the attachment. It needs to be base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an Amazon Web Services SDK, the SDK takes care of the base 64-encoding for you.

ContentDisposition -> (string)

A standard descriptor indicating how the attachment should be rendered in the email. Supported values: `ATTACHMENT` or `INLINE` .

FileName -> (string)

The file name for the attachment as it will appear in the email. Amazon SES restricts certain file extensions. To ensure attachments are accepted, check the [Unsupported attachment types](https://docs.aws.amazon.com/ses/latest/dg/mime-types.html) in the Amazon SES Developer Guide.

ContentDescription -> (string)

A brief description of the attachment content.

ContentId -> (string)

Unique identifier for the attachment, used for referencing attachments with INLINE disposition in HTML content.

ContentTransferEncoding -> (string)

Specifies how the attachment is encoded. Supported values: `BASE64` , `QUOTED_PRINTABLE` , `SEVEN_BIT` .

ContentType -> (string)

The MIME type of the attachment.

### Note

Example: `application/pdf` , `image/jpeg`

JSON Syntax:

```
{
  "Template": {
    "TemplateName": "string",
    "TemplateArn": "string",
    "TemplateContent": {
      "Subject": "string",
      "Text": "string",
      "Html": "string"
    },
    "TemplateData": "string",
    "Headers": [
      {
        "Name": "string",
        "Value": "string"
      }
      ...
    ],
    "Attachments": [
      {
        "RawContent": blob,
        "ContentDisposition": "ATTACHMENT"|"INLINE",
        "FileName": "string",
        "ContentDescription": "string",
        "ContentId": "string",
        "ContentTransferEncoding": "BASE64"|"QUOTED_PRINTABLE"|"SEVEN_BIT",
        "ContentType": "string"
      }
      ...
    ]
  }
}
```

`--bulk-email-entries` (list)

The list of bulk email entry objects.

(structure)

Destination -> (structure)

Represents the destination of the message, consisting of To:, CC:, and BCC: fields.

### Note

Amazon SES does not support the SMTPUTF8 extension, as described in [RFC6531](https://tools.ietf.org/html/rfc6531) . For this reason, the local part of a destination email address (the part of the email address that precedes the @ sign) may only contain [7-bit ASCII characters](https://en.wikipedia.org/wiki/Email_address#Local-part) . If the domain part of an address (the part after the @ sign) contains non-ASCII characters, they must be encoded using Punycode, as described in [RFC3492](https://tools.ietf.org/html/rfc3492.html) .

ToAddresses -> (list)

An array that contains the email addresses of the âToâ recipients for the email.

(string)

CcAddresses -> (list)

An array that contains the email addresses of the âCCâ (carbon copy) recipients for the email.

(string)

BccAddresses -> (list)

An array that contains the email addresses of the âBCCâ (blind carbon copy) recipients for the email.

(string)

ReplacementTags -> (list)

A list of tags, in the form of name/value pairs, to apply to an email that you send using the `SendBulkTemplatedEmail` operation. Tags correspond to characteristics of the email that you define, so that you can publish email sending events.

(structure)

Contains the name and value of a tag that you apply to an email. You can use message tags when you publish email sending events.

Name -> (string)

The name of the message tag. The message tag name has to meet the following criteria:

- It can only contain ASCII letters (aâz, AâZ), numbers (0â9), underscores (_), or dashes (-).
- It can contain no more than 256 characters.

Value -> (string)

The value of the message tag. The message tag value has to meet the following criteria:

- It can only contain ASCII letters (aâz, AâZ), numbers (0â9), underscores (_), or dashes (-).
- It can contain no more than 256 characters.

ReplacementEmailContent -> (structure)

The `ReplacementEmailContent` associated with a `BulkEmailEntry` .

ReplacementTemplate -> (structure)

The `ReplacementTemplate` associated with `ReplacementEmailContent` .

ReplacementTemplateData -> (string)

A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

ReplacementHeaders -> (list)

The list of message headers associated with the `BulkEmailEntry` data type.

- Headers Not Present in `BulkEmailEntry` : If a header is specified in ` `Template` [https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template).html`__ but not in `BulkEmailEntry` , the header from `Template` will be added to the outgoing email.
- Headers Present in `BulkEmailEntry` : If a header is specified in `BulkEmailEntry` , it takes precedence over any header of the same name specified in ` `Template` [https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template](https://docs.aws.amazon.com/ses/latest/APIReference-V2/API_Template).html`__ :
- If the header is also defined within `Template` , the value from `BulkEmailEntry` will replace the headerâs value in the email.
- If the header is not defined within `Template` , it will simply be added to the email as specified in `BulkEmailEntry` .

(structure)

Contains the name and value of a message header that you add to an email.

Name -> (string)

The name of the message header. The message header name has to meet the following criteria:

- Can contain any printable ASCII character (33 - 126) except for colon (:).
- Can contain no more than 126 characters.

Value -> (string)

The value of the message header. The message header value has to meet the following criteria:

- Can contain any printable ASCII character.
- Can contain no more than 870 characters.

Shorthand Syntax:

```
Destination={ToAddresses=[string,string],CcAddresses=[string,string],BccAddresses=[string,string]},ReplacementTags=[{Name=string,Value=string},{Name=string,Value=string}],ReplacementEmailContent={ReplacementTemplate={ReplacementTemplateData=string}},ReplacementHeaders=[{Name=string,Value=string},{Name=string,Value=string}] ...
```

JSON Syntax:

```
[
  {
    "Destination": {
      "ToAddresses": ["string", ...],
      "CcAddresses": ["string", ...],
      "BccAddresses": ["string", ...]
    },
    "ReplacementTags": [
      {
        "Name": "string",
        "Value": "string"
      }
      ...
    ],
    "ReplacementEmailContent": {
      "ReplacementTemplate": {
        "ReplacementTemplateData": "string"
      }
    },
    "ReplacementHeaders": [
      {
        "Name": "string",
        "Value": "string"
      }
      ...
    ]
  }
  ...
]
```

`--configuration-set-name` (string)

The name of the configuration set to use when sending the email.

`--endpoint-id` (string)

The ID of the multi-region endpoint (global-endpoint).

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

BulkEmailEntryResults -> (list)

One object per intended recipient. Check each response object and retry any messages with a failure status.

(structure)

The result of the `SendBulkEmail` operation of each specified `BulkEmailEntry` .

Status -> (string)

The status of a message sent using the `SendBulkTemplatedEmail` operation.

Possible values for this parameter include:

- SUCCESS: Amazon SES accepted the message, and will attempt to deliver it to the recipients.
- MESSAGE_REJECTED: The message was rejected because it contained a virus.
- MAIL_FROM_DOMAIN_NOT_VERIFIED: The senderâs email address or domain was not verified.
- CONFIGURATION_SET_DOES_NOT_EXIST: The configuration set you specified does not exist.
- TEMPLATE_DOES_NOT_EXIST: The template you specified does not exist.
- ACCOUNT_SUSPENDED: Your account has been shut down because of issues related to your email sending practices.
- ACCOUNT_THROTTLED: The number of emails you can send has been reduced because your account has exceeded its allocated sending limit.
- ACCOUNT_DAILY_QUOTA_EXCEEDED: You have reached or exceeded the maximum number of emails you can send from your account in a 24-hour period.
- INVALID_SENDING_POOL_NAME: The configuration set you specified refers to an IP pool that does not exist.
- ACCOUNT_SENDING_PAUSED: Email sending for the Amazon SES account was disabled using the [UpdateAccountSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateAccountSendingEnabled.html) operation.
- CONFIGURATION_SET_SENDING_PAUSED: Email sending for this configuration set was disabled using the [UpdateConfigurationSetSendingEnabled](https://docs.aws.amazon.com/ses/latest/APIReference/API_UpdateConfigurationSetSendingEnabled.html) operation.
- INVALID_PARAMETER_VALUE: One or more of the parameters you specified when calling this operation was invalid. See the error message for additional information.
- TRANSIENT_FAILURE: Amazon SES was unable to process your request because of a temporary issue.
- FAILED: Amazon SES was unable to process your request. See the error message for additional information.

Error -> (string)

A description of an error that prevented a message being sent using the `SendBulkTemplatedEmail` operation.

MessageId -> (string)

The unique message identifier returned from the `SendBulkTemplatedEmail` operation.