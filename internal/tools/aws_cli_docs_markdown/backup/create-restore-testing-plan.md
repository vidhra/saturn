# create-restore-testing-planÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-plan.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-plan.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# create-restore-testing-plan

## Description

Creates a restore testing plan.

The first of two steps to create a restore testing plan. After this request is successful, finish the procedure using CreateRestoreTestingSelection.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/CreateRestoreTestingPlan)

## Synopsis

```
create-restore-testing-plan
[--creator-request-id <value>]
--restore-testing-plan <value>
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

`--creator-request-id` (string)

This is a unique string that identifies the request and allows failed requests to be retriedwithout the risk of running the operation twice. This parameter is optional. If used, this parameter must contain 1 to 50 alphanumeric or â-_.â characters.

`--restore-testing-plan` (structure)

A restore testing plan must contain a unique `RestoreTestingPlanName` string you create and must contain a `ScheduleExpression` cron. You may optionally include a `StartWindowHours` integer and a `CreatorRequestId` string.

The `RestoreTestingPlanName` is a unique string that is the name of the restore testing plan. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.

RecoveryPointSelection -> (structure)

`RecoveryPointSelection` has five parameters (three required and two optional). The values you specify determine which recovery point is included in the restore test. You must indicate with `Algorithm` if you want the latest recovery point within your `SelectionWindowDays` or if you want a random recovery point, and you must indicate through `IncludeVaults` from which vaults the recovery points can be chosen.

`Algorithm` (*required* ) Valid values: â`LATEST_WITHIN_WINDOW` â or â`RANDOM_WITHIN_WINDOW` â.

`Recovery point types` (*required* ) Valid values: â`SNAPSHOT` â and/or â`CONTINUOUS` â. Include `SNAPSHOT` to restore only snapshot recovery points; include `CONTINUOUS` to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for `Algorithm` .

`IncludeVaults` (*required* ). You must include one or more backup vaults. Use the wildcard [â*â] or specific ARNs.

`SelectionWindowDays` (*optional* ) Value must be an integer (in days) from 1 to 365. If not included, the value defaults to `30` .

`ExcludeVaults` (*optional* ). You can choose to input one or more specific backup vault ARNs to exclude those vaultsâ contents from restore eligibility. Or, you can include a list of selectors. If this parameter and its value are not included, it defaults to empty list.

Algorithm -> (string)

Acceptable values include âLATEST_WITHIN_WINDOWâ or âRANDOM_WITHIN_WINDOWâ

ExcludeVaults -> (list)

Accepted values include specific ARNs or list of selectors. Defaults to empty list if not listed.

(string)

IncludeVaults -> (list)

Accepted values include wildcard [â*â] or by specific ARNs or ARN wilcard replacement [âarn:aws:backup:us-west-2:123456789012:backup-vault:asdfâ, â¦] [âarn:aws:backup:*:*:backup-vault:asdf-[*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/create-restore-testing-plan.html#id1)â, â¦]

(string)

RecoveryPointTypes -> (list)

These are the types of recovery points.

Include `SNAPSHOT` to restore only snapshot recovery points; include `CONTINUOUS` to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for `Algorithm` .

(string)

SelectionWindowDays -> (integer)

Accepted values are integers from 1 to 365.

RestoreTestingPlanName -> (string)

The RestoreTestingPlanName is a unique string that is the name of the restore testing plan. This cannot be changed after creation, and it must consist of only alphanumeric characters and underscores.

ScheduleExpression -> (string)

A CRON expression in specified timezone when a restore testing plan is executed.

ScheduleExpressionTimezone -> (string)

Optional. This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.

StartWindowHours -> (integer)

Defaults to 24 hours.

A value in hours after a restore test is scheduled before a job will be canceled if it doesnât start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).

Shorthand Syntax:

```
RecoveryPointSelection={Algorithm=string,ExcludeVaults=[string,string],IncludeVaults=[string,string],RecoveryPointTypes=[string,string],SelectionWindowDays=integer},RestoreTestingPlanName=string,ScheduleExpression=string,ScheduleExpressionTimezone=string,StartWindowHours=integer
```

JSON Syntax:

```
{
  "RecoveryPointSelection": {
    "Algorithm": "LATEST_WITHIN_WINDOW"|"RANDOM_WITHIN_WINDOW",
    "ExcludeVaults": ["string", ...],
    "IncludeVaults": ["string", ...],
    "RecoveryPointTypes": ["CONTINUOUS"|"SNAPSHOT", ...],
    "SelectionWindowDays": integer
  },
  "RestoreTestingPlanName": "string",
  "ScheduleExpression": "string",
  "ScheduleExpressionTimezone": "string",
  "StartWindowHours": integer
}
```

`--tags` (map)

The tags to assign to the restore testing plan.

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

## Output

CreationTime -> (timestamp)

The date and time a restore testing plan was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087AM.

RestoreTestingPlanArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies the created restore testing plan.

RestoreTestingPlanName -> (string)

This unique string is the name of the restore testing plan.

The name cannot be changed after creation. The name consists of only alphanumeric characters and underscores. Maximum length is 50.