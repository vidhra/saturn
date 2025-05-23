# send-emailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-email.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-email.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html#cli-aws-ses) ]

# send-email

## Description

Composes an email message and immediately queues it for sending. To send email using this operation, your message must meet the following requirements:

- The message must be sent from a verified email address or domain. If you attempt to send email using a non-verified address or domain, the operation results in an âEmail address not verifiedâ error.
- If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see [Verifying Email Addresses and Domains](https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html) in the *Amazon SES Developer Guide.*
- The maximum message size is 10 MB.
- The message must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format *UserName@[SubDomain.]Domain.TopLevelDomain* ), the entire message is rejected, even if the message contains other recipients that are valid.
- The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the `SendEmail` operation several times to send the message to each group.

### Warning

For every message that you send, the total number of recipients (including each recipient in the To:, CC: and BCC: fields) is counted against the maximum number of emails you can send in a 24-hour period (your *sending quota* ). For more information about sending quotas in Amazon SES, see [Managing Your Amazon SES Sending Limits](https://docs.aws.amazon.com/ses/latest/dg/manage-sending-quotas.html) in the *Amazon SES Developer Guide.*

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendEmail)

## Synopsis

```
send-email
[--destination <value>]
[--message <value>]
[--reply-to-addresses <value>]
[--return-path <value>]
[--source-arn <value>]
[--return-path-arn <value>]
[--tags <value>]
[--configuration-set-name <value>]
--from <value>
[--to <value>]
[--cc <value>]
[--bcc <value>]
[--subject <value>]
[--text <value>]
[--html <value>]
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

`--destination` (structure)

The destination for this email, composed of To:, CC:, and BCC: fields.

ToAddresses -> (list)

The recipients to place on the To: line of the message.

(string)

CcAddresses -> (list)

The recipients to place on the CC: line of the message.

(string)

BccAddresses -> (list)

The recipients to place on the BCC: line of the message.

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

`--message` (structure)

The message to be sent.

Subject -> (structure)

The subject of the message: A short summary of the content, which appears in the recipientâs inbox.

Data -> (string)

The textual data of the content.

Charset -> (string)

The character set of the content.

Body -> (structure)

The message body.

Text -> (structure)

The content of the message, in text format. Use this for text-based email clients, or clients on high-latency networks (such as mobile devices).

Data -> (string)

The textual data of the content.

Charset -> (string)

The character set of the content.

Html -> (structure)

The content of the message, in HTML format. Use this for email clients that can process HTML. You can include clickable links, formatted text, and much more in an HTML message.

Data -> (string)

The textual data of the content.

Charset -> (string)

The character set of the content.

Shorthand Syntax:

```
Subject={Data=string,Charset=string},Body={Text={Data=string,Charset=string},Html={Data=string,Charset=string}}
```

JSON Syntax:

```
{
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
}
```

`--reply-to-addresses` (list)

The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address receives the reply.

(string)

Syntax:

```
"string" "string" ...
```

`--return-path` (string)

The email address that bounces and complaints are forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message is returned from the recipientâs ISP; this message is forwarded to the email address specified by the `ReturnPath` parameter. The `ReturnPath` parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

`--source-arn` (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the `Source` parameter.

For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-east-1:123456789012:identity/example.com` ) attaches a policy to it that authorizes you to send from `user@example.com` , then you would specify the `SourceArn` to be `arn:aws:ses:us-east-1:123456789012:identity/example.com` , and the `Source` to be `user@example.com` .

For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) .

`--return-path-arn` (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the `ReturnPath` parameter.

For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-east-1:123456789012:identity/example.com` ) attaches a policy to it that authorizes you to use `feedback@example.com` , then you would specify the `ReturnPathArn` to be `arn:aws:ses:us-east-1:123456789012:identity/example.com` , and the `ReturnPath` to be `feedback@example.com` .

For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) .

`--tags` (list)

A list of tags, in the form of name/value pairs, to apply to an email that you send using `SendEmail` . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.

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

The name of the configuration set to use when you send an email using `SendEmail` .

`--from` (string)

The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html) .

If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the `SourceArn` parameter. For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) .

### Note

Amazon SES does not support the SMTPUTF8 extension, as described in [RFC6531](https://tools.ietf.org/html/rfc6531) . For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the âfriendly fromâ name. If you want to use Unicode characters in the âfriendly fromâ name, you must encode the âfriendly fromâ name using MIME encoded-word syntax, as described in [Sending raw email using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html) . For more information about Punycode, see [RFC 3492](http://tools.ietf.org/html/rfc3492) .

`--to` (string)
The email addresses of the primary recipients. You can specify multiple recipients as space-separated values

`--cc` (string)
The email addresses of copy recipients (Cc). You can specify multiple recipients as space-separated values

`--bcc` (string)
The email addresses of blind-carbon-copy recipients (Bcc). You can specify multiple recipients as space-separated values

`--subject` (string)
The subject of the message

`--text` (string)
The raw text body of the message

`--html` (string)
The HTML body of the message

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

**To send a formatted email using Amazon SES**

The following example uses the `send-email` command to send a formatted email:

```
aws ses send-email --from sender@example.com --destination file://destination.json --message file://message.json
```

Output:

```
{
   "MessageId": "EXAMPLEf3a5efcd1-51adec81-d2a4-4e3f-9fe2-5d85c1b23783-000000"
}
```

The destination and the message are JSON data structures saved in .json files in the current directory. These files are as follows:

`destination.json`:

```
{
  "ToAddresses":  ["recipient1@example.com", "recipient2@example.com"],
  "CcAddresses":  ["recipient3@example.com"],
  "BccAddresses": []
}
```

`message.json`:

```
{
   "Subject": {
       "Data": "Test email sent using the AWS CLI",
       "Charset": "UTF-8"
   },
   "Body": {
       "Text": {
           "Data": "This is the message body in text format.",
           "Charset": "UTF-8"
       },
       "Html": {
           "Data": "This message body contains HTML formatting. It can, for example, contain links like this one: <a class=\"ulink\" href=\"http://docs.aws.amazon.com/ses/latest/DeveloperGuide\" target=\"_blank\">Amazon SES Developer Guide</a>.",
           "Charset": "UTF-8"
       }
   }
}
```

Replace the sender and recipient email addresses with the ones you want to use. Note that the senderâs email address must be verified with Amazon SES. Until you are granted production access to Amazon SES, you must also verify the email address of each recipient
unless the recipient is the Amazon SES mailbox simulator. For more information on verification, see [Verifying Email Addresses and Domains in Amazon SES](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-addresses-and-domains.html) in the *Amazon Simple Email Service Developer Guide*.

The Message ID in the output indicates that the call to send-email was successful.

If you donât receive the email, check your Junk box.

For more information on sending formatted email, see [Sending Formatted Email Using the Amazon SES API](http://docs.aws.amazon.com/ses/latest/DeveloperGuide/send-email-formatted.html) in the *Amazon Simple Email Service Developer Guide*.

## Output

MessageId -> (string)

The unique message identifier returned from the `SendEmail` action.