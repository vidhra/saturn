# describe-app-assessmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/describe-app-assessment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/describe-app-assessment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# describe-app-assessment

## Description

Describes an assessment for an Resilience Hub application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/DescribeAppAssessment)

## Synopsis

```
describe-app-assessment
--assessment-arn <value>
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

`--assessment-arn` (string)

Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app-assessment/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

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

assessment -> (structure)

The assessment for an Resilience Hub application, returned as an object. This object includes Amazon Resource Names (ARNs), compliance information, compliance status, cost, messages, resiliency scores, and more.

appArn -> (string)

Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

appVersion -> (string)

Version of an application.

assessmentArn -> (string)

Amazon Resource Name (ARN) of the assessment. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :app-assessment/`app-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

assessmentName -> (string)

Name of the assessment.

assessmentStatus -> (string)

Current status of the assessment for the resiliency policy.

compliance -> (map)

Application compliance against the resiliency policy.

key -> (string)

value -> (structure)

Defines the compliance against the resiliency policy for a disruption.

achievableRpoInSecs -> (integer)

The Recovery Point Objective (RPO) that is achievable, in seconds.

achievableRtoInSecs -> (integer)

The Recovery Time Objective (RTO) that is achievable, in seconds

complianceStatus -> (string)

The current status of compliance for the resiliency policy.

currentRpoInSecs -> (integer)

The current RPO, in seconds.

currentRtoInSecs -> (integer)

The current RTO, in seconds.

message -> (string)

The disruption compliance message.

rpoDescription -> (string)

The RPO description.

rpoReferenceId -> (string)

Reference identifier of the RPO .

rtoDescription -> (string)

The RTO description.

rtoReferenceId -> (string)

Reference identifier of the RTO.

complianceStatus -> (string)

Current status of the compliance for the resiliency policy.

cost -> (structure)

Cost for the application.

amount -> (double)

The cost amount.

currency -> (string)

The cost currency, for example `USD` .

frequency -> (string)

The cost frequency.

driftStatus -> (string)

Indicates if compliance drifts (deviations) were detected while running an assessment for your application.

endTime -> (timestamp)

End time for the action.

invoker -> (string)

The entity that invoked the assessment.

message -> (string)

Error or warning message from the assessment execution

policy -> (structure)

Resiliency policy of an application.

creationTime -> (timestamp)

Date and time when the resiliency policy was created.

dataLocationConstraint -> (string)

Specifies a high-level geographical location constraint for where your resilience policy data can be stored.

estimatedCostTier -> (string)

Specifies the estimated cost tier of the resiliency policy.

policy -> (map)

The resiliency policy.

key -> (string)

value -> (structure)

Defines a failure policy.

rpoInSecs -> (integer)

Recovery Point Objective (RPO) in seconds.

rtoInSecs -> (integer)

Recovery Time Objective (RTO) in seconds.

policyArn -> (string)

Amazon Resource Name (ARN) of the resiliency policy. The format for this ARN is: arn:`partition` :resiliencehub:`region` :`account` :resiliency-policy/`policy-id` . For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* guide.

policyDescription -> (string)

Description of the resiliency policy.

policyName -> (string)

The name of the policy

tags -> (map)

Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.

key -> (string)

value -> (string)

tier -> (string)

The tier for this resiliency policy, ranging from the highest severity (`MissionCritical` ) to lowest (`NonCritical` ).

resiliencyScore -> (structure)

Current resiliency score for an application.

componentScore -> (map)

The score generated by Resilience Hub for the scoring component after running an assessment.

For example, if the `score` is 25 points, it indicates the overall score of your application generated by Resilience Hub after running an assessment.

key -> (string)

value -> (structure)

Resiliency score of each scoring component. For more information about scoring component, see [Calculating resiliency score](https://docs.aws.amazon.com/resilience-hub/latest/userguide/calculate-score.html) .

excludedCount -> (long)

Number of recommendations that were excluded from the assessment.

For example, if the `excludedCount` for Alarms coverage scoring component is 7, it indicates that 7 Amazon CloudWatch alarms are excluded from the assessment.

outstandingCount -> (long)

Number of recommendations that must be implemented to obtain the maximum possible score for the scoring component. For SOPs, alarms, and tests, these are the number of recommendations that must be implemented. For compliance, these are the number of Application Components that have breached the resiliency policy.

For example, if the `outstandingCount` for Alarms coverage scoring component is 5, it indicates that 5 Amazon CloudWatch alarms need to be implemented to achieve the maximum possible score.

possibleScore -> (double)

Maximum possible score that can be obtained for the scoring component.

For example, if the `possibleScore` is 20 points, it indicates the maximum possible score you can achieve for the scoring component when you run a new assessment after implementing all the Resilience Hub recommendations.

score -> (double)

Resiliency score points given for the scoring component. The score is always less than or equal to the `possibleScore` .

disruptionScore -> (map)

The disruption score for a valid key.

key -> (string)

value -> (double)

score -> (double)

The outage score for a valid key.

resourceErrorsDetails -> (structure)

A resource error object containing a list of errors retrieving an applicationâs resources.

hasMoreErrors -> (boolean)

This indicates if there are more errors not listed in the `resourceErrors` list.

resourceErrors -> (list)

A list of errors retrieving an applicationâs resources.

(structure)

Defines application resource errors.

logicalResourceId -> (string)

Identifier of the logical resource.

physicalResourceId -> (string)

Identifier of the physical resource.

reason -> (string)

This is the error message.

startTime -> (timestamp)

Starting time for the action.

summary -> (structure)

Indicates the AI-generated summary for the Resilience Hub assessment, providing a concise overview that highlights the top risks and recommendations.

### Note

This property is available only in the US East (N. Virginia) Region.

riskRecommendations -> (list)

Indicates the top risks and recommendations identified by the Resilience Hub assessment, each representing a specific risk and the corresponding recommendation to address it.

### Note

This property is available only in the US East (N. Virginia) Region.

(structure)

Indicates a specific risk identified in the Resilience Hub assessment and the corresponding recommendation provided to address that risk.

### Note

The assessment summary generated by large language models (LLMs) on Amazon Bedrock are only suggestions. The current level of generative AI technology is not perfect and LLMs are not infallible. Bias and incorrect answers, although rare, should be expected. Review each recommendation in the assessment summary before you use the output from an LLM.

### Note

This property is available only in the US East (N. Virginia) Region.

appComponents -> (list)

Indicates the Application Components (AppComponents) that were assessed as part of the assessment and are associated with the identified risk and recommendation.

### Note

This property is available only in the US East (N. Virginia) Region.

(string)

recommendation -> (string)

Indicates the recommendation provided by the Resilience Hub to address the identified risks in the application.

### Note

This property is available only in the US East (N. Virginia) Region.

risk -> (string)

Indicates the description of the potential risk identified in the application as part of the Resilience Hub assessment.

### Note

This property is available only in the US East (N. Virginia) Region.

summary -> (string)

Indicates a concise summary that provides an overview of the Resilience Hub assessment.

### Note

This property is available only in the US East (N. Virginia) Region.

tags -> (map)

Tags assigned to the resource. A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key/value pair.

key -> (string)

value -> (string)

versionName -> (string)

Version name of the published application.