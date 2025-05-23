# describe-instance-type-limitsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/describe-instance-type-limits.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/describe-instance-type-limits.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opensearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html#cli-aws-opensearch) ]

# describe-instance-type-limits

## Description

Describes the instance count, storage, and master node limits for a given OpenSearch or Elasticsearch version and instance type.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opensearch-2021-01-01/DescribeInstanceTypeLimits)

## Synopsis

```
describe-instance-type-limits
[--domain-name <value>]
--instance-type <value>
--engine-version <value>
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

The name of the domain. Only specify if you need the limits for an existing domain.

`--instance-type` (string)

The OpenSearch Service instance type for which you need limit information.

Possible values:

- `m3.medium.search`
- `m3.large.search`
- `m3.xlarge.search`
- `m3.2xlarge.search`
- `m4.large.search`
- `m4.xlarge.search`
- `m4.2xlarge.search`
- `m4.4xlarge.search`
- `m4.10xlarge.search`
- `m5.large.search`
- `m5.xlarge.search`
- `m5.2xlarge.search`
- `m5.4xlarge.search`
- `m5.12xlarge.search`
- `m5.24xlarge.search`
- `r5.large.search`
- `r5.xlarge.search`
- `r5.2xlarge.search`
- `r5.4xlarge.search`
- `r5.12xlarge.search`
- `r5.24xlarge.search`
- `c5.large.search`
- `c5.xlarge.search`
- `c5.2xlarge.search`
- `c5.4xlarge.search`
- `c5.9xlarge.search`
- `c5.18xlarge.search`
- `t3.nano.search`
- `t3.micro.search`
- `t3.small.search`
- `t3.medium.search`
- `t3.large.search`
- `t3.xlarge.search`
- `t3.2xlarge.search`
- `or1.medium.search`
- `or1.large.search`
- `or1.xlarge.search`
- `or1.2xlarge.search`
- `or1.4xlarge.search`
- `or1.8xlarge.search`
- `or1.12xlarge.search`
- `or1.16xlarge.search`
- `ultrawarm1.medium.search`
- `ultrawarm1.large.search`
- `ultrawarm1.xlarge.search`
- `t2.micro.search`
- `t2.small.search`
- `t2.medium.search`
- `r3.large.search`
- `r3.xlarge.search`
- `r3.2xlarge.search`
- `r3.4xlarge.search`
- `r3.8xlarge.search`
- `i2.xlarge.search`
- `i2.2xlarge.search`
- `d2.xlarge.search`
- `d2.2xlarge.search`
- `d2.4xlarge.search`
- `d2.8xlarge.search`
- `c4.large.search`
- `c4.xlarge.search`
- `c4.2xlarge.search`
- `c4.4xlarge.search`
- `c4.8xlarge.search`
- `r4.large.search`
- `r4.xlarge.search`
- `r4.2xlarge.search`
- `r4.4xlarge.search`
- `r4.8xlarge.search`
- `r4.16xlarge.search`
- `i3.large.search`
- `i3.xlarge.search`
- `i3.2xlarge.search`
- `i3.4xlarge.search`
- `i3.8xlarge.search`
- `i3.16xlarge.search`
- `r6g.large.search`
- `r6g.xlarge.search`
- `r6g.2xlarge.search`
- `r6g.4xlarge.search`
- `r6g.8xlarge.search`
- `r6g.12xlarge.search`
- `m6g.large.search`
- `m6g.xlarge.search`
- `m6g.2xlarge.search`
- `m6g.4xlarge.search`
- `m6g.8xlarge.search`
- `m6g.12xlarge.search`
- `c6g.large.search`
- `c6g.xlarge.search`
- `c6g.2xlarge.search`
- `c6g.4xlarge.search`
- `c6g.8xlarge.search`
- `c6g.12xlarge.search`
- `r6gd.large.search`
- `r6gd.xlarge.search`
- `r6gd.2xlarge.search`
- `r6gd.4xlarge.search`
- `r6gd.8xlarge.search`
- `r6gd.12xlarge.search`
- `r6gd.16xlarge.search`
- `t4g.small.search`
- `t4g.medium.search`

`--engine-version` (string)

Version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.

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

Map that contains all applicable instance type limits.``data`` refers to data nodes.``master`` refers to dedicated master nodes.

key -> (string)

value -> (structure)

Limits for a given instance type and for each of its roles.

StorageTypes -> (list)

Storage-related attributes that are available for a given instance type.

(structure)

A list of storage types for an Amazon OpenSearch Service domain that are available for a given intance type.

StorageTypeName -> (string)

The name of the storage type.

StorageSubTypeName -> (string)

The storage sub-type, such as `gp3` or `io1` .

StorageTypeLimits -> (list)

Limits that are applicable for the given storage type.

(structure)

Limits that are applicable for the given Amazon OpenSearch Service storage type.

LimitName -> (string)

Name of storage limits that are applicable for the given storage type. If `StorageType` is `ebs` , the following options are available:

- **MinimumVolumeSize** - Minimum volume size that is available for the given storage type. Can be empty if not applicable.
- **MaximumVolumeSize** - Maximum volume size that is available for the given storage type. Can be empty if not applicable.
- **MaximumIops** - Maximum amount of IOPS that is available for the given the storage type. Can be empty if not applicable.
- **MinimumIops** - Minimum amount of IOPS that is available for the given the storage type. Can be empty if not applicable.
- **MaximumThroughput** - Maximum amount of throughput that is available for the given the storage type. Can be empty if not applicable.
- **MinimumThroughput** - Minimum amount of throughput that is available for the given the storage type. Can be empty if not applicable.

LimitValues -> (list)

The limit values.

(string)

InstanceLimits -> (structure)

The limits for a given instance type.

InstanceCountLimits -> (structure)

Limits on the number of instances that can be created for a given instance type.

MinimumInstanceCount -> (integer)

The maximum allowed number of instances.

MaximumInstanceCount -> (integer)

The minimum allowed number of instances.

AdditionalLimits -> (list)

List of additional limits that are specific to a given instance type for each of its instance roles.

(structure)

List of limits that are specific to a given instance type.

LimitName -> (string)

- `MaximumNumberOfDataNodesSupported` - This attribute only applies to master nodes and specifies the maximum number of data nodes of a given instance type a master node can support.
- `MaximumNumberOfDataNodesWithoutMasterNode` - This attribute only applies to data nodes and specifies the maximum number of data nodes of a given instance type can exist without a master node governing them.

LimitValues -> (list)

The values of the additional instance type limits.

(string)