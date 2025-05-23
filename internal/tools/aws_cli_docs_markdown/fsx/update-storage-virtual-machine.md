# update-storage-virtual-machineÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/update-storage-virtual-machine.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/update-storage-virtual-machine.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fsx](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fsx/index.html#cli-aws-fsx) ]

# update-storage-virtual-machine

## Description

Updates an FSx for ONTAP storage virtual machine (SVM).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fsx-2018-03-01/UpdateStorageVirtualMachine)

## Synopsis

```
update-storage-virtual-machine
[--active-directory-configuration <value>]
[--client-request-token <value>]
--storage-virtual-machine-id <value>
[--svm-admin-password <value>]
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

`--active-directory-configuration` (structure)

Specifies updates to an SVMâs Microsoft Active Directory (AD) configuration.

SelfManagedActiveDirectoryConfiguration -> (structure)

Specifies changes you are making to the self-managed Microsoft Active Directory configuration to which an FSx for Windows File Server file system or an FSx for ONTAP SVM is joined.

UserName -> (string)

Specifies the updated user name for the service account on your self-managed Active Directory domain. Amazon FSx uses this account to join to your self-managed Active Directory domain.

This account must have the permissions required to join computers to the domain in the organizational unit provided in `OrganizationalUnitDistinguishedName` .

Password -> (string)

Specifies the updated password for the service account on your self-managed Active Directory domain. Amazon FSx uses this account to join to your self-managed Active Directory domain.

DnsIps -> (list)

A list of up to three DNS server or domain controller IP addresses in your self-managed Active Directory domain.

(string)

DomainName -> (string)

Specifies an updated fully qualified domain name of your self-managed Active Directory configuration.

OrganizationalUnitDistinguishedName -> (string)

Specifies an updated fully qualified distinguished name of the organization unit within your self-managed Active Directory.

FileSystemAdministratorsGroup -> (string)

For FSx for ONTAP file systems only - Specifies the updated name of the self-managed Active Directory domain group whose members are granted administrative privileges for the Amazon FSx resource.

NetBiosName -> (string)

Specifies an updated NetBIOS name of the AD computer object `NetBiosName` to which an SVM is joined.

Shorthand Syntax:

```
SelfManagedActiveDirectoryConfiguration={UserName=string,Password=string,DnsIps=[string,string],DomainName=string,OrganizationalUnitDistinguishedName=string,FileSystemAdministratorsGroup=string},NetBiosName=string
```

JSON Syntax:

```
{
  "SelfManagedActiveDirectoryConfiguration": {
    "UserName": "string",
    "Password": "string",
    "DnsIps": ["string", ...],
    "DomainName": "string",
    "OrganizationalUnitDistinguishedName": "string",
    "FileSystemAdministratorsGroup": "string"
  },
  "NetBiosName": "string"
}
```

`--client-request-token` (string)

(Optional) An idempotency token for resource creation, in a string of up to 63 ASCII characters. This token is automatically filled on your behalf when you use the Command Line Interface (CLI) or an Amazon Web Services SDK.

`--storage-virtual-machine-id` (string)

The ID of the SVM that you want to update, in the format `svm-0123456789abcdef0` .

`--svm-admin-password` (string)

Specifies a new SvmAdminPassword.

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

StorageVirtualMachine -> (structure)

Describes the Amazon FSx for NetApp ONTAP storage virtual machine (SVM) configuration.

ActiveDirectoryConfiguration -> (structure)

Describes the Microsoft Active Directory configuration to which the SVM is joined, if applicable.

NetBiosName -> (string)

The NetBIOS name of the AD computer object to which the SVM is joined.

SelfManagedActiveDirectoryConfiguration -> (structure)

The configuration of the self-managed Microsoft Active Directory (AD) directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

DomainName -> (string)

The fully qualified domain name of the self-managed AD directory.

OrganizationalUnitDistinguishedName -> (string)

The fully qualified distinguished name of the organizational unit within the self-managed AD directory to which the Windows File Server or ONTAP storage virtual machine (SVM) instance is joined.

FileSystemAdministratorsGroup -> (string)

The name of the domain group whose members have administrative privileges for the FSx file system.

UserName -> (string)

The user name for the service account on your self-managed AD domain that FSx uses to join to your AD domain.

DnsIps -> (list)

A list of up to three IP addresses of DNS servers or domain controllers in the self-managed AD directory.

(string)

CreationTime -> (timestamp)

The time that the resource was created, in seconds (since 1970-01-01T00:00:00Z), also known as Unix time.

Endpoints -> (structure)

The endpoints that are used to access data or to manage the SVM using the NetApp ONTAP CLI, REST API, or NetApp CloudManager. They are the `Iscsi` , `Management` , `Nfs` , and `Smb` endpoints.

Iscsi -> (structure)

An endpoint for connecting using the Internet Small Computer Systems Interface (iSCSI) protocol.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

The SVM endpointâs IP addresses.

(string)

Management -> (structure)

An endpoint for managing SVMs using the NetApp ONTAP CLI, NetApp ONTAP API, or NetApp CloudManager.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

The SVM endpointâs IP addresses.

(string)

Nfs -> (structure)

An endpoint for connecting using the Network File System (NFS) protocol.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

The SVM endpointâs IP addresses.

(string)

Smb -> (structure)

An endpoint for connecting using the Server Message Block (SMB) protocol.

DNSName -> (string)

The file systemâs DNS name. You can mount your file system using its DNS name.

IpAddresses -> (list)

The SVM endpointâs IP addresses.

(string)

FileSystemId -> (string)

The globally unique ID of the file system, assigned by Amazon FSx.

Lifecycle -> (string)

Describes the SVMâs lifecycle status.

- `CREATED` - The SVM is fully available for use.
- `CREATING` - Amazon FSx is creating the new SVM.
- `DELETING` - Amazon FSx is deleting an existing SVM.
- `FAILED` - Amazon FSx was unable to create the SVM.
- `MISCONFIGURED` - The SVM is in a failed but recoverable state.
- `PENDING` - Amazon FSx has not started creating the SVM.

Name -> (string)

The name of the SVM, if provisioned.

ResourceARN -> (string)

The Amazon Resource Name (ARN) for a given resource. ARNs uniquely identify Amazon Web Services resources. We require an ARN when you need to specify a resource unambiguously across all of Amazon Web Services. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

StorageVirtualMachineId -> (string)

The SVMâs system generated unique ID.

Subtype -> (string)

Describes the SVMâs subtype.

UUID -> (string)

The SVMâs UUID (universally unique identifier).

Tags -> (list)

A list of `Tag` values, with a maximum of 50 elements.

(structure)

Specifies a key-value pair for a resource tag.

Key -> (string)

A value that specifies the `TagKey` , the name of the tag. Tag keys must be unique for the resource to which they are attached.

Value -> (string)

A value that specifies the `TagValue` , the value assigned to the corresponding tag key. Tag values can be null and donât have to be unique in a tag set. For example, you can have a key-value pair in a tag set of `finances : April` and also of `payroll : April` .

LifecycleTransitionReason -> (structure)

Describes why the SVM lifecycle state changed.

Message -> (string)

A detailed error message.

RootVolumeSecurityStyle -> (string)

The security style of the root volume of the SVM.