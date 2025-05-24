# update-api-cacheÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-api-cache.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/update-api-cache.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appsync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/index.html#cli-aws-appsync) ]

# update-api-cache

## Description

Updates the cache for the GraphQL API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/UpdateApiCache)

## Synopsis

```
update-api-cache
--api-id <value>
--ttl <value>
--api-caching-behavior <value>
--type <value>
[--health-metrics-config <value>]
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

`--api-id` (string)

The GraphQL API ID.

`--ttl` (long)

TTL in seconds for cache entries.

Valid values are 1â3,600 seconds.

`--api-caching-behavior` (string)

Caching behavior.

- **FULL_REQUEST_CACHING** : All requests from the same user are cached. Individual resolvers are automatically cached. All API calls will try to return responses from the cache.
- **PER_RESOLVER_CACHING** : Individual resolvers that you specify are cached.
- **OPERATION_LEVEL_CACHING** : Full requests are cached together and returned without executing resolvers.

Possible values:

- `FULL_REQUEST_CACHING`
- `PER_RESOLVER_CACHING`
- `OPERATION_LEVEL_CACHING`

`--type` (string)

The cache instance type. Valid values are

- `SMALL`
- `MEDIUM`
- `LARGE`
- `XLARGE`
- `LARGE_2X`
- `LARGE_4X`
- `LARGE_8X` (not available in all regions)
- `LARGE_12X`

Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.

The following legacy instance types are available, but their use is discouraged:

- **T2_SMALL** : A t2.small instance type.
- **T2_MEDIUM** : A t2.medium instance type.
- **R4_LARGE** : A r4.large instance type.
- **R4_XLARGE** : A r4.xlarge instance type.
- **R4_2XLARGE** : A r4.2xlarge instance type.
- **R4_4XLARGE** : A r4.4xlarge instance type.
- **R4_8XLARGE** : A r4.8xlarge instance type.

Possible values:

- `T2_SMALL`
- `T2_MEDIUM`
- `R4_LARGE`
- `R4_XLARGE`
- `R4_2XLARGE`
- `R4_4XLARGE`
- `R4_8XLARGE`
- `SMALL`
- `MEDIUM`
- `LARGE`
- `XLARGE`
- `LARGE_2X`
- `LARGE_4X`
- `LARGE_8X`
- `LARGE_12X`

`--health-metrics-config` (string)

Controls how cache health metrics will be emitted to CloudWatch. Cache health metrics include:

- NetworkBandwidthOutAllowanceExceeded: The network packets dropped because the throughput exceeded the aggregated bandwidth limit. This is useful for diagnosing bottlenecks in a cache configuration.
- EngineCPUUtilization: The CPU utilization (percentage) allocated to the Redis process. This is useful for diagnosing bottlenecks in a cache configuration.

Metrics will be recorded by API ID. You can set the value to `ENABLED` or `DISABLED` .

Possible values:

- `ENABLED`
- `DISABLED`

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

apiCache -> (structure)

The `ApiCache` object.

ttl -> (long)

TTL in seconds for cache entries.

Valid values are 1â3,600 seconds.

apiCachingBehavior -> (string)

Caching behavior.

- **FULL_REQUEST_CACHING** : All requests from the same user are cached. Individual resolvers are automatically cached. All API calls will try to return responses from the cache.
- **PER_RESOLVER_CACHING** : Individual resolvers that you specify are cached.
- **OPERATION_LEVEL_CACHING** : Full requests are cached together and returned without executing resolvers.

transitEncryptionEnabled -> (boolean)

Transit encryption flag when connecting to cache. You cannot update this setting after creation.

atRestEncryptionEnabled -> (boolean)

At-rest encryption flag for cache. You cannot update this setting after creation.

type -> (string)

The cache instance type. Valid values are

- `SMALL`
- `MEDIUM`
- `LARGE`
- `XLARGE`
- `LARGE_2X`
- `LARGE_4X`
- `LARGE_8X` (not available in all regions)
- `LARGE_12X`

Historically, instance types were identified by an EC2-style value. As of July 2020, this is deprecated, and the generic identifiers above should be used.

The following legacy instance types are available, but their use is discouraged:

- **T2_SMALL** : A t2.small instance type.
- **T2_MEDIUM** : A t2.medium instance type.
- **R4_LARGE** : A r4.large instance type.
- **R4_XLARGE** : A r4.xlarge instance type.
- **R4_2XLARGE** : A r4.2xlarge instance type.
- **R4_4XLARGE** : A r4.4xlarge instance type.
- **R4_8XLARGE** : A r4.8xlarge instance type.

status -> (string)

The cache instance status.

- **AVAILABLE** : The instance is available for use.
- **CREATING** : The instance is currently creating.
- **DELETING** : The instance is currently deleting.
- **MODIFYING** : The instance is currently modifying.
- **FAILED** : The instance has failed creation.

healthMetricsConfig -> (string)

Controls how cache health metrics will be emitted to CloudWatch. Cache health metrics include:

- NetworkBandwidthOutAllowanceExceeded: The network packets dropped because the throughput exceeded the aggregated bandwidth limit. This is useful for diagnosing bottlenecks in a cache configuration.
- EngineCPUUtilization: The CPU utilization (percentage) allocated to the Redis process. This is useful for diagnosing bottlenecks in a cache configuration.

Metrics will be recorded by API ID. You can set the value to `ENABLED` or `DISABLED` .