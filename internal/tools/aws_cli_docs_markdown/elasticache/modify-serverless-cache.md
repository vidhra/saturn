# modify-serverless-cacheÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-serverless-cache.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/modify-serverless-cache.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/index.html#cli-aws-elasticache) ]

# modify-serverless-cache

## Description

This API modifies the attributes of a serverless cache.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/ModifyServerlessCache)

## Synopsis

```
modify-serverless-cache
--serverless-cache-name <value>
[--description <value>]
[--cache-usage-limits <value>]
[--remove-user-group | --no-remove-user-group]
[--user-group-id <value>]
[--security-group-ids <value>]
[--snapshot-retention-limit <value>]
[--daily-snapshot-time <value>]
[--engine <value>]
[--major-engine-version <value>]
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

User-provided identifier for the serverless cache to be modified.

`--description` (string)

User provided description for the serverless cache. Default = NULL, i.e. the existing description is not removed/modified. The description has a maximum length of 255 characters.

`--cache-usage-limits` (structure)

Modify the cache usage limit for the serverless cache.

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

`--remove-user-group` | `--no-remove-user-group` (boolean)

The identifier of the UserGroup to be removed from association with the Valkey and Redis OSS serverless cache. Available for Valkey and Redis OSS only. Default is NULL.

`--user-group-id` (string)

The identifier of the UserGroup to be associated with the serverless cache. Available for Valkey and Redis OSS only. Default is NULL - the existing UserGroup is not removed.

`--security-group-ids` (list)

The new list of VPC security groups to be associated with the serverless cache. Populating this list means the current VPC security groups will be removed. This security group is used to authorize traffic access for the VPC end-point (private-link). Default = NULL - the existing list of VPC security groups is not removed.

(string)

Syntax:

```
"string" "string" ...
```

`--snapshot-retention-limit` (integer)

The number of days for which Elasticache retains automatic snapshots before deleting them. Available for Valkey, Redis OSS and Serverless Memcached only. Default = NULL, i.e. the existing snapshot-retention-limit will not be removed or modified. The maximum value allowed is 35 days.

`--daily-snapshot-time` (string)

The daily time during which Elasticache begins taking a daily snapshot of the serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only. The default is NULL, i.e. the existing snapshot time configured for the cluster is not removed.

`--engine` (string)

Modifies the engine listed in a serverless cache request. The options are redis, memcached or valkey.

`--major-engine-version` (string)

Modifies the engine vesion listed in a serverless cache request.

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

The response for the attempt to modify the serverless cache.

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