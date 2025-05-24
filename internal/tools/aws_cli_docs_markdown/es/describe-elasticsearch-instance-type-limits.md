# describe-elasticsearch-instance-type-limitsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-instance-type-limits.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/describe-elasticsearch-instance-type-limits.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [es](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/es/index.html#cli-aws-es) ]

# describe-elasticsearch-instance-type-limits

## Description

Describe Elasticsearch Limits for a given InstanceType and ElasticsearchVersion. When modifying existing Domain, specify the ``  DomainName `` to know what Limits are supported for modifying.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/es-2015-01-01/DescribeElasticsearchInstanceTypeLimits)

## Synopsis

```
describe-elasticsearch-instance-type-limits
[--domain-name <value>]
--instance-type <value>
--elasticsearch-version <value>
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

`--domain-name` (string)

DomainName represents the name of the Domain that we are trying to modify. This should be present only if we are querying for Elasticsearch ``  Limits `` for existing domain.

`--instance-type` (string)

The instance type for an Elasticsearch cluster for which Elasticsearch ``  Limits `` are needed.

Possible values:

- `m3.medium.elasticsearch`
- `m3.large.elasticsearch`
- `m3.xlarge.elasticsearch`
- `m3.2xlarge.elasticsearch`
- `m4.large.elasticsearch`
- `m4.xlarge.elasticsearch`
- `m4.2xlarge.elasticsearch`
- `m4.4xlarge.elasticsearch`
- `m4.10xlarge.elasticsearch`
- `m5.large.elasticsearch`
- `m5.xlarge.elasticsearch`
- `m5.2xlarge.elasticsearch`
- `m5.4xlarge.elasticsearch`
- `m5.12xlarge.elasticsearch`
- `r5.large.elasticsearch`
- `r5.xlarge.elasticsearch`
- `r5.2xlarge.elasticsearch`
- `r5.4xlarge.elasticsearch`
- `r5.12xlarge.elasticsearch`
- `c5.large.elasticsearch`
- `c5.xlarge.elasticsearch`
- `c5.2xlarge.elasticsearch`
- `c5.4xlarge.elasticsearch`
- `c5.9xlarge.elasticsearch`
- `c5.18xlarge.elasticsearch`
- `ultrawarm1.medium.elasticsearch`
- `ultrawarm1.large.elasticsearch`
- `t2.micro.elasticsearch`
- `t2.small.elasticsearch`
- `t2.medium.elasticsearch`
- `r3.large.elasticsearch`
- `r3.xlarge.elasticsearch`
- `r3.2xlarge.elasticsearch`
- `r3.4xlarge.elasticsearch`
- `r3.8xlarge.elasticsearch`
- `i2.xlarge.elasticsearch`
- `i2.2xlarge.elasticsearch`
- `d2.xlarge.elasticsearch`
- `d2.2xlarge.elasticsearch`
- `d2.4xlarge.elasticsearch`
- `d2.8xlarge.elasticsearch`
- `c4.large.elasticsearch`
- `c4.xlarge.elasticsearch`
- `c4.2xlarge.elasticsearch`
- `c4.4xlarge.elasticsearch`
- `c4.8xlarge.elasticsearch`
- `r4.large.elasticsearch`
- `r4.xlarge.elasticsearch`
- `r4.2xlarge.elasticsearch`
- `r4.4xlarge.elasticsearch`
- `r4.8xlarge.elasticsearch`
- `r4.16xlarge.elasticsearch`
- `i3.large.elasticsearch`
- `i3.xlarge.elasticsearch`
- `i3.2xlarge.elasticsearch`
- `i3.4xlarge.elasticsearch`
- `i3.8xlarge.elasticsearch`
- `i3.16xlarge.elasticsearch`

`--elasticsearch-version` (string)

Version of Elasticsearch for which ``  Limits `` are needed.

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

LimitsByRole -> (map)

Map of Role of the Instance and Limits that are applicable. Role performed by given Instance in Elasticsearch can be one of the following:

- data: If the given InstanceType is used as data node
- master: If the given InstanceType is used as master node
- ultra_warm: If the given InstanceType is used as warm node

key -> (string)

value -> (structure)

Limits for given InstanceType and for each of itâs role. Limits contains following ``  StorageTypes, ``  ``  InstanceLimits `` and ``  AdditionalLimits ``

StorageTypes -> (list)

StorageType represents the list of storage related types and attributes that are available for given InstanceType.

(structure)

StorageTypes represents the list of storage related types and their attributes that are available for given InstanceType.

StorageTypeName -> (string)

Type of the storage. List of available storage options:

- instance

Inbuilt storage available for the given Instance
* ebs
Elastic block storage that would be attached to the given Instance

StorageSubTypeName -> (string)

SubType of the given storage type. List of available sub-storage options: For âinstanceâ storageType we wont have any storageSubType, in case of âebsâ storageType we will have following valid storageSubTypes

- standard
- gp2
- gp3
- io1

Refer `` VolumeType`` for more information regarding above EBS storage options.

StorageTypeLimits -> (list)

List of limits that are applicable for given storage type.

(structure)

Limits that are applicable for given storage type.

LimitName -> (string)

Name of storage limits that are applicable for given storage type. If ``  StorageType `` is ebs, following storage options are applicable

- MinimumVolumeSize

Minimum amount of volume size that is applicable for given storage type.It can be empty if it is not applicable.
* MaximumVolumeSize
Maximum amount of volume size that is applicable for given storage type.It can be empty if it is not applicable.
* MaximumIops
Maximum amount of Iops that is applicable for given storage type.It can be empty if it is not applicable.
* MinimumIops
Minimum amount of Iops that is applicable for given storage type.It can be empty if it is not applicable.
* MaximumThroughput
Maximum amount of Throughput that is applicable for given storage type.It can be empty if it is not applicable.
* MinimumThroughput
Minimum amount of Throughput that is applicable for given storage type.It can be empty if it is not applicable.

LimitValues -> (list)

Values for the ``  StorageTypeLimit$LimitName `` .

(string)

InstanceLimits -> (structure)

InstanceLimits represents the list of instance related attributes that are available for given InstanceType.

InstanceCountLimits -> (structure)

InstanceCountLimits represents the limits on number of instances that be created in Amazon Elasticsearch for given InstanceType.

MinimumInstanceCount -> (integer)

Minimum number of Instances that can be instantiated for given InstanceType.

MaximumInstanceCount -> (integer)

Maximum number of Instances that can be instantiated for given InstanceType.

AdditionalLimits -> (list)

List of additional limits that are specific to a given InstanceType and for each of itâs ``  InstanceRole `` .

(structure)

List of limits that are specific to a given InstanceType and for each of itâs ``  InstanceRole `` .

LimitName -> (string)

Name of Additional Limit is specific to a given InstanceType and for each of itâs ``  InstanceRole `` etc. Attributes and their details:

- MaximumNumberOfDataNodesSupported

This attribute will be present in Master node only to specify how much data nodes upto which given ``  ESPartitionInstanceType `` can support as master node.
* MaximumNumberOfDataNodesWithoutMasterNode
This attribute will be present in Data node only to specify how much data nodes of given ``  ESPartitionInstanceType `` upto which you donât need any master nodes to govern them.

LimitValues -> (list)

Value for given ``  AdditionalLimit$LimitName `` .

(string)