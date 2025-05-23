# create-experiment-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [fis](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/index.html#cli-aws-fis) ]

# create-experiment-template

## Description

Creates an experiment template.

An experiment template includes the following components:

- **Targets** : A target can be a specific resource in your Amazon Web Services environment, or one or more resources that match criteria that you specify, for example, resources that have specific tags.
- **Actions** : The actions to carry out on the target. You can specify multiple actions, the duration of each action, and when to start each action during an experiment.
- **Stop conditions** : If a stop condition is triggered while an experiment is running, the experiment is automatically stopped. You can define a stop condition as a CloudWatch alarm.

For more information, see [experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html) in the *Fault Injection Service User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/fis-2020-12-01/CreateExperimentTemplate)

## Synopsis

```
create-experiment-template
[--client-token <value>]
--description <value>
--stop-conditions <value>
[--targets <value>]
--actions <value>
--role-arn <value>
[--tags <value>]
[--log-configuration <value>]
[--experiment-options <value>]
[--experiment-report-configuration <value>]
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

`--description` (string)

A description for the experiment template.

`--stop-conditions` (list)

The stop conditions.

(structure)

Specifies a stop condition for an experiment template.

source -> (string)

The source for the stop condition. Specify `aws:cloudwatch:alarm` if the stop condition is defined by a CloudWatch alarm. Specify `none` if there is no stop condition.

value -> (string)

The Amazon Resource Name (ARN) of the CloudWatch alarm. This is required if the source is a CloudWatch alarm.

Shorthand Syntax:

```
source=string,value=string ...
```

JSON Syntax:

```
[
  {
    "source": "string",
    "value": "string"
  }
  ...
]
```

`--targets` (map)

The targets for the experiment.

key -> (string)

value -> (structure)

Specifies a target for an experiment. You must specify at least one Amazon Resource Name (ARN) or at least one resource tag. You cannot specify both ARNs and tags.

For more information, see [Targets](https://docs.aws.amazon.com/fis/latest/userguide/targets.html) in the *Fault Injection Service User Guide* .

resourceType -> (string)

The resource type. The resource type must be supported for the specified action.

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

Specifies a filter used for the target resource input in an experiment template.

For more information, see [Resource filters](https://docs.aws.amazon.com/fis/latest/userguide/targets.html#target-filters) in the *Fault Injection Service User Guide* .

path -> (string)

The attribute path for the filter.

values -> (list)

The attribute values for the filter.

(string)

selectionMode -> (string)

Scopes the identified resources to a specific count of the resources at random, or a percentage of the resources. All identified resources are included in the target.

- ALL - Run the action on all identified targets. This is the default.
- COUNT(n) - Run the action on the specified number of targets, chosen from the identified targets at random. For example, COUNT(1) selects one of the targets.
- PERCENT(n) - Run the action on the specified percentage of targets, chosen from the identified targets at random. For example, PERCENT(25) selects 25% of the targets.

parameters -> (map)

The resource type parameters.

key -> (string)

value -> (string)

JSON Syntax:

```
{"string": {
      "resourceType": "string",
      "resourceArns": ["string", ...],
      "resourceTags": {"string": "string"
        ...},
      "filters": [
        {
          "path": "string",
          "values": ["string", ...]
        }
        ...
      ],
      "selectionMode": "string",
      "parameters": {"string": "string"
        ...}
    }
  ...}
```

`--actions` (map)

The actions for the experiment.

key -> (string)

value -> (structure)

Specifies an action for an experiment template.

For more information, see [Actions](https://docs.aws.amazon.com/fis/latest/userguide/actions.html) in the *Fault Injection Service User Guide* .

actionId -> (string)

The ID of the action. The format of the action ID is: aws:*service-name* :*action-type* .

description -> (string)

A description for the action.

parameters -> (map)

The parameters for the action, if applicable.

key -> (string)

value -> (string)

targets -> (map)

The targets for the action.

key -> (string)

value -> (string)

startAfter -> (list)

The name of the action that must be completed before the current action starts. Omit this parameter to run the action at the start of the experiment.

(string)

Shorthand Syntax:

```
KeyName1=actionId=string,description=string,parameters={KeyName1=string,KeyName2=string},targets={KeyName1=string,KeyName2=string},startAfter=string,string,KeyName2=actionId=string,description=string,parameters={KeyName1=string,KeyName2=string},targets={KeyName1=string,KeyName2=string},startAfter=string,string
```

JSON Syntax:

```
{"string": {
      "actionId": "string",
      "description": "string",
      "parameters": {"string": "string"
        ...},
      "targets": {"string": "string"
        ...},
      "startAfter": ["string", ...]
    }
  ...}
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role that grants the FIS service permission to perform service actions on your behalf.

`--tags` (map)

The tags to apply to the experiment template.

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

`--log-configuration` (structure)

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

Shorthand Syntax:

```
cloudWatchLogsConfiguration={logGroupArn=string},s3Configuration={bucketName=string,prefix=string},logSchemaVersion=integer
```

JSON Syntax:

```
{
  "cloudWatchLogsConfiguration": {
    "logGroupArn": "string"
  },
  "s3Configuration": {
    "bucketName": "string",
    "prefix": "string"
  },
  "logSchemaVersion": integer
}
```

`--experiment-options` (structure)

The experiment options for the experiment template.

accountTargeting -> (string)

Specifies the account targeting setting for experiment options.

emptyTargetResolutionMode -> (string)

Specifies the empty target resolution mode for experiment options.

Shorthand Syntax:

```
accountTargeting=string,emptyTargetResolutionMode=string
```

JSON Syntax:

```
{
  "accountTargeting": "single-account"|"multi-account",
  "emptyTargetResolutionMode": "fail"|"skip"
}
```

`--experiment-report-configuration` (structure)

The experiment report configuration for the experiment template.

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

Specifies the CloudWatch dashboard for the experiment report.

dashboardIdentifier -> (string)

The Amazon Resource Name (ARN) of the CloudWatch dashboard to include in the experiment report.

preExperimentDuration -> (string)

The duration before the experiment start time for the data sources to include in the report.

postExperimentDuration -> (string)

The duration after the experiment end time for the data sources to include in the report.

JSON Syntax:

```
{
  "outputs": {
    "s3Configuration": {
      "bucketName": "string",
      "prefix": "string"
    }
  },
  "dataSources": {
    "cloudWatchDashboards": [
      {
        "dashboardIdentifier": "string"
      }
      ...
    ]
  },
  "preExperimentDuration": "string",
  "postExperimentDuration": "string"
}
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

**To create an experiment template**

The following `create-experiment-template` example creates an experiment template in your AWS FIS account.

```
aws fis create-experiment-template \
    --cli-input-json file://myfile.json
```

Contents of `myfile.json`:

```
{
    "description": "experimentTemplate",
    "stopConditions": [
        {
            "source": "aws:cloudwatch:alarm",
            "value": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:alarmName"
        }
    ],
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
            "description": "reboot",
            "parameters": {},
            "targets": {
                "Instances": "Instances-Target-1"
            }
        }
    },
    "roleArn": "arn:aws:iam::123456789012:role/myRole"
}
```

Output:

```
{
    "experimentTemplate": {
        "id": "ABCDE1fgHIJkLmNop",
        "description": "experimentTemplate",
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
                "description": "reboot",
                "parameters": {},
                "targets": {
                    "Instances": "Instances-Target-1"
                }
            }
        },
        "stopConditions": [
            {
                "source": "aws:cloudwatch:alarm",
                "value": "arn:aws:cloudwatch:us-west-2:123456789012:alarm:alarmName"
            }
        ],
        "creationTime": 1616434850.659,
        "lastUpdateTime": 1616434850.659,
        "roleArn": "arn:aws:iam::123456789012:role/myRole",
        "tags": {}
    }
}
```

For more information, see [Create an experiment template](https://docs.aws.amazon.com/fis/latest/userguide/working-with-templates.html#create-template) in the *AWS Fault Injection Simulator User Guide*.

## Output

experimentTemplate -> (structure)

Information about the experiment template.

id -> (string)

The ID of the experiment template.

arn -> (string)

The Amazon Resource Name (ARN) of the experiment template.

description -> (string)

The description for the experiment template.

targets -> (map)

The targets for the experiment.

key -> (string)

value -> (structure)

Describes a target for an experiment template.

resourceType -> (string)

The resource type.

resourceArns -> (list)

The Amazon Resource Names (ARNs) of the targets.

(string)

resourceTags -> (map)

The tags for the target resources.

key -> (string)

value -> (string)

filters -> (list)

The filters to apply to identify target resources using specific attributes.

(structure)

Describes a filter used for the target resources in an experiment template.

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

Describes an action for an experiment template.

actionId -> (string)

The ID of the action.

description -> (string)

A description for the action.

parameters -> (map)

The parameters for the action.

key -> (string)

value -> (string)

targets -> (map)

The targets for the action.

key -> (string)

value -> (string)

startAfter -> (list)

The name of the action that must be completed before the current action starts.

(string)

stopConditions -> (list)

The stop conditions for the experiment.

(structure)

Describes a stop condition for an experiment template.

source -> (string)

The source for the stop condition.

value -> (string)

The Amazon Resource Name (ARN) of the CloudWatch alarm, if applicable.

creationTime -> (timestamp)

The time the experiment template was created.

lastUpdateTime -> (timestamp)

The time the experiment template was last updated.

roleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role.

tags -> (map)

The tags for the experiment template.

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

The experiment options for an experiment template.

accountTargeting -> (string)

The account targeting setting for an experiment template.

emptyTargetResolutionMode -> (string)

The empty target resolution mode for an experiment template.

targetAccountConfigurationsCount -> (long)

The count of target account configurations for the experiment template.

experimentReportConfiguration -> (structure)

Describes the report configuration for the experiment template.

outputs -> (structure)

Describes the output destinations of the experiment report.

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

The CloudWatch dashboards to include as data sources in the experiment report.

dashboardIdentifier -> (string)

The Amazon Resource Name (ARN) of the CloudWatch dashboard to include in the experiment report.

preExperimentDuration -> (string)

The duration before the experiment start time for the data sources to include in the report.

postExperimentDuration -> (string)

The duration after the experiment end time for the data sources to include in the report.