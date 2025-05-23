# describe-rulesetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-ruleset.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/describe-ruleset.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [databrew](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/databrew/index.html#cli-aws-databrew) ]

# describe-ruleset

## Description

Retrieves detailed information about the ruleset.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/databrew-2017-07-25/DescribeRuleset)

## Synopsis

```
describe-ruleset
--name <value>
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

`--name` (string)

The name of the ruleset to be described.

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

Name -> (string)

The name of the ruleset.

Description -> (string)

The description of the ruleset.

TargetArn -> (string)

The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is associated with.

Rules -> (list)

A list of rules that are defined with the ruleset. A rule includes one or more checks to be validated on a DataBrew dataset.

(structure)

Represents a single data quality requirement that should be validated in the scope of this dataset.

Name -> (string)

The name of the rule.

Disabled -> (boolean)

A value that specifies whether the rule is disabled. Once a rule is disabled, a profile job will not validate it during a job run. Default value is false.

CheckExpression -> (string)

The expression which includes column references, condition names followed by variable references, possibly grouped and combined with other conditions. For example, `(:col1 starts_with :prefix1 or :col1 starts_with :prefix2) and (:col1 ends_with :suffix1 or :col1 ends_with :suffix2)` . Column and value references are substitution variables that should start with the â:â symbol. Depending on the context, substitution variablesâ values can be either an actual value or a column name. These values are defined in the SubstitutionMap. If a CheckExpression starts with a column reference, then ColumnSelectors in the rule should be null. If ColumnSelectors has been defined, then there should be no column reference in the left side of a condition, for example, `is_between :val1 and :val2` .

For more information, see [Available checks](https://docs.aws.amazon.com/databrew/latest/dg/profile.data-quality-available-checks.html)

SubstitutionMap -> (map)

The map of substitution variable names to their values used in a check expression. Variable names should start with a â:â (colon). Variable values can either be actual values or column names. To differentiate between the two, column names should be enclosed in backticks, for example, `":col1": "`Column A`".`

key -> (string)

value -> (string)

Threshold -> (structure)

The threshold used with a non-aggregate check expression. Non-aggregate check expressions will be applied to each row in a specific column, and the threshold will be used to determine whether the validation succeeds.

Value -> (double)

The value of a threshold.

Type -> (string)

The type of a threshold. Used for comparison of an actual count of rows that satisfy the rule to the threshold value.

Unit -> (string)

Unit of threshold value. Can be either a COUNT or PERCENTAGE of the full sample size used for validation.

ColumnSelectors -> (list)

List of column selectors. Selectors can be used to select columns using a name or regular expression from the dataset. Rule will be applied to selected columns.

(structure)

Selector of a column from a dataset for profile job configuration. One selector includes either a column name or a regular expression.

Regex -> (string)

A regular expression for selecting a column from a dataset.

Name -> (string)

The name of a column from a dataset.

CreateDate -> (timestamp)

The date and time that the ruleset was created.

CreatedBy -> (string)

The Amazon Resource Name (ARN) of the user who created the ruleset.

LastModifiedBy -> (string)

The Amazon Resource Name (ARN) of the user who last modified the ruleset.

LastModifiedDate -> (timestamp)

The modification date and time of the ruleset.

ResourceArn -> (string)

The Amazon Resource Name (ARN) for the ruleset.

Tags -> (map)

Metadata tags that have been applied to the ruleset.

key -> (string)

value -> (string)