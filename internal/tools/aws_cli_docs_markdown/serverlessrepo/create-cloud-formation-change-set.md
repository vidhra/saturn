# create-cloud-formation-change-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [serverlessrepo](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/index.html#cli-aws-serverlessrepo) ]

# create-cloud-formation-change-set

## Description

Creates an AWS CloudFormation change set for the given application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/serverlessrepo-2017-09-08/CreateCloudFormationChangeSet)

## Synopsis

```
create-cloud-formation-change-set
--application-id <value>
[--capabilities <value>]
[--change-set-name <value>]
[--client-token <value>]
[--description <value>]
[--notification-arns <value>]
[--parameter-overrides <value>]
[--resource-types <value>]
[--rollback-configuration <value>]
[--semantic-version <value>]
--stack-name <value>
[--tags <value>]
[--template-id <value>]
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

`--capabilities` (list)

A list of values that you must specify before you can deploy certain applications. Some applications might include resources that can affect permissions in your AWS account, for example, by creating new AWS Identity and Access Management (IAM) users. For those applications, you must explicitly acknowledge their capabilities by specifying this parameter.

The only valid values are CAPABILITY_IAM, CAPABILITY_NAMED_IAM, CAPABILITY_RESOURCE_POLICY, and CAPABILITY_AUTO_EXPAND.

The following resources require you to specify CAPABILITY_IAM or CAPABILITY_NAMED_IAM: [AWS::IAM::Group](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-group.html) , [AWS::IAM::InstanceProfile](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-instanceprofile.html) , [AWS::IAM::Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html) , and [AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html) . If the application contains IAM resources, you can specify either CAPABILITY_IAM or CAPABILITY_NAMED_IAM. If the application contains IAM resources with custom names, you must specify CAPABILITY_NAMED_IAM.

The following resources require you to specify CAPABILITY_RESOURCE_POLICY: [AWS::Lambda::Permission](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-permission.html) , [AWS::IAM:Policy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-policy.html) , [AWS::ApplicationAutoScaling::ScalingPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-applicationautoscaling-scalingpolicy.html) , [AWS::S3::BucketPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-policy.html) , [AWS::SQS::QueuePolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sqs-policy.html) , and [AWS::SNS:TopicPolicy](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-sns-policy.html) .

Applications that contain one or more nested applications require you to specify CAPABILITY_AUTO_EXPAND.

If your application template contains any of the above resources, we recommend that you review all permissions associated with the application before deploying. If you donât specify this parameter for an application that requires capabilities, the call will fail.

(string)

Syntax:

```
"string" "string" ...
```

`--change-set-name` (string)

This property corresponds to the parameter of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id1)AWS CloudFormation [CreateChangeSet](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet) * API.

`--client-token` (string)

This property corresponds to the parameter of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id3)AWS CloudFormation [CreateChangeSet](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet) * API.

`--description` (string)

This property corresponds to the parameter of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id5)AWS CloudFormation [CreateChangeSet](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet) * API.

`--notification-arns` (list)

This property corresponds to the parameter of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id7)AWS CloudFormation [CreateChangeSet](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet) * API.

(string)

Syntax:

```
"string" "string" ...
```

`--parameter-overrides` (list)

A list of parameter values for the parameters of the application.

(structure)

Parameter value of the application.

Name -> (string)

The key associated with the parameter. If you donât specify a key and value for a particular parameter, AWS CloudFormation uses the default value that is specified in your template.

Value -> (string)

The input value associated with the parameter.

Shorthand Syntax:

```
Name=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Value": "string"
  }
  ...
]
```

`--resource-types` (list)

This property corresponds to the parameter of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id9)AWS CloudFormation [CreateChangeSet](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet) * API.

(string)

Syntax:

```
"string" "string" ...
```

`--rollback-configuration` (structure)

This property corresponds to the parameter of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id11)AWS CloudFormation [CreateChangeSet](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet) * API.

MonitoringTimeInMinutes -> (integer)

This property corresponds to the content of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id13)AWS CloudFormation [RollbackConfiguration](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration) * Data Type.

RollbackTriggers -> (list)

This property corresponds to the content of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id15)AWS CloudFormation [RollbackConfiguration](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackConfiguration) * Data Type.

(structure)

This property corresponds to the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id17)AWS CloudFormation [RollbackTrigger](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger) * Data Type.

Arn -> (string)

This property corresponds to the content of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id19)AWS CloudFormation [RollbackTrigger](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger) * Data Type.

Type -> (string)

This property corresponds to the content of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id21)AWS CloudFormation [RollbackTrigger](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/RollbackTrigger) * Data Type.

Shorthand Syntax:

```
MonitoringTimeInMinutes=integer,RollbackTriggers=[{Arn=string,Type=string},{Arn=string,Type=string}]
```

JSON Syntax:

```
{
  "MonitoringTimeInMinutes": integer,
  "RollbackTriggers": [
    {
      "Arn": "string",
      "Type": "string"
    }
    ...
  ]
}
```

`--semantic-version` (string)

The semantic version of the application:

[https://semver.org/](https://semver.org/)

`--stack-name` (string)

This property corresponds to the parameter of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id23)AWS CloudFormation [CreateChangeSet](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet) * API.

`--tags` (list)

This property corresponds to the parameter of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id25)AWS CloudFormation [CreateChangeSet](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/CreateChangeSet) * API.

(structure)

This property corresponds to the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id27)AWS CloudFormation [Tag](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag) * Data Type.

Key -> (string)

This property corresponds to the content of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id29)AWS CloudFormation [Tag](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag) * Data Type.

Value -> (string)

This property corresponds to the content of the same name for the [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/serverlessrepo/create-cloud-formation-change-set.html#id31)AWS CloudFormation [Tag](https://docs.aws.amazon.com/goto/WebAPI/cloudformation-2010-05-15/Tag) * Data Type.

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

`--template-id` (string)

The UUID returned by CreateCloudFormationTemplate.

Pattern: [0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}

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

ChangeSetId -> (string)

The Amazon Resource Name (ARN) of the change set.

Length constraints: Minimum length of 1.

Pattern: ARN:[-a-zA-Z0-9:/]*

SemanticVersion -> (string)

The semantic version of the application:

[https://semver.org/](https://semver.org/)

StackId -> (string)

The unique ID of the stack.