# describe-keyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-key.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/describe-key.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# describe-key

## Description

Provides detailed information about a KMS key. You can run `DescribeKey` on a [customer managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk) or an [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) .

This detailed information includes the key ARN, creation date (and deletion date, if applicable), the key state, and the origin and expiration date (if any) of the key material. It includes fields, like `KeySpec` , that help you distinguish different types of KMS keys. It also displays the key usage (encryption, signing, or generating and verifying MACs) and the algorithms that the KMS key supports.

For [multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) , `DescribeKey` displays the primary key and all related replica keys. For KMS keys in [CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html) , it includes information about the key store, such as the key store ID and the CloudHSM cluster ID. For KMS keys in [external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) , it includes the custom key store ID and the ID of the external key.

`DescribeKey` does not return the following information:

- Aliases associated with the KMS key. To get this information, use  ListAliases .
- Whether automatic key rotation is enabled on the KMS key. To get this information, use  GetKeyRotationStatus . Also, some key states prevent a KMS key from being automatically rotated. For details, see [How Automatic Key Rotation Works](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html#rotate-keys-how-it-works) in the *Key Management Service Developer Guide* .
- Tags on the KMS key. To get this information, use  ListResourceTags .
- Key policies and grants on the KMS key. To get this information, use  GetKeyPolicy and  ListGrants .

In general, `DescribeKey` is a non-mutating operation. It returns data about KMS keys, but doesnât change them. However, Amazon Web Services services use `DescribeKey` to create [Amazon Web Services managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-managed-cmk) from a *predefined Amazon Web Services alias* with no key ID.

**Cross-account use** : Yes. To perform this operation with a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

**Required permissions** : [kms:DescribeKey](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

**Related operations:**

- GetKeyPolicy
- GetKeyRotationStatus
- ListAliases
- ListGrants
- ListKeys
- ListResourceTags
- ListRetirableGrants

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/DescribeKey)

## Synopsis

```
describe-key
--key-id <value>
[--grant-tokens <value>]
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

Describes the specified KMS key.

If you specify a predefined Amazon Web Services alias (an Amazon Web Services alias with no key ID), KMS associates the alias with an [Amazon Web Services managed key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html##aws-managed-cmk) and returns its `KeyId` and `Arn` in the response.

To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"` . To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.

For example:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

`--grant-tokens` (list)

A list of grant tokens.

Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency* . For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grant-manage.html#using-grant-token) in the *Key Management Service Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To find detailed information about a KMS key**

The following `describe-key` example gets detailed information about the AWS managed key for Amazon S3 in the example account and Region. You can use this command to find details about AWS managed keys and customer managed keys.

To specify the KMS key, use the `key-id` parameter. This example uses an alias name value, but you can use a key ID, key ARN, alias name, or alias ARN in this command.

```
aws kms describe-key \
    --key-id alias/aws/s3
```

Output:

```
{
    "KeyMetadata": {
        "AWSAccountId": "846764612917",
        "KeyId": "b8a9477d-836c-491f-857e-07937918959b",
        "Arn": "arn:aws:kms:us-west-2:846764612917:key/b8a9477d-836c-491f-857e-07937918959b",
        "CreationDate": 2017-06-30T21:44:32.140000+00:00,
        "Enabled": true,
        "Description": "Default KMS key that protects my S3 objects when no other key is defined",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "AWS",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ]
    }
}
```

For more information, see [Viewing keys](https://docs.aws.amazon.com/kms/latest/developerguide/viewing-keys.html) in the *AWS Key Management Service Developer Guide*.

**Example 2: To get details about an RSA asymmetric KMS key**

The following `describe-key` example gets detailed information about an asymmetric RSA KMS key used for signing and verification.

```
aws kms describe-key \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
```

Output:

```
{
    "KeyMetadata": {
        "AWSAccountId": "111122223333",
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "Arn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "CreationDate": "2019-12-02T19:47:14.861000+00:00",
        "CustomerMasterKeySpec": "RSA_2048",
        "Enabled": false,
        "Description": "",
        "KeyState": "Disabled",
        "Origin": "AWS_KMS",
        "MultiRegion": false,
        "KeyManager": "CUSTOMER",
        "KeySpec": "RSA_2048",
        "KeyUsage": "SIGN_VERIFY",
        "SigningAlgorithms": [
            "RSASSA_PKCS1_V1_5_SHA_256",
            "RSASSA_PKCS1_V1_5_SHA_384",
            "RSASSA_PKCS1_V1_5_SHA_512",
            "RSASSA_PSS_SHA_256",
            "RSASSA_PSS_SHA_384",
            "RSASSA_PSS_SHA_512"
        ]
    }
}
```

**Example 3: To get details about a multi-Region replica key**

The following `describe-key` example gets metadata for a multi-Region replica key. This multi-Region key is a symmetric encryption key. The output of a `describe-key` command for any multi-Region key returns information about the primary key and all of its replicas.

```
aws kms describe-key \
    --key-id arn:aws:kms:ap-northeast-1:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab
```

Output:

```
{
    "KeyMetadata": {
        "MultiRegion": true,
        "AWSAccountId": "111122223333",
        "Arn": "arn:aws:kms:ap-northeast-1:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab",
        "CreationDate": "2021-06-28T21:09:16.114000+00:00",
        "Description": "",
        "Enabled": true,
        "KeyId": "mrk-1234abcd12ab34cd56ef1234567890ab",
        "KeyManager": "CUSTOMER",
        "KeyState": "Enabled",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "Origin": "AWS_KMS",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "MultiRegionConfiguration": {
            "MultiRegionKeyType": "PRIMARY",
            "PrimaryKey": {
                "Arn": "arn:aws:kms:us-west-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab",
                "Region": "us-west-2"
            },
            "ReplicaKeys": [
                {
                    "Arn": "arn:aws:kms:eu-west-1:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab",
                    "Region": "eu-west-1"
                },
                {
                    "Arn": "arn:aws:kms:ap-northeast-1:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab",
                    "Region": "ap-northeast-1"
                },
                {
                    "Arn": "arn:aws:kms:sa-east-1:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab",
                    "Region": "sa-east-1"
                }
            ]
        }
    }
}
```

**Example 4: To get details about an HMAC KMS key**

The following `describe-key` example gets detailed information about an HMAC KMS key.

```
aws kms describe-key \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab
```

Output:

```
{
    "KeyMetadata": {
        "AWSAccountId": "123456789012",
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "Arn": "arn:aws:kms:us-west-2:123456789012:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "CreationDate": "2022-04-03T22:23:10.194000+00:00",
        "Enabled": true,
        "Description": "Test key",
        "KeyUsage": "GENERATE_VERIFY_MAC",
        "KeyState": "Enabled",
        "Origin": "AWS_KMS",
        "KeyManager": "CUSTOMER",
        "CustomerMasterKeySpec": "HMAC_256",
        "MacAlgorithms": [
            "HMAC_SHA_256"
        ],
        "MultiRegion": false
    }
}
```

## Output

KeyMetadata -> (structure)

Metadata associated with the key.

AWSAccountId -> (string)

The twelve-digit account ID of the Amazon Web Services account that owns the KMS key.

KeyId -> (string)

The globally unique identifier for the KMS key.

Arn -> (string)

The Amazon Resource Name (ARN) of the KMS key. For examples, see [Key Management Service (KMS)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-kms) in the Example ARNs section of the *Amazon Web Services General Reference* .

CreationDate -> (timestamp)

The date and time when the KMS key was created.

Enabled -> (boolean)

Specifies whether the KMS key is enabled. When `KeyState` is `Enabled` this value is true, otherwise it is false.

Description -> (string)

The description of the KMS key.

KeyUsage -> (string)

The [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) for which you can use the KMS key.

KeyState -> (string)

The current status of the KMS key.

For more information about how key state affects the use of a KMS key, see [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Key Management Service Developer Guide* .

DeletionDate -> (timestamp)

The date and time after which KMS deletes this KMS key. This value is present only when the KMS key is scheduled for deletion, that is, when its `KeyState` is `PendingDeletion` .

When the primary key in a multi-Region key is scheduled for deletion but still has replica keys, its key state is `PendingReplicaDeletion` and the length of its waiting period is displayed in the `PendingDeletionWindowInDays` field.

ValidTo -> (timestamp)

The time at which the imported key material expires. When the key material expires, KMS deletes the key material and the KMS key becomes unusable. This value is present only for KMS keys whose `Origin` is `EXTERNAL` and whose `ExpirationModel` is `KEY_MATERIAL_EXPIRES` , otherwise this value is omitted.

Origin -> (string)

The source of the key material for the KMS key. When this value is `AWS_KMS` , KMS created the key material. When this value is `EXTERNAL` , the key material was imported or the KMS key doesnât have any key material. When this value is `AWS_CLOUDHSM` , the key material was created in the CloudHSM cluster associated with a custom key store.

CustomKeyStoreId -> (string)

A unique identifier for the [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) that contains the KMS key. This field is present only when the KMS key is created in a custom key store.

CloudHsmClusterId -> (string)

The cluster ID of the CloudHSM cluster that contains the key material for the KMS key. When you create a KMS key in an CloudHSM [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) , KMS creates the key material for the KMS key in the associated CloudHSM cluster. This field is present only when the KMS key is created in an CloudHSM key store.

ExpirationModel -> (string)

Specifies whether the KMS keyâs key material expires. This value is present only when `Origin` is `EXTERNAL` , otherwise this value is omitted.

KeyManager -> (string)

The manager of the KMS key. KMS keys in your Amazon Web Services account are either customer managed or Amazon Web Services managed. For more information about the difference, see [KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) in the *Key Management Service Developer Guide* .

CustomerMasterKeySpec -> (string)

Instead, use the `KeySpec` field.

The `KeySpec` and `CustomerMasterKeySpec` fields have the same value. We recommend that you use the `KeySpec` field in your code. However, to avoid breaking changes, KMS supports both fields.

KeySpec -> (string)

Describes the type of key material in the KMS key.

EncryptionAlgorithms -> (list)

The encryption algorithms that the KMS key supports. You cannot use the KMS key with other encryption algorithms within KMS.

This value is present only when the `KeyUsage` of the KMS key is `ENCRYPT_DECRYPT` .

(string)

SigningAlgorithms -> (list)

The signing algorithms that the KMS key supports. You cannot use the KMS key with other signing algorithms within KMS.

This field appears only when the `KeyUsage` of the KMS key is `SIGN_VERIFY` .

(string)

KeyAgreementAlgorithms -> (list)

The key agreement algorithm used to derive a shared secret.

(string)

MultiRegion -> (boolean)

Indicates whether the KMS key is a multi-Region (`True` ) or regional (`False` ) key. This value is `True` for multi-Region primary and replica keys and `False` for regional KMS keys.

For more information about multi-Region keys, see [Multi-Region keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *Key Management Service Developer Guide* .

MultiRegionConfiguration -> (structure)

Lists the primary and replica keys in same multi-Region key. This field is present only when the value of the `MultiRegion` field is `True` .

For more information about any listed KMS key, use the  DescribeKey operation.

- `MultiRegionKeyType` indicates whether the KMS key is a `PRIMARY` or `REPLICA` key.
- `PrimaryKey` displays the key ARN and Region of the primary key. This field displays the current KMS key if it is the primary key.
- `ReplicaKeys` displays the key ARNs and Regions of all replica keys. This field includes the current KMS key if it is a replica key.

MultiRegionKeyType -> (string)

Indicates whether the KMS key is a `PRIMARY` or `REPLICA` key.

PrimaryKey -> (structure)

Displays the key ARN and Region of the primary key. This field includes the current KMS key if it is the primary key.

Arn -> (string)

Displays the key ARN of a primary or replica key of a multi-Region key.

Region -> (string)

Displays the Amazon Web Services Region of a primary or replica key in a multi-Region key.

ReplicaKeys -> (list)

displays the key ARNs and Regions of all replica keys. This field includes the current KMS key if it is a replica key.

(structure)

Describes the primary or replica key in a multi-Region key.

Arn -> (string)

Displays the key ARN of a primary or replica key of a multi-Region key.

Region -> (string)

Displays the Amazon Web Services Region of a primary or replica key in a multi-Region key.

PendingDeletionWindowInDays -> (integer)

The waiting period before the primary key in a multi-Region key is deleted. This waiting period begins when the last of its replica keys is deleted. This value is present only when the `KeyState` of the KMS key is `PendingReplicaDeletion` . That indicates that the KMS key is the primary key in a multi-Region key, it is scheduled for deletion, and it still has existing replica keys.

When a single-Region KMS key or a multi-Region replica key is scheduled for deletion, its deletion date is displayed in the `DeletionDate` field. However, when the primary key in a multi-Region key is scheduled for deletion, its waiting period doesnât begin until all of its replica keys are deleted. This value displays that waiting period. When the last replica key in the multi-Region key is deleted, the `KeyState` of the scheduled primary key changes from `PendingReplicaDeletion` to `PendingDeletion` and the deletion date appears in the `DeletionDate` field.

MacAlgorithms -> (list)

The message authentication code (MAC) algorithm that the HMAC KMS key supports.

This value is present only when the `KeyUsage` of the KMS key is `GENERATE_VERIFY_MAC` .

(string)

XksKeyConfiguration -> (structure)

Information about the external key that is associated with a KMS key in an external key store.

For more information, see [External key](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-external-key) in the *Key Management Service Developer Guide* .

Id -> (string)

The ID of the external key in its external key manager. This is the ID that the external key store proxy uses to identify the external key.