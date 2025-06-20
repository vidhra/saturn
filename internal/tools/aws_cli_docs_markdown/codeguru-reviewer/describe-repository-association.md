# describe-repository-associationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-repository-association.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/describe-repository-association.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeguru-reviewer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguru-reviewer/index.html#cli-aws-codeguru-reviewer) ]

# describe-repository-association

## Description

Returns a [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) object that contains information about the requested repository association.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeguru-reviewer-2019-09-19/DescribeRepositoryAssociation)

## Synopsis

```
describe-repository-association
--association-arn <value>
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

`--association-arn` (string)

The Amazon Resource Name (ARN) of the [RepositoryAssociation](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) object. You can retrieve this ARN by calling [ListRepositoryAssociations](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_ListRepositoryAssociations.html) .

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

**Example 1: To return information about a GitHub repository association**

The following `describe-repository-association` example returns information about a repository association that uses a GitHub Enterprise repository and is in the `Associated` state.

```
aws codeguru-reviewer describe-repository-association \
    --association-arn arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

Output:

```
{
    "RepositoryAssociation": {
        "AssociationId": "b822717e-0711-4e8a-bada-0e738289c75e",
        "Name": "mySampleRepo",
        "LastUpdatedTimeStamp": 1588102637.649,
        "ProviderType": "GitHub",
        "CreatedTimeStamp": 1588102615.636,
        "Owner": "sample-owner",
        "State": "Associated",
        "StateReason": "Pull Request Notification configuration successful",
        "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
    }
}
```

For more information, see [Create a GitHub Enterprise Server repository association in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-github-enterprise-association.html) in the *Amazon CodeGuru Reviewer User Guide*.

**Example 2: To return information about a failed repository association**

The following `describe-repository-association` example returns information about a repository association that uses a GitHub Enterprise repository and is in the `Failed` state.

```
aws codeguru-reviewer describe-repository-association \
    --association-arn arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

Output:

```
{
    "RepositoryAssociation": {
        "ProviderType": "GitHubEnterpriseServer",
        "Name": "mySampleRepo",
        "LastUpdatedTimeStamp": 1596217036.892,
        "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "CreatedTimeStamp": 1596216896.979,
        "ConnectionArn": "arn:aws:codestar-connections:us-west-2:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "State": "Failed",
        "StateReason": "Failed, Please retry.",
        "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
        "Owner": "sample-owner"
    }
}
```

For more information, see [Create a GitHub Enterprise Server repository association in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-github-enterprise-association.html) in the *Amazon CodeGuru Reviewer User Guide*.

**Example 3: To return information about a disassociating repository association**

The following `describe-repository-association` example returns information about a repository association that uses a GitHub Enterprise repository and is in the `Disassociating` state.

```
aws codeguru-reviewer describe-repository-association \
    --association-arn arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

Output:

```
{
    "RepositoryAssociation": {
        "ProviderType": "GitHubEnterpriseServer",
        "Name": "mySampleRepo",
        "LastUpdatedTimeStamp": 1596217036.892,
        "AssociationId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "CreatedTimeStamp": 1596216896.979,
        "ConnectionArn": "arn:aws:codestar-connections:us-west-2:123456789012:connection/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "State": "Disassociating",
        "StateReason": "Source code access removal in progress",
        "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:a1b2c3d4-5678-90ab-cdef-EXAMPLE33333",
        "Owner": "sample-owner"
    }
}
```

For more information, see [Create a GitHub Enterprise Server repository association in Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/create-github-enterprise-association.html) in the *Amazon CodeGuru Reviewer User Guide*.

## Output

RepositoryAssociation -> (structure)

Information about the repository association.

AssociationId -> (string)

The ID of the repository association.

AssociationArn -> (string)

The Amazon Resource Name (ARN) identifying the repository association.

ConnectionArn -> (string)

The Amazon Resource Name (ARN) of an Amazon Web Services CodeStar Connections connection. Its format is `arn:aws:codestar-connections:region-id:aws-account_id:connection/connection-id` . For more information, see [Connection](https://docs.aws.amazon.com/codestar-connections/latest/APIReference/API_Connection.html) in the *Amazon Web Services CodeStar Connections API Reference* .

Name -> (string)

The name of the repository.

Owner -> (string)

The owner of the repository. For an Amazon Web Services CodeCommit repository, this is the Amazon Web Services account ID of the account that owns the repository. For a GitHub, GitHub Enterprise Server, or Bitbucket repository, this is the username for the account that owns the repository. For an S3 repository, it can be the username or Amazon Web Services account ID.

ProviderType -> (string)

The provider type of the repository association.

State -> (string)

The state of the repository association.

The valid repository association states are:

- **Associated** : The repository association is complete.
- **Associating** : CodeGuru Reviewer is:

- Setting up pull request notifications. This is required for pull requests to trigger a CodeGuru Reviewer review.

### Note

If your repository `ProviderType` is `GitHub` , `GitHub Enterprise Server` , or `Bitbucket` , CodeGuru Reviewer creates webhooks in your repository to trigger CodeGuru Reviewer reviews. If you delete these webhooks, reviews of code in your repository cannot be triggered.

- Setting up source code access. This is required for CodeGuru Reviewer to securely clone code in your repository.
- **Failed** : The repository failed to associate or disassociate.
- **Disassociating** : CodeGuru Reviewer is removing the repositoryâs pull request notifications and source code access.
- **Disassociated** : CodeGuru Reviewer successfully disassociated the repository. You can create a new association with this repository if you want to review source code in it later. You can control access to code reviews created in anassociated repository with tags after it has been disassociated. For more information, see [Using tags to control access to associated repositories](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/auth-and-access-control-using-tags.html) in the *Amazon CodeGuru Reviewer User Guide* .

StateReason -> (string)

A description of why the repository association is in the current state.

LastUpdatedTimeStamp -> (timestamp)

The time, in milliseconds since the epoch, when the repository association was last updated.

CreatedTimeStamp -> (timestamp)

The time, in milliseconds since the epoch, when the repository association was created.

KMSKeyDetails -> (structure)

A `KMSKeyDetails` object that contains:

- The encryption option for this repository association. It is either owned by Amazon Web Services Key Management Service (KMS) (`AWS_OWNED_CMK` ) or customer managed (`CUSTOMER_MANAGED_CMK` ).
- The ID of the Amazon Web Services KMS key that is associated with this repository association.

KMSKeyId -> (string)

The ID of the Amazon Web Services KMS key that is associated with a repository association.

EncryptionOption -> (string)

The encryption option for a repository association. It is either owned by Amazon Web Services Key Management Service (KMS) (`AWS_OWNED_CMK` ) or customer managed (`CUSTOMER_MANAGED_CMK` ).

S3RepositoryDetails -> (structure)

Specifies the name of an S3 bucket and a `CodeArtifacts` object that contains the S3 object keys for a source code .zip file and for a build artifacts .zip file that contains .jar or .class files.

BucketName -> (string)

The name of the S3 bucket used for associating a new S3 repository. It must begin with `codeguru-reviewer-` .

CodeArtifacts -> (structure)

A `CodeArtifacts` object. The `CodeArtifacts` object includes the S3 object key for a source code .zip file and for a build artifacts .zip file that contains .jar or .class files.

SourceCodeArtifactsObjectKey -> (string)

The S3 object key for a source code .zip file. This is required for all code reviews.

BuildArtifactsObjectKey -> (string)

The S3 object key for a build artifacts .zip file that contains .jar or .class files. This is required for a code review with security analysis. For more information, see [Create code reviews with GitHub Actions](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/working-with-cicd.html) in the *Amazon CodeGuru Reviewer User Guide* .

Tags -> (map)

An array of key-value pairs used to tag an associated repository. A tag is a custom attribute label with two parts:

- A *tag key* (for example, `CostCenter` , `Environment` , `Project` , or `Secret` ). Tag keys are case sensitive.
- An optional field known as a *tag value* (for example, `111122223333` , `Production` , or a team name). Omitting the tag value is the same as using an empty string. Like tag keys, tag values are case sensitive.

key -> (string)

value -> (string)