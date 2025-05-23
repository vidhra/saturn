# start-experimentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/start-experiment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/start-experiment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/index.html#cli-aws-fis) ]

# start-experiment

## Description

Starts running an experiment from the specified experiment template.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fis-2020-12-01/StartExperiment)

## Synopsis

```
start-experiment
[--client-token <value>]
--experiment-template-id <value>
[--experiment-options <value>]
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

`--client-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--experiment-template-id` (string)

The ID of the experiment template.

`--experiment-options` (structure)

The experiment options for running the experiment.

actionsMode -> (string)

Specifies the actions mode for experiment options.

Shorthand Syntax:

```
actionsMode=string
```

JSON Syntax:

```
{
  "actionsMode": "skip-all"|"run-all"
}
```

`--tags` (map)

The tags to apply to the experiment.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

**To start an experiment**

The following `start-experiment` example starts the specified experiment.

```
aws fis start-experiment \
    --experiment-template-id ABCDE1fgHIJkLmNop
```

Output:

```
{
    "experiment": {
        "id": "ABC12DeFGhI3jKLMNOP",
        "experimentTemplateId": "ABCDE1fgHIJkLmNop",
        "roleArn": "arn:aws:iam::123456789012:role/myRole",
        "state": {
            "status": "initiating",
            "reason": "Experiment is initiating."
        },
        "targets": {
            "Instances-Target-1": {
                "resourceType": "aws:ec2:instance",
                "resourceArns": [
                    "arn:aws:ec2:us-west-2:123456789012:instance/i-12a3b4c56d78e9012"
                ],
                "selectionMode": "ALL"
            }
        },
        "actions": {
            "reboot": {
                "actionId": "aws:ec2:reboot-instances",
                "parameters": {},
                "targets": {
                    "Instances": "Instances-Target-1"
                },
                "state": {
                    "status": "pending",
                    "reason": "Initial state"
                }
            }
        },
        "stopConditions": [
            {
                "source": "none"
            }
        ],
        "creationTime": 1616432464.025,
        "startTime": 1616432464.374,
        "tags": {}
    }
}
```

For more information, see [Experiments for AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/experiments.html) in the *AWS Fault Injection Simulator User Guide*.

## Output

experiment -> (structure)

Information about the experiment.

id -> (string)

The ID of the experiment.

arn -> (string)

The Amazon Resource Name (ARN) of the experiment.

experimentTemplateId -> (string)

The ID of the experiment template.

roleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf.

state -> (structure)

The state of the experiment.

status -> (string)

The state of the experiment.

reason -> (string)

The reason for the state.

error -> (structure)

The error information of the experiment when the action has `failed` .

accountId -> (string)

The Amazon Web Services Account ID where the experiment failure occurred.

code -> (string)

The error code for the failed experiment.

location -> (string)

Context for the section of the experiment template that failed.

targets -> (map)

The targets for the experiment.

key -> (string)

value -> (structure)

Describes a target for an experiment.

resourceType -> (string)

The resource type.

resourceArns -> (list)

The Amazon Resource Names (ARNs) of the resources.

(string)

resourceTags -> (map)

The tags for the target resources.

key -> (string)

value -> (string)

filters -> (list)

The filters to apply to identify target resources using specific attributes.

(structure)

Describes a filter used for the target resources in an experiment.

path -> (string)

The attribute path for the filter.

values -> (list)

The attribute values for the filter.

(string)

selectionMode -> (string)

Scopes the identified resources to a specific count or percentage.

parameters -> (map)

The resource type parameters.

key -> (string)

value -> (string)

actions -> (map)

The actions for the experiment.

key -> (string)

value -> (structure)

Describes the action for an experiment.

actionId -> (string)

The ID of the action.

description -> (string)

The description for the action.

parameters -> (map)

The parameters for the action.

key -> (string)

value -> (string)

targets -> (map)

The targets for the action.

key -> (string)

value -> (string)

startAfter -> (list)

The name of the action that must be completed before this action starts.

(string)

state -> (structure)

The state of the action.

status -> (string)

The state of the action.

reason -> (string)

The reason for the state.

startTime -> (timestamp)

The time that the action started.

endTime -> (timestamp)

The time that the action ended.

stopConditions -> (list)

The stop conditions for the experiment.

(structure)

Describes the stop condition for an experiment.

source -> (string)

The source for the stop condition.

value -> (string)

The Amazon Resource Name (ARN) of the CloudWatch alarm, if applicable.

creationTime -> (timestamp)

The time that the experiment was created.

startTime -> (timestamp)

The time that the experiment started.

endTime -> (timestamp)

The time that the experiment ended.

tags -> (map)

The tags for the experiment.

key -> (string)

value -> (string)

logConfiguration -> (structure)

The configuration for experiment logging.

cloudWatchLogsConfiguration -> (structure)

The configuration for experiment logging to Amazon CloudWatch Logs.

logGroupArn -> (string)

The Amazon Resource Name (ARN) of the destination Amazon CloudWatch Logs log group.

s3Configuration -> (structure)

The configuration for experiment logging to Amazon S3.

bucketName -> (string)

The name of the destination bucket.

prefix -> (string)

The bucket prefix.

logSchemaVersion -> (integer)

The schema version.

experimentOptions -> (structure)

The experiment options for the experiment.

accountTargeting -> (string)

The account targeting setting for an experiment.

emptyTargetResolutionMode -> (string)

The empty target resolution mode for an experiment.

actionsMode -> (string)

The actions mode of the experiment that is set from the StartExperiment API command.

targetAccountConfigurationsCount -> (long)

The count of target account configurations for the experiment.

experimentReportConfiguration -> (structure)

The experiment report configuration for the experiment.

outputs -> (structure)

The output destinations of the experiment report.

s3Configuration -> (structure)

The S3 destination for the experiment report.

bucketName -> (string)

The name of the S3 bucket where the experiment report will be stored.

prefix -> (string)

The prefix of the S3 bucket where the experiment report will be stored.

dataSources -> (structure)

The data sources for the experiment report.

cloudWatchDashboards -> (list)

The CloudWatch dashboards to include as data sources in the experiment report.

(structure)

Specifies the CloudWatch dashboard to include in the experiment report. The dashboard widgets will be captured as snapshot graphs within the report.

dashboardIdentifier -> (string)

The Amazon Resource Name (ARN) of the CloudWatch dashboard to include in the experiment report.

preExperimentDuration -> (string)

The duration before the experiment start time for the data sources to include in the report.

postExperimentDuration -> (string)

The duration after the experiment end time for the data sources to include in the report.

experimentReport -> (structure)

The experiment report for the experiment.

state -> (structure)

The state of the experiment report.

status -> (string)

The state of the experiment report generation.

reason -> (string)

The reason for the state of the experiment report generation.

error -> (structure)

The error information of the experiment when the experiment report generation has failed.

code -> (string)

The error code for the failed experiment report generation.

s3Reports -> (list)

The S3 destination of the experiment report.

(structure)

Describes the S3 destination for the report.

arn -> (string)

The Amazon Resource Name (ARN) of the generated report.

reportType -> (string)

The report type for the experiment report.