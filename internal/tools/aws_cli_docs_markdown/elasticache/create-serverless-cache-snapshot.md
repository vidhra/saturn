# create-serverless-cache-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-serverless-cache-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/create-serverless-cache-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticache](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticache/index.html#cli-aws-elasticache) ]

# create-serverless-cache-snapshot

## Description

This API creates a copy of an entire ServerlessCache at a specific moment in time. Available for Valkey, Redis OSS and Serverless Memcached only.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticache-2015-02-02/CreateServerlessCacheSnapshot)

## Synopsis

```
create-serverless-cache-snapshot
--serverless-cache-snapshot-name <value>
--serverless-cache-name <value>
[--kms-key-id <value>]
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

`--serverless-cache-snapshot-name` (string)

The name for the snapshot being created. Must be unique for the customer account. Available for Valkey, Redis OSS and Serverless Memcached only. Must be between 1 and 255 characters.

`--serverless-cache-name` (string)

The name of an existing serverless cache. The snapshot is created from this cache. Available for Valkey, Redis OSS and Serverless Memcached only.

`--kms-key-id` (string)

The ID of the KMS key used to encrypt the snapshot. Available for Valkey, Redis OSS and Serverless Memcached only. Default: NULL

`--tags` (list)

A list of tags to be added to the snapshot resource. A tag is a key-value pair. Available for Valkey, Redis OSS and Serverless Memcached only.

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

## Output

ServerlessCacheSnapshot -> (structure)

The state of a serverless cache snapshot at a specific point in time, to the millisecond. Available for Valkey, Redis OSS and Serverless Memcached only.

ServerlessCacheSnapshotName -> (string)

The identifier of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.

ARN -> (string)

The Amazon Resource Name (ARN) of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.

KmsKeyId -> (string)

The ID of the Amazon Web Services Key Management Service (KMS) key of a serverless cache snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.

SnapshotType -> (string)

The type of snapshot of serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.

Status -> (string)

The current status of the serverless cache. Available for Valkey, Redis OSS and Serverless Memcached only.

CreateTime -> (timestamp)

The date and time that the source serverless cacheâs metadata and cache data set was obtained for the snapshot. Available for Valkey, Redis OSS and Serverless Memcached only.

ExpiryTime -> (timestamp)

The time that the serverless cache snapshot will expire. Available for Valkey, Redis OSS and Serverless Memcached only.

BytesUsedForCache -> (string)

The total size of a serverless cache snapshot, in bytes. Available for Valkey, Redis OSS and Serverless Memcached only.

ServerlessCacheConfiguration -> (structure)

The configuration of the serverless cache, at the time the snapshot was taken. Available for Valkey, Redis OSS and Serverless Memcached only.

ServerlessCacheName -> (string)

The identifier of a serverless cache.

Engine -> (string)

The engine that the serverless cache is configured with.

MajorEngineVersion -> (string)

The engine version number that the serverless cache is configured with.