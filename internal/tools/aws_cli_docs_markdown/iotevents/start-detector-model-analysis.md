# start-detector-model-analysisÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/start-detector-model-analysis.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/start-detector-model-analysis.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotevents](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotevents/index.html#cli-aws-iotevents) ]

# start-detector-model-analysis

## Description

Performs an analysis of your detector model. For more information, see [Troubleshooting a detector model](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-analyze-api.html) in the *AWS IoT Events Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotevents-2018-07-27/StartDetectorModelAnalysis)

## Synopsis

```
start-detector-model-analysis
--detector-model-definition <value>
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

`--detector-model-definition` (structure)

Information that defines how a detector operates.

states -> (list)

Information about the states of the detector.

(structure)

Information that defines a state of a detector.

stateName -> (string)

The name of the state.

onInput -> (structure)

When an input is received and the `condition` is TRUE, perform the specified `actions` .

events -> (list)

Specifies the actions performed when the `condition` evaluates to TRUE.

(structure)

Specifies the `actions` to be performed when the `condition` evaluates to TRUE.

eventName -> (string)

The name of the event.

condition -> (string)

Optional. The Boolean expression that, when TRUE, causes the `actions` to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).

actions -> (list)

The actions to be performed.

(structure)

An action to be performed when the `condition` is TRUE.

setVariable -> (structure)

Sets a variable to a specified value.

variableName -> (string)

The name of the variable.

value -> (string)

The new value of the variable.

sns -> (structure)

Sends an Amazon SNS message.

targetArn -> (string)

The ARN of the Amazon SNS target where the message is sent.

payload -> (structure)

You can configure the action payload when you send a message as an Amazon SNS push notification.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

iotTopicPublish -> (structure)

Publishes an MQTT message with the given topic to the AWS IoT message broker.

mqttTopic -> (string)

The MQTT topic of the message. You can use a string expression that includes variables (`$variable.<variable-name>` ) and input values (`$input.<input-name>.<path-to-datum>` ) as the topic string.

payload -> (structure)

You can configure the action payload when you publish a message to an AWS IoT Core topic.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

setTimer -> (structure)

Information needed to set the timer.

timerName -> (string)

The name of the timer.

seconds -> (integer)

The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.

durationExpression -> (string)

The duration of the timer, in seconds. You can use a string expression that includes numbers, variables (`$variable.<variable-name>` ), and input values (`$input.<input-name>.<path-to-datum>` ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.

clearTimer -> (structure)

Information needed to clear the timer.

timerName -> (string)

The name of the timer to clear.

resetTimer -> (structure)

Information needed to reset the timer.

timerName -> (string)

The name of the timer to reset.

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

Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.

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

Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html) . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *AWS IoT Events Developer Guide* .

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

Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html) . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *AWS IoT Events Developer Guide* .

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

Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .

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

transitionEvents -> (list)

Specifies the actions performed, and the next state entered, when a `condition` evaluates to TRUE.

(structure)

Specifies the actions performed and the next state entered when a `condition` evaluates to TRUE.

eventName -> (string)

The name of the transition event.

condition -> (string)

Required. A Boolean expression that when TRUE causes the actions to be performed and the `nextState` to be entered.

actions -> (list)

The actions to be performed.

(structure)

An action to be performed when the `condition` is TRUE.

setVariable -> (structure)

Sets a variable to a specified value.

variableName -> (string)

The name of the variable.

value -> (string)

The new value of the variable.

sns -> (structure)

Sends an Amazon SNS message.

targetArn -> (string)

The ARN of the Amazon SNS target where the message is sent.

payload -> (structure)

You can configure the action payload when you send a message as an Amazon SNS push notification.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

iotTopicPublish -> (structure)

Publishes an MQTT message with the given topic to the AWS IoT message broker.

mqttTopic -> (string)

The MQTT topic of the message. You can use a string expression that includes variables (`$variable.<variable-name>` ) and input values (`$input.<input-name>.<path-to-datum>` ) as the topic string.

payload -> (structure)

You can configure the action payload when you publish a message to an AWS IoT Core topic.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

setTimer -> (structure)

Information needed to set the timer.

timerName -> (string)

The name of the timer.

seconds -> (integer)

The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.

durationExpression -> (string)

The duration of the timer, in seconds. You can use a string expression that includes numbers, variables (`$variable.<variable-name>` ), and input values (`$input.<input-name>.<path-to-datum>` ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.

clearTimer -> (structure)

Information needed to clear the timer.

timerName -> (string)

The name of the timer to clear.

resetTimer -> (structure)

Information needed to reset the timer.

timerName -> (string)

The name of the timer to reset.

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

Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.

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

Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html) . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *AWS IoT Events Developer Guide* .

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

Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html) . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *AWS IoT Events Developer Guide* .

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

Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .

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

nextState -> (string)

The next state to enter.

onEnter -> (structure)

When entering this state, perform these `actions` if the `condition` is TRUE.

events -> (list)

Specifies the actions that are performed when the state is entered and the `condition` is `TRUE` .

(structure)

Specifies the `actions` to be performed when the `condition` evaluates to TRUE.

eventName -> (string)

The name of the event.

condition -> (string)

Optional. The Boolean expression that, when TRUE, causes the `actions` to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).

actions -> (list)

The actions to be performed.

(structure)

An action to be performed when the `condition` is TRUE.

setVariable -> (structure)

Sets a variable to a specified value.

variableName -> (string)

The name of the variable.

value -> (string)

The new value of the variable.

sns -> (structure)

Sends an Amazon SNS message.

targetArn -> (string)

The ARN of the Amazon SNS target where the message is sent.

payload -> (structure)

You can configure the action payload when you send a message as an Amazon SNS push notification.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

iotTopicPublish -> (structure)

Publishes an MQTT message with the given topic to the AWS IoT message broker.

mqttTopic -> (string)

The MQTT topic of the message. You can use a string expression that includes variables (`$variable.<variable-name>` ) and input values (`$input.<input-name>.<path-to-datum>` ) as the topic string.

payload -> (structure)

You can configure the action payload when you publish a message to an AWS IoT Core topic.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

setTimer -> (structure)

Information needed to set the timer.

timerName -> (string)

The name of the timer.

seconds -> (integer)

The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.

durationExpression -> (string)

The duration of the timer, in seconds. You can use a string expression that includes numbers, variables (`$variable.<variable-name>` ), and input values (`$input.<input-name>.<path-to-datum>` ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.

clearTimer -> (structure)

Information needed to clear the timer.

timerName -> (string)

The name of the timer to clear.

resetTimer -> (structure)

Information needed to reset the timer.

timerName -> (string)

The name of the timer to reset.

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

Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.

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

Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html) . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *AWS IoT Events Developer Guide* .

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

Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html) . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *AWS IoT Events Developer Guide* .

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

Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .

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

onExit -> (structure)

When exiting this state, perform these `actions` if the specified `condition` is `TRUE` .

events -> (list)

Specifies the `actions` that are performed when the state is exited and the `condition` is `TRUE` .

(structure)

Specifies the `actions` to be performed when the `condition` evaluates to TRUE.

eventName -> (string)

The name of the event.

condition -> (string)

Optional. The Boolean expression that, when TRUE, causes the `actions` to be performed. If not present, the actions are performed (=TRUE). If the expression result is not a Boolean value, the actions are not performed (=FALSE).

actions -> (list)

The actions to be performed.

(structure)

An action to be performed when the `condition` is TRUE.

setVariable -> (structure)

Sets a variable to a specified value.

variableName -> (string)

The name of the variable.

value -> (string)

The new value of the variable.

sns -> (structure)

Sends an Amazon SNS message.

targetArn -> (string)

The ARN of the Amazon SNS target where the message is sent.

payload -> (structure)

You can configure the action payload when you send a message as an Amazon SNS push notification.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

iotTopicPublish -> (structure)

Publishes an MQTT message with the given topic to the AWS IoT message broker.

mqttTopic -> (string)

The MQTT topic of the message. You can use a string expression that includes variables (`$variable.<variable-name>` ) and input values (`$input.<input-name>.<path-to-datum>` ) as the topic string.

payload -> (structure)

You can configure the action payload when you publish a message to an AWS IoT Core topic.

contentExpression -> (string)

The content of the payload. You can use a string expression that includes quoted strings (`'<string>'` ), variables (`$variable.<variable-name>` ), input values (`$input.<input-name>.<path-to-datum>` ), string concatenations, and quoted strings that contain `${}` as the content. The recommended maximum size of a content expression is 1 KB.

type -> (string)

The value of the payload type can be either `STRING` or `JSON` .

setTimer -> (structure)

Information needed to set the timer.

timerName -> (string)

The name of the timer.

seconds -> (integer)

The number of seconds until the timer expires. The minimum value is 60 seconds to ensure accuracy. The maximum value is 31622400 seconds.

durationExpression -> (string)

The duration of the timer, in seconds. You can use a string expression that includes numbers, variables (`$variable.<variable-name>` ), and input values (`$input.<input-name>.<path-to-datum>` ) as the duration. The range of the duration is 1-31622400 seconds. To ensure accuracy, the minimum duration is 60 seconds. The evaluated result of the duration is rounded down to the nearest whole number.

clearTimer -> (structure)

Information needed to clear the timer.

timerName -> (string)

The name of the timer to clear.

resetTimer -> (structure)

Information needed to reset the timer.

timerName -> (string)

The name of the timer to reset.

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

Sends AWS IoT Events input, which passes information about the detector model instance and the event that triggered the action.

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

Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html) . One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *AWS IoT Events Developer Guide* .

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

Writes to the DynamoDB table that you created. The default action payload contains all attribute-value pairs that have the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html) . A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify. For more information, see [Actions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-event-actions.html) in *AWS IoT Events Developer Guide* .

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

Sends information about the detector model instance and the event that triggered the action to an asset property in AWS IoT SiteWise .

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

initialStateName -> (string)

The state that is entered at the creation of each detector (instance).

JSON Syntax:

```
{
  "states": [
    {
      "stateName": "string",
      "onInput": {
        "events": [
          {
            "eventName": "string",
            "condition": "string",
            "actions": [
              {
                "setVariable": {
                  "variableName": "string",
                  "value": "string"
                },
                "sns": {
                  "targetArn": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotTopicPublish": {
                  "mqttTopic": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "setTimer": {
                  "timerName": "string",
                  "seconds": integer,
                  "durationExpression": "string"
                },
                "clearTimer": {
                  "timerName": "string"
                },
                "resetTimer": {
                  "timerName": "string"
                },
                "lambda": {
                  "functionArn": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotEvents": {
                  "inputName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "sqs": {
                  "queueUrl": "string",
                  "useBase64": true|false,
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "firehose": {
                  "deliveryStreamName": "string",
                  "separator": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "dynamoDB": {
                  "hashKeyType": "string",
                  "hashKeyField": "string",
                  "hashKeyValue": "string",
                  "rangeKeyType": "string",
                  "rangeKeyField": "string",
                  "rangeKeyValue": "string",
                  "operation": "string",
                  "payloadField": "string",
                  "tableName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "dynamoDBv2": {
                  "tableName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotSiteWise": {
                  "entryId": "string",
                  "assetId": "string",
                  "propertyId": "string",
                  "propertyAlias": "string",
                  "propertyValue": {
                    "value": {
                      "stringValue": "string",
                      "integerValue": "string",
                      "doubleValue": "string",
                      "booleanValue": "string"
                    },
                    "timestamp": {
                      "timeInSeconds": "string",
                      "offsetInNanos": "string"
                    },
                    "quality": "string"
                  }
                }
              }
              ...
            ]
          }
          ...
        ],
        "transitionEvents": [
          {
            "eventName": "string",
            "condition": "string",
            "actions": [
              {
                "setVariable": {
                  "variableName": "string",
                  "value": "string"
                },
                "sns": {
                  "targetArn": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotTopicPublish": {
                  "mqttTopic": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "setTimer": {
                  "timerName": "string",
                  "seconds": integer,
                  "durationExpression": "string"
                },
                "clearTimer": {
                  "timerName": "string"
                },
                "resetTimer": {
                  "timerName": "string"
                },
                "lambda": {
                  "functionArn": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotEvents": {
                  "inputName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "sqs": {
                  "queueUrl": "string",
                  "useBase64": true|false,
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "firehose": {
                  "deliveryStreamName": "string",
                  "separator": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "dynamoDB": {
                  "hashKeyType": "string",
                  "hashKeyField": "string",
                  "hashKeyValue": "string",
                  "rangeKeyType": "string",
                  "rangeKeyField": "string",
                  "rangeKeyValue": "string",
                  "operation": "string",
                  "payloadField": "string",
                  "tableName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "dynamoDBv2": {
                  "tableName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotSiteWise": {
                  "entryId": "string",
                  "assetId": "string",
                  "propertyId": "string",
                  "propertyAlias": "string",
                  "propertyValue": {
                    "value": {
                      "stringValue": "string",
                      "integerValue": "string",
                      "doubleValue": "string",
                      "booleanValue": "string"
                    },
                    "timestamp": {
                      "timeInSeconds": "string",
                      "offsetInNanos": "string"
                    },
                    "quality": "string"
                  }
                }
              }
              ...
            ],
            "nextState": "string"
          }
          ...
        ]
      },
      "onEnter": {
        "events": [
          {
            "eventName": "string",
            "condition": "string",
            "actions": [
              {
                "setVariable": {
                  "variableName": "string",
                  "value": "string"
                },
                "sns": {
                  "targetArn": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotTopicPublish": {
                  "mqttTopic": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "setTimer": {
                  "timerName": "string",
                  "seconds": integer,
                  "durationExpression": "string"
                },
                "clearTimer": {
                  "timerName": "string"
                },
                "resetTimer": {
                  "timerName": "string"
                },
                "lambda": {
                  "functionArn": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotEvents": {
                  "inputName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "sqs": {
                  "queueUrl": "string",
                  "useBase64": true|false,
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "firehose": {
                  "deliveryStreamName": "string",
                  "separator": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "dynamoDB": {
                  "hashKeyType": "string",
                  "hashKeyField": "string",
                  "hashKeyValue": "string",
                  "rangeKeyType": "string",
                  "rangeKeyField": "string",
                  "rangeKeyValue": "string",
                  "operation": "string",
                  "payloadField": "string",
                  "tableName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "dynamoDBv2": {
                  "tableName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotSiteWise": {
                  "entryId": "string",
                  "assetId": "string",
                  "propertyId": "string",
                  "propertyAlias": "string",
                  "propertyValue": {
                    "value": {
                      "stringValue": "string",
                      "integerValue": "string",
                      "doubleValue": "string",
                      "booleanValue": "string"
                    },
                    "timestamp": {
                      "timeInSeconds": "string",
                      "offsetInNanos": "string"
                    },
                    "quality": "string"
                  }
                }
              }
              ...
            ]
          }
          ...
        ]
      },
      "onExit": {
        "events": [
          {
            "eventName": "string",
            "condition": "string",
            "actions": [
              {
                "setVariable": {
                  "variableName": "string",
                  "value": "string"
                },
                "sns": {
                  "targetArn": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotTopicPublish": {
                  "mqttTopic": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "setTimer": {
                  "timerName": "string",
                  "seconds": integer,
                  "durationExpression": "string"
                },
                "clearTimer": {
                  "timerName": "string"
                },
                "resetTimer": {
                  "timerName": "string"
                },
                "lambda": {
                  "functionArn": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotEvents": {
                  "inputName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "sqs": {
                  "queueUrl": "string",
                  "useBase64": true|false,
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "firehose": {
                  "deliveryStreamName": "string",
                  "separator": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "dynamoDB": {
                  "hashKeyType": "string",
                  "hashKeyField": "string",
                  "hashKeyValue": "string",
                  "rangeKeyType": "string",
                  "rangeKeyField": "string",
                  "rangeKeyValue": "string",
                  "operation": "string",
                  "payloadField": "string",
                  "tableName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "dynamoDBv2": {
                  "tableName": "string",
                  "payload": {
                    "contentExpression": "string",
                    "type": "STRING"|"JSON"
                  }
                },
                "iotSiteWise": {
                  "entryId": "string",
                  "assetId": "string",
                  "propertyId": "string",
                  "propertyAlias": "string",
                  "propertyValue": {
                    "value": {
                      "stringValue": "string",
                      "integerValue": "string",
                      "doubleValue": "string",
                      "booleanValue": "string"
                    },
                    "timestamp": {
                      "timeInSeconds": "string",
                      "offsetInNanos": "string"
                    },
                    "quality": "string"
                  }
                }
              }
              ...
            ]
          }
          ...
        ]
      }
    }
    ...
  ],
  "initialStateName": "string"
}
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

analysisId -> (string)

The ID that you can use to retrieve the analysis result.