# create-keyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-key.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-key.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# create-key

## Description

Creates a unique customer managed [KMS key](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms-keys) in your Amazon Web Services account and Region. You can use a KMS key in cryptographic operations, such as encryption and signing. Some Amazon Web Services services let you use KMS keys that you create and manage to protect your service resources.

A KMS key is a logical representation of a cryptographic key. In addition to the key material used in cryptographic operations, a KMS key includes metadata, such as the key ID, key policy, creation date, description, and key state. For details, see [Managing keys](https://docs.aws.amazon.com/kms/latest/developerguide/getting-started.html) in the *Key Management Service Developer Guide*

Use the parameters of `CreateKey` to specify the type of KMS key, the source of its key material, its key policy, description, tags, and other properties.

### Note

KMS has replaced the term *customer master key (CMK)* with *KMS key* and *KMS key* . The concept has not changed. To prevent breaking changes, KMS is keeping some variations of this term.

To create different types of KMS keys, use the following guidance:

Symmetric encryption KMS key

By default, `CreateKey` creates a symmetric encryption KMS key with key material that KMS generates. This is the basic and most widely used type of KMS key, and provides the best performance.

To create a symmetric encryption KMS key, you donât need to specify any parameters. The default value for `KeySpec` , `SYMMETRIC_DEFAULT` , the default value for `KeyUsage` , `ENCRYPT_DECRYPT` , and the default value for `Origin` , `AWS_KMS` , create a symmetric encryption KMS key with KMS key material.

If you need a key for basic encryption and decryption or you are creating a KMS key to protect your resources in an Amazon Web Services service, create a symmetric encryption KMS key. The key material in a symmetric encryption key never leaves KMS unencrypted. You can use a symmetric encryption KMS key to encrypt and decrypt data up to 4,096 bytes, but they are typically used to generate data keys and data keys pairs. For details, see  GenerateDataKey and  GenerateDataKeyPair .

Asymmetric KMS keys

To create an asymmetric KMS key, use the `KeySpec` parameter to specify the type of key material in the KMS key. Then, use the `KeyUsage` parameter to determine whether the KMS key will be used to encrypt and decrypt or sign and verify. You canât change these properties after the KMS key is created.

Asymmetric KMS keys contain an RSA key pair, Elliptic Curve (ECC) key pair, or an SM2 key pair (China Regions only). The private key in an asymmetric KMS key never leaves KMS unencrypted. However, you can use the  GetPublicKey operation to download the public key so it can be used outside of KMS. Each KMS key can have only one key usage. KMS keys with RSA key pairs can be used to encrypt and decrypt data or sign and verify messages (but not both). KMS keys with NIST-recommended ECC key pairs can be used to sign and verify messages or derive shared secrets (but not both). KMS keys with `ECC_SECG_P256K1` can be used only to sign and verify messages. KMS keys with SM2 key pairs (China Regions only) can be used to either encrypt and decrypt data, sign and verify messages, or derive shared secrets (you must choose one key usage type). For information about asymmetric KMS keys, see [Asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Key Management Service Developer Guide* .

HMAC KMS key

To create an HMAC KMS key, set the `KeySpec` parameter to a key spec value for HMAC KMS keys. Then set the `KeyUsage` parameter to `GENERATE_VERIFY_MAC` . You must set the key usage even though `GENERATE_VERIFY_MAC` is the only valid key usage value for HMAC KMS keys. You canât change these properties after the KMS key is created.

HMAC KMS keys are symmetric keys that never leave KMS unencrypted. You can use HMAC keys to generate ( GenerateMac ) and verify ( VerifyMac ) HMAC codes for messages up to 4096 bytes.

Multi-Region primary keys Imported key material

To create a multi-Region *primary key* in the local Amazon Web Services Region, use the `MultiRegion` parameter with a value of `True` . To create a multi-Region *replica key* , that is, a KMS key with the same key ID and key material as a primary key, but in a different Amazon Web Services Region, use the  ReplicateKey operation. To change a replica key to a primary key, and its primary key to a replica key, use the  UpdatePrimaryRegion operation.

You can create multi-Region KMS keys for all supported KMS key types: symmetric encryption KMS keys, HMAC KMS keys, asymmetric encryption KMS keys, and asymmetric signing KMS keys. You can also create multi-Region keys with imported key material. However, you canât create multi-Region keys in a custom key store.

This operation supports *multi-Region keys* , an KMS feature that lets you create multiple interoperable KMS keys in different Amazon Web Services Regions. Because these KMS keys have the same key ID, key material, and other metadata, you can use them interchangeably to encrypt data in one Amazon Web Services Region and decrypt it in a different Amazon Web Services Region without re-encrypting the data or making a cross-Region call. For more information about multi-Region keys, see [Multi-Region keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *Key Management Service Developer Guide* .

To import your own key material into a KMS key, begin by creating a KMS key with no key material. To do this, use the `Origin` parameter of `CreateKey` with a value of `EXTERNAL` . Next, use  GetParametersForImport operation to get a public key and import token. Use the wrapping public key to encrypt your key material. Then, use  ImportKeyMaterial with your import token to import the key material. For step-by-step instructions, see [Importing Key Material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the * *Key Management Service Developer Guide* * .

You can import key material into KMS keys of all supported KMS key types: symmetric encryption KMS keys, HMAC KMS keys, asymmetric encryption KMS keys, and asymmetric signing KMS keys. You can also create multi-Region keys with imported key material. However, you canât import key material into a KMS key in a custom key store.

To create a multi-Region primary key with imported key material, use the `Origin` parameter of `CreateKey` with a value of `EXTERNAL` and the `MultiRegion` parameter with a value of `True` . To create replicas of the multi-Region primary key, use the  ReplicateKey operation. For instructions, see [`Importing key material into multi-Region keys <https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-import.html >`__](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-key.html#id1) . For more information about multi-Region keys, see [Multi-Region keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *Key Management Service Developer Guide* .

Custom key store

A [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) lets you protect your Amazon Web Services resources using keys in a backing key store that you own and manage. When you request a cryptographic operation with a KMS key in a custom key store, the operation is performed in the backing key store using its cryptographic keys.

KMS supports [CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html) backed by an CloudHSM cluster and [external key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) backed by an external key manager outside of Amazon Web Services. When you create a KMS key in an CloudHSM key store, KMS generates an encryption key in the CloudHSM cluster and associates it with the KMS key. When you create a KMS key in an external key store, you specify an existing encryption key in the external key manager.

### Note

Some external key managers provide a simpler method for creating a KMS key in an external key store. For details, see your external key manager documentation.

Before you create a KMS key in a custom key store, the `ConnectionState` of the key store must be `CONNECTED` . To connect the custom key store, use the  ConnectCustomKeyStore operation. To find the `ConnectionState` , use the  DescribeCustomKeyStores operation.

To create a KMS key in a custom key store, use the `CustomKeyStoreId` . Use the default `KeySpec` value, `SYMMETRIC_DEFAULT` , and the default `KeyUsage` value, `ENCRYPT_DECRYPT` to create a symmetric encryption key. No other key type is supported in a custom key store.

To create a KMS key in an [CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html) , use the `Origin` parameter with a value of `AWS_CLOUDHSM` . The CloudHSM cluster that is associated with the custom key store must have at least two active HSMs in different Availability Zones in the Amazon Web Services Region.

To create a KMS key in an [external key store](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) , use the `Origin` parameter with a value of `EXTERNAL_KEY_STORE` and an `XksKeyId` parameter that identifies an existing external key.

### Note

Some external key managers provide a simpler method for creating a KMS key in an external key store. For details, see your external key manager documentation.

**Cross-account use** : No. You cannot use this operation to create a KMS key in a different Amazon Web Services account.

**Required permissions** : [kms:CreateKey](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy). To use the `Tags` parameter, [kms:TagResource](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (IAM policy). For examples and information about related permissions, see [Allow a user to create KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/iam-policies.html#iam-policy-example-create-key) in the *Key Management Service Developer Guide* .

**Related operations:**

- DescribeKey
- ListKeys
- ScheduleKeyDeletion

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateKey)

## Synopsis

```
create-key
[--policy <value>]
[--description <value>]
[--key-usage <value>]
[--customer-master-key-spec <value>]
[--key-spec <value>]
[--origin <value>]
[--custom-key-store-id <value>]
[--bypass-policy-lockout-safety-check | --no-bypass-policy-lockout-safety-check]
[--tags <value>]
[--multi-region | --no-multi-region]
[--xks-key-id <value>]
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

`--policy` (string)

The key policy to attach to the KMS key.

If you provide a key policy, it must meet the following criteria:

- The key policy must allow the calling principal to make a subsequent `PutKeyPolicy` request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the *Key Management Service Developer Guide* . (To omit this condition, set `BypassPolicyLockoutSafetyCheck` to true.)
- Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to KMS. When you create a new Amazon Web Services principal, you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to KMS. For more information, see [Changes that I make are not always immediately visible](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the *Amazon Web Services Identity and Access Management User Guide* .

If you do not provide a key policy, KMS attaches a default key policy to the KMS key. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default) in the *Key Management Service Developer Guide* .

The key policy size quota is 32 kilobytes (32768 bytes).

For help writing and formatting a JSON policy document, see the [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the * *Identity and Access Management User Guide* * .

`--description` (string)

A description of the KMS key. Use a description that helps you decide whether the KMS key is appropriate for a task. The default value is an empty string (no description).

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

To set or change the description after the key is created, use  UpdateKeyDescription .

`--key-usage` (string)

Determines the [cryptographic operations](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) for which you can use the KMS key. The default value is `ENCRYPT_DECRYPT` . This parameter is optional when you are creating a symmetric encryption KMS key; otherwise, it is required. You canât change the `KeyUsage` value after the KMS key is created.

Select only one valid value.

- For symmetric encryption KMS keys, omit the parameter or specify `ENCRYPT_DECRYPT` .
- For HMAC KMS keys (symmetric), specify `GENERATE_VERIFY_MAC` .
- For asymmetric KMS keys with RSA key pairs, specify `ENCRYPT_DECRYPT` or `SIGN_VERIFY` .
- For asymmetric KMS keys with NIST-recommended elliptic curve key pairs, specify `SIGN_VERIFY` or `KEY_AGREEMENT` .
- For asymmetric KMS keys with `ECC_SECG_P256K1` key pairs specify `SIGN_VERIFY` .
- For asymmetric KMS keys with SM2 key pairs (China Regions only), specify `ENCRYPT_DECRYPT` , `SIGN_VERIFY` , or `KEY_AGREEMENT` .

Possible values:

- `SIGN_VERIFY`
- `ENCRYPT_DECRYPT`
- `GENERATE_VERIFY_MAC`
- `KEY_AGREEMENT`

`--customer-master-key-spec` (string)

Instead, use the `KeySpec` parameter.

The `KeySpec` and `CustomerMasterKeySpec` parameters work the same way. Only the names differ. We recommend that you use `KeySpec` parameter in your code. However, to avoid breaking changes, KMS supports both parameters.

Possible values:

- `RSA_2048`
- `RSA_3072`
- `RSA_4096`
- `ECC_NIST_P256`
- `ECC_NIST_P384`
- `ECC_NIST_P521`
- `ECC_SECG_P256K1`
- `SYMMETRIC_DEFAULT`
- `HMAC_224`
- `HMAC_256`
- `HMAC_384`
- `HMAC_512`
- `SM2`

`--key-spec` (string)

Specifies the type of KMS key to create. The default value, `SYMMETRIC_DEFAULT` , creates a KMS key with a 256-bit AES-GCM key that is used for encryption and decryption, except in China Regions, where it creates a 128-bit symmetric key that uses SM4 encryption. For help choosing a key spec for your KMS key, see [Choosing a KMS key type](https://docs.aws.amazon.com/kms/latest/developerguide/key-types.html#symm-asymm-choose) in the * *Key Management Service Developer Guide* * .

The `KeySpec` determines whether the KMS key contains a symmetric key or an asymmetric key pair. It also determines the algorithms that the KMS key supports. You canât change the `KeySpec` after the KMS key is created. To further restrict the algorithms that can be used with the KMS key, use a condition key in its key policy or IAM policy. For more information, see [kms:EncryptionAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-encryption-algorithm) , [kms:MacAlgorithm](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-mac-algorithm) or [kms:Signing Algorithm](https://docs.aws.amazon.com/kms/latest/developerguide/policy-conditions.html#conditions-kms-signing-algorithm) in the * *Key Management Service Developer Guide* * .

### Warning

[Amazon Web Services services that are integrated with KMS](http://aws.amazon.com/kms/features/#AWS_Service_Integration) use symmetric encryption KMS keys to protect your data. These services do not support asymmetric KMS keys or HMAC KMS keys.

KMS supports the following key specs for KMS keys:

- Symmetric encryption key (default)
- `SYMMETRIC_DEFAULT`
- HMAC keys (symmetric)
- `HMAC_224`
- `HMAC_256`
- `HMAC_384`
- `HMAC_512`
- Asymmetric RSA key pairs (encryption and decryption -or- signing and verification)
- `RSA_2048`
- `RSA_3072`
- `RSA_4096`
- Asymmetric NIST-recommended elliptic curve key pairs (signing and verification -or- deriving shared secrets)
- `ECC_NIST_P256` (secp256r1)
- `ECC_NIST_P384` (secp384r1)
- `ECC_NIST_P521` (secp521r1)
- Other asymmetric elliptic curve key pairs (signing and verification)
- `ECC_SECG_P256K1` (secp256k1), commonly used for cryptocurrencies.
- SM2 key pairs (encryption and decryption -or- signing and verification -or- deriving shared secrets)
- `SM2` (China Regions only)

Possible values:

- `RSA_2048`
- `RSA_3072`
- `RSA_4096`
- `ECC_NIST_P256`
- `ECC_NIST_P384`
- `ECC_NIST_P521`
- `ECC_SECG_P256K1`
- `SYMMETRIC_DEFAULT`
- `HMAC_224`
- `HMAC_256`
- `HMAC_384`
- `HMAC_512`
- `SM2`

`--origin` (string)

The source of the key material for the KMS key. You cannot change the origin after you create the KMS key. The default is `AWS_KMS` , which means that KMS creates the key material.

To [create a KMS key with no key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys-create-cmk.html) (for imported key material), set this value to `EXTERNAL` . For more information about importing key material into KMS, see [Importing Key Material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the *Key Management Service Developer Guide* . The `EXTERNAL` origin value is valid only for symmetric KMS keys.

To [create a KMS key in an CloudHSM key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-cmk-keystore.html) and create its key material in the associated CloudHSM cluster, set this value to `AWS_CLOUDHSM` . You must also use the `CustomKeyStoreId` parameter to identify the CloudHSM key store. The `KeySpec` value must be `SYMMETRIC_DEFAULT` .

To [create a KMS key in an external key store](https://docs.aws.amazon.com/kms/latest/developerguide/create-xks-keys.html) , set this value to `EXTERNAL_KEY_STORE` . You must also use the `CustomKeyStoreId` parameter to identify the external key store and the `XksKeyId` parameter to identify the associated external key. The `KeySpec` value must be `SYMMETRIC_DEFAULT` .

Possible values:

- `AWS_KMS`
- `EXTERNAL`
- `AWS_CLOUDHSM`
- `EXTERNAL_KEY_STORE`

`--custom-key-store-id` (string)

Creates the KMS key in the specified [custom key store](https://docs.aws.amazon.com/kms/latest/developerguide/custom-key-store-overview.html) . The `ConnectionState` of the custom key store must be `CONNECTED` . To find the CustomKeyStoreID and ConnectionState use the  DescribeCustomKeyStores operation.

This parameter is valid only for symmetric encryption KMS keys in a single Region. You cannot create any other type of KMS key in a custom key store.

When you create a KMS key in an CloudHSM key store, KMS generates a non-exportable 256-bit symmetric key in its associated CloudHSM cluster and associates it with the KMS key. When you create a KMS key in an external key store, you must use the `XksKeyId` parameter to specify an external key that serves as key material for the KMS key.

`--bypass-policy-lockout-safety-check` | `--no-bypass-policy-lockout-safety-check` (boolean)

Skips (âbypassesâ) the key policy lockout safety check. The default value is false.

### Warning

Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately.

For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the *Key Management Service Developer Guide* .

Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html) request on the KMS key.

`--tags` (list)

Assigns one or more tags to the KMS key. Use this parameter to tag the KMS key when it is created. To tag an existing KMS key, use the  TagResource operation.

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

### Note

Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see [ABAC for KMS](https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) in the *Key Management Service Developer Guide* .

To use this parameter, you must have [kms:TagResource](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) permission in an IAM policy.

Each tag consists of a tag key and a tag value. Both the tag key and the tag value are required, but the tag value can be an empty (null) string. You cannot have more than one tag on a KMS key with the same tag key. If you specify an existing tag key with a different tag value, KMS replaces the current tag value with the specified one.

When you add tags to an Amazon Web Services resource, Amazon Web Services generates a cost allocation report with usage and costs aggregated by tags. Tags can also be used to control access to a KMS key. For details, see [Tagging Keys](https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html) .

(structure)

A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

For information about the rules that apply to tag keys and tag values, see [User-Defined Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html) in the *Amazon Web Services Billing and Cost Management User Guide* .

TagKey -> (string)

The key of the tag.

TagValue -> (string)

The value of the tag.

Shorthand Syntax:

```
TagKey=string,TagValue=string ...
```

JSON Syntax:

```
[
  {
    "TagKey": "string",
    "TagValue": "string"
  }
  ...
]
```

`--multi-region` | `--no-multi-region` (boolean)

Creates a multi-Region primary key that you can replicate into other Amazon Web Services Regions. You cannot change this value after you create the KMS key.

For a multi-Region key, set this parameter to `True` . For a single-Region KMS key, omit this parameter or set it to `False` . The default value is `False` .

This operation supports *multi-Region keys* , an KMS feature that lets you create multiple interoperable KMS keys in different Amazon Web Services Regions. Because these KMS keys have the same key ID, key material, and other metadata, you can use them interchangeably to encrypt data in one Amazon Web Services Region and decrypt it in a different Amazon Web Services Region without re-encrypting the data or making a cross-Region call. For more information about multi-Region keys, see [Multi-Region keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *Key Management Service Developer Guide* .

This value creates a *primary key* , not a replica. To create a *replica key* , use the  ReplicateKey operation.

You can create a symmetric or asymmetric multi-Region key, and you can create a multi-Region key with imported key material. However, you cannot create a multi-Region key in a custom key store.

`--xks-key-id` (string)

Identifies the [external key](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-external-key) that serves as key material for the KMS key in an [external key store](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) . Specify the ID that the [external key store proxy](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-xks-proxy) uses to refer to the external key. For help, see the documentation for your external key store proxy.

This parameter is required for a KMS key with an `Origin` value of `EXTERNAL_KEY_STORE` . It is not valid for KMS keys with any other `Origin` value.

The external key must be an existing 256-bit AES symmetric encryption key hosted outside of Amazon Web Services in an external key manager associated with the external key store specified by the `CustomKeyStoreId` parameter. This key must be enabled and configured to perform encryption and decryption. Each KMS key in an external key store must use a different external key. For details, see [Requirements for a KMS key in an external key store](https://docs.aws.amazon.com/create-xks-keys.html#xks-key-requirements) in the *Key Management Service Developer Guide* .

Each KMS key in an external key store is associated two backing keys. One is key material that KMS generates. The other is the external key specified by this parameter. When you use the KMS key in an external key store to encrypt data, the encryption operation is performed first by KMS using the KMS key material, and then by the external key manager using the specified external key, a process known as *double encryption* . For details, see [Double encryption](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html#concept-double-encryption) in the *Key Management Service Developer Guide* .

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

**Example 1: To create a customer managed KMS key in AWS KMS**

The following `create-key` example creates a symmetric encryption KMS key.

To create the basic KMS key, a symmetric encryption key, you do not need to specify any parameters. The default values for those parameters create a symmetric encryption key.

Because this command doesnât specify a key policy, the KMS key gets the [default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default) for programmatically created KMS keys. To view the key policy, use the `get-key-policy` command. To change the key policy, use the `put-key-policy` command.

```
aws kms create-key
```

The `create-key` command returns the key metadata, including the key ID and ARN of the new KMS key. You can use these values to identify the KMS key in other AWS KMS operations. The output does not include the tags. To view the tags for a KMS key, use the `list-resource-tags command`.

Output:

```
{
    "KeyMetadata": {
        "AWSAccountId": "111122223333",
        "Arn": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "CreationDate": "2017-07-05T14:04:55-07:00",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "Description": "",
        "Enabled": true,
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "KeyManager": "CUSTOMER",
        "KeySpec": "SYMMETRIC_DEFAULT",
        "KeyState": "Enabled",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "MultiRegion": false,
        "Origin": "AWS_KMS"
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ]
    }
}
```

Note: The `create-key` command does not let you specify an alias, To create an alias for the new KMS key, use the `create-alias` command.

For more information, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the *AWS Key Management Service Developer Guide*.

**Example 2: To create an asymmetric RSA KMS key for encryption and decryption**

The following `create-key` example creates a KMS key that contains an asymmetric RSA key pair for encryption and decryption.

```
aws kms create-key \
   --key-spec RSA_4096 \
   --key-usage ENCRYPT_DECRYPT
```

Output:

```
{
    "KeyMetadata": {
        "Arn": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "AWSAccountId": "111122223333",
        "CreationDate": "2021-04-05T14:04:55-07:00",
        "CustomerMasterKeySpec": "RSA_4096",
        "Description": "",
        "Enabled": true,
        "EncryptionAlgorithms": [
            "RSAES_OAEP_SHA_1",
            "RSAES_OAEP_SHA_256"
        ],
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "KeyManager": "CUSTOMER",
        "KeySpec": "RSA_4096",
        "KeyState": "Enabled",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "MultiRegion": false,
        "Origin": "AWS_KMS"
    }
}
```

For more information, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.

**Example 3: To create an asymmetric elliptic curve KMS key for signing and verification**

To create an asymmetric KMS key that contains an asymmetric elliptic curve (ECC) key pair for signing and verification. The `--key-usage` parameter is required even though `SIGN_VERIFY` is the only valid value for ECC KMS keys.

```
aws kms create-key \
    --key-spec ECC_NIST_P521 \
    --key-usage SIGN_VERIFY
```

Output:

```
{
    "KeyMetadata": {
        "Arn": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "AWSAccountId": "111122223333",
        "CreationDate": "2019-12-02T07:48:55-07:00",
        "CustomerMasterKeySpec": "ECC_NIST_P521",
        "Description": "",
        "Enabled": true,
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "KeyManager": "CUSTOMER",
        "KeySpec": "ECC_NIST_P521",
        "KeyState": "Enabled",
        "KeyUsage": "SIGN_VERIFY",
        "MultiRegion": false,
        "Origin": "AWS_KMS",
        "SigningAlgorithms": [
            "ECDSA_SHA_512"
        ]
    }
}
```

For more information, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.

**Example 4: To create an HMAC KMS key**

The following `create-key` example creates a 384-bit HMAC KMS key. The `GENERATE_VERIFY_MAC` value for the `--key-usage` parameter is required even though itâs the only valid value for HMAC KMS keys.

```
aws kms create-key \
    --key-spec HMAC_384 \
    --key-usage GENERATE_VERIFY_MAC
```

Output:

```
{
    "KeyMetadata": {
        "Arn": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "AWSAccountId": "111122223333",
        "CreationDate": "2022-04-05T14:04:55-07:00",
        "CustomerMasterKeySpec": "HMAC_384",
        "Description": "",
        "Enabled": true,
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "KeyManager": "CUSTOMER",
        "KeySpec": "HMAC_384",
        "KeyState": "Enabled",
        "KeyUsage": "GENERATE_VERIFY_MAC",
        "MacAlgorithms": [
            "HMAC_SHA_384"
        ],
        "MultiRegion": false,
        "Origin": "AWS_KMS"
    }
}
```

For more information, see [HMAC keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html) in the *AWS Key Management Service Developer Guide*.

**Example 4: To create a multi-Region primary KMS key**

The following `create-key` example creates a multi-Region primary symmetric encryption key. Because the default values for all parameters create a symmetric encryption key, only the `--multi-region` parameter is required for this KMS key. In the AWS CLI, to indicate that a Boolean parameter is true, just specify the parameter name.

```
aws kms create-key \
    --multi-region
```

Output:

```
{
    "KeyMetadata": {
        "Arn": "arn:aws:kms:us-west-2:111122223333:key/mrk-1234abcd12ab34cd56ef12345678990ab",
        "AWSAccountId": "111122223333",
        "CreationDate": "2021-09-02T016:15:21-09:00",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "Description": "",
        "Enabled": true,
        "EncryptionAlgorithms": [
          "SYMMETRIC_DEFAULT"
        ],
        "KeyId": "mrk-1234abcd12ab34cd56ef12345678990ab",
        "KeyManager": "CUSTOMER",
        "KeySpec": "SYMMETRIC_DEFAULT",
        "KeyState": "Enabled",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "MultiRegion": true,
        "MultiRegionConfiguration": {
            "MultiRegionKeyType": "PRIMARY",
            "PrimaryKey": {
                "Arn": "arn:aws:kms:us-west-2:111122223333:key/mrk-1234abcd12ab34cd56ef12345678990ab",
                "Region": "us-west-2"
            },
            "ReplicaKeys": []
        },
        "Origin": "AWS_KMS"
    }
}
```

For more information, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.

**Example 5: To create a KMS key for imported key material**

The following `create-key` example creates a creates a KMS key with no key material. When the operation is complete, you can import your own key material into the KMS key. To create this KMS key, set the `--origin` parameter to `EXTERNAL`.

```
aws kms create-key \
    --origin EXTERNAL
```

Output:

```
{
     "KeyMetadata": {
         "Arn": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
         "AWSAccountId": "111122223333",
         "CreationDate": "2019-12-02T07:48:55-07:00",
         "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
         "Description": "",
         "Enabled": false,
         "EncryptionAlgorithms": [
             "SYMMETRIC_DEFAULT"
         ],
         "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
         "KeyManager": "CUSTOMER",
         "KeySpec": "SYMMETRIC_DEFAULT",
         "KeyState": "PendingImport",
         "KeyUsage": "ENCRYPT_DECRYPT",
         "MultiRegion": false,
         "Origin": "EXTERNAL"
     }
 }
```

For more information, see [Importing key material in AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the *AWS Key Management Service Developer Guide*.

**Example 6: To create a KMS key in an AWS CloudHSM key store**

The following `create-key` example creates a creates a KMS key in the specified AWS CloudHSM key store. The operation creates the KMS key and its metadata in AWS KMS and creates the key material in the AWS CloudHSM cluster associated with the custom key store. The `--custom-key-store-id` and `--origin` parameters are required.

```
aws kms create-key \
    --origin AWS_CLOUDHSM \
    --custom-key-store-id cks-1234567890abcdef0
```

Output:

```
{
    "KeyMetadata": {
        "Arn": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "AWSAccountId": "111122223333",
        "CloudHsmClusterId": "cluster-1a23b4cdefg",
        "CreationDate": "2019-12-02T07:48:55-07:00",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "CustomKeyStoreId": "cks-1234567890abcdef0",
        "Description": "",
        "Enabled": true,
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "KeyManager": "CUSTOMER",
        "KeySpec": "SYMMETRIC_DEFAULT",
        "KeyState": "Enabled",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "MultiRegion": false,
        "Origin": "AWS_CLOUDHSM"
    }
}
```

For more information, see [AWS CloudHSM key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-cloudhsm.html) in the *AWS Key Management Service Developer Guide*.

**Example 7: To create a KMS key in an external key store**

The following `create-key` example creates a creates a KMS key in the specified external key store. The `--custom-key-store-id`, `--origin`, and `--xks-key-id` parameters are required in this command.

- The `--xks-key-id` parameter specifies the ID of an existing symmetric encryption key in your external key manager. This key serves as the external key material for the KMS key.
- The value of the `--origin` parameter must be `EXTERNAL_KEY_STORE`.
- The `custom-key-store-id` parameter must identify an external key store that is connected to its external key store proxy.

```
aws kms create-key \
    --origin EXTERNAL_KEY_STORE \
    --custom-key-store-id cks-9876543210fedcba9 \
    --xks-key-id bb8562717f809024
```

Output:

```
{
    "KeyMetadata": {
        "Arn": "arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
        "AWSAccountId": "111122223333",
        "CreationDate": "2022-12-02T07:48:55-07:00",
        "CustomerMasterKeySpec": "SYMMETRIC_DEFAULT",
        "CustomKeyStoreId": "cks-9876543210fedcba9",
        "Description": "",
        "Enabled": true,
        "EncryptionAlgorithms": [
            "SYMMETRIC_DEFAULT"
        ],
        "KeyId": "1234abcd-12ab-34cd-56ef-1234567890ab",
        "KeyManager": "CUSTOMER",
        "KeySpec": "SYMMETRIC_DEFAULT",
        "KeyState": "Enabled",
        "KeyUsage": "ENCRYPT_DECRYPT",
        "MultiRegion": false,
        "Origin": "EXTERNAL_KEY_STORE",
        "XksKeyConfiguration": {
            "Id": "bb8562717f809024"
        }
    }
}
```

For more information, see [External key stores](https://docs.aws.amazon.com/kms/latest/developerguide/keystore-external.html) in the *AWS Key Management Service Developer Guide*.

## Output

KeyMetadata -> (structure)

Metadata associated with the KMS key.

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