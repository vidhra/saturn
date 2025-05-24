# purchase-reserved-cache-nodes-offeringÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/purchase-reserved-cache-nodes-offering.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/purchase-reserved-cache-nodes-offering.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/index.html#cli-aws-elasticache) ]

# purchase-reserved-cache-nodes-offering

## Description

Allows you to purchase a reserved cache node offering. Reserved nodes are not eligible for cancellation and are non-refundable. For more information, see [Managing Costs with Reserved Nodes](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/reserved-nodes.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/PurchaseReservedCacheNodesOffering)

## Synopsis

```
purchase-reserved-cache-nodes-offering
--reserved-cache-nodes-offering-id <value>
[--reserved-cache-node-id <value>]
[--cache-node-count <value>]
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

`--reserved-cache-nodes-offering-id` (string)

The ID of the reserved cache node offering to purchase.

Example: `438012d3-4052-4cc7-b2e3-8d3372e0e706`

`--reserved-cache-node-id` (string)

A customer-specified identifier to track this reservation.

### Note

The Reserved Cache Node ID is an unique customer-specified identifier to track this reservation. If this parameter is not specified, ElastiCache automatically generates an identifier for the reservation.

Example: myreservationID

`--cache-node-count` (integer)

The number of cache node instances to reserve.

Default: `1`

`--tags` (list)

A list of tags to be added to this resource. A tag is a key-value pair. A tag key must be accompanied by a tag value, although null is accepted.

(structure)

A tag that can be added to an ElastiCache cluster or replication group. Tags are composed of a Key/Value pair. You can use tags to categorize and track all your ElastiCache resources, with the exception of global replication group. When you add or remove tags on replication groups, those actions will be replicated to all nodes in the replication group. A tag with a null Value is permitted.

Key -> (string)

The key for the tag. May not be null.

Value -> (string)

The tagâs value. May be null.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

**To purchase a reserved-cache-node-offering**

The following `purchase-reserved-cache-nodes-offering` example allows you to purchase a reserved cache node offering.

```
aws elasticache purchase-reserved-cache-nodes-offering \
    --reserved-cache-nodes-offering-id xxxxxxx-4da5-4b90-b92d-929fbd7abed2
```

Output

```
{
    "ReservedCacheNode": {
        "ReservedCacheNodeId": "ri-2020-06-30-17-59-40-474",
        "ReservedCacheNodesOfferingId": "xxxxxxx-4da5-4b90-b92d-929fbd7abed2",
        "CacheNodeType": "cache.m3.2xlarge",
        "StartTime": "2020-06-30T17:59:40.474000+00:00",
        "Duration": 31536000,
        "FixedPrice": 1772.0,
        "UsagePrice": 0.0,
        "CacheNodeCount": 1,
        "ProductDescription": "redis",
        "OfferingType": "Heavy Utilization",
        "State": "payment-pending",
        "RecurringCharges": [
            {
                "RecurringChargeAmount": 0.25,
                "RecurringChargeFrequency": "Hourly"
            }
        ]
    }
}
```

For more information, see [Getting Info About Reserved Node Offerings](https://docs.aws.amazon.com/AmazonElastiCache/latest/red-ug/reserved-nodes-offerings.html) in the *Elasticache Redis User Guide* or [Getting Info About Reserved Node Offerings](https://docs.aws.amazon.com/AmazonElastiCache/latest/mem-ug/reserved-nodes-offerings.html) in the *Elasticache Memcached User Guide*.

## Output

ReservedCacheNode -> (structure)

Represents the output of a `PurchaseReservedCacheNodesOffering` operation.

ReservedCacheNodeId -> (string)

The unique identifier for the reservation.

ReservedCacheNodesOfferingId -> (string)

The offering identifier.

CacheNodeType -> (string)

The cache node type for the reserved cache nodes.

The following node types are supported by ElastiCache. Generally speaking, the current generation types provide more memory and computational power at lower cost when compared to their equivalent previous generation counterparts.

- General purpose:

- Current generation:   **M7g node types** : `cache.m7g.large` , `cache.m7g.xlarge` , `cache.m7g.2xlarge` , `cache.m7g.4xlarge` , `cache.m7g.8xlarge` , `cache.m7g.12xlarge` , `cache.m7g.16xlarge`

### Note

For region availability, see [Supported Node Types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)

**M6g node types** (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): `cache.m6g.large` , `cache.m6g.xlarge` , `cache.m6g.2xlarge` , `cache.m6g.4xlarge` , `cache.m6g.8xlarge` , `cache.m6g.12xlarge` , `cache.m6g.16xlarge` **M5 node types:** `cache.m5.large` , `cache.m5.xlarge` , `cache.m5.2xlarge` , `cache.m5.4xlarge` , `cache.m5.12xlarge` , `cache.m5.24xlarge` **M4 node types:** `cache.m4.large` , `cache.m4.xlarge` , `cache.m4.2xlarge` , `cache.m4.4xlarge` , `cache.m4.10xlarge` **T4g node types** (available only for Redis OSS engine version 5.0.6 onward and Memcached engine version 1.5.16 onward): `cache.t4g.micro` , `cache.t4g.small` , `cache.t4g.medium` **T3 node types:** `cache.t3.micro` , `cache.t3.small` , `cache.t3.medium` **T2 node types:** `cache.t2.micro` , `cache.t2.small` , `cache.t2.medium`

- Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)  **T1 node types:** `cache.t1.micro` **M1 node types:** `cache.m1.small` , `cache.m1.medium` , `cache.m1.large` , `cache.m1.xlarge` **M3 node types:** `cache.m3.medium` , `cache.m3.large` , `cache.m3.xlarge` , `cache.m3.2xlarge`
- Compute optimized:

- Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)  **C1 node types:** `cache.c1.xlarge`
- Memory optimized:

- Current generation:   **R7g node types** : `cache.r7g.large` , `cache.r7g.xlarge` , `cache.r7g.2xlarge` , `cache.r7g.4xlarge` , `cache.r7g.8xlarge` , `cache.r7g.12xlarge` , `cache.r7g.16xlarge`

### Note

For region availability, see [Supported Node Types](https://docs.aws.amazon.com/AmazonElastiCache/latest/dg/CacheNodes.SupportedTypes.html#CacheNodes.SupportedTypesByRegion)

**R6g node types** (available only for Redis OSS engine version 5.0.6 onward and for Memcached engine version 1.5.16 onward): `cache.r6g.large` , `cache.r6g.xlarge` , `cache.r6g.2xlarge` , `cache.r6g.4xlarge` , `cache.r6g.8xlarge` , `cache.r6g.12xlarge` , `cache.r6g.16xlarge` **R5 node types:** `cache.r5.large` , `cache.r5.xlarge` , `cache.r5.2xlarge` , `cache.r5.4xlarge` , `cache.r5.12xlarge` , `cache.r5.24xlarge` **R4 node types:** `cache.r4.large` , `cache.r4.xlarge` , `cache.r4.2xlarge` , `cache.r4.4xlarge` , `cache.r4.8xlarge` , `cache.r4.16xlarge`

- Previous generation: (not recommended. Existing clusters are still supported but creation of new clusters is not supported for these types.)  **M2 node types:** `cache.m2.xlarge` , `cache.m2.2xlarge` , `cache.m2.4xlarge` **R3 node types:** `cache.r3.large` , `cache.r3.xlarge` , `cache.r3.2xlarge` , `cache.r3.4xlarge` , `cache.r3.8xlarge`

**Additional node type info**

- All current generation instance types are created in Amazon VPC by default.
- Valkey or Redis OSS append-only files (AOF) are not supported for T1 or T2 instances.
- Valkey or Redis OSS Multi-AZ with automatic failover is not supported on T1 instances.
- The configuration variables `appendonly` and `appendfsync` are not supported on Valkey, or on Redis OSS version 2.8.22 and later.

StartTime -> (timestamp)

The time the reservation started.

Duration -> (integer)

The duration of the reservation in seconds.

FixedPrice -> (double)

The fixed price charged for this reserved cache node.

UsagePrice -> (double)

The hourly price charged for this reserved cache node.

CacheNodeCount -> (integer)

The number of cache nodes that have been reserved.

ProductDescription -> (string)

The description of the reserved cache node.

OfferingType -> (string)

The offering type of this reserved cache node.

State -> (string)

The state of the reserved cache node.

RecurringCharges -> (list)

The recurring price charged to run this reserved cache node.

(structure)

Contains the specific price and frequency of a recurring charges for a reserved cache node, or for a reserved cache node offering.

RecurringChargeAmount -> (double)

The monetary amount of the recurring charge.

RecurringChargeFrequency -> (string)

The frequency of the recurring charge.

ReservationARN -> (string)

The Amazon Resource Name (ARN) of the reserved cache node.

Example: `arn:aws:elasticache:us-east-1:123456789012:reserved-instance:ri-2017-03-27-08-33-25-582`