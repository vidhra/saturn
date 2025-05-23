# create-location-smbÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-location-smb.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/create-location-smb.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datasync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datasync/index.html#cli-aws-datasync) ]

# create-location-smb

## Description

Creates a transfer *location* for a Server Message Block (SMB) file server. DataSync can use this location as a source or destination for transferring data.

Before you begin, make sure that you understand how DataSync accesses SMB file servers. For more information, see [Providing DataSync access to SMB file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datasync-2018-11-09/CreateLocationSmb)

## Synopsis

```
create-location-smb
--subdirectory <value>
--server-hostname <value>
[--user <value>]
[--domain <value>]
[--password <value>]
--agent-arns <value>
[--mount-options <value>]
[--tags <value>]
[--authentication-type <value>]
[--dns-ip-addresses <value>]
[--kerberos-principal <value>]
[--kerberos-keytab <value>]
[--kerberos-krb5-conf <value>]
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

Specifies the name of the share exported by your SMB file server where DataSync will read or write data. You can include a subdirectory in the share path (for example, `/path/to/subdirectory` ). Make sure that other SMB clients in your network can also mount this path.

To copy all data in the subdirectory, DataSync must be able to mount the SMB share and access all of its data. For more information, see [Providing DataSync access to SMB file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions) .

`--server-hostname` (string)

Specifies the domain name or IP address of the SMB file server that your DataSync agent connects to.

Remember the following when configuring this parameter:

- You canât specify an IP version 6 (IPv6) address.
- If youâre using Kerberos authentication, you must specify a domain name.

`--user` (string)

Specifies the user that can mount and access the files, folders, and file metadata in your SMB file server. This parameter applies only if `AuthenticationType` is set to `NTLM` .

For information about choosing a user with the right level of access for your transfer, see [Providing DataSync access to SMB file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions) .

`--domain` (string)

Specifies the Windows domain name that your SMB file server belongs to. This parameter applies only if `AuthenticationType` is set to `NTLM` .

If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right file server.

`--password` (string)

Specifies the password of the user who can mount your SMB file server and has permission to access the files and folders involved in your transfer. This parameter applies only if `AuthenticationType` is set to `NTLM` .

`--agent-arns` (list)

Specifies the DataSync agent (or agents) that can connect to your SMB file server. You specify an agent by using its Amazon Resource Name (ARN).

(string)

Syntax:

```
"string" "string" ...
```

`--mount-options` (structure)

Specifies the version of the SMB protocol that DataSync uses to access your SMB file server.

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

Shorthand Syntax:

```
Version=string
```

JSON Syntax:

```
{
  "Version": "AUTOMATIC"|"SMB2"|"SMB3"|"SMB1"|"SMB2_0"
}
```

`--tags` (list)

Specifies labels that help you categorize, filter, and search for your Amazon Web Services resources. We recommend creating at least a name tag for your location.

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

`--authentication-type` (string)

Specifies the authentication protocol that DataSync uses to connect to your SMB file server. DataSync supports `NTLM` (default) and `KERBEROS` authentication.

For more information, see [Providing DataSync access to SMB file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions) .

Possible values:

- `NTLM`
- `KERBEROS`

`--dns-ip-addresses` (list)

Specifies the IPv4 addresses for the DNS servers that your SMB file server belongs to. This parameter applies only if `AuthenticationType` is set to `KERBEROS` .

If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right SMB file server.

(string)

Syntax:

```
"string" "string" ...
```

`--kerberos-principal` (string)

Specifies a Kerberos prinicpal, which is an identity in your Kerberos realm that has permission to access the files, folders, and file metadata in your SMB file server.

A Kerberos principal might look like `HOST/kerberosuser@MYDOMAIN.ORG` .

Principal names are case sensitive. Your DataSync task execution will fail if the principal that you specify for this parameter doesnât exactly match the principal that you use to create the keytab file.

`--kerberos-keytab` (blob)

Specifies your Kerberos key table (keytab) file, which includes mappings between your Kerberos principal and encryption keys.

To avoid task execution errors, make sure that the Kerberos principal that you use to create the keytab file matches exactly what you specify for `KerberosPrincipal` .

`--kerberos-krb5-conf` (blob)

Specifies a Kerberos configuration file (`krb5.conf` ) that defines your Kerberos realm configuration.

The file must be base64 encoded. If youâre using the CLI, the encoding is done for you.

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

The ARN of the SMB location that you created.