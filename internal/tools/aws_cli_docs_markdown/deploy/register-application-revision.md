# register-application-revisionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register-application-revision.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register-application-revision.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deploy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/index.html#cli-aws-deploy) ]

# register-application-revision

## Description

Registers with CodeDeploy a revision for the specified application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codedeploy-2014-10-06/RegisterApplicationRevision)

## Synopsis

```
register-application-revision
--application-name <value>
[--description <value>]
[--revision <value>]
[--s3-location <value>]
[--github-location <value>]
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

The name of an CodeDeploy application associated with the user or Amazon Web Services account.

`--description` (string)

A comment about the revision.

`--revision` (structure)

Information about the application revision to register, including type and location.

revisionType -> (string)

The type of application revision:

- S3: An application revision stored in Amazon S3.
- GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
- String: A YAML-formatted or JSON-formatted string (Lambda deployments only).
- AppSpecContent: An `AppSpecContent` object that contains the contents of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.

s3Location -> (structure)

Information about the location of a revision stored in Amazon S3.

bucket -> (string)

The name of the Amazon S3 bucket where the application revision is stored.

key -> (string)

The name of the Amazon S3 object that represents the bundled artifacts for the application revision.

bundleType -> (string)

The file type of the application revision. Must be one of the following:

- `tar` : A tar archive file.
- `tgz` : A compressed tar archive file.
- `zip` : A zip archive file.
- `YAML` : A YAML-formatted file.
- `JSON` : A JSON-formatted file.

version -> (string)

A specific version of the Amazon S3 object that represents the bundled artifacts for the application revision.

If the version is not specified, the system uses the most recent version by default.

eTag -> (string)

The ETag of the Amazon S3 object that represents the bundled artifacts for the application revision.

If the ETag is not specified as an input parameter, ETag validation of the object is skipped.

gitHubLocation -> (structure)

Information about the location of application artifacts stored in GitHub.

repository -> (string)

The GitHub account and repository pair that stores a reference to the commit that represents the bundled artifacts for the application revision.

Specified as account/repository.

commitId -> (string)

The SHA1 commit ID of the GitHub commit that represents the bundled artifacts for the application revision.

string -> (structure)

Information about the location of an Lambda deployment revision stored as a RawString.

content -> (string)

The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.

sha256 -> (string)

The SHA256 hash value of the revision content.

appSpecContent -> (structure)

The content of an AppSpec file for an Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.

content -> (string)

The YAML-formatted or JSON-formatted revision string.

For an Lambda deployment, the content includes a Lambda function name, the alias for its original version, and the alias for its replacement version. The deployment shifts traffic from the original version of the Lambda function to the replacement version.

For an Amazon ECS deployment, the content includes the task name, information about the load balancer that serves traffic to the container, and more.

For both types of deployments, the content can specify Lambda functions that run at specified hooks, such as `BeforeInstall` , during a deployment.

sha256 -> (string)

The SHA256 hash value of the revision content.

Shorthand Syntax:

```
revisionType=string,s3Location={bucket=string,key=string,bundleType=string,version=string,eTag=string},gitHubLocation={repository=string,commitId=string},string={content=string,sha256=string},appSpecContent={content=string,sha256=string}
```

JSON Syntax:

```
{
  "revisionType": "S3"|"GitHub"|"String"|"AppSpecContent",
  "s3Location": {
    "bucket": "string",
    "key": "string",
    "bundleType": "tar"|"tgz"|"zip"|"YAML"|"JSON",
    "version": "string",
    "eTag": "string"
  },
  "gitHubLocation": {
    "repository": "string",
    "commitId": "string"
  },
  "string": {
    "content": "string",
    "sha256": "string"
  },
  "appSpecContent": {
    "content": "string",
    "sha256": "string"
  }
}
```

`--s3-location` (structure)
Information about the location of the application revision in Amazon S3. You must specify the bucket, the key, and bundleType. Optionally, you can also specify an eTag and version.bucket -> (string)

The Amazon S3 bucket name.

key -> (string)

The Amazon S3 object key name.

bundleType -> (string)

The format of the bundle stored in Amazon S3.

eTag -> (string)

The Amazon S3 object eTag.

version -> (string)

The Amazon S3 object version.

Shorthand Syntax:

```
bucket=string,key=string,bundleType=string,eTag=string,version=string
```

JSON Syntax:

```
{
  "bucket": "string",
  "key": "string",
  "bundleType": "tar"|"tgz"|"zip",
  "eTag": "string",
  "version": "string"
}
```

`--github-location` (structure)
Information about the location of the application revision in GitHub. You must specify the repository and commit ID that references the application revision. For the repository, use the format GitHub-account/repository-name or GitHub-org/repository-name. For the commit ID, use the SHA1 Git commit reference.repository -> (string)

The GitHub account or organization and repository. Specify as GitHub-account/repository or GitHub-org/repository.

commitId -> (string)

The SHA1 Git commit reference.

Shorthand Syntax:

```
repository=string,commitId=string
```

JSON Syntax:

```
{
  "repository": "string",
  "commitId": "string"
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

**To register information about an already-uploaded application revision**

The following `register-application-revision` example registers information about an already-uploaded application revision stored in Amazon S3 with AWS CodeDeploy.

```
aws deploy register-application-revision \
    --application-name WordPress_App \
    --description "Revised WordPress application" \
    --s3-location bucket=CodeDeployDemoBucket,key=RevisedWordPressApp.zip,bundleType=zip,eTag=cecc9b8a08eac650a6e71fdb88EXAMPLE
```

This command produces no output.

## Output

None