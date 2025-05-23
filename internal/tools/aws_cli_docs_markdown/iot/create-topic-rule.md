# create-topic-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-topic-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/create-topic-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# create-topic-rule

## Description

Creates a rule. Creating rules is an administrator-level action. Any user who has permission to create rules will be able to access data processed by the rule.

Requires permission to access the [CreateTopicRule](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/CreateTopicRule)

## Synopsis

```
create-topic-rule
--rule-name <value>
--topic-rule-payload <value>
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

`--rule-name` (string)

The name of the rule.

`--topic-rule-payload` (structure)

The rule payload.

sql -> (string)

The SQL statement used to query the topic. For more information, see [IoT SQL Reference](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-reference.html) in the *IoT Developer Guide* .

description -> (string)

The description of the rule.

actions -> (list)

The actions associated with the rule.

(structure)

Describes the actions associated with a rule.

dynamoDB -> (structure)

Write to a DynamoDB table.

tableName -> (string)

The name of the DynamoDB table.

roleArn -> (string)

The ARN of the IAM role that grants access to the DynamoDB table.

operation -> (string)

The type of operation to be performed. This follows the substitution template, so it can be `${operation}` , but the substitution must result in one of the following: `INSERT` , `UPDATE` , or `DELETE` .

hashKeyField -> (string)

The hash key name.

hashKeyValue -> (string)

The hash key value.

hashKeyType -> (string)

The hash key type. Valid values are âSTRINGâ or âNUMBERâ

rangeKeyField -> (string)

The range key name.

rangeKeyValue -> (string)

The range key value.

rangeKeyType -> (string)

The range key type. Valid values are âSTRINGâ or âNUMBERâ

payloadField -> (string)

The action payload. This name can be customized.

dynamoDBv2 -> (structure)

Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

roleArn -> (string)

The ARN of the IAM role that grants access to the DynamoDB table.

putItem -> (structure)

Specifies the DynamoDB table to which the message data will be written. For example:

`{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }`

Each attribute in the message payload will be written to a separate column in the DynamoDB database.

tableName -> (string)

The table where the message data will be written.

lambda -> (structure)

Invoke a Lambda function.

functionArn -> (string)

The ARN of the Lambda function.

sns -> (structure)

Publish to an Amazon SNS topic.

targetArn -> (string)

The ARN of the SNS topic.

roleArn -> (string)

The ARN of the IAM role that grants access.

messageFormat -> (string)

(Optional) The message format of the message to publish. Accepted values are âJSONâ and âRAWâ. The default value of the attribute is âRAWâ. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see [https://docs.aws.amazon.com/sns/latest/dg/json-formats.html](https://docs.aws.amazon.com/sns/latest/dg/json-formats.html) refer to their official documentation.

sqs -> (structure)

Publish to an Amazon SQS queue.

roleArn -> (string)

The ARN of the IAM role that grants access.

queueUrl -> (string)

The URL of the Amazon SQS queue.

useBase64 -> (boolean)

Specifies whether to use Base64 encoding.

kinesis -> (structure)

Write data to an Amazon Kinesis stream.

roleArn -> (string)

The ARN of the IAM role that grants access to the Amazon Kinesis stream.

streamName -> (string)

The name of the Amazon Kinesis stream.

partitionKey -> (string)

The partition key.

republish -> (structure)

Publish to another MQTT topic.

roleArn -> (string)

The ARN of the IAM role that grants access.

topic -> (string)

The name of the MQTT topic.

qos -> (integer)

The Quality of Service (QoS) level to use when republishing messages. The default value is 0.

headers -> (structure)

MQTT Version 5.0 headers information. For more information, see [MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) from the Amazon Web Services IoT Core Developer Guide.

payloadFormatIndicator -> (string)

An `Enum` string value that indicates whether the payload is formatted as UTF-8.

Valid values are `UNSPECIFIED_BYTES` and `UTF8_DATA` .

For more information, see [Payload Format Indicator](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901111) from the MQTT Version 5.0 specification.

Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

contentType -> (string)

A UTF-8 encoded string that describes the content of the publishing message.

For more information, see [Content Type](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901118) from the MQTT Version 5.0 specification.

Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

responseTopic -> (string)

A UTF-8 encoded string thatâs used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.

For more information, see [Response Topic](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901114) from the MQTT Version 5.0 specification.

Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

correlationData -> (string)

The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when itâs received.

For more information, see [Correlation Data](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901115) from the MQTT Version 5.0 specification.

### Note

This binary data must be based64-encoded.

Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

messageExpiry -> (string)

A user-defined integer value that will persist a message at the message broker for a specified amount of time to ensure that the message will expire if itâs no longer relevant to the subscriber. The value of `messageExpiry` represents the number of seconds before it expires. For more information about the limits of `messageExpiry` , see [Amazon Web Services IoT Core message broker and protocol limits and quotas](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) from the Amazon Web Services Reference Guide.

Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

userProperties -> (list)

An array of key-value pairs that you define in the MQTT5 header.

(structure)

A key-value pair that you define in the header. Both the key and the value are either literal strings or valid [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

key -> (string)

A key to be specified in `UserProperty` .

value -> (string)

A value to be specified in `UserProperty` .

s3 -> (structure)

Write to an Amazon S3 bucket.

roleArn -> (string)

The ARN of the IAM role that grants access.

bucketName -> (string)

The Amazon S3 bucket.

key -> (string)

The object key. For more information, see [Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html) .

cannedAcl -> (string)

The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see [S3 canned ACLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) .

firehose -> (structure)

Write to an Amazon Kinesis Firehose stream.

roleArn -> (string)

The IAM role that grants access to the Amazon Kinesis Firehose stream.

deliveryStreamName -> (string)

The delivery stream name.

separator -> (string)

A character separator that will be used to separate records written to the Firehose stream. Valid values are: ânâ (newline), âtâ (tab), ârnâ (Windows newline), â,â (comma).

batchMode -> (boolean)

Whether to deliver the Kinesis Data Firehose stream as a batch by using ` `PutRecordBatch` [https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch).html`__ . The default value is `false` .

When `batchMode` is `true` and the ruleâs SQL statement evaluates to an Array, each Array element forms one record in the ` `PutRecordBatch` [https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch).html`__ request. The resulting array canât have more than 500 records.

cloudwatchMetric -> (structure)

Capture a CloudWatch metric.

roleArn -> (string)

The IAM role that allows access to the CloudWatch metric.

metricNamespace -> (string)

The CloudWatch metric namespace name.

metricName -> (string)

The CloudWatch metric name.

metricValue -> (string)

The CloudWatch metric value.

metricUnit -> (string)

The [metric unit](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit) supported by CloudWatch.

metricTimestamp -> (string)

An optional [Unix timestamp](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp) .

cloudwatchAlarm -> (structure)

Change the state of a CloudWatch alarm.

roleArn -> (string)

The IAM role that allows access to the CloudWatch alarm.

alarmName -> (string)

The CloudWatch alarm name.

stateReason -> (string)

The reason for the alarm change.

stateValue -> (string)

The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

cloudwatchLogs -> (structure)

Send data to CloudWatch Logs.

roleArn -> (string)

The IAM role that allows access to the CloudWatch log.

logGroupName -> (string)

The CloudWatch log group to which the action sends data.

batchMode -> (boolean)

Indicates whether batches of log records will be extracted and uploaded into CloudWatch. Values include `true` or `false` *(default)* .

elasticsearch -> (structure)

Write data to an Amazon OpenSearch Service domain.

### Note

The `Elasticsearch` action can only be used by existing rule actions. To create a new rule action or to update an existing rule action, use the `OpenSearch` rule action instead. For more information, see [OpenSearchAction](https://docs.aws.amazon.com/iot/latest/apireference/API_OpenSearchAction.html) .

roleArn -> (string)

The IAM role ARN that has access to OpenSearch.

endpoint -> (string)

The endpoint of your OpenSearch domain.

index -> (string)

The index where you want to store your data.

type -> (string)

The type of document you are storing.

id -> (string)

The unique identifier for the document you are storing.

salesforce -> (structure)

Send a message to a Salesforce IoT Cloud Input Stream.

token -> (string)

The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

url -> (string)

The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

iotAnalytics -> (structure)

Sends message data to an IoT Analytics channel.

channelArn -> (string)

(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

channelName -> (string)

The name of the IoT Analytics channel to which message data will be sent.

batchMode -> (boolean)

Whether to process the action as a batch. The default value is `false` .

When `batchMode` is `true` and the rule SQL statement evaluates to an Array, each Array element is delivered as a separate message when passed by ` `BatchPutMessage` [https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage).html`__ to the IoT Analytics channel. The resulting array canât have more than 100 messages.

roleArn -> (string)

The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).

iotEvents -> (structure)

Sends an input to an IoT Events detector.

inputName -> (string)

The name of the IoT Events input.

messageId -> (string)

The ID of the message. The default `messageId` is a new UUID value.

When `batchMode` is `true` , you canât specify a `messageId` âa new UUID value will be assigned.

Assign a value to this property to ensure that only one input (message) with a given `messageId` will be processed by an IoT Events detector.

batchMode -> (boolean)

Whether to process the event actions as a batch. The default value is `false` .

When `batchMode` is `true` , you canât specify a `messageId` .

When `batchMode` is `true` and the rule SQL statement evaluates to an Array, each Array element is treated as a separate message when itâs sent to IoT Events by calling ` `BatchPutMessage` [https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage).html`__ . The resulting array canât have more than 10 messages.

roleArn -> (string)

The ARN of the role that grants IoT permission to send an input to an IoT Events detector. (âActionâ:âiotevents:BatchPutMessageâ).

iotSiteWise -> (structure)

Sends data from the MQTT message that triggered the rule to IoT SiteWise asset properties.

putAssetPropertyValueEntries -> (list)

A list of asset property value entries.

(structure)

An asset property value entry containing the following information.

entryId -> (string)

Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.

assetId -> (string)

The ID of the IoT SiteWise asset. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId` . Accepts substitution templates.

propertyId -> (string)

The ID of the assetâs property. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId` . Accepts substitution templates.

propertyAlias -> (string)

The name of the property alias associated with your asset property. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId` . Accepts substitution templates.

propertyValues -> (list)

A list of property values to insert that each contain timestamp, quality, and value (TQV) information.

(structure)

An asset property value entry containing the following information.

value -> (structure)

The value of the asset property.

stringValue -> (string)

Optional. The string value of the value entry. Accepts substitution templates.

integerValue -> (string)

Optional. A string that contains the integer value of the value entry. Accepts substitution templates.

doubleValue -> (string)

Optional. A string that contains the double value of the value entry. Accepts substitution templates.

booleanValue -> (string)

Optional. A string that contains the boolean value (`true` or `false` ) of the value entry. Accepts substitution templates.

timestamp -> (structure)

The asset property value timestamp.

timeInSeconds -> (string)

A string that contains the time in seconds since epoch. Accepts substitution templates.

offsetInNanos -> (string)

Optional. A string that contains the nanosecond time offset. Accepts substitution templates.

quality -> (string)

Optional. A string that describes the quality of the value. Accepts substitution templates. Must be `GOOD` , `BAD` , or `UNCERTAIN` .

roleArn -> (string)

The ARN of the role that grants IoT permission to send an asset property value to IoT SiteWise. (`"Action": "iotsitewise:BatchPutAssetPropertyValue"` ). The trust policy can restrict access to specific asset hierarchy paths.

stepFunctions -> (structure)

Starts execution of a Step Functions state machine.

executionNamePrefix -> (string)

(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.

stateMachineName -> (string)

The name of the Step Functions state machine whose execution will be started.

roleArn -> (string)

The ARN of the role that grants IoT permission to start execution of a state machine (âActionâ:âstates:StartExecutionâ).

timestream -> (structure)

The Timestream rule action writes attributes (measures) from an MQTT message into an Amazon Timestream table. For more information, see the [Timestream](https://docs.aws.amazon.com/iot/latest/developerguide/timestream-rule-action.html) topic rule action documentation.

roleArn -> (string)

The ARN of the role that grants permission to write to the Amazon Timestream database table.

databaseName -> (string)

The name of an Amazon Timestream database.

tableName -> (string)

The name of the database table into which to write the measure records.

dimensions -> (list)

Metadata attributes of the time series that are written in each measure record.

(structure)

Metadata attributes of the time series that are written in each measure record.

name -> (string)

The metadata dimension name. This is the name of the column in the Amazon Timestream database table record.

Dimensions cannot be named: `measure_name` , `measure_value` , or `time` . These names are reserved. Dimension names cannot start with `ts_` or `measure_value` and they cannot contain the colon (`:` ) character.

value -> (string)

The value to write in this column of the database record.

timestamp -> (structure)

Specifies an application-defined value to replace the default value assigned to the Timestream recordâs timestamp in the `time` column.

You can use this property to specify the value and the precision of the Timestream recordâs timestamp. You can specify a value from the message payload or a value computed by a substitution template.

If omitted, the topic rule action assigns the timestamp, in milliseconds, at the time it processed the rule.

value -> (string)

An expression that returns a long epoch time value.

unit -> (string)

The precision of the timestamp value that results from the expression described in `value` .

Valid values: `SECONDS` | `MILLISECONDS` | `MICROSECONDS` | `NANOSECONDS` . The default is `MILLISECONDS` .

http -> (structure)

Send data to an HTTPS endpoint.

url -> (string)

The endpoint URL. If substitution templates are used in the URL, you must also specify a `confirmationUrl` . If this is a new destination, a new `TopicRuleDestination` is created if possible.

confirmationUrl -> (string)

The URL to which IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.

headers -> (list)

The HTTP headers to send with the message data.

(structure)

The HTTP action header.

key -> (string)

The HTTP header key.

value -> (string)

The HTTP header value. Substitution templates are supported.

auth -> (structure)

The authentication method to use when sending data to an HTTPS endpoint.

sigv4 -> (structure)

Use Sig V4 authorization. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) .

signingRegion -> (string)

The signing region.

serviceName -> (string)

The service name to use while signing with Sig V4.

roleArn -> (string)

The ARN of the signing role.

kafka -> (structure)

Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.

destinationArn -> (string)

The ARN of Kafka actionâs VPC `TopicRuleDestination` .

topic -> (string)

The Kafka topic for messages to be sent to the Kafka broker.

key -> (string)

The Kafka message key.

partition -> (string)

The Kafka message partition.

clientProperties -> (map)

Properties of the Apache Kafka producer client.

key -> (string)

value -> (string)

headers -> (list)

The list of Kafka headers that you specify.

(structure)

Specifies a Kafka header using key-value pairs when you create a Ruleâs Kafka Action. You can use these headers to route data from IoT clients to downstream Kafka clusters without modifying your message payload.

For more information about Ruleâs Kafka action, see [Apache Kafka](https://docs.aws.amazon.com/iot/latest/developerguide/apache-kafka-rule-action.html) .

key -> (string)

The key of the Kafka header.

value -> (string)

The value of the Kafka header.

openSearch -> (structure)

Write data to an Amazon OpenSearch Service domain.

roleArn -> (string)

The IAM role ARN that has access to OpenSearch.

endpoint -> (string)

The endpoint of your OpenSearch domain.

index -> (string)

The OpenSearch index where you want to store your data.

type -> (string)

The type of document you are storing.

id -> (string)

The unique identifier for the document you are storing.

location -> (structure)

The Amazon Location Service rule action sends device location updates from an MQTT message to an Amazon Location tracker resource.

roleArn -> (string)

The IAM role that grants permission to write to the Amazon Location resource.

trackerName -> (string)

The name of the tracker resource in Amazon Location in which the location is updated.

deviceId -> (string)

The unique ID of the device providing the location data.

timestamp -> (structure)

The time that the location data was sampled. The default value is the time the MQTT message was processed.

value -> (string)

An expression that returns a long epoch time value.

unit -> (string)

The precision of the timestamp value that results from the expression described in `value` .

Valid values: `SECONDS` | `MILLISECONDS` | `MICROSECONDS` | `NANOSECONDS` . The default is `MILLISECONDS` .

latitude -> (string)

A string that evaluates to a double value that represents the latitude of the deviceâs location.

longitude -> (string)

A string that evaluates to a double value that represents the longitude of the deviceâs location.

ruleDisabled -> (boolean)

Specifies whether the rule is disabled.

awsIotSqlVersion -> (string)

The version of the SQL rules engine to use when evaluating the rule.

errorAction -> (structure)

The action to take when an error occurs.

dynamoDB -> (structure)

Write to a DynamoDB table.

tableName -> (string)

The name of the DynamoDB table.

roleArn -> (string)

The ARN of the IAM role that grants access to the DynamoDB table.

operation -> (string)

The type of operation to be performed. This follows the substitution template, so it can be `${operation}` , but the substitution must result in one of the following: `INSERT` , `UPDATE` , or `DELETE` .

hashKeyField -> (string)

The hash key name.

hashKeyValue -> (string)

The hash key value.

hashKeyType -> (string)

The hash key type. Valid values are âSTRINGâ or âNUMBERâ

rangeKeyField -> (string)

The range key name.

rangeKeyValue -> (string)

The range key value.

rangeKeyType -> (string)

The range key type. Valid values are âSTRINGâ or âNUMBERâ

payloadField -> (string)

The action payload. This name can be customized.

dynamoDBv2 -> (structure)

Write to a DynamoDB table. This is a new version of the DynamoDB action. It allows you to write each attribute in an MQTT message payload into a separate DynamoDB column.

roleArn -> (string)

The ARN of the IAM role that grants access to the DynamoDB table.

putItem -> (structure)

Specifies the DynamoDB table to which the message data will be written. For example:

`{ "dynamoDBv2": { "roleArn": "aws:iam:12341251:my-role" "putItem": { "tableName": "my-table" } } }`

Each attribute in the message payload will be written to a separate column in the DynamoDB database.

tableName -> (string)

The table where the message data will be written.

lambda -> (structure)

Invoke a Lambda function.

functionArn -> (string)

The ARN of the Lambda function.

sns -> (structure)

Publish to an Amazon SNS topic.

targetArn -> (string)

The ARN of the SNS topic.

roleArn -> (string)

The ARN of the IAM role that grants access.

messageFormat -> (string)

(Optional) The message format of the message to publish. Accepted values are âJSONâ and âRAWâ. The default value of the attribute is âRAWâ. SNS uses this setting to determine if the payload should be parsed and relevant platform-specific bits of the payload should be extracted. To read more about SNS message formats, see [https://docs.aws.amazon.com/sns/latest/dg/json-formats.html](https://docs.aws.amazon.com/sns/latest/dg/json-formats.html) refer to their official documentation.

sqs -> (structure)

Publish to an Amazon SQS queue.

roleArn -> (string)

The ARN of the IAM role that grants access.

queueUrl -> (string)

The URL of the Amazon SQS queue.

useBase64 -> (boolean)

Specifies whether to use Base64 encoding.

kinesis -> (structure)

Write data to an Amazon Kinesis stream.

roleArn -> (string)

The ARN of the IAM role that grants access to the Amazon Kinesis stream.

streamName -> (string)

The name of the Amazon Kinesis stream.

partitionKey -> (string)

The partition key.

republish -> (structure)

Publish to another MQTT topic.

roleArn -> (string)

The ARN of the IAM role that grants access.

topic -> (string)

The name of the MQTT topic.

qos -> (integer)

The Quality of Service (QoS) level to use when republishing messages. The default value is 0.

headers -> (structure)

MQTT Version 5.0 headers information. For more information, see [MQTT](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) from the Amazon Web Services IoT Core Developer Guide.

payloadFormatIndicator -> (string)

An `Enum` string value that indicates whether the payload is formatted as UTF-8.

Valid values are `UNSPECIFIED_BYTES` and `UTF8_DATA` .

For more information, see [Payload Format Indicator](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901111) from the MQTT Version 5.0 specification.

Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

contentType -> (string)

A UTF-8 encoded string that describes the content of the publishing message.

For more information, see [Content Type](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901118) from the MQTT Version 5.0 specification.

Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

responseTopic -> (string)

A UTF-8 encoded string thatâs used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.

For more information, see [Response Topic](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901114) from the MQTT Version 5.0 specification.

Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

correlationData -> (string)

The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when itâs received.

For more information, see [Correlation Data](https://docs.oasis-open.org/mqtt/mqtt/v5.0/os/mqtt-v5.0-os.html#_Toc3901115) from the MQTT Version 5.0 specification.

### Note

This binary data must be based64-encoded.

Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

messageExpiry -> (string)

A user-defined integer value that will persist a message at the message broker for a specified amount of time to ensure that the message will expire if itâs no longer relevant to the subscriber. The value of `messageExpiry` represents the number of seconds before it expires. For more information about the limits of `messageExpiry` , see [Amazon Web Services IoT Core message broker and protocol limits and quotas](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) from the Amazon Web Services Reference Guide.

Supports [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

userProperties -> (list)

An array of key-value pairs that you define in the MQTT5 header.

(structure)

A key-value pair that you define in the header. Both the key and the value are either literal strings or valid [substitution templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html) .

key -> (string)

A key to be specified in `UserProperty` .

value -> (string)

A value to be specified in `UserProperty` .

s3 -> (structure)

Write to an Amazon S3 bucket.

roleArn -> (string)

The ARN of the IAM role that grants access.

bucketName -> (string)

The Amazon S3 bucket.

key -> (string)

The object key. For more information, see [Actions, resources, and condition keys for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/list_amazons3.html) .

cannedAcl -> (string)

The Amazon S3 canned ACL that controls access to the object identified by the object key. For more information, see [S3 canned ACLs](https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl) .

firehose -> (structure)

Write to an Amazon Kinesis Firehose stream.

roleArn -> (string)

The IAM role that grants access to the Amazon Kinesis Firehose stream.

deliveryStreamName -> (string)

The delivery stream name.

separator -> (string)

A character separator that will be used to separate records written to the Firehose stream. Valid values are: ânâ (newline), âtâ (tab), ârnâ (Windows newline), â,â (comma).

batchMode -> (boolean)

Whether to deliver the Kinesis Data Firehose stream as a batch by using ` `PutRecordBatch` [https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch).html`__ . The default value is `false` .

When `batchMode` is `true` and the ruleâs SQL statement evaluates to an Array, each Array element forms one record in the ` `PutRecordBatch` [https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch](https://docs.aws.amazon.com/firehose/latest/APIReference/API_PutRecordBatch).html`__ request. The resulting array canât have more than 500 records.

cloudwatchMetric -> (structure)

Capture a CloudWatch metric.

roleArn -> (string)

The IAM role that allows access to the CloudWatch metric.

metricNamespace -> (string)

The CloudWatch metric namespace name.

metricName -> (string)

The CloudWatch metric name.

metricValue -> (string)

The CloudWatch metric value.

metricUnit -> (string)

The [metric unit](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#Unit) supported by CloudWatch.

metricTimestamp -> (string)

An optional [Unix timestamp](https://docs.aws.amazon.com/AmazonCloudWatch/latest/DeveloperGuide/cloudwatch_concepts.html#about_timestamp) .

cloudwatchAlarm -> (structure)

Change the state of a CloudWatch alarm.

roleArn -> (string)

The IAM role that allows access to the CloudWatch alarm.

alarmName -> (string)

The CloudWatch alarm name.

stateReason -> (string)

The reason for the alarm change.

stateValue -> (string)

The value of the alarm state. Acceptable values are: OK, ALARM, INSUFFICIENT_DATA.

cloudwatchLogs -> (structure)

Send data to CloudWatch Logs.

roleArn -> (string)

The IAM role that allows access to the CloudWatch log.

logGroupName -> (string)

The CloudWatch log group to which the action sends data.

batchMode -> (boolean)

Indicates whether batches of log records will be extracted and uploaded into CloudWatch. Values include `true` or `false` *(default)* .

elasticsearch -> (structure)

Write data to an Amazon OpenSearch Service domain.

### Note

The `Elasticsearch` action can only be used by existing rule actions. To create a new rule action or to update an existing rule action, use the `OpenSearch` rule action instead. For more information, see [OpenSearchAction](https://docs.aws.amazon.com/iot/latest/apireference/API_OpenSearchAction.html) .

roleArn -> (string)

The IAM role ARN that has access to OpenSearch.

endpoint -> (string)

The endpoint of your OpenSearch domain.

index -> (string)

The index where you want to store your data.

type -> (string)

The type of document you are storing.

id -> (string)

The unique identifier for the document you are storing.

salesforce -> (structure)

Send a message to a Salesforce IoT Cloud Input Stream.

token -> (string)

The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

url -> (string)

The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.

iotAnalytics -> (structure)

Sends message data to an IoT Analytics channel.

channelArn -> (string)

(deprecated) The ARN of the IoT Analytics channel to which message data will be sent.

channelName -> (string)

The name of the IoT Analytics channel to which message data will be sent.

batchMode -> (boolean)

Whether to process the action as a batch. The default value is `false` .

When `batchMode` is `true` and the rule SQL statement evaluates to an Array, each Array element is delivered as a separate message when passed by ` `BatchPutMessage` [https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage](https://docs.aws.amazon.com/iotanalytics/latest/APIReference/API_BatchPutMessage).html`__ to the IoT Analytics channel. The resulting array canât have more than 100 messages.

roleArn -> (string)

The ARN of the role which has a policy that grants IoT Analytics permission to send message data via IoT Analytics (iotanalytics:BatchPutMessage).

iotEvents -> (structure)

Sends an input to an IoT Events detector.

inputName -> (string)

The name of the IoT Events input.

messageId -> (string)

The ID of the message. The default `messageId` is a new UUID value.

When `batchMode` is `true` , you canât specify a `messageId` âa new UUID value will be assigned.

Assign a value to this property to ensure that only one input (message) with a given `messageId` will be processed by an IoT Events detector.

batchMode -> (boolean)

Whether to process the event actions as a batch. The default value is `false` .

When `batchMode` is `true` , you canât specify a `messageId` .

When `batchMode` is `true` and the rule SQL statement evaluates to an Array, each Array element is treated as a separate message when itâs sent to IoT Events by calling ` `BatchPutMessage` [https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage](https://docs.aws.amazon.com/iotevents/latest/apireference/API_iotevents-data_BatchPutMessage).html`__ . The resulting array canât have more than 10 messages.

roleArn -> (string)

The ARN of the role that grants IoT permission to send an input to an IoT Events detector. (âActionâ:âiotevents:BatchPutMessageâ).

iotSiteWise -> (structure)

Sends data from the MQTT message that triggered the rule to IoT SiteWise asset properties.

putAssetPropertyValueEntries -> (list)

A list of asset property value entries.

(structure)

An asset property value entry containing the following information.

entryId -> (string)

Optional. A unique identifier for this entry that you can define to better track which message caused an error in case of failure. Accepts substitution templates. Defaults to a new UUID.

assetId -> (string)

The ID of the IoT SiteWise asset. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId` . Accepts substitution templates.

propertyId -> (string)

The ID of the assetâs property. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId` . Accepts substitution templates.

propertyAlias -> (string)

The name of the property alias associated with your asset property. You must specify either a `propertyAlias` or both an `aliasId` and a `propertyId` . Accepts substitution templates.

propertyValues -> (list)

A list of property values to insert that each contain timestamp, quality, and value (TQV) information.

(structure)

An asset property value entry containing the following information.

value -> (structure)

The value of the asset property.

stringValue -> (string)

Optional. The string value of the value entry. Accepts substitution templates.

integerValue -> (string)

Optional. A string that contains the integer value of the value entry. Accepts substitution templates.

doubleValue -> (string)

Optional. A string that contains the double value of the value entry. Accepts substitution templates.

booleanValue -> (string)

Optional. A string that contains the boolean value (`true` or `false` ) of the value entry. Accepts substitution templates.

timestamp -> (structure)

The asset property value timestamp.

timeInSeconds -> (string)

A string that contains the time in seconds since epoch. Accepts substitution templates.

offsetInNanos -> (string)

Optional. A string that contains the nanosecond time offset. Accepts substitution templates.

quality -> (string)

Optional. A string that describes the quality of the value. Accepts substitution templates. Must be `GOOD` , `BAD` , or `UNCERTAIN` .

roleArn -> (string)

The ARN of the role that grants IoT permission to send an asset property value to IoT SiteWise. (`"Action": "iotsitewise:BatchPutAssetPropertyValue"` ). The trust policy can restrict access to specific asset hierarchy paths.

stepFunctions -> (structure)

Starts execution of a Step Functions state machine.

executionNamePrefix -> (string)

(Optional) A name will be given to the state machine execution consisting of this prefix followed by a UUID. Step Functions automatically creates a unique name for each state machine execution if one is not provided.

stateMachineName -> (string)

The name of the Step Functions state machine whose execution will be started.

roleArn -> (string)

The ARN of the role that grants IoT permission to start execution of a state machine (âActionâ:âstates:StartExecutionâ).

timestream -> (structure)

The Timestream rule action writes attributes (measures) from an MQTT message into an Amazon Timestream table. For more information, see the [Timestream](https://docs.aws.amazon.com/iot/latest/developerguide/timestream-rule-action.html) topic rule action documentation.

roleArn -> (string)

The ARN of the role that grants permission to write to the Amazon Timestream database table.

databaseName -> (string)

The name of an Amazon Timestream database.

tableName -> (string)

The name of the database table into which to write the measure records.

dimensions -> (list)

Metadata attributes of the time series that are written in each measure record.

(structure)

Metadata attributes of the time series that are written in each measure record.

name -> (string)

The metadata dimension name. This is the name of the column in the Amazon Timestream database table record.

Dimensions cannot be named: `measure_name` , `measure_value` , or `time` . These names are reserved. Dimension names cannot start with `ts_` or `measure_value` and they cannot contain the colon (`:` ) character.

value -> (string)

The value to write in this column of the database record.

timestamp -> (structure)

Specifies an application-defined value to replace the default value assigned to the Timestream recordâs timestamp in the `time` column.

You can use this property to specify the value and the precision of the Timestream recordâs timestamp. You can specify a value from the message payload or a value computed by a substitution template.

If omitted, the topic rule action assigns the timestamp, in milliseconds, at the time it processed the rule.

value -> (string)

An expression that returns a long epoch time value.

unit -> (string)

The precision of the timestamp value that results from the expression described in `value` .

Valid values: `SECONDS` | `MILLISECONDS` | `MICROSECONDS` | `NANOSECONDS` . The default is `MILLISECONDS` .

http -> (structure)

Send data to an HTTPS endpoint.

url -> (string)

The endpoint URL. If substitution templates are used in the URL, you must also specify a `confirmationUrl` . If this is a new destination, a new `TopicRuleDestination` is created if possible.

confirmationUrl -> (string)

The URL to which IoT sends a confirmation message. The value of the confirmation URL must be a prefix of the endpoint URL. If you do not specify a confirmation URL IoT uses the endpoint URL as the confirmation URL. If you use substitution templates in the confirmationUrl, you must create and enable topic rule destinations that match each possible value of the substitution template before traffic is allowed to your endpoint URL.

headers -> (list)

The HTTP headers to send with the message data.

(structure)

The HTTP action header.

key -> (string)

The HTTP header key.

value -> (string)

The HTTP header value. Substitution templates are supported.

auth -> (structure)

The authentication method to use when sending data to an HTTPS endpoint.

sigv4 -> (structure)

Use Sig V4 authorization. For more information, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) .

signingRegion -> (string)

The signing region.

serviceName -> (string)

The service name to use while signing with Sig V4.

roleArn -> (string)

The ARN of the signing role.

kafka -> (structure)

Send messages to an Amazon Managed Streaming for Apache Kafka (Amazon MSK) or self-managed Apache Kafka cluster.

destinationArn -> (string)

The ARN of Kafka actionâs VPC `TopicRuleDestination` .

topic -> (string)

The Kafka topic for messages to be sent to the Kafka broker.

key -> (string)

The Kafka message key.

partition -> (string)

The Kafka message partition.

clientProperties -> (map)

Properties of the Apache Kafka producer client.

key -> (string)

value -> (string)

headers -> (list)

The list of Kafka headers that you specify.

(structure)

Specifies a Kafka header using key-value pairs when you create a Ruleâs Kafka Action. You can use these headers to route data from IoT clients to downstream Kafka clusters without modifying your message payload.

For more information about Ruleâs Kafka action, see [Apache Kafka](https://docs.aws.amazon.com/iot/latest/developerguide/apache-kafka-rule-action.html) .

key -> (string)

The key of the Kafka header.

value -> (string)

The value of the Kafka header.

openSearch -> (structure)

Write data to an Amazon OpenSearch Service domain.

roleArn -> (string)

The IAM role ARN that has access to OpenSearch.

endpoint -> (string)

The endpoint of your OpenSearch domain.

index -> (string)

The OpenSearch index where you want to store your data.

type -> (string)

The type of document you are storing.

id -> (string)

The unique identifier for the document you are storing.

location -> (structure)

The Amazon Location Service rule action sends device location updates from an MQTT message to an Amazon Location tracker resource.

roleArn -> (string)

The IAM role that grants permission to write to the Amazon Location resource.

trackerName -> (string)

The name of the tracker resource in Amazon Location in which the location is updated.

deviceId -> (string)

The unique ID of the device providing the location data.

timestamp -> (structure)

The time that the location data was sampled. The default value is the time the MQTT message was processed.

value -> (string)

An expression that returns a long epoch time value.

unit -> (string)

The precision of the timestamp value that results from the expression described in `value` .

Valid values: `SECONDS` | `MILLISECONDS` | `MICROSECONDS` | `NANOSECONDS` . The default is `MILLISECONDS` .

latitude -> (string)

A string that evaluates to a double value that represents the latitude of the deviceâs location.

longitude -> (string)

A string that evaluates to a double value that represents the longitude of the deviceâs location.

JSON Syntax:

```
{
  "sql": "string",
  "description": "string",
  "actions": [
    {
      "dynamoDB": {
        "tableName": "string",
        "roleArn": "string",
        "operation": "string",
        "hashKeyField": "string",
        "hashKeyValue": "string",
        "hashKeyType": "STRING"|"NUMBER",
        "rangeKeyField": "string",
        "rangeKeyValue": "string",
        "rangeKeyType": "STRING"|"NUMBER",
        "payloadField": "string"
      },
      "dynamoDBv2": {
        "roleArn": "string",
        "putItem": {
          "tableName": "string"
        }
      },
      "lambda": {
        "functionArn": "string"
      },
      "sns": {
        "targetArn": "string",
        "roleArn": "string",
        "messageFormat": "RAW"|"JSON"
      },
      "sqs": {
        "roleArn": "string",
        "queueUrl": "string",
        "useBase64": true|false
      },
      "kinesis": {
        "roleArn": "string",
        "streamName": "string",
        "partitionKey": "string"
      },
      "republish": {
        "roleArn": "string",
        "topic": "string",
        "qos": integer,
        "headers": {
          "payloadFormatIndicator": "string",
          "contentType": "string",
          "responseTopic": "string",
          "correlationData": "string",
          "messageExpiry": "string",
          "userProperties": [
            {
              "key": "string",
              "value": "string"
            }
            ...
          ]
        }
      },
      "s3": {
        "roleArn": "string",
        "bucketName": "string",
        "key": "string",
        "cannedAcl": "private"|"public-read"|"public-read-write"|"aws-exec-read"|"authenticated-read"|"bucket-owner-read"|"bucket-owner-full-control"|"log-delivery-write"
      },
      "firehose": {
        "roleArn": "string",
        "deliveryStreamName": "string",
        "separator": "string",
        "batchMode": true|false
      },
      "cloudwatchMetric": {
        "roleArn": "string",
        "metricNamespace": "string",
        "metricName": "string",
        "metricValue": "string",
        "metricUnit": "string",
        "metricTimestamp": "string"
      },
      "cloudwatchAlarm": {
        "roleArn": "string",
        "alarmName": "string",
        "stateReason": "string",
        "stateValue": "string"
      },
      "cloudwatchLogs": {
        "roleArn": "string",
        "logGroupName": "string",
        "batchMode": true|false
      },
      "elasticsearch": {
        "roleArn": "string",
        "endpoint": "string",
        "index": "string",
        "type": "string",
        "id": "string"
      },
      "salesforce": {
        "token": "string",
        "url": "string"
      },
      "iotAnalytics": {
        "channelArn": "string",
        "channelName": "string",
        "batchMode": true|false,
        "roleArn": "string"
      },
      "iotEvents": {
        "inputName": "string",
        "messageId": "string",
        "batchMode": true|false,
        "roleArn": "string"
      },
      "iotSiteWise": {
        "putAssetPropertyValueEntries": [
          {
            "entryId": "string",
            "assetId": "string",
            "propertyId": "string",
            "propertyAlias": "string",
            "propertyValues": [
              {
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
              ...
            ]
          }
          ...
        ],
        "roleArn": "string"
      },
      "stepFunctions": {
        "executionNamePrefix": "string",
        "stateMachineName": "string",
        "roleArn": "string"
      },
      "timestream": {
        "roleArn": "string",
        "databaseName": "string",
        "tableName": "string",
        "dimensions": [
          {
            "name": "string",
            "value": "string"
          }
          ...
        ],
        "timestamp": {
          "value": "string",
          "unit": "string"
        }
      },
      "http": {
        "url": "string",
        "confirmationUrl": "string",
        "headers": [
          {
            "key": "string",
            "value": "string"
          }
          ...
        ],
        "auth": {
          "sigv4": {
            "signingRegion": "string",
            "serviceName": "string",
            "roleArn": "string"
          }
        }
      },
      "kafka": {
        "destinationArn": "string",
        "topic": "string",
        "key": "string",
        "partition": "string",
        "clientProperties": {"string": "string"
          ...},
        "headers": [
          {
            "key": "string",
            "value": "string"
          }
          ...
        ]
      },
      "openSearch": {
        "roleArn": "string",
        "endpoint": "string",
        "index": "string",
        "type": "string",
        "id": "string"
      },
      "location": {
        "roleArn": "string",
        "trackerName": "string",
        "deviceId": "string",
        "timestamp": {
          "value": "string",
          "unit": "string"
        },
        "latitude": "string",
        "longitude": "string"
      }
    }
    ...
  ],
  "ruleDisabled": true|false,
  "awsIotSqlVersion": "string",
  "errorAction": {
    "dynamoDB": {
      "tableName": "string",
      "roleArn": "string",
      "operation": "string",
      "hashKeyField": "string",
      "hashKeyValue": "string",
      "hashKeyType": "STRING"|"NUMBER",
      "rangeKeyField": "string",
      "rangeKeyValue": "string",
      "rangeKeyType": "STRING"|"NUMBER",
      "payloadField": "string"
    },
    "dynamoDBv2": {
      "roleArn": "string",
      "putItem": {
        "tableName": "string"
      }
    },
    "lambda": {
      "functionArn": "string"
    },
    "sns": {
      "targetArn": "string",
      "roleArn": "string",
      "messageFormat": "RAW"|"JSON"
    },
    "sqs": {
      "roleArn": "string",
      "queueUrl": "string",
      "useBase64": true|false
    },
    "kinesis": {
      "roleArn": "string",
      "streamName": "string",
      "partitionKey": "string"
    },
    "republish": {
      "roleArn": "string",
      "topic": "string",
      "qos": integer,
      "headers": {
        "payloadFormatIndicator": "string",
        "contentType": "string",
        "responseTopic": "string",
        "correlationData": "string",
        "messageExpiry": "string",
        "userProperties": [
          {
            "key": "string",
            "value": "string"
          }
          ...
        ]
      }
    },
    "s3": {
      "roleArn": "string",
      "bucketName": "string",
      "key": "string",
      "cannedAcl": "private"|"public-read"|"public-read-write"|"aws-exec-read"|"authenticated-read"|"bucket-owner-read"|"bucket-owner-full-control"|"log-delivery-write"
    },
    "firehose": {
      "roleArn": "string",
      "deliveryStreamName": "string",
      "separator": "string",
      "batchMode": true|false
    },
    "cloudwatchMetric": {
      "roleArn": "string",
      "metricNamespace": "string",
      "metricName": "string",
      "metricValue": "string",
      "metricUnit": "string",
      "metricTimestamp": "string"
    },
    "cloudwatchAlarm": {
      "roleArn": "string",
      "alarmName": "string",
      "stateReason": "string",
      "stateValue": "string"
    },
    "cloudwatchLogs": {
      "roleArn": "string",
      "logGroupName": "string",
      "batchMode": true|false
    },
    "elasticsearch": {
      "roleArn": "string",
      "endpoint": "string",
      "index": "string",
      "type": "string",
      "id": "string"
    },
    "salesforce": {
      "token": "string",
      "url": "string"
    },
    "iotAnalytics": {
      "channelArn": "string",
      "channelName": "string",
      "batchMode": true|false,
      "roleArn": "string"
    },
    "iotEvents": {
      "inputName": "string",
      "messageId": "string",
      "batchMode": true|false,
      "roleArn": "string"
    },
    "iotSiteWise": {
      "putAssetPropertyValueEntries": [
        {
          "entryId": "string",
          "assetId": "string",
          "propertyId": "string",
          "propertyAlias": "string",
          "propertyValues": [
            {
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
            ...
          ]
        }
        ...
      ],
      "roleArn": "string"
    },
    "stepFunctions": {
      "executionNamePrefix": "string",
      "stateMachineName": "string",
      "roleArn": "string"
    },
    "timestream": {
      "roleArn": "string",
      "databaseName": "string",
      "tableName": "string",
      "dimensions": [
        {
          "name": "string",
          "value": "string"
        }
        ...
      ],
      "timestamp": {
        "value": "string",
        "unit": "string"
      }
    },
    "http": {
      "url": "string",
      "confirmationUrl": "string",
      "headers": [
        {
          "key": "string",
          "value": "string"
        }
        ...
      ],
      "auth": {
        "sigv4": {
          "signingRegion": "string",
          "serviceName": "string",
          "roleArn": "string"
        }
      }
    },
    "kafka": {
      "destinationArn": "string",
      "topic": "string",
      "key": "string",
      "partition": "string",
      "clientProperties": {"string": "string"
        ...},
      "headers": [
        {
          "key": "string",
          "value": "string"
        }
        ...
      ]
    },
    "openSearch": {
      "roleArn": "string",
      "endpoint": "string",
      "index": "string",
      "type": "string",
      "id": "string"
    },
    "location": {
      "roleArn": "string",
      "trackerName": "string",
      "deviceId": "string",
      "timestamp": {
        "value": "string",
        "unit": "string"
      },
      "latitude": "string",
      "longitude": "string"
    }
  }
}
```

`--tags` (string)

Metadata which can be used to manage the topic rule.

### Note

For URI Request parameters use format: â¦key1=value1&key2=value2â¦

For the CLI command-line parameter use format: âtags âkey1=value1&key2=value2â¦â

For the cli-input-json file use format: âtagsâ: âkey1=value1&key2=value2â¦â

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a rule that sends an Amazon SNS alert**

The following `create-topic-rule` example creates a rule that sends an Amazon SNS message when soil moisture level readings, as found in a device shadow, are low.

```
aws iot create-topic-rule \
    --rule-name "LowMoistureRule" \
    --topic-rule-payload file://plant-rule.json
```

The example requires the following JSON code to be saved to a file named `plant-rule.json`:

```
{
    "sql": "SELECT * FROM '$aws/things/MyRPi/shadow/update/accepted' WHERE state.reported.moisture = 'low'\n",
    "description": "Sends an alert whenever soil moisture level readings are too low.",
    "ruleDisabled": false,
    "awsIotSqlVersion": "2016-03-23",
    "actions": [{
            "sns": {
                "targetArn": "arn:aws:sns:us-west-2:123456789012:MyRPiLowMoistureTopic",
                "roleArn": "arn:aws:iam::123456789012:role/service-role/MyRPiLowMoistureTopicRole",
                "messageFormat": "RAW"
            }
    }]
}
```

This command produces no output.

For more information, see [Creating an AWS IoT Rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-create-rule.html) in the *AWS IoT Developers Guide*.

## Output

None