# create-rule-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mailmanager/create-rule-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mailmanager/create-rule-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mailmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mailmanager/index.html#cli-aws-mailmanager) ]

# create-rule-set

## Description

Provision a new rule set.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mailmanager-2023-10-17/CreateRuleSet)

## Synopsis

```
create-rule-set
[--client-token <value>]
--rule-set-name <value>
--rules <value>
[--tags <value>]
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

`--client-token` (string)

A unique token that Amazon SES uses to recognize subsequent retries of the same request.

`--rule-set-name` (string)

A user-friendly name for the rule set.

`--rules` (list)

Conditional rules that are evaluated for determining actions on email.

(structure)

A rule contains conditions, âunless conditionsâ and actions. For each envelope recipient of an email, if all conditions match and none of the âunless conditionsâ match, then all of the actions are executed sequentially. If no conditions are provided, the rule always applies and the actions are implicitly executed. If only âunless conditionsâ are provided, the rule applies if the email does not match the evaluation of the âunless conditionsâ.

Actions -> (list)

The list of actions to execute when the conditions match the incoming email, and none of the âunless conditionsâ match.

(tagged union structure)

The action for a rule to take. Only one of the contained actions can be set.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `AddHeader`, `Archive`, `DeliverToMailbox`, `DeliverToQBusiness`, `Drop`, `PublishToSns`, `Relay`, `ReplaceRecipient`, `Send`, `WriteToS3`.

AddHeader -> (structure)

This action adds a header. This can be used to add arbitrary email headers.

HeaderName -> (string)

The name of the header to add to an email. The header must be prefixed with âX-â. Headers are added regardless of whether the header name pre-existed in the email.

HeaderValue -> (string)

The value of the header to add to the email.

Archive -> (structure)

This action archives the email. This can be used to deliver an email to an archive.

ActionFailurePolicy -> (string)

A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified archive has been deleted.

TargetArchive -> (string)

The identifier of the archive to send the email to.

DeliverToMailbox -> (structure)

This action delivers an email to a WorkMail mailbox.

ActionFailurePolicy -> (string)

A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the mailbox ARN is no longer valid.

MailboxArn -> (string)

The Amazon Resource Name (ARN) of a WorkMail organization to deliver the email to.

RoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role to use to execute this action. The role must have access to the workmail:DeliverToMailbox API.

DeliverToQBusiness -> (structure)

This action delivers an email to an Amazon Q Business application for ingestion into its knowledge base.

ActionFailurePolicy -> (string)

A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified application has been deleted or the role lacks necessary permissions to call the `qbusiness:BatchPutDocument` API.

ApplicationId -> (string)

The unique identifier of the Amazon Q Business application instance where the email content will be delivered.

IndexId -> (string)

The identifier of the knowledge base index within the Amazon Q Business application where the email content will be stored and indexed.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM Role to use while delivering to Amazon Q Business. This role must have access to the `qbusiness:BatchPutDocument` API for the given application and index.

Drop -> (structure)

This action terminates the evaluation of rules in the rule set.

PublishToSns -> (structure)

This action publishes the email content to an Amazon SNS topic.

ActionFailurePolicy -> (string)

A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, specified SNS topic has been deleted or the role lacks necessary permissions to call the `sns:Publish` API.

Encoding -> (string)

The encoding to use for the email within the Amazon SNS notification. The default value is `UTF-8` . Use `BASE64` if you need to preserve all special characters, especially when the original message uses a different encoding format.

PayloadType -> (string)

The expected payload type within the Amazon SNS notification. `CONTENT` attempts to publish the full email content with 20KB of headers content. `HEADERS` extracts up to 100KB of header content to include in the notification, email content will not be included to the notification. The default value is `CONTENT` .

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM Role to use while writing to Amazon SNS. This role must have access to the `sns:Publish` API for the given topic.

TopicArn -> (string)

The Amazon Resource Name (ARN) of the Amazon SNS Topic to which notification for the email received will be published.

Relay -> (structure)

This action relays the email to another SMTP server.

ActionFailurePolicy -> (string)

A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified relay has been deleted.

MailFrom -> (string)

This action specifies whether to preserve or replace original mail from address while relaying received emails to a destination server.

Relay -> (string)

The identifier of the relay resource to be used when relaying an email.

ReplaceRecipient -> (structure)

The action replaces certain or all recipients with a different set of recipients.

ReplaceWith -> (list)

This action specifies the replacement recipient email addresses to insert.

(string)

Send -> (structure)

This action sends the email to the internet.

ActionFailurePolicy -> (string)

A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the caller does not have the permissions to call the sendRawEmail API.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role to use for this action. This role must have access to the ses:SendRawEmail API.

WriteToS3 -> (structure)

This action writes the MIME content of the email to an S3 bucket.

ActionFailurePolicy -> (string)

A policy that states what to do in the case of failure. The action will fail if there are configuration errors. For example, the specified the bucket has been deleted.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM Role to use while writing to S3. This role must have access to the s3:PutObject, kms:Encrypt, and kms:GenerateDataKey APIs for the given bucket.

S3Bucket -> (string)

The bucket name of the S3 bucket to write to.

S3Prefix -> (string)

The S3 prefix to use for the write to the s3 bucket.

S3SseKmsKeyId -> (string)

The KMS Key ID to use to encrypt the message in S3.

Conditions -> (list)

The conditions of this rule. All conditions must match the email for the actions to be executed. An empty list of conditions means that all emails match, but are still subject to any âunless conditionsâ

(tagged union structure)

The conditional expression used to evaluate an email for determining if a rule action should be taken.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `BooleanExpression`, `DmarcExpression`, `IpExpression`, `NumberExpression`, `StringExpression`, `VerdictExpression`.

BooleanExpression -> (structure)

The condition applies to a boolean expression passed in this field.

Evaluate -> (tagged union structure)

The operand on which to perform a boolean condition operation.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Analysis`, `Attribute`, `IsInAddressList`.

Analysis -> (structure)

The Add On ARN and its returned value to evaluate in a boolean condition expression.

Analyzer -> (string)

The Amazon Resource Name (ARN) of an Add On.

ResultField -> (string)

The returned value from an Add On.

Attribute -> (string)

The boolean type representing the allowed attribute types for an email.

IsInAddressList -> (structure)

The structure representing the address lists and address list attribute that will be used in evaluation of boolean expression.

AddressLists -> (list)

The address lists that will be used for evaluation.

(string)

Attribute -> (string)

The email attribute that needs to be evaluated against the address list.

Operator -> (string)

The matching operator for a boolean condition expression.

DmarcExpression -> (structure)

The condition applies to a DMARC policy expression passed in this field.

Operator -> (string)

The operator to apply to the DMARC policy of the incoming email.

Values -> (list)

The values to use for the given DMARC policy operator. For the operator EQUALS, if multiple values are given, they are evaluated as an OR. That is, if any of the given values match, the condition is deemed to match. For the operator NOT_EQUALS, if multiple values are given, they are evaluated as an AND. That is, only if the emailâs DMARC policy is not equal to any of the given values, then the condition is deemed to match.

(string)

IpExpression -> (structure)

The condition applies to an IP address expression passed in this field.

Evaluate -> (tagged union structure)

The IP address to evaluate in this condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Attribute`.

Attribute -> (string)

The attribute of the email to evaluate.

Operator -> (string)

The operator to evaluate the IP address.

Values -> (list)

The IP CIDR blocks in format âx.y.z.w/nâ (eg 10.0.0.0/8) to match with the emailâs IP address. For the operator CIDR_MATCHES, if multiple values are given, they are evaluated as an OR. That is, if the IP address is contained within any of the given CIDR ranges, the condition is deemed to match. For NOT_CIDR_MATCHES, if multiple CIDR ranges are given, the condition is deemed to match if the IP address is not contained in any of the given CIDR ranges.

(string)

NumberExpression -> (structure)

The condition applies to a number expression passed in this field.

Evaluate -> (tagged union structure)

The number to evaluate in a numeric condition expression.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Attribute`.

Attribute -> (string)

An email attribute that is used as the number to evaluate.

Operator -> (string)

The operator for a numeric condition expression.

Value -> (double)

The value to evaluate in a numeric condition expression.

StringExpression -> (structure)

The condition applies to a string expression passed in this field.

Evaluate -> (tagged union structure)

The string to evaluate in a string condition expression.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Analysis`, `Attribute`, `MimeHeaderAttribute`.

Analysis -> (structure)

The Add On ARN and its returned value to evaluate in a string condition expression.

Analyzer -> (string)

The Amazon Resource Name (ARN) of an Add On.

ResultField -> (string)

The returned value from an Add On.

Attribute -> (string)

The email attribute to evaluate in a string condition expression.

MimeHeaderAttribute -> (string)

The email MIME X-Header attribute to evaluate in a string condition expression.

Operator -> (string)

The matching operator for a string condition expression.

Values -> (list)

The string(s) to be evaluated in a string condition expression. For all operators, except for NOT_EQUALS, if multiple values are given, the values are processed as an OR. That is, if any of the values match the emailâs string using the given operator, the condition is deemed to match. However, for NOT_EQUALS, the condition is only deemed to match if none of the given strings match the emailâs string.

(string)

VerdictExpression -> (structure)

The condition applies to a verdict expression passed in this field.

Evaluate -> (tagged union structure)

The verdict to evaluate in a verdict condition expression.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Analysis`, `Attribute`.

Analysis -> (structure)

The Add On ARN and its returned value to evaluate in a verdict condition expression.

Analyzer -> (string)

The Amazon Resource Name (ARN) of an Add On.

ResultField -> (string)

The returned value from an Add On.

Attribute -> (string)

The email verdict attribute to evaluate in a string verdict expression.

Operator -> (string)

The matching operator for a verdict condition expression.

Values -> (list)

The values to match with the emailâs verdict using the given operator. For the EQUALS operator, if multiple values are given, the condition is deemed to match if any of the given verdicts match that of the email. For the NOT_EQUALS operator, if multiple values are given, the condition is deemed to match of none of the given verdicts match the verdict of the email.

(string)

Name -> (string)

The user-friendly name of the rule.

Unless -> (list)

The âunless conditionsâ of this rule. None of the conditions can match the email for the actions to be executed. If any of these conditions do match the email, then the actions are not executed.

(tagged union structure)

The conditional expression used to evaluate an email for determining if a rule action should be taken.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `BooleanExpression`, `DmarcExpression`, `IpExpression`, `NumberExpression`, `StringExpression`, `VerdictExpression`.

BooleanExpression -> (structure)

The condition applies to a boolean expression passed in this field.

Evaluate -> (tagged union structure)

The operand on which to perform a boolean condition operation.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Analysis`, `Attribute`, `IsInAddressList`.

Analysis -> (structure)

The Add On ARN and its returned value to evaluate in a boolean condition expression.

Analyzer -> (string)

The Amazon Resource Name (ARN) of an Add On.

ResultField -> (string)

The returned value from an Add On.

Attribute -> (string)

The boolean type representing the allowed attribute types for an email.

IsInAddressList -> (structure)

The structure representing the address lists and address list attribute that will be used in evaluation of boolean expression.

AddressLists -> (list)

The address lists that will be used for evaluation.

(string)

Attribute -> (string)

The email attribute that needs to be evaluated against the address list.

Operator -> (string)

The matching operator for a boolean condition expression.

DmarcExpression -> (structure)

The condition applies to a DMARC policy expression passed in this field.

Operator -> (string)

The operator to apply to the DMARC policy of the incoming email.

Values -> (list)

The values to use for the given DMARC policy operator. For the operator EQUALS, if multiple values are given, they are evaluated as an OR. That is, if any of the given values match, the condition is deemed to match. For the operator NOT_EQUALS, if multiple values are given, they are evaluated as an AND. That is, only if the emailâs DMARC policy is not equal to any of the given values, then the condition is deemed to match.

(string)

IpExpression -> (structure)

The condition applies to an IP address expression passed in this field.

Evaluate -> (tagged union structure)

The IP address to evaluate in this condition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Attribute`.

Attribute -> (string)

The attribute of the email to evaluate.

Operator -> (string)

The operator to evaluate the IP address.

Values -> (list)

The IP CIDR blocks in format âx.y.z.w/nâ (eg 10.0.0.0/8) to match with the emailâs IP address. For the operator CIDR_MATCHES, if multiple values are given, they are evaluated as an OR. That is, if the IP address is contained within any of the given CIDR ranges, the condition is deemed to match. For NOT_CIDR_MATCHES, if multiple CIDR ranges are given, the condition is deemed to match if the IP address is not contained in any of the given CIDR ranges.

(string)

NumberExpression -> (structure)

The condition applies to a number expression passed in this field.

Evaluate -> (tagged union structure)

The number to evaluate in a numeric condition expression.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Attribute`.

Attribute -> (string)

An email attribute that is used as the number to evaluate.

Operator -> (string)

The operator for a numeric condition expression.

Value -> (double)

The value to evaluate in a numeric condition expression.

StringExpression -> (structure)

The condition applies to a string expression passed in this field.

Evaluate -> (tagged union structure)

The string to evaluate in a string condition expression.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Analysis`, `Attribute`, `MimeHeaderAttribute`.

Analysis -> (structure)

The Add On ARN and its returned value to evaluate in a string condition expression.

Analyzer -> (string)

The Amazon Resource Name (ARN) of an Add On.

ResultField -> (string)

The returned value from an Add On.

Attribute -> (string)

The email attribute to evaluate in a string condition expression.

MimeHeaderAttribute -> (string)

The email MIME X-Header attribute to evaluate in a string condition expression.

Operator -> (string)

The matching operator for a string condition expression.

Values -> (list)

The string(s) to be evaluated in a string condition expression. For all operators, except for NOT_EQUALS, if multiple values are given, the values are processed as an OR. That is, if any of the values match the emailâs string using the given operator, the condition is deemed to match. However, for NOT_EQUALS, the condition is only deemed to match if none of the given strings match the emailâs string.

(string)

VerdictExpression -> (structure)

The condition applies to a verdict expression passed in this field.

Evaluate -> (tagged union structure)

The verdict to evaluate in a verdict condition expression.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `Analysis`, `Attribute`.

Analysis -> (structure)

The Add On ARN and its returned value to evaluate in a verdict condition expression.

Analyzer -> (string)

The Amazon Resource Name (ARN) of an Add On.

ResultField -> (string)

The returned value from an Add On.

Attribute -> (string)

The email verdict attribute to evaluate in a string verdict expression.

Operator -> (string)

The matching operator for a verdict condition expression.

Values -> (list)

The values to match with the emailâs verdict using the given operator. For the EQUALS operator, if multiple values are given, the condition is deemed to match if any of the given verdicts match that of the email. For the NOT_EQUALS operator, if multiple values are given, the condition is deemed to match of none of the given verdicts match the verdict of the email.

(string)

JSON Syntax:

```
[
  {
    "Actions": [
      {
        "AddHeader": {
          "HeaderName": "string",
          "HeaderValue": "string"
        },
        "Archive": {
          "ActionFailurePolicy": "CONTINUE"|"DROP",
          "TargetArchive": "string"
        },
        "DeliverToMailbox": {
          "ActionFailurePolicy": "CONTINUE"|"DROP",
          "MailboxArn": "string",
          "RoleArn": "string"
        },
        "DeliverToQBusiness": {
          "ActionFailurePolicy": "CONTINUE"|"DROP",
          "ApplicationId": "string",
          "IndexId": "string",
          "RoleArn": "string"
        },
        "Drop": {

        },
        "PublishToSns": {
          "ActionFailurePolicy": "CONTINUE"|"DROP",
          "Encoding": "UTF-8"|"BASE64",
          "PayloadType": "HEADERS"|"CONTENT",
          "RoleArn": "string",
          "TopicArn": "string"
        },
        "Relay": {
          "ActionFailurePolicy": "CONTINUE"|"DROP",
          "MailFrom": "REPLACE"|"PRESERVE",
          "Relay": "string"
        },
        "ReplaceRecipient": {
          "ReplaceWith": ["string", ...]
        },
        "Send": {
          "ActionFailurePolicy": "CONTINUE"|"DROP",
          "RoleArn": "string"
        },
        "WriteToS3": {
          "ActionFailurePolicy": "CONTINUE"|"DROP",
          "RoleArn": "string",
          "S3Bucket": "string",
          "S3Prefix": "string",
          "S3SseKmsKeyId": "string"
        }
      }
      ...
    ],
    "Conditions": [
      {
        "BooleanExpression": {
          "Evaluate": {
            "Analysis": {
              "Analyzer": "string",
              "ResultField": "string"
            },
            "Attribute": "READ_RECEIPT_REQUESTED"|"TLS"|"TLS_WRAPPED",
            "IsInAddressList": {
              "AddressLists": ["string", ...],
              "Attribute": "RECIPIENT"|"MAIL_FROM"|"SENDER"|"FROM"|"TO"|"CC"
            }
          },
          "Operator": "IS_TRUE"|"IS_FALSE"
        },
        "DmarcExpression": {
          "Operator": "EQUALS"|"NOT_EQUALS",
          "Values": ["NONE"|"QUARANTINE"|"REJECT", ...]
        },
        "IpExpression": {
          "Evaluate": {
            "Attribute": "SOURCE_IP"
          },
          "Operator": "CIDR_MATCHES"|"NOT_CIDR_MATCHES",
          "Values": ["string", ...]
        },
        "NumberExpression": {
          "Evaluate": {
            "Attribute": "MESSAGE_SIZE"
          },
          "Operator": "EQUALS"|"NOT_EQUALS"|"LESS_THAN"|"GREATER_THAN"|"LESS_THAN_OR_EQUAL"|"GREATER_THAN_OR_EQUAL",
          "Value": double
        },
        "StringExpression": {
          "Evaluate": {
            "Analysis": {
              "Analyzer": "string",
              "ResultField": "string"
            },
            "Attribute": "MAIL_FROM"|"HELO"|"RECIPIENT"|"SENDER"|"FROM"|"SUBJECT"|"TO"|"CC",
            "MimeHeaderAttribute": "string"
          },
          "Operator": "EQUALS"|"NOT_EQUALS"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS",
          "Values": ["string", ...]
        },
        "VerdictExpression": {
          "Evaluate": {
            "Analysis": {
              "Analyzer": "string",
              "ResultField": "string"
            },
            "Attribute": "SPF"|"DKIM"
          },
          "Operator": "EQUALS"|"NOT_EQUALS",
          "Values": ["PASS"|"FAIL"|"GRAY"|"PROCESSING_FAILED", ...]
        }
      }
      ...
    ],
    "Name": "string",
    "Unless": [
      {
        "BooleanExpression": {
          "Evaluate": {
            "Analysis": {
              "Analyzer": "string",
              "ResultField": "string"
            },
            "Attribute": "READ_RECEIPT_REQUESTED"|"TLS"|"TLS_WRAPPED",
            "IsInAddressList": {
              "AddressLists": ["string", ...],
              "Attribute": "RECIPIENT"|"MAIL_FROM"|"SENDER"|"FROM"|"TO"|"CC"
            }
          },
          "Operator": "IS_TRUE"|"IS_FALSE"
        },
        "DmarcExpression": {
          "Operator": "EQUALS"|"NOT_EQUALS",
          "Values": ["NONE"|"QUARANTINE"|"REJECT", ...]
        },
        "IpExpression": {
          "Evaluate": {
            "Attribute": "SOURCE_IP"
          },
          "Operator": "CIDR_MATCHES"|"NOT_CIDR_MATCHES",
          "Values": ["string", ...]
        },
        "NumberExpression": {
          "Evaluate": {
            "Attribute": "MESSAGE_SIZE"
          },
          "Operator": "EQUALS"|"NOT_EQUALS"|"LESS_THAN"|"GREATER_THAN"|"LESS_THAN_OR_EQUAL"|"GREATER_THAN_OR_EQUAL",
          "Value": double
        },
        "StringExpression": {
          "Evaluate": {
            "Analysis": {
              "Analyzer": "string",
              "ResultField": "string"
            },
            "Attribute": "MAIL_FROM"|"HELO"|"RECIPIENT"|"SENDER"|"FROM"|"SUBJECT"|"TO"|"CC",
            "MimeHeaderAttribute": "string"
          },
          "Operator": "EQUALS"|"NOT_EQUALS"|"STARTS_WITH"|"ENDS_WITH"|"CONTAINS",
          "Values": ["string", ...]
        },
        "VerdictExpression": {
          "Evaluate": {
            "Analysis": {
              "Analyzer": "string",
              "ResultField": "string"
            },
            "Attribute": "SPF"|"DKIM"
          },
          "Operator": "EQUALS"|"NOT_EQUALS",
          "Values": ["PASS"|"FAIL"|"GRAY"|"PROCESSING_FAILED", ...]
        }
      }
      ...
    ]
  }
  ...
]
```

`--tags` (list)

The tags used to organize, track, or control access for the resource. For example, { âtagsâ: {âkey1â:âvalue1â, âkey2â:âvalue2â} }.

(structure)

A key-value pair (the value is optional), that you can define and assign to Amazon Web Services resources.

Key -> (string)

The key of the key-value tag.

Value -> (string)

The value of the key-value tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
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

RuleSetId -> (string)

The identifier of the created rule set.