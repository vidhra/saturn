# get-key-rotation-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-key-rotation-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/get-key-rotation-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# get-key-rotation-status

## Description

Provides detailed information about the rotation status for a KMS key, including whether [automatic rotation of the key material](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) is enabled for the specified KMS key, the [rotation period](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotation-period) , and the next scheduled rotation date.

Automatic key rotation is supported only on [symmetric encryption KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#symmetric-cmks) . You cannot enable automatic rotation of [asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) , [HMAC KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html) , KMS keys with [imported key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) , or KMS keys in a [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) . To enable or disable automatic rotation of a set of related [multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-manage.html#multi-region-rotate) , set the property on the primary key..

You can enable ( EnableKeyRotation ) and disable automatic rotation ( DisableKeyRotation ) of the key material in customer managed KMS keys. Key material rotation of [Amazon Web Services managed KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) is not configurable. KMS always rotates the key material in Amazon Web Services managed KMS keys every year. The key rotation status for Amazon Web Services managed KMS keys is always `true` .

You can perform on-demand ( RotateKeyOnDemand ) rotation of the key material in customer managed KMS keys, regardless of whether or not automatic key rotation is enabled. You can use GetKeyRotationStatus to identify the date and time that an in progress on-demand rotation was initiated. You can use  ListKeyRotations to view the details of completed rotations.

### Note

In May 2022, KMS changed the rotation schedule for Amazon Web Services managed keys from every three years to every year. For details, see  EnableKeyRotation .

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Key Management Service Developer Guide* .

- Disabled: The key rotation status does not change when you disable a KMS key. However, while the KMS key is disabled, KMS does not rotate the key material. When you re-enable the KMS key, rotation resumes. If the key material in the re-enabled KMS key hasnât been rotated in one year, KMS rotates it immediately, and every year thereafter. If itâs been less than a year since the key material in the re-enabled KMS key was rotated, the KMS key resumes its prior rotation schedule.
- Pending deletion: While a KMS key is pending deletion, its key rotation status is `false` and KMS does not rotate the key material. If you cancel the deletion, the original key rotation status returns to `true` .

**Cross-account use** : Yes. To perform this operation on a KMS key in a different Amazon Web Services account, specify the key ARN in the value of the `KeyId` parameter.

**Required permissions** : [kms:GetKeyRotationStatus](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

**Related operations:**

- DisableKeyRotation
- EnableKeyRotation
- ListKeyRotations
- RotateKeyOnDemand

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/GetKeyRotationStatus)

## Synopsis

```
get-key-rotation-status
--key-id <value>
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

`--key-id` (string)

Gets the rotation status for the specified KMS key.

Specify the key ID or key ARN of the KMS key. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN.

For example:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey .

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To retrieve the rotation status for a KMS key.**

The following `get-key-rotation-status` example returns information about the rotation status of the specified KMS key, including whether automatic rotation is enabled, the rotation period, and the next scheduled rotation date. You can use this command on customer managed KMS keys and AWS managed KMS keys. However, all AWS managed KMS keys are automatically rotated every year.

```
aws kms get-key-rotation-status \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
```

Output:

```
{
    "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
    "KeyRotationEnabled": true,
    "NextRotationDate": "2024-02-14T18:14:33.587000+00:00",
    "RotationPeriodInDays": 365
}
```

For more information, see [Rotating keys](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) in the *AWS Key Management Service Developer Guide*.

## Output

KeyRotationEnabled -> (boolean)

A Boolean value that specifies whether key rotation is enabled.

KeyId -> (string)

Identifies the specified symmetric encryption KMS key.

RotationPeriodInDays -> (integer)

The number of days between each automatic rotation. The default value is 365 days.

NextRotationDate -> (timestamp)

The next date that KMS will automatically rotate the key material.

OnDemandRotationStartDate -> (timestamp)

Identifies the date and time that an in progress on-demand rotation was initiated.

The KMS API follows an [eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) model due to the distributed nature of the system. As a result, there might be a slight delay between initiating on-demand key rotation and the rotationâs completion. Once the on-demand rotation is complete, use  ListKeyRotations to view the details of the on-demand rotation.