# create-serverless-cacheÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-serverless-cache.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-serverless-cache.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/index.html#cli-aws-elasticache) ]

# create-serverless-cache

## Description

Creates a serverless cache.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateServerlessCache)

## Synopsis

```
create-serverless-cache
--serverless-cache-name <value>
[--description <value>]
--engine <value>
[--major-engine-version <value>]
[--cache-usage-limits <value>]
[--kms-key-id <value>]
[--security-group-ids <value>]
[--snapshot-arns-to-restore <value>]
[--tags <value>]
[--user-group-id <value>]
[--subnet-ids <value>]
[--snapshot-retention-limit <value>]
[--daily-snapshot-time <value>]
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

`--serverless-cache-name` (string)

User-provided identifier for the serverless cache. This parameter is stored as a lowercase string.

`--description` (string)

User-provided description for the serverless cache. The default is NULL, i.e. if no description is provided then an empty string will be returned. The maximum length is 255 characters.

`--engine` (string)

The name of the cache engine to be used for creating the serverless cache.

`--major-engine-version` (string)

The version of the cache engine that will be used to create the serverless cache.

`--cache-usage-limits` (structure)

Sets the cache usage limits for storage and ElastiCache Processing Units for the cache.

DataStorage -> (structure)

The maximum data storage limit in the cache, expressed in Gigabytes.

Maximum -> (integer)

The upper limit for data storage the cache is set to use.

Minimum -> (integer)

The lower limit for data storage the cache is set to use.

Unit -> (string)

The unit that the storage is measured in, in GB.

ECPUPerSecond -> (structure)

The configuration for the number of ElastiCache Processing Units (ECPU) the cache can consume per second.

Maximum -> (integer)

The configuration for the maximum number of ECPUs the cache can consume per second.

Minimum -> (integer)

The configuration for the minimum number of ECPUs the cache should be able consume per second.

Shorthand Syntax:

```
DataStorage={Maximum=integer,Minimum=integer,Unit=string},ECPUPerSecond={Maximum=integer,Minimum=integer}
```

JSON Syntax:

```
{
  "DataStorage": {
    "Maximum": integer,
    "Minimum": integer,
    "Unit": "GB"
  },
  "ECPUPerSecond": {
    "Maximum": integer,
    "Minimum": integer
  }
}
```

`--kms-key-id` (string)

ARN of the customer managed key for encrypting the data at rest. If no KMS key is provided, a default service key is used.

`--security-group-ids` (list)

A list of the one or more VPC security groups to be associated with the serverless cache. The security group will authorize traffic access for the VPC end-point (private-link). If no other information is given this will be the VPCâs Default Security Group that is associated with the cluster VPC end-point.

(string)

Syntax:

```
"string" "string" ...
```

`--snapshot-arns-to-restore` (list)

The ARN(s) of the snapshot that the new serverless cache will be created from. Available for Valkey, Redis OSS and Serverless Memcached only.

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

The list of tags (key, value) pairs to be added to the serverless cache resource. Default is NULL.

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

`--user-group-id` (string)

The identifier of the UserGroup to be associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL.

`--subnet-ids` (list)

A list of the identifiers of the subnets where the VPC endpoint for the serverless cache will be deployed. All the subnetIds must belong to the same VPC.

(string)

Syntax:

```
"string" "string" ...
```

`--snapshot-retention-limit` (integer)

The number of snapshots that will be retained for the serverless cache that is being created. As new snapshots beyond this limit are added, the oldest snapshots will be deleted on a rolling basis. Available for Valkey, Redis OSS and Serverless Memcached only.

`--daily-snapshot-time` (string)

The daily time that snapshots will be created from the new serverless cache. By default this number is populated with 0, i.e. no snapshots will be created on an automatic daily basis. Available for Valkey, Redis OSS and Serverless Memcached only.

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

ServerlessCache -> (structure)

The response for the attempt to create the serverless cache.

ServerlessCacheName -> (string)

The unique identifier of the serverless cache.

Description -> (string)

A description of the serverless cache.

CreateTime -> (timestamp)

When the serverless cache was created.

Status -> (string)

The current status of the serverless cache. The allowed values are CREATING, AVAILABLE, DELETING, CREATE-FAILED and MODIFYING.

Engine -> (string)

The engine the serverless cache is compatible with.

MajorEngineVersion -> (string)

The version number of the engine the serverless cache is compatible with.

FullEngineVersion -> (string)

The name and version number of the engine the serverless cache is compatible with.

CacheUsageLimits -> (structure)

The cache usage limit for the serverless cache.

DataStorage -> (structure)

The maximum data storage limit in the cache, expressed in Gigabytes.

Maximum -> (integer)

The upper limit for data storage the cache is set to use.

Minimum -> (integer)

The lower limit for data storage the cache is set to use.

Unit -> (string)

The unit that the storage is measured in, in GB.

ECPUPerSecond -> (structure)

The configuration for the number of ElastiCache Processing Units (ECPU) the cache can consume per second.

Maximum -> (integer)

The configuration for the maximum number of ECPUs the cache can consume per second.

Minimum -> (integer)

The configuration for the minimum number of ECPUs the cache should be able consume per second.

KmsKeyId -> (string)

The ID of the Amazon Web Services Key Management Service (KMS) key that is used to encrypt data at rest in the serverless cache.

SecurityGroupIds -> (list)

The IDs of the EC2 security groups associated with the serverless cache.

(string)

Endpoint -> (structure)

Represents the information required for client programs to connect to a cache node. This value is read-only.

Address -> (string)

The DNS hostname of the cache node.

Port -> (integer)

The port number that the cache engine is listening on.

ReaderEndpoint -> (structure)

Represents the information required for client programs to connect to a cache node. This value is read-only.

Address -> (string)

The DNS hostname of the cache node.

Port -> (integer)

The port number that the cache engine is listening on.

ARN -> (string)

The Amazon Resource Name (ARN) of the serverless cache.

UserGroupId -> (string)

The identifier of the user group associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL.

SubnetIds -> (list)

If no subnet IDs are given and your VPC is in us-west-1, then ElastiCache will select 2 default subnets across AZs in your VPC. For all other Regions, if no subnet IDs are given then ElastiCache will select 3 default subnets across AZs in your default VPC.

(string)

SnapshotRetentionLimit -> (integer)

The current setting for the number of serverless cache snapshots the system will retain. Available for Valkey, Redis OSS and Serverless Memcached only.

DailySnapshotTime -> (string)

The daily time that a cache snapshot will be created. Default is NULL, i.e. snapshots will not be created at a specific time on a daily basis. Available for Valkey, Redis OSS and Serverless Memcached only.