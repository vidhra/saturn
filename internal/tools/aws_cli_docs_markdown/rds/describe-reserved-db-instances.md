# describe-reserved-db-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-reserved-db-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/describe-reserved-db-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# describe-reserved-db-instances

## Description

Returns information about reserved DB instances for this account, or about a specified reserved DB instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DescribeReservedDBInstances)

`describe-reserved-db-instances` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ReservedDBInstances`

## Synopsis

```
describe-reserved-db-instances
[--reserved-db-instance-id <value>]
[--reserved-db-instances-offering-id <value>]
[--db-instance-class <value>]
[--duration <value>]
[--product-description <value>]
[--offering-type <value>]
[--multi-az | --no-multi-az]
[--lease-id <value>]
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

`--reserved-db-instance-id` (string)

The reserved DB instance identifier filter value. Specify this parameter to show only the reservation that matches the specified reservation ID.

`--reserved-db-instances-offering-id` (string)

The offering identifier filter value. Specify this parameter to show only purchased reservations matching the specified offering identifier.

`--db-instance-class` (string)

The DB instance class filter value. Specify this parameter to show only those reservations matching the specified DB instances class.

`--duration` (string)

The duration filter value, specified in years or seconds. Specify this parameter to show only reservations for this duration.

Valid Values: `1 | 3 | 31536000 | 94608000`

`--product-description` (string)

The product description filter value. Specify this parameter to show only those reservations matching the specified product description.

`--offering-type` (string)

The offering type filter value. Specify this parameter to show only the available offerings matching the specified offering type.

Valid Values: `"Partial Upfront" | "All Upfront" | "No Upfront"`

`--multi-az` | `--no-multi-az` (boolean)

Specifies whether to show only those reservations that support Multi-AZ.

`--lease-id` (string)

The lease identifier filter value. Specify this parameter to show only the reservation that matches the specified lease ID.

### Note

Amazon Web Services Support might request the lease ID for an issue related to a reserved DB instance.

`--filters` (list)

This parameter isnât currently supported.

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as IDs. The filters supported by a describe operation are documented with the describe operation.

### Note

Currently, wildcards are not supported in filters.

The following actions can be filtered:

- `DescribeDBClusterBacktracks`
- `DescribeDBClusterEndpoints`
- `DescribeDBClusters`
- `DescribeDBInstances`
- `DescribeDBRecommendations`
- `DescribeDBShardGroups`
- `DescribePendingMaintenanceActions`

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

One or more filter values. Filter values are case-sensitive.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To describe reserved DB instances**

The following `describe-reserved-db-instances` example retrieves details about any reserved DB instances in the current AWS account.

```
aws rds describe-reserved-db-instances
```

Output:

```
{
    "ReservedDBInstances": [
        {
            "ReservedDBInstanceId": "myreservedinstance",
            "ReservedDBInstancesOfferingId": "12ab34cd-59af-4b2c-a660-1abcdef23456",
            "DBInstanceClass": "db.t3.micro",
            "StartTime": "2020-06-01T13:44:21.436Z",
            "Duration": 31536000,
            "FixedPrice": 0.0,
            "UsagePrice": 0.0,
            "CurrencyCode": "USD",
            "DBInstanceCount": 1,
            "ProductDescription": "sqlserver-ex(li)",
            "OfferingType": "No Upfront",
            "MultiAZ": false,
            "State": "payment-pending",
            "RecurringCharges": [
                {
                    "RecurringChargeAmount": 0.014,
                    "RecurringChargeFrequency": "Hourly"
                }
            ],
            "ReservedDBInstanceArn": "arn:aws:rds:us-west-2:123456789012:ri:myreservedinstance",
            "LeaseId": "a1b2c3d4-6b69-4a59-be89-5e11aa446666"
        }
    ]
}
```

For more information, see [Reserved DB Instances for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_WorkingWithReservedDBInstances.html) in the *Amazon RDS User Guide*.

## Output

Marker -> (string)

An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by `MaxRecords` .

ReservedDBInstances -> (list)

A list of reserved DB instances.

(structure)

This data type is used as a response element in the `DescribeReservedDBInstances` and `PurchaseReservedDBInstancesOffering` actions.

ReservedDBInstanceId -> (string)

The unique identifier for the reservation.

ReservedDBInstancesOfferingId -> (string)

The offering identifier.

DBInstanceClass -> (string)

The DB instance class for the reserved DB instance.

StartTime -> (timestamp)

The time the reservation started.

Duration -> (integer)

The duration of the reservation in seconds.

FixedPrice -> (double)

The fixed price charged for this reserved DB instance.

UsagePrice -> (double)

The hourly price charged for this reserved DB instance.

CurrencyCode -> (string)

The currency code for the reserved DB instance.

DBInstanceCount -> (integer)

The number of reserved DB instances.

ProductDescription -> (string)

The description of the reserved DB instance.

OfferingType -> (string)

The offering type of this reserved DB instance.

MultiAZ -> (boolean)

Indicates whether the reservation applies to Multi-AZ deployments.

State -> (string)

The state of the reserved DB instance.

RecurringCharges -> (list)

The recurring price charged to run this reserved DB instance.

(structure)

This data type is used as a response element in the `DescribeReservedDBInstances` and `DescribeReservedDBInstancesOfferings` actions.

RecurringChargeAmount -> (double)

The amount of the recurring charge.

RecurringChargeFrequency -> (string)

The frequency of the recurring charge.

ReservedDBInstanceArn -> (string)

The Amazon Resource Name (ARN) for the reserved DB instance.

LeaseId -> (string)

The unique identifier for the lease associated with the reserved DB instance.

### Note

Amazon Web Services Support might request the lease ID for an issue related to a reserved DB instance.