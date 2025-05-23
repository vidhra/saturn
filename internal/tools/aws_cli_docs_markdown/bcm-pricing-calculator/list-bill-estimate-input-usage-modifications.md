# list-bill-estimate-input-usage-modificationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/list-bill-estimate-input-usage-modifications.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/list-bill-estimate-input-usage-modifications.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bcm-pricing-calculator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/index.html#cli-aws-bcm-pricing-calculator) ]

# list-bill-estimate-input-usage-modifications

## Description

Lists the input usage modifications associated with a bill estimate.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bcm-pricing-calculator-2024-06-19/ListBillEstimateInputUsageModifications)

`list-bill-estimate-input-usage-modifications` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `items`

## Synopsis

```
list-bill-estimate-input-usage-modifications
--bill-estimate-id <value>
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--bill-estimate-id` (string)

The unique identifier of the bill estimate to list input usage modifications for.

`--filters` (list)

Filters to apply to the list of input usage modifications.

(structure)

Represents a filter for listing usage data.

name -> (string)

The name of the filter attribute.

values -> (list)

The values to filter by.

(string)

matchOption -> (string)

The match option for the filter (e.g., equals, contains).

Shorthand Syntax:

```
name=string,values=string,string,matchOption=string ...
```

JSON Syntax:

```
[
  {
    "name": "USAGE_ACCOUNT_ID"|"SERVICE_CODE"|"USAGE_TYPE"|"OPERATION"|"LOCATION"|"USAGE_GROUP"|"HISTORICAL_USAGE_ACCOUNT_ID"|"HISTORICAL_SERVICE_CODE"|"HISTORICAL_USAGE_TYPE"|"HISTORICAL_OPERATION"|"HISTORICAL_LOCATION",
    "values": ["string", ...],
    "matchOption": "EQUALS"|"STARTS_WITH"|"CONTAINS"
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

items -> (list)

The list of input usage modifications associated with the bill estimate.

(structure)

Summarizes an input usage modification for a bill estimate.

serviceCode -> (string)

The Amazon Web Services service code for this usage modification.

usageType -> (string)

The type of usage being modified.

operation -> (string)

The specific operation associated with this usage modification.

location -> (string)

The location associated with this usage modification.

availabilityZone -> (string)

The availability zone associated with this usage modification, if applicable.

id -> (string)

The unique identifier of the usage modification.

group -> (string)

The group identifier for the usage modification.

usageAccountId -> (string)

The Amazon Web Services account ID associated with this usage modification.

quantities -> (list)

The modified usage quantities.

(structure)

Represents a usage quantity with associated unit and time period.

startHour -> (timestamp)

The start hour of the usage period.

unit -> (string)

The unit of measurement for the usage quantity.

amount -> (double)

The numeric value of the usage quantity.

historicalUsage -> (structure)

Historical usage data associated with this modification, if available.

serviceCode -> (string)

The Amazon Web Services service code associated with the usage.

usageType -> (string)

The type of usage.

operation -> (string)

The specific operation associated with the usage.

location -> (string)

The location associated with the usage.

usageAccountId -> (string)

The Amazon Web Services account ID associated with the usage.

billInterval -> (structure)

The time interval for the historical usage data.

start -> (timestamp)

The start date and time of the interval.

end -> (timestamp)

The end date and time of the interval.

filterExpression -> (structure)

An optional filter expression to apply to the historical usage data.

and -> (list)

A list of expressions to be combined with AND logic.

(structure)

Represents a complex filtering expression for cost and usage data.

and -> (list)

A list of expressions to be combined with AND logic.

( â¦ recursive â¦ )

or -> (list)

A list of expressions to be combined with OR logic.

( â¦ recursive â¦ )

( â¦ recursive â¦ )costCategories -> (structure)

Filters based on cost categories.

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

dimensions -> (structure)

Filters based on dimensions (e.g., service, operation).

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

tags -> (structure)

Filters based on resource tags.

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

or -> (list)

A list of expressions to be combined with OR logic.

(structure)

Represents a complex filtering expression for cost and usage data.

and -> (list)

A list of expressions to be combined with AND logic.

( â¦ recursive â¦ )

or -> (list)

A list of expressions to be combined with OR logic.

( â¦ recursive â¦ )

( â¦ recursive â¦ )costCategories -> (structure)

Filters based on cost categories.

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

dimensions -> (structure)

Filters based on dimensions (e.g., service, operation).

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

tags -> (structure)

Filters based on resource tags.

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

not -> (structure)

An expression to be negated.

and -> (list)

A list of expressions to be combined with AND logic.

( â¦ recursive â¦ )

or -> (list)

A list of expressions to be combined with OR logic.

( â¦ recursive â¦ )

( â¦ recursive â¦ )costCategories -> (structure)

Filters based on cost categories.

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

dimensions -> (structure)

Filters based on dimensions (e.g., service, operation).

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

tags -> (structure)

Filters based on resource tags.

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

costCategories -> (structure)

Filters based on cost categories.

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

dimensions -> (structure)

Filters based on dimensions (e.g., service, operation).

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

tags -> (structure)

Filters based on resource tags.

key -> (string)

The key or attribute to filter on.

matchOptions -> (list)

The match options for the filter (e.g., equals, contains).

(string)

values -> (list)

The values to match against.

(string)

nextToken -> (string)

A token to retrieve the next page of results, if any.