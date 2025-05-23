# get-configuration-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-configuration-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-configuration-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# get-configuration-set

## Description

Get information about an existing configuration set, including the dedicated IP pool that itâs associated with, whether or not itâs enabled for sending email, and more.

*Configuration sets* are groups of rules that you can apply to the emails you send. You apply a configuration set to an email by including a reference to the configuration set in the headers of the email. When you apply a configuration set to an email, all of the rules in that configuration set are applied to the email.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/GetConfigurationSet)

## Synopsis

```
get-configuration-set
--configuration-set-name <value>
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

`--configuration-set-name` (string)

The name of the configuration set.

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

ConfigurationSetName -> (string)

The name of the configuration set.

TrackingOptions -> (structure)

An object that defines the open and click tracking options for emails that you send using the configuration set.

CustomRedirectDomain -> (string)

The domain to use for tracking open and click events.

HttpsPolicy -> (string)

The https policy to use for tracking open and click events.

DeliveryOptions -> (structure)

An object that defines the dedicated IP pool that is used to send emails that you send using the configuration set.

TlsPolicy -> (string)

Specifies whether messages that use the configuration set are required to use Transport Layer Security (TLS). If the value is `Require` , messages are only delivered if a TLS connection can be established. If the value is `Optional` , messages can be delivered in plain text if a TLS connection canât be established.

SendingPoolName -> (string)

The name of the dedicated IP pool to associate with the configuration set.

MaxDeliverySeconds -> (long)

The maximum amount of time, in seconds, that Amazon SES API v2 will attempt delivery of email. If specified, the value must greater than or equal to 300 seconds (5 minutes) and less than or equal to 50400 seconds (840 minutes).

ReputationOptions -> (structure)

An object that defines whether or not Amazon SES collects reputation metrics for the emails that you send that use the configuration set.

ReputationMetricsEnabled -> (boolean)

If `true` , tracking of reputation metrics is enabled for the configuration set. If `false` , tracking of reputation metrics is disabled for the configuration set.

LastFreshStart -> (timestamp)

The date and time (in Unix time) when the reputation metrics were last given a fresh start. When your account is given a fresh start, your reputation metrics are calculated starting from the date of the fresh start.

SendingOptions -> (structure)

An object that defines whether or not Amazon SES can send email that you send using the configuration set.

SendingEnabled -> (boolean)

If `true` , email sending is enabled for the configuration set. If `false` , email sending is disabled for the configuration set.

Tags -> (list)

An array of objects that define the tags (keys and values) that are associated with the configuration set.

(structure)

An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.

Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:

- Tag keys and values are case sensitive.
- For each associated resource, each tag key must be unique and it can have only one value.
- The `aws:` prefix is reserved for use by Amazon Web Services; you canât use it in any tag keys or values that you define. In addition, you canât edit or remove tag keys or values that use this prefix. Tags that use this prefix donât count against the limit of 50 tags per resource.
- You can associate tags with public or shared resources, but the tags are available only for your Amazon Web Services account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified Amazon Web Services Region for your Amazon Web Services account.

Key -> (string)

One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.

Value -> (string)

The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you donât want a resource to have a specific tag value, donât specify a value for this parameter. If you donât specify a value, Amazon SES sets the value to an empty string.

SuppressionOptions -> (structure)

An object that contains information about the suppression list preferences for your account.

SuppressedReasons -> (list)

A list that contains the reasons that email addresses are automatically added to the suppression list for your account. This list can contain any or all of the following:

- `COMPLAINT` â Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a complaint.
- `BOUNCE` â Amazon SES adds an email address to the suppression list for your account when a message sent to that address results in a hard bounce.

(string)

The reason that the address was added to the suppression list for your account. The value can be one of the following:

- `COMPLAINT` â Amazon SES added an email address to the suppression list for your account because a message sent to that address results in a complaint.
- `BOUNCE` â Amazon SES added an email address to the suppression list for your account because a message sent to that address results in a hard bounce.

VdmOptions -> (structure)

An object that contains information about the VDM preferences for your configuration set.

DashboardOptions -> (structure)

Specifies additional settings for your VDM configuration as applicable to the Dashboard.

EngagementMetrics -> (string)

Specifies the status of your VDM engagement metrics collection. Can be one of the following:

- `ENABLED` â Amazon SES enables engagement metrics for the configuration set.
- `DISABLED` â Amazon SES disables engagement metrics for the configuration set.

GuardianOptions -> (structure)

Specifies additional settings for your VDM configuration as applicable to the Guardian.

OptimizedSharedDelivery -> (string)

Specifies the status of your VDM optimized shared delivery. Can be one of the following:

- `ENABLED` â Amazon SES enables optimized shared delivery for the configuration set.
- `DISABLED` â Amazon SES disables optimized shared delivery for the configuration set.

ArchivingOptions -> (structure)

An object that defines the MailManager archive where sent emails are archived that you send using the configuration set.

ArchiveArn -> (string)

The Amazon Resource Name (ARN) of the MailManager archive where the Amazon SES API v2 will archive sent emails.