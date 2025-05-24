# create-stored-iscsi-volumeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-stored-iscsi-volume.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/create-stored-iscsi-volume.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [storagegateway](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/storagegateway/index.html#cli-aws-storagegateway) ]

# create-stored-iscsi-volume

## Description

Creates a volume on a specified gateway. This operation is only supported in the stored volume gateway type.

The size of the volume to create is inferred from the disk size. You can choose to preserve existing data on the disk, create volume from an existing snapshot, or create an empty volume. If you choose to create an empty gateway volume, then any existing data on the disk is erased.

In the request, you must specify the gateway and the disk information on which you are creating the volume. In response, the gateway creates the volume and returns volume information such as the volume Amazon Resource Name (ARN), its size, and the iSCSI target ARN that initiators can use to connect to the volume target.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/storagegateway-2013-06-30/CreateStorediSCSIVolume)

## Synopsis

```
create-stored-iscsi-volume
--gateway-arn <value>
--disk-id <value>
[--snapshot-id <value>]
--preserve-existing-data | --no-preserve-existing-data
--target-name <value>
--network-interface-id <value>
[--kms-encrypted | --no-kms-encrypted]
[--kms-key <value>]
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

`--gateway-arn` (string)

The Amazon Resource Name (ARN) of the gateway. Use the  ListGateways operation to return a list of gateways for your account and Amazon Web Services Region.

`--disk-id` (string)

The unique identifier for the gateway local disk that is configured as a stored volume. Use [ListLocalDisks](https://docs.aws.amazon.com/storagegateway/latest/userguide/API_ListLocalDisks.html) to list disk IDs for a gateway.

`--snapshot-id` (string)

The snapshot ID (e.g., âsnap-1122aabbâ) of the snapshot to restore as the new stored volume. Specify this field if you want to create the iSCSI storage volume from a snapshot; otherwise, do not include this field. To list snapshots for your account use [DescribeSnapshots](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/ApiReference-query-DescribeSnapshots.html) in the *Amazon Elastic Compute Cloud API Reference* .

`--preserve-existing-data` | `--no-preserve-existing-data` (boolean)

Set to `true` if you want to preserve the data on the local disk. Otherwise, set to `false` to create an empty volume.

Valid Values: `true` | `false`

`--target-name` (string)

The name of the iSCSI target used by an initiator to connect to a volume and used as a suffix for the target ARN. For example, specifying `TargetName` as *myvolume* results in the target ARN of `arn:aws:storagegateway:us-east-2:111122223333:gateway/sgw-12A3456B/target/iqn.1997-05.com.amazon:myvolume` . The target name must be unique across all volumes on a gateway.

If you donât specify a value, Storage Gateway uses the value that was previously used for this volume as the new target name.

`--network-interface-id` (string)

The network interface of the gateway on which to expose the iSCSI target. Only IPv4 addresses are accepted. Use  DescribeGatewayInformation to get a list of the network interfaces available on a gateway.

Valid Values: A valid IP address.

`--kms-encrypted` | `--no-kms-encrypted` (boolean)

Set to `true` to use Amazon S3 server-side encryption with your own KMS key, or `false` to use a key managed by Amazon S3. Optional.

Valid Values: `true` | `false`

`--kms-key` (string)

The Amazon Resource Name (ARN) of a symmetric customer master key (CMK) used for Amazon S3 server-side encryption. Storage Gateway does not support asymmetric CMKs. This value can only be set when `KMSEncrypted` is `true` . Optional.

`--tags` (list)

A list of up to 50 tags that can be assigned to a stored volume. Each tag is a key-value pair.

### Note

Valid characters for key and value are letters, spaces, and numbers representable in UTF-8 format, and the following special characters: + - = . _ : / @. The maximum length of a tagâs key is 128 characters, and the maximum length for a tagâs value is 256.

(structure)

A key-value pair that helps you manage, filter, and search for your resource. Allowed characters: letters, white space, and numbers, representable in UTF-8, and the following characters: + - = . _ : /.

Key -> (string)

Tag key. The key canât start with aws:.

Value -> (string)

Value of the tag key.

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

VolumeARN -> (string)

The Amazon Resource Name (ARN) of the configured volume.

VolumeSizeInBytes -> (long)

The size of the volume in bytes.

TargetARN -> (string)

The Amazon Resource Name (ARN) of the volume target, which includes the iSCSI name that initiators can use to connect to the target.