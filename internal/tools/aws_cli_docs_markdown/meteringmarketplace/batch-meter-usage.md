# batch-meter-usageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/batch-meter-usage.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/batch-meter-usage.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [meteringmarketplace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/index.html#cli-aws-meteringmarketplace) ]

# batch-meter-usage

## Description

### Warning

The `CustomerIdentifier` parameter is scheduled for deprecation. Use `CustomerAWSAccountID` instead.

These parameters are mutually exclusive. You canât specify both `CustomerIdentifier` and `CustomerAWSAccountID` in the same request.

To post metering records for customers, SaaS applications call `BatchMeterUsage` , which is used for metering SaaS flexible consumption pricing (FCP). Identical requests are idempotent and can be retried with the same records or a subset of records. Each `BatchMeterUsage` request is for only one product. If you want to meter usage for multiple products, you must make multiple `BatchMeterUsage` calls.

Usage records should be submitted in quick succession following a recorded event. Usage records arenât accepted 6 hours or more after an event.

`BatchMeterUsage` can process up to 25 `UsageRecords` at a time, and each request must be less than 1 MB in size. Optionally, you can have multiple usage allocations for usage data thatâs split into buckets according to predefined tags.

`BatchMeterUsage` returns a list of `UsageRecordResult` objects, which have each `UsageRecord` . It also returns a list of `UnprocessedRecords` , which indicate errors on the service side that should be retried.

For Amazon Web Services Regions that support `BatchMeterUsage` , see [BatchMeterUsage Region support](https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#batchmeterusage-region-support) .

### Note

For an example of `BatchMeterUsage` , see [BatchMeterUsage code example](https://docs.aws.amazon.com/marketplace/latest/userguide/saas-code-examples.html#saas-batchmeterusage-example) in the *Amazon Web Services Marketplace Seller Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/meteringmarketplace-2016-01-14/BatchMeterUsage)

## Synopsis

```
batch-meter-usage
--usage-records <value>
--product-code <value>
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

`--usage-records` (list)

The set of `UsageRecords` to submit. `BatchMeterUsage` accepts up to 25 `UsageRecords` at a time.

(structure)

A `UsageRecord` indicates a quantity of usage for a given product, customer, dimension and time.

Multiple requests with the same `UsageRecords` as input will be de-duplicated to prevent double charges.

Timestamp -> (timestamp)

Timestamp, in UTC, for which the usage is being reported.

Your application can meter usage for up to one hour in the past. Make sure the `timestamp` value is not before the start of the software usage.

CustomerIdentifier -> (string)

The `CustomerIdentifier` is obtained through the `ResolveCustomer` operation and represents an individual buyer in your application.

Dimension -> (string)

During the process of registering a product on Amazon Web Services Marketplace, dimensions are specified. These represent different units of value in your application.

Quantity -> (integer)

The quantity of usage consumed by the customer for the given dimension and time. Defaults to `0` if not specified.

UsageAllocations -> (list)

The set of `UsageAllocations` to submit. The sum of all `UsageAllocation` quantities must equal the Quantity of the `UsageRecord` .

(structure)

Usage allocations allow you to split usage into buckets by tags.

Each `UsageAllocation` indicates the usage quantity for a specific set of tags.

AllocatedUsageQuantity -> (integer)

The total quantity allocated to this bucket of usage.

Tags -> (list)

The set of tags that define the bucket of usage. For the bucket of items with no tags, this parameter can be left out.

(structure)

Metadata assigned to an allocation. Each tag is made up of a `key` and a `value` .

Key -> (string)

One part of a key-value pair that makes up a `tag` . A `key` is a label that acts like a category for the specific tag values.

Value -> (string)

One part of a key-value pair that makes up a `tag` . A `value` acts as a descriptor within a tag category (key). The value can be empty or null.

CustomerAWSAccountId -> (string)

The `CustomerAWSAccountID` parameter specifies the AWS account ID of the buyer.

JSON Syntax:

```
[
  {
    "Timestamp": timestamp,
    "CustomerIdentifier": "string",
    "Dimension": "string",
    "Quantity": integer,
    "UsageAllocations": [
      {
        "AllocatedUsageQuantity": integer,
        "Tags": [
          {
            "Key": "string",
            "Value": "string"
          }
          ...
        ]
      }
      ...
    ],
    "CustomerAWSAccountId": "string"
  }
  ...
]
```

`--product-code` (string)

Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.

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

Results -> (list)

Contains all `UsageRecords` processed by `BatchMeterUsage` . These records were either honored by Amazon Web Services Marketplace Metering Service or were invalid. Invalid records should be fixed before being resubmitted.

(structure)

A `UsageRecordResult` indicates the status of a given `UsageRecord` processed by `BatchMeterUsage` .

UsageRecord -> (structure)

The `UsageRecord` that was part of the `BatchMeterUsage` request.

Timestamp -> (timestamp)

Timestamp, in UTC, for which the usage is being reported.

Your application can meter usage for up to one hour in the past. Make sure the `timestamp` value is not before the start of the software usage.

CustomerIdentifier -> (string)

The `CustomerIdentifier` is obtained through the `ResolveCustomer` operation and represents an individual buyer in your application.

Dimension -> (string)

During the process of registering a product on Amazon Web Services Marketplace, dimensions are specified. These represent different units of value in your application.

Quantity -> (integer)

The quantity of usage consumed by the customer for the given dimension and time. Defaults to `0` if not specified.

UsageAllocations -> (list)

The set of `UsageAllocations` to submit. The sum of all `UsageAllocation` quantities must equal the Quantity of the `UsageRecord` .

(structure)

Usage allocations allow you to split usage into buckets by tags.

Each `UsageAllocation` indicates the usage quantity for a specific set of tags.

AllocatedUsageQuantity -> (integer)

The total quantity allocated to this bucket of usage.

Tags -> (list)

The set of tags that define the bucket of usage. For the bucket of items with no tags, this parameter can be left out.

(structure)

Metadata assigned to an allocation. Each tag is made up of a `key` and a `value` .

Key -> (string)

One part of a key-value pair that makes up a `tag` . A `key` is a label that acts like a category for the specific tag values.

Value -> (string)

One part of a key-value pair that makes up a `tag` . A `value` acts as a descriptor within a tag category (key). The value can be empty or null.

CustomerAWSAccountId -> (string)

The `CustomerAWSAccountID` parameter specifies the AWS account ID of the buyer.

MeteringRecordId -> (string)

The `MeteringRecordId` is a unique identifier for this metering event.

Status -> (string)

The `UsageRecordResult` `Status` indicates the status of an individual `UsageRecord` processed by `BatchMeterUsage` .

- *Success* - The `UsageRecord` was accepted and honored by `BatchMeterUsage` .
- *CustomerNotSubscribed* - The `CustomerIdentifier` specified is not able to use your product. The `UsageRecord` was not honored. There are three causes for this result:
- The customer identifier is invalid.
- The customer identifier provided in the metering record does not have an active agreement or subscription with this product. Future `UsageRecords` for this customer will fail until the customer subscribes to your product.
- The customerâs Amazon Web Services account was suspended.
- *DuplicateRecord* - Indicates that the `UsageRecord` was invalid and not honored. A previously metered `UsageRecord` had the same customer, dimension, and time, but a different quantity.

UnprocessedRecords -> (list)

Contains all `UsageRecords` that were not processed by `BatchMeterUsage` . This is a list of `UsageRecords` . You can retry the failed request by making another `BatchMeterUsage` call with this list as input in the `BatchMeterUsageRequest` .

(structure)

A `UsageRecord` indicates a quantity of usage for a given product, customer, dimension and time.

Multiple requests with the same `UsageRecords` as input will be de-duplicated to prevent double charges.

Timestamp -> (timestamp)

Timestamp, in UTC, for which the usage is being reported.

Your application can meter usage for up to one hour in the past. Make sure the `timestamp` value is not before the start of the software usage.

CustomerIdentifier -> (string)

The `CustomerIdentifier` is obtained through the `ResolveCustomer` operation and represents an individual buyer in your application.

Dimension -> (string)

During the process of registering a product on Amazon Web Services Marketplace, dimensions are specified. These represent different units of value in your application.

Quantity -> (integer)

The quantity of usage consumed by the customer for the given dimension and time. Defaults to `0` if not specified.

UsageAllocations -> (list)

The set of `UsageAllocations` to submit. The sum of all `UsageAllocation` quantities must equal the Quantity of the `UsageRecord` .

(structure)

Usage allocations allow you to split usage into buckets by tags.

Each `UsageAllocation` indicates the usage quantity for a specific set of tags.

AllocatedUsageQuantity -> (integer)

The total quantity allocated to this bucket of usage.

Tags -> (list)

The set of tags that define the bucket of usage. For the bucket of items with no tags, this parameter can be left out.

(structure)

Metadata assigned to an allocation. Each tag is made up of a `key` and a `value` .

Key -> (string)

One part of a key-value pair that makes up a `tag` . A `key` is a label that acts like a category for the specific tag values.

Value -> (string)

One part of a key-value pair that makes up a `tag` . A `value` acts as a descriptor within a tag category (key). The value can be empty or null.

CustomerAWSAccountId -> (string)

The `CustomerAWSAccountID` parameter specifies the AWS account ID of the buyer.