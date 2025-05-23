# create-file-cacheÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-file-cache.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-file-cache.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fsx](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/index.html#cli-aws-fsx) ]

# create-file-cache

## Description

Creates a new Amazon File Cache resource.

You can use this operation with a client request token in the request that Amazon File Cache uses to ensure idempotent creation. If a cache with the specified client request token exists and the parameters match, `CreateFileCache` returns the description of the existing cache. If a cache with the specified client request token exists and the parameters donât match, this call returns `IncompatibleParameterError` . If a file cache with the specified client request token doesnât exist, `CreateFileCache` does the following:

- Creates a new, empty Amazon File Cache resource with an assigned ID, and an initial lifecycle state of `CREATING` .
- Returns the description of the cache in JSON format.

### Note

The `CreateFileCache` call returns while the cacheâs lifecycle state is still `CREATING` . You can check the cache creation status by calling the [DescribeFileCaches](https://docs.aws.amazon.com/fsx/latest/APIReference/API_DescribeFileCaches.html) operation, which returns the cache state along with other information.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/CreateFileCache)

## Synopsis

```
create-file-cache
[--client-request-token <value>]
--file-cache-type <value>
--file-cache-type-version <value>
--storage-capacity <value>
--subnet-ids <value>
[--security-group-ids <value>]
[--tags <value>]
[--copy-tags-to-data-repository-associations | --no-copy-tags-to-data-repository-associations]
[--kms-key-id <value>]
[--lustre-configuration <value>]
[--data-repository-associations <value>]
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

`--client-request-token` (string)

An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.

By using the idempotent operation, you can retry a `CreateFileCache` operation without the risk of creating an extra cache. This approach can be useful when an initial call fails in a way that makes it unclear whether a cache was created. Examples are if a transport level timeout occurred, or your connection was reset. If you use the same client request token and the initial call created a cache, the client receives success as long as the parameters are the same.

`--file-cache-type` (string)

The type of cache that youâre creating, which must be `LUSTRE` .

Possible values:

- `LUSTRE`

`--file-cache-type-version` (string)

Sets the Lustre version for the cache that youâre creating, which must be `2.12` .

`--storage-capacity` (integer)

The storage capacity of the cache in gibibytes (GiB). Valid values are 1200 GiB, 2400 GiB, and increments of 2400 GiB.

`--subnet-ids` (list)

A list of subnet IDs that the cache will be accessible from. You can specify only one subnet ID in a call to the `CreateFileCache` operation.

(string)

The ID for a subnet. A *subnet* is a range of IP addresses in your virtual private cloud (VPC). For more information, see [VPC and subnets](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Subnets.html) in the *Amazon VPC User Guide.*

Syntax:

```
"string" "string" ...
```

`--security-group-ids` (list)

A list of IDs specifying the security groups to apply to all network interfaces created for Amazon File Cache access. This list isnât returned in later requests to describe the cache.

(string)

The ID of your Amazon EC2 security group. This ID is used to control network access to the endpoint that Amazon FSx creates on your behalf in each subnet. For more information, see [Amazon EC2 Security groups for Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-network-security.html) in the *Amazon EC2 User Guide* .

Syntax:

```
"string" "string" ...
```

`--tags` (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

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

`--copy-tags-to-data-repository-associations` | `--no-copy-tags-to-data-repository-associations` (boolean)

A boolean flag indicating whether tags for the cache should be copied to data repository associations. This value defaults to false.

`--kms-key-id` (string)

Specifies the ID of the Key Management Service (KMS) key to use for encrypting data on an Amazon File Cache. If a `KmsKeyId` isnât specified, the Amazon FSx-managed KMS key for your account is used. For more information, see [Encrypt](https://docs.aws.amazon.com/kms/latest/APIReference/API_Encrypt.html) in the *Key Management Service API Reference* .

`--lustre-configuration` (structure)

The configuration for the Amazon File Cache resource being created.

PerUnitStorageThroughput -> (integer)

Provisions the amount of read and write throughput for each 1 tebibyte (TiB) of cache storage capacity, in MB/s/TiB. The only supported value is `1000` .

DeploymentType -> (string)

Specifies the cache deployment type, which must be `CACHE_1` .

WeeklyMaintenanceStartTime -> (string)

A recurring weekly time, in the format `D:HH:MM` .

`D` is the day of the week, for which 1 represents Monday and 7 represents Sunday. For further details, see [the ISO-8601 spec as described on Wikipedia](https://en.wikipedia.org/wiki/ISO_week_date) .

`HH` is the zero-padded hour of the day (0-23), and `MM` is the zero-padded minute of the hour.

For example, `1:05:00` specifies maintenance at 5 AM Monday.

MetadataConfiguration -> (structure)

The configuration for a Lustre MDT (Metadata Target) storage volume.

StorageCapacity -> (integer)

The storage capacity of the Lustre MDT (Metadata Target) storage volume in gibibytes (GiB). The only supported value is `2400` GiB.

Shorthand Syntax:

```
PerUnitStorageThroughput=integer,DeploymentType=string,WeeklyMaintenanceStartTime=string,MetadataConfiguration={StorageCapacity=integer}
```

JSON Syntax:

```
{
  "PerUnitStorageThroughput": integer,
  "DeploymentType": "CACHE_1",
  "WeeklyMaintenanceStartTime": "string",
  "MetadataConfiguration": {
    "StorageCapacity": integer
  }
}
```

`--data-repository-associations` (list)

A list of up to 8 configurations for data repository associations (DRAs) to be created during the cache creation. The DRAs link the cache to either an Amazon S3 data repository or a Network File System (NFS) data repository that supports the NFSv3 protocol.

The DRA configurations must meet the following requirements:

- All configurations on the list must be of the same data repository type, either all S3 or all NFS. A cache canât link to different data repository types at the same time.
- An NFS DRA must link to an NFS file system that supports the NFSv3 protocol.

DRA automatic import and automatic export is not supported.

(structure)

The configuration for a data repository association (DRA) to be created during the Amazon File Cache resource creation. The DRA links the cache to either an Amazon S3 bucket or prefix, or a Network File System (NFS) data repository that supports the NFSv3 protocol.

The DRA does not support automatic import or automatic export.

FileCachePath -> (string)

A path on the cache that points to a high-level directory (such as `/ns1/` ) or subdirectory (such as `/ns1/subdir/` ) that will be mapped 1-1 with `DataRepositoryPath` . The leading forward slash in the name is required. Two data repository associations cannot have overlapping cache paths. For example, if a data repository is associated with cache path `/ns1/` , then you cannot link another data repository with cache path `/ns1/ns2` .

This path specifies where in your cache files will be exported from. This cache directory can be linked to only one data repository, and no data repository other can be linked to the directory.

### Note

The cache path can only be set to root (/) on an NFS DRA when `DataRepositorySubdirectories` is specified. If you specify root (/) as the cache path, you can create only one DRA on the cache.

The cache path cannot be set to root (/) for an S3 DRA.

DataRepositoryPath -> (string)

The path to the S3 or NFS data repository that links to the cache. You must provide one of the following paths:

- The path can be an NFS data repository that links to the cache. The path can be in one of two formats:
- If you are not using the `DataRepositorySubdirectories` parameter, the path is to an NFS Export directory (or one of its subdirectories) in the format `nfs://nfs-domain-name/exportpath` . You can therefore link a single NFS Export to a single data repository association.
- If you are using the `DataRepositorySubdirectories` parameter, the path is the domain name of the NFS file system in the format `nfs://filer-domain-name` , which indicates the root of the subdirectories specified with the `DataRepositorySubdirectories` parameter.
- The path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix/` (where `prefix` is optional).

DataRepositorySubdirectories -> (list)

A list of NFS Exports that will be linked with this data repository association. The Export paths are in the format `/exportpath1` . To use this parameter, you must configure `DataRepositoryPath` as the domain name of the NFS file system. The NFS file system domain name in effect is the root of the subdirectories. Note that `DataRepositorySubdirectories` is not supported for S3 data repositories.

(string)

NFS -> (structure)

The configuration for a data repository association that links an Amazon File Cache resource to an NFS data repository.

Version -> (string)

The version of the NFS (Network File System) protocol of the NFS data repository. The only supported value is `NFS3` , which indicates that the data repository must support the NFSv3 protocol.

DnsIps -> (list)

A list of up to 2 IP addresses of DNS servers used to resolve the NFS file system domain name. The provided IP addresses can either be the IP addresses of a DNS forwarder or resolver that the customer manages and runs inside the customer VPC, or the IP addresses of the on-premises DNS servers.

(string)

Shorthand Syntax:

```
FileCachePath=string,DataRepositoryPath=string,DataRepositorySubdirectories=string,string,NFS={Version=string,DnsIps=[string,string]} ...
```

JSON Syntax:

```
[
  {
    "FileCachePath": "string",
    "DataRepositoryPath": "string",
    "DataRepositorySubdirectories": ["string", ...],
    "NFS": {
      "Version": "NFS3",
      "DnsIps": ["string", ...]
    }
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

FileCache -> (structure)

A description of the cache that was created.

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

A structure providing details of any failures that occurred in creating a cache.

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

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

CopyTagsToDataRepositoryAssociations -> (boolean)

A boolean flag indicating whether tags for the cache should be copied to data repository associations.

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