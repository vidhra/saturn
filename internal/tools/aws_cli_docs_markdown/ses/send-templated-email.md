# send-templated-emailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-templated-email.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-templated-email.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html#cli-aws-ses) ]

# send-templated-email

## Description

Composes an email message using an email template and immediately queues it for sending.

To send email using this operation, your call must meet the following requirements:

- The call must refer to an existing email template. You can create email templates using the  CreateTemplate operation.
- The message must be sent from a verified email address or domain.
- If your account is still in the Amazon SES sandbox, you may only send to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see [Verifying Email Addresses and Domains](https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html) in the *Amazon SES Developer Guide.*
- The maximum message size is 10 MB.
- Calls to the `SendTemplatedEmail` operation may only include one `Destination` parameter. A destination is a set of recipients that receives the same version of the email. The `Destination` parameter can include up to 50 recipients, across the To:, CC: and BCC: fields.
- The `Destination` parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format *UserName@[SubDomain.]Domain.TopLevelDomain* ), the entire message is rejected, even if the message contains other recipients that are valid.

### Warning

If your call to the `SendTemplatedEmail` operation includes all of the required parameters, Amazon SES accepts it and returns a Message ID. However, if Amazon SES canât render the email because the template contains errors, it doesnât send the email. Additionally, because it already accepted the message, Amazon SES doesnât return a message stating that it was unable to send the email.

For these reasons, we highly recommend that you set up Amazon SES to send you notifications when Rendering Failure events occur. For more information, see [Sending Personalized Email Using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-personalized-email-api.html) in the *Amazon Simple Email Service Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendTemplatedEmail)

## Synopsis

```
send-templated-email
--source <value>
--destination <value>
[--reply-to-addresses <value>]
[--return-path <value>]
[--source-arn <value>]
[--return-path-arn <value>]
[--tags <value>]
[--configuration-set-name <value>]
--template <value>
[--template-arn <value>]
--template-data <value>
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

The email address that is sending the email. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES. For information about verifying identities, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/creating-identities.html) .

If you are sending on behalf of another user and have been permitted to do so by a sending authorization policy, then you must also specify the `SourceArn` parameter. For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) .

### Note

Amazon SES does not support the SMTPUTF8 extension, as described in [RFC6531](https://tools.ietf.org/html/rfc6531) . for this reason, The email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the âfriendly fromâ name. If you want to use Unicode characters in the âfriendly fromâ name, you must encode the âfriendly fromâ name using MIME encoded-word syntax, as described in [Sending raw email using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html) . For more information about Punycode, see [RFC 3492](http://tools.ietf.org/html/rfc3492) .

`--destination` (structure)

The destination for this email, composed of To:, CC:, and BCC: fields. A Destination can include up to 50 recipients across these three fields.

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

A list of tags, in the form of name/value pairs, to apply to an email that you send using `SendTemplatedEmail` . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.

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

The name of the configuration set to use when you send an email using `SendTemplatedEmail` .

`--template` (string)

The template to use when sending this email.

`--template-arn` (string)

The ARN of the template to use when sending this email.

`--template-data` (string)

A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

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

The unique message identifier returned from the `SendTemplatedEmail` action.