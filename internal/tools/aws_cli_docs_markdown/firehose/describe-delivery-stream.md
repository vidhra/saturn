# describe-delivery-streamÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/describe-delivery-stream.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/describe-delivery-stream.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [firehose](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/index.html#cli-aws-firehose) ]

# describe-delivery-stream

## Description

Describes the specified Firehose stream and its status. For example, after your Firehose stream is created, call `DescribeDeliveryStream` to see whether the Firehose stream is `ACTIVE` and therefore ready for data to be sent to it.

If the status of a Firehose stream is `CREATING_FAILED` , this status doesnât change, and you canât invoke  CreateDeliveryStream again on it. However, you can invoke the  DeleteDeliveryStream operation to delete it. If the status is `DELETING_FAILED` , you can force deletion by invoking  DeleteDeliveryStream again but with  DeleteDeliveryStreamInput$AllowForceDelete set to true.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/firehose-2015-08-04/DescribeDeliveryStream)

## Synopsis

```
describe-delivery-stream
--delivery-stream-name <value>
[--limit <value>]
[--exclusive-start-destination-id <value>]
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

`--delivery-stream-name` (string)

The name of the Firehose stream.

`--limit` (integer)

The limit on the number of destinations to return. You can have one destination per Firehose stream.

`--exclusive-start-destination-id` (string)

The ID of the destination to start returning the destination information. Firehose supports one destination per Firehose stream.

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

DeliveryStreamDescription -> (structure)

Information about the Firehose stream.

DeliveryStreamName -> (string)

The name of the Firehose stream.

DeliveryStreamARN -> (string)

The Amazon Resource Name (ARN) of the Firehose stream. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

DeliveryStreamStatus -> (string)

The status of the Firehose stream. If the status of a Firehose stream is `CREATING_FAILED` , this status doesnât change, and you canât invoke `CreateDeliveryStream` again on it. However, you can invoke the  DeleteDeliveryStream operation to delete it.

FailureDescription -> (structure)

Provides details in case one of the following operations fails due to an error related to KMS:  CreateDeliveryStream ,  DeleteDeliveryStream ,  StartDeliveryStreamEncryption ,  StopDeliveryStreamEncryption .

Type -> (string)

The type of error that caused the failure.

Details -> (string)

A message providing details about the error that caused the failure.

DeliveryStreamEncryptionConfiguration -> (structure)

Indicates the server-side encryption (SSE) status for the Firehose stream.

KeyARN -> (string)

If `KeyType` is `CUSTOMER_MANAGED_CMK` , this field contains the ARN of the customer managed CMK. If `KeyType` is `Amazon Web Services_OWNED_CMK` , `DeliveryStreamEncryptionConfiguration` doesnât contain a value for `KeyARN` .

KeyType -> (string)

Indicates the type of customer master key (CMK) that is used for encryption. The default setting is `Amazon Web Services_OWNED_CMK` . For more information about CMKs, see [Customer Master Keys (CMKs)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#master_keys) .

Status -> (string)

This is the server-side encryption (SSE) status for the Firehose stream. For a full description of the different values of this status, see  StartDeliveryStreamEncryption and  StopDeliveryStreamEncryption . If this status is `ENABLING_FAILED` or `DISABLING_FAILED` , it is the status of the most recent attempt to enable or disable SSE, respectively.

FailureDescription -> (structure)

Provides details in case one of the following operations fails due to an error related to KMS:  CreateDeliveryStream ,  DeleteDeliveryStream ,  StartDeliveryStreamEncryption ,  StopDeliveryStreamEncryption .

Type -> (string)

The type of error that caused the failure.

Details -> (string)

A message providing details about the error that caused the failure.

DeliveryStreamType -> (string)

The Firehose stream type. This can be one of the following values:

- `DirectPut` : Provider applications access the Firehose stream directly.
- `KinesisStreamAsSource` : The Firehose stream uses a Kinesis data stream as a source.

VersionId -> (string)

Each time the destination is updated for a Firehose stream, the version ID is changed, and the current version ID is required when updating the destination. This is so that the service knows it is applying the changes to the correct version of the delivery stream.

CreateTimestamp -> (timestamp)

The date and time that the Firehose stream was created.

LastUpdateTimestamp -> (timestamp)

The date and time that the Firehose stream was last updated.

Source -> (structure)

If the `DeliveryStreamType` parameter is `KinesisStreamAsSource` , a  SourceDescription object describing the source Kinesis data stream.

DirectPutSourceDescription -> (structure)

Details about Direct PUT used as the source for a Firehose stream.

ThroughputHintInMBs -> (integer)

The value that you configure for this parameter is for information purpose only and does not affect Firehose delivery throughput limit. You can use the [Firehose Limits form](https://support.console.aws.amazon.com/support/home#/case/create%3FissueType=service-limit-increase%26limitType=kinesis-firehose-limits) to request a throughput limit increase.

KinesisStreamSourceDescription -> (structure)

The  KinesisStreamSourceDescription value for the source Kinesis data stream.

KinesisStreamARN -> (string)

The Amazon Resource Name (ARN) of the source Kinesis data stream. For more information, see [Amazon Kinesis Data Streams ARN Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kinesis-streams) .

RoleARN -> (string)

The ARN of the role used by the source Kinesis data stream. For more information, see [Amazon Web Services Identity and Access Management (IAM) ARN Format](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-iam) .

DeliveryStartTimestamp -> (timestamp)

Firehose starts retrieving records from the Kinesis data stream starting with this timestamp.

MSKSourceDescription -> (structure)

The configuration description for the Amazon MSK cluster to be used as the source for a delivery stream.

MSKClusterARN -> (string)

The ARN of the Amazon MSK cluster.

TopicName -> (string)

The topic name within the Amazon MSK cluster.

AuthenticationConfiguration -> (structure)

The authentication configuration of the Amazon MSK cluster.

RoleARN -> (string)

The ARN of the role used to access the Amazon MSK cluster.

Connectivity -> (string)

The type of connectivity used to access the Amazon MSK cluster.

DeliveryStartTimestamp -> (timestamp)

Firehose starts retrieving records from the topic within the Amazon MSK cluster starting with this timestamp.

ReadFromTimestamp -> (timestamp)

The start date and time in UTC for the offset position within your MSK topic from where Firehose begins to read. By default, this is set to timestamp when Firehose becomes Active.

If you want to create a Firehose stream with Earliest start position from SDK or CLI, you need to set the `ReadFromTimestampUTC` parameter to Epoch (1970-01-01T00:00:00Z).

DatabaseSourceDescription -> (structure)

Details about a database used as the source for a Firehose stream.

Amazon Data Firehose is in preview release and is subject to change.

Type -> (string)

The type of database engine. This can be one of the following values.

- MySQL
- PostgreSQL

Amazon Data Firehose is in preview release and is subject to change.

Endpoint -> (string)

The endpoint of the database server.

Amazon Data Firehose is in preview release and is subject to change.

Port -> (integer)

The port of the database. This can be one of the following values.

- 3306 for MySQL database type
- 5432 for PostgreSQL database type

Amazon Data Firehose is in preview release and is subject to change.

SSLMode -> (string)

The mode to enable or disable SSL when Firehose connects to the database endpoint.

Amazon Data Firehose is in preview release and is subject to change.

Databases -> (structure)

The list of database patterns in source database endpoint for Firehose to read from.

Amazon Data Firehose is in preview release and is subject to change.

Include -> (list)

The list of database patterns in source database endpoint to be included for Firehose to read from.

Amazon Data Firehose is in preview release and is subject to change.

(string)

Exclude -> (list)

The list of database patterns in source database endpoint to be excluded for Firehose to read from.

Amazon Data Firehose is in preview release and is subject to change.

(string)

Tables -> (structure)

The list of table patterns in source database endpoint for Firehose to read from.

Amazon Data Firehose is in preview release and is subject to change.

Include -> (list)

The list of table patterns in source database endpoint to be included for Firehose to read from.

Amazon Data Firehose is in preview release and is subject to change.

(string)

Exclude -> (list)

The list of table patterns in source database endpoint to be excluded for Firehose to read from.

Amazon Data Firehose is in preview release and is subject to change.

(string)

Columns -> (structure)

The list of column patterns in source database endpoint for Firehose to read from.

Amazon Data Firehose is in preview release and is subject to change.

Include -> (list)

The list of column patterns in source database to be included for Firehose to read from.

Amazon Data Firehose is in preview release and is subject to change.

(string)

Exclude -> (list)

The list of column patterns in source database to be excluded for Firehose to read from.

Amazon Data Firehose is in preview release and is subject to change.

(string)

SurrogateKeys -> (list)

The optional list of table and column names used as unique key columns when taking snapshot if the tables donât have primary keys configured.

Amazon Data Firehose is in preview release and is subject to change.

(string)

SnapshotWatermarkTable -> (string)

The fully qualified name of the table in source database endpoint that Firehose uses to track snapshot progress.

Amazon Data Firehose is in preview release and is subject to change.

SnapshotInfo -> (list)

The structure that describes the snapshot information of a table in source database endpoint that Firehose reads.

Amazon Data Firehose is in preview release and is subject to change.

(structure)

The structure that describes the snapshot information of a table in source database endpoint that Firehose reads.

Amazon Data Firehose is in preview release and is subject to change.

Id -> (string)

The identifier of the current snapshot of the table in source database endpoint.

Amazon Data Firehose is in preview release and is subject to change.

Table -> (string)

The fully qualified name of the table in source database endpoint that Firehose reads.

Amazon Data Firehose is in preview release and is subject to change.

RequestTimestamp -> (timestamp)

The timestamp when the current snapshot is taken on the table.

Amazon Data Firehose is in preview release and is subject to change.

RequestedBy -> (string)

The principal that sent the request to take the current snapshot on the table.

Amazon Data Firehose is in preview release and is subject to change.

Status -> (string)

The status of the current snapshot of the table.

Amazon Data Firehose is in preview release and is subject to change.

FailureDescription -> (structure)

Provides details in case one of the following operations fails due to an error related to KMS:  CreateDeliveryStream ,  DeleteDeliveryStream ,  StartDeliveryStreamEncryption ,  StopDeliveryStreamEncryption .

Type -> (string)

The type of error that caused the failure.

Details -> (string)

A message providing details about the error that caused the failure.

DatabaseSourceAuthenticationConfiguration -> (structure)

The structure to configure the authentication methods for Firehose to connect to source database endpoint.

Amazon Data Firehose is in preview release and is subject to change.

SecretsManagerConfiguration -> (structure)

The structure that defines how Firehose accesses the secret.

SecretARN -> (string)

The ARN of the secret that stores your credentials. It must be in the same region as the Firehose stream and the role. The secret ARN can reside in a different account than the Firehose stream and role as Firehose supports cross-account secret access. This parameter is required when **Enabled** is set to `True` .

RoleARN -> (string)

Specifies the role that Firehose assumes when calling the Secrets Manager API operation. When you provide the role, it overrides any destination specific role defined in the destination configuration. If you do not provide the then we use the destination specific role. This parameter is required for Splunk.

Enabled -> (boolean)

Specifies whether you want to use the secrets manager feature. When set as `True` the secrets manager configuration overwrites the existing secrets in the destination configuration. When itâs set to `False` Firehose falls back to the credentials in the destination configuration.

DatabaseSourceVPCConfiguration -> (structure)

The details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database.

Amazon Data Firehose is in preview release and is subject to change.

VpcEndpointServiceName -> (string)

The VPC endpoint service name which Firehose uses to create a PrivateLink to the database. The endpoint service must have the Firehose service principle `firehose.amazonaws.com` as an allowed principal on the VPC endpoint service. The VPC endpoint service name is a string that looks like `com.amazonaws.vpce.<region>.<vpc-endpoint-service-id>` .

Amazon Data Firehose is in preview release and is subject to change.

Destinations -> (list)

The destinations.

(structure)

Describes the destination for a Firehose stream.

DestinationId -> (string)

The ID of the destination.

S3DestinationDescription -> (structure)

[Deprecated] The destination in Amazon S3.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

ExtendedS3DestinationDescription -> (structure)

The destination in Amazon S3.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

ProcessingConfiguration -> (structure)

The data processing configuration.

Enabled -> (boolean)

Enables or disables data processing.

Processors -> (list)

The data processors.

(structure)

Describes a data processor.

### Note

If you want to add a new line delimiter between records in objects that are delivered to Amazon S3, choose `AppendDelimiterToRecord` as a processor type. You donât have to put a processor parameter when you select `AppendDelimiterToRecord` .

Type -> (string)

The type of processor.

Parameters -> (list)

The processor parameters.

(structure)

Describes the processor parameter.

ParameterName -> (string)

The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds` . The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

ParameterValue -> (string)

The parameter value.

S3BackupMode -> (string)

The Amazon S3 backup mode.

S3BackupDescription -> (structure)

The configuration for backup in Amazon S3.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

DataFormatConversionConfiguration -> (structure)

The serializer, deserializer, and schema for converting data from the JSON format to the Parquet or ORC format before writing it to Amazon S3.

SchemaConfiguration -> (structure)

Specifies the Amazon Web Services Glue Data Catalog table that contains the column information. This parameter is required if `Enabled` is set to true.

RoleARN -> (string)

The role that Firehose can use to access Amazon Web Services Glue. This role must be in the same account you use for Firehose. Cross-account roles arenât allowed.

### Warning

If the `SchemaConfiguration` request parameter is used as part of invoking the `CreateDeliveryStream` API, then the `RoleARN` property is required and its value must be specified.

CatalogId -> (string)

The ID of the Amazon Web Services Glue Data Catalog. If you donât supply this, the Amazon Web Services account ID is used by default.

DatabaseName -> (string)

Specifies the name of the Amazon Web Services Glue database that contains the schema for the output data.

### Warning

If the `SchemaConfiguration` request parameter is used as part of invoking the `CreateDeliveryStream` API, then the `DatabaseName` property is required and its value must be specified.

TableName -> (string)

Specifies the Amazon Web Services Glue table that contains the column information that constitutes your data schema.

### Warning

If the `SchemaConfiguration` request parameter is used as part of invoking the `CreateDeliveryStream` API, then the `TableName` property is required and its value must be specified.

Region -> (string)

If you donât specify an Amazon Web Services Region, the default is the current Region.

VersionId -> (string)

Specifies the table version for the output data schema. If you donât specify this version ID, or if you set it to `LATEST` , Firehose uses the most recent version. This means that any updates to the table are automatically picked up.

InputFormatConfiguration -> (structure)

Specifies the deserializer that you want Firehose to use to convert the format of your data from JSON. This parameter is required if `Enabled` is set to true.

Deserializer -> (structure)

Specifies which deserializer to use. You can choose either the Apache Hive JSON SerDe or the OpenX JSON SerDe. If both are non-null, the server rejects the request.

OpenXJsonSerDe -> (structure)

The OpenX SerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.

ConvertDotsInJsonKeysToUnderscores -> (boolean)

When set to `true` , specifies that the names of the keys include dots and that you want Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is âa.bâ, you can define the column name to be âa_bâ when using this option.

The default is `false` .

CaseInsensitive -> (boolean)

When set to `true` , which is the default, Firehose converts JSON keys to lowercase before deserializing them.

ColumnToJsonKeyMappings -> (map)

Maps column names to JSON keys that arenât identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, `timestamp` is a Hive keyword. If you have a JSON key named `timestamp` , set this parameter to `{"ts": "timestamp"}` to map this key to a column named `ts` .

key -> (string)

value -> (string)

HiveJsonSerDe -> (structure)

The native Hive / HCatalog JsonSerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.

TimestampFormats -> (list)

Indicates how you want Firehose to parse the date and timestamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTimeâs DateTimeFormat format strings. For more information, see [Class DateTimeFormat](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html) . You can also use the special value `millis` to parse timestamps in epoch milliseconds. If you donât specify a format, Firehose uses `java.sql.Timestamp::valueOf` by default.

(string)

OutputFormatConfiguration -> (structure)

Specifies the serializer that you want Firehose to use to convert the format of your data to the Parquet or ORC format. This parameter is required if `Enabled` is set to true.

Serializer -> (structure)

Specifies which serializer to use. You can choose either the ORC SerDe or the Parquet SerDe. If both are non-null, the server rejects the request.

ParquetSerDe -> (structure)

A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see [Apache Parquet](https://parquet.apache.org/docs/contribution-guidelines/) .

BlockSizeBytes -> (integer)

The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.

PageSizeBytes -> (integer)

The Parquet page size. Column chunks are divided into pages. A page is conceptually an indivisible unit (in terms of compression and encoding). The minimum value is 64 KiB and the default is 1 MiB.

Compression -> (string)

The compression code to use over data blocks. The possible values are `UNCOMPRESSED` , `SNAPPY` , and `GZIP` , with the default being `SNAPPY` . Use `SNAPPY` for higher decompression speed. Use `GZIP` if the compression ratio is more important than speed.

EnableDictionaryCompression -> (boolean)

Indicates whether to enable dictionary compression.

MaxPaddingBytes -> (integer)

The maximum amount of padding to apply. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 0.

WriterVersion -> (string)

Indicates the version of row format to output. The possible values are `V1` and `V2` . The default is `V1` .

OrcSerDe -> (structure)

A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see [Apache ORC](https://orc.apache.org/docs/) .

StripeSizeBytes -> (integer)

The number of bytes in each stripe. The default is 64 MiB and the minimum is 8 MiB.

BlockSizeBytes -> (integer)

The Hadoop Distributed File System (HDFS) block size. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is 256 MiB and the minimum is 64 MiB. Firehose uses this value for padding calculations.

RowIndexStride -> (integer)

The number of rows between index entries. The default is 10,000 and the minimum is 1,000.

EnablePadding -> (boolean)

Set this to `true` to indicate that you want stripes to be padded to the HDFS block boundaries. This is useful if you intend to copy the data from Amazon S3 to HDFS before querying. The default is `false` .

PaddingTolerance -> (double)

A number between 0 and 1 that defines the tolerance for block padding as a decimal fraction of stripe size. The default value is 0.05, which means 5 percent of stripe size.

For the default values of 64 MiB ORC stripes and 256 MiB HDFS blocks, the default block padding tolerance of 5 percent reserves a maximum of 3.2 MiB for padding within the 256 MiB block. In such a case, if the available size within the block is more than 3.2 MiB, a new, smaller stripe is inserted to fit within that space. This ensures that no stripe crosses block boundaries and causes remote reads within a node-local task.

Firehose ignores this parameter when  OrcSerDe$EnablePadding is `false` .

Compression -> (string)

The compression code to use over data blocks. The default is `SNAPPY` .

BloomFilterColumns -> (list)

The column names for which you want Firehose to create bloom filters. The default is `null` .

(string)

BloomFilterFalsePositiveProbability -> (double)

The Bloom filter false positive probability (FPP). The lower the FPP, the bigger the Bloom filter. The default value is 0.05, the minimum is 0, and the maximum is 1.

DictionaryKeyThreshold -> (double)

Represents the fraction of the total number of non-null rows. To turn off dictionary encoding, set this fraction to a number that is less than the number of distinct keys in a dictionary. To always use dictionary encoding, set this threshold to 1.

FormatVersion -> (string)

The version of the file to write. The possible values are `V0_11` and `V0_12` . The default is `V0_12` .

Enabled -> (boolean)

Defaults to `true` . Set it to `false` if you want to disable format conversion while preserving the configuration details.

DynamicPartitioningConfiguration -> (structure)

The configuration of the dynamic partitioning mechanism that creates smaller data sets from the streaming data by partitioning it based on partition keys. Currently, dynamic partitioning is only supported for Amazon S3 destinations.

RetryOptions -> (structure)

The retry behavior in case Firehose is unable to deliver data to an Amazon S3 prefix.

DurationInSeconds -> (integer)

The period of time during which Firehose retries to deliver data to the specified destination.

Enabled -> (boolean)

Specifies that the dynamic partitioning is enabled for this Firehose stream.

FileExtension -> (string)

Specify a file extension. It will override the default file extension

CustomTimeZone -> (string)

The time zone you prefer. UTC is the default.

RedshiftDestinationDescription -> (structure)

The destination in Amazon Redshift.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

ClusterJDBCURL -> (string)

The database connection string.

CopyCommand -> (structure)

The `COPY` command.

DataTableName -> (string)

The name of the target table. The table must already exist in the database.

DataTableColumns -> (string)

A comma-separated list of column names.

CopyOptions -> (string)

Optional parameters to use with the Amazon Redshift `COPY` command. For more information, see the âOptional Parametersâ section of [Amazon Redshift COPY command](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html) . Some possible examples that would apply to Firehose are as follows:

`delimiter '\t' lzop;` - fields are delimited with âtâ (TAB character) and compressed using lzop.

`delimiter '|'` - fields are delimited with â|â (this is the default delimiter).

`delimiter '|' escape` - the delimiter should be escaped.

`fixedwidth 'venueid:3,venuename:25,venuecity:12,venuestate:2,venueseats:6'` - fields are fixed width in the source, with each width specified after every column in the table.

`JSON 's3://mybucket/jsonpaths.txt'` - data is in JSON format, and the path specified is the format of the data.

For more examples, see [Amazon Redshift COPY command examples](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY_command_examples.html) .

Username -> (string)

The name of the user.

RetryOptions -> (structure)

The retry behavior in case Firehose is unable to deliver documents to Amazon Redshift. Default value is 3600 (60 minutes).

DurationInSeconds -> (integer)

The length of time during which Firehose retries delivery after a failure, starting from the initial request and including the first attempt. The default value is 3600 seconds (60 minutes). Firehose does not retry if the value of `DurationInSeconds` is 0 (zero) or if the first delivery attempt takes longer than the current value.

S3DestinationDescription -> (structure)

The Amazon S3 destination.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

ProcessingConfiguration -> (structure)

The data processing configuration.

Enabled -> (boolean)

Enables or disables data processing.

Processors -> (list)

The data processors.

(structure)

Describes a data processor.

### Note

If you want to add a new line delimiter between records in objects that are delivered to Amazon S3, choose `AppendDelimiterToRecord` as a processor type. You donât have to put a processor parameter when you select `AppendDelimiterToRecord` .

Type -> (string)

The type of processor.

Parameters -> (list)

The processor parameters.

(structure)

Describes the processor parameter.

ParameterName -> (string)

The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds` . The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

ParameterValue -> (string)

The parameter value.

S3BackupMode -> (string)

The Amazon S3 backup mode.

S3BackupDescription -> (structure)

The configuration for backup in Amazon S3.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

SecretsManagerConfiguration -> (structure)

The configuration that defines how you access secrets for Amazon Redshift.

SecretARN -> (string)

The ARN of the secret that stores your credentials. It must be in the same region as the Firehose stream and the role. The secret ARN can reside in a different account than the Firehose stream and role as Firehose supports cross-account secret access. This parameter is required when **Enabled** is set to `True` .

RoleARN -> (string)

Specifies the role that Firehose assumes when calling the Secrets Manager API operation. When you provide the role, it overrides any destination specific role defined in the destination configuration. If you do not provide the then we use the destination specific role. This parameter is required for Splunk.

Enabled -> (boolean)

Specifies whether you want to use the secrets manager feature. When set as `True` the secrets manager configuration overwrites the existing secrets in the destination configuration. When itâs set to `False` Firehose falls back to the credentials in the destination configuration.

ElasticsearchDestinationDescription -> (structure)

The destination in Amazon OpenSearch Service.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

DomainARN -> (string)

The ARN of the Amazon OpenSearch Service domain. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Firehose uses either `ClusterEndpoint` or `DomainARN` to send data to Amazon OpenSearch Service.

ClusterEndpoint -> (string)

The endpoint to use when communicating with the cluster. Firehose uses either this `ClusterEndpoint` or the `DomainARN` field to send data to Amazon OpenSearch Service.

IndexName -> (string)

The Elasticsearch index name.

TypeName -> (string)

The Elasticsearch type name. This applies to Elasticsearch 6.x and lower versions. For Elasticsearch 7.x and OpenSearch Service 1.x, thereâs no value for `TypeName` .

IndexRotationPeriod -> (string)

The Elasticsearch index rotation period

BufferingHints -> (structure)

The buffering options.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

RetryOptions -> (structure)

The Amazon OpenSearch Service retry options.

DurationInSeconds -> (integer)

After an initial failure to deliver to Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

S3BackupMode -> (string)

The Amazon S3 backup mode.

S3DestinationDescription -> (structure)

The Amazon S3 destination.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

ProcessingConfiguration -> (structure)

The data processing configuration.

Enabled -> (boolean)

Enables or disables data processing.

Processors -> (list)

The data processors.

(structure)

Describes a data processor.

### Note

If you want to add a new line delimiter between records in objects that are delivered to Amazon S3, choose `AppendDelimiterToRecord` as a processor type. You donât have to put a processor parameter when you select `AppendDelimiterToRecord` .

Type -> (string)

The type of processor.

Parameters -> (list)

The processor parameters.

(structure)

Describes the processor parameter.

ParameterName -> (string)

The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds` . The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

ParameterValue -> (string)

The parameter value.

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

VpcConfigurationDescription -> (structure)

The details of the VPC of the Amazon OpenSearch or the Amazon OpenSearch Serverless destination.

SubnetIds -> (list)

The IDs of the subnets that Firehose uses to create ENIs in the VPC of the Amazon OpenSearch Service destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon OpenSearch Service endpoints. Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.

The number of ENIs that Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Firehose can create up to three ENIs for this Firehose stream for each of the subnets specified here. For more information about ENI quota, see [Network Interfaces](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-enis) in the Amazon VPC Quotas topic.

(string)

RoleARN -> (string)

The ARN of the IAM role that the Firehose stream uses to create endpoints in the destination VPC. You can use your existing Firehose delivery role or you can specify a new role. In either case, make sure that the role trusts the Firehose service principal and that it grants the following permissions:

- `ec2:DescribeVpcs`
- `ec2:DescribeVpcAttribute`
- `ec2:DescribeSubnets`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeNetworkInterfaces`
- `ec2:CreateNetworkInterface`
- `ec2:CreateNetworkInterfacePermission`
- `ec2:DeleteNetworkInterface`

If you revoke these permissions after you create the Firehose stream, Firehose canât scale out by creating more ENIs when necessary. You might therefore see a degradation in performance.

SecurityGroupIds -> (list)

The IDs of the security groups that Firehose uses when it creates ENIs in the VPC of the Amazon OpenSearch Service destination. You can use the same security group that the Amazon ES domain uses or different ones. If you specify different security groups, ensure that they allow outbound HTTPS traffic to the Amazon OpenSearch Service domainâs security group. Also ensure that the Amazon OpenSearch Service domainâs security group allows HTTPS traffic from the security groups specified here. If you use the same security group for both your Firehose stream and the Amazon OpenSearch Service domain, make sure the security group inbound rule allows HTTPS traffic. For more information about security group rules, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules) in the Amazon VPC documentation.

(string)

VpcId -> (string)

The ID of the Amazon OpenSearch Service destinationâs VPC.

DocumentIdOptions -> (structure)

Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.

DefaultDocumentIdFormat -> (string)

When the `FIREHOSE_DEFAULT` option is chosen, Firehose generates a unique document ID for each record based on a unique internal identifier. The generated document ID is stable across multiple delivery attempts, which helps prevent the same record from being indexed multiple times with different document IDs.

When the `NO_DOCUMENT_ID` option is chosen, Firehose does not include any document IDs in the requests it sends to the Amazon OpenSearch Service. This causes the Amazon OpenSearch Service domain to generate document IDs. In case of multiple delivery attempts, this may cause the same record to be indexed more than once with different document IDs. This option enables write-heavy operations, such as the ingestion of logs and observability data, to consume less resources in the Amazon OpenSearch Service domain, resulting in improved performance.

AmazonopensearchserviceDestinationDescription -> (structure)

The destination in Amazon OpenSearch Service.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials.

DomainARN -> (string)

The ARN of the Amazon OpenSearch Service domain.

ClusterEndpoint -> (string)

The endpoint to use when communicating with the cluster. Firehose uses either this ClusterEndpoint or the DomainARN field to send data to Amazon OpenSearch Service.

IndexName -> (string)

The Amazon OpenSearch Service index name.

TypeName -> (string)

The Amazon OpenSearch Service type name. This applies to Elasticsearch 6.x and lower versions. For Elasticsearch 7.x and OpenSearch Service 1.x, thereâs no value for TypeName.

IndexRotationPeriod -> (string)

The Amazon OpenSearch Service index rotation period

BufferingHints -> (structure)

The buffering options.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

RetryOptions -> (structure)

The Amazon OpenSearch Service retry options.

DurationInSeconds -> (integer)

After an initial failure to deliver to Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

S3BackupMode -> (string)

The Amazon S3 backup mode.

S3DestinationDescription -> (structure)

Describes a destination in Amazon S3.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

ProcessingConfiguration -> (structure)

Describes a data processing configuration.

Enabled -> (boolean)

Enables or disables data processing.

Processors -> (list)

The data processors.

(structure)

Describes a data processor.

### Note

If you want to add a new line delimiter between records in objects that are delivered to Amazon S3, choose `AppendDelimiterToRecord` as a processor type. You donât have to put a processor parameter when you select `AppendDelimiterToRecord` .

Type -> (string)

The type of processor.

Parameters -> (list)

The processor parameters.

(structure)

Describes the processor parameter.

ParameterName -> (string)

The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds` . The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

ParameterValue -> (string)

The parameter value.

CloudWatchLoggingOptions -> (structure)

Describes the Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

VpcConfigurationDescription -> (structure)

The details of the VPC of the Amazon OpenSearch Service destination.

SubnetIds -> (list)

The IDs of the subnets that Firehose uses to create ENIs in the VPC of the Amazon OpenSearch Service destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon OpenSearch Service endpoints. Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.

The number of ENIs that Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Firehose can create up to three ENIs for this Firehose stream for each of the subnets specified here. For more information about ENI quota, see [Network Interfaces](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-enis) in the Amazon VPC Quotas topic.

(string)

RoleARN -> (string)

The ARN of the IAM role that the Firehose stream uses to create endpoints in the destination VPC. You can use your existing Firehose delivery role or you can specify a new role. In either case, make sure that the role trusts the Firehose service principal and that it grants the following permissions:

- `ec2:DescribeVpcs`
- `ec2:DescribeVpcAttribute`
- `ec2:DescribeSubnets`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeNetworkInterfaces`
- `ec2:CreateNetworkInterface`
- `ec2:CreateNetworkInterfacePermission`
- `ec2:DeleteNetworkInterface`

If you revoke these permissions after you create the Firehose stream, Firehose canât scale out by creating more ENIs when necessary. You might therefore see a degradation in performance.

SecurityGroupIds -> (list)

The IDs of the security groups that Firehose uses when it creates ENIs in the VPC of the Amazon OpenSearch Service destination. You can use the same security group that the Amazon ES domain uses or different ones. If you specify different security groups, ensure that they allow outbound HTTPS traffic to the Amazon OpenSearch Service domainâs security group. Also ensure that the Amazon OpenSearch Service domainâs security group allows HTTPS traffic from the security groups specified here. If you use the same security group for both your Firehose stream and the Amazon OpenSearch Service domain, make sure the security group inbound rule allows HTTPS traffic. For more information about security group rules, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules) in the Amazon VPC documentation.

(string)

VpcId -> (string)

The ID of the Amazon OpenSearch Service destinationâs VPC.

DocumentIdOptions -> (structure)

Indicates the method for setting up document ID. The supported methods are Firehose generated document ID and OpenSearch Service generated document ID.

DefaultDocumentIdFormat -> (string)

When the `FIREHOSE_DEFAULT` option is chosen, Firehose generates a unique document ID for each record based on a unique internal identifier. The generated document ID is stable across multiple delivery attempts, which helps prevent the same record from being indexed multiple times with different document IDs.

When the `NO_DOCUMENT_ID` option is chosen, Firehose does not include any document IDs in the requests it sends to the Amazon OpenSearch Service. This causes the Amazon OpenSearch Service domain to generate document IDs. In case of multiple delivery attempts, this may cause the same record to be indexed more than once with different document IDs. This option enables write-heavy operations, such as the ingestion of logs and observability data, to consume less resources in the Amazon OpenSearch Service domain, resulting in improved performance.

SplunkDestinationDescription -> (structure)

The destination in Splunk.

HECEndpoint -> (string)

The HTTP Event Collector (HEC) endpoint to which Firehose sends your data.

HECEndpointType -> (string)

This type can be either âRawâ or âEvent.â

HECToken -> (string)

A GUID you obtain from your Splunk cluster when you create a new HEC endpoint.

HECAcknowledgmentTimeoutInSeconds -> (integer)

The amount of time that Firehose waits to receive an acknowledgment from Splunk after it sends it data. At the end of the timeout period, Firehose either tries to send the data again or considers it an error, based on your retry settings.

RetryOptions -> (structure)

The retry behavior in case Firehose is unable to deliver data to Splunk or if it doesnât receive an acknowledgment of receipt from Splunk.

DurationInSeconds -> (integer)

The total amount of time that Firehose spends on retries. This duration starts after the initial attempt to send data to Splunk fails. It doesnât include the periods during which Firehose waits for acknowledgment from Splunk after each attempt.

S3BackupMode -> (string)

Defines how documents should be delivered to Amazon S3. When set to `FailedDocumentsOnly` , Firehose writes any data that could not be indexed to the configured Amazon S3 destination. When set to `AllDocuments` , Firehose delivers all incoming records to Amazon S3, and also writes failed documents to Amazon S3. Default value is `FailedDocumentsOnly` .

S3DestinationDescription -> (structure)

The Amazon S3 destination.>

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

ProcessingConfiguration -> (structure)

The data processing configuration.

Enabled -> (boolean)

Enables or disables data processing.

Processors -> (list)

The data processors.

(structure)

Describes a data processor.

### Note

If you want to add a new line delimiter between records in objects that are delivered to Amazon S3, choose `AppendDelimiterToRecord` as a processor type. You donât have to put a processor parameter when you select `AppendDelimiterToRecord` .

Type -> (string)

The type of processor.

Parameters -> (list)

The processor parameters.

(structure)

Describes the processor parameter.

ParameterName -> (string)

The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds` . The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

ParameterValue -> (string)

The parameter value.

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

BufferingHints -> (structure)

The buffering options. If no value is specified, the default values for Splunk are used.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 60 (1 minute).

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.

SecretsManagerConfiguration -> (structure)

The configuration that defines how you access secrets for Splunk.

SecretARN -> (string)

The ARN of the secret that stores your credentials. It must be in the same region as the Firehose stream and the role. The secret ARN can reside in a different account than the Firehose stream and role as Firehose supports cross-account secret access. This parameter is required when **Enabled** is set to `True` .

RoleARN -> (string)

Specifies the role that Firehose assumes when calling the Secrets Manager API operation. When you provide the role, it overrides any destination specific role defined in the destination configuration. If you do not provide the then we use the destination specific role. This parameter is required for Splunk.

Enabled -> (boolean)

Specifies whether you want to use the secrets manager feature. When set as `True` the secrets manager configuration overwrites the existing secrets in the destination configuration. When itâs set to `False` Firehose falls back to the credentials in the destination configuration.

HttpEndpointDestinationDescription -> (structure)

Describes the specified HTTP endpoint destination.

EndpointConfiguration -> (structure)

The configuration of the specified HTTP endpoint destination.

Url -> (string)

The URL of the HTTP endpoint selected as the destination.

Name -> (string)

The name of the HTTP endpoint selected as the destination.

BufferingHints -> (structure)

Describes buffering options that can be applied to the data before it is delivered to the HTTPS endpoint destination. Firehose teats these options as hints, and it might choose to use more optimal values. The `SizeInMBs` and `IntervalInSeconds` parameters are optional. However, if specify a value for one of them, you must also provide a value for the other.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).

CloudWatchLoggingOptions -> (structure)

Describes the Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

RequestConfiguration -> (structure)

The configuration of request sent to the HTTP endpoint specified as the destination.

ContentEncoding -> (string)

Firehose uses the content encoding to compress the body of a request before sending the request to the destination. For more information, see [Content-Encoding](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Encoding) in MDN Web Docs, the official Mozilla documentation.

CommonAttributes -> (list)

Describes the metadata sent to the HTTP endpoint destination.

(structure)

Describes the metadata thatâs delivered to the specified HTTP endpoint destination.

AttributeName -> (string)

The name of the HTTP endpoint common attribute.

AttributeValue -> (string)

The value of the HTTP endpoint common attribute.

ProcessingConfiguration -> (structure)

Describes a data processing configuration.

Enabled -> (boolean)

Enables or disables data processing.

Processors -> (list)

The data processors.

(structure)

Describes a data processor.

### Note

If you want to add a new line delimiter between records in objects that are delivered to Amazon S3, choose `AppendDelimiterToRecord` as a processor type. You donât have to put a processor parameter when you select `AppendDelimiterToRecord` .

Type -> (string)

The type of processor.

Parameters -> (list)

The processor parameters.

(structure)

Describes the processor parameter.

ParameterName -> (string)

The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds` . The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

ParameterValue -> (string)

The parameter value.

RoleARN -> (string)

Firehose uses this IAM role for all the permissions that the delivery stream needs.

RetryOptions -> (structure)

Describes the retry behavior in case Firehose is unable to deliver data to the specified HTTP endpoint destination, or if it doesnât receive a valid acknowledgment of receipt from the specified HTTP endpoint destination.

DurationInSeconds -> (integer)

The total amount of time that Firehose spends on retries. This duration starts after the initial attempt to send data to the custom destination via HTTPS endpoint fails. It doesnât include the periods during which Firehose waits for acknowledgment from the specified destination after each attempt.

S3BackupMode -> (string)

Describes the S3 bucket backup options for the data that Kinesis Firehose delivers to the HTTP endpoint destination. You can back up all documents (`AllData` ) or only the documents that Firehose could not deliver to the specified HTTP endpoint destination (`FailedDataOnly` ).

S3DestinationDescription -> (structure)

Describes a destination in Amazon S3.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

SecretsManagerConfiguration -> (structure)

The configuration that defines how you access secrets for HTTP Endpoint destination.

SecretARN -> (string)

The ARN of the secret that stores your credentials. It must be in the same region as the Firehose stream and the role. The secret ARN can reside in a different account than the Firehose stream and role as Firehose supports cross-account secret access. This parameter is required when **Enabled** is set to `True` .

RoleARN -> (string)

Specifies the role that Firehose assumes when calling the Secrets Manager API operation. When you provide the role, it overrides any destination specific role defined in the destination configuration. If you do not provide the then we use the destination specific role. This parameter is required for Splunk.

Enabled -> (boolean)

Specifies whether you want to use the secrets manager feature. When set as `True` the secrets manager configuration overwrites the existing secrets in the destination configuration. When itâs set to `False` Firehose falls back to the credentials in the destination configuration.

SnowflakeDestinationDescription -> (structure)

Optional description for the destination

AccountUrl -> (string)

URL for accessing your Snowflake account. This URL must include your [account identifier](https://docs.snowflake.com/en/user-guide/admin-account-identifier) . Note that the protocol ([https://](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/firehose/describe-delivery-stream.html)) and port number are optional.

User -> (string)

User login name for the Snowflake account.

Database -> (string)

All data in Snowflake is maintained in databases.

Schema -> (string)

Each database consists of one or more schemas, which are logical groupings of database objects, such as tables and views

Table -> (string)

All data in Snowflake is stored in database tables, logically structured as collections of columns and rows.

SnowflakeRoleConfiguration -> (structure)

Optionally configure a Snowflake role. Otherwise the default user role will be used.

Enabled -> (boolean)

Enable Snowflake role

SnowflakeRole -> (string)

The Snowflake role you wish to configure

DataLoadingOption -> (string)

Choose to load JSON keys mapped to table column names or choose to split the JSON payload where content is mapped to a record content column and source metadata is mapped to a record metadata column.

MetaDataColumnName -> (string)

The name of the record metadata column

ContentColumnName -> (string)

The name of the record content column

SnowflakeVpcConfiguration -> (structure)

The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see [Amazon PrivateLink & Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink)

PrivateLinkVpceId -> (string)

The VPCE ID for Firehose to privately connect with Snowflake. The ID format is com.amazonaws.vpce.[region].vpce-svc-<[id]>. For more information, see [Amazon PrivateLink & Snowflake](https://docs.snowflake.com/en/user-guide/admin-security-privatelink)

CloudWatchLoggingOptions -> (structure)

Describes the Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

ProcessingConfiguration -> (structure)

Describes a data processing configuration.

Enabled -> (boolean)

Enables or disables data processing.

Processors -> (list)

The data processors.

(structure)

Describes a data processor.

### Note

If you want to add a new line delimiter between records in objects that are delivered to Amazon S3, choose `AppendDelimiterToRecord` as a processor type. You donât have to put a processor parameter when you select `AppendDelimiterToRecord` .

Type -> (string)

The type of processor.

Parameters -> (list)

The processor parameters.

(structure)

Describes the processor parameter.

ParameterName -> (string)

The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds` . The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

ParameterValue -> (string)

The parameter value.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Snowflake role

RetryOptions -> (structure)

The time period where Firehose will retry sending data to the chosen HTTP endpoint.

DurationInSeconds -> (integer)

the time period where Firehose will retry sending data to the chosen HTTP endpoint.

S3BackupMode -> (string)

Choose an S3 backup mode

S3DestinationDescription -> (structure)

Describes a destination in Amazon S3.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

SecretsManagerConfiguration -> (structure)

The configuration that defines how you access secrets for Snowflake.

SecretARN -> (string)

The ARN of the secret that stores your credentials. It must be in the same region as the Firehose stream and the role. The secret ARN can reside in a different account than the Firehose stream and role as Firehose supports cross-account secret access. This parameter is required when **Enabled** is set to `True` .

RoleARN -> (string)

Specifies the role that Firehose assumes when calling the Secrets Manager API operation. When you provide the role, it overrides any destination specific role defined in the destination configuration. If you do not provide the then we use the destination specific role. This parameter is required for Splunk.

Enabled -> (boolean)

Specifies whether you want to use the secrets manager feature. When set as `True` the secrets manager configuration overwrites the existing secrets in the destination configuration. When itâs set to `False` Firehose falls back to the credentials in the destination configuration.

BufferingHints -> (structure)

Describes the buffering to perform before delivering data to the Snowflake destination. If you do not specify any value, Firehose uses the default values.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 128.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 0.

AmazonOpenSearchServerlessDestinationDescription -> (structure)

The destination in the Serverless offering for Amazon OpenSearch Service.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials.

CollectionEndpoint -> (string)

The endpoint to use when communicating with the collection in the Serverless offering for Amazon OpenSearch Service.

IndexName -> (string)

The Serverless offering for Amazon OpenSearch Service index name.

BufferingHints -> (structure)

The buffering options.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300 (5 minutes).

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MBs, before delivering it to the destination. The default value is 5.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MB/sec, the value should be 10 MB or higher.

RetryOptions -> (structure)

The Serverless offering for Amazon OpenSearch Service retry options.

DurationInSeconds -> (integer)

After an initial failure to deliver to the Serverless offering for Amazon OpenSearch Service, the total amount of time during which Firehose retries delivery (including the first attempt). After this time has elapsed, the failed documents are written to Amazon S3. Default value is 300 seconds (5 minutes). A value of 0 (zero) results in no retries.

S3BackupMode -> (string)

The Amazon S3 backup mode.

S3DestinationDescription -> (structure)

Describes a destination in Amazon S3.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

ProcessingConfiguration -> (structure)

Describes a data processing configuration.

Enabled -> (boolean)

Enables or disables data processing.

Processors -> (list)

The data processors.

(structure)

Describes a data processor.

### Note

If you want to add a new line delimiter between records in objects that are delivered to Amazon S3, choose `AppendDelimiterToRecord` as a processor type. You donât have to put a processor parameter when you select `AppendDelimiterToRecord` .

Type -> (string)

The type of processor.

Parameters -> (list)

The processor parameters.

(structure)

Describes the processor parameter.

ParameterName -> (string)

The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds` . The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

ParameterValue -> (string)

The parameter value.

CloudWatchLoggingOptions -> (structure)

Describes the Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

VpcConfigurationDescription -> (structure)

The details of the VPC of the Amazon OpenSearch Service destination.

SubnetIds -> (list)

The IDs of the subnets that Firehose uses to create ENIs in the VPC of the Amazon OpenSearch Service destination. Make sure that the routing tables and inbound and outbound rules allow traffic to flow from the subnets whose IDs are specified here to the subnets that have the destination Amazon OpenSearch Service endpoints. Firehose creates at least one ENI in each of the subnets that are specified here. Do not delete or modify these ENIs.

The number of ENIs that Firehose creates in the subnets specified here scales up and down automatically based on throughput. To enable Firehose to scale up the number of ENIs to match throughput, ensure that you have sufficient quota. To help you calculate the quota you need, assume that Firehose can create up to three ENIs for this Firehose stream for each of the subnets specified here. For more information about ENI quota, see [Network Interfaces](https://docs.aws.amazon.com/vpc/latest/userguide/amazon-vpc-limits.html#vpc-limits-enis) in the Amazon VPC Quotas topic.

(string)

RoleARN -> (string)

The ARN of the IAM role that the Firehose stream uses to create endpoints in the destination VPC. You can use your existing Firehose delivery role or you can specify a new role. In either case, make sure that the role trusts the Firehose service principal and that it grants the following permissions:

- `ec2:DescribeVpcs`
- `ec2:DescribeVpcAttribute`
- `ec2:DescribeSubnets`
- `ec2:DescribeSecurityGroups`
- `ec2:DescribeNetworkInterfaces`
- `ec2:CreateNetworkInterface`
- `ec2:CreateNetworkInterfacePermission`
- `ec2:DeleteNetworkInterface`

If you revoke these permissions after you create the Firehose stream, Firehose canât scale out by creating more ENIs when necessary. You might therefore see a degradation in performance.

SecurityGroupIds -> (list)

The IDs of the security groups that Firehose uses when it creates ENIs in the VPC of the Amazon OpenSearch Service destination. You can use the same security group that the Amazon ES domain uses or different ones. If you specify different security groups, ensure that they allow outbound HTTPS traffic to the Amazon OpenSearch Service domainâs security group. Also ensure that the Amazon OpenSearch Service domainâs security group allows HTTPS traffic from the security groups specified here. If you use the same security group for both your Firehose stream and the Amazon OpenSearch Service domain, make sure the security group inbound rule allows HTTPS traffic. For more information about security group rules, see [Security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#SecurityGroupRules) in the Amazon VPC documentation.

(string)

VpcId -> (string)

The ID of the Amazon OpenSearch Service destinationâs VPC.

IcebergDestinationDescription -> (structure)

Describes a destination in Apache Iceberg Tables.

DestinationTableConfigurationList -> (list)

Provides a list of `DestinationTableConfigurations` which Firehose uses to deliver data to Apache Iceberg Tables. Firehose will write data with insert if table specific configuration is not provided here.

(structure)

Describes the configuration of a destination in Apache Iceberg Tables.

DestinationTableName -> (string)

Specifies the name of the Apache Iceberg Table.

DestinationDatabaseName -> (string)

The name of the Apache Iceberg database.

UniqueKeys -> (list)

A list of unique keys for a given Apache Iceberg table. Firehose will use these for running Create, Update, or Delete operations on the given Iceberg table.

(string)

PartitionSpec -> (structure)

The partition spec configuration for a table that is used by automatic table creation.

Amazon Data Firehose is in preview release and is subject to change.

Identity -> (list)

List of identity [transforms](https://iceberg.apache.org/spec/#partition-transforms) that performs an identity transformation. The transform takes the source value, and does not modify it. Result type is the source type.

Amazon Data Firehose is in preview release and is subject to change.

(structure)

Represents a single field in a `PartitionSpec` .

Amazon Data Firehose is in preview release and is subject to change.

SourceName -> (string)

The column name to be configured in partition spec.

Amazon Data Firehose is in preview release and is subject to change.

S3ErrorOutputPrefix -> (string)

The table specific S3 error output prefix. All the errors that occurred while delivering to this table will be prefixed with this value in S3 destination.

SchemaEvolutionConfiguration -> (structure)

The description of automatic schema evolution configuration.

Amazon Data Firehose is in preview release and is subject to change.

Enabled -> (boolean)

Specify whether you want to enable schema evolution.

Amazon Data Firehose is in preview release and is subject to change.

TableCreationConfiguration -> (structure)

The description of table creation configuration.

Amazon Data Firehose is in preview release and is subject to change.

Enabled -> (boolean)

Specify whether you want to enable automatic table creation.

Amazon Data Firehose is in preview release and is subject to change.

BufferingHints -> (structure)

Describes hints for the buffering to perform before delivering data to the destination. These options are treated as hints, and therefore Firehose might choose to use different values when it is optimal. The `SizeInMBs` and `IntervalInSeconds` parameters are optional. However, if specify a value for one of them, you must also provide a value for the other.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CloudWatchLoggingOptions -> (structure)

Describes the Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

ProcessingConfiguration -> (structure)

Describes a data processing configuration.

Enabled -> (boolean)

Enables or disables data processing.

Processors -> (list)

The data processors.

(structure)

Describes a data processor.

### Note

If you want to add a new line delimiter between records in objects that are delivered to Amazon S3, choose `AppendDelimiterToRecord` as a processor type. You donât have to put a processor parameter when you select `AppendDelimiterToRecord` .

Type -> (string)

The type of processor.

Parameters -> (list)

The processor parameters.

(structure)

Describes the processor parameter.

ParameterName -> (string)

The name of the parameter. Currently the following default values are supported: 3 for `NumberOfRetries` and 60 for the `BufferIntervalInSeconds` . The `BufferSizeInMBs` ranges between 0.2 MB and up to 3MB. The default buffering hint is 1MB for all destinations, except Splunk. For Splunk, the default buffering hint is 256 KB.

ParameterValue -> (string)

The parameter value.

S3BackupMode -> (string)

Describes how Firehose will backup records. Currently,Firehose only supports `FailedDataOnly` .

RetryOptions -> (structure)

The retry behavior in case Firehose is unable to deliver data to a destination.

DurationInSeconds -> (integer)

The period of time during which Firehose retries to deliver data to the specified destination.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the IAM role to be assumed by Firehose for calling Apache Iceberg Tables.

AppendOnly -> (boolean)

Describes whether all incoming data for this delivery stream will be append only (inserts only and not for updates and deletes) for Iceberg delivery. This feature is only applicable for Apache Iceberg Tables.

The default value is false. If you set this value to true, Firehose automatically increases the throughput limit of a stream based on the throttling levels of the stream. If you set this parameter to true for a stream with updates and deletes, you will see out of order delivery.

CatalogConfiguration -> (structure)

Configuration describing where the destination Iceberg tables are persisted.

CatalogARN -> (string)

Specifies the Glue catalog ARN identifier of the destination Apache Iceberg Tables. You must specify the ARN in the format `arn:aws:glue:region:account-id:catalog` .

WarehouseLocation -> (string)

The warehouse location for Apache Iceberg tables. You must configure this when schema evolution and table creation is enabled.

Amazon Data Firehose is in preview release and is subject to change.

S3DestinationDescription -> (structure)

Describes a destination in Amazon S3.

RoleARN -> (string)

The Amazon Resource Name (ARN) of the Amazon Web Services credentials. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

BucketARN -> (string)

The ARN of the S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

Prefix -> (string)

The âYYYY/MM/DD/HHâ time format prefix is automatically used for delivered Amazon S3 files. You can also specify a custom prefix, as described in [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

ErrorOutputPrefix -> (string)

A prefix that Firehose evaluates and adds to failed records before writing them to S3. This prefix appears immediately following the bucket name. For information about how to specify this prefix, see [Custom Prefixes for Amazon S3 Objects](https://docs.aws.amazon.com/firehose/latest/dev/s3-prefixes.html) .

BufferingHints -> (structure)

The buffering option. If no value is specified, `BufferingHints` object default values are used.

SizeInMBs -> (integer)

Buffer incoming data to the specified size, in MiBs, before delivering it to the destination. The default value is 5. This parameter is optional but if you specify a value for it, you must also specify a value for `IntervalInSeconds` , and vice versa.

We recommend setting this parameter to a value greater than the amount of data you typically ingest into the Firehose stream in 10 seconds. For example, if you typically ingest data at 1 MiB/sec, the value should be 10 MiB or higher.

IntervalInSeconds -> (integer)

Buffer incoming data for the specified period of time, in seconds, before delivering it to the destination. The default value is 300. This parameter is optional but if you specify a value for it, you must also specify a value for `SizeInMBs` , and vice versa.

CompressionFormat -> (string)

The compression format. If no value is specified, the default is `UNCOMPRESSED` .

EncryptionConfiguration -> (structure)

The encryption configuration. If no value is specified, the default is no encryption.

NoEncryptionConfig -> (string)

Specifically override existing encryption information to ensure that no encryption is used.

KMSEncryptionConfig -> (structure)

The encryption key.

AWSKMSKeyARN -> (string)

The Amazon Resource Name (ARN) of the encryption key. Must belong to the same Amazon Web Services Region as the destination Amazon S3 bucket. For more information, see [Amazon Resource Names (ARNs) and Amazon Web Services Service Namespaces](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) .

CloudWatchLoggingOptions -> (structure)

The Amazon CloudWatch logging options for your Firehose stream.

Enabled -> (boolean)

Enables or disables CloudWatch logging.

LogGroupName -> (string)

The CloudWatch group name for logging. This value is required if CloudWatch logging is enabled.

LogStreamName -> (string)

The CloudWatch log stream name for logging. This value is required if CloudWatch logging is enabled.

HasMoreDestinations -> (boolean)

Indicates whether there are more destinations available to list.