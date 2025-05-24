# update-application-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-application-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/update-application-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# update-application-version

## Description

Updates the specified application version to have the specified properties.

### Note

If a property (for example, `description` ) is not provided, the value remains unchanged. To clear properties, specify an empty string.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)

## Synopsis

```
update-application-version
--application-name <value>
--version-label <value>
[--description <value>]
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

`--application-name` (string)

The name of the application associated with this version.

If no application is found with this name, `UpdateApplication` returns an `InvalidParameterValue` error.

`--version-label` (string)

The name of the version to update.

If no application version is found with this label, `UpdateApplication` returns an `InvalidParameterValue` error.

`--description` (string)

A new description for this version.

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

**To change an application versionâs description**

The following command updates the description of an application version named `22a0-stage-150819_185942`:

```
aws elasticbeanstalk update-application-version --version-label 22a0-stage-150819_185942 --application-name my-app --description "new description"
```

Output:

```
{
    "ApplicationVersion": {
        "ApplicationName": "my-app",
        "VersionLabel": "22a0-stage-150819_185942",
        "Description": "new description",
        "DateCreated": "2015-08-19T18:59:17.646Z",
        "DateUpdated": "2015-08-20T22:53:28.871Z",
        "SourceBundle": {
            "S3Bucket": "elasticbeanstalk-us-west-2-0123456789012",
            "S3Key": "my-app/22a0-stage-150819_185942.war"
        }
    }
}
```

## Output

ApplicationVersion -> (structure)

The  ApplicationVersionDescription of the application version.

ApplicationVersionArn -> (string)

The Amazon Resource Name (ARN) of the application version.

ApplicationName -> (string)

The name of the application to which the application version belongs.

Description -> (string)

The description of the application version.

VersionLabel -> (string)

A unique identifier for the application version.

SourceBuildInformation -> (structure)

If the versionâs source code was retrieved from AWS CodeCommit, the location of the source code for the application version.

SourceType -> (string)

The type of repository.

- `Git`
- `Zip`

SourceRepository -> (string)

Location where the repository is stored.

- `CodeCommit`
- `S3`

SourceLocation -> (string)

The location of the source code, as a formatted string, depending on the value of `SourceRepository`

- For `CodeCommit` , the format is the repository name and commit ID, separated by a forward slash. For example, `my-git-repo/265cfa0cf6af46153527f55d6503ec030551f57a` .
- For `S3` , the format is the S3 bucket name and object key, separated by a forward slash. For example, `my-s3-bucket/Folders/my-source-file` .

BuildArn -> (string)

Reference to the artifact from the AWS CodeBuild build.

SourceBundle -> (structure)

The storage location of the application versionâs source bundle in Amazon S3.

S3Bucket -> (string)

The Amazon S3 bucket where the data is located.

S3Key -> (string)

The Amazon S3 key where the data is located.

DateCreated -> (timestamp)

The creation date of the application version.

DateUpdated -> (timestamp)

The last modified date of the application version.

Status -> (string)

The processing status of the application version. Reflects the state of the application version during its creation. Many of the values are only applicable if you specified `True` for the `Process` parameter of the `CreateApplicationVersion` action. The following list describes the possible values.

- `Unprocessed` â Application version wasnât pre-processed or validated. Elastic Beanstalk will validate configuration files during deployment of the application version to an environment.
- `Processing` â Elastic Beanstalk is currently processing the application version.
- `Building` â Application version is currently undergoing an AWS CodeBuild build.
- `Processed` â Elastic Beanstalk was successfully pre-processed and validated.
- `Failed` â Either the AWS CodeBuild build failed or configuration files didnât pass validation. This application version isnât usable.