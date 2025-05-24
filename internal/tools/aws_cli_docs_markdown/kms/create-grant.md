# create-grantÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-grant.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/create-grant.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kms/index.html#cli-aws-kms) ]

# create-grant

## Description

Adds a grant to a KMS key.

A *grant* is a policy instrument that allows Amazon Web Services principals to use KMS keys in cryptographic operations. It also can allow them to view a KMS key ( DescribeKey ) and create and manage grants. When authorizing access to a KMS key, grants are considered along with key policies and IAM policies. Grants are often used for temporary permissions because you can create one, use its permissions, and delete it without changing your key policies or IAM policies.

For detailed information about grants, including grant terminology, see [Grants in KMS](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the * *Key Management Service Developer Guide* * . For examples of working with grants in several programming languages, see [Programming grants](https://docs.aws.amazon.com/kms/latest/developerguide/programming-grants.html) .

The `CreateGrant` operation returns a `GrantToken` and a `GrantId` .

- When you create, retire, or revoke a grant, there might be a brief delay, usually less than five minutes, until the grant is available throughout KMS. This state is known as *eventual consistency* . Once the grant has achieved eventual consistency, the grantee principal can use the permissions in the grant without identifying the grant.  However, to use the permissions in the grant immediately, use the `GrantToken` that `CreateGrant` returns. For details, see [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grant-manage.html#using-grant-token) in the * *Key Management Service Developer Guide* * .
- The `CreateGrant` operation also returns a `GrantId` . You can use the `GrantId` and a key identifier to identify the grant in the  RetireGrant and  RevokeGrant operations. To find the grant ID, use the  ListGrants or  ListRetirableGrants operations.

The KMS key that you use for this operation must be in a compatible key state. For details, see [Key states of KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/key-state.html) in the *Key Management Service Developer Guide* .

**Cross-account use** : Yes. To perform this operation on a KMS key in a different Amazon Web Services account, specify the key ARN in the value of the `KeyId` parameter.

**Required permissions** : [kms:CreateGrant](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) (key policy)

**Related operations:**

- ListGrants
- ListRetirableGrants
- RetireGrant
- RevokeGrant

**Eventual consistency** : The KMS API follows an eventual consistency model. For more information, see [KMS eventual consistency](https://docs.aws.amazon.com/kms/latest/developerguide/programming-eventual-consistency.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kms-2014-11-01/CreateGrant)

## Synopsis

```
create-grant
--key-id <value>
--grantee-principal <value>
[--retiring-principal <value>]
--operations <value>
[--constraints <value>]
[--grant-tokens <value>]
[--name <value>]
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

Identifies the KMS key for the grant. The grant gives principals permission to use this KMS key.

Specify the key ID or key ARN of the KMS key. To specify a KMS key in a different Amazon Web Services account, you must use the key ARN.

For example:

- Key ID: `1234abcd-12ab-34cd-56ef-1234567890ab`
- Key ARN: `arn:aws:kms:us-east-2:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab`

To get the key ID and key ARN for a KMS key, use  ListKeys or  DescribeKey .

`--grantee-principal` (string)

The identity that gets the permissions specified in the grant.

To specify the grantee principal, use the Amazon Resource Name (ARN) of an Amazon Web Services principal. Valid principals include Amazon Web Services accounts, IAM users, IAM roles, federated users, and assumed role users. For help with the ARN syntax for a principal, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) in the * *Identity and Access Management User Guide* * .

`--retiring-principal` (string)

The principal that has permission to use the  RetireGrant operation to retire the grant.

To specify the principal, use the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an Amazon Web Services principal. Valid principals include Amazon Web Services accounts, IAM users, IAM roles, federated users, and assumed role users. For help with the ARN syntax for a principal, see [IAM ARNs](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-arns) in the * *Identity and Access Management User Guide* * .

The grant determines the retiring principal. Other principals might have permission to retire the grant or revoke the grant. For details, see  RevokeGrant and [Retiring and revoking grants](https://docs.aws.amazon.com/kms/latest/developerguide/grant-manage.html#grant-delete) in the *Key Management Service Developer Guide* .

`--operations` (list)

A list of operations that the grant permits.

This list must include only operations that are permitted in a grant. Also, the operation must be supported on the KMS key. For example, you cannot create a grant for a symmetric encryption KMS key that allows the  Sign operation, or a grant for an asymmetric KMS key that allows the  GenerateDataKey operation. If you try, KMS returns a `ValidationError` exception. For details, see [Grant operations](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-grant-operations) in the *Key Management Service Developer Guide* .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Decrypt
  Encrypt
  GenerateDataKey
  GenerateDataKeyWithoutPlaintext
  ReEncryptFrom
  ReEncryptTo
  Sign
  Verify
  GetPublicKey
  CreateGrant
  RetireGrant
  DescribeKey
  GenerateDataKeyPair
  GenerateDataKeyPairWithoutPlaintext
  GenerateMac
  VerifyMac
  DeriveSharedSecret
```

`--constraints` (structure)

Specifies a grant constraint.

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

KMS supports the `EncryptionContextEquals` and `EncryptionContextSubset` grant constraints, which allow the permissions in the grant only when the encryption context in the request matches (`EncryptionContextEquals` ) or includes (`EncryptionContextSubset` ) the encryption context specified in the constraint.

The encryption context grant constraints are supported only on [grant operations](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#terms-grant-operations) that include an `EncryptionContext` parameter, such as cryptographic operations on symmetric encryption KMS keys. Grants with grant constraints can include the  DescribeKey and  RetireGrant operations, but the constraint doesnât apply to these operations. If a grant with a grant constraint includes the `CreateGrant` operation, the constraint requires that any grants created with the `CreateGrant` permission have an equally strict or stricter encryption context constraint.

You cannot use an encryption context grant constraint for cryptographic operations with asymmetric KMS keys or HMAC KMS keys. Operations with these keys donât support an encryption context.

Each constraint value can include up to 8 encryption context pairs. The encryption context value in each constraint cannot exceed 384 characters. For information about grant constraints, see [Using grant constraints](https://docs.aws.amazon.com/kms/latest/developerguide/create-grant-overview.html#grant-constraints) in the *Key Management Service Developer Guide* . For more information about encryption context, see [Encryption context](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#encrypt_context) in the * *Key Management Service Developer Guide* * .

EncryptionContextSubset -> (map)

A list of key-value pairs that must be included in the encryption context of the [cryptographic operation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) request. The grant allows the cryptographic operation only when the encryption context in the request includes the key-value pairs specified in this constraint, although it can include additional key-value pairs.

key -> (string)

value -> (string)

EncryptionContextEquals -> (map)

A list of key-value pairs that must match the encryption context in the [cryptographic operation](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#cryptographic-operations) request. The grant allows the operation only when the encryption context in the request is the same as the encryption context specified in this constraint.

key -> (string)

value -> (string)

Shorthand Syntax:

```
EncryptionContextSubset={KeyName1=string,KeyName2=string},EncryptionContextEquals={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "EncryptionContextSubset": {"string": "string"
    ...},
  "EncryptionContextEquals": {"string": "string"
    ...}
}
```

`--grant-tokens` (list)

A list of grant tokens.

Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency* . For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grant-manage.html#using-grant-token) in the *Key Management Service Developer Guide* .

(string)

Syntax:

```
"string" "string" ...
```

`--name` (string)

A friendly name for the grant. Use this value to prevent the unintended creation of duplicate grants when retrying this request.

### Warning

Do not include confidential or sensitive information in this field. This field may be displayed in plaintext in CloudTrail logs and other output.

When this value is absent, all `CreateGrant` requests result in a new grant with a unique `GrantId` even if all the supplied parameters are identical. This can result in unintended duplicates when you retry the `CreateGrant` request.

When this value is present, you can retry a `CreateGrant` request with identical parameters; if the grant already exists, the original `GrantId` is returned without creating a new grant. Note that the returned grant token is unique with every `CreateGrant` request, even when a duplicate `GrantId` is returned. All grant tokens for the same grant ID can be used interchangeably.

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

**To create a grant**

The following `create-grant` example creates a grant that allows the `exampleUser` user to use the `decrypt` command on the `1234abcd-12ab-34cd-56ef-1234567890ab` example KMS key. The retiring principal is the `adminRole` role. The grant uses the `EncryptionContextSubset` grant constraint to allow this permission only when the encryption context in the `decrypt` request includes the `"Department": "IT"` key-value pair.

```
aws kms create-grant \
    --key-id 1234abcd-12ab-34cd-56ef-1234567890ab \
    --grantee-principal arn:aws:iam::123456789012:user/exampleUser \
    --operations Decrypt \
    --constraints EncryptionContextSubset={Department=IT} \
    --retiring-principal arn:aws:iam::123456789012:role/adminRole
```

Output:

```
{
    "GrantId": "1a2b3c4d2f5e69f440bae30eaec9570bb1fb7358824f9ddfa1aa5a0dab1a59b2",
    "GrantToken": "<grant token here>"
}
```

To view detailed information about the grant, use the `list-grants` command.

For more information, see [Grants in AWS KMS](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html) in the *AWS Key Management Service Developer Guide*.

## Output

GrantToken -> (string)

The grant token.

Use a grant token when your permission to call this operation comes from a new grant that has not yet achieved *eventual consistency* . For more information, see [Grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grants.html#grant_token) and [Using a grant token](https://docs.aws.amazon.com/kms/latest/developerguide/grant-manage.html#using-grant-token) in the *Key Management Service Developer Guide* .

GrantId -> (string)

The unique identifier for the grant.

You can use the `GrantId` in a  ListGrants ,  RetireGrant , or  RevokeGrant operation.