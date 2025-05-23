# send-emailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/send-email.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/send-email.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint-email](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/index.html#cli-aws-pinpoint-email) ]

# send-email

## Description

Sends an email message. You can use the Amazon Pinpoint Email API to send two types of messages:

- **Simple** â A standard email message. When you create this type of message, you specify the sender, the recipient, and the message body, and Amazon Pinpoint assembles the message for you.
- **Raw** â A raw, MIME-formatted email message. When you send this type of email, you have to specify all of the message headers, as well as the message body. You can use this message type to send messages that contain attachments. The message that you specify has to be a valid MIME message.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/SendEmail)

## Synopsis

```
send-email
[--from-email-address <value>]
--destination <value>
[--reply-to-addresses <value>]
[--feedback-forwarding-email-address <value>]
--content <value>
[--email-tags <value>]
[--configuration-set-name <value>]
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

The email address that you want to use as the âFromâ address for the email. The address that you specify has to be verified.

`--destination` (structure)

An object that contains the recipients of the email message.

ToAddresses -> (list)

An array that contains the email addresses of the âToâ recipients for the email.

(string)

CcAddresses -> (list)

An array that contains the email addresses of the âCCâ (carbon copy) recipients for the email.

(string)

BccAddresses -> (list)

An array that contains the email addresses of the âBCCâ (blind carbon copy) recipients for the email.

(string)

Shorthand Syntax:

```
ToAddresses=string,string,CcAddresses=string,string,BccAddresses=string,string
```

JSON Syntax:

```
{
  "ToAddresses": ["string", ...],
  "CcAddresses": ["string", ...],
  "BccAddresses": ["string", ...]
}
```

`--reply-to-addresses` (list)

The âReply-toâ email addresses for the message. When the recipient replies to the message, each Reply-to address receives the reply.

(string)

Syntax:

```
"string" "string" ...
```

`--feedback-forwarding-email-address` (string)

The address that Amazon Pinpoint should send bounce and complaint notifications to.

`--content` (structure)

An object that contains the body of the message. You can send either a Simple message or a Raw message.

Simple -> (structure)

The simple email message. The message consists of a subject and a message body.

Subject -> (structure)

The subject line of the email. The subject line can only contain 7-bit ASCII characters. However, you can specify non-ASCII characters in the subject line by using encoded-word syntax, as described in [RFC 2047](https://tools.ietf.org/html/rfc2047) .

Data -> (string)

The content of the message itself.

Charset -> (string)

The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify `UTF-8` , `ISO-8859-1` , or `Shift_JIS` .

Body -> (structure)

The body of the message. You can specify an HTML version of the message, a text-only version of the message, or both.

Text -> (structure)

An object that represents the version of the message that is displayed in email clients that donât support HTML, or clients where the recipient has disabled HTML rendering.

Data -> (string)

The content of the message itself.

Charset -> (string)

The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify `UTF-8` , `ISO-8859-1` , or `Shift_JIS` .

Html -> (structure)

An object that represents the version of the message that is displayed in email clients that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.

Data -> (string)

The content of the message itself.

Charset -> (string)

The character set for the content. Because of the constraints of the SMTP protocol, Amazon Pinpoint uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify `UTF-8` , `ISO-8859-1` , or `Shift_JIS` .

Raw -> (structure)

The raw email message. The message has to meet the following criteria:

- The message has to contain a header and a body, separated by one blank line.
- All of the required header fields must be present in the message.
- Each part of a multipart MIME message must be formatted properly.
- If you include attachments, they must be in a file format that Amazon Pinpoint supports.
- The entire message must be Base64 encoded.
- If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipientsâ email clients render the message properly.
- The length of any single line of text in the message canât exceed 1,000 characters. This restriction is defined in [RFC 5321](https://tools.ietf.org/html/rfc5321) .

Data -> (blob)

The raw email message. The message has to meet the following criteria:

- The message has to contain a header and a body, separated by one blank line.
- All of the required header fields must be present in the message.
- Each part of a multipart MIME message must be formatted properly.
- Attachments must be in a file format that Amazon Pinpoint supports.
- The entire message must be Base64 encoded.
- If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipientsâ email clients render the message properly.
- The length of any single line of text in the message canât exceed 1,000 characters. This restriction is defined in [RFC 5321](https://tools.ietf.org/html/rfc5321) .

Template -> (structure)

The template to use for the email message.

TemplateArn -> (string)

The Amazon Resource Name (ARN) of the template.

TemplateData -> (string)

An object that defines the values to use for message variables in the template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the value to use for that variable.

JSON Syntax:

```
{
  "Simple": {
    "Subject": {
      "Data": "string",
      "Charset": "string"
    },
    "Body": {
      "Text": {
        "Data": "string",
        "Charset": "string"
      },
      "Html": {
        "Data": "string",
        "Charset": "string"
      }
    }
  },
  "Raw": {
    "Data": blob
  },
  "Template": {
    "TemplateArn": "string",
    "TemplateData": "string"
  }
}
```

`--email-tags` (list)

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

`--configuration-set-name` (string)

The name of the configuration set that you want to use when sending the email.

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

A unique identifier for the message that is generated when Amazon Pinpoint accepts the message.

### Note

It is possible for Amazon Pinpoint to accept a message without sending it. This can happen when the message youâre trying to send has an attachment doesnât pass a virus check, or when you send a templated email that contains invalid personalization content, for example.