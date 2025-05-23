# create-workteamÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-workteam.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/create-workteam.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# create-workteam

## Description

Creates a new work team for labeling your data. A work team is defined by one or more Amazon Cognito user pools. You must first create the user pools before you can create a work team.

You cannot create more than 25 work teams in an account and region.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/CreateWorkteam)

## Synopsis

```
create-workteam
--workteam-name <value>
[--workforce-name <value>]
--member-definitions <value>
--description <value>
[--notification-configuration <value>]
[--worker-access-configuration <value>]
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

`--workteam-name` (string)

The name of the work team. Use this name to identify the work team.

`--workforce-name` (string)

The name of the workforce.

`--member-definitions` (list)

A list of `MemberDefinition` objects that contains objects that identify the workers that make up the work team.

Workforces can be created using Amazon Cognito or your own OIDC Identity Provider (IdP). For private workforces created using Amazon Cognito use `CognitoMemberDefinition` . For workforces created using your own OIDC identity provider (IdP) use `OidcMemberDefinition` . Do not provide input for both of these parameters in a single request.

For workforces created using Amazon Cognito, private work teams correspond to Amazon Cognito *user groups* within the user pool used to create a workforce. All of the `CognitoMemberDefinition` objects that make up the member definition must have the same `ClientId` and `UserPool` values. To add a Amazon Cognito user group to an existing worker pool, see [Adding groups to a User Pool . For more information about user pools, see `Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) .

For workforces created using your own OIDC IdP, specify the user groups that you want to include in your private work team in `OidcMemberDefinition` by listing those groups in `Groups` .

(structure)

Defines an Amazon Cognito or your own OIDC IdP user group that is part of a work team.

CognitoMemberDefinition -> (structure)

The Amazon Cognito user group that is part of the work team.

UserPool -> (string)

An identifier for a user pool. The user pool must be in the same region as the service that you are calling.

UserGroup -> (string)

An identifier for a user group.

ClientId -> (string)

An identifier for an application client. You must create the app client ID using Amazon Cognito.

OidcMemberDefinition -> (structure)

A list user groups that exist in your OIDC Identity Provider (IdP). One to ten groups can be used to create a single private work team. When you add a user group to the list of `Groups` , you can add that user group to one or more private work teams. If you add a user group to a private work team, all workers in that user group are added to the work team.

Groups -> (list)

A list of comma seperated strings that identifies user groups in your OIDC IdP. Each user group is made up of a group of private workers.

(string)

Shorthand Syntax:

```
CognitoMemberDefinition={UserPool=string,UserGroup=string,ClientId=string},OidcMemberDefinition={Groups=[string,string]} ...
```

JSON Syntax:

```
[
  {
    "CognitoMemberDefinition": {
      "UserPool": "string",
      "UserGroup": "string",
      "ClientId": "string"
    },
    "OidcMemberDefinition": {
      "Groups": ["string", ...]
    }
  }
  ...
]
```

`--description` (string)

A description of the work team.

`--notification-configuration` (structure)

Configures notification of workers regarding available or expiring work items.

NotificationTopicArn -> (string)

The ARN for the Amazon SNS topic to which notifications should be published.

Shorthand Syntax:

```
NotificationTopicArn=string
```

JSON Syntax:

```
{
  "NotificationTopicArn": "string"
}
```

`--worker-access-configuration` (structure)

Use this optional parameter to constrain access to an Amazon S3 resource based on the IP address using supported IAM global condition keys. The Amazon S3 resource is accessed in the worker portal using a Amazon S3 presigned URL.

S3Presign -> (structure)

Defines any Amazon S3 resource constraints.

IamPolicyConstraints -> (structure)

Use this parameter to specify the allowed request source. Possible sources are either `SourceIp` or `VpcSourceIp` .

SourceIp -> (string)

When `SourceIp` is `Enabled` the workerâs IP address when a task is rendered in the worker portal is added to the IAM policy as a `Condition` used to generate the Amazon S3 presigned URL. This IP address is checked by Amazon S3 and must match in order for the Amazon S3 resource to be rendered in the worker portal.

VpcSourceIp -> (string)

When `VpcSourceIp` is `Enabled` the workerâs IP address when a task is rendered in private worker portal inside the VPC is added to the IAM policy as a `Condition` used to generate the Amazon S3 presigned URL. To render the task successfully Amazon S3 checks that the presigned URL is being accessed over an Amazon S3 VPC Endpoint, and that the workerâs IP address matches the IP address in the IAM policy. To learn more about configuring private worker portal, see [Use Amazon VPC mode from a private worker portal](https://docs.aws.amazon.com/sagemaker/latest/dg/samurai-vpc-worker-portal.html) .

Shorthand Syntax:

```
S3Presign={IamPolicyConstraints={SourceIp=string,VpcSourceIp=string}}
```

JSON Syntax:

```
{
  "S3Presign": {
    "IamPolicyConstraints": {
      "SourceIp": "Enabled"|"Disabled",
      "VpcSourceIp": "Enabled"|"Disabled"
    }
  }
}
```

`--tags` (list)

An array of key-value pairs.

For more information, see [Resource Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html) and [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what) in the *Amazon Web Services Billing and Cost Management User Guide* .

(structure)

A tag object that consists of a key and an optional value, used to manage metadata for SageMaker Amazon Web Services resources.

You can add tags to notebook instances, training jobs, hyperparameter tuning jobs, batch transform jobs, models, labeling jobs, work teams, endpoint configurations, and endpoints. For more information on adding tags to SageMaker resources, see [AddTags](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AddTags.html) .

For more information on adding metadata to your Amazon Web Services resources with tagging, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) . For advice on best practices for managing Amazon Web Services resources with tagging, see [Tagging Best Practices: Implement an Effective Amazon Web Services Resource Tagging Strategy](https://d1.awsstatic.com/whitepapers/aws-tagging-best-practices.pdf) .

Key -> (string)

The tag key. Tag keys must be unique per resource.

Value -> (string)

The tag value.

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

## Output

WorkteamArn -> (string)

The Amazon Resource Name (ARN) of the work team. You can use this ARN to identify the work team.