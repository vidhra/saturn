# apply-pending-maintenance-actionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb-elastic/apply-pending-maintenance-action.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb-elastic/apply-pending-maintenance-action.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [docdb-elastic](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/docdb-elastic/index.html#cli-aws-docdb-elastic) ]

# apply-pending-maintenance-action

## Description

The type of pending maintenance action to be applied to the resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/docdb-elastic-2022-11-28/ApplyPendingMaintenanceAction)

## Synopsis

```
apply-pending-maintenance-action
--apply-action <value>
[--apply-on <value>]
--opt-in-type <value>
--resource-arn <value>
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

`--apply-action` (string)

The pending maintenance action to apply to the resource.

Valid actions are:

- `ENGINE_UPDATE`
- `ENGINE_UPGRADE`
- `SECURITY_UPDATE`
- `OS_UPDATE`
- `MASTER_USER_PASSWORD_UPDATE`

`--apply-on` (string)

A specific date to apply the pending maintenance action. Required if opt-in-type is `APPLY_ON` . Format: `yyyy/MM/dd HH:mm-yyyy/MM/dd HH:mm`

`--opt-in-type` (string)

A value that specifies the type of opt-in request, or undoes an opt-in request. An opt-in request of type `IMMEDIATE` canât be undone.

Possible values:

- `IMMEDIATE`
- `NEXT_MAINTENANCE`
- `APPLY_ON`
- `UNDO_OPT_IN`

`--resource-arn` (string)

The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.

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

resourcePendingMaintenanceAction -> (structure)

The output of the pending maintenance action being applied.

pendingMaintenanceActionDetails -> (list)

Provides information about a pending maintenance action for a resource.

(structure)

Retrieves the details of maintenance actions that are pending.

action -> (string)

Displays the specific action of a pending maintenance action.

autoAppliedAfterDate -> (string)

Displays the date of the maintenance window when the action is applied. The maintenance action is applied to the resource during its first maintenance window after this date. If this date is specified, any `NEXT_MAINTENANCE` `optInType` requests are ignored.

currentApplyDate -> (string)

Displays the effective date when the pending maintenance action is applied to the resource.

description -> (string)

Displays a description providing more detail about the maintenance action.

forcedApplyDate -> (string)

Displays the date when the maintenance action is automatically applied. The maintenance action is applied to the resource on this date regardless of the maintenance window for the resource. If this date is specified, any `IMMEDIATE` `optInType` requests are ignored.

optInStatus -> (string)

Displays the type of `optInType` request that has been received for the resource.

resourceArn -> (string)

The Amazon DocumentDB Amazon Resource Name (ARN) of the resource to which the pending maintenance action applies.