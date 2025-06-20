# get-restore-testing-planÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-restore-testing-plan.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-restore-testing-plan.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# get-restore-testing-plan

## Description

Returns `RestoreTestingPlan` details for the specified `RestoreTestingPlanName` . The details are the body of a restore testing plan in JSON format, in addition to plan metadata.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetRestoreTestingPlan)

## Synopsis

```
get-restore-testing-plan
--restore-testing-plan-name <value>
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

`--restore-testing-plan-name` (string)

Required unique name of the restore testing plan.

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

RestoreTestingPlan -> (structure)

Specifies the body of a restore testing plan. Includes `RestoreTestingPlanName` .

CreationTime -> (timestamp)

The date and time that a restore testing plan was created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CreatorRequestId -> (string)

This identifies the request and allows failed requests to be retried without the risk of running the operation twice. If the request includes a `CreatorRequestId` that matches an existing backup plan, that plan is returned. This parameter is optional.

If used, this parameter must contain 1 to 50 alphanumeric or â-_.â characters.

LastExecutionTime -> (timestamp)

The last time a restore test was run with the specified restore testing plan. A date and time, in Unix format and Coordinated Universal Time (UTC). The value of `LastExecutionDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

LastUpdateTime -> (timestamp)

The date and time that the restore testing plan was updated. This update is in Unix format and Coordinated Universal Time (UTC). The value of `LastUpdateTime` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

RecoveryPointSelection -> (structure)

The specified criteria to assign a set of resources, such as recovery point types or backup vaults.

Algorithm -> (string)

Acceptable values include âLATEST_WITHIN_WINDOWâ or âRANDOM_WITHIN_WINDOWâ

ExcludeVaults -> (list)

Accepted values include specific ARNs or list of selectors. Defaults to empty list if not listed.

(string)

IncludeVaults -> (list)

Accepted values include wildcard [â*â] or by specific ARNs or ARN wilcard replacement [âarn:aws:backup:us-west-2:123456789012:backup-vault:asdfâ, â¦] [âarn:aws:backup:*:*:backup-vault:asdf-[*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-restore-testing-plan.html#id1)â, â¦]

(string)

RecoveryPointTypes -> (list)

These are the types of recovery points.

Include `SNAPSHOT` to restore only snapshot recovery points; include `CONTINUOUS` to restore continuous recovery points (point in time restore / PITR); use both to restore either a snapshot or a continuous recovery point. The recovery point will be determined by the value for `Algorithm` .

(string)

SelectionWindowDays -> (integer)

Accepted values are integers from 1 to 365.

RestoreTestingPlanArn -> (string)

An Amazon Resource Name (ARN) that uniquely identifies a restore testing plan.

RestoreTestingPlanName -> (string)

The restore testing plan name.

ScheduleExpression -> (string)

A CRON expression in specified timezone when a restore testing plan is executed.

ScheduleExpressionTimezone -> (string)

Optional. This is the timezone in which the schedule expression is set. By default, ScheduleExpressions are in UTC. You can modify this to a specified timezone.

StartWindowHours -> (integer)

Defaults to 24 hours.

A value in hours after a restore test is scheduled before a job will be canceled if it doesnât start successfully. This value is optional. If this value is included, this parameter has a maximum value of 168 hours (one week).