# list-app-assessment-compliance-driftsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/list-app-assessment-compliance-drifts.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/list-app-assessment-compliance-drifts.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# list-app-assessment-compliance-drifts

## Description

List of compliance drifts that were detected while running an assessment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/ListAppAssessmentComplianceDrifts)

## Synopsis

```
list-app-assessment-compliance-drifts
--assessment-arn <value>
[--max-results <value>]
[--next-token <value>]
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

`--max-results` (integer)

Maximum number of compliance drifts requested.

`--next-token` (string)

Null, or the token from a previous call to get the next set of results.

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

complianceDrifts -> (list)

Indicates compliance drifts (recovery time objective (RTO) and recovery point objective (RPO)) detected for an assessed entity.

(structure)

Indicates the compliance drifts (recovery time objective (RTO) and recovery point objective (RPO)) that were detected for an assessed entity.

actualReferenceId -> (string)

Assessment identifier that is associated with this drift item.

actualValue -> (map)

Actual compliance value of the entity.

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

appId -> (string)

Identifier of your application.

appVersion -> (string)

Published version of your application on which drift was detected.

diffType -> (string)

Difference type between actual and expected recovery point objective (RPO) and recovery time objective (RTO) values. Currently, Resilience Hub supports only `NotEqual` difference type.

driftType -> (string)

The type of drift detected. Currently, Resilience Hub supports only **ApplicationCompliance** drift type.

entityId -> (string)

Identifier of an entity in which drift was detected. For compliance drift, the entity ID can be either application ID or the AppComponent ID.

entityType -> (string)

The type of entity in which drift was detected. For compliance drifts, Resilience Hub supports `AWS::ResilienceHub::AppComponent` and `AWS::ResilienceHub::Application` .

expectedReferenceId -> (string)

Assessment identifier of a previous assessment of the same application version. Resilience Hub uses the previous assessment (associated with the reference identifier) to compare the compliance with the current assessment to identify drifts.

expectedValue -> (map)

The expected compliance value of an entity.

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

nextToken -> (string)

Null, or the token from a previous call to get the next set of results.