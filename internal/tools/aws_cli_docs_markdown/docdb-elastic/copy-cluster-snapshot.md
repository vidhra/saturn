# copy-cluster-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb-elastic/copy-cluster-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb-elastic/copy-cluster-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [docdb-elastic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb-elastic/index.html#cli-aws-docdb-elastic) ]

# copy-cluster-snapshot

## Description

Copies a snapshot of an elastic cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-elastic-2022-11-28/CopyClusterSnapshot)

## Synopsis

```
copy-cluster-snapshot
[--copy-tags | --no-copy-tags]
[--kms-key-id <value>]
--snapshot-arn <value>
[--tags <value>]
--target-snapshot-name <value>
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

`--copy-tags` | `--no-copy-tags` (boolean)

Set to `true` to copy all tags from the source cluster snapshot to the target elastic cluster snapshot. The default is `false` .

`--kms-key-id` (string)

The Amazon Web Services KMS key ID for an encrypted elastic cluster snapshot. The Amazon Web Services KMS key ID is the Amazon Resource Name (ARN), Amazon Web Services KMS key identifier, or the Amazon Web Services KMS key alias for the Amazon Web Services KMS encryption key.

If you copy an encrypted elastic cluster snapshot from your Amazon Web Services account, you can specify a value for `KmsKeyId` to encrypt the copy with a new Amazon Web ServicesS KMS encryption key. If you donât specify a value for `KmsKeyId` , then the copy of the elastic cluster snapshot is encrypted with the same `AWS` KMS key as the source elastic cluster snapshot.

To copy an encrypted elastic cluster snapshot to another Amazon Web Services region, set `KmsKeyId` to the Amazon Web Services KMS key ID that you want to use to encrypt the copy of the elastic cluster snapshot in the destination region. Amazon Web Services KMS encryption keys are specific to the Amazon Web Services region that they are created in, and you canât use encryption keys from one Amazon Web Services region in another Amazon Web Services region.

If you copy an unencrypted elastic cluster snapshot and specify a value for the `KmsKeyId` parameter, an error is returned.

`--snapshot-arn` (string)

The Amazon Resource Name (ARN) identifier of the elastic cluster snapshot.

`--tags` (map)

The tags to be assigned to the elastic cluster snapshot.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--target-snapshot-name` (string)

The identifier of the new elastic cluster snapshot to create from the source cluster snapshot. This parameter is not case sensitive.

Constraints:

- Must contain from 1 to 63 letters, numbers, or hyphens.
- The first character must be a letter.
- Cannot end with a hyphen or contain two consecutive hyphens.

Example: `elastic-cluster-snapshot-5`

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

snapshot -> (structure)

Returns information about a specific elastic cluster snapshot.

adminUserName -> (string)

The name of the elastic cluster administrator.

clusterArn -> (string)

The ARN identifier of the elastic cluster.

clusterCreationTime -> (string)

The time when the elastic cluster was created in Universal Coordinated Time (UTC).

kmsKeyId -> (string)

The KMS key identifier is the Amazon Resource Name (ARN) for the KMS encryption key. If you are creating a cluster using the same Amazon account that owns this KMS encryption key, you can use the KMS key alias instead of the ARN as the KMS encryption key. If an encryption key is not specified here, Amazon DocumentDB uses the default encryption key that KMS creates for your account. Your account has a different default encryption key for each Amazon Region.

snapshotArn -> (string)

The ARN identifier of the elastic cluster snapshot.

snapshotCreationTime -> (string)

The time when the elastic cluster snapshot was created in Universal Coordinated Time (UTC).

snapshotName -> (string)

The name of the elastic cluster snapshot.

snapshotType -> (string)

The type of cluster snapshots to be returned. You can specify one of the following values:

- `automated` - Return all cluster snapshots that Amazon DocumentDB has automatically created for your Amazon Web Services account.
- `manual` - Return all cluster snapshots that you have manually created for your Amazon Web Services account.

status -> (string)

The status of the elastic cluster snapshot.

subnetIds -> (list)

The Amazon EC2 subnet IDs for the elastic cluster.

(string)

vpcSecurityGroupIds -> (list)

A list of EC2 VPC security groups to associate with the elastic cluster.

(string)