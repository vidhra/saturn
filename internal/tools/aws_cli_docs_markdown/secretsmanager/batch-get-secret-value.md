# batch-get-secret-valueÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/batch-get-secret-value.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/batch-get-secret-value.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [secretsmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/secretsmanager/index.html#cli-aws-secretsmanager) ]

# batch-get-secret-value

## Description

Retrieves the contents of the encrypted fields `SecretString` or `SecretBinary` for up to 20 secrets. To retrieve a single secret, call  GetSecretValue .

To choose which secrets to retrieve, you can specify a list of secrets by name or ARN, or you can use filters. If Secrets Manager encounters errors such as `AccessDeniedException` while attempting to retrieve any of the secrets, you can see the errors in `Errors` in the response.

Secrets Manager generates CloudTrail `GetSecretValue` log entries for each secret you request when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html) .

**Required permissions:** `secretsmanager:BatchGetSecretValue` , and you must have `secretsmanager:GetSecretValue` for each secret. If you use filters, you must also have `secretsmanager:ListSecrets` . If the secrets are encrypted using customer-managed keys instead of the Amazon Web Services managed key `aws/secretsmanager` , then you also need `kms:Decrypt` permissions for the keys. For more information, see [IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/secretsmanager-2017-10-17/BatchGetSecretValue)

## Synopsis

```
batch-get-secret-value
[--secret-id-list <value>]
[--filters <value>]
[--max-results <value>]
[--next-token <value>]
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

`--secret-id-list` (list)

The ARN or names of the secrets to retrieve. You must include `Filters` or `SecretIdList` , but not both.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

The filters to choose which secrets to retrieve. You must include `Filters` or `SecretIdList` , but not both.

(structure)

Allows you to add filters when you use the search function in Secrets Manager. For more information, see [Find secrets in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html) .

Key -> (string)

The following are keys you can use:

- **description** : Prefix match, not case-sensitive.
- **name** : Prefix match, case-sensitive.
- **tag-key** : Prefix match, case-sensitive.
- **tag-value** : Prefix match, case-sensitive.
- **primary-region** : Prefix match, case-sensitive.
- **owning-service** : Prefix match, case-sensitive.
- **all** : Breaks the filter value string into words and then searches all attributes for matches. Not case-sensitive.

Values -> (list)

The keyword to filter for.

You can prefix your search value with an exclamation mark (`!` ) in order to perform negation filters.

(string)

Shorthand Syntax:

```
Key=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Key": "description"|"name"|"tag-key"|"tag-value"|"primary-region"|"owning-service"|"all",
    "Values": ["string", ...]
  }
  ...
]
```

`--max-results` (integer)

The number of results to include in the response.

If there are more results available, in the response, Secrets Manager includes `NextToken` . To get the next results, call `BatchGetSecretValue` again with the value from `NextToken` . To use this parameter, you must also use the `Filters` parameter.

`--next-token` (string)

A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call `BatchGetSecretValue` again with this value.

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

**Example 1: To retrieve the secret value for a group of secrets listed by name**

The following `batch-get-secret-value` example gets the secret value secrets for three secrets.

```
aws secretsmanager batch-get-secret-value \
    --secret-id-list MySecret1 MySecret2 MySecret3
```

Output:

```
{
    "SecretValues": [
        {
            "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret1-a1b2c3",
            "Name": "MySecret1",
            "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
            "SecretString": "{\"username\":\"diego_ramirez\",\"password\":\"EXAMPLE-PASSWORD\",\"engine\":\"mysql\",\"host\":\"secretsmanagertutorial.cluster.us-west-2.rds.amazonaws.com\",\"port\":3306,\"dbClusterIdentifier\":\"secretsmanagertutorial\"}",
            "VersionStages": [
                "AWSCURRENT"
            ],
            "CreatedDate": "1523477145.729"
        },
        {
            "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret2-a1b2c3",
            "Name": "MySecret2",
            "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
            "SecretString": "{\"username\":\"akua_mansa\",\"password\":\"EXAMPLE-PASSWORD\"",
            "VersionStages": [
                "AWSCURRENT"
            ],
            "CreatedDate": "1673477781.275"
        },
        {
            "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret3-a1b2c3",
            "Name": "MySecret3",
            "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEccccc",
            "SecretString": "{\"username\":\"jie_liu\",\"password\":\"EXAMPLE-PASSWORD\"",
            "VersionStages": [
                "AWSCURRENT"
            ],
            "CreatedDate": "1373477721.124"
        }
    ],
    "Errors": []
}
```

For more information, see [Retrieve a group of secrets in a batch](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_batch.html) in the *AWS Secrets Manager User Guide*.

**Example 2: To retrieve the secret value for a group of secrets selected by filter**

The following `batch-get-secret-value` example gets the secret value secrets in your account that have `MySecret` in the name. Filtering by name is case sensitive.

```
aws secretsmanager batch-get-secret-value \
    --filters Key="name",Values="MySecret"
```

Output:

```
{
    "SecretValues": [
        {
            "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret1-a1b2c3",
            "Name": "MySecret1",
            "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
            "SecretString": "{\"username\":\"diego_ramirez\",\"password\":\"EXAMPLE-PASSWORD\",\"engine\":\"mysql\",\"host\":\"secretsmanagertutorial.cluster.us-west-2.rds.amazonaws.com\",\"port\":3306,\"dbClusterIdentifier\":\"secretsmanagertutorial\"}",
            "VersionStages": [
                "AWSCURRENT"
            ],
            "CreatedDate": "1523477145.729"
        },
        {
            "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret2-a1b2c3",
            "Name": "MySecret2",
            "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
            "SecretString": "{\"username\":\"akua_mansa\",\"password\":\"EXAMPLE-PASSWORD\"",
            "VersionStages": [
                "AWSCURRENT"
            ],
            "CreatedDate": "1673477781.275"
        },
        {
            "ARN": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret3-a1b2c3",
            "Name": "MySecret3",
            "VersionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLEccccc",
            "SecretString": "{\"username\":\"jie_liu\",\"password\":\"EXAMPLE-PASSWORD\"",
            "VersionStages": [
                "AWSCURRENT"
            ],
            "CreatedDate": "1373477721.124"
        }
    ],
    "Errors": []
}
```

For more information, see [Retrieve a group of secrets in a batch](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieving-secrets_batch.html) in the *AWS Secrets Manager User Guide*.

## Output

SecretValues -> (list)

A list of secret values.

(structure)

A structure that contains the secret value and other details for a secret.

ARN -> (string)

The Amazon Resource Name (ARN) of the secret.

Name -> (string)

The friendly name of the secret.

VersionId -> (string)

The unique version identifier of this version of the secret.

SecretBinary -> (blob)

The decrypted secret value, if the secret value was originally provided as binary data in the form of a byte array. The parameter represents the binary data as a [base64-encoded](https://tools.ietf.org/html/rfc4648#section-4) string.

SecretString -> (string)

The decrypted secret value, if the secret value was originally provided as a string or through the Secrets Manager console.

VersionStages -> (list)

A list of all of the staging labels currently attached to this version of the secret.

(string)

CreatedDate -> (timestamp)

The date the secret was created.

NextToken -> (string)

Secrets Manager includes this value if thereâs more output available than what is included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a long list. To get the next results, call `BatchGetSecretValue` again with this value.

Errors -> (list)

A list of errors Secrets Manager encountered while attempting to retrieve individual secrets.

(structure)

The error Secrets Manager encountered while retrieving an individual secret as part of  BatchGetSecretValue .

SecretId -> (string)

The ARN or name of the secret.

ErrorCode -> (string)

The error Secrets Manager encountered while retrieving an individual secret as part of  BatchGetSecretValue , for example `ResourceNotFoundException` ,``InvalidParameterException`` , `InvalidRequestException` , `DecryptionFailure` , or `AccessDeniedException` .

Message -> (string)

A message describing the error.