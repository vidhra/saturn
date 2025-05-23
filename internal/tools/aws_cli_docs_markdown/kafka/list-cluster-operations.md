# list-cluster-operationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/list-cluster-operations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/list-cluster-operations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kafka](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/index.html#cli-aws-kafka) ]

# list-cluster-operations

## Description

Returns a list of all the operations that have been performed on the specified MSK cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/ListClusterOperations)

`list-cluster-operations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ClusterOperationInfoList`

## Synopsis

```
list-cluster-operations
--cluster-arn <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--cluster-arn` (string)

The Amazon Resource Name (ARN) that uniquely identifies the cluster.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

ClusterOperationInfoList -> (list)

An array of cluster operation information objects.

(structure)

Returns information about a cluster operation.

ClientRequestId -> (string)

The ID of the API request that triggered this operation.

ClusterArn -> (string)

ARN of the cluster.

CreationTime -> (timestamp)

The time that the operation was created.

EndTime -> (timestamp)

The time at which the operation finished.

ErrorInfo -> (structure)

Describes the error if the operation fails.

ErrorCode -> (string)

A number describing the error programmatically.

ErrorString -> (string)

An optional field to provide more details about the error.

OperationArn -> (string)

ARN of the cluster operation.

OperationState -> (string)

State of the cluster operation.

OperationSteps -> (list)

Steps completed during the operation.

(structure)

Step taken during a cluster operation.

StepInfo -> (structure)

Information about the step and its status.

StepStatus -> (string)

The steps current status.

StepName -> (string)

The name of the step.

OperationType -> (string)

Type of the cluster operation.

SourceClusterInfo -> (structure)

Information about cluster attributes before a cluster is updated.

BrokerEBSVolumeInfo -> (list)

Specifies the size of the EBS volume and the ID of the associated broker.

(structure)

Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword ALL. This means the changes apply to all the brokers in the cluster.

KafkaBrokerNodeId -> (string)

The ID of the broker to update.

ProvisionedThroughput -> (structure)

EBS volume provisioned throughput information.

Enabled -> (boolean)

Provisioned throughput is enabled or not.

VolumeThroughput -> (integer)

Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second.

VolumeSizeGB -> (integer)

Size of the EBS volume to update.

ConfigurationInfo -> (structure)

Information about the changes in the configuration of the brokers.

Arn -> (string)

ARN of the configuration to use.

Revision -> (long)

The revision of the configuration to use.

NumberOfBrokerNodes -> (integer)

The number of broker nodes in the cluster.

EnhancedMonitoring -> (string)

Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster.

OpenMonitoring -> (structure)

The settings for open monitoring.

Prometheus -> (structure)

Prometheus settings.

JmxExporter -> (structure)

Indicates whether you want to turn on or turn off the JMX Exporter.

EnabledInBroker -> (boolean)

Indicates whether you want to turn on or turn off the JMX Exporter.

NodeExporter -> (structure)

Indicates whether you want to turn on or turn off the Node Exporter.

EnabledInBroker -> (boolean)

Indicates whether you want to turn on or turn off the Node Exporter.

KafkaVersion -> (string)

The Apache Kafka version.

LoggingInfo -> (structure)

You can configure your MSK cluster to send broker logs to different destination types. This is a container for the configuration details related to broker logs.

BrokerLogs -> (structure)

CloudWatchLogs -> (structure)

Enabled -> (boolean)

LogGroup -> (string)

Firehose -> (structure)

DeliveryStream -> (string)

Enabled -> (boolean)

S3 -> (structure)

Bucket -> (string)

Enabled -> (boolean)

Prefix -> (string)

InstanceType -> (string)

Information about the Amazon MSK broker type.

ClientAuthentication -> (structure)

Includes all client authentication information.

Sasl -> (structure)

Details for ClientAuthentication using SASL.

Scram -> (structure)

Details for SASL/SCRAM client authentication.

Enabled -> (boolean)

SASL/SCRAM authentication is enabled or not.

Iam -> (structure)

Indicates whether IAM access control is enabled.

Enabled -> (boolean)

Indicates whether IAM access control is enabled.

Tls -> (structure)

Details for ClientAuthentication using TLS.

CertificateAuthorityArnList -> (list)

List of ACM Certificate Authority ARNs.

(string)

Enabled -> (boolean)

Specifies whether you want to turn on or turn off TLS authentication.

Unauthenticated -> (structure)

Contains information about unauthenticated traffic to the cluster.

Enabled -> (boolean)

Specifies whether you want to turn on or turn off unauthenticated traffic to your cluster.

EncryptionInfo -> (structure)

Includes all encryption-related information.

EncryptionAtRest -> (structure)

The data-volume encryption details.

DataVolumeKMSKeyId -> (string)

The ARN of the AWS KMS key for encrypting data at rest. If you donât specify a KMS key, MSK creates one for you and uses it.

EncryptionInTransit -> (structure)

The details for encryption in transit.

ClientBroker -> (string)

Indicates the encryption setting for data in transit between clients and brokers. The following are the possible values.

TLS means that client-broker communication is enabled with TLS only.

TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.

PLAINTEXT means that client-broker communication is enabled in plaintext only.

The default value is TLS_PLAINTEXT.

InCluster -> (boolean)

When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.

The default value is true.

ConnectivityInfo -> (structure)

Information about the broker access configuration.

PublicAccess -> (structure)

Public access control for brokers.

Type -> (string)

The value DISABLED indicates that public access is turned off. SERVICE_PROVIDED_EIPS indicates that public access is turned on.

VpcConnectivity -> (structure)

VPC connectivity access control for brokers.

ClientAuthentication -> (structure)

Includes all client authentication information for VPC connectivity.

Sasl -> (structure)

SASL authentication type details for VPC connectivity.

Scram -> (structure)

Details for SASL/SCRAM client authentication for VPC connectivity.

Enabled -> (boolean)

SASL/SCRAM authentication is on or off for VPC connectivity.

Iam -> (structure)

Details for SASL/IAM client authentication for VPC connectivity.

Enabled -> (boolean)

SASL/IAM authentication is on or off for VPC connectivity.

Tls -> (structure)

TLS authentication type details for VPC connectivity.

Enabled -> (boolean)

TLS authentication is on or off for VPC connectivity.

StorageMode -> (string)

This controls storage mode for supported storage tiers.

BrokerCountUpdateInfo -> (structure)

Describes brokers being changed during a broker count update.

CreatedBrokerIds -> (list)

Kafka Broker IDs of brokers being created.

(double)

DeletedBrokerIds -> (list)

Kafka Broker IDs of brokers being deleted.

(double)

TargetClusterInfo -> (structure)

Information about cluster attributes after a cluster is updated.

BrokerEBSVolumeInfo -> (list)

Specifies the size of the EBS volume and the ID of the associated broker.

(structure)

Specifies the EBS volume upgrade information. The broker identifier must be set to the keyword ALL. This means the changes apply to all the brokers in the cluster.

KafkaBrokerNodeId -> (string)

The ID of the broker to update.

ProvisionedThroughput -> (structure)

EBS volume provisioned throughput information.

Enabled -> (boolean)

Provisioned throughput is enabled or not.

VolumeThroughput -> (integer)

Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second.

VolumeSizeGB -> (integer)

Size of the EBS volume to update.

ConfigurationInfo -> (structure)

Information about the changes in the configuration of the brokers.

Arn -> (string)

ARN of the configuration to use.

Revision -> (long)

The revision of the configuration to use.

NumberOfBrokerNodes -> (integer)

The number of broker nodes in the cluster.

EnhancedMonitoring -> (string)

Specifies which Apache Kafka metrics Amazon MSK gathers and sends to Amazon CloudWatch for this cluster.

OpenMonitoring -> (structure)

The settings for open monitoring.

Prometheus -> (structure)

Prometheus settings.

JmxExporter -> (structure)

Indicates whether you want to turn on or turn off the JMX Exporter.

EnabledInBroker -> (boolean)

Indicates whether you want to turn on or turn off the JMX Exporter.

NodeExporter -> (structure)

Indicates whether you want to turn on or turn off the Node Exporter.

EnabledInBroker -> (boolean)

Indicates whether you want to turn on or turn off the Node Exporter.

KafkaVersion -> (string)

The Apache Kafka version.

LoggingInfo -> (structure)

You can configure your MSK cluster to send broker logs to different destination types. This is a container for the configuration details related to broker logs.

BrokerLogs -> (structure)

CloudWatchLogs -> (structure)

Enabled -> (boolean)

LogGroup -> (string)

Firehose -> (structure)

DeliveryStream -> (string)

Enabled -> (boolean)

S3 -> (structure)

Bucket -> (string)

Enabled -> (boolean)

Prefix -> (string)

InstanceType -> (string)

Information about the Amazon MSK broker type.

ClientAuthentication -> (structure)

Includes all client authentication information.

Sasl -> (structure)

Details for ClientAuthentication using SASL.

Scram -> (structure)

Details for SASL/SCRAM client authentication.

Enabled -> (boolean)

SASL/SCRAM authentication is enabled or not.

Iam -> (structure)

Indicates whether IAM access control is enabled.

Enabled -> (boolean)

Indicates whether IAM access control is enabled.

Tls -> (structure)

Details for ClientAuthentication using TLS.

CertificateAuthorityArnList -> (list)

List of ACM Certificate Authority ARNs.

(string)

Enabled -> (boolean)

Specifies whether you want to turn on or turn off TLS authentication.

Unauthenticated -> (structure)

Contains information about unauthenticated traffic to the cluster.

Enabled -> (boolean)

Specifies whether you want to turn on or turn off unauthenticated traffic to your cluster.

EncryptionInfo -> (structure)

Includes all encryption-related information.

EncryptionAtRest -> (structure)

The data-volume encryption details.

DataVolumeKMSKeyId -> (string)

The ARN of the AWS KMS key for encrypting data at rest. If you donât specify a KMS key, MSK creates one for you and uses it.

EncryptionInTransit -> (structure)

The details for encryption in transit.

ClientBroker -> (string)

Indicates the encryption setting for data in transit between clients and brokers. The following are the possible values.

TLS means that client-broker communication is enabled with TLS only.

TLS_PLAINTEXT means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.

PLAINTEXT means that client-broker communication is enabled in plaintext only.

The default value is TLS_PLAINTEXT.

InCluster -> (boolean)

When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.

The default value is true.

ConnectivityInfo -> (structure)

Information about the broker access configuration.

PublicAccess -> (structure)

Public access control for brokers.

Type -> (string)

The value DISABLED indicates that public access is turned off. SERVICE_PROVIDED_EIPS indicates that public access is turned on.

VpcConnectivity -> (structure)

VPC connectivity access control for brokers.

ClientAuthentication -> (structure)

Includes all client authentication information for VPC connectivity.

Sasl -> (structure)

SASL authentication type details for VPC connectivity.

Scram -> (structure)

Details for SASL/SCRAM client authentication for VPC connectivity.

Enabled -> (boolean)

SASL/SCRAM authentication is on or off for VPC connectivity.

Iam -> (structure)

Details for SASL/IAM client authentication for VPC connectivity.

Enabled -> (boolean)

SASL/IAM authentication is on or off for VPC connectivity.

Tls -> (structure)

TLS authentication type details for VPC connectivity.

Enabled -> (boolean)

TLS authentication is on or off for VPC connectivity.

StorageMode -> (string)

This controls storage mode for supported storage tiers.

BrokerCountUpdateInfo -> (structure)

Describes brokers being changed during a broker count update.

CreatedBrokerIds -> (list)

Kafka Broker IDs of brokers being created.

(double)

DeletedBrokerIds -> (list)

Kafka Broker IDs of brokers being deleted.

(double)

VpcConnectionInfo -> (structure)

Description of the VPC connection for CreateVpcConnection and DeleteVpcConnection operations.

VpcConnectionArn -> (string)

The Amazon Resource Name (ARN) of the VPC connection.

Owner -> (string)

The owner of the VPC Connection.

UserIdentity -> (structure)

Description of the requester that calls the API operation.

Type -> (string)

The identity type of the requester that calls the API operation.

PrincipalId -> (string)

A unique identifier for the requester that calls the API operation.

CreationTime -> (timestamp)

The time when Amazon MSK creates the VPC Connnection.

NextToken -> (string)

If the response of ListClusterOperations is truncated, it returns a NextToken in the response. This Nexttoken should be sent in the subsequent request to ListClusterOperations.