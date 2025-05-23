# get-accountÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-account.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/get-account.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint-email](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint-email/index.html#cli-aws-pinpoint-email) ]

# get-account

## Description

Obtain information about the email-sending status and capabilities of your Amazon Pinpoint account in the current AWS Region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-email-2018-07-26/GetAccount)

## Synopsis

```
get-account
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

SendQuota -> (structure)

An object that contains information about the per-day and per-second sending limits for your Amazon Pinpoint account in the current AWS Region.

Max24HourSend -> (double)

The maximum number of emails that you can send in the current AWS Region over a 24-hour period. This value is also called your *sending quota* .

MaxSendRate -> (double)

The maximum number of emails that you can send per second in the current AWS Region. This value is also called your *maximum sending rate* or your *maximum TPS (transactions per second) rate* .

SentLast24Hours -> (double)

The number of emails sent from your Amazon Pinpoint account in the current AWS Region over the past 24 hours.

SendingEnabled -> (boolean)

Indicates whether or not email sending is enabled for your Amazon Pinpoint account in the current AWS Region.

DedicatedIpAutoWarmupEnabled -> (boolean)

Indicates whether or not the automatic warm-up feature is enabled for dedicated IP addresses that are associated with your account.

EnforcementStatus -> (string)

The reputation status of your Amazon Pinpoint account. The status can be one of the following:

- `HEALTHY` â There are no reputation-related issues that currently impact your account.
- `PROBATION` â Weâve identified some issues with your Amazon Pinpoint account. Weâre placing your account under review while you work on correcting these issues.
- `SHUTDOWN` â Your accountâs ability to send email is currently paused because of an issue with the email sent from your account. When you correct the issue, you can contact us and request that your accountâs ability to send email is resumed.

ProductionAccessEnabled -> (boolean)

Indicates whether or not your account has production access in the current AWS Region.

If the value is `false` , then your account is in the *sandbox* . When your account is in the sandbox, you can only send email to verified identities. Additionally, the maximum number of emails you can send in a 24-hour period (your sending quota) is 200, and the maximum number of emails you can send per second (your maximum sending rate) is 1.

If the value is `true` , then your account has production access. When your account has production access, you can send email to any address. The sending quota and maximum sending rate for your account vary based on your specific use case.