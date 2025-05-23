# update-event-source-mappingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-event-source-mapping.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lambda](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/index.html#cli-aws-lambda) ]

# update-event-source-mapping

## Description

Updates an event source mapping. You can change the function that Lambda invokes, or pause invocation and resume later from the same location.

For details about how to configure different event sources, see the following topics.

- [Amazon DynamoDB Streams](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-dynamodb-eventsourcemapping)
- [Amazon Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-eventsourcemapping)
- [Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-eventsource)
- [Amazon MQ and RabbitMQ](https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-eventsourcemapping)
- [Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html)
- [Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/kafka-smaa.html)
- [Amazon DocumentDB](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html)

The following error handling options are available only for DynamoDB and Kinesis event sources:

- `BisectBatchOnFunctionError` â If the function returns an error, split the batch in two and retry.
- `MaximumRecordAgeInSeconds` â Discard records older than the specified age. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires
- `MaximumRetryAttempts` â Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.
- `ParallelizationFactor` â Process multiple batches from each shard concurrently.

For stream sources (DynamoDB, Kinesis, Amazon MSK, and self-managed Apache Kafka), the following option is also available:

- `DestinationConfig` â Send discarded records to an Amazon SQS queue, Amazon SNS topic, or Amazon S3 bucket.

For information about which configuration parameters apply to each event source, see the following topics.

- [Amazon DynamoDB Streams](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html#services-ddb-params)
- [Amazon Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html#services-kinesis-params)
- [Amazon SQS](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#services-sqs-params)
- [Amazon MQ and RabbitMQ](https://docs.aws.amazon.com/lambda/latest/dg/with-mq.html#services-mq-params)
- [Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-parms)
- [Apache Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-kafka-parms)
- [Amazon DocumentDB](https://docs.aws.amazon.com/lambda/latest/dg/with-documentdb.html#docdb-configuration)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lambda-2015-03-31/UpdateEventSourceMapping)

## Synopsis

```
update-event-source-mapping
--uuid <value>
[--function-name <value>]
[--enabled | --no-enabled]
[--batch-size <value>]
[--filter-criteria <value>]
[--maximum-batching-window-in-seconds <value>]
[--destination-config <value>]
[--maximum-record-age-in-seconds <value>]
[--bisect-batch-on-function-error | --no-bisect-batch-on-function-error]
[--maximum-retry-attempts <value>]
[--parallelization-factor <value>]
[--source-access-configurations <value>]
[--tumbling-window-in-seconds <value>]
[--function-response-types <value>]
[--scaling-config <value>]
[--document-db-event-source-config <value>]
[--kms-key-arn <value>]
[--metrics-config <value>]
[--provisioned-poller-config <value>]
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

`--uuid` (string)

The identifier of the event source mapping.

`--function-name` (string)

The name or ARN of the Lambda function.

**Name formats**

- **Function name** â `MyFunction` .
- **Function ARN** â `arn:aws:lambda:us-west-2:123456789012:function:MyFunction` .
- **Version or Alias ARN** â `arn:aws:lambda:us-west-2:123456789012:function:MyFunction:PROD` .
- **Partial ARN** â `123456789012:function:MyFunction` .

The length constraint applies only to the full ARN. If you specify only the function name, itâs limited to 64 characters in length.

`--enabled` | `--no-enabled` (boolean)

When true, the event source mapping is active. When false, Lambda pauses polling and invocation.

Default: True

`--batch-size` (integer)

The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).

- **Amazon Kinesis** â Default 100. Max 10,000.
- **Amazon DynamoDB Streams** â Default 100. Max 10,000.
- **Amazon Simple Queue Service** â Default 10. For standard queues the max is 10,000. For FIFO queues the max is 10.
- **Amazon Managed Streaming for Apache Kafka** â Default 100. Max 10,000.
- **Self-managed Apache Kafka** â Default 100. Max 10,000.
- **Amazon MQ (ActiveMQ and RabbitMQ)** â Default 100. Max 10,000.
- **DocumentDB** â Default 100. Max 10,000.

`--filter-criteria` (structure)

An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see [Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html) .

Filters -> (list)

A list of filters.

(structure)

A structure within a `FilterCriteria` object that defines an event filtering pattern.

Pattern -> (string)

A filter pattern. For more information on the syntax of a filter pattern, see [Filter rule syntax](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax) .

Shorthand Syntax:

```
Filters=[{Pattern=string},{Pattern=string}]
```

JSON Syntax:

```
{
  "Filters": [
    {
      "Pattern": "string"
    }
    ...
  ]
}
```

`--maximum-batching-window-in-seconds` (integer)

The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure `MaximumBatchingWindowInSeconds` to any value from 0 seconds to 300 seconds in increments of seconds.

For Kinesis, DynamoDB, and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change `MaximumBatchingWindowInSeconds` in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.

Related setting: For Kinesis, DynamoDB, and Amazon SQS event sources, when you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.

`--destination-config` (structure)

(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Kafka only) A configuration object that specifies the destination of an event after Lambda processes it.

OnSuccess -> (structure)

The destination configuration for successful invocations.

Destination -> (string)

The Amazon Resource Name (ARN) of the destination resource.

OnFailure -> (structure)

The destination configuration for failed invocations.

Destination -> (string)

The Amazon Resource Name (ARN) of the destination resource.

To retain records of unsuccessful [asynchronous invocations](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) , you can configure an Amazon SNS topic, Amazon SQS queue, Amazon S3 bucket, Lambda function, or Amazon EventBridge event bus as the destination.

To retain records of failed invocations from [Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html) , [DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html) , [self-managed Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-smaa-onfailure-destination) or [Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-onfailure-destination) , you can configure an Amazon SNS topic, Amazon SQS queue, or Amazon S3 bucket as the destination.

Shorthand Syntax:

```
OnSuccess={Destination=string},OnFailure={Destination=string}
```

JSON Syntax:

```
{
  "OnSuccess": {
    "Destination": "string"
  },
  "OnFailure": {
    "Destination": "string"
  }
}
```

`--maximum-record-age-in-seconds` (integer)

(Kinesis and DynamoDB Streams only) Discard records older than the specified age. The default value is infinite (-1).

`--bisect-batch-on-function-error` | `--no-bisect-batch-on-function-error` (boolean)

(Kinesis and DynamoDB Streams only) If the function returns an error, split the batch in two and retry.

`--maximum-retry-attempts` (integer)

(Kinesis and DynamoDB Streams only) Discard records after the specified number of retries. The default value is infinite (-1). When set to infinite (-1), failed records are retried until the record expires.

`--parallelization-factor` (integer)

(Kinesis and DynamoDB Streams only) The number of batches to process from each shard concurrently.

`--source-access-configurations` (list)

An array of authentication protocols or VPC components required to secure your event source.

(structure)

To secure and define access to your event source, you can specify the authentication protocol, VPC components, or virtual host.

Type -> (string)

The type of authentication protocol, VPC components, or virtual host for your event source. For example: `"Type":"SASL_SCRAM_512_AUTH"` .

- `BASIC_AUTH` â (Amazon MQ) The Secrets Manager secret that stores your broker credentials.
- `BASIC_AUTH` â (Self-managed Apache Kafka) The Secrets Manager ARN of your secret key used for SASL/PLAIN authentication of your Apache Kafka brokers.
- `VPC_SUBNET` â (Self-managed Apache Kafka) The subnets associated with your VPC. Lambda connects to these subnets to fetch data from your self-managed Apache Kafka cluster.
- `VPC_SECURITY_GROUP` â (Self-managed Apache Kafka) The VPC security group used to manage access to your self-managed Apache Kafka brokers.
- `SASL_SCRAM_256_AUTH` â (Self-managed Apache Kafka) The Secrets Manager ARN of your secret key used for SASL SCRAM-256 authentication of your self-managed Apache Kafka brokers.
- `SASL_SCRAM_512_AUTH` â (Amazon MSK, Self-managed Apache Kafka) The Secrets Manager ARN of your secret key used for SASL SCRAM-512 authentication of your self-managed Apache Kafka brokers.
- `VIRTUAL_HOST` â- (RabbitMQ) The name of the virtual host in your RabbitMQ broker. Lambda uses this RabbitMQ host as the event source. This property cannot be specified in an UpdateEventSourceMapping API call.
- `CLIENT_CERTIFICATE_TLS_AUTH` â (Amazon MSK, self-managed Apache Kafka) The Secrets Manager ARN of your secret key containing the certificate chain (X.509 PEM), private key (PKCS#8 PEM), and private key password (optional) used for mutual TLS authentication of your MSK/Apache Kafka brokers.
- `SERVER_ROOT_CA_CERTIFICATE` â (Self-managed Apache Kafka) The Secrets Manager ARN of your secret key containing the root CA certificate (X.509 PEM) used for TLS encryption of your Apache Kafka brokers.

URI -> (string)

The value for your chosen configuration in `Type` . For example: `"URI": "arn:aws:secretsmanager:us-east-1:01234567890:secret:MyBrokerSecretName"` .

Shorthand Syntax:

```
Type=string,URI=string ...
```

JSON Syntax:

```
[
  {
    "Type": "BASIC_AUTH"|"VPC_SUBNET"|"VPC_SECURITY_GROUP"|"SASL_SCRAM_512_AUTH"|"SASL_SCRAM_256_AUTH"|"VIRTUAL_HOST"|"CLIENT_CERTIFICATE_TLS_AUTH"|"SERVER_ROOT_CA_CERTIFICATE",
    "URI": "string"
  }
  ...
]
```

`--tumbling-window-in-seconds` (integer)

(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.

`--function-response-types` (list)

(Kinesis, DynamoDB Streams, and Amazon SQS) A list of current response type enums applied to the event source mapping.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  ReportBatchItemFailures
```

`--scaling-config` (structure)

(Amazon SQS only) The scaling configuration for the event source. For more information, see [Configuring maximum concurrency for Amazon SQS event sources](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency) .

MaximumConcurrency -> (integer)

Limits the number of concurrent instances that the Amazon SQS event source can invoke.

Shorthand Syntax:

```
MaximumConcurrency=integer
```

JSON Syntax:

```
{
  "MaximumConcurrency": integer
}
```

`--document-db-event-source-config` (structure)

Specific configuration settings for a DocumentDB event source.

DatabaseName -> (string)

The name of the database to consume within the DocumentDB cluster.

CollectionName -> (string)

The name of the collection to consume within the database. If you do not specify a collection, Lambda consumes all collections.

FullDocument -> (string)

Determines what DocumentDB sends to your event stream during document update operations. If set to UpdateLookup, DocumentDB sends a delta describing the changes, along with a copy of the entire document. Otherwise, DocumentDB sends only a partial document that contains the changes.

Shorthand Syntax:

```
DatabaseName=string,CollectionName=string,FullDocument=string
```

JSON Syntax:

```
{
  "DatabaseName": "string",
  "CollectionName": "string",
  "FullDocument": "UpdateLookup"|"Default"
}
```

`--kms-key-arn` (string)

The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your functionâs [filter criteria](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics) . By default, Lambda does not encrypt your filter criteria object. Specify this property to encrypt data using your own customer managed key.

`--metrics-config` (structure)

The metrics configuration for your event source. For more information, see [Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics) .

Metrics -> (list)

The metrics you want your event source mapping to produce. Include `EventCount` to receive event source mapping metrics related to the number of events processed by your event source mapping. For more information about these metrics, see [Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics) .

(string)

Shorthand Syntax:

```
Metrics=string,string
```

JSON Syntax:

```
{
  "Metrics": ["EventCount", ...]
}
```

`--provisioned-poller-config` (structure)

(Amazon MSK and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see [provisioned mode](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode) .

MinimumPollers -> (integer)

The minimum number of event pollers this event source can scale down to.

MaximumPollers -> (integer)

The maximum number of event pollers this event source can scale up to.

Shorthand Syntax:

```
MinimumPollers=integer,MaximumPollers=integer
```

JSON Syntax:

```
{
  "MinimumPollers": integer,
  "MaximumPollers": integer
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update the mapping between an event source and an AWS Lambda function**

The following `update-event-source-mapping` example updates the batch size to 8 in the specified mapping.

```
aws lambda update-event-source-mapping \
    --uuid  "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE" \
    --batch-size 8
```

Output:

```
{
    "UUID": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE",
    "StateTransitionReason": "USER_INITIATED",
    "LastModified": 1569284520.333,
    "BatchSize": 8,
    "State": "Updating",
    "FunctionArn": "arn:aws:lambda:us-west-2:123456789012:function:my-function",
    "EventSourceArn": "arn:aws:sqs:us-west-2:123456789012:mySQSqueue"
}
```

For more information, see [AWS Lambda Event Source Mapping](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html) in the *AWS Lambda Developer Guide*.

## Output

UUID -> (string)

The identifier of the event source mapping.

StartingPosition -> (string)

The position in a stream from which to start reading. Required for Amazon Kinesis and Amazon DynamoDB Stream event sources. `AT_TIMESTAMP` is supported only for Amazon Kinesis streams, Amazon DocumentDB, Amazon MSK, and self-managed Apache Kafka.

StartingPositionTimestamp -> (timestamp)

With `StartingPosition` set to `AT_TIMESTAMP` , the time from which to start reading. `StartingPositionTimestamp` cannot be in the future.

BatchSize -> (integer)

The maximum number of records in each batch that Lambda pulls from your stream or queue and sends to your function. Lambda passes all of the records in the batch to the function in a single call, up to the payload limit for synchronous invocation (6 MB).

Default value: Varies by service. For Amazon SQS, the default is 10. For all other services, the default is 100.

Related setting: When you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.

MaximumBatchingWindowInSeconds -> (integer)

The maximum amount of time, in seconds, that Lambda spends gathering records before invoking the function. You can configure `MaximumBatchingWindowInSeconds` to any value from 0 seconds to 300 seconds in increments of seconds.

For streams and Amazon SQS event sources, the default batching window is 0 seconds. For Amazon MSK, Self-managed Apache Kafka, Amazon MQ, and DocumentDB event sources, the default batching window is 500 ms. Note that because you can only change `MaximumBatchingWindowInSeconds` in increments of seconds, you cannot revert back to the 500 ms default batching window after you have changed it. To restore the default batching window, you must create a new event source mapping.

Related setting: For streams and Amazon SQS event sources, when you set `BatchSize` to a value greater than 10, you must set `MaximumBatchingWindowInSeconds` to at least 1.

ParallelizationFactor -> (integer)

(Kinesis and DynamoDB Streams only) The number of batches to process concurrently from each shard. The default value is 1.

EventSourceArn -> (string)

The Amazon Resource Name (ARN) of the event source.

FilterCriteria -> (structure)

An object that defines the filter criteria that determine whether Lambda should process an event. For more information, see [Lambda event filtering](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html) .

If filter criteria is encrypted, this field shows up as `null` in the response of ListEventSourceMapping API calls. You can view this field in plaintext in the response of GetEventSourceMapping and DeleteEventSourceMapping calls if you have `kms:Decrypt` permissions for the correct KMS key.

Filters -> (list)

A list of filters.

(structure)

A structure within a `FilterCriteria` object that defines an event filtering pattern.

Pattern -> (string)

A filter pattern. For more information on the syntax of a filter pattern, see [Filter rule syntax](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-syntax) .

FunctionArn -> (string)

The ARN of the Lambda function.

LastModified -> (timestamp)

The date that the event source mapping was last updated or that its state changed.

LastProcessingResult -> (string)

The result of the last Lambda invocation of your function.

State -> (string)

The state of the event source mapping. It can be one of the following: `Creating` , `Enabling` , `Enabled` , `Disabling` , `Disabled` , `Updating` , or `Deleting` .

StateTransitionReason -> (string)

Indicates whether a user or Lambda made the last change to the event source mapping.

DestinationConfig -> (structure)

(Kinesis, DynamoDB Streams, Amazon MSK, and self-managed Apache Kafka event sources only) A configuration object that specifies the destination of an event after Lambda processes it.

OnSuccess -> (structure)

The destination configuration for successful invocations.

Destination -> (string)

The Amazon Resource Name (ARN) of the destination resource.

OnFailure -> (structure)

The destination configuration for failed invocations.

Destination -> (string)

The Amazon Resource Name (ARN) of the destination resource.

To retain records of unsuccessful [asynchronous invocations](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations) , you can configure an Amazon SNS topic, Amazon SQS queue, Amazon S3 bucket, Lambda function, or Amazon EventBridge event bus as the destination.

To retain records of failed invocations from [Kinesis](https://docs.aws.amazon.com/lambda/latest/dg/with-kinesis.html) , [DynamoDB](https://docs.aws.amazon.com/lambda/latest/dg/with-ddb.html) , [self-managed Kafka](https://docs.aws.amazon.com/lambda/latest/dg/with-kafka.html#services-smaa-onfailure-destination) or [Amazon MSK](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-onfailure-destination) , you can configure an Amazon SNS topic, Amazon SQS queue, or Amazon S3 bucket as the destination.

Topics -> (list)

The name of the Kafka topic.

(string)

Queues -> (list)

(Amazon MQ) The name of the Amazon MQ broker destination queue to consume.

(string)

SourceAccessConfigurations -> (list)

An array of the authentication protocol, VPC components, or virtual host to secure and define your event source.

(structure)

To secure and define access to your event source, you can specify the authentication protocol, VPC components, or virtual host.

Type -> (string)

The type of authentication protocol, VPC components, or virtual host for your event source. For example: `"Type":"SASL_SCRAM_512_AUTH"` .

- `BASIC_AUTH` â (Amazon MQ) The Secrets Manager secret that stores your broker credentials.
- `BASIC_AUTH` â (Self-managed Apache Kafka) The Secrets Manager ARN of your secret key used for SASL/PLAIN authentication of your Apache Kafka brokers.
- `VPC_SUBNET` â (Self-managed Apache Kafka) The subnets associated with your VPC. Lambda connects to these subnets to fetch data from your self-managed Apache Kafka cluster.
- `VPC_SECURITY_GROUP` â (Self-managed Apache Kafka) The VPC security group used to manage access to your self-managed Apache Kafka brokers.
- `SASL_SCRAM_256_AUTH` â (Self-managed Apache Kafka) The Secrets Manager ARN of your secret key used for SASL SCRAM-256 authentication of your self-managed Apache Kafka brokers.
- `SASL_SCRAM_512_AUTH` â (Amazon MSK, Self-managed Apache Kafka) The Secrets Manager ARN of your secret key used for SASL SCRAM-512 authentication of your self-managed Apache Kafka brokers.
- `VIRTUAL_HOST` â- (RabbitMQ) The name of the virtual host in your RabbitMQ broker. Lambda uses this RabbitMQ host as the event source. This property cannot be specified in an UpdateEventSourceMapping API call.
- `CLIENT_CERTIFICATE_TLS_AUTH` â (Amazon MSK, self-managed Apache Kafka) The Secrets Manager ARN of your secret key containing the certificate chain (X.509 PEM), private key (PKCS#8 PEM), and private key password (optional) used for mutual TLS authentication of your MSK/Apache Kafka brokers.
- `SERVER_ROOT_CA_CERTIFICATE` â (Self-managed Apache Kafka) The Secrets Manager ARN of your secret key containing the root CA certificate (X.509 PEM) used for TLS encryption of your Apache Kafka brokers.

URI -> (string)

The value for your chosen configuration in `Type` . For example: `"URI": "arn:aws:secretsmanager:us-east-1:01234567890:secret:MyBrokerSecretName"` .

SelfManagedEventSource -> (structure)

The self-managed Apache Kafka cluster for your event source.

Endpoints -> (map)

The list of bootstrap servers for your Kafka brokers in the following format: `"KAFKA_BOOTSTRAP_SERVERS": ["abc.xyz.com:xxxx","abc2.xyz.com:xxxx"]` .

key -> (string)

value -> (list)

(string)

MaximumRecordAgeInSeconds -> (integer)

(Kinesis and DynamoDB Streams only) Discard records older than the specified age. The default value is -1, which sets the maximum age to infinite. When the value is set to infinite, Lambda never discards old records.

### Note

The minimum valid value for maximum record age is 60s. Although values less than 60 and greater than -1 fall within the parameterâs absolute range, they are not allowed

BisectBatchOnFunctionError -> (boolean)

(Kinesis and DynamoDB Streams only) If the function returns an error, split the batch in two and retry. The default value is false.

MaximumRetryAttempts -> (integer)

(Kinesis and DynamoDB Streams only) Discard records after the specified number of retries. The default value is -1, which sets the maximum number of retries to infinite. When MaximumRetryAttempts is infinite, Lambda retries failed records until the record expires in the event source.

TumblingWindowInSeconds -> (integer)

(Kinesis and DynamoDB Streams only) The duration in seconds of a processing window for DynamoDB and Kinesis Streams event sources. A value of 0 seconds indicates no tumbling window.

FunctionResponseTypes -> (list)

(Kinesis, DynamoDB Streams, and Amazon SQS) A list of current response type enums applied to the event source mapping.

(string)

AmazonManagedKafkaEventSourceConfig -> (structure)

Specific configuration settings for an Amazon Managed Streaming for Apache Kafka (Amazon MSK) event source.

ConsumerGroupId -> (string)

The identifier for the Kafka consumer group to join. The consumer group ID must be unique among all your Kafka event sources. After creating a Kafka event source mapping with the consumer group ID specified, you cannot update this value. For more information, see [Customizable consumer group ID](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-consumer-group-id) .

SelfManagedKafkaEventSourceConfig -> (structure)

Specific configuration settings for a self-managed Apache Kafka event source.

ConsumerGroupId -> (string)

The identifier for the Kafka consumer group to join. The consumer group ID must be unique among all your Kafka event sources. After creating a Kafka event source mapping with the consumer group ID specified, you cannot update this value. For more information, see [Customizable consumer group ID](https://docs.aws.amazon.com/lambda/latest/dg/with-msk.html#services-msk-consumer-group-id) .

ScalingConfig -> (structure)

(Amazon SQS only) The scaling configuration for the event source. For more information, see [Configuring maximum concurrency for Amazon SQS event sources](https://docs.aws.amazon.com/lambda/latest/dg/with-sqs.html#events-sqs-max-concurrency) .

MaximumConcurrency -> (integer)

Limits the number of concurrent instances that the Amazon SQS event source can invoke.

DocumentDBEventSourceConfig -> (structure)

Specific configuration settings for a DocumentDB event source.

DatabaseName -> (string)

The name of the database to consume within the DocumentDB cluster.

CollectionName -> (string)

The name of the collection to consume within the database. If you do not specify a collection, Lambda consumes all collections.

FullDocument -> (string)

Determines what DocumentDB sends to your event stream during document update operations. If set to UpdateLookup, DocumentDB sends a delta describing the changes, along with a copy of the entire document. Otherwise, DocumentDB sends only a partial document that contains the changes.

KMSKeyArn -> (string)

The ARN of the Key Management Service (KMS) customer managed key that Lambda uses to encrypt your functionâs [filter criteria](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventfiltering.html#filtering-basics) .

FilterCriteriaError -> (structure)

An object that contains details about an error related to filter criteria encryption.

ErrorCode -> (string)

The KMS exception that resulted from filter criteria encryption or decryption.

Message -> (string)

The error message.

EventSourceMappingArn -> (string)

The Amazon Resource Name (ARN) of the event source mapping.

MetricsConfig -> (structure)

The metrics configuration for your event source. For more information, see [Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics) .

Metrics -> (list)

The metrics you want your event source mapping to produce. Include `EventCount` to receive event source mapping metrics related to the number of events processed by your event source mapping. For more information about these metrics, see [Event source mapping metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics-types.html#event-source-mapping-metrics) .

(string)

ProvisionedPollerConfig -> (structure)

(Amazon MSK and self-managed Apache Kafka only) The provisioned mode configuration for the event source. For more information, see [provisioned mode](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode) .

MinimumPollers -> (integer)

The minimum number of event pollers this event source can scale down to.

MaximumPollers -> (integer)

The maximum number of event pollers this event source can scale up to.