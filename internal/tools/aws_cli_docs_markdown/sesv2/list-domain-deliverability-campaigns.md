# list-domain-deliverability-campaignsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-domain-deliverability-campaigns.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/list-domain-deliverability-campaigns.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# list-domain-deliverability-campaigns

## Description

Retrieve deliverability data for all the campaigns that used a specific domain to send email during a specified time range. This data is available for a domain only if you enabled the Deliverability dashboard for the domain.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/ListDomainDeliverabilityCampaigns)

## Synopsis

```
list-domain-deliverability-campaigns
--start-date <value>
--end-date <value>
--subscribed-domain <value>
[--next-token <value>]
[--page-size <value>]
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

`--start-date` (timestamp)

The first day that you want to obtain deliverability data for.

`--end-date` (timestamp)

The last day that you want to obtain deliverability data for. This value has to be less than or equal to 30 days after the value of the `StartDate` parameter.

`--subscribed-domain` (string)

The domain to obtain deliverability data for.

`--next-token` (string)

A token thatâs returned from a previous call to the `ListDomainDeliverabilityCampaigns` operation. This token indicates the position of a campaign in the list of campaigns.

`--page-size` (integer)

The maximum number of results to include in response to a single call to the `ListDomainDeliverabilityCampaigns` operation. If the number of results is larger than the number that you specify in this parameter, the response includes a `NextToken` element, which you can use to obtain additional results.

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

DomainDeliverabilityCampaigns -> (list)

An array of responses, one for each campaign that used the domain to send email during the specified time range.

(structure)

An object that contains the deliverability data for a specific campaign. This data is available for a campaign only if the campaign sent email by using a domain that the Deliverability dashboard is enabled for (`PutDeliverabilityDashboardOption` operation).

CampaignId -> (string)

The unique identifier for the campaign. The Deliverability dashboard automatically generates and assigns this identifier to a campaign.

ImageUrl -> (string)

The URL of an image that contains a snapshot of the email message that was sent.

Subject -> (string)

The subject line, or title, of the email message.

FromAddress -> (string)

The verified email address that the email message was sent from.

SendingIps -> (list)

The IP addresses that were used to send the email message.

(string)

An IPv4 address.

FirstSeenDateTime -> (timestamp)

The first time when the email message was delivered to any recipientâs inbox. This value can help you determine how long it took for a campaign to deliver an email message.

LastSeenDateTime -> (timestamp)

The last time when the email message was delivered to any recipientâs inbox. This value can help you determine how long it took for a campaign to deliver an email message.

InboxCount -> (long)

The number of email messages that were delivered to recipientsâ inboxes.

SpamCount -> (long)

The number of email messages that were delivered to recipientsâ spam or junk mail folders.

ReadRate -> (double)

The percentage of email messages that were opened by recipients. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.

DeleteRate -> (double)

The percentage of email messages that were deleted by recipients, without being opened first. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.

ReadDeleteRate -> (double)

The percentage of email messages that were opened and then deleted by recipients. Due to technical limitations, this value only includes recipients who opened the message by using an email client that supports images.

ProjectedVolume -> (long)

The projected number of recipients that the email message was sent to.

Esps -> (list)

The major email providers who handled the email message.

(string)

NextToken -> (string)

A token thatâs returned from a previous call to the `ListDomainDeliverabilityCampaigns` operation. This token indicates the position of the campaign in the list of campaigns.