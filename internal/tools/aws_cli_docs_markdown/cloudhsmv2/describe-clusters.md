# describe-clustersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/describe-clusters.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/describe-clusters.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudhsmv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudhsmv2/index.html#cli-aws-cloudhsmv2) ]

# describe-clusters

## Description

Gets information about CloudHSM clusters.

This is a paginated operation, which means that each response might contain only a subset of all the clusters. When the response contains only a subset of clusters, it includes a `NextToken` value. Use this value in a subsequent `DescribeClusters` request to get more clusters. When you receive a response with no `NextToken` (or an empty or null value), that means there are no more clusters to get.

**Cross-account use:** No. You cannot perform this operation on CloudHSM clusters in a different Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudhsmv2-2017-04-28/DescribeClusters)

`describe-clusters` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Clusters`

## Synopsis

```
describe-clusters
[--filters <value>]
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

`--filters` (map)

One or more filters to limit the items returned in the response.

Use the `clusterIds` filter to return only the specified clusters. Specify clusters by their cluster identifier (ID).

Use the `vpcIds` filter to return only the clusters in the specified virtual private clouds (VPCs). Specify VPCs by their VPC identifier (ID).

Use the `states` filter to return only clusters that match the specified state.

key -> (string)

value -> (list)

(string)

Shorthand Syntax:

```
KeyName1=string,string,KeyName2=string,string
```

JSON Syntax:

```
{"string": ["string", ...]
  ...}
```

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

Clusters -> (list)

A list of clusters.

(structure)

Contains information about an CloudHSM cluster.

BackupPolicy -> (string)

The clusterâs backup policy.

BackupRetentionPolicy -> (structure)

A policy that defines how the service retains backups.

Type -> (string)

The type of backup retention policy. For the `DAYS` type, the value is the number of days to retain backups.

Value -> (string)

Use a value between 7 - 379.

ClusterId -> (string)

The clusterâs identifier (ID).

CreateTimestamp -> (timestamp)

The date and time when the cluster was created.

Hsms -> (list)

Contains information about the HSMs in the cluster.

(structure)

Contains information about a hardware security module (HSM) in an CloudHSM cluster.

AvailabilityZone -> (string)

The Availability Zone that contains the HSM.

ClusterId -> (string)

The identifier (ID) of the cluster that contains the HSM.

SubnetId -> (string)

The subnet that contains the HSMâs elastic network interface (ENI).

EniId -> (string)

The identifier (ID) of the HSMâs elastic network interface (ENI).

EniIp -> (string)

The IP address of the HSMâs elastic network interface (ENI).

EniIpV6 -> (string)

The IPv6 address (if any) of the HSMâs elastic network interface (ENI).

HsmId -> (string)

The HSMâs identifier (ID).

HsmType -> (string)

The type of HSM.

State -> (string)

The HSMâs state.

StateMessage -> (string)

A description of the HSMâs state.

HsmType -> (string)

The type of HSM that the cluster contains.

HsmTypeRollbackExpiration -> (timestamp)

The timestamp until when the cluster can be rolled back to its original HSM type.

PreCoPassword -> (string)

The default password for the clusterâs Pre-Crypto Officer (PRECO) user.

SecurityGroup -> (string)

The identifier (ID) of the clusterâs security group.

SourceBackupId -> (string)

The identifier (ID) of the backup used to create the cluster. This value exists only when the cluster was created from a backup.

State -> (string)

The clusterâs state.

StateMessage -> (string)

A description of the clusterâs state.

SubnetMapping -> (map)

A map from availability zone to the clusterâs subnet in that availability zone.

key -> (string)

value -> (string)

VpcId -> (string)

The identifier (ID) of the virtual private cloud (VPC) that contains the cluster.

NetworkType -> (string)

The clusterâs NetworkType can be IPv4 (the default) or DUALSTACK. The IPv4 NetworkType restricts communication between your application and the hardware security modules (HSMs) to the IPv4 protocol only. The DUALSTACK NetworkType enables communication over both IPv4 and IPv6 protocols. To use DUALSTACK, configure your virtual private cloud (VPC) and subnets to support both IPv4 and IPv6. This configuration involves adding IPv6 Classless Inter-Domain Routing (CIDR) blocks to the existing IPv4 CIDR blocks in your subnets. The NetworkType you choose affects the network addressing options for your cluster. DUALSTACK provides more flexibility by supporting both IPv4 and IPv6 communication.

Certificates -> (structure)

Contains one or more certificates or a certificate signing request (CSR).

ClusterCsr -> (string)

The clusterâs certificate signing request (CSR). The CSR exists only when the clusterâs state is `UNINITIALIZED` .

HsmCertificate -> (string)

The HSM certificate issued (signed) by the HSM hardware.

AwsHardwareCertificate -> (string)

The HSM hardware certificate issued (signed) by CloudHSM.

ManufacturerHardwareCertificate -> (string)

The HSM hardware certificate issued (signed) by the hardware manufacturer.

ClusterCertificate -> (string)

The cluster certificate issued (signed) by the issuing certificate authority (CA) of the clusterâs owner.

TagList -> (list)

The list of tags for the cluster.

(structure)

Contains a tag. A tag is a key-value pair.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

Mode -> (string)

The mode of the cluster.

NextToken -> (string)

An opaque string that indicates that the response contains only a subset of clusters. Use this value in a subsequent `DescribeClusters` request to get more clusters.