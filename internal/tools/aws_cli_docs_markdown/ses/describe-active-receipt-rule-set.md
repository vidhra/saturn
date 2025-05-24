# describe-active-receipt-rule-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-active-receipt-rule-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/describe-active-receipt-rule-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ses](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html#cli-aws-ses) ]

# describe-active-receipt-rule-set

## Description

Returns the metadata and receipt rules for the receipt rule set that is currently active.

For information about setting up receipt rule sets, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-concepts.html#receiving-email-concepts-rules) .

You can execute this operation no more than once per second.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/email-2010-12-01/DescribeActiveReceiptRuleSet)

## Synopsis

```
describe-active-receipt-rule-set
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

Metadata -> (structure)

The metadata for the currently active receipt rule set. The metadata consists of the rule set name and a timestamp of when the rule set was created.

Name -> (string)

The name of the receipt rule set. The name must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-).
- Start and end with a letter or number.
- Contain 64 characters or fewer.

CreatedTimestamp -> (timestamp)

The date and time the receipt rule set was created.

Rules -> (list)

The receipt rules that belong to the active rule set.

(structure)

Receipt rules enable you to specify which actions Amazon SES should take when it receives mail on behalf of one or more email addresses or domains that you own.

Each receipt rule defines a set of email addresses or domains that it applies to. If the email addresses or domains match at least one recipient address of the message, Amazon SES executes all of the receipt ruleâs actions on the message.

For information about setting up receipt rules, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html) .

Name -> (string)

The name of the receipt rule. The name must meet the following requirements:

- Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (_), dashes (-), or periods (.).
- Start and end with a letter or number.
- Contain 64 characters or fewer.

Enabled -> (boolean)

If `true` , the receipt rule is active. The default value is `false` .

TlsPolicy -> (string)

Specifies whether Amazon SES should require that incoming email is delivered over a connection encrypted with Transport Layer Security (TLS). If this parameter is set to `Require` , Amazon SES bounces emails that are not received over TLS. The default is `Optional` .

Recipients -> (list)

The recipient domains and email addresses that the receipt rule applies to. If this field is not specified, this rule matches all recipients on all verified domains.

(string)

Actions -> (list)

An ordered list of actions to perform on messages that match at least one of the recipient email addresses or domains specified in the receipt rule.

(structure)

An action that Amazon SES can take when it receives an email on behalf of one or more email addresses or domains that you own. An instance of this data type can represent only one action.

For information about setting up receipt rules, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-receipt-rules-console-walkthrough.html) .

S3Action -> (structure)

Saves the received message to an Amazon Simple Storage Service (Amazon S3) bucket and, optionally, publishes a notification to Amazon SNS.

TopicArn -> (string)

The ARN of the Amazon SNS topic to notify when the message is saved to the Amazon S3 bucket. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) operation in Amazon SNS.

For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) .

BucketName -> (string)

The name of the Amazon S3 bucket for incoming email.

ObjectKeyPrefix -> (string)

The key prefix of the Amazon S3 bucket. The key prefix is similar to a directory name that enables you to store similar data under the same directory in a bucket.

KmsKeyArn -> (string)

The customer managed key that Amazon SES should use to encrypt your emails before saving them to the Amazon S3 bucket. You can use the Amazon Web Services managed key or a customer managed key that you created in Amazon Web Services KMS as follows:

- To use the Amazon Web Services managed key, provide an ARN in the form of `arn:aws:kms:REGION:ACCOUNT-ID-WITHOUT-HYPHENS:alias/aws/ses` . For example, if your Amazon Web Services account ID is 123456789012 and you want to use the Amazon Web Services managed key in the US West (Oregon) Region, the ARN of the Amazon Web Services managed key would be `arn:aws:kms:us-west-2:123456789012:alias/aws/ses` . If you use the Amazon Web Services managed key, you donât need to perform any extra steps to give Amazon SES permission to use the key.
- To use a customer managed key that you created in Amazon Web Services KMS, provide the ARN of the customer managed key and ensure that you add a statement to your keyâs policy to give Amazon SES permission to use it. For more information about giving permissions, see the [Amazon SES Developer Guide](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-permissions.html) .

For more information about key policies, see the [Amazon Web Services KMS Developer Guide](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) . If you do not specify an Amazon Web Services KMS key, Amazon SES does not encrypt your emails.

### Warning

Your mail is encrypted by Amazon SES using the Amazon S3 encryption client before the mail is submitted to Amazon S3 for storage. It is not encrypted using Amazon S3 server-side encryption. This means that you must use the Amazon S3 encryption client to decrypt the email after retrieving it from Amazon S3, as the service has no access to use your Amazon Web Services KMS keys for decryption. This encryption client is currently available with the [Amazon Web Services SDK for Java](http://aws.amazon.com/sdk-for-java/) and [Amazon Web Services SDK for Ruby](http://aws.amazon.com/sdk-for-ruby/) only. For more information about client-side encryption using Amazon Web Services KMS managed keys, see the [Amazon S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingClientSideEncryption.html) .

IamRoleArn -> (string)

The ARN of the IAM role to be used by Amazon Simple Email Service while writing to the Amazon S3 bucket, optionally encrypting your mail via the provided customer managed key, and publishing to the Amazon SNS topic. This role should have access to the following APIs:

- `s3:PutObject` , `kms:Encrypt` and `kms:GenerateDataKey` for the given Amazon S3 bucket.
- `kms:GenerateDataKey` for the given Amazon Web Services KMS customer managed key.
- `sns:Publish` for the given Amazon SNS topic.

### Note

If an IAM role ARN is provided, the role (and only the role) is used to access all the given resources (Amazon S3 bucket, Amazon Web Services KMS customer managed key and Amazon SNS topic). Therefore, setting up individual resource access permissions is not required.

BounceAction -> (structure)

Rejects the received email by returning a bounce response to the sender and, optionally, publishes a notification to Amazon Simple Notification Service (Amazon SNS).

TopicArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the bounce action is taken. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) operation in Amazon SNS.

For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) .

SmtpReplyCode -> (string)

The SMTP reply code, as defined by [RFC 5321](https://tools.ietf.org/html/rfc5321) .

StatusCode -> (string)

The SMTP enhanced status code, as defined by [RFC 3463](https://tools.ietf.org/html/rfc3463) .

Message -> (string)

Human-readable text to include in the bounce message.

Sender -> (string)

The email address of the sender of the bounced email. This is the address from which the bounce message is sent.

WorkmailAction -> (structure)

Calls Amazon WorkMail and, optionally, publishes a notification to Amazon Amazon SNS.

TopicArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the WorkMail action is called. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) operation in Amazon SNS.

For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) .

OrganizationArn -> (string)

The Amazon Resource Name (ARN) of the Amazon WorkMail organization. Amazon WorkMail ARNs use the following format:

`arn:aws:workmail:<region>:<awsAccountId>:organization/<workmailOrganizationId>`

You can find the ID of your organization by using the [ListOrganizations](https://docs.aws.amazon.com/workmail/latest/APIReference/API_ListOrganizations.html) operation in Amazon WorkMail. Amazon WorkMail organization IDs begin with â`m-` â, followed by a string of alphanumeric characters.

For information about Amazon WorkMail organizations, see the [Amazon WorkMail Administrator Guide](https://docs.aws.amazon.com/workmail/latest/adminguide/organizations_overview.html) .

LambdaAction -> (structure)

Calls an Amazon Web Services Lambda function, and optionally, publishes a notification to Amazon SNS.

TopicArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the Lambda action is executed. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) operation in Amazon SNS.

For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) .

FunctionArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services Lambda function. An example of an Amazon Web Services Lambda function ARN is `arn:aws:lambda:us-west-2:account-id:function:MyFunction` . For more information about Amazon Web Services Lambda, see the [Amazon Web Services Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) .

InvocationType -> (string)

The invocation type of the Amazon Web Services Lambda function. An invocation type of `RequestResponse` means that the execution of the function immediately results in a response, and a value of `Event` means that the function is invoked asynchronously. The default value is `Event` . For information about Amazon Web Services Lambda invocation types, see the [Amazon Web Services Lambda Developer Guide](https://docs.aws.amazon.com/lambda/latest/dg/API_Invoke.html) .

### Warning

There is a 30-second timeout on `RequestResponse` invocations. You should use `Event` invocation in most cases. Use `RequestResponse` only to make a mail flow decision, such as whether to stop the receipt rule or the receipt rule set.

StopAction -> (structure)

Terminates the evaluation of the receipt rule set and optionally publishes a notification to Amazon SNS.

Scope -> (string)

The scope of the StopAction. The only acceptable value is `RuleSet` .

TopicArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS topic to notify when the stop action is taken. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) Amazon SNS operation.

For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) .

AddHeaderAction -> (structure)

Adds a header to the received email.

HeaderName -> (string)

The name of the header to add to the incoming message. The name must contain at least one character, and can contain up to 50 characters. It consists of alphanumeric (aâz, AâZ, 0â9) characters and dashes.

HeaderValue -> (string)

The content to include in the header. This value can contain up to 2048 characters. It canât contain newline (`\n` ) or carriage return (`\r` ) characters.

SNSAction -> (structure)

Publishes the email content within a notification to Amazon SNS.

TopicArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS topic to notify. You can find the ARN of a topic by using the [ListTopics](https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html) operation in Amazon SNS.

For more information about Amazon SNS topics, see the [Amazon SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/CreateTopic.html) .

Encoding -> (string)

The encoding to use for the email within the Amazon SNS notification. UTF-8 is easier to use, but may not preserve all special characters when a message was encoded with a different encoding format. Base64 preserves all special characters. The default value is UTF-8.

ConnectAction -> (structure)

Parses the received message and starts an email contact in Amazon Connect on your behalf.

InstanceARN -> (string)

The Amazon Resource Name (ARN) for the Amazon Connect instance that Amazon SES integrates with for starting email contacts.

For more information about Amazon Connect instances, see the [Amazon Connect Administrator Guide](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-instances.html)

IAMRoleARN -> (string)

The Amazon Resource Name (ARN) of the IAM role to be used by Amazon Simple Email Service while starting email contacts to the Amazon Connect instance. This role should have permission to invoke `connect:StartEmailContact` for the given Amazon Connect instance.

ScanEnabled -> (boolean)

If `true` , then messages that this receipt rule applies to are scanned for spam and viruses. The default value is `false` .