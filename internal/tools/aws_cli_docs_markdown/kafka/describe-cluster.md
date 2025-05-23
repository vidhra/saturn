# describe-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/describe-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kafka](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafka/index.html#cli-aws-kafka) ]

# describe-cluster

## Description

Returns a description of the MSK cluster whose Amazon Resource Name (ARN) is specified in the request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kafka-2018-11-14/DescribeCluster)

## Synopsis

```
describe-cluster
--cluster-arn <value>
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

`--cluster-arn` (string)

The Amazon Resource Name (ARN) that uniquely identifies the cluster.

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

**To describe a cluster**

The following `describe-cluster` example describes an Amazon MSK cluster.

```
aws kafka describe-cluster \
    --cluster-arn arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5
```

Output:

```
{
    "ClusterInfo": {
        "BrokerNodeGroupInfo": {
            "BrokerAZDistribution": "DEFAULT",
            "ClientSubnets": [
                "subnet-cbfff283",
                "subnet-6746046b"
            ],
            "InstanceType": "kafka.m5.large",
            "SecurityGroups": [
                "sg-f839b688"
            ],
            "StorageInfo": {
                "EbsStorageInfo": {
                    "VolumeSize": 100
                }
            }
        },
        "ClusterArn": "arn:aws:kafka:us-east-1:123456789012:cluster/demo-cluster-1/6357e0b2-0e6a-4b86-a0b4-70df934c2e31-5",
        "ClusterName": "demo-cluster-1",
        "CreationTime": "2020-07-09T02:31:36.223000+00:00",
        "CurrentBrokerSoftwareInfo": {
            "KafkaVersion": "2.2.1"
        },
        "CurrentVersion": "K3AEGXETSR30VB",
        "EncryptionInfo": {
            "EncryptionAtRest": {
                "DataVolumeKMSKeyId": "arn:aws:kms:us-east-1:123456789012:key/a7ca56d5-0768-4b64-a670-339a9fbef81c"
            },
            "EncryptionInTransit": {
                "ClientBroker": "TLS_PLAINTEXT",
                "InCluster": true
            }
        },
        "EnhancedMonitoring": "DEFAULT",
        "OpenMonitoring": {
            "Prometheus": {
                "JmxExporter": {
                    "EnabledInBroker": false
                },
                "NodeExporter": {
                    "EnabledInBroker": false
                }
            }
        },
        "NumberOfBrokerNodes": 2,
        "State": "ACTIVE",
        "Tags": {},
        "ZookeeperConnectString": "z-2.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:2181,z-1.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:2181,z-3.demo-cluster-1.xuy0sb.c5.kafka.us-east-1.amazonaws.com:2181"
    }
}
```

For more information, see [Listing Amazon MSK Clusters](https://docs.aws.amazon.com/msk/latest/developerguide/msk-list-clusters.html) in the *Amazon Managed Streaming for Apache Kafka Developer Guide*.

## Output

ClusterInfo -> (structure)

The cluster information.

ActiveOperationArn -> (string)

Arn of active cluster operation.

BrokerNodeGroupInfo -> (structure)

Information about the broker nodes.

BrokerAZDistribution -> (string)

The distribution of broker nodes across Availability Zones. This is an optional parameter. If you donât specify it, Amazon MSK gives it the value DEFAULT. You can also explicitly set this parameter to the value DEFAULT. No other values are currently allowed.

Amazon MSK distributes the broker nodes evenly across the Availability Zones that correspond to the subnets you provide when you create the cluster.

ClientSubnets -> (list)

The list of subnets to connect to in the client virtual private cloud (VPC). AWS creates elastic network interfaces inside these subnets. Client applications use elastic network interfaces to produce and consume data. Client subnets canât occupy the Availability Zone with ID use use1-az3.

(string)

InstanceType -> (string)

The type of Amazon EC2 instances to use for Apache Kafka brokers. The following instance types are allowed: kafka.m5.large, kafka.m5.xlarge, kafka.m5.2xlarge, kafka.m5.4xlarge, kafka.m5.12xlarge, and kafka.m5.24xlarge.

SecurityGroups -> (list)

The AWS security groups to associate with the elastic network interfaces in order to specify who can connect to and communicate with the Amazon MSK cluster. If you donât specify a security group, Amazon MSK uses the default security group associated with the VPC.

(string)

StorageInfo -> (structure)

Contains information about storage volumes attached to MSK broker nodes.

EbsStorageInfo -> (structure)

EBS volume information.

ProvisionedThroughput -> (structure)

EBS volume provisioned throughput information.

Enabled -> (boolean)

Provisioned throughput is enabled or not.

VolumeThroughput -> (integer)

Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second.

VolumeSize -> (integer)

The size in GiB of the EBS volume for the data drive on each broker node.

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

ZoneIds -> (list)

The list of zoneIds for the cluster in the virtual private cloud (VPC).

(string)

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

ClusterArn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies the cluster.

ClusterName -> (string)

The name of the cluster.

CreationTime -> (timestamp)

The time when the cluster was created.

CurrentBrokerSoftwareInfo -> (structure)

Information about the version of software currently deployed on the Apache Kafka brokers in the cluster.

ConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the configuration used for the cluster. This field isnât visible in this preview release.

ConfigurationRevision -> (long)

The revision of the configuration to use. This field isnât visible in this preview release.

KafkaVersion -> (string)

The version of Apache Kafka.

CurrentVersion -> (string)

The current version of the MSK cluster.

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

EnhancedMonitoring -> (string)

Specifies which metrics are gathered for the MSK cluster. This property has the following possible values: DEFAULT, PER_BROKER, PER_TOPIC_PER_BROKER, and PER_TOPIC_PER_PARTITION. For a list of the metrics associated with each of these levels of monitoring, see [Monitoring](https://docs.aws.amazon.com/msk/latest/developerguide/monitoring.html) .

OpenMonitoring -> (structure)

Settings for open monitoring using Prometheus.

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

LoggingInfo -> (structure)

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

NumberOfBrokerNodes -> (integer)

The number of broker nodes in the cluster.

State -> (string)

The state of the cluster. The possible states are ACTIVE, CREATING, DELETING, FAILED, HEALING, MAINTENANCE, REBOOTING_BROKER, and UPDATING.

StateInfo -> (structure)

Code -> (string)

Message -> (string)

Tags -> (map)

Tags attached to the cluster.

key -> (string)

value -> (string)

ZookeeperConnectString -> (string)

The connection string to use to connect to the Apache ZooKeeper cluster.

ZookeeperConnectStringTls -> (string)

The connection string to use to connect to zookeeper cluster on Tls port.

StorageMode -> (string)

This controls storage mode for supported storage tiers.

CustomerActionStatus -> (string)

Determines if there is an action required from the customer.