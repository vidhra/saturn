# check-no-public-accessÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/check-no-public-access.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/check-no-public-access.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [accessanalyzer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/accessanalyzer/index.html#cli-aws-accessanalyzer) ]

# check-no-public-access

## Description

Checks whether a resource policy can grant public access to the specified resource type.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/accessanalyzer-2019-11-01/CheckNoPublicAccess)

## Synopsis

```
check-no-public-access
--policy-document <value>
--resource-type <value>
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

`--policy-document` (string)

The JSON policy document to evaluate for public access.

`--resource-type` (string)

The type of resource to evaluate for public access. For example, to check for public access to Amazon S3 buckets, you can choose `AWS::S3::Bucket` for the resource type.

For resource types not supported as valid values, IAM Access Analyzer will return an error.

Possible values:

- `AWS::DynamoDB::Table`
- `AWS::DynamoDB::Stream`
- `AWS::EFS::FileSystem`
- `AWS::OpenSearchService::Domain`
- `AWS::Kinesis::Stream`
- `AWS::Kinesis::StreamConsumer`
- `AWS::KMS::Key`
- `AWS::Lambda::Function`
- `AWS::S3::Bucket`
- `AWS::S3::AccessPoint`
- `AWS::S3Express::DirectoryBucket`
- `AWS::S3::Glacier`
- `AWS::S3Outposts::Bucket`
- `AWS::S3Outposts::AccessPoint`
- `AWS::SecretsManager::Secret`
- `AWS::SNS::Topic`
- `AWS::SQS::Queue`
- `AWS::IAM::AssumeRolePolicyDocument`
- `AWS::S3Tables::TableBucket`
- `AWS::ApiGateway::RestApi`
- `AWS::CodeArtifact::Domain`
- `AWS::Backup::BackupVault`
- `AWS::CloudTrail::Dashboard`
- `AWS::CloudTrail::EventDataStore`
- `AWS::S3Tables::Table`
- `AWS::S3Express::AccessPoint`

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

**To check whether a resource policy can grant public access to the specified resource type**

The following `check-no-public-access` example checks whether a resource policy can grant public access to the specified resource type.

```
aws accessanalyzer check-no-public-access \
    --policy-document file://check-no-public-access-myfile.json \
    --resource-type AWS::S3::Bucket
```

Contents of `myfile.json`:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "CheckNoPublicAccess",
            "Effect": "Allow",
            "Principal": { "AWS": "arn:aws:iam::111122223333:user/JohnDoe" },
            "Action": [
                "s3:GetObject"
            ]
        }
    ]
}
```

Output:

```
{
    "result": "PASS",
    "message": "The resource policy does not grant public access for the given resource type."
}
```

For more information, see [Previewing access with IAM Access Analyzer APIs](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-preview-access-apis.html) in the *AWS IAM User Guide*.

## Output

result -> (string)

The result of the check for public access to the specified resource type. If the result is `PASS` , the policy doesnât allow public access to the specified resource type. If the result is `FAIL` , the policy might allow public access to the specified resource type.

message -> (string)

The message indicating whether the specified policy allows public access to resources.

reasons -> (list)

A list of reasons why the specified resource policy grants public access for the resource type.

(structure)

Contains information about the reasoning why a check for access passed or failed.

description -> (string)

A description of the reasoning of a result of checking for access.

statementIndex -> (integer)

The index number of the reason statement.

statementId -> (string)

The identifier for the reason statement.