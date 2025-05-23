# describe-assessment-runsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-runs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/describe-assessment-runs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [inspector](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/inspector/index.html#cli-aws-inspector) ]

# describe-assessment-runs

## Description

Describes the assessment runs that are specified by the ARNs of the assessment runs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/inspector-2016-02-16/DescribeAssessmentRuns)

## Synopsis

```
describe-assessment-runs
--assessment-run-arns <value>
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

`--assessment-run-arns` (list)

The ARN that specifies the assessment run that you want to describe.

(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To describe assessment runs**

The following `describe-assessment-run` command describes an assessment run with the ARN of `arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE`:

```
aws inspector describe-assessment-runs --assessment-run-arns arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE
```

Output:

```
{
        "assessmentRuns": [
          {
                "arn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw/run/0-MKkpXXPE",
                "assessmentTemplateArn": "arn:aws:inspector:us-west-2:123456789012:target/0-0kFIPusq/template/0-4r1V2mAw",
                "completedAt": 1458680301.4,
                "createdAt": 1458680170.035,
                "dataCollected": true,
                "durationInSeconds": 3600,
                "name": "Run 1 for ExampleAssessmentTemplate",
                "notifications": [],
                "rulesPackageArns": [
                  "arn:aws:inspector:us-west-2:758058086616:rulespackage/0-X1KXtawP"
                ],
                "startedAt": 1458680170.161,
                "state": "COMPLETED",
                "stateChangedAt": 1458680301.4,
                "stateChanges": [
                  {
                        "state": "CREATED",
                        "stateChangedAt": 1458680170.035
                  },
                  {
                        "state": "START_DATA_COLLECTION_PENDING",
                        "stateChangedAt": 1458680170.065
                  },
                  {
                        "state": "START_DATA_COLLECTION_IN_PROGRESS",
                        "stateChangedAt": 1458680170.096
                  },
                  {
                        "state": "COLLECTING_DATA",
                        "stateChangedAt": 1458680170.161
                  },
                  {
                        "state": "STOP_DATA_COLLECTION_PENDING",
                        "stateChangedAt": 1458680239.883
                  },
                  {
                        "state": "DATA_COLLECTED",
                        "stateChangedAt": 1458680299.847
                  },
                  {
                        "state": "EVALUATING_RULES",
                        "stateChangedAt": 1458680300.099
                  },
                  {
                        "state": "COMPLETED",
                        "stateChangedAt": 1458680301.4
                  }
                ],
                "userAttributesForFindings": []
          }
        ],
        "failedItems": {}
}
```

For more information, see [Amazon Inspector Assessment Templates and Assessment Runs](https://docs.aws.amazon.com/inspector/latest/userguide/inspector_assessments.html) in the *Amazon Inspector* guide.

## Output

assessmentRuns -> (list)

Information about the assessment run.

(structure)

A snapshot of an Amazon Inspector assessment run that contains the findings of the assessment run .

Used as the response element in the  DescribeAssessmentRuns action.

arn -> (string)

The ARN of the assessment run.

name -> (string)

The auto-generated name for the assessment run.

assessmentTemplateArn -> (string)

The ARN of the assessment template that is associated with the assessment run.

state -> (string)

The state of the assessment run.

durationInSeconds -> (integer)

The duration of the assessment run.

rulesPackageArns -> (list)

The rules packages selected for the assessment run.

(string)

userAttributesForFindings -> (list)

The user-defined attributes that are assigned to every generated finding.

(structure)

This data type is used as a request parameter in the  AddAttributesToFindings and  CreateAssessmentTemplate actions.

key -> (string)

The attribute key.

value -> (string)

The value assigned to the attribute key.

createdAt -> (timestamp)

The time when  StartAssessmentRun was called.

startedAt -> (timestamp)

The time when  StartAssessmentRun was called.

completedAt -> (timestamp)

The assessment run completion time that corresponds to the rules packages evaluation completion time or failure.

stateChangedAt -> (timestamp)

The last time when the assessment runâs state changed.

dataCollected -> (boolean)

A Boolean value (true or false) that specifies whether the process of collecting data from the agents is completed.

stateChanges -> (list)

A list of the assessment run state changes.

(structure)

Used as one of the elements of the  AssessmentRun data type.

stateChangedAt -> (timestamp)

The last time the assessment run state changed.

state -> (string)

The assessment run state.

notifications -> (list)

A list of notifications for the event subscriptions. A notification about a particular generated finding is added to this list only once.

(structure)

Used as one of the elements of the  AssessmentRun data type.

date -> (timestamp)

The date of the notification.

event -> (string)

The event for which a notification is sent.

message -> (string)

The message included in the notification.

error -> (boolean)

The Boolean value that specifies whether the notification represents an error.

snsTopicArn -> (string)

The SNS topic to which the SNS notification is sent.

snsPublishStatusCode -> (string)

The status code of the SNS notification.

findingCounts -> (map)

Provides a total count of generated findings per severity.

key -> (string)

value -> (integer)

failedItems -> (map)

Assessment run details that cannot be described. An error code is provided for each failed item.

key -> (string)

value -> (structure)

Includes details about the failed items.

failureCode -> (string)

The status code of a failed item.

retryable -> (boolean)

Indicates whether you can immediately retry a request for this item for a specified resource.