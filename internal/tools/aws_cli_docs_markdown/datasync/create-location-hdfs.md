# create-location-hdfsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-location-hdfs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-location-hdfs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datasync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/index.html#cli-aws-datasync) ]

# create-location-hdfs

## Description

Creates a transfer *location* for a Hadoop Distributed File System (HDFS). DataSync can use this location as a source or destination for transferring data.

Before you begin, make sure that you understand how DataSync [accesses HDFS clusters](https://docs.aws.amazon.com/datasync/latest/userguide/create-hdfs-location.html#accessing-hdfs) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/CreateLocationHdfs)

## Synopsis

```
create-location-hdfs
[--subdirectory <value>]
--name-nodes <value>
[--block-size <value>]
[--replication-factor <value>]
[--kms-key-provider-uri <value>]
[--qop-configuration <value>]
--authentication-type <value>
[--simple-user <value>]
[--kerberos-principal <value>]
[--kerberos-keytab <value>]
[--kerberos-krb5-conf <value>]
--agent-arns <value>
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

`--subdirectory` (string)

A subdirectory in the HDFS cluster. This subdirectory is used to read data from or write data to the HDFS cluster. If the subdirectory isnât specified, it will default to `/` .

`--name-nodes` (list)

The NameNode that manages the HDFS namespace. The NameNode performs operations such as opening, closing, and renaming files and directories. The NameNode contains the information to map blocks of data to the DataNodes. You can use only one NameNode.

(structure)

The NameNode of the Hadoop Distributed File System (HDFS). The NameNode manages the file systemâs namespace. The NameNode performs operations such as opening, closing, and renaming files and directories. The NameNode contains the information to map blocks of data to the DataNodes.

Hostname -> (string)

The hostname of the NameNode in the HDFS cluster. This value is the IP address or Domain Name Service (DNS) name of the NameNode. An agent thatâs installed on-premises uses this hostname to communicate with the NameNode in the network.

Port -> (integer)

The port that the NameNode uses to listen to client requests.

Shorthand Syntax:

```
Hostname=string,Port=integer ...
```

JSON Syntax:

```
[
  {
    "Hostname": "string",
    "Port": integer
  }
  ...
]
```

`--block-size` (integer)

The size of data blocks to write into the HDFS cluster. The block size must be a multiple of 512 bytes. The default block size is 128 mebibytes (MiB).

`--replication-factor` (integer)

The number of DataNodes to replicate the data to when writing to the HDFS cluster. By default, data is replicated to three DataNodes.

`--kms-key-provider-uri` (string)

The URI of the HDFS clusterâs Key Management Server (KMS).

`--qop-configuration` (structure)

The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the Hadoop Distributed File System (HDFS) cluster. If `QopConfiguration` isnât specified, `RpcProtection` and `DataTransferProtection` default to `PRIVACY` . If you set `RpcProtection` or `DataTransferProtection` , the other parameter assumes the same value.

RpcProtection -> (string)

The RPC protection setting configured on the HDFS cluster. This setting corresponds to your `hadoop.rpc.protection` setting in your `core-site.xml` file on your Hadoop cluster.

DataTransferProtection -> (string)

The data transfer protection setting configured on the HDFS cluster. This setting corresponds to your `dfs.data.transfer.protection` setting in the `hdfs-site.xml` file on your Hadoop cluster.

Shorthand Syntax:

```
RpcProtection=string,DataTransferProtection=string
```

JSON Syntax:

```
{
  "RpcProtection": "DISABLED"|"AUTHENTICATION"|"INTEGRITY"|"PRIVACY",
  "DataTransferProtection": "DISABLED"|"AUTHENTICATION"|"INTEGRITY"|"PRIVACY"
}
```

`--authentication-type` (string)

The type of authentication used to determine the identity of the user.

Possible values:

- `SIMPLE`
- `KERBEROS`

`--simple-user` (string)

The user name used to identify the client on the host operating system.

### Note

If `SIMPLE` is specified for `AuthenticationType` , this parameter is required.

`--kerberos-principal` (string)

The Kerberos principal with access to the files and folders on the HDFS cluster.

### Note

If `KERBEROS` is specified for `AuthenticationType` , this parameter is required.

`--kerberos-keytab` (blob)

The Kerberos key table (keytab) that contains mappings between the defined Kerberos principal and the encrypted keys. You can load the keytab from a file by providing the fileâs address.

### Note

If `KERBEROS` is specified for `AuthenticationType` , this parameter is required.

`--kerberos-krb5-conf` (blob)

The `krb5.conf` file that contains the Kerberos configuration information. You can load the `krb5.conf` file by providing the fileâs address. If youâre using the CLI, it performs the base64 encoding for you. Otherwise, provide the base64-encoded text.

### Note

If `KERBEROS` is specified for `AuthenticationType` , this parameter is required.

`--agent-arns` (list)

The Amazon Resource Names (ARNs) of the DataSync agents that can connect to your HDFS cluster.

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (list)

The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.

(structure)

A key-value pair representing a single tag thatâs been applied to an Amazon Web Services resource.

Key -> (string)

The key for an Amazon Web Services resource tag.

Value -> (string)

The value for an Amazon Web Services resource tag.

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

LocationArn -> (string)

The ARN of the source HDFS cluster location that you create.