# describe-domain-healthÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/describe-domain-health.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/describe-domain-health.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opensearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html#cli-aws-opensearch) ]

# describe-domain-health

## Description

Returns information about domain and node health, the standby Availability Zone, number of nodes per Availability Zone, and shard count per node.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opensearch-2021-01-01/DescribeDomainHealth)

## Synopsis

```
describe-domain-health
--domain-name <value>
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

The name of the domain.

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

DomainState -> (string)

The current state of the domain.

- `Processing` - The domain has updates in progress.
- `Active` - Requested changes have been processed and deployed to the domain.

AvailabilityZoneCount -> (string)

The number of Availability Zones configured for the domain. If the service is unable to fetch this information, it will return `NotAvailable` .

ActiveAvailabilityZoneCount -> (string)

The number of active Availability Zones configured for the domain. If the service is unable to fetch this information, it will return `NotAvailable` .

StandByAvailabilityZoneCount -> (string)

The number of standby Availability Zones configured for the domain. If the service is unable to fetch this information, it will return `NotAvailable` .

DataNodeCount -> (string)

The number of data nodes configured for the domain. If the service is unable to fetch this information, it will return `NotAvailable` .

DedicatedMaster -> (boolean)

A boolean that indicates if dedicated master nodes are activated for the domain.

MasterEligibleNodeCount -> (string)

The number of nodes that can be elected as a master node. If dedicated master nodes is turned on, this value is the number of dedicated master nodes configured for the domain. If the service is unable to fetch this information, it will return `NotAvailable` .

WarmNodeCount -> (string)

The number of warm nodes configured for the domain.

MasterNode -> (string)

Indicates whether the domain has an elected master node.

- **Available** - The domain has an elected master node.
- **UnAvailable** - The master node hasnât yet been elected, and a quorum to elect a new master node hasnât been reached.

ClusterHealth -> (string)

The current health status of your cluster.

- `Red` - At least one primary shard is not allocated to any node.
- `Yellow` - All primary shards are allocated to nodes, but some replicas arenât.
- `Green` - All primary shards and their replicas are allocated to nodes.
- `NotAvailable` - Unable to retrieve cluster health.

TotalShards -> (string)

The total number of primary and replica shards for the domain.

TotalUnAssignedShards -> (string)

The total number of primary and replica shards not allocated to any of the nodes for the cluster.

EnvironmentInformation -> (list)

A list of `EnvironmentInfo` for the domain.

(structure)

Information about the active domain environment.

AvailabilityZoneInformation -> (list)

A list of `AvailabilityZoneInfo` for the domain.

(structure)

Information about an Availability Zone on a domain.

AvailabilityZoneName -> (string)

The name of the Availability Zone.

ZoneStatus -> (string)

The current state of the Availability Zone. Current options are `Active` and `StandBy` .

- `Active` - Data nodes in the Availability Zone are in use.
- `StandBy` - Data nodes in the Availability Zone are in a standby state.
- `NotAvailable` - Unable to retrieve information.

ConfiguredDataNodeCount -> (string)

The total number of data nodes configured in the Availability Zone.

AvailableDataNodeCount -> (string)

The number of data nodes active in the Availability Zone.

TotalShards -> (string)

The total number of primary and replica shards in the Availability Zone.

TotalUnAssignedShards -> (string)

The total number of primary and replica shards that arenât allocated to any of the nodes in the Availability Zone.