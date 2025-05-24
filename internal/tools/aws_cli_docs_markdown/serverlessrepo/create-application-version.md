# create-application-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-application-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-application-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [serverlessrepo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/index.html#cli-aws-serverlessrepo) ]

# create-application-version

## Description

Creates an application version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/CreateApplicationVersion)

## Synopsis

```
create-application-version
--application-id <value>
--semantic-version <value>
[--source-code-archive-url <value>]
[--source-code-url <value>]
[--template-body <value>]
[--template-url <value>]
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

`--application-id` (string)

The Amazon Resource Name (ARN) of the application.

`--semantic-version` (string)

The semantic version of the new version.

`--source-code-archive-url` (string)

A link to the S3 object that contains the ZIP archive of the source code for this version of your application.

Maximum size 50 MB

`--source-code-url` (string)

A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.

`--template-body` (string)

The raw packaged AWS SAM template of your application.

`--template-url` (string)

A link to the packaged AWS SAM template of your application.

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

## Output

ApplicationId -> (string)

The application Amazon Resource Name (ARN).

CreationTime -> (string)

The date and time this resource was created.

ParameterDefinitions -> (list)

An array of parameter types supported by the application.

(structure)

Parameters supported by the application.

AllowedPattern -> (string)

A regular expression that represents the patterns to allow for String types.

AllowedValues -> (list)

An array containing the list of values allowed for the parameter.

(string)

ConstraintDescription -> (string)

A string that explains a constraint when the constraint is violated. For example, without a constraint description, a parameter that has an allowed pattern of [A-Za-z0-9]+ displays the following error message when the user specifies an invalid value:

Malformed input-Parameter MyParameter must match pattern [A-Za-z0-9]+

By adding a constraint description, such as âmust contain only uppercase and lowercase letters and numbers,â you can display the following customized error message:

Malformed input-Parameter MyParameter must contain only uppercase and lowercase letters and numbers.

DefaultValue -> (string)

A value of the appropriate type for the template to use if no value is specified when a stack is created. If you define constraints for the parameter, you must specify a value that adheres to those constraints.

Description -> (string)

A string of up to 4,000 characters that describes the parameter.

MaxLength -> (integer)

An integer value that determines the largest number of characters that you want to allow for String types.

MaxValue -> (integer)

A numeric value that determines the largest numeric value that you want to allow for Number types.

MinLength -> (integer)

An integer value that determines the smallest number of characters that you want to allow for String types.

MinValue -> (integer)

A numeric value that determines the smallest numeric value that you want to allow for Number types.

Name -> (string)

The name of the parameter.

NoEcho -> (boolean)

Whether to mask the parameter value whenever anyone makes a call that describes the stack. If you set the value to true, the parameter value is masked with asterisks (*****).

ReferencedByResources -> (list)

A list of AWS SAM resources that use this parameter.

(string)

Type -> (string)

The type of the parameter.

Valid values: String | Number | List<Number> | CommaDelimitedList

String: A literal string.

For example, users can specify âMyUserNameâ.

Number: An integer or float. AWS CloudFormation validates the parameter value as a number. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a string.

For example, users might specify â8888â.

List<Number>: An array of integers or floats that are separated by commas. AWS CloudFormation validates the parameter value as numbers. However, when you use the parameter elsewhere in your template (for example, by using the Ref intrinsic function), the parameter value becomes a list of strings.

For example, users might specify â80,20â, and then Ref results in [â80â,â20â].

CommaDelimitedList: An array of literal strings that are separated by commas. The total number of strings should be one more than the total number of commas. Also, each member string is space-trimmed.

For example, users might specify âtest,dev,prodâ, and then Ref results in [âtestâ,âdevâ,âprodâ].

RequiredCapabilities -> (list)

A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.

The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.

The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: [AWS::IAM::Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html) , [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html) , [AWS::IAM::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html) , and [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html) . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.

The following resources require you to specify CAPABILITY_RESOURCE_POLICY: [AWS::Lambda::Permission](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html) , [AWS::IAM:Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html) , [AWS::ApplicationAutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html) , [AWS::S3::BucketPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html) , [AWS::SQS::QueuePolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html) , and [AWS::SNS::TopicPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html) .

Applications that contain one or more nested applications require you to specify CAPABILITY_AUTO_EXPAND.

If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you donât specify this parameter for an application that requires capabilities, the call will fail.

(string)

Values that must be specified in order to deploy some applications.

ResourcesSupported -> (boolean)

Whether all of the AWS resources contained in this application are supported in the region in which it is being retrieved.

SemanticVersion -> (string)

The semantic version of the application:

[https://semver.org/](https://semver.org/)

SourceCodeArchiveUrl -> (string)

A link to the S3 object that contains the ZIP archive of the source code for this version of your application.

Maximum size 50 MB

SourceCodeUrl -> (string)

A link to a public repository for the source code of your application, for example the URL of a specific GitHub commit.

TemplateUrl -> (string)

A link to the packaged AWS SAM template of your application.