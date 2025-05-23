# create-secretÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/create-secret.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [secretsmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/index.html#cli-aws-secretsmanager) ]

# create-secret

## Description

Creates a new secret. A *secret* can be a password, a set of credentials such as a user name and password, an OAuth token, or other secret information that you store in an encrypted form in Secrets Manager. The secret also includes the connection information to access a database or other service, which Secrets Manager doesnât encrypt. A secret in Secrets Manager consists of both the protected secret data and the important information needed to manage the secret.

For secrets that use *managed rotation* , you need to create the secret through the managing service. For more information, see [Secrets Manager secrets managed by other Amazon Web Services services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html) .

For information about creating a secret in the console, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html) .

To create a secret, you can provide the secret value to be encrypted in either the `SecretString` parameter or the `SecretBinary` parameter, but not both. If you include `SecretString` or `SecretBinary` then Secrets Manager creates an initial secret version and automatically attaches the staging label `AWSCURRENT` to it.

For database credentials you want to rotate, for Secrets Manager to be able to rotate the secret, you must make sure the JSON you store in the `SecretString` matches the [JSON structure of a database secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_secret_json_structure.html) .

If you donât specify an KMS encryption key, Secrets Manager uses the Amazon Web Services managed key `aws/secretsmanager` . If this key doesnât already exist in your account, then Secrets Manager creates it for you automatically. All users and roles in the Amazon Web Services account automatically have access to use `aws/secretsmanager` . Creating `aws/secretsmanager` can result in a one-time significant delay in returning the result.

If the secret is in a different Amazon Web Services account from the credentials calling the API, then you canât use `aws/secretsmanager` to encrypt the secret, and you must create and use a customer managed KMS key.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters except `SecretBinary` or `SecretString` because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html) .

**Required permissions:** `secretsmanager:CreateSecret` . If you include tags in the secret, you also need `secretsmanager:TagResource` . To add replica Regions, you must also have `secretsmanager:ReplicateSecretToRegions` . For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html) .

To encrypt the secret with a KMS key other than `aws/secretsmanager` , you need `kms:GenerateDataKey` and `kms:Decrypt` permission to the key.

### Warning

When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. This is a concern if the command includes the value of a secret. Learn how to [Mitigate the risks of using command-line tools to store Secrets Manager secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security_cli-exposure-risks.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/CreateSecret)

## Synopsis

```
create-secret
--name <value>
[--client-request-token <value>]
[--description <value>]
[--kms-key-id <value>]
[--secret-binary <value>]
[--secret-string <value>]
[--tags <value>]
[--add-replica-regions <value>]
[--force-overwrite-replica-secret | --no-force-overwrite-replica-secret]
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

The name of the new secret.

The secret name can contain ASCII letters, numbers, and the following characters: /_+=.@-

Do not end your secret name with a hyphen followed by six characters. If you do so, you risk confusion and unexpected results when searching for a secret by partial ARN. Secrets Manager automatically adds a hyphen and six random characters after the secret name at the end of the ARN.

`--client-request-token` (string)

If you include `SecretString` or `SecretBinary` , then Secrets Manager creates an initial version for the secret, and this parameter specifies the unique identifier for the new version.

### Note

If you use the Amazon Web Services CLI or one of the Amazon Web Services SDKs to call this operation, then you can leave this parameter empty. The CLI or SDK generates a random UUID for you and includes it as the value for this parameter in the request.

If you generate a raw HTTP request to the Secrets Manager service endpoint, then you must generate a `ClientRequestToken` and include it in the request.

This value helps ensure idempotency. Secrets Manager uses this value to prevent the accidental creation of duplicate versions if there are failures and retries during a rotation. We recommend that you generate a [UUID-type](https://wikipedia.org/wiki/Universally_unique_identifier) value to ensure uniqueness of your versions within the specified secret.

- If the `ClientRequestToken` value isnât already associated with a version of the secret then a new version of the secret is created.
- If a version with this value already exists and the version `SecretString` and `SecretBinary` values are the same as those in the request, then the request is ignored.
- If a version with this value already exists and that versionâs `SecretString` and `SecretBinary` values are different from those in the request, then the request fails because you cannot modify an existing version. Instead, use  PutSecretValue to create a new version.

This value becomes the `VersionId` of the new version.

`--description` (string)

The description of the secret.

`--kms-key-id` (string)

The ARN, key ID, or alias of the KMS key that Secrets Manager uses to encrypt the secret value in the secret. An alias is always prefixed by `alias/` , for example `alias/aws/secretsmanager` . For more information, see [About aliases](https://docs.aws.amazon.com/kms/latest/developerguide/alias-about.html) .

To use a KMS key in a different account, use the key ARN or the alias ARN.

If you donât specify this value, then Secrets Manager uses the key `aws/secretsmanager` . If that key doesnât yet exist, then Secrets Manager creates it for you automatically the first time it encrypts the secret value.

If the secret is in a different Amazon Web Services account from the credentials calling the API, then you canât use `aws/secretsmanager` to encrypt the secret, and you must create and use a customer managed KMS key.

`--secret-binary` (blob)

The binary data to encrypt and store in the new version of the secret. We recommend that you store your binary data in a file and then pass the contents of the file as a parameter.

Either `SecretString` or `SecretBinary` must have a value, but not both.

This parameter is not available in the Secrets Manager console.

Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.

`--secret-string` (string)

The text data to encrypt and store in this new version of the secret. We recommend you use a JSON structure of key/value pairs for your secret value.

Either `SecretString` or `SecretBinary` must have a value, but not both.

If you create a secret by using the Secrets Manager console then Secrets Manager puts the protected secret text in only the `SecretString` parameter. The Secrets Manager console stores the information as a JSON structure of key/value pairs that a Lambda rotation function can parse.

Sensitive: This field contains sensitive information, so the service does not include it in CloudTrail log entries. If you create your own log entries, you must also avoid logging the information in this field.

`--tags` (list)

A list of tags to attach to the secret. Each tag is a key and value pair of strings in a JSON text string, for example:

`[{"Key":"CostCenter","Value":"12345"},{"Key":"environment","Value":"production"}]`

Secrets Manager tag key names are case sensitive. A tag with the key âABCâ is a different tag from one with key âabcâ.

If you check tags in permissions policies as part of your security strategy, then adding or removing a tag can change permissions. If the completion of this operation would result in you losing your permissions for this secret, then Secrets Manager blocks the operation and returns an `Access Denied` error. For more information, see [Control access to secrets using tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#tag-secrets-abac) and [Limit access to identities with tags that match secretsâ tags](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html#auth-and-access_tags2) .

For information about how to format a JSON parameter for the various command line tool environments, see [Using JSON for Parameters](https://docs.aws.amazon.com/cli/latest/userguide/cli-using-param.html#cli-using-param-json) . If your command-line tool or SDK requires quotation marks around the parameter, you should use single quotes to avoid confusion with the double quotes required in the JSON text.

For tag quotas and naming restrictions, see [Service quotas for Tagging](https://docs.aws.amazon.com/general/latest/gr/arg.html#taged-reference-quotas) in the *Amazon Web Services General Reference guide* .

(structure)

A structure that contains information about a tag.

Key -> (string)

The key identifier, or name, of the tag.

Value -> (string)

The string value associated with the key of the tag.

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

`--add-replica-regions` (list)

A list of Regions and KMS keys to replicate secrets.

(structure)

A custom type that specifies a `Region` and the `KmsKeyId` for a replica secret.

Region -> (string)

A Region code. For a list of Region codes, see [Name and code of Regions](https://docs.aws.amazon.com/general/latest/gr/rande.html#regional-endpoints) .

KmsKeyId -> (string)

The ARN, key ID, or alias of the KMS key to encrypt the secret. If you donât include this field, Secrets Manager uses `aws/secretsmanager` .

Shorthand Syntax:

```
Region=string,KmsKeyId=string ...
```

JSON Syntax:

```
[
  {
    "Region": "string",
    "KmsKeyId": "string"
  }
  ...
]
```

`--force-overwrite-replica-secret` | `--no-force-overwrite-replica-secret` (boolean)

Specifies whether to overwrite a secret with the same name in the destination Region. By default, secrets arenât overwritten.

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

**Example 1: To create a secret from credentials in a JSON file**

The following `create-secret` example creates a secret from credentials in a file. For more information, see [Loading AWS CLI parameters from a file](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-file.html) in the *AWS CLI User Guide*.

```
aws secretsmanager create-secret \
    --name MyTestSecret \
    --secret-string file://mycreds.json
```

Contents of `mycreds.json`:

```
{
  "engine": "mysql",
  "username": "saanvis",
  "password": "EXAMPLE-PASSWORD",
  "host": "my-database-endpoint.us-west-2.rds.amazonaws.com",
  "dbname": "myDatabase",
  "port": "3306"
}
```

Output:

```
{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3",
  "Name": "MyTestSecret",
  "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

For more information, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html) in the *Secrets Manager User Guide*.

**Example 2: To create a secret**

The following `create-secret` example creates a secret with two key-value pairs. When you enter commands in a command shell, there is a risk of the command history being accessed or utilities having access to your command parameters. This is a concern if the command includes the value of a secret. For more information, see [Mitigate the risks of using command-line tools to store secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/security_cli-exposure-risks.html) in the *Secrets Manager User Guide*.

```
aws secretsmanager create-secret \
    --name MyTestSecret \
    --description "My test secret created with the CLI." \
    --secret-string "{\"user\":\"diegor\",\"password\":\"EXAMPLE-PASSWORD\"}"
```

Output:

```
{
  "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestSecret-a1b2c3",
  "Name": "MyTestSecret",
  "VersionId": "EXAMPLE1-90ab-cdef-fedc-ba987EXAMPLE"
}
```

For more information, see [Create a secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_create-basic-secret.html) in the *Secrets Manager User Guide*.

## Output

ARN -> (string)

The ARN of the new secret. The ARN includes the name of the secret followed by six random characters. This ensures that if you create a new secret with the same name as a deleted secret, then users with access to the old secret donât get access to the new secret because the ARNs are different.

Name -> (string)

The name of the new secret.

VersionId -> (string)

The unique identifier associated with the version of the new secret.

ReplicationStatus -> (list)

A list of the replicas of this secret and their status:

- `Failed` , which indicates that the replica was not created.
- `InProgress` , which indicates that Secrets Manager is in the process of creating the replica.
- `InSync` , which indicates that the replica was created.

(structure)

A replication object consisting of a `RegionReplicationStatus` object and includes a Region, KMSKeyId, status, and status message.

Region -> (string)

The Region where replication occurs.

KmsKeyId -> (string)

Can be an `ARN` , `Key ID` , or `Alias` .

Status -> (string)

The status can be `InProgress` , `Failed` , or `InSync` .

StatusMessage -> (string)

Status message such as â*Secret with this name already exists in this region* â.

LastAccessedDate -> (timestamp)

The date that the secret was last accessed in the Region. This field is omitted if the secret has never been retrieved in the Region.