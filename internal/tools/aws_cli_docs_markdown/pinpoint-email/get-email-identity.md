# get-email-identityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-email-identity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-email-identity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint-email](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/index.html#cli-aws-pinpoint-email) ]

# get-email-identity

## Description

Provides information about a specific identity associated with your Amazon Pinpoint account, including the identityâs verification status, its DKIM authentication status, and its custom Mail-From settings.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetEmailIdentity)

## Synopsis

```
get-email-identity
--email-identity <value>
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

`--email-identity` (string)

The email identity that you want to retrieve details for.

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

IdentityType -> (string)

The email identity type.

FeedbackForwardingStatus -> (boolean)

The feedback forwarding configuration for the identity.

If the value is `true` , Amazon Pinpoint sends you email notifications when bounce or complaint events occur. Amazon Pinpoint sends this notification to the address that you specified in the Return-Path header of the original email.

When you set this value to `false` , Amazon Pinpoint sends notifications through other mechanisms, such as by notifying an Amazon SNS topic or another event destination. Youâre required to have a method of tracking bounces and complaints. If you havenât set up another mechanism for receiving bounce or complaint notifications, Amazon Pinpoint sends an email notification when these events occur (even if this setting is disabled).

VerifiedForSendingStatus -> (boolean)

Specifies whether or not the identity is verified. In Amazon Pinpoint, you can only send email from verified email addresses or domains. For more information about verifying identities, see the [Amazon Pinpoint User Guide](https://docs.aws.amazon.com/pinpoint/latest/userguide/channels-email-manage-verify.html) .

DkimAttributes -> (structure)

An object that contains information about the DKIM attributes for the identity. This object includes the tokens that you use to create the CNAME records that are required to complete the DKIM verification process.

SigningEnabled -> (boolean)

If the value is `true` , then the messages that Amazon Pinpoint sends from the identity are DKIM-signed. If the value is `false` , then the messages that Amazon Pinpoint sends from the identity arenât DKIM-signed.

Status -> (string)

Describes whether or not Amazon Pinpoint has successfully located the DKIM records in the DNS records for the domain. The status can be one of the following:

- `PENDING` â Amazon Pinpoint hasnât yet located the DKIM records in the DNS configuration for the domain, but will continue to attempt to locate them.
- `SUCCESS` â Amazon Pinpoint located the DKIM records in the DNS configuration for the domain and determined that theyâre correct. Amazon Pinpoint can now send DKIM-signed email from the identity.
- `FAILED` â Amazon Pinpoint was unable to locate the DKIM records in the DNS settings for the domain, and wonât continue to search for them.
- `TEMPORARY_FAILURE` â A temporary issue occurred, which prevented Amazon Pinpoint from determining the DKIM status for the domain.
- `NOT_STARTED` â Amazon Pinpoint hasnât yet started searching for the DKIM records in the DKIM records for the domain.

Tokens -> (list)

A set of unique strings that you use to create a set of CNAME records that you add to the DNS configuration for your domain. When Amazon Pinpoint detects these records in the DNS configuration for your domain, the DKIM authentication process is complete. Amazon Pinpoint usually detects these records within about 72 hours of adding them to the DNS configuration for your domain.

(string)

MailFromAttributes -> (structure)

An object that contains information about the Mail-From attributes for the email identity.

MailFromDomain -> (string)

The name of a domain that an email identity uses as a custom MAIL FROM domain.

MailFromDomainStatus -> (string)

The status of the MAIL FROM domain. This status can have the following values:

- `PENDING` â Amazon Pinpoint hasnât started searching for the MX record yet.
- `SUCCESS` â Amazon Pinpoint detected the required MX record for the MAIL FROM domain.
- `FAILED` â Amazon Pinpoint canât find the required MX record, or the record no longer exists.
- `TEMPORARY_FAILURE` â A temporary issue occurred, which prevented Amazon Pinpoint from determining the status of the MAIL FROM domain.

BehaviorOnMxFailure -> (string)

The action that Amazon Pinpoint to takes if it canât read the required MX record for a custom MAIL FROM domain. When you set this value to `UseDefaultValue` , Amazon Pinpoint uses *amazonses.com* as the MAIL FROM domain. When you set this value to `RejectMessage` , Amazon Pinpoint returns a `MailFromDomainNotVerified` error, and doesnât attempt to deliver the email.

These behaviors are taken when the custom MAIL FROM domain configuration is in the `Pending` , `Failed` , and `TemporaryFailure` states.

Tags -> (list)

An array of objects that define the tags (keys and values) that are associated with the email identity.

(structure)

An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource in Amazon Pinpoint. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.

Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:

- Tag keys and values are case sensitive.
- For each associated resource, each tag key must be unique and it can have only one value.
- The `aws:` prefix is reserved for use by AWS; you canât use it in any tag keys or values that you define. In addition, you canât edit or remove tag keys or values that use this prefix. Tags that use this prefix donât count against the limit of 50 tags per resource.
- You can associate tags with public or shared resources, but the tags are available only for your AWS account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified AWS Region for your AWS account.

Key -> (string)

One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.

Value -> (string)

The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you donât want a resource to have a specific tag value, donât specify a value for this parameter. Amazon Pinpoint will set the value to an empty string.