# create-data-repository-associationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-data-repository-association.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/create-data-repository-association.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fsx](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/index.html#cli-aws-fsx) ]

# create-data-repository-association

## Description

Creates an Amazon FSx for Lustre data repository association (DRA). A data repository association is a link between a directory on the file system and an Amazon S3 bucket or prefix. You can have a maximum of 8 data repository associations on a file system. Data repository associations are supported on all FSx for Lustre 2.12 and 2.15 file systems, excluding `scratch_1` deployment type.

Each data repository association must have a unique Amazon FSx file system directory and a unique S3 bucket or prefix associated with it. You can configure a data repository association for automatic import only, for automatic export only, or for both. To learn more about linking a data repository to your file system, see [Linking your file system to an S3 bucket](https://docs.aws.amazon.com/fsx/latest/LustreGuide/create-dra-linked-data-repo.html) .

### Note

`CreateDataRepositoryAssociation` isnât supported on Amazon File Cache resources. To create a DRA on Amazon File Cache, use the `CreateFileCache` operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/CreateDataRepositoryAssociation)

## Synopsis

```
create-data-repository-association
--file-system-id <value>
[--file-system-path <value>]
--data-repository-path <value>
[--batch-import-meta-data-on-create | --no-batch-import-meta-data-on-create]
[--imported-file-chunk-size <value>]
[--s3 <value>]
[--client-request-token <value>]
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

`--file-system-id` (string)

The globally unique ID of the file system, assigned by Amazon FSx.

`--file-system-path` (string)

A path on the file system that points to a high-level directory (such as `/ns1/` ) or subdirectory (such as `/ns1/subdir/` ) that will be mapped 1-1 with `DataRepositoryPath` . The leading forward slash in the name is required. Two data repository associations cannot have overlapping file system paths. For example, if a data repository is associated with file system path `/ns1/` , then you cannot link another data repository with file system path `/ns1/ns2` .

This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.

### Note

If you specify only a forward slash (`/` ) as the file system path, you can link only one data repository to the file system. You can only specify â/â as the file system path for the first data repository associated with a file system.

`--data-repository-path` (string)

The path to the Amazon S3 data repository that will be linked to the file system. The path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix/` (where `prefix` is optional). This path specifies where in the S3 data repository files will be imported from or exported to.

`--batch-import-meta-data-on-create` | `--no-batch-import-meta-data-on-create` (boolean)

Set to `true` to run an import data repository task to import metadata from the data repository to the file system after the data repository association is created. Default is `false` .

`--imported-file-chunk-size` (integer)

For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system.

The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.

`--s3` (structure)

The configuration for an Amazon S3 data repository linked to an Amazon FSx Lustre file system with a data repository association. The configuration defines which file events (new, changed, or deleted files or directories) are automatically imported from the linked data repository to the file system or automatically exported from the file system to the data repository.

AutoImportPolicy -> (structure)

Specifies the type of updated objects (new, changed, deleted) that will be automatically imported from the linked S3 bucket to your file system.

Events -> (list)

The `AutoImportPolicy` can have the following event values:

- `NEW` - Amazon FSx automatically imports metadata of files added to the linked S3 bucket that do not currently exist in the FSx file system.
- `CHANGED` - Amazon FSx automatically updates file metadata and invalidates existing file content on the file system as files change in the data repository.
- `DELETED` - Amazon FSx automatically deletes files on the file system as corresponding files are deleted in the data repository.

You can define any combination of event types for your `AutoImportPolicy` .

(string)

AutoExportPolicy -> (structure)

Specifies the type of updated objects (new, changed, deleted) that will be automatically exported from your file system to the linked S3 bucket.

Events -> (list)

The `AutoExportPolicy` can have the following event values:

- `NEW` - New files and directories are automatically exported to the data repository as they are added to the file system.
- `CHANGED` - Changes to files and directories on the file system are automatically exported to the data repository.
- `DELETED` - Files and directories are automatically deleted on the data repository when they are deleted on the file system.

You can define any combination of event types for your `AutoExportPolicy` .

(string)

Shorthand Syntax:

```
AutoImportPolicy={Events=[string,string]},AutoExportPolicy={Events=[string,string]}
```

JSON Syntax:

```
{
  "AutoImportPolicy": {
    "Events": ["NEW"|"CHANGED"|"DELETED", ...]
  },
  "AutoExportPolicy": {
    "Events": ["NEW"|"CHANGED"|"DELETED", ...]
  }
}
```

`--client-request-token` (string)

(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.

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

Association -> (structure)

The response object returned after the data repository association is created.

AssociationId -> (string)

The system-generated, unique ID of the data repository association.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

FileSystemId -> (string)

The globally unique ID of the file system, assigned by Amazon FSx.

Lifecycle -> (string)

Describes the state of a data repository association. The lifecycle can have the following values:

- `CREATING` - The data repository association between the file system or cache and the data repository is being created. The data repository is unavailable.
- `AVAILABLE` - The data repository association is available for use.
- `MISCONFIGURED` - The data repository association is misconfigured. Until the configuration is corrected, automatic import and automatic export will not work (only for Amazon FSx for Lustre).
- `UPDATING` - The data repository association is undergoing a customer initiated update that might affect its availability.
- `DELETING` - The data repository association is undergoing a customer initiated deletion.
- `FAILED` - The data repository association is in a terminal state that cannot be recovered.

FailureDetails -> (structure)

Provides detailed information about the data repository if its `Lifecycle` is set to `MISCONFIGURED` or `FAILED` .

Message -> (string)

A detailed error message.

FileSystemPath -> (string)

A path on the Amazon FSx for Lustre file system that points to a high-level directory (such as `/ns1/` ) or subdirectory (such as `/ns1/subdir/` ) that will be mapped 1-1 with `DataRepositoryPath` . The leading forward slash in the name is required. Two data repository associations cannot have overlapping file system paths. For example, if a data repository is associated with file system path `/ns1/` , then you cannot link another data repository with file system path `/ns1/ns2` .

This path specifies where in your file system files will be exported from or imported to. This file system directory can be linked to only one Amazon S3 bucket, and no other S3 bucket can be linked to the directory.

### Note

If you specify only a forward slash (`/` ) as the file system path, you can link only one data repository to the file system. You can only specify â/â as the file system path for the first data repository associated with a file system.

DataRepositoryPath -> (string)

The path to the data repository that will be linked to the cache or file system.

- For Amazon File Cache, the path can be an NFS data repository that will be linked to the cache. The path can be in one of two formats:
- If you are not using the `DataRepositorySubdirectories` parameter, the path is to an NFS Export directory (or one of its subdirectories) in the format `nsf://nfs-domain-name/exportpath` . You can therefore link a single NFS Export to a single data repository association.
- If you are using the `DataRepositorySubdirectories` parameter, the path is the domain name of the NFS file system in the format `nfs://filer-domain-name` , which indicates the root of the subdirectories specified with the `DataRepositorySubdirectories` parameter.
- For Amazon File Cache, the path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix/` (where `prefix` is optional).
- For Amazon FSx for Lustre, the path can be an S3 bucket or prefix in the format `s3://bucket-name/prefix/` (where `prefix` is optional).

BatchImportMetaDataOnCreate -> (boolean)

A boolean flag indicating whether an import data repository task to import metadata should run after the data repository association is created. The task runs if this flag is set to `true` .

### Note

`BatchImportMetaDataOnCreate` is not supported for data repositories linked to an Amazon File Cache resource.

ImportedFileChunkSize -> (integer)

For files imported from a data repository, this value determines the stripe count and maximum amount of data per file (in MiB) stored on a single physical disk. The maximum number of disks that a single file can be striped across is limited by the total number of disks that make up the file system or cache.

The default chunk size is 1,024 MiB (1 GiB) and can go as high as 512,000 MiB (500 GiB). Amazon S3 objects have a maximum size of 5 TB.

S3 -> (structure)

The configuration for an Amazon S3 data repository linked to an Amazon FSx for Lustre file system with a data repository association.

AutoImportPolicy -> (structure)

Specifies the type of updated objects (new, changed, deleted) that will be automatically imported from the linked S3 bucket to your file system.

Events -> (list)

The `AutoImportPolicy` can have the following event values:

- `NEW` - Amazon FSx automatically imports metadata of files added to the linked S3 bucket that do not currently exist in the FSx file system.
- `CHANGED` - Amazon FSx automatically updates file metadata and invalidates existing file content on the file system as files change in the data repository.
- `DELETED` - Amazon FSx automatically deletes files on the file system as corresponding files are deleted in the data repository.

You can define any combination of event types for your `AutoImportPolicy` .

(string)

AutoExportPolicy -> (structure)

Specifies the type of updated objects (new, changed, deleted) that will be automatically exported from your file system to the linked S3 bucket.

Events -> (list)

The `AutoExportPolicy` can have the following event values:

- `NEW` - New files and directories are automatically exported to the data repository as they are added to the file system.
- `CHANGED` - Changes to files and directories on the file system are automatically exported to the data repository.
- `DELETED` - Files and directories are automatically deleted on the data repository when they are deleted on the file system.

You can define any combination of event types for your `AutoExportPolicy` .

(string)

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

FileCacheId -> (string)

The globally unique ID of the Amazon File Cache resource.

FileCachePath -> (string)

A path on the Amazon File Cache that points to a high-level directory (such as `/ns1/` ) or subdirectory (such as `/ns1/subdir/` ) that will be mapped 1-1 with `DataRepositoryPath` . The leading forward slash in the path is required. Two data repository associations cannot have overlapping cache paths. For example, if a data repository is associated with cache path `/ns1/` , then you cannot link another data repository with cache path `/ns1/ns2` .

This path specifies the directory in your cache where files will be exported from. This cache directory can be linked to only one data repository (S3 or NFS) and no other data repository can be linked to the directory.

### Note

The cache path can only be set to root (/) on an NFS DRA when `DataRepositorySubdirectories` is specified. If you specify root (/) as the cache path, you can create only one DRA on the cache.

The cache path cannot be set to root (/) for an S3 DRA.

DataRepositorySubdirectories -> (list)

For Amazon File Cache, a list of NFS Exports that will be linked with an NFS data repository association. All the subdirectories must be on a single NFS file system. The Export paths are in the format `/exportpath1` . To use this parameter, you must configure `DataRepositoryPath` as the domain name of the NFS file system. The NFS file system domain name in effect is the root of the subdirectories. Note that `DataRepositorySubdirectories` is not supported for S3 data repositories.

(string)

NFS -> (structure)

The configuration for an NFS data repository linked to an Amazon File Cache resource with a data repository association.

Version -> (string)

The version of the NFS (Network File System) protocol of the NFS data repository. Currently, the only supported value is `NFS3` , which indicates that the data repository must support the NFSv3 protocol.

DnsIps -> (list)

A list of up to 2 IP addresses of DNS servers used to resolve the NFS file system domain name. The provided IP addresses can either be the IP addresses of a DNS forwarder or resolver that the customer manages and runs inside the customer VPC, or the IP addresses of the on-premises DNS servers.

(string)

AutoExportPolicy -> (structure)

This parameter is not supported for Amazon File Cache.

Events -> (list)

The `AutoExportPolicy` can have the following event values:

- `NEW` - New files and directories are automatically exported to the data repository as they are added to the file system.
- `CHANGED` - Changes to files and directories on the file system are automatically exported to the data repository.
- `DELETED` - Files and directories are automatically deleted on the data repository when they are deleted on the file system.

You can define any combination of event types for your `AutoExportPolicy` .

(string)