# create-slack-channel-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chatbot/create-slack-channel-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chatbot/create-slack-channel-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chatbot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chatbot/index.html#cli-aws-chatbot) ]

# create-slack-channel-configuration

## Description

Creates an AWS Chatbot confugration for Slack.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chatbot-2017-10-11/CreateSlackChannelConfiguration)

## Synopsis

```
create-slack-channel-configuration
--slack-team-id <value>
--slack-channel-id <value>
[--slack-channel-name <value>]
[--sns-topic-arns <value>]
--iam-role-arn <value>
--configuration-name <value>
[--logging-level <value>]
[--guardrail-policy-arns <value>]
[--user-authorization-required | --no-user-authorization-required]
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

`--slack-team-id` (string)

The ID of the Slack workspace authorized with AWS Chatbot.

`--slack-channel-id` (string)

The ID of the Slack channel.

To get this ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ.

`--slack-channel-name` (string)

The name of the Slack channel.

`--sns-topic-arns` (list)

The Amazon Resource Names (ARNs) of the SNS topics that deliver notifications to AWS Chatbot.

(string)

Syntax:

```
"string" "string" ...
```

`--iam-role-arn` (string)

A user-defined role that AWS Chatbot assumes. This is not the service-linked role.

For more information, see [IAM policies for AWS Chatbot](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the *AWS Chatbot Administrator Guide* .

`--configuration-name` (string)

The name of the configuration.

`--logging-level` (string)

Logging levels include `ERROR` , `INFO` , or `NONE` .

`--guardrail-policy-arns` (list)

The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed `AdministratorAccess` policy is applied by default if this is not set.

(string)

Syntax:

```
"string" "string" ...
```

`--user-authorization-required` | `--no-user-authorization-required` (boolean)

Enables use of a user role requirement in your chat configuration.

`--tags` (list)

A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.

(structure)

A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

### Warning

Do not include confidential or sensitive information in this field.

For more information, see [User-Defined Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html) in the *AWS Billing and Cost Management User Guide* .

TagKey -> (string)

The key of the tag.

TagValue -> (string)

The value of the tag.

Shorthand Syntax:

```
TagKey=string,TagValue=string ...
```

JSON Syntax:

```
[
  {
    "TagKey": "string",
    "TagValue": "string"
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

ChannelConfiguration -> (structure)

The configuration for a Slack channel configured with AWS Chatbot.

SlackTeamName -> (string)

Name of the Slack workspace.

SlackTeamId -> (string)

The ID of the Slack workspace authorized with Amazon Chime.

SlackChannelId -> (string)

The ID of the Slack channel.

To get this ID, open Slack, right click on the channel name in the left pane, then choose Copy Link. The channel ID is the 9-character string at the end of the URL. For example, ABCBBLZZZ.

SlackChannelName -> (string)

The name of the Slack channel.

ChatConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the SlackChannelConfiguration.

IamRoleArn -> (string)

A user-defined role that AWS Chatbot assumes. This is not the service-linked role.

For more information, see [IAM policies for AWS Chatbot](https://docs.aws.amazon.com/chatbot/latest/adminguide/chatbot-iam-policies.html) in the *AWS Chatbot Administrator Guide* .

SnsTopicArns -> (list)

The ARNs of the SNS topics that deliver notifications to AWS Chatbot.

(string)

ConfigurationName -> (string)

The name of the configuration.

LoggingLevel -> (string)

Logging levels include `ERROR` , `INFO` , or `NONE` .

GuardrailPolicyArns -> (list)

The list of IAM policy ARNs that are applied as channel guardrails. The AWS managed `AdministratorAccess` policy is applied by default if this is not set.

(string)

UserAuthorizationRequired -> (boolean)

Enables use of a user role requirement in your chat configuration.

Tags -> (list)

A map of tags assigned to a resource. A tag is a string-to-string map of key-value pairs.

(structure)

A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

### Warning

Do not include confidential or sensitive information in this field.

For more information, see [User-Defined Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html) in the *AWS Billing and Cost Management User Guide* .

TagKey -> (string)

The key of the tag.

TagValue -> (string)

The value of the tag.

State -> (string)

Either `ENABLED` or `DISABLED` . The resource returns `DISABLED` if the organizationâs AWS Chatbot policy has explicitly denied that configuration. For example, if Amazon Chime is disabled.

StateReason -> (string)

Provided if State is `DISABLED` . Provides context as to why the resource is disabled.