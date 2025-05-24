# replicate-keyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/replicate-key.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/replicate-key.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# replicate-key

## Description

Replicates a multi-Region key into the specified Region. This operation creates a multi-Region replica key based on a multi-Region primary key in a different Region of the same Amazon Web Services partition. You can create multiple replicas of a primary key, but each must be in a different Region. To create a multi-Region primary key, use the  CreateKey operation.

This operation supports *multi-Region keys* , an KMS feature that lets you create multiple interoperable KMS keys in different Amazon Web Services Regions. Because these KMS keys have the same key ID, key material, and other metadata, you can use them interchangeably to encrypt data in one Amazon Web Services Region and decrypt it in a different Amazon Web Services Region without re-encrypting the data or making a cross-Region call. For more information about multi-Region keys, see [Multi-Region keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html) in the *Key Management Service Developer Guide* .

A *replica key* is a fully-functional KMS key that can be used independently of its primary and peer replica keys. A primary key and its replica keys share properties that make them interoperable. They have the same [key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-id) and key material. They also have the same [key spec](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-spec) , [key usage](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-usage) , [key material origin](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-origin) , and [automatic key rotation status](https://docs.aws.amazon.com/kms/latest/developerguide/rotate-keys.html) . KMS automatically synchronizes these shared properties among related multi-Region keys. All other properties of a replica key can differ, including its [key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) , [tags](https://docs.aws.amazon.com/kms/latest/developerguide/tagging-keys.html) , [aliases](https://docs.aws.amazon.com/kms/latest/developerguide/kms-alias.html) , and [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) . KMS pricing and quotas for KMS keys apply to each primary key and replica key.

When this operation completes, the new replica key has a transient key state of `Creating` . This key state changes to `Enabled` (or `PendingImport` ) after a few seconds when the process of creating the new replica key is complete. While the key state is `Creating` , you can manage key, but you cannot yet use it in cryptographic operations. If you are creating and using the replica key programmatically, retry on `KMSInvalidStateException` or call `DescribeKey` to check its `KeyState` value before using it. For details about the `Creating` key state, see [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Key Management Service Developer Guide* .

You cannot create more than one replica of a primary key in any Region. If the Region already includes a replica of the key youâre trying to replicate, `ReplicateKey` returns an `AlreadyExistsException` error. If the key state of the existing replica is `PendingDeletion` , you can cancel the scheduled key deletion ( CancelKeyDeletion ) or wait for the key to be deleted. The new replica key you create will have the same [shared properties](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-overview.html#mrk-sync-properties) as the original replica key.

The CloudTrail log of a `ReplicateKey` operation records a `ReplicateKey` operation in the primary keyâs Region and a  CreateKey operation in the replica keyâs Region.

If you replicate a multi-Region primary key with imported key material, the replica key is created with no key material. You must import the same key material that you imported into the primary key. For details, see [Importing key material into multi-Region keys](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-import.html) in the *Key Management Service Developer Guide* .

To convert a replica key to a primary key, use the  UpdatePrimaryRegion operation.

### Note

`ReplicateKey` uses different default values for the `KeyPolicy` and `Tags` parameters than those used in the KMS console. For details, see the parameter descriptions.

**Cross-account use** : No. You cannot use this operation to create a replica key in a different Amazon Web Services account.

**Required permissions** :

- `kms:ReplicateKey` on the primary key (in the primary keyâs Region). Include this permission in the primary keyâs key policy.
- `kms:CreateKey` in an IAM policy in the replica Region.
- To use the `Tags` parameter, `kms:TagResource` in an IAM policy in the replica Region.

**Related operations**

- CreateKey
- UpdatePrimaryRegion

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ReplicateKey)

## Synopsis

```
replicate-key
--key-id <value>
--replica-region <value>
[--policy <value>]
[--bypass-policy-lockout-safety-check | --no-bypass-policy-lockout-safety-check]
[--description <value>]
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

`--key-id` (string)

Identifies the multi-Region primary key that is being replicated. To determine whether a KMS key is a multi-Region primary key, use the  DescribeKey operation to check the value of the `MultiRegionKeyType` property.

Specify the key ID or key ARN of a multi-Region primary key.

For example:

- Key ID: `mrk-1234abcd12ab34cd56ef1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/mrk-1234abcd12ab34cd56ef1234567890ab`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey .

`--replica-region` (string)

The Region ID of the Amazon Web Services Region for this replica key.

Enter the Region ID, such as `us-east-1` or `ap-southeast-2` . For a list of Amazon Web Services Regions in which KMS is supported, see [KMS service endpoints](https://docs.aws.amazon.com/general/latest/gr/kms.html#kms_region) in the *Amazon Web Services General Reference* .

### Note

HMAC KMS keys are not supported in all Amazon Web Services Regions. If you try to replicate an HMAC KMS key in an Amazon Web Services Region in which HMAC keys are not supported, the `ReplicateKey` operation returns an `UnsupportedOperationException` . For a list of Regions in which HMAC KMS keys are supported, see [HMAC keys in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/hmac.html) in the *Key Management Service Developer Guide* .

The replica must be in a different Amazon Web Services Region than its primary key and other replicas of that primary key, but in the same Amazon Web Services partition. KMS must be available in the replica Region. If the Region is not enabled by default, the Amazon Web Services account must be enabled in the Region. For information about Amazon Web Services partitions, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* . For information about enabling and disabling Regions, see [Enabling a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-enable) and [Disabling a Region](https://docs.aws.amazon.com/general/latest/gr/rande-manage.html#rande-manage-disable) in the *Amazon Web Services General Reference* .

`--policy` (string)

The key policy to attach to the KMS key. This parameter is optional. If you do not provide a key policy, KMS attaches the [default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html#key-policy-default) to the KMS key.

The key policy is not a shared property of multi-Region keys. You can specify the same key policy or a different key policy for each key in a set of related multi-Region keys. KMS does not synchronize this property.

If you provide a key policy, it must meet the following criteria:

- The key policy must allow the calling principal to make a subsequent `PutKeyPolicy` request on the KMS key. This reduces the risk that the KMS key becomes unmanageable. For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the *Key Management Service Developer Guide* . (To omit this condition, set `BypassPolicyLockoutSafetyCheck` to true.)
- Each statement in the key policy must contain one or more principals. The principals in the key policy must exist and be visible to KMS. When you create a new Amazon Web Services principal, you might need to enforce a delay before including the new principal in a key policy because the new principal might not be immediately visible to KMS. For more information, see [Changes that I make are not always immediately visible](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_general.html#troubleshoot_general_eventual-consistency) in the *Amazon Web Services Identity and Access Management User Guide* .

A key policy document can include only the following characters:

- Printable ASCII characters from the space character (`\u0020` ) through the end of the ASCII character range.
- Printable characters in the Basic Latin and Latin-1 Supplement character set (through `\u00FF` ).
- The tab (`\u0009` ), line feed (`\u000A` ), and carriage return (`\u000D` ) special characters

For information about key policies, see [Key policies in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/key-policies.html) in the *Key Management Service Developer Guide* . For help writing and formatting a JSON policy document, see the [IAM JSON Policy Reference](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html) in the * *Identity and Access Management User Guide* * .

`--bypass-policy-lockout-safety-check` | `--no-bypass-policy-lockout-safety-check` (boolean)

Skips (âbypassesâ) the key policy lockout safety check. The default value is false.

### Warning

Setting this value to true increases the risk that the KMS key becomes unmanageable. Do not set this value to true indiscriminately.

For more information, see [Default key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-default.html#prevent-unmanageable-key) in the *Key Management Service Developer Guide* .

Use this parameter only when you intend to prevent the principal that is making the request from making a subsequent [PutKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_PutKeyPolicy.html) request on the KMS key.

`--description` (string)

A description of the KMS key. The default value is an empty string (no description).

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

The description is not a shared property of multi-Region keys. You can specify the same description or a different description for each key in a set of related multi-Region keys. KMS does not synchronize this property.

`--tags` (list)

Assigns one or more tags to the replica key. Use this parameter to tag the KMS key when it is created. To tag an existing KMS key, use the  TagResource operation.

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

### Note

Tagging or untagging a KMS key can allow or deny permission to the KMS key. For details, see [ABAC for KMS](https://docs.aws.amazon.com/kms/latest/developerguide/abac.html) in the *Key Management Service Developer Guide* .

To use this parameter, you must have [kms:TagResource](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) permission in an IAM policy.

Tags are not a shared property of multi-Region keys. You can specify the same tags or different tags for each key in a set of related multi-Region keys. KMS does not synchronize this property.

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

ReplicaKeyMetadata -> (structure)

Displays details about the new replica key, including its Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) ) and [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) . It also includes the ARN and Amazon Web Services Region of its primary key and other replica keys.

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

ReplicaPolicy -> (string)

The key policy of the new replica key. The value is a key policy document in JSON format.

ReplicaTags -> (list)

The tags on the new replica key. The value is a list of tag key and tag value pairs.

(structure)

A key-value pair. A tag consists of a tag key and a tag value. Tag keys and tag values are both required, but tag values can be empty (null) strings.

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

For information about the rules that apply to tag keys and tag values, see [User-Defined Tag Restrictions](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/allocation-tag-restrictions.html) in the *Amazon Web Services Billing and Cost Management User Guide* .

TagKey -> (string)

The key of the tag.

TagValue -> (string)

The value of the tag.