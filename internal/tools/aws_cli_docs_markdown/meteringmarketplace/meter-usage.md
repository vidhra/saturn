# meter-usageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/meter-usage.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/meter-usage.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [meteringmarketplace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/meteringmarketplace/index.html#cli-aws-meteringmarketplace) ]

# meter-usage

## Description

API to emit metering records. For identical requests, the API is idempotent and returns the metering record ID. This is used for metering flexible consumption pricing (FCP) Amazon Machine Images (AMI) and container products.

`MeterUsage` is authenticated on the buyerâs Amazon Web Services account using credentials from the Amazon EC2 instance, Amazon ECS task, or Amazon EKS pod.

`MeterUsage` can optionally include multiple usage allocations, to provide customers with usage data split into buckets by tags that you define (or allow the customer to define).

Usage records are expected to be submitted as quickly as possible after the event that is being recorded, and are not accepted more than 6 hours after the event.

For Amazon Web Services Regions that support `MeterUsage` , see [MeterUsage Region support for Amazon EC2](https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#meterusage-region-support-ec2) and [MeterUsage Region support for Amazon ECS and Amazon EKS](https://docs.aws.amazon.com/marketplace/latest/APIReference/metering-regions.html#meterusage-region-support-ecs-eks) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/meteringmarketplace-2016-01-14/MeterUsage)

## Synopsis

```
meter-usage
--product-code <value>
--timestamp <value>
--usage-dimension <value>
[--usage-quantity <value>]
[--dry-run | --no-dry-run]
[--usage-allocations <value>]
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

`--product-code` (string)

Product code is used to uniquely identify a product in Amazon Web Services Marketplace. The product code should be the same as the one used during the publishing of a new product.

`--timestamp` (timestamp)

Timestamp, in UTC, for which the usage is being reported. Your application can meter usage for up to six hours in the past. Make sure the `timestamp` value is not before the start of the software usage.

`--usage-dimension` (string)

It will be one of the fcp dimension name provided during the publishing of the product.

`--usage-quantity` (integer)

Consumption value for the hour. Defaults to `0` if not specified.

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the permissions required for the action, but does not make the request. If you have the permissions, the request returns `DryRunOperation` ; otherwise, it returns `UnauthorizedException` . Defaults to `false` if not specified.

`--usage-allocations` (list)

The set of `UsageAllocations` to submit.

The sum of all `UsageAllocation` quantities must equal the `UsageQuantity` of the `MeterUsage` request, and each `UsageAllocation` must have a unique set of tags (include no tags).

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

Shorthand Syntax:

```
AllocatedUsageQuantity=integer,Tags=[{Key=string,Value=string},{Key=string,Value=string}] ...
```

JSON Syntax:

```
[
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

MeteringRecordId -> (string)

Metering record id.