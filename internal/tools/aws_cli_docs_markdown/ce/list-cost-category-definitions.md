# list-cost-category-definitionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-cost-category-definitions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/list-cost-category-definitions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ce](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html#cli-aws-ce) ]

# list-cost-category-definitions

## Description

Returns the name, Amazon Resource Name (ARN), `NumberOfRules` and effective dates of all Cost Categories defined in the account. You have the option to use `EffectiveOn` to return a list of Cost Categories that were active on a specific date. If there is no `EffectiveOn` specified, youâll see Cost Categories that are effective on the current date. If Cost Category is still effective, `EffectiveEnd` is omitted in the response. `ListCostCategoryDefinitions` supports pagination. The request can have a `MaxResults` range up to 100.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/ListCostCategoryDefinitions)

## Synopsis

```
list-cost-category-definitions
[--effective-on <value>]
[--next-token <value>]
[--max-results <value>]
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

`--effective-on` (string)

The date when the Cost Category was effective.

`--next-token` (string)

The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.

`--max-results` (integer)

The number of entries a paginated response contains.

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

CostCategoryReferences -> (list)

A reference to a Cost Category that contains enough information to identify the Cost Category.

(structure)

A reference to a Cost Category containing only enough information to identify the Cost Category.

You can use this information to retrieve the full Cost Category information using `DescribeCostCategory` .

CostCategoryArn -> (string)

The unique identifier for your Cost Category.

Name -> (string)

The unique name of the Cost Category.

EffectiveStart -> (string)

The Cost Categoryâs effective start date.

EffectiveEnd -> (string)

The Cost Categoryâs effective end date.

NumberOfRules -> (integer)

The number of rules that are associated with a specific Cost Category.

ProcessingStatus -> (list)

The list of processing statuses for Cost Management products for a specific cost category.

(structure)

The list of processing statuses for Cost Management products for a specific cost category.

Component -> (string)

The Cost Management product name of the applied status.

Status -> (string)

The process status for a specific cost category.

Values -> (list)

A list of unique cost category values in a specific cost category.

(string)

The default value for the cost category.

DefaultValue -> (string)

The default value for the cost category.

NextToken -> (string)

The token to retrieve the next set of results. Amazon Web Services provides the token when the response from a previous call has more results than the maximum page size.