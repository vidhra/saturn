# describe-alarm-modelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/describe-alarm-model.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/describe-alarm-model.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotevents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/index.html#cli-aws-iotevents) ]

# describe-alarm-model

## Description

Retrieves information about an alarm model. If you donât specify a value for the `alarmModelVersion` parameter, the latest version is returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/DescribeAlarmModel)

## Synopsis

```
describe-alarm-model
--alarm-model-name <value>
[--alarm-model-version <value>]
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

`--alarm-model-name` (string)

The name of the alarm model.

`--alarm-model-version` (string)

The version of the alarm model.

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

creationTime -> (timestamp)

The time the alarm model was created, in the Unix epoch format.

alarmModelArn -> (string)

The ARN of the alarm model. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference* .

alarmModelVersion -> (string)

The version of the alarm model.

lastUpdateTime -> (timestamp)

The time the alarm model was last updated, in the Unix epoch format.

status -> (string)

The status of the alarm model. The status can be one of the following values:

- `ACTIVE` - The alarm model is active and itâs ready to evaluate data.
- `ACTIVATING` - AWS IoT Events is activating your alarm model. Activating an alarm model can take up to a few minutes.
- `INACTIVE` - The alarm model is inactive, so it isnât ready to evaluate data. Check your alarm model information and update the alarm model.
- `FAILED` - You couldnât create or update the alarm model. Check your alarm model information and try again.

statusMessage -> (string)

Contains information about the status of the alarm model.

alarmModelName -> (string)

The name of the alarm model.

alarmModelDescription -> (string)

The description of the alarm model.

roleArn -> (string)

The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference* .

key -> (string)

An input attribute used as a key to create an alarm. AWS IoT Events routes [inputs](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html) associated with this key to the alarm.

severity -> (integer)

A non-negative integer that reflects the severity level of the alarm.

alarmRule -> (structure)

Defines when your alarm is invoked.

simpleRule -> (structure)

A rule that compares an input property value to a threshold value with a comparison operator.

inputProperty -> (string)

The value on the left side of the comparison operator. You can specify an AWS IoT Events input attribute as an input property.

comparisonOperator -> (string)

The comparison operator.

threshold -> (string)

The value on the right side of the comparison operator. You can enter a number or specify an AWS IoT Events input attribute.

alarmNotification -> (structure)

Contains information about one or more notification actions.

notificationActions -> (list)

Contains the notification settings of an alarm model. The settings apply to all alarms that were created based on this alarm model.

(structure)

Contains the notification settings of an alarm model. The settings apply to all alarms that were created based on this alarm model.

action -> (structure)

Specifies an AWS Lambda function to manage alarm notifications. You can create one or use the [AWS Lambda function provided by AWS IoT Events](https://docs.aws.amazon.com/iotevents/latest/developerguide/lambda-support.html) .

lambdaAction -> (structure)

Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

functionArn -> (string)

The ARN of the Lambda function that is executed.

payload -> (structure)

You can configure the action payload when you send a message to a Lambda function.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

smsConfigurations -> (list)

Contains the configuration information of SMS notifications.

(structure)

Contains the configuration information of SMS notifications.

senderId -> (string)

The sender ID.

additionalMessage -> (string)

The message that you want to send. The message can be up to 200 characters.

recipients -> (list)

Specifies one or more recipients who receive the message.

### Warning

You must [add the users that receive SMS messages to your AWS SSO store](https://docs.aws.amazon.com/singlesignon/latest/userguide/addusers.html) .

(structure)

The information that identifies the recipient.

ssoIdentity -> (structure)

The AWS Single Sign-On (AWS SSO) authentication information.

identityStoreId -> (string)

The ID of the AWS SSO identity store.

userId -> (string)

The user ID.

emailConfigurations -> (list)

Contains the configuration information of email notifications.

(structure)

Contains the configuration information of email notifications.

from -> (string)

The email address that sends emails.

### Warning

If you use the AWS IoT Events managed AWS Lambda function to manage your emails, you must [verify the email address that sends emails in Amazon SES](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/verify-email-addresses.html) .

content -> (structure)

Contains the subject and message of an email.

subject -> (string)

The subject of the email.

additionalMessage -> (string)

The message that you want to send. The message can be up to 200 characters.

recipients -> (structure)

Contains the information of one or more recipients who receive the emails.

### Warning

You must [add the users that receive emails to your AWS SSO store](https://docs.aws.amazon.com/singlesignon/latest/userguide/addusers.html) .

to -> (list)

Specifies one or more recipients who receive the email.

(structure)

The information that identifies the recipient.

ssoIdentity -> (structure)

The AWS Single Sign-On (AWS SSO) authentication information.

identityStoreId -> (string)

The ID of the AWS SSO identity store.

userId -> (string)

The user ID.

alarmEventActions -> (structure)

Contains information about one or more alarm actions.

alarmActions -> (list)

Specifies one or more supported actions to receive notifications when the alarm state changes.

(structure)

Specifies one of the following actions to receive notifications when the alarm state changes.

sns -> (structure)

Information required to publish the Amazon SNS message.

targetArn -> (string)

The ARN of the Amazon SNS target where the message is sent.

payload -> (structure)

You can configure the action payload when you send a message as an Amazon SNS push notification.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

iotTopicPublish -> (structure)

Information required to publish the MQTT message through the AWS IoT message broker.

mqttTopic -> (string)

The MQTT topic of the message. You can use a string expression that includes variables (`$variable.<variable-name>` ) and input values (`$input.<input-name>.<path-to-datum>` ) as the topic string.

payload -> (structure)

You can configure the action payload when you publish a message to an AWS IoT Core topic.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

lambda -> (structure)

Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action.

functionArn -> (string)

The ARN of the Lambda function that is executed.

payload -> (structure)

You can configure the action payload when you send a message to a Lambda function.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

iotEvents -> (structure)

Sends an AWS IoT Events input, passing in information about the detector model instance and the event that triggered the action.

inputName -> (string)

The name of the AWS IoT Events input where the data is sent.

payload -> (structure)

You can configure the action payload when you send a message to an AWS IoT Events input.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

sqs -> (structure)

Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue.

queueUrl -> (string)

The URL of the SQS queue where the data is written.

useBase64 -> (boolean)

Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE.

payload -> (structure)

You can configure the action payload when you send a message to an Amazon SQS queue.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

firehose -> (structure)

Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.

deliveryStreamName -> (string)

The name of the Kinesis Data Firehose delivery stream where the data is written.

separator -> (string)

A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: ânâ (newline), âtâ (tab), ârnâ (Windows newline), â,â (comma).

payload -> (structure)

You can configure the action payload when you send a message to an Amazon Kinesis Data Firehose delivery stream.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

dynamoDB -> (structure)

Defines an action to write to the Amazon DynamoDB table that you created. The standard action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html) . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify.

You must use expressions for all parameters in `DynamoDBAction` . The expressions accept literals, operators, functions, references, and substitution templates.

**Examples**

- For literal values, the expressions must contain single quotes. For example, the value for the `hashKeyType` parameter can be `'STRING'` .
- For references, you must specify either variables or input values. For example, the value for the `hashKeyField` parameter can be `$input.GreenhouseInput.name` .
- For a substitution template, you must use `${}` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates. In the following example, the value for the `hashKeyValue` parameter uses a substitution template.   `'${$input.GreenhouseInput.temperature * 6 / 5 + 32} in Fahrenheit'`
- For a string concatenation, you must use `+` . A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates. In the following example, the value for the `tableName` parameter uses a string concatenation.   `'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date`

For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *AWS IoT Events Developer Guide* .

If the defined payload type is a string, `DynamoDBAction` writes non-JSON data to the DynamoDB table as binary data. The DynamoDB console displays the data as Base64-encoded text. The value for the `payloadField` parameter is `<payload-field>_raw` .

hashKeyType -> (string)

The data type for the hash key (also called the partition key). You can specify the following values:

- `'STRING'` - The hash key is a string.
- `'NUMBER'` - The hash key is a number.

If you donât specify `hashKeyType` , the default value is `'STRING'` .

hashKeyField -> (string)

The name of the hash key (also called the partition key). The `hashKeyField` value must match the partition key of the target DynamoDB table.

hashKeyValue -> (string)

The value of the hash key (also called the partition key).

rangeKeyType -> (string)

The data type for the range key (also called the sort key), You can specify the following values:

- `'STRING'` - The range key is a string.
- `'NUMBER'` - The range key is number.

If you donât specify `rangeKeyField` , the default value is `'STRING'` .

rangeKeyField -> (string)

The name of the range key (also called the sort key). The `rangeKeyField` value must match the sort key of the target DynamoDB table.

rangeKeyValue -> (string)

The value of the range key (also called the sort key).

operation -> (string)

The type of operation to perform. You can specify the following values:

- `'INSERT'` - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.
- `'UPDATE'` - Update an existing item of the DynamoDB table with new data. This itemâs partition key must match the specified hash key. If you specified a range key, the range key must match the itemâs sort key.
- `'DELETE'` - Delete an existing item of the DynamoDB table. This itemâs partition key must match the specified hash key. If you specified a range key, the range key must match the itemâs sort key.

If you donât specify this parameter, AWS IoT Events triggers the `'INSERT'` operation.

payloadField -> (string)

The name of the DynamoDB column that receives the action payload.

If you donât specify this parameter, the name of the DynamoDB column is `payload` .

tableName -> (string)

The name of the DynamoDB table. The `tableName` value must match the table name of the target DynamoDB table.

payload -> (structure)

Information needed to configure the payload.

By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use `contentExpression` .

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

dynamoDBv2 -> (structure)

Defines an action to write to the Amazon DynamoDB table that you created. The default action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html) . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify.

You must use expressions for all parameters in `DynamoDBv2Action` . The expressions accept literals, operators, functions, references, and substitution templates.

**Examples**

- For literal values, the expressions must contain single quotes. For example, the value for the `tableName` parameter can be `'GreenhouseTemperatureTable'` .
- For references, you must specify either variables or input values. For example, the value for the `tableName` parameter can be `$variable.ddbtableName` .
- For a substitution template, you must use `${}` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates. In the following example, the value for the `contentExpression` parameter in `Payload` uses a substitution template.   `'{\"sensorID\": \"${$input.GreenhouseInput.sensor_id}\", \"temperature\": \"${$input.GreenhouseInput.temperature * 9 / 5 + 32}\"}'`
- For a string concatenation, you must use `+` . A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates. In the following example, the value for the `tableName` parameter uses a string concatenation.   `'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date`

For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *AWS IoT Events Developer Guide* .

The value for the `type` parameter in `Payload` must be `JSON` .

tableName -> (string)

The name of the DynamoDB table.

payload -> (structure)

Information needed to configure the payload.

By default, AWS IoT Events generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use `contentExpression` .

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

iotSiteWise -> (structure)

Sends information about the detector model instance and the event that triggered the action to a specified asset property in AWS IoT SiteWise.

You must use expressions for all parameters in `IotSiteWiseAction` . The expressions accept literals, operators, functions, references, and substitutions templates.

**Examples**

- For literal values, the expressions must contain single quotes. For example, the value for the `propertyAlias` parameter can be `'/company/windfarm/3/turbine/7/temperature'` .
- For references, you must specify either variables or input values. For example, the value for the `assetId` parameter can be `$input.TurbineInput.assetId1` .
- For a substitution template, you must use `${}` , and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates. In the following example, the value for the `propertyAlias` parameter uses a substitution template.   `'company/windfarm/${$input.TemperatureInput.sensorData.windfarmID}/turbine/ ${$input.TemperatureInput.sensorData.turbineID}/temperature'`

You must specify either `propertyAlias` or both `assetId` and `propertyId` to identify the target asset property in AWS IoT SiteWise.

For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *AWS IoT Events Developer Guide* .

entryId -> (string)

A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier.

assetId -> (string)

The ID of the asset that has the specified property.

propertyId -> (string)

The ID of the asset property.

propertyAlias -> (string)

The alias of the asset property.

propertyValue -> (structure)

The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information.

value -> (structure)

The value to send to an asset property.

stringValue -> (string)

The asset property value is a string. You must use an expression, and the evaluated result should be a string.

integerValue -> (string)

The asset property value is an integer. You must use an expression, and the evaluated result should be an integer.

doubleValue -> (string)

The asset property value is a double. You must use an expression, and the evaluated result should be a double.

booleanValue -> (string)

The asset property value is a Boolean value that must be `'TRUE'` or `'FALSE'` . You must use an expression, and the evaluated result should be a Boolean value.

timestamp -> (structure)

The timestamp associated with the asset property value. The default is the current event time.

timeInSeconds -> (string)

The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199.

offsetInNanos -> (string)

The nanosecond offset converted from `timeInSeconds` . The valid range is between 0-999999999.

quality -> (string)

The quality of the asset property value. The value must be `'GOOD'` , `'BAD'` , or `'UNCERTAIN'` .

alarmCapabilities -> (structure)

Contains the configuration information of alarm state changes.

initializationConfiguration -> (structure)

Specifies the default alarm state. The configuration applies to all alarms that were created based on this alarm model.

disabledOnInitialization -> (boolean)

The value must be `TRUE` or `FALSE` . If `FALSE` , all alarm instances created based on the alarm model are activated. The default value is `TRUE` .

acknowledgeFlow -> (structure)

Specifies whether to get notified for alarm state changes.

enabled -> (boolean)

The value must be `TRUE` or `FALSE` . If `TRUE` , you receive a notification when the alarm state changes. You must choose to acknowledge the notification before the alarm state can return to `NORMAL` . If `FALSE` , you wonât receive notifications. The alarm automatically changes to the `NORMAL` state when the input property value returns to the specified range.