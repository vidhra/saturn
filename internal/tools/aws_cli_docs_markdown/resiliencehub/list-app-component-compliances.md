# list-app-component-compliancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/list-app-component-compliances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/list-app-component-compliances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# list-app-component-compliances

## Description

Lists the compliances for an Resilience Hub Application Component.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/ListAppComponentCompliances)

## Synopsis

```
list-app-component-compliances
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

Maximum number of results to include in the response. If more results exist than the specified `MaxResults` value, a token is included in the response so that the remaining results can be retrieved.

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

componentCompliances -> (list)

The compliances for an Resilience Hub Application Component, returned as an object. This object contains the names of the Application Components, compliances, costs, resiliency scores, outage scores, and more.

(structure)

Defines the compliance of an Application Component against the resiliency policy.

appComponentName -> (string)

Name of the Application Component.

compliance -> (map)

The compliance of the Application Component against the resiliency policy.

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

cost -> (structure)

The cost for the application.

amount -> (double)

The cost amount.

currency -> (string)

The cost currency, for example `USD` .

frequency -> (string)

The cost frequency.

message -> (string)

The compliance message.

resiliencyScore -> (structure)

The current resiliency score for the application.

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

status -> (string)

Status of the action.

nextToken -> (string)

Token for the next set of results, or null if there are no more results.