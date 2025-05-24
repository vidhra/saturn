# send-bulk-templated-emailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-bulk-templated-email.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/send-bulk-templated-email.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html#cli-aws-ses) ]

# send-bulk-templated-email

## Description

Composes an email message to multiple destinations. The message body is created using an email template.

To send email using this operation, your call must meet the following requirements:

- The call must refer to an existing email template. You can create email templates using  CreateTemplate .
- The message must be sent from a verified email address or domain.
- If your account is still in the Amazon SES sandbox, you may send only to verified addresses or domains, or to email addresses associated with the Amazon SES Mailbox Simulator. For more information, see [Verifying Email Addresses and Domains](https://docs.aws.amazon.com/ses/latest/dg/verify-addresses-and-domains.html) in the *Amazon SES Developer Guide.*
- The maximum message size is 10 MB.
- Each `Destination` parameter must include at least one recipient email address. The recipient address can be a To: address, a CC: address, or a BCC: address. If a recipient email address is invalid (that is, it is not in the format *UserName@[SubDomain.]Domain.TopLevelDomain* ), the entire message is rejected, even if the message contains other recipients that are valid.
- The message may not include more than 50 recipients, across the To:, CC: and BCC: fields. If you need to send an email message to a larger audience, you can divide your recipient list into groups of 50 or fewer, and then call the `SendBulkTemplatedEmail` operation several times to send the message to each group.
- The number of destinations you can contact in a single call can be limited by your accountâs maximum sending rate.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/SendBulkTemplatedEmail)

## Synopsis

```
send-bulk-templated-email
--source <value>
[--source-arn <value>]
[--reply-to-addresses <value>]
[--return-path <value>]
[--return-path-arn <value>]
[--configuration-set-name <value>]
[--default-tags <value>]
--template <value>
[--template-arn <value>]
--default-template-data <value>
--destinations <value>
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

Amazon SES does not support the SMTPUTF8 extension, as described in [RFC6531](https://tools.ietf.org/html/rfc6531) . For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the âfriendly fromâ name. If you want to use Unicode characters in the âfriendly fromâ name, you must encode the âfriendly fromâ name using MIME encoded-word syntax, as described in [Sending raw email using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html) . For more information about Punycode, see [RFC 3492](http://tools.ietf.org/html/rfc3492) .

`--source-arn` (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to send for the email address specified in the `Source` parameter.

For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-east-1:123456789012:identity/example.com` ) attaches a policy to it that authorizes you to send from `user@example.com` , then you would specify the `SourceArn` to be `arn:aws:ses:us-east-1:123456789012:identity/example.com` , and the `Source` to be `user@example.com` .

For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) .

`--reply-to-addresses` (list)

The reply-to email address(es) for the message. If the recipient replies to the message, each reply-to address receives the reply.

(string)

Syntax:

```
"string" "string" ...
```

`--return-path` (string)

The email address that bounces and complaints are forwarded to when feedback forwarding is enabled. If the message cannot be delivered to the recipient, then an error message is returned from the recipientâs ISP; this message is forwarded to the email address specified by the `ReturnPath` parameter. The `ReturnPath` parameter is never overwritten. This email address must be either individually verified with Amazon SES, or from a domain that has been verified with Amazon SES.

`--return-path-arn` (string)

This parameter is used only for sending authorization. It is the ARN of the identity that is associated with the sending authorization policy that permits you to use the email address specified in the `ReturnPath` parameter.

For example, if the owner of `example.com` (which has ARN `arn:aws:ses:us-east-1:123456789012:identity/example.com` ) attaches a policy to it that authorizes you to use `feedback@example.com` , then you would specify the `ReturnPathArn` to be `arn:aws:ses:us-east-1:123456789012:identity/example.com` , and the `ReturnPath` to be `feedback@example.com` .

For more information about sending authorization, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/sending-authorization.html) .

`--configuration-set-name` (string)

The name of the configuration set to use when you send an email using `SendBulkTemplatedEmail` .

`--default-tags` (list)

A list of tags, in the form of name/value pairs, to apply to an email that you send to a destination using `SendBulkTemplatedEmail` .

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

`--template` (string)

The template to use when sending this email.

`--template-arn` (string)

The ARN of the template to use when sending this email.

`--default-template-data` (string)

A list of replacement values to apply to the template when replacement data is not specified in a Destination object. These values act as a default or fallback option when no other data is available.

The template data is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

`--destinations` (list)

One or more `Destination` objects. All of the recipients in a `Destination` receive the same version of the email. You can specify up to 50 `Destination` objects within a `Destinations` array.

(structure)

An array that contains one or more Destinations, as well as the tags and replacement data associated with each of those Destinations.

Destination -> (structure)

Represents the destination of the message, consisting of To:, CC:, and BCC: fields.

### Note

Amazon SES does not support the SMTPUTF8 extension, as described in [RFC6531](https://tools.ietf.org/html/rfc6531) . For this reason, the email address string must be 7-bit ASCII. If you want to send to or from email addresses that contain Unicode characters in the domain part of an address, you must encode the domain using Punycode. Punycode is not permitted in the local part of the email address (the part before the @ sign) nor in the âfriendly fromâ name. If you want to use Unicode characters in the âfriendly fromâ name, you must encode the âfriendly fromâ name using MIME encoded-word syntax, as described in [Sending raw email using the Amazon SES API](https://docs.aws.amazon.com/ses/latest/dg/send-email-raw.html) . For more information about Punycode, see [RFC 3492](http://tools.ietf.org/html/rfc3492) .

ToAddresses -> (list)

The recipients to place on the To: line of the message.

(string)

CcAddresses -> (list)

The recipients to place on the CC: line of the message.

(string)

BccAddresses -> (list)

The recipients to place on the BCC: line of the message.

(string)

ReplacementTags -> (list)

A list of tags, in the form of name/value pairs, to apply to an email that you send using `SendBulkTemplatedEmail` . Tags correspond to characteristics of the email that you define, so that you can publish email sending events.

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

ReplacementTemplateData -> (string)

A list of replacement values to apply to the template. This parameter is a JSON object, typically consisting of key-value pairs in which the keys correspond to replacement tags in the email template.

Shorthand Syntax:

```
Destination={ToAddresses=[string,string],CcAddresses=[string,string],BccAddresses=[string,string]},ReplacementTags=[{Name=string,Value=string},{Name=string,Value=string}],ReplacementTemplateData=string ...
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
    "ReplacementTemplateData": "string"
  }
  ...
]
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

Status -> (list)

One object per intended recipient. Check each response object and retry any messages with a failure status. (Note that order of responses will be respective to order of destinations in the request.)Receipt rules enable you to specify which actions

(structure)

An object that contains the response from the `SendBulkTemplatedEmail` operation.

Status -> (string)

The status of a message sent using the `SendBulkTemplatedEmail` operation.

Possible values for this parameter include:

- `Success` : Amazon SES accepted the message, and attempts to deliver it to the recipients.
- `MessageRejected` : The message was rejected because it contained a virus.
- `MailFromDomainNotVerified` : The senderâs email address or domain was not verified.
- `ConfigurationSetDoesNotExist` : The configuration set you specified does not exist.
- `TemplateDoesNotExist` : The template you specified does not exist.
- `AccountSuspended` : Your account has been shut down because of issues related to your email sending practices.
- `AccountThrottled` : The number of emails you can send has been reduced because your account has exceeded its allocated sending limit.
- `AccountDailyQuotaExceeded` : You have reached or exceeded the maximum number of emails you can send from your account in a 24-hour period.
- `InvalidSendingPoolName` : The configuration set you specified refers to an IP pool that does not exist.
- `AccountSendingPaused` : Email sending for the Amazon SES account was disabled using the  UpdateAccountSendingEnabled operation.
- `ConfigurationSetSendingPaused` : Email sending for this configuration set was disabled using the  UpdateConfigurationSetSendingEnabled operation.
- `InvalidParameterValue` : One or more of the parameters you specified when calling this operation was invalid. See the error message for additional information.
- `TransientFailure` : Amazon SES was unable to process your request because of a temporary issue.
- `Failed` : Amazon SES was unable to process your request. See the error message for additional information.

Error -> (string)

A description of an error that prevented a message being sent using the `SendBulkTemplatedEmail` operation.

MessageId -> (string)

The unique message identifier returned from the `SendBulkTemplatedEmail` operation.