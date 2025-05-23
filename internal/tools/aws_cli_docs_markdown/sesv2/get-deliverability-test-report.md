# get-deliverability-test-reportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-deliverability-test-report.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/get-deliverability-test-report.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# get-deliverability-test-report

## Description

Retrieve the results of a predictive inbox placement test.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/GetDeliverabilityTestReport)

## Synopsis

```
get-deliverability-test-report
--report-id <value>
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

`--report-id` (string)

A unique string that identifies the predictive inbox placement test.

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

DeliverabilityTestReport -> (structure)

An object that contains the results of the predictive inbox placement test.

ReportId -> (string)

A unique string that identifies the predictive inbox placement test.

ReportName -> (string)

A name that helps you identify a predictive inbox placement test report.

Subject -> (string)

The subject line for an email that you submitted in a predictive inbox placement test.

FromEmailAddress -> (string)

The sender address that you specified for the predictive inbox placement test.

CreateDate -> (timestamp)

The date and time when the predictive inbox placement test was created.

DeliverabilityTestStatus -> (string)

The status of the predictive inbox placement test. If the status is `IN_PROGRESS` , then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is `COMPLETE` , then the test is finished, and you can use the `GetDeliverabilityTestReport` to view the results of the test.

OverallPlacement -> (structure)

An object that specifies how many test messages that were sent during the predictive inbox placement test were delivered to recipientsâ inboxes, how many were sent to recipientsâ spam folders, and how many werenât delivered.

InboxPercentage -> (double)

The percentage of emails that arrived in recipientsâ inboxes during the predictive inbox placement test.

SpamPercentage -> (double)

The percentage of emails that arrived in recipientsâ spam or junk mail folders during the predictive inbox placement test.

MissingPercentage -> (double)

The percentage of emails that didnât arrive in recipientsâ inboxes at all during the predictive inbox placement test.

SpfPercentage -> (double)

The percentage of emails that were authenticated by using Sender Policy Framework (SPF) during the predictive inbox placement test.

DkimPercentage -> (double)

The percentage of emails that were authenticated by using DomainKeys Identified Mail (DKIM) during the predictive inbox placement test.

IspPlacements -> (list)

An object that describes how the test email was handled by several email providers, including Gmail, Hotmail, Yahoo, AOL, and others.

(structure)

An object that describes how email sent during the predictive inbox placement test was handled by a certain email provider.

IspName -> (string)

The name of the email provider that the inbox placement data applies to.

PlacementStatistics -> (structure)

An object that contains inbox placement metrics for a specific email provider.

InboxPercentage -> (double)

The percentage of emails that arrived in recipientsâ inboxes during the predictive inbox placement test.

SpamPercentage -> (double)

The percentage of emails that arrived in recipientsâ spam or junk mail folders during the predictive inbox placement test.

MissingPercentage -> (double)

The percentage of emails that didnât arrive in recipientsâ inboxes at all during the predictive inbox placement test.

SpfPercentage -> (double)

The percentage of emails that were authenticated by using Sender Policy Framework (SPF) during the predictive inbox placement test.

DkimPercentage -> (double)

The percentage of emails that were authenticated by using DomainKeys Identified Mail (DKIM) during the predictive inbox placement test.

Message -> (string)

An object that contains the message that you sent when you performed this predictive inbox placement test.

Tags -> (list)

An array of objects that define the tags (keys and values) that are associated with the predictive inbox placement test.

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