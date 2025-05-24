# describe-file-cachesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-file-caches.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/describe-file-caches.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fsx](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/index.html#cli-aws-fsx) ]

# describe-file-caches

## Description

Returns the description of a specific Amazon File Cache resource, if a `FileCacheIds` value is provided for that cache. Otherwise, it returns descriptions of all caches owned by your Amazon Web Services account in the Amazon Web Services Region of the endpoint that youâre calling.

When retrieving all cache descriptions, you can optionally specify the `MaxResults` parameter to limit the number of descriptions in a response. If more cache descriptions remain, the operation returns a `NextToken` value in the response. In this case, send a later request with the `NextToken` request parameter set to the value of `NextToken` from the last response.

This operation is used in an iterative process to retrieve a list of your cache descriptions. `DescribeFileCaches` is called first without a `NextToken` value. Then the operation continues to be called with the `NextToken` parameter set to the value of the last `NextToken` value until a response has no `NextToken` .

When using this operation, keep the following in mind:

- The implementation might return fewer than `MaxResults` cache descriptions while still including a `NextToken` value.
- The order of caches returned in the response of one `DescribeFileCaches` call and the order of caches returned across the responses of a multicall iteration is unspecified.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/DescribeFileCaches)

## Synopsis

```
describe-file-caches
[--file-cache-ids <value>]
[--max-results <value>]
[--next-token <value>]
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

`--file-cache-ids` (list)

IDs of the caches whose descriptions you want to retrieve (String).

(string)

Syntax:

```
"string" "string" ...
```

`--max-results` (integer)

The maximum number of resources to return in the response. This value must be an integer greater than zero.

`--next-token` (string)

(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.

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

FileCaches -> (list)

The response object for the `DescribeFileCaches` operation.

(structure)

A description of a specific Amazon File Cache resource, which is a response object from the `DescribeFileCaches` operation.

OwnerId -> (string)

An Amazon Web Services account ID. This ID is a 12-digit number that you use to construct Amazon Resource Names (ARNs) for resources.

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileCacheId -> (string)

The system-generated, unique ID of the cache.

FileCacheType -> (string)

The type of cache, which must be `LUSTRE` .

FileCacheTypeVersion -> (string)

The Lustre version of the cache, which must be `2.12` .

Lifecycle -> (string)

The lifecycle status of the cache. The following are the possible values and what they mean:

- `AVAILABLE` - The cache is in a healthy state, and is reachable and available for use.
- `CREATING` - The new cache is being created.
- `DELETING` - An existing cache is being deleted.
- `UPDATING` - The cache is undergoing a customer-initiated update.
- `FAILED` - An existing cache has experienced an unrecoverable failure. When creating a new cache, the cache was unable to be created.

FailureDetails -> (structure)

A structure providing details of any failures that occurred.

Message -> (string)

A message describing any failures that occurred.

StorageCapacity -> (integer)

The storage capacity of the cache in gibibytes (GiB).

VpcId -> (string)

The ID of your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide* .

SubnetIds -> (list)

A list of subnet IDs that the cache will be accessible from. You can specify only one subnet ID in a call to the `CreateFileCache` operation.

(string)

The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*

NetworkInterfaceIds -> (list)

A list of network interface IDs.

(string)

An elastic network interface ID. An elastic network interface is a logical networking component in a virtual private cloud (VPC) that represents a virtual network card. For more information, see [Elastic Network Interfaces](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-eni.html) in the *Amazon EC2 User Guide for Linux Instances* .

DNSName -> (string)

The Domain Name System (DNS) name for the cache.

KmsKeyId -> (string)

Specifies the ID of the Key Management Service (KMS) key to use for encrypting data on an Amazon File Cache. If a `KmsKeyId` isnât specified, the Amazon FSx-managed KMS key for your account is used. For more information, see [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) in the *Key Management Service API Reference* .

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

LustreConfiguration -> (structure)

The configuration for the Amazon File Cache resource.

PerUnitStorageThroughput -> (integer)

Per unit storage throughput represents the megabytes per second of read or write throughput per 1 tebibyte of storage provisioned. Cache throughput capacity is equal to Storage capacity (TiB) * PerUnitStorageThroughput (MB/s/TiB). The only supported value is `1000` .

DeploymentType -> (string)

The deployment type of the Amazon File Cache resource, which must be `CACHE_1` .

MountName -> (string)

You use the `MountName` value when mounting the cache. If you pass a cache ID to the `DescribeFileCaches` operation, it returns the the `MountName` value as part of the cacheâs description.

WeeklyMaintenanceStartTime -> (string)

A recurring weekly time, in the format `D:HH:MM` .

`D` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see [the ISO-8601 spec as described on Wikipedia](https://en.wikipedia.org/wiki/ISO_week_date) .

`HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour.

For example, `1:05:00` specifies maintenance at 5 AM Monday.

MetadataConfiguration -> (structure)

The configuration for a Lustre MDT (Metadata Target) storage volume.

StorageCapacity -> (integer)

The storage capacity of the Lustre MDT (Metadata Target) storage volume in gibibytes (GiB). The only supported value is `2400` GiB.

LogConfiguration -> (structure)

The configuration for Lustre logging used to write the enabled logging events for your Amazon File Cache resource to Amazon CloudWatch Logs.

Level -> (string)

The data repository events that are logged by Amazon FSx.

- `WARN_ONLY` - only warning events are logged.
- `ERROR_ONLY` - only error events are logged.
- `WARN_ERROR` - both warning events and error events are logged.
- `DISABLED` - logging of data repository events is turned off.

Note that Amazon File Cache uses a default setting of `WARN_ERROR` , which canât be changed.

Destination -> (string)

The Amazon Resource Name (ARN) that specifies the destination of the logs. The destination can be any Amazon CloudWatch Logs log group ARN. The destination ARN must be in the same Amazon Web Services partition, Amazon Web Services Region, and Amazon Web Services account as your Amazon FSx file system.

DataRepositoryAssociationIds -> (list)

A list of IDs of data repository associations that are associated with this cache.

(string)

NextToken -> (string)

(Optional) Opaque pagination token returned from a previous operation (String). If present, this token indicates from what point you can continue processing the request, where the previous `NextToken` value left off.