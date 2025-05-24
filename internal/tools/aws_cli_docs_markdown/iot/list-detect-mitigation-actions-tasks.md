# list-detect-mitigation-actions-tasksÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-detect-mitigation-actions-tasks.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/list-detect-mitigation-actions-tasks.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# list-detect-mitigation-actions-tasks

## Description

List of Device Defender ML Detect mitigation actions tasks.

Requires permission to access the [ListDetectMitigationActionsTasks](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/ListDetectMitigationActionsTasks)

`list-detect-mitigation-actions-tasks` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `tasks`

## Synopsis

```
list-detect-mitigation-actions-tasks
--start-time <value>
--end-time <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--start-time` (timestamp)

A filter to limit results to those found after the specified time. You must specify either the startTime and endTime or the taskId, but not both.

`--end-time` (timestamp)

The end of the time period for which ML Detect mitigation actions tasks are returned.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

tasks -> (list)

The collection of ML Detect mitigation tasks that matched the filter criteria.

(structure)

The summary of the mitigation action tasks.

taskId -> (string)

The unique identifier of the task.

taskStatus -> (string)

The status of the task.

taskStartTime -> (timestamp)

The date the task started.

taskEndTime -> (timestamp)

The date the task ended.

target -> (structure)

Specifies the ML Detect findings to which the mitigation actions are applied.

violationIds -> (list)

The unique identifiers of the violations.

(string)

securityProfileName -> (string)

The name of the security profile.

behaviorName -> (string)

The name of the behavior.

violationEventOccurrenceRange -> (structure)

Specifies the time period of which violation events occurred between.

startTime -> (timestamp)

The start date and time of a time period in which violation events occurred.

endTime -> (timestamp)

The end date and time of a time period in which violation events occurred.

onlyActiveViolationsIncluded -> (boolean)

Includes only active violations.

suppressedAlertsIncluded -> (boolean)

Includes suppressed alerts.

actionsDefinition -> (list)

The definition of the actions.

(structure)

Describes which changes should be applied as part of a mitigation action.

name -> (string)

A user-friendly name for the mitigation action.

id -> (string)

A unique identifier for the mitigation action.

roleArn -> (string)

The IAM role ARN used to apply this mitigation action.

actionParams -> (structure)

The set of parameters for this mitigation action. The parameters vary, depending on the kind of action you apply.

updateDeviceCertificateParams -> (structure)

Parameters to define a mitigation action that changes the state of the device certificate to inactive.

action -> (string)

The action that you want to apply to the device certificate. The only supported value is `DEACTIVATE` .

updateCACertificateParams -> (structure)

Parameters to define a mitigation action that changes the state of the CA certificate to inactive.

action -> (string)

The action that you want to apply to the CA certificate. The only supported value is `DEACTIVATE` .

addThingsToThingGroupParams -> (structure)

Parameters to define a mitigation action that moves devices associated with a certificate to one or more specified thing groups, typically for quarantine.

thingGroupNames -> (list)

The list of groups to which you want to add the things that triggered the mitigation action. You can add a thing to a maximum of 10 groups, but you canât add a thing to more than one group in the same hierarchy.

(string)

overrideDynamicGroups -> (boolean)

Specifies if this mitigation action can move the things that triggered the mitigation action even if they are part of one or more dynamic thing groups.

replaceDefaultPolicyVersionParams -> (structure)

Parameters to define a mitigation action that adds a blank policy to restrict permissions.

templateName -> (string)

The name of the template to be applied. The only supported value is `BLANK_POLICY` .

enableIoTLoggingParams -> (structure)

Parameters to define a mitigation action that enables Amazon Web Services IoT Core logging at a specified level of detail.

roleArnForLogging -> (string)

The Amazon Resource Name (ARN) of the IAM role used for logging.

logLevel -> (string)

Specifies the type of information to be logged.

publishFindingToSnsParams -> (structure)

Parameters to define a mitigation action that publishes findings to Amazon Simple Notification Service (Amazon SNS. You can implement your own custom actions in response to the Amazon SNS messages.

topicArn -> (string)

The ARN of the topic to which you want to publish the findings.

taskStatistics -> (structure)

The statistics of a mitigation action task.

actionsExecuted -> (long)

The actions that were performed.

actionsSkipped -> (long)

The actions that were skipped.

actionsFailed -> (long)

The actions that failed.

nextToken -> (string)

A token that can be used to retrieve the next set of results, or `null` if there are no additional results.