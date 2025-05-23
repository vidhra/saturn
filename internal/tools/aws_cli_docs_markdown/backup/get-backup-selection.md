# get-backup-selectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-selection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/get-backup-selection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# get-backup-selection

## Description

Returns selection metadata and a document in JSON format that specifies a list of resources that are associated with a backup plan.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/GetBackupSelection)

## Synopsis

```
get-backup-selection
--backup-plan-id <value>
--selection-id <value>
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

`--backup-plan-id` (string)

Uniquely identifies a backup plan.

`--selection-id` (string)

Uniquely identifies the body of a request to assign a set of resources to a backup plan.

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

BackupSelection -> (structure)

Specifies the body of a request to assign a set of resources to a backup plan.

SelectionName -> (string)

The display name of a resource selection document. Must contain 1 to 50 alphanumeric or â-_.â characters.

IamRoleArn -> (string)

The ARN of the IAM role that Backup uses to authenticate when backing up the target resource; for example, `arn:aws:iam::123456789012:role/S3Access` .

Resources -> (list)

The Amazon Resource Names (ARNs) of the resources to assign to a backup plan. The maximum number of ARNs is 500 without wildcards, or 30 ARNs with wildcards.

If you need to assign many resources to a backup plan, consider a different resource selection strategy, such as assigning all resources of a resource type or refining your resource selection using tags.

If you specify multiple ARNs, the resources much match any of the ARNs (OR logic).

(string)

ListOfTags -> (list)

The conditions that you define to assign resources to your backup plans using tags. For example, `"StringEquals": { "ConditionKey": "backup", "ConditionValue": "daily"}` .

`ListOfTags` supports only `StringEquals` . Condition operators are case sensitive.

If you specify multiple conditions, the resources much match any of the conditions (OR logic).

(structure)

Contains an array of triplets made up of a condition type (such as `StringEquals` ), a key, and a value. Used to filter resources using their tags and assign them to a backup plan. Case sensitive.

ConditionType -> (string)

An operation applied to a key-value pair used to assign resources to your backup plan. Condition only supports `StringEquals` . For more flexible assignment options, including `StringLike` and the ability to exclude resources from your backup plan, use `Conditions` (with an âsâ on the end) for your ` `BackupSelection` [https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupSelection](https://docs.aws.amazon.com/aws-backup/latest/devguide/API_BackupSelection).html`__ .

ConditionKey -> (string)

The key in a key-value pair. For example, in the tag `Department: Accounting` , `Department` is the key.

ConditionValue -> (string)

The value in a key-value pair. For example, in the tag `Department: Accounting` , `Accounting` is the value.

NotResources -> (list)

The Amazon Resource Names (ARNs) of the resources to exclude from a backup plan. The maximum number of ARNs is 500 without wildcards, or 30 ARNs with wildcards.

If you need to exclude many resources from a backup plan, consider a different resource selection strategy, such as assigning only one or a few resource types or refining your resource selection using tags.

(string)

Conditions -> (structure)

The conditions that you define to assign resources to your backup plans using tags. For example, `"StringEquals": { "ConditionKey": "aws:ResourceTag/backup", "ConditionValue": "daily" }` .

`Conditions` supports `StringEquals` , `StringLike` , `StringNotEquals` , and `StringNotLike` . Condition operators are case sensitive.

If you specify multiple conditions, the resources much match all conditions (AND logic).

StringEquals -> (list)

Filters the values of your tagged resources for only those resources that you tagged with the same value. Also called âexact matching.â

(structure)

Includes information about tags you define to assign tagged resources to a backup plan.

Include the prefix `aws:ResourceTag` in your tags. For example, `"aws:ResourceTag/TagKey1": "Value1"` .

ConditionKey -> (string)

The key in a key-value pair. For example, in the tag `Department: Accounting` , `Department` is the key.

ConditionValue -> (string)

The value in a key-value pair. For example, in the tag `Department: Accounting` , `Accounting` is the value.

StringNotEquals -> (list)

Filters the values of your tagged resources for only those resources that you tagged that do not have the same value. Also called ânegated matching.â

(structure)

Includes information about tags you define to assign tagged resources to a backup plan.

Include the prefix `aws:ResourceTag` in your tags. For example, `"aws:ResourceTag/TagKey1": "Value1"` .

ConditionKey -> (string)

The key in a key-value pair. For example, in the tag `Department: Accounting` , `Department` is the key.

ConditionValue -> (string)

The value in a key-value pair. For example, in the tag `Department: Accounting` , `Accounting` is the value.

StringLike -> (list)

Filters the values of your tagged resources for matching tag values with the use of a wildcard character (*) anywhere in the string. For example, âprod*â or â*rod*â matches the tag value âproductionâ.

(structure)

Includes information about tags you define to assign tagged resources to a backup plan.

Include the prefix `aws:ResourceTag` in your tags. For example, `"aws:ResourceTag/TagKey1": "Value1"` .

ConditionKey -> (string)

The key in a key-value pair. For example, in the tag `Department: Accounting` , `Department` is the key.

ConditionValue -> (string)

The value in a key-value pair. For example, in the tag `Department: Accounting` , `Accounting` is the value.

StringNotLike -> (list)

Filters the values of your tagged resources for non-matching tag values with the use of a wildcard character (*) anywhere in the string.

(structure)

Includes information about tags you define to assign tagged resources to a backup plan.

Include the prefix `aws:ResourceTag` in your tags. For example, `"aws:ResourceTag/TagKey1": "Value1"` .

ConditionKey -> (string)

The key in a key-value pair. For example, in the tag `Department: Accounting` , `Department` is the key.

ConditionValue -> (string)

The value in a key-value pair. For example, in the tag `Department: Accounting` , `Accounting` is the value.

SelectionId -> (string)

Uniquely identifies the body of a request to assign a set of resources to a backup plan.

BackupPlanId -> (string)

Uniquely identifies a backup plan.

CreationDate -> (timestamp)

The date and time a backup selection is created, in Unix format and Coordinated Universal Time (UTC). The value of `CreationDate` is accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

CreatorRequestId -> (string)

A unique string that identifies the request and allows failed requests to be retried without the risk of running the operation twice.