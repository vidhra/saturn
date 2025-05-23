# create-application-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-application-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/create-application-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elasticbeanstalk](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elasticbeanstalk/index.html#cli-aws-elasticbeanstalk) ]

# create-application-version

## Description

Creates an application version for the specified application. You can create an application version from a source bundle in Amazon S3, a commit in AWS CodeCommit, or the output of an AWS CodeBuild build as follows:

Specify a commit in an AWS CodeCommit repository with `SourceBuildInformation` .

Specify a build in an AWS CodeBuild with `SourceBuildInformation` and `BuildConfiguration` .

Specify a source bundle in S3 with `SourceBundle`

Omit both `SourceBuildInformation` and `SourceBundle` to use the default sample application.

### Note

After you create an application version with a specified Amazon S3 bucket and key location, you canât change that Amazon S3 location. If you change the Amazon S3 location, you receive an exception when you attempt to launch an environment from the application version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticbeanstalk-2010-12-01/CreateApplicationVersion)

## Synopsis

```
create-application-version
--application-name <value>
--version-label <value>
[--description <value>]
[--source-build-information <value>]
[--source-bundle <value>]
[--build-configuration <value>]
[--auto-create-application | --no-auto-create-application]
[--process | --no-process]
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

`--application-name` (string)

The name of the application. If no application is found with this name, and `AutoCreateApplication` is `false` , returns an `InvalidParameterValue` error.

`--version-label` (string)

A label identifying this version.

Constraint: Must be unique per application. If an application version already exists with this label for the specified application, AWS Elastic Beanstalk returns an `InvalidParameterValue` error.

`--description` (string)

A description of this application version.

`--source-build-information` (structure)

Specify a commit in an AWS CodeCommit Git repository to use as the source code for the application version.

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

Shorthand Syntax:

```
SourceType=string,SourceRepository=string,SourceLocation=string
```

JSON Syntax:

```
{
  "SourceType": "Git"|"Zip",
  "SourceRepository": "CodeCommit"|"S3",
  "SourceLocation": "string"
}
```

`--source-bundle` (structure)

The Amazon S3 bucket and key that identify the location of the source bundle for this version.

### Note

The Amazon S3 bucket must be in the same region as the environment.

Specify a source bundle in S3 or a commit in an AWS CodeCommit repository (with `SourceBuildInformation` ), but not both. If neither `SourceBundle` nor `SourceBuildInformation` are provided, Elastic Beanstalk uses a sample application.

S3Bucket -> (string)

The Amazon S3 bucket where the data is located.

S3Key -> (string)

The Amazon S3 key where the data is located.

Shorthand Syntax:

```
S3Bucket=string,S3Key=string
```

JSON Syntax:

```
{
  "S3Bucket": "string",
  "S3Key": "string"
}
```

`--build-configuration` (structure)

Settings for an AWS CodeBuild build.

ArtifactName -> (string)

The name of the artifact of the CodeBuild build. If provided, Elastic Beanstalk stores the build artifact in the S3 location *S3-bucket* /resources/*application-name* /codebuild/codebuild-*version-label* -*artifact-name* .zip. If not provided, Elastic Beanstalk stores the build artifact in the S3 location *S3-bucket* /resources/*application-name* /codebuild/codebuild-*version-label* .zip.

CodeBuildServiceRole -> (string)

The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS services on behalf of the AWS account.

ComputeType -> (string)

Information about the compute resources the build project will use.

- `BUILD_GENERAL1_SMALL: Use up to 3 GB memory and 2 vCPUs for builds`
- `BUILD_GENERAL1_MEDIUM: Use up to 7 GB memory and 4 vCPUs for builds`
- `BUILD_GENERAL1_LARGE: Use up to 15 GB memory and 8 vCPUs for builds`

Image -> (string)

The ID of the Docker image to use for this build project.

TimeoutInMinutes -> (integer)

How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.

Shorthand Syntax:

```
ArtifactName=string,CodeBuildServiceRole=string,ComputeType=string,Image=string,TimeoutInMinutes=integer
```

JSON Syntax:

```
{
  "ArtifactName": "string",
  "CodeBuildServiceRole": "string",
  "ComputeType": "BUILD_GENERAL1_SMALL"|"BUILD_GENERAL1_MEDIUM"|"BUILD_GENERAL1_LARGE",
  "Image": "string",
  "TimeoutInMinutes": integer
}
```

`--auto-create-application` | `--no-auto-create-application` (boolean)

Set to `true` to create an application with the specified name if it doesnât already exist.

`--process` | `--no-process` (boolean)

Pre-processes and validates the environment manifest (`env.yaml` ) and configuration files (`*.config` files in the `.ebextensions` folder) in the source bundle. Validating configuration files can identify issues prior to deploying the application version to an environment.

You must turn processing on for application versions that you create using AWS CodeBuild or AWS CodeCommit. For application versions built from a source bundle in Amazon S3, processing is optional.

### Note

The `Process` option validates Elastic Beanstalk configuration files. It doesnât validate your applicationâs configuration files, like proxy server or Docker configuration.

`--tags` (list)

Specifies the tags applied to the application version.

Elastic Beanstalk applies these tags only to the application version. Environments that use the application version donât inherit the tags.

(structure)

Describes a tag applied to a resource in an environment.

Key -> (string)

The key of the tag.

Value -> (string)

The value of the tag.

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

**To create a new application version**

The following command creates a new version, âv1â of an application named âMyAppâ:

```
aws elasticbeanstalk create-application-version --application-name MyApp --version-label v1 --description MyAppv1 --source-bundle S3Bucket="amzn-s3-demo-bucket",S3Key="sample.war" --auto-create-application
```

The application will be created automatically if it does not already exist, due to the auto-create-application option. The source bundle is a .war file stored in an s3 bucket named âamzn-s3-demo-bucketâ that contains the Apache Tomcat sample application.

Output:

```
{
  "ApplicationVersion": {
      "ApplicationName": "MyApp",
      "VersionLabel": "v1",
      "Description": "MyAppv1",
      "DateCreated": "2015-02-03T23:01:25.412Z",
      "DateUpdated": "2015-02-03T23:01:25.412Z",
      "SourceBundle": {
          "S3Bucket": "amzn-s3-demo-bucket",
          "S3Key": "sample.war"
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