# describe-appÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/describe-app.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/describe-app.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# describe-app

## Description

Describes an Resilience Hub application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/DescribeApp)

## Synopsis

```
describe-app
--app-arn <value>
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

`--app-arn` (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

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

app -> (structure)

The specified application, returned as an object with details including compliance status, creation time, description, resiliency score, and more.

appArn -> (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

assessmentSchedule -> (string)

Assessment execution schedule with âDailyâ or âDisabledâ values.

awsApplicationArn -> (string)

Amazon Resource Name (ARN) of Resource Groups group that is integrated with an AppRegistry application. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

complianceStatus -> (string)

Current status of compliance for the resiliency policy.

creationTime -> (timestamp)

Date and time when the application was created.

description -> (string)

Optional description for an application.

driftStatus -> (string)

Indicates if compliance drifts (deviations) were detected while running an assessment for your application.

eventSubscriptions -> (list)

The list of events you would like to subscribe and get notification for. Currently, Resilience Hub supports notifications only for **Drift detected** and **Scheduled assessment failure** events.

(structure)

Indicates an event you would like to subscribe and get notification for. Currently, Resilience Hub supports notifications only for **Drift detected** and **Scheduled assessment failure** events.

eventType -> (string)

The type of event you would like to subscribe and get notification for. Currently, Resilience Hub supports notifications only for **Drift detected** (`DriftDetected` ) and **Scheduled assessment failure** (`ScheduledAssessmentFailure` ) events.

name -> (string)

Unique name to identify an event subscription.

snsTopicArn -> (string)

Amazon Resource Name (ARN) of the Amazon Simple Notification Service topic. The format for this ARN is: `arn:partition:sns:region:account:topic-name` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

lastAppComplianceEvaluationTime -> (timestamp)

Date and time the most recent compliance evaluation.

lastDriftEvaluationTime -> (timestamp)

Indicates the last time that a drift was evaluated.

lastResiliencyScoreEvaluationTime -> (timestamp)

Date and time the most recent resiliency score evaluation.

name -> (string)

Name for the application.

permissionModel -> (structure)

Defines the roles and credentials that Resilience Hub would use while creating the application, importing its resources, and running an assessment.

crossAccountRoleArns -> (list)

Defines a list of role Amazon Resource Names (ARNs) to be used in other accounts. These ARNs are used for querying purposes while importing resources and assessing your application.

### Note

- These ARNs are required only when your resources are in other accounts and you have different role name in these accounts. Else, the invoker role name will be used in the other accounts.
- These roles must have a trust policy with `iam:AssumeRole` permission to the invoker role in the primary account.

(string)

invokerRoleName -> (string)

Existing Amazon Web Services IAM role name in the primary Amazon Web Services account that will be assumed by Resilience Hub Service Principle to obtain a read-only access to your application resources while running an assessment.

If your IAM role includes a path, you must include the path in the `invokerRoleName` parameter. For example, if your IAM roleâs ARN is `arn:aws:iam:123456789012:role/my-path/role-name` , you should pass `my-path/role-name` .

### Note

- You must have `iam:passRole` permission for this role while creating or updating the application.
- Currently, `invokerRoleName` accepts only `[A-Za-z0-9_+=,.@-]` characters.

type -> (string)

Defines how Resilience Hub scans your resources. It can scan for the resources by using a pre-existing role in your Amazon Web Services account, or by using the credentials of the current IAM user.

policyArn -> (string)

Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :resiliency-policy/`policy-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

resiliencyScore -> (double)

Current resiliency score for the application.

rpoInSecs -> (integer)

Recovery Point Objective (RPO) in seconds.

rtoInSecs -> (integer)

Recovery Time Objective (RTO) in seconds.

status -> (string)

Status of the application.

tags -> (map)

Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.

key -> (string)

value -> (string)