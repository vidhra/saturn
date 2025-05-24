# list-connectorsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafkaconnect/list-connectors.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafkaconnect/list-connectors.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kafkaconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kafkaconnect/index.html#cli-aws-kafkaconnect) ]

# list-connectors

## Description

Returns a list of all the connectors in this account and Region. The list is limited to connectors whose name starts with the specified prefix. The response also includes a description of each of the listed connectors.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kafkaconnect-2021-09-14/ListConnectors)

`list-connectors` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `connectors`

## Synopsis

```
list-connectors
[--connector-name-prefix <value>]
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

`--connector-name-prefix` (string)

The name prefix that you want to use to search for and list connectors.

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

connectors -> (list)

An array of connector descriptions.

(structure)

Summary of a connector.

capacity -> (structure)

The connectorâs compute capacity settings.

autoScaling -> (structure)

Describes the connectorâs auto scaling capacity.

maxWorkerCount -> (integer)

The maximum number of workers allocated to the connector.

mcuCount -> (integer)

The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.

minWorkerCount -> (integer)

The minimum number of workers allocated to the connector.

scaleInPolicy -> (structure)

The sacle-in policy for the connector.

cpuUtilizationPercentage -> (integer)

Specifies the CPU utilization percentage threshold at which you want connector scale in to be triggered.

scaleOutPolicy -> (structure)

The sacle-out policy for the connector.>

cpuUtilizationPercentage -> (integer)

The CPU utilization percentage threshold at which you want connector scale out to be triggered.

provisionedCapacity -> (structure)

Describes a connectorâs provisioned capacity.

mcuCount -> (integer)

The number of microcontroller units (MCUs) allocated to each connector worker. The valid values are 1,2,4,8.

workerCount -> (integer)

The number of workers that are allocated to the connector.

connectorArn -> (string)

The Amazon Resource Name (ARN) of the connector.

connectorDescription -> (string)

The description of the connector.

connectorName -> (string)

The name of the connector.

connectorState -> (string)

The state of the connector.

creationTime -> (timestamp)

The time that the connector was created.

currentVersion -> (string)

The current version of the connector.

kafkaCluster -> (structure)

The details of the Apache Kafka cluster to which the connector is connected.

apacheKafkaCluster -> (structure)

The Apache Kafka cluster to which the connector is connected.

bootstrapServers -> (string)

The bootstrap servers of the cluster.

vpc -> (structure)

Details of an Amazon VPC which has network connectivity to the Apache Kafka cluster.

securityGroups -> (list)

The security groups for the connector.

(string)

subnets -> (list)

The subnets for the connector.

(string)

kafkaClusterClientAuthentication -> (structure)

The type of client authentication used to connect to the Apache Kafka cluster. The value is NONE when no client authentication is used.

authenticationType -> (string)

The type of client authentication used to connect to the Apache Kafka cluster. Value NONE means that no client authentication is used.

kafkaClusterEncryptionInTransit -> (structure)

Details of encryption in transit to the Apache Kafka cluster.

encryptionType -> (string)

The type of encryption in transit to the Apache Kafka cluster.

kafkaConnectVersion -> (string)

The version of Kafka Connect. It has to be compatible with both the Apache Kafka clusterâs version and the plugins.

logDelivery -> (structure)

The settings for delivering connector logs to Amazon CloudWatch Logs.

workerLogDelivery -> (structure)

The workers can send worker logs to different destination types. This configuration specifies the details of these destinations.

cloudWatchLogs -> (structure)

Details about delivering logs to Amazon CloudWatch Logs.

enabled -> (boolean)

Whether log delivery to Amazon CloudWatch Logs is enabled.

logGroup -> (string)

The name of the CloudWatch log group that is the destination for log delivery.

firehose -> (structure)

Details about delivering logs to Amazon Kinesis Data Firehose.

deliveryStream -> (string)

The name of the Kinesis Data Firehose delivery stream that is the destination for log delivery.

enabled -> (boolean)

Specifies whether connector logs get delivered to Amazon Kinesis Data Firehose.

s3 -> (structure)

Details about delivering logs to Amazon S3.

bucket -> (string)

The name of the S3 bucket that is the destination for log delivery.

enabled -> (boolean)

Specifies whether connector logs get sent to the specified Amazon S3 destination.

prefix -> (string)

The S3 prefix that is the destination for log delivery.

plugins -> (list)

Specifies which plugins were used for this connector.

(structure)

The description of the plugin.

customPlugin -> (structure)

Details about a custom plugin.

customPluginArn -> (string)

The Amazon Resource Name (ARN) of the custom plugin.

revision -> (long)

The revision of the custom plugin.

serviceExecutionRoleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role used by the connector to access Amazon Web Services resources.

workerConfiguration -> (structure)

The worker configurations that are in use with the connector.

revision -> (long)

The revision of the worker configuration.

workerConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the worker configuration.

nextToken -> (string)

If the response of a ListConnectors operation is truncated, it will include a NextToken. Send this NextToken in a subsequent request to continue listing from where it left off.