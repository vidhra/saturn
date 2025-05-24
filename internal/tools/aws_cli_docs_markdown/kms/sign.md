# signÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/sign.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/sign.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# sign

## Description

Creates a [digital signature](https://en.wikipedia.org/wiki/Digital_signature) for a message or message digest by using the private key in an asymmetric signing KMS key. To verify the signature, use the  Verify operation, or use the public key in the same asymmetric KMS key outside of KMS. For information about asymmetric KMS keys, see [Asymmetric KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *Key Management Service Developer Guide* .

Digital signatures are generated and verified by using asymmetric key pair, such as an RSA or ECC pair that is represented by an asymmetric KMS key. The key owner (or an authorized user) uses their private key to sign a message. Anyone with the public key can verify that the message was signed with that particular private key and that the message hasnât changed since it was signed.

To use the `Sign` operation, provide the following information:

- Use the `KeyId` parameter to identify an asymmetric KMS key with a `KeyUsage` value of `SIGN_VERIFY` . To get the `KeyUsage` value of a KMS key, use the  DescribeKey operation. The caller must have `kms:Sign` permission on the KMS key.
- Use the `Message` parameter to specify the message or message digest to sign. You can submit messages of up to 4096 bytes. To sign a larger message, generate a hash digest of the message, and then provide the hash digest in the `Message` parameter. To indicate whether the message is a full message or a digest, use the `MessageType` parameter.
- Choose a signing algorithm that is compatible with the KMS key.

### Warning

When signing a message, be sure to record the KMS key and the signing algorithm. This information is required to verify the signature.

### Note

Best practices recommend that you limit the time during which any signature is effective. This deters an attack where the actor uses a signed message to establish validity repeatedly or long after the message is superseded. Signatures do not include a timestamp, but you can include a timestamp in the signed message to help you detect when its time to refresh the signature.

To verify the signature that this operation generates, use the  Verify operation. Or use the  GetPublicKey operation to download the public key and then use the public key to verify the signature outside of KMS.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Key Management Service Developer Guide* .

**Cross-account use** : Yes. To perform this operation with a KMS key in a different Amazon Web Services account, specify the key ARN or alias ARN in the value of the `KeyId` parameter.

**Required permissions** : [kms:Sign](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

**Related operations** :  Verify

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/Sign)

## Synopsis

```
sign
--key-id <value>
--message <value>
[--message-type <value>]
[--grant-tokens <value>]
--signing-algorithm <value>
[--dry-run | --no-dry-run]
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

Identifies an asymmetric KMS key. KMS uses the private key in the asymmetric KMS key to sign the message. The `KeyUsage` type of the KMS key must be `SIGN_VERIFY` . To find the `KeyUsage` of a KMS key, use the  DescribeKey operation.

To specify a KMS key, use its key ID, key ARN, alias name, or alias ARN. When using an alias name, prefix it with `"alias/"` . To specify a KMS key in a different Amazon Web Services account, you must use the key ARN or alias ARN.

For example:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`
- Alias name: `alias/ExampleAlias`
- Alias ARN: `arn:aws:kms:us-east-2:111122223333:alias/ExampleAlias`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey . To get the alias name and alias ARN, use  ListAliases .

`--message` (blob)

Specifies the message or message digest to sign. Messages can be 0-4096 bytes. To sign a larger message, provide a message digest.

If you provide a message digest, use the `DIGEST` value of `MessageType` to prevent the digest from being hashed again while signing.

`--message-type` (string)

Tells KMS whether the value of the `Message` parameter should be hashed as part of the signing algorithm. Use `RAW` for unhashed messages; use `DIGEST` for message digests, which are already hashed.

When the value of `MessageType` is `RAW` , KMS uses the standard signing algorithm, which begins with a hash function. When the value is `DIGEST` , KMS skips the hashing step in the signing algorithm.

### Warning

Use the `DIGEST` value only when the value of the `Message` parameter is a message digest. If you use the `DIGEST` value with an unhashed message, the security of the signing operation can be compromised.

When the value of `MessageType` is `DIGEST` , the length of the `Message` value must match the length of hashed messages for the specified signing algorithm.

You can submit a message digest and omit the `MessageType` or specify `RAW` so the digest is hashed again while signing. However, this can cause verification failures when verifying with a system that assumes a single hash.

The hashing algorithm in that `Sign` uses is based on the `SigningAlgorithm` value.

- Signing algorithms that end in SHA_256 use the SHA_256 hashing algorithm.
- Signing algorithms that end in SHA_384 use the SHA_384 hashing algorithm.
- Signing algorithms that end in SHA_512 use the SHA_512 hashing algorithm.
- SM2DSA uses the SM3 hashing algorithm. For details, see [Offline verification with SM2 key pairs](https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-sm-offline-verification) .

Possible values:

- `RAW`
- `DIGEST`

`--grant-tokens` (list)

A list of grant tokens.

Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency* . For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grant-manage.html#using-grant-token) in the *Key Management Service Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--signing-algorithm` (string)

Specifies the signing algorithm to use when signing the message.

Choose an algorithm that is compatible with the type and size of the specified asymmetric KMS key. When signing with RSA key pairs, RSASSA-PSS algorithms are preferred. We include RSASSA-PKCS1-v1_5 algorithms for compatibility with existing applications.

Possible values:

- `RSASSA_PSS_SHA_256`
- `RSASSA_PSS_SHA_384`
- `RSASSA_PSS_SHA_512`
- `RSASSA_PKCS1_V1_5_SHA_256`
- `RSASSA_PKCS1_V1_5_SHA_384`
- `RSASSA_PKCS1_V1_5_SHA_512`
- `ECDSA_SHA_256`
- `ECDSA_SHA_384`
- `ECDSA_SHA_512`
- `SM2DSA`

`--dry-run` | `--no-dry-run` (boolean)

Checks if your request will succeed. `DryRun` is an optional parameter.

To learn more about how to use this parameter, see [Testing your KMS API calls](https://docs.aws.amazon.com/kms/latest/developerguide/programming-dryrun.html) in the *Key Management Service Developer Guide* .

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

**Example 1: To generate a digital signature for a message**

The following `sign` example generates a cryptographic signature for a short message. The output of the command includes a base-64 encoded `Signature` field that you can verify by using the `verify` command.

You must specify a message to sign and a signing algorithm that your asymmetric KMS key supports. To get the signing algorithms for your KMS key, use the `describe-key` command.

In AWS CLI 2.0, the value of the `message` parameter must be Base64-encoded. Or, you can save the message in a file and use the `fileb://` prefix, which tells the AWS CLI to read binary data from the file.

Before running this command, replace the example key ID with a valid key ID from your AWS account. The key ID must represent an asymmetric KMS key with a key usage of SIGN_VERIFY.

```
msg=(echo 'Hello World' | base64)

aws kms sign \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --message fileb://UnsignedMessage \
    --message-type RAW \
    --signing-algorithm RSASSA_PKCS1_V1_5_SHA_256
```

Output:

```
{
    "KeyId": "arn:aws:kms:us-west-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab",
    "Signature": "ABCDEFhpyVYyTxbafE74ccSvEJLJr3zuoV1Hfymz4qv+/fxmxNLA7SE1SiF8lHw80fKZZ3bJ...",
    "SigningAlgorithm": "RSASSA_PKCS1_V1_5_SHA_256"
}
```

For more information about using asymmetric KMS keys in AWS KMS, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.

**Example 2: To save a digital signature in a file (Linux and macOs)**

The following `sign` example generates a cryptographic signature for a short message stored in a local file. The command also gets the `Signature` property from the response, Base64-decodes it and saves it in the ExampleSignature file. You can use the signature file in a `verify` command that verifies the signature.

The `sign` command requires a Base64-encoded message and a signing algorithm that your asymmetric KMS key supports. To get the signing algorithms that your KMS key supports, use the `describe-key` command.

Before running this command, replace the example key ID with a valid key ID from your AWS account. The key ID must represent an asymmetric KMS key with a key usage of SIGN_VERIFY.

```
echo 'hello world' | base64 > EncodedMessage

aws kms sign \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --message fileb://EncodedMessage \
    --message-type RAW \
    --signing-algorithm RSASSA_PKCS1_V1_5_SHA_256 \
    --output text \
    --query Signature | base64 --decode > ExampleSignature
```

This command produces no output. This example extracts the `Signature` property of the output and saves it in a file.

For more information about using asymmetric KMS keys in AWS KMS, see [Asymmetric keys in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/symmetric-asymmetric.html) in the *AWS Key Management Service Developer Guide*.

## Output

KeyId -> (string)

The Amazon Resource Name ([key ARN](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id-key-ARN) ) of the asymmetric KMS key that was used to sign the message.

Signature -> (blob)

The cryptographic signature that was generated for the message.

- When used with the supported RSA signing algorithms, the encoding of this value is defined by [PKCS #1 in RFC 8017](https://tools.ietf.org/html/rfc8017) .
- When used with the `ECDSA_SHA_256` , `ECDSA_SHA_384` , or `ECDSA_SHA_512` signing algorithms, this value is a DER-encoded object as defined by ANSI X9.62â2005 and [RFC 3279 Section 2.2.3](https://tools.ietf.org/html/rfc3279#section-2.2.3) . This is the most commonly used signature format and is appropriate for most uses.

When you use the HTTP API or the Amazon Web Services CLI, the value is Base64-encoded. Otherwise, it is not Base64-encoded.

SigningAlgorithm -> (string)

The signing algorithm that was used to sign the message.