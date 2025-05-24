# update-location-fsx-ontapÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-fsx-ontap.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/update-location-fsx-ontap.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datasync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/index.html#cli-aws-datasync) ]

# update-location-fsx-ontap

## Description

Modifies the following configuration parameters of the Amazon FSx for NetApp ONTAP transfer location that youâre using with DataSync.

For more information, see [Configuring DataSync transfers with FSx for ONTAP](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/UpdateLocationFsxOntap)

## Synopsis

```
update-location-fsx-ontap
--location-arn <value>
[--protocol <value>]
[--subdirectory <value>]
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

`--location-arn` (string)

Specifies the Amazon Resource Name (ARN) of the FSx for ONTAP transfer location that youâre updating.

`--protocol` (structure)

Specifies the data transfer protocol that DataSync uses to access your Amazon FSx file system.

NFS -> (structure)

Specifies the Network File System (NFS) protocol configuration that DataSync uses to access your FSx for OpenZFS file system or FSx for ONTAP file systemâs storage virtual machine (SVM).

MountOptions -> (structure)

Specifies how DataSync can access a location using the NFS protocol.

Version -> (string)

Specifies the NFS version that you want DataSync to use when mounting your NFS share. If the server refuses to use the version specified, the task fails.

You can specify the following options:

- `AUTOMATIC` (default): DataSync chooses NFS version 4.1.
- `NFS3` : Stateless protocol version that allows for asynchronous writes on the server.
- `NFSv4_0` : Stateful, firewall-friendly protocol version that supports delegations and pseudo file systems.
- `NFSv4_1` : Stateful protocol version that supports sessions, directory delegations, and parallel data processing. NFS version 4.1 also includes all features available in version 4.0.

### Note

DataSync currently only supports NFS version 3 with Amazon FSx for NetApp ONTAP locations.

SMB -> (structure)

Specifies the Server Message Block (SMB) protocol configuration that DataSync uses to access your FSx for ONTAP file systemâs storage virtual machine (SVM).

Domain -> (string)

Specifies the name of the Windows domain that your storage virtual machine (SVM) belongs to.

If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right SVM.

MountOptions -> (structure)

Specifies the version of the Server Message Block (SMB) protocol that DataSync uses to access an SMB file server.

Version -> (string)

By default, DataSync automatically chooses an SMB protocol version based on negotiation with your SMB file server. You also can configure DataSync to use a specific SMB version, but we recommend doing this only if DataSync has trouble negotiating with the SMB file server automatically.

These are the following options for configuring the SMB version:

- `AUTOMATIC` (default): DataSync and the SMB file server negotiate the highest version of SMB that they mutually support between 2.1 and 3.1.1. This is the recommended option. If you instead choose a specific version that your file server doesnât support, you may get an `Operation Not Supported` error.
- `SMB3` : Restricts the protocol negotiation to only SMB version 3.0.2.
- `SMB2` : Restricts the protocol negotiation to only SMB version 2.1.
- `SMB2_0` : Restricts the protocol negotiation to only SMB version 2.0.
- `SMB1` : Restricts the protocol negotiation to only SMB version 1.0.

### Note

The `SMB1` option isnât available when [creating an Amazon FSx for NetApp ONTAP location](https://docs.aws.amazon.com/datasync/latest/userguide/API_CreateLocationFsxOntap.html) .

Password -> (string)

Specifies the password of a user who has permission to access your SVM.

User -> (string)

Specifies a user that can mount and access the files, folders, and metadata in your SVM.

For information about choosing a user with the right level of access for your transfer, see [Using the SMB protocol](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-smb) .

Shorthand Syntax:

```
NFS={MountOptions={Version=string}},SMB={Domain=string,MountOptions={Version=string},Password=string,User=string}
```

JSON Syntax:

```
{
  "NFS": {
    "MountOptions": {
      "Version": "AUTOMATIC"|"NFS3"|"NFS4_0"|"NFS4_1"
    }
  },
  "SMB": {
    "Domain": "string",
    "MountOptions": {
      "Version": "AUTOMATIC"|"SMB2"|"SMB3"|"SMB1"|"SMB2_0"
    },
    "Password": "string",
    "User": "string"
  }
}
```

`--subdirectory` (string)

Specifies a path to the file share in the storage virtual machine (SVM) where you want to transfer data to or from.

You can specify a junction path (also known as a mount point), qtree path (for NFS file shares), or share name (for SMB file shares). For example, your mount path might be `/vol1` , `/vol1/tree1` , or `/share1` .

### Note

Donât specify a junction path in the SVMâs root volume. For more information, see [Managing FSx for ONTAP storage virtual machines](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-svms.html) in the *Amazon FSx for NetApp ONTAP User Guide* .

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

None