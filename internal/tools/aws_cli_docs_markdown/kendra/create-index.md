# create-indexÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-index.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-index.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# create-index

## Description

Creates an Amazon Kendra index. Index creation is an asynchronous API. To determine if index creation has completed, check the `Status` field returned from a call to `DescribeIndex` . The `Status` field is set to `ACTIVE` when the index is ready to use.

Once the index is active, you can index your documents using the `BatchPutDocument` API or using one of the supported [data sources](https://docs.aws.amazon.com/kendra/latest/dg/data-sources.html) .

For an example of creating an index and data source using the Python SDK, see [Getting started with Python SDK](https://docs.aws.amazon.com/kendra/latest/dg/gs-python.html) . For an example of creating an index and data source using the Java SDK, see [Getting started with Java SDK](https://docs.aws.amazon.com/kendra/latest/dg/gs-java.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/CreateIndex)

## Synopsis

```
create-index
--name <value>
[--edition <value>]
--role-arn <value>
[--server-side-encryption-configuration <value>]
[--description <value>]
[--client-token <value>]
[--tags <value>]
[--user-token-configurations <value>]
[--user-context-policy <value>]
[--user-group-resolution-configuration <value>]
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

`--name` (string)

A name for the index.

`--edition` (string)

The Amazon Kendra edition to use for the index. Choose `DEVELOPER_EDITION` for indexes intended for development, testing, or proof of concept. Use `ENTERPRISE_EDITION` for production. Use `GEN_AI_ENTERPRISE_EDITION` for creating generative AI applications. Once you set the edition for an index, it canât be changed.

The `Edition` parameter is optional. If you donât supply a value, the default is `ENTERPRISE_EDITION` .

For more information on quota limits for Gen AI Enterprise Edition, Enterprise Edition, and Developer Edition indices, see [Quotas](https://docs.aws.amazon.com/kendra/latest/dg/quotas.html) .

Possible values:

- `DEVELOPER_EDITION`
- `ENTERPRISE_EDITION`
- `GEN_AI_ENTERPRISE_EDITION`

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role with permission to access your Amazon CloudWatch logs and metrics. For more information, see [IAM access roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

`--server-side-encryption-configuration` (structure)

The identifier of the KMS customer managed key (CMK) thatâs used to encrypt data indexed by Amazon Kendra. Amazon Kendra doesnât support asymmetric CMKs.

KmsKeyId -> (string)

The identifier of the KMS key. Amazon Kendra doesnât support asymmetric keys.

Shorthand Syntax:

```
KmsKeyId=string
```

JSON Syntax:

```
{
  "KmsKeyId": "string"
}
```

`--description` (string)

A description for the index.

`--client-token` (string)

A token that you provide to identify the request to create an index. Multiple calls to the `CreateIndex` API with the same client token will create only one index.

`--tags` (list)

A list of key-value pairs that identify or categorize the index. You can also use tags to help control access to the index. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

(structure)

A key-value pair that identifies or categorizes an index, FAQ, data source, or other resource. TA tag key and value can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

Key -> (string)

The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, data source, or other resource.

Value -> (string)

The value associated with the tag. The value may be an empty string but it canât be null.

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

`--user-token-configurations` (list)

The user token configuration.

### Warning

If youâre using an Amazon Kendra Gen AI Enterprise Edition index and you try to use `UserTokenConfigurations` to configure user context policy, Amazon Kendra returns a `ValidationException` error.

(structure)

Provides the configuration information for a token.

### Warning

If youâre using an Amazon Kendra Gen AI Enterprise Edition index and you try to use `UserTokenConfigurations` to configure user context policy, Amazon Kendra returns a `ValidationException` error.

JwtTokenTypeConfiguration -> (structure)

Information about the JWT token type configuration.

KeyLocation -> (string)

The location of the key.

URL -> (string)

The signing key URL.

SecretManagerArn -> (string)

The Amazon Resource Name (arn) of the secret.

UserNameAttributeField -> (string)

The user name attribute field.

GroupAttributeField -> (string)

The group attribute field.

Issuer -> (string)

The issuer of the token.

ClaimRegex -> (string)

The regular expression that identifies the claim.

JsonTokenTypeConfiguration -> (structure)

Information about the JSON token type configuration.

UserNameAttributeField -> (string)

The user name attribute field.

GroupAttributeField -> (string)

The group attribute field.

Shorthand Syntax:

```
JwtTokenTypeConfiguration={KeyLocation=string,URL=string,SecretManagerArn=string,UserNameAttributeField=string,GroupAttributeField=string,Issuer=string,ClaimRegex=string},JsonTokenTypeConfiguration={UserNameAttributeField=string,GroupAttributeField=string} ...
```

JSON Syntax:

```
[
  {
    "JwtTokenTypeConfiguration": {
      "KeyLocation": "URL"|"SECRET_MANAGER",
      "URL": "string",
      "SecretManagerArn": "string",
      "UserNameAttributeField": "string",
      "GroupAttributeField": "string",
      "Issuer": "string",
      "ClaimRegex": "string"
    },
    "JsonTokenTypeConfiguration": {
      "UserNameAttributeField": "string",
      "GroupAttributeField": "string"
    }
  }
  ...
]
```

`--user-context-policy` (string)

The user context policy.

### Warning

If youâre using an Amazon Kendra Gen AI Enterprise Edition index, you can only use `ATTRIBUTE_FILTER` to filter search results by user context. If youâre using an Amazon Kendra Gen AI Enterprise Edition index and you try to use `USER_TOKEN` to configure user context policy, Amazon Kendra returns a `ValidationException` error.

ATTRIBUTE_FILTER

All indexed content is searchable and displayable for all users. If you want to filter search results on user context, you can use the attribute filters of `_user_id` and `_group_ids` or you can provide user and group information in `UserContext` .

USER_TOKEN

Enables token-based user access control to filter search results on user context. All documents with no access control and all documents accessible to the user will be searchable and displayable.

Possible values:

- `ATTRIBUTE_FILTER`
- `USER_TOKEN`

`--user-group-resolution-configuration` (structure)

Gets users and groups from IAM Identity Center identity source. To configure this, see [UserGroupResolutionConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_UserGroupResolutionConfiguration.html) . This is useful for user context filtering, where search results are filtered based on the user or their group access to documents.

### Warning

If youâre using an Amazon Kendra Gen AI Enterprise Edition index, `UserGroupResolutionConfiguration` isnât supported.

UserGroupResolutionMode -> (string)

The identity store provider (mode) you want to use to get users and groups. IAM Identity Center is currently the only available mode. Your users and groups must exist in an IAM Identity Center identity source in order to use this mode.

Shorthand Syntax:

```
UserGroupResolutionMode=string
```

JSON Syntax:

```
{
  "UserGroupResolutionMode": "AWS_SSO"|"NONE"
}
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

**To create an Amazon Kendra index**

The following `create-index` creates and configures an Amazon Kendra index. You can use `describe-index` to view the status of an index, and read any error messages if the status shows an index âFAILEDâ to completely create.

```
aws kendra create-index \
    --name "example index 1" \
    --description "Example index 1 contains the first set of example documents" \
    --tags '{"Key": "test resources", "Value": "kendra"}, {"Key": "test resources", "Value": "aws"}' \
    --role-arn "arn:aws:iam::my-account-id:role/KendraRoleForExampleIndex" \
    --edition "DEVELOPER_EDITION" \
    --server-side-encryption-configuration '{"KmsKeyId": "my-kms-key-id"}' \
    --user-context-policy "USER_TOKEN" \
    --user-token-configurations '{"JsonTokenTypeConfiguration": {"GroupAttributeField": "groupNameField", "UserNameAttributeField": "userNameField"}}'
```

Output:

```
{
   "Id": index1
}
```

For more information, see [Getting started with an Amazon Kendra index and data source connector](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html) in the *Amazon Kendra Developer Guide*.

## Output

Id -> (string)

The identifier of the index. Use this identifier when you query an index, set up a data source, or index a document.