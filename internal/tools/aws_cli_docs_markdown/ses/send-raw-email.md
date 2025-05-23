# send-raw-emailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-raw-email.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-raw-email.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html#cli-aws-ses) ]

# send-raw-email

## Description

Composes an email message and immediately queues it for sending.

This operation is more flexible than the `SendEmail` operation. When you use the `SendRawEmail` operation, you can specify the headers of the message as well as its content. This flexibility is useful, for example, when you need to send a multipart MIME email (such a message that contains both a text and an HTML version). You can also use this operation to send messages that include attachments.

The `SendRawEmail` operation has the following requirements:

- You can only send email from [verified email addresses or domains](https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html) . If you try to send email from an address that isnât verified, the operation results in an âEmail address not verifiedâ error.
- If your account is still in the [Amazon SES sandbox](https://docs.aws.amazon.com/ses/latest/dg/request-production-access.html) , you can only send email to other verified addresses in your account, or to addresses that are associated with the [Amazon SES mailbox simulator](https://docs.aws.amazon.com/ses/latest/dg/send-an-email-from-console.html) .
- The maximum message size, including attachments, is 10 MB.
- Each message has to include at least one recipient address. A recipient address includes any address on the To:, CC:, or BCC: lines.
- If you send a single message to more than one recipient address, and one of the recipient addresses isnât in a valid format (that is, itâs not in the format *UserName@[SubDomain.]Domain.TopLevelDomain* ), Amazon SES rejects the entire message, even if the other addresses are valid.
- Each message can include up to 50 recipient addresses across the To:, CC:, or BCC: lines. If you need to send a single message to more than 50 recipients, you have to split the list of recipient addresses into groups of less than 50 recipients, and send separate messages to each group.
- Amazon SES allows you to specify 8-bit Content-Transfer-Encoding for MIME message parts. However, if Amazon SES has to modify the contents of your message (for example, if you use open and click tracking), 8-bit content isnât preserved. For this reason, we highly recommend that you encode all content that isnât 7-bit ASCII. For more information, see [MIME Encoding](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html#send-email-mime-encoding) in the *Amazon SES Developer Guide* .

Additionally, keep the following considerations in mind when using the `SendRawEmail` operation:

- Although you can customize the message headers when using the `SendRawEmail` operation, Amazon SES automatically applies its own `Message-ID` and `Date` headers; if you passed these headers when creating the message, they are overwritten by the values that Amazon SES provides.
- If you are using sending authorization to send on behalf of another user, `SendRawEmail` enables you to specify the cross-account identity for the emailâs Source, From, and Return-Path parameters in one of two ways: you can pass optional parameters `SourceArn` , `FromArn` , and/or `ReturnPathArn` , or you can include the following X-headers in the header of your raw email:
- `X-SES-SOURCE-ARN`
- `X-SES-FROM-ARN`
- `X-SES-RETURN-PATH-ARN`

### Warning

Donât include these X-headers in the DKIM signature. Amazon SES removes these before it sends the email.

If you only specify the `SourceIdentityArn` parameter, Amazon SES sets the From and Return-Path addresses to the same identity that you specified.

For more information about sending authorization, see the [Using Sending Authorization with Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) in the *Amazon SES Developer Guide.*

- For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your *sending quota* ). For more information about sending quotas in Amazon SES, see [Managing Your Amazon SES Sending Limits](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html) in the *Amazon SES Developer Guide.*

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendRawEmail)

## Synopsis

```
send-raw-email
[--source <value>]
[--destinations <value>]
--raw-message <value>
[--from-arn <value>]
[--source-arn <value>]
[--return-path-arn <value>]
[--tags <value>]
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

`--source` (string)

The identityâs email address. If you do not provide a value for this parameter, you must specify a âFromâ address in the raw text of the message. (You can also specify both.)

### Note

Amazon SES does not support the SMTPUTF8 extension, as described in`RFC6531 <[https://tools.ietf.org/html/rfc6531](https://tools.ietf.org/html/rfc6531)>`__ . For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the âfriendly fromâ name. If you want to use Unicode characters in the âfriendly fromâ name, you must encode the âfriendly fromâ name using MIME encoded-word syntax, as described in [Sending raw email using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html) . For more information about Punycode, see [RFC 3492](http://tools.ietf.org/html/rfc3492) .

If you specify the `Source` parameter and have feedback forwarding enabled, then bounces and complaints are sent to this email address. This takes precedence over any Return-Path header that you might include in the raw text of the message.

`--destinations` (list)

A list of destinations for the message, consisting of To:, CC:, and BCC: addresses.

(string)

Syntax:

```
"string" "string" ...
```

`--raw-message` (structure)

The raw email message itself. The message has to meet the following criteria:

- The message has to contain a header and a body, separated by a blank line.
- All of the required header fields must be present in the message.
- Each part of a multipart MIME message must be formatted properly.
- Attachments must be of a content type that Amazon SES supports. For a list on unsupported content types, see [Unsupported Attachment Types](https://docs.aws.amazon.com/ses/latest/dg/mime-types.html) in the *Amazon SES Developer Guide* .
- The entire message must be base64-encoded.
- If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, we highly recommend that you encode that content. For more information, see [Sending Raw Email](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html) in the *Amazon SES Developer Guide* .
- Per [RFC 5321](https://tools.ietf.org/html/rfc5321#section-4.5.3.1.6) , the maximum length of each line of text, including the <CRLF>, must not exceed 1,000 characters.

Data -> (blob)

The raw data of the message. This data needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an Amazon Web Services SDK, the SDK takes care of the base 64-encoding for you. In all cases, the client must ensure that the message format complies with Internet email standards regarding email header fields, MIME types, and MIME encoding.

The To:, CC:, and BCC: headers in the raw message can contain a group list.

If you are using `SendRawEmail` with sending authorization, you can include X-headers in the raw message to specify the âSource,â âFrom,â and âReturn-Pathâ addresses. For more information, see the documentation for `SendRawEmail` .

### Warning

Do not include these X-headers in the DKIM signature, because they are removed by Amazon SES before sending the email.

For more information, go to the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html) .

Shorthand Syntax:

```
Data=blob
```

JSON Syntax:

```
{
  "Data": blob
}
```

`--from-arn` (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to specify a particular âFromâ address in the header of the raw email.

Instead of using this parameter, you can use the X-header `X-SES-FROM-ARN` in the raw message of the email. If you use both the `FromArn` parameter and the corresponding X-header, Amazon SES uses the value of the `FromArn` parameter.

### Note

For information about when to use this parameter, see the description of `SendRawEmail` in this guide, or see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html) .

`--source-arn` (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the `Source` parameter.

For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-east-1:123456789012:identity/example.com` ) attaches a policy to it that authorizes you to send from `user@example.com` , then you would specify the `SourceArn` to be `arn:aws:ses:us-east-1:123456789012:identity/example.com` , and the `Source` to be `user@example.com` .

Instead of using this parameter, you can use the X-header `X-SES-SOURCE-ARN` in the raw message of the email. If you use both the `SourceArn` parameter and the corresponding X-header, Amazon SES uses the value of the `SourceArn` parameter.

### Note

For information about when to use this parameter, see the description of `SendRawEmail` in this guide, or see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html) .

`--return-path-arn` (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the `ReturnPath` parameter.

For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-east-1:123456789012:identity/example.com` ) attaches a policy to it that authorizes you to use `feedback@example.com` , then you would specify the `ReturnPathArn` to be `arn:aws:ses:us-east-1:123456789012:identity/example.com` , and the `ReturnPath` to be `feedback@example.com` .

Instead of using this parameter, you can use the X-header `X-SES-RETURN-PATH-ARN` in the raw message of the email. If you use both the `ReturnPathArn` parameter and the corresponding X-header, Amazon SES uses the value of the `ReturnPathArn` parameter.

### Note

For information about when to use this parameter, see the description of `SendRawEmail` in this guide, or see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization-delegate-sender-tasks-email.html) .

`--tags` (list)

A list of tags, in the form of name/value pairs, to apply to an email that you send using `SendRawEmail` . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.

(structure)

Contains the name and value of a tag that you can provide to `SendEmail` or `SendRawEmail` to apply to an email.

Message tags, which you use with configuration sets, enable you to publish email sending events. For information about using configuration sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-activity.html) .

Name -> (string)

The name of the tag. The name must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
- Contain 256 characters or fewer.

Value -> (string)

The value of the tag. The value must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
- Contain 256 characters or fewer.

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

The name of the configuration set to use when you send an email using `SendRawEmail` .

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To send a raw email using Amazon SES**

The following example uses the `send-raw-email` command to send an email with a TXT attachment:

```
aws ses send-raw-email \
--cli-binary-format raw-in-base64-out \
--raw-message file://message.json
```

Output:

```
{
   "MessageId": "EXAMPLEf3f73d99b-c63fb06f-d263-41f8-a0fb-d0dc67d56c07-000000"
}
```

The raw message is a JSON data structure saved in a file named `message.json` in the current directory. It contains the following:

```
{
   "Data": "From: sender@example.com\nTo: recipient@example.com\nSubject: Test email sent using the AWS CLI (contains an attachment)\nMIME-Version: 1.0\nContent-type: Multipart/Mixed; boundary=\"NextPart\"\n\n--NextPart\nContent-Type: text/plain\n\nThis is the message body.\n\n--NextPart\nContent-Type: text/plain;\nContent-Disposition: attachment; filename=\"attachment.txt\"\n\nThis is the text in the attachment.\n\n--NextPart--"
}
```

As you can see, âDataâ is one long string that contains the entire raw email content in MIME format, including an attachment called attachment.txt.

Replace [sender@example.com](mailto:sender%40example.com) and [recipient@example.com](mailto:recipient%40example.com) with the addresses you want to use. Note that the senderâs email address must be verified with Amazon SES. Until you are granted production access to Amazon SES, you must also verify the email address of the recipient
unless the recipient is the Amazon SES mailbox simulator. For more information on verification, see [Verifying Email Addresses and Domains in Amazon SES](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html) in the *Amazon Simple Email Service Developer Guide*.

The Message ID in the output indicates that the call to send-raw-email was successful.

If you donât receive the email, check your Junk box.

For more information on sending raw email, see [Sending Raw Email Using the Amazon SES API](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-raw.html) in the *Amazon Simple Email Service Developer Guide*.

## Output

MessageId -> (string)

The unique message identifier returned from the `SendRawEmail` action.