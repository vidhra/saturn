# get-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/get-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/get-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rbin](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rbin/index.html#cli-aws-rbin) ]

# get-rule

## Description

Gets information about a Recycle Bin retention rule.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rbin-2021-06-15/GetRule)

## Synopsis

```
get-rule
--identifier <value>
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

`--identifier` (string)

The unique ID of the retention rule.

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

Identifier -> (string)

The unique ID of the retention rule.

Description -> (string)

The retention rule description.

ResourceType -> (string)

The resource type retained by the retention rule.

RetentionPeriod -> (structure)

Information about the retention period for which the retention rule is to retain resources.

RetentionPeriodValue -> (integer)

The period value for which the retention rule is to retain resources. The period is measured using the unit specified for **RetentionPeriodUnit** .

RetentionPeriodUnit -> (string)

The unit of time in which the retention period is measured. Currently, only `DAYS` is supported.

ResourceTags -> (list)

[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.

(structure)

[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.

ResourceTagKey -> (string)

The tag key.

ResourceTagValue -> (string)

The tag value.

Status -> (string)

The state of the retention rule. Only retention rules that are in the `available` state retain resources.

LockConfiguration -> (structure)

Information about the retention rule lock configuration.

UnlockDelay -> (structure)

Information about the retention rule unlock delay.

UnlockDelayValue -> (integer)

The unlock delay period, measured in the unit specified for **UnlockDelayUnit** .

UnlockDelayUnit -> (string)

The unit of time in which to measure the unlock delay. Currently, the unlock delay can be measure only in days.

LockState -> (string)

[Region-level retention rules only] The lock state for the retention rule.

- `locked` - The retention rule is locked and canât be modified or deleted.
- `pending_unlock` - The retention rule has been unlocked but it is still within the unlock delay period. The retention rule can be modified or deleted only after the unlock delay period has expired.
- `unlocked` - The retention rule is unlocked and it can be modified or deleted by any user with the required permissions.
- `null` - The retention rule has never been locked. Once a retention rule has been locked, it can transition between the `locked` and `unlocked` states only; it can never transition back to `null` .

LockEndTime -> (timestamp)

The date and time at which the unlock delay is set to expire. Only returned for retention rules that have been unlocked and that are still within the unlock delay period.

RuleArn -> (string)

The Amazon Resource Name (ARN) of the retention rule.

ExcludeResourceTags -> (list)

[Region-level retention rules only] Information about the exclusion tags used to identify resources that are to be excluded, or ignored, by the retention rule.

(structure)

[Tag-level retention rules only] Information about the resource tags used to identify resources that are retained by the retention rule.

ResourceTagKey -> (string)

The tag key.

ResourceTagValue -> (string)

The tag value.