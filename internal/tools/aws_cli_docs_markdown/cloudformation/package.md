# packageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/package.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/package.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html#cli-aws-cloudformation) ]

# package

## Description

Packages the local artifacts (local paths) that your AWS CloudFormation template
references. The command uploads local artifacts, such as source code for an AWS
Lambda function or a Swagger file for an AWS API Gateway REST API, to an S3
bucket. The command returns a copy of your template, replacing references to
local artifacts with the S3 location where the command uploaded the artifacts.

Use this command to quickly upload local artifacts that might be required by
your template. After you package your templateâs artifacts, run the `deploy`
command to deploy the returned template.

This command can upload local artifacts referenced in the following places:

- `BodyS3Location` property for the `AWS::ApiGateway::RestApi` resource
- `Code` property for the `AWS::Lambda::Function` resource
- `Content` property for the `AWS::Lambda::LayerVersion` resource
- `CodeUri` property for the `AWS::Serverless::Function` resource
- `ContentUri` property for the `AWS::Serverless::LayerVersion` resource
- `Location` property for the `AWS::Serverless::Application` resource
- `DefinitionS3Location` property for the `AWS::AppSync::GraphQLSchema` resource
- `RequestMappingTemplateS3Location` property for the `AWS::AppSync::Resolver` resource
- `ResponseMappingTemplateS3Location` property for the `AWS::AppSync::Resolver` resource
- `RequestMappingTemplateS3Location` property for the `AWS::AppSync::FunctionConfiguration` resource
- `ResponseMappingTemplateS3Location` property for the `AWS::AppSync::FunctionConfiguration` resource
- `DefinitionUri` property for the `AWS::Serverless::Api` resource
- `Location` parameter for the `AWS::Include` transform
- `SourceBundle` property for the `AWS::ElasticBeanstalk::ApplicationVersion` resource
- `TemplateURL` property for the `AWS::CloudFormation::Stack` resource
- `Command.ScriptLocation` property for the `AWS::Glue::Job` resource
- `DefinitionS3Location` property for the `AWS::StepFunctions::StateMachine` resource
- `DefinitionUri` property for the `AWS::Serverless::StateMachine` resource
- `S3` property for the `AWS::CodeCommit::Repository` resource

To specify a local artifact in your template, specify a path to a local file or folder,
as either an absolute or relative path. The relative path is a location
that is relative to your templateâs location.

For example, if your AWS Lambda function source code is in the
`/home/user/code/lambdafunction/` folder, specify
`CodeUri: /home/user/code/lambdafunction` for the
`AWS::Serverless::Function` resource. The command returns a template and replaces
the local path with the S3 location: `CodeUri: s3://amzn-s3-demo-bucket/lambdafunction.zip`.

If you specify a file, the command directly uploads it to the S3 bucket. If you
specify a folder, the command zips the folder and then uploads the .zip file.
For most resources, if you donât specify a path, the command zips and uploads the
current working directory. The exception is `AWS::ApiGateway::RestApi`;
if you donât specify a `BodyS3Location`, this command will not upload an artifact to S3.

Before the command uploads artifacts, it checks if the artifacts are already
present in the S3 bucket to prevent unnecessary uploads. The command uses MD5
checksums to compare files. If the values match, the command doesnât upload the
artifacts. Use the `--force-upload flag` to skip this check and always upload the
artifacts.

## Synopsis

```
package
--template-file <value>
--s3-bucket <value>
[--s3-prefix <value>]
[--kms-key-id <value>]
[--output-template-file <value>]
[--use-json]
[--force-upload]
[--metadata <value>]
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

`--template-file` (string)
The path where your AWS CloudFormation template is located.

`--s3-bucket` (string)
The name of the S3 bucket where this command uploads the artifacts that are referenced in your template.

`--s3-prefix` (string)
A prefix name that the command adds to the artifactsâ name when it uploads them to the S3 bucket. The prefix name is a path name (folder name) for the S3 bucket.

`--kms-key-id` (string)
The ID of an AWS KMS key that the command uses to encrypt artifacts that are at rest in the S3 bucket.

`--output-template-file` (string)
The path to the file where the command writes the output AWS CloudFormation template. If you donât specify a path, the command writes the template to the standard output.

`--use-json` (boolean)
Indicates whether to use JSON as the format for the output AWS CloudFormation template. YAML is used by default.

`--force-upload` (boolean)
Indicates whether to override existing files in the S3 bucket. Specify this flag to upload artifacts even if they match existing artifacts in the S3 bucket.

`--metadata` (map)
A map of metadata to attach to *ALL* the artifacts that are referenced in your template.key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

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

Following command exports a template named `template.json` by uploading local
artifacts to S3 bucket `bucket-name` and writes the exported template to
`packaged-template.json`:

```
aws cloudformation package --template-file /path_to_template/template.json --s3-bucket bucket-name --output-template-file packaged-template.json --use-json
```