# list-alarm-recommendationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/list-alarm-recommendations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/list-alarm-recommendations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [resiliencehub](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/resiliencehub/index.html#cli-aws-resiliencehub) ]

# list-alarm-recommendations

## Description

Lists the alarm recommendations for an Resilience Hub application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/resiliencehub-2020-04-30/ListAlarmRecommendations)

## Synopsis

```
list-alarm-recommendations
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

alarmRecommendations -> (list)

The alarm recommendations for an Resilience Hub application, returned as an object. This object includes Application Component names, descriptions, information about whether a recommendation has already been implemented or not, prerequisites, and more.

(structure)

Defines a recommendation for a CloudWatch alarm.

appComponentName -> (string)

Application Component name for the CloudWatch alarm recommendation. This name is saved as the first item in the `appComponentNames` list.

appComponentNames -> (list)

List of Application Component names for the CloudWatch alarm recommendation.

(string)

description -> (string)

Description of the alarm recommendation.

items -> (list)

List of CloudWatch alarm recommendations.

(structure)

Defines a recommendation.

alreadyImplemented -> (boolean)

Specifies if the recommendation has already been implemented.

discoveredAlarm -> (structure)

Indicates the previously implemented Amazon CloudWatch alarm discovered by Resilience Hub.

alarmArn -> (string)

Amazon Resource Name (ARN) of the Amazon CloudWatch alarm.

source -> (string)

Indicates the source of the Amazon CloudWatch alarm. That is, it indicates if the alarm was created using Resilience Hub recommendation (`AwsResilienceHub` ), or if you had created the alarm in Amazon CloudWatch (`Customer` ).

excludeReason -> (string)

Indicates the reason for excluding an operational recommendation.

excluded -> (boolean)

Indicates if an operational recommendation item is excluded.

latestDiscoveredExperiment -> (structure)

Indicates the experiment created in FIS that was discovered by Resilience Hub, which matches the recommendation.

experimentArn -> (string)

Amazon Resource Name (ARN) of the FIS experiment.

experimentTemplateId -> (string)

Identifier of the FIS experiment template.

resourceId -> (string)

Identifier of the resource.

targetAccountId -> (string)

Identifier of the target account.

targetRegion -> (string)

The target region.

name -> (string)

Name of the alarm recommendation.

prerequisite -> (string)

The prerequisite for the alarm recommendation.

recommendationId -> (string)

Identifier of the alarm recommendation.

recommendationStatus -> (string)

Status of the recommended Amazon CloudWatch alarm.

referenceId -> (string)

Reference identifier of the alarm recommendation.

type -> (string)

Type of alarm recommendation.

nextToken -> (string)

Token for the next set of results, or null if there are no more results.