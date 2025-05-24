# batch-update-workload-estimate-usageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/batch-update-workload-estimate-usage.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/batch-update-workload-estimate-usage.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bcm-pricing-calculator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/index.html#cli-aws-bcm-pricing-calculator) ]

# batch-update-workload-estimate-usage

## Description

Update a newly added or existing usage lines. You can update the usage amounts and usage group based on a usage ID and a Workload estimate ID.

### Note

The `BatchUpdateWorkloadEstimateUsage` operation doesnât have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission `bcm-pricing-calculator:UpdateWorkloadEstimateUsage` in your policies.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bcm-pricing-calculator-2024-06-19/BatchUpdateWorkloadEstimateUsage)

## Synopsis

```
batch-update-workload-estimate-usage
--workload-estimate-id <value>
--usage <value>
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

`--workload-estimate-id` (string)

The ID of the Workload estimate for which you want to modify the usage lines.

`--usage` (list)

List of usage line amounts and usage group that you want to update in a Workload estimate identified by the usage ID.

(structure)

Represents an entry in a batch operation to update workload estimate usage.

id -> (string)

The unique identifier of the usage estimate to update.

group -> (string)

The updated group identifier for the usage estimate.

amount -> (double)

The updated estimated usage amount.

Shorthand Syntax:

```
id=string,group=string,amount=double ...
```

JSON Syntax:

```
[
  {
    "id": "string",
    "group": "string",
    "amount": double
  }
  ...
]
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

items -> (list)

Returns the list of successful usage line items that were updated for a Workload estimate.

(structure)

Represents a usage item in a workload estimate.

serviceCode -> (string)

The Amazon Web Services service code associated with this usage item.

usageType -> (string)

The type of usage for this item.

operation -> (string)

The specific operation associated with this usage item.

location -> (string)

The location associated with this usage item.

id -> (string)

The unique identifier of this usage item.

usageAccountId -> (string)

The Amazon Web Services account ID associated with this usage item.

group -> (string)

The group identifier for this usage item.

quantity -> (structure)

The estimated usage quantity for this item.

unit -> (string)

The unit of measurement for the usage quantity.

amount -> (double)

The numeric value of the usage quantity.

cost -> (double)

The estimated cost for this usage item.

currency -> (string)

The currency of the estimated cost.

status -> (string)

The current status of this usage item.

historicalUsage -> (structure)

Historical usage data associated with this item, if available.

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

errors -> (list)

Returns the list of error reasons and usage line item IDs that could not be updated for the Workload estimate.

(structure)

Represents an error that occurred when updating usage in a workload estimate.

id -> (string)

The ID of the error.

errorMessage -> (string)

The message that describes the error.

errorCode -> (string)

The code associated with the error.