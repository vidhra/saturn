# batch-create-bill-scenario-usage-modificationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/batch-create-bill-scenario-usage-modification.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/batch-create-bill-scenario-usage-modification.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bcm-pricing-calculator](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bcm-pricing-calculator/index.html#cli-aws-bcm-pricing-calculator) ]

# batch-create-bill-scenario-usage-modification

## Description

Create Amazon Web Services service usage that you want to model in a Bill Scenario.

### Note

The `BatchCreateBillScenarioUsageModification` operation doesnât have its own IAM permission. To authorize this operation for Amazon Web Services principals, include the permission `bcm-pricing-calculator:CreateBillScenarioUsageModification` in your policies.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bcm-pricing-calculator-2024-06-19/BatchCreateBillScenarioUsageModification)

## Synopsis

```
batch-create-bill-scenario-usage-modification
--bill-scenario-id <value>
--usage-modifications <value>
[--client-token <value>]
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

`--bill-scenario-id` (string)

The ID of the Bill Scenario for which you want to create the modeled usage.

`--usage-modifications` (list)

List of usage that you want to model in the Bill Scenario.

(structure)

Represents an entry in a batch operation to create bill scenario usage modifications.

serviceCode -> (string)

The Amazon Web Services service code for this usage modification. This identifies the specific Amazon Web Services service to the customer as a unique short abbreviation. For example, `AmazonEC2` and `AWSKMS` .

usageType -> (string)

Describes the usage details of the usage line item.

operation -> (string)

The specific operation associated with this usage modification. Describes the specific Amazon Web Services operation that this usage line models. For example, `RunInstances` indicates the operation of an Amazon EC2 instance.

availabilityZone -> (string)

The Availability Zone that this usage line uses.

key -> (string)

A unique identifier for this entry in the batch operation. This can be any valid string. This key is useful to identify errors associated with any usage entry as any error is returned with this key.

group -> (string)

An optional group identifier for the usage modification.

usageAccountId -> (string)

The Amazon Web Services account ID to which this usage will be applied to.

amounts -> (list)

The amount of usage you want to create for the service use you are modeling.

(structure)

Represents a usage amount for a specific time period.

startHour -> (timestamp)

The start hour of the usage period.

amount -> (double)

The usage amount for the period.

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

JSON Syntax:

```
[
  {
    "serviceCode": "string",
    "usageType": "string",
    "operation": "string",
    "availabilityZone": "string",
    "key": "string",
    "group": "string",
    "usageAccountId": "string",
    "amounts": [
      {
        "startHour": timestamp,
        "amount": double
      }
      ...
    ],
    "historicalUsage": {
      "serviceCode": "string",
      "usageType": "string",
      "operation": "string",
      "location": "string",
      "usageAccountId": "string",
      "billInterval": {
        "start": timestamp,
        "end": timestamp
      },
      "filterExpression": {
        "and": [
          {
            "and": [
              { ... recursive ... }
              ...
            ],
            "or": [
              { ... recursive ... }
              ...
            ],
            "not": { ... recursive ... },
            "costCategories": {
              "key": "string",
              "matchOptions": ["string", ...],
              "values": ["string", ...]
            },
            "dimensions": {
              "key": "string",
              "matchOptions": ["string", ...],
              "values": ["string", ...]
            },
            "tags": {
              "key": "string",
              "matchOptions": ["string", ...],
              "values": ["string", ...]
            }
          }
          ...
        ],
        "or": [
          {
            "and": [
              { ... recursive ... }
              ...
            ],
            "or": [
              { ... recursive ... }
              ...
            ],
            "not": { ... recursive ... },
            "costCategories": {
              "key": "string",
              "matchOptions": ["string", ...],
              "values": ["string", ...]
            },
            "dimensions": {
              "key": "string",
              "matchOptions": ["string", ...],
              "values": ["string", ...]
            },
            "tags": {
              "key": "string",
              "matchOptions": ["string", ...],
              "values": ["string", ...]
            }
          }
          ...
        ],
        "not": {
          "and": [
            { ... recursive ... }
            ...
          ],
          "or": [
            { ... recursive ... }
            ...
          ],
          "not": { ... recursive ... },
          "costCategories": {
            "key": "string",
            "matchOptions": ["string", ...],
            "values": ["string", ...]
          },
          "dimensions": {
            "key": "string",
            "matchOptions": ["string", ...],
            "values": ["string", ...]
          },
          "tags": {
            "key": "string",
            "matchOptions": ["string", ...],
            "values": ["string", ...]
          }
        },
        "costCategories": {
          "key": "string",
          "matchOptions": ["string", ...],
          "values": ["string", ...]
        },
        "dimensions": {
          "key": "string",
          "matchOptions": ["string", ...],
          "values": ["string", ...]
        },
        "tags": {
          "key": "string",
          "matchOptions": ["string", ...],
          "values": ["string", ...]
        }
      }
    }
  }
  ...
]
```

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

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

Returns the list of successful usage line items that were created for the Bill Scenario.

(structure)

Represents a successfully created item in a batch operation for bill scenario usage modifications.

serviceCode -> (string)

The Amazon Web Services service code for this usage modification.

usageType -> (string)

The type of usage that was modified.

operation -> (string)

The specific operation associated with this usage modification.

location -> (string)

The location associated with this usage modification.

availabilityZone -> (string)

The availability zone associated with this usage modification, if applicable.

id -> (string)

The unique identifier assigned to the created usage modification.

group -> (string)

The group identifier for the created usage modification.

usageAccountId -> (string)

The Amazon Web Services account ID associated with the created usage modification.

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

key -> (string)

The key of the successfully created entry.

errors -> (list)

Returns the list of errors reason and the usage item keys that cannot be created in the Bill Scenario.

(structure)

Represents an error that occurred during a batch create operation for bill scenario usage modifications.

key -> (string)

The key of the entry that caused the error.

errorMessage -> (string)

A descriptive message for the error that occurred.

errorCode -> (string)

The error code associated with the failed operation.