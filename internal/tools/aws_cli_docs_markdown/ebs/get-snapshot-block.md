# get-snapshot-blockÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ebs/get-snapshot-block.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ebs/get-snapshot-block.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ebs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ebs/index.html#cli-aws-ebs) ]

# get-snapshot-block

## Description

Returns the data in a block in an Amazon Elastic Block Store snapshot.

### Note

You should always retry requests that receive server (`5xx` ) error responses, and `ThrottlingException` and `RequestThrottledException` client error responses. For more information see [Error retries](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/error-retries.html) in the *Amazon Elastic Compute Cloud User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ebs-2019-11-02/GetSnapshotBlock)

## Synopsis

```
get-snapshot-block
--snapshot-id <value>
--block-index <value>
--block-token <value>
<outfile>
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

`--snapshot-id` (string)

The ID of the snapshot containing the block from which to get data.

### Warning

If the specified snapshot is encrypted, you must have permission to use the KMS key that was used to encrypt the snapshot. For more information, see [Using encryption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebsapis-using-encryption.html) in the *Amazon Elastic Compute Cloud User Guide* .

`--block-index` (integer)

The block index of the block in which to read the data. A block index is a logical index in units of `512` KiB blocks. To identify the block index, divide the logical offset of the data in the logical volume by the block size (logical offset of data/`524288` ). The logical offset of the data must be `512` KiB aligned.

`--block-token` (string)

The block token of the block from which to get data. You can obtain the `BlockToken` by running the `ListChangedBlocks` or `ListSnapshotBlocks` operations.

`outfile` (string)
Filename where the content will be saved

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

DataLength -> (integer)

The size of the data in the block.

BlockData -> (streaming blob)

The data content of the block.

Checksum -> (string)

The checksum generated for the block, which is Base64 encoded.

ChecksumAlgorithm -> (string)

The algorithm used to generate the checksum for the block, such as SHA256.