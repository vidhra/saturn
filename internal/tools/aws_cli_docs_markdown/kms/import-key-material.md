# import-key-materialÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/import-key-material.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/import-key-material.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# import-key-material

## Description

Imports or reimports key material into an existing KMS key that was created without key material. `ImportKeyMaterial` also sets the expiration model and expiration date of the imported key material.

By default, KMS keys are created with key material that KMS generates. This operation supports [Importing key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) , an advanced feature that lets you generate and import the cryptographic key material for a KMS key. For more information about importing key material into KMS, see [Importing key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the *Key Management Service Developer Guide* .

After you successfully import key material into a KMS key, you can [reimport the same key material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html#reimport-key-material) into that KMS key, but you cannot import different key material. You might reimport key material to replace key material that expired or key material that you deleted. You might also reimport key material to change the expiration model or expiration date of the key material.

Each time you import key material into KMS, you can determine whether (`ExpirationModel` ) and when (`ValidTo` ) the key material expires. To change the expiration of your key material, you must import it again, either by calling `ImportKeyMaterial` or using the [import features](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/kms/latest/developerguide/importing-keys-import-key-material.html#importing-keys-import-key-material-console) of the KMS console.

Before calling `ImportKeyMaterial` :

- Create or identify a KMS key with no key material. The KMS key must have an `Origin` value of `EXTERNAL` , which indicates that the KMS key is designed for imported key material.  To create an new KMS key for imported key material, call the  CreateKey operation with an `Origin` value of `EXTERNAL` . You can create a symmetric encryption KMS key, HMAC KMS key, asymmetric encryption KMS key, or asymmetric signing KMS key. You can also import key material into a [multi-Region key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/kms/latest/developerguide/multi-region-keys-overview.html) of any supported type. However, you canât import key material into a KMS key in a [custom key store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/kms/latest/developerguide/custom-key-store-overview.html) .
- Use the  DescribeKey operation to verify that the `KeyState` of the KMS key is `PendingImport` , which indicates that the KMS key has no key material.  If you are reimporting the same key material into an existing KMS key, you might need to call the  DeleteImportedKeyMaterial to delete its existing key material.
- Call the  GetParametersForImport operation to get a public key and import token set for importing key material.
- Use the public key in the  GetParametersForImport response to encrypt your key material.

Then, in an `ImportKeyMaterial` request, you submit your encrypted key material and import token. When calling this operation, you must specify the following values:

- The key ID or key ARN of the KMS key to associate with the imported key material. Its `Origin` must be `EXTERNAL` and its `KeyState` must be `PendingImport` . You cannot perform this operation on a KMS key in a [custom key store](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/kms/latest/developerguide/custom-key-store-overview.html) , or on a KMS key in a different Amazon Web Services account. To get the `Origin` and `KeyState` of a KMS key, call  DescribeKey .
- The encrypted key material.
- The import token that  GetParametersForImport returned. You must use a public key and token from the same `GetParametersForImport` response.
- Whether the key material expires (`ExpirationModel` ) and, if so, when (`ValidTo` ). For help with this choice, see [Setting an expiration time](https://docs.aws.amazon.com/en_us/kms/latest/developerguide/importing-keys.html#importing-keys-expiration) in the *Key Management Service Developer Guide* . If you set an expiration date, KMS deletes the key material from the KMS key on the specified date, making the KMS key unusable. To use the KMS key in cryptographic operations again, you must reimport the same key material. However, you can delete and reimport the key material at any time, including before the key material expires. Each time you reimport, you can eliminate or reset the expiration time.

When this operation is successful, the key state of the KMS key changes from `PendingImport` to `Enabled` , and you can use the KMS key in cryptographic operations.

If this operation fails, use the exception to help determine the problem. If the error is related to the key material, the import token, or wrapping key, use  GetParametersForImport to get a new public key and import token for the KMS key and repeat the import procedure. For help, see [How To Import Key Material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html#importing-keys-overview) in the *Key Management Service Developer Guide* .

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Key Management Service Developer Guide* .

**Cross-account use** : No. You cannot perform this operation on a KMS key in a different Amazon Web Services account.

**Required permissions** : [kms:ImportKeyMaterial](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

**Related operations:**

- DeleteImportedKeyMaterial
- GetParametersForImport

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/ImportKeyMaterial)

## Synopsis

```
import-key-material
--key-id <value>
--import-token <value>
--encrypted-key-material <value>
[--valid-to <value>]
[--expiration-model <value>]
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

The identifier of the KMS key that will be associated with the imported key material. This must be the same KMS key specified in the `KeyID` parameter of the corresponding  GetParametersForImport request. The `Origin` of the KMS key must be `EXTERNAL` and its `KeyState` must be `PendingImport` .

The KMS key can be a symmetric encryption KMS key, HMAC KMS key, asymmetric encryption KMS key, or asymmetric signing KMS key, including a [multi-Region key](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/kms/latest/developerguide/multi-region-keys-overview.html) of any supported type. You cannot perform this operation on a KMS key in a custom key store, or on a KMS key in a different Amazon Web Services account.

Specify the key ID or key ARN of the KMS key.

For example:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey .

`--import-token` (blob)

The import token that you received in the response to a previous  GetParametersForImport request. It must be from the same response that contained the public key that you used to encrypt the key material.

`--encrypted-key-material` (blob)

The encrypted key material to import. The key material must be encrypted under the public wrapping key that  GetParametersForImport returned, using the wrapping algorithm that you specified in the same `GetParametersForImport` request.

`--valid-to` (timestamp)

The date and time when the imported key material expires. This parameter is required when the value of the `ExpirationModel` parameter is `KEY_MATERIAL_EXPIRES` . Otherwise it is not valid.

The value of this parameter must be a future date and time. The maximum value is 365 days from the request date.

When the key material expires, KMS deletes the key material from the KMS key. Without its key material, the KMS key is unusable. To use the KMS key in cryptographic operations, you must reimport the same key material.

You cannot change the `ExpirationModel` or `ValidTo` values for the current import after the request completes. To change either value, you must delete ( DeleteImportedKeyMaterial ) and reimport the key material.

`--expiration-model` (string)

Specifies whether the key material expires. The default is `KEY_MATERIAL_EXPIRES` . For help with this choice, see [Setting an expiration time](https://docs.aws.amazon.com/en_us/kms/latest/developerguide/importing-keys.html#importing-keys-expiration) in the *Key Management Service Developer Guide* .

When the value of `ExpirationModel` is `KEY_MATERIAL_EXPIRES` , you must specify a value for the `ValidTo` parameter. When value is `KEY_MATERIAL_DOES_NOT_EXPIRE` , you must omit the `ValidTo` parameter.

You cannot change the `ExpirationModel` or `ValidTo` values for the current import after the request completes. To change either value, you must reimport the key material.

Possible values:

- `KEY_MATERIAL_EXPIRES`
- `KEY_MATERIAL_DOES_NOT_EXPIRE`

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

**To import key material into a KMS key**

The following `import-key-material` example uploads key material into a KMS key that was created with no key material. The key state of the KMS key must be `PendingImport`.

This command uses key material that you encrypted with the public key that the `get-parameters-for-import` command returned. It also uses the import token from the same `get-parameters-for-import` command.

The `expiration-model` parameter indicates that the key material automatically expires on the date and time specified by the `valid-to` parameter. When the key material expires, AWS KMS deletes the key material, the key state of the KMS key changes to `Pending import` and the KMS key becomes unusable. To restore the KMS key, you must reimport the same key material. To use different key material, you must create a new KMS key.

Before running this command, replace the example key ID with a valid key ID or key ARN from your AWS account.

```
aws kms import-key-material \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --encrypted-key-material fileb://EncryptedKeyMaterial.bin \
    --import-token fileb://ImportToken.bin \
    --expiration-model KEY_MATERIAL_EXPIRES \
    --valid-to 2021-09-21T19:00:00Z
```

This command produces no output.

For more information about importing key material, see [Importing Key Material](https://docs.aws.amazon.com/kms/latest/developerguide/importing-keys.html) in the *AWS Key Management Service Developer Guide*.

## Output

None