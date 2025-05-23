# describe-reserved-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-reserved-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-reserved-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-reserved-instances

## Description

Describes one or more of the Reserved Instances that you purchased.

For more information about Reserved Instances, see [Reserved Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts-on-demand-reserved-instances.html) in the *Amazon EC2 User Guide* .

### Note

The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeReservedInstances)

## Synopsis

```
describe-reserved-instances
[--offering-class <value>]
[--reserved-instances-ids <value>]
[--dry-run | --no-dry-run]
[--filters <value>]
[--offering-type <value>]
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

`--offering-class` (string)

Describes whether the Reserved Instance is Standard or Convertible.

Possible values:

- `standard`
- `convertible`

`--reserved-instances-ids` (list)

One or more Reserved Instance IDs.

Default: Describes all your Reserved Instances, or only those otherwise specified.

(string)

Syntax:

```
"string" "string" ...
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--filters` (list)

One or more filters.

- `availability-zone` - The Availability Zone where the Reserved Instance can be used.
- `availability-zone-id` - The ID of the Availability Zone where the Reserved Instance can be used.
- `duration` - The duration of the Reserved Instance (one year or three years), in seconds (`31536000` | `94608000` ).
- `end` - The time when the Reserved Instance expires (for example, 2015-08-07T11:54:42.000Z).
- `fixed-price` - The purchase price of the Reserved Instance (for example, 9800.0).
- `instance-type` - The instance type that is covered by the reservation.
- `scope` - The scope of the Reserved Instance (`Region` or `Availability Zone` ).
- `product-description` - The Reserved Instance product platform description (`Linux/UNIX` | `Linux with SQL Server Standard` | `Linux with SQL Server Web` | `Linux with SQL Server Enterprise` | `SUSE Linux` | `Red Hat Enterprise Linux` | `Red Hat Enterprise Linux with HA` | `Windows` | `Windows with SQL Server Standard` | `Windows with SQL Server Web` | `Windows with SQL Server Enterprise` ).
- `reserved-instances-id` - The ID of the Reserved Instance.
- `start` - The time at which the Reserved Instance purchase request was placed (for example, 2014-08-07T11:54:42.000Z).
- `state` - The state of the Reserved Instance (`payment-pending` | `active` | `payment-failed` | `retired` ).
- `tag:<key>` - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.
- `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
- `usage-price` - The usage price of the Reserved Instance, per hour (for example, 0.84).

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

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

`--offering-type` (string)

The Reserved Instance offering type. If you are using tools that predate the 2011-11-01 API version, you only have access to the `Medium Utilization` Reserved Instance offering type.

Possible values:

- `Heavy Utilization`
- `Medium Utilization`
- `Light Utilization`
- `No Upfront`
- `Partial Upfront`
- `All Upfront`

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To describe your Reserved Instances**

This example command describes the Reserved Instances that you own.

Command:

```
aws ec2 describe-reserved-instances
```

Output:

```
{
  "ReservedInstances": [
      {
          "ReservedInstancesId": "b847fa93-e282-4f55-b59a-1342fexample",
          "OfferingType": "No Upfront",
          "AvailabilityZone": "us-west-1c",
          "End": "2016-08-14T21:34:34.000Z",
          "ProductDescription": "Linux/UNIX",
          "UsagePrice": 0.00,
          "RecurringCharges": [
              {
                  "Amount": 0.104,
                  "Frequency": "Hourly"
              }
          ],
          "Start": "2015-08-15T21:34:35.086Z",
          "State": "active",
          "FixedPrice": 0.0,
          "CurrencyCode": "USD",
          "Duration": 31536000,
          "InstanceTenancy": "default",
          "InstanceType": "m3.medium",
          "InstanceCount": 2
      },
      ...
  ]
}
```

**To describe your Reserved Instances using filters**

This example filters the response to include only three-year, t2.micro Linux/UNIX Reserved Instances in us-west-1c.

Command:

```
aws ec2 describe-reserved-instances --filters Name=duration,Values=94608000 Name=instance-type,Values=t2.micro Name=product-description,Values=Linux/UNIX Name=availability-zone,Values=us-east-1e
```

Output:

```
{
    "ReservedInstances": [
        {
            "ReservedInstancesId": "f127bd27-edb7-44c9-a0eb-0d7e09259af0",
            "OfferingType": "All Upfront",
            "AvailabilityZone": "us-east-1e",
            "End": "2018-03-26T21:34:34.000Z",
            "ProductDescription": "Linux/UNIX",
            "UsagePrice": 0.00,
            "RecurringCharges": [],
            "Start": "2015-03-27T21:34:35.848Z",
            "State": "active",
            "FixedPrice": 151.0,
            "CurrencyCode": "USD",
            "Duration": 94608000,
            "InstanceTenancy": "default",
            "InstanceType": "t2.micro",
            "InstanceCount": 1
        }
    ]
}
```

For more information, see [Using Amazon EC2 Instances](http://docs.aws.amazon.com/cli/latest/userguide/cli-ec2-launch.html) in the *AWS Command Line Interface User Guide*.

## Output

ReservedInstances -> (list)

A list of Reserved Instances.

(structure)

Describes a Reserved Instance.

CurrencyCode -> (string)

The currency of the Reserved Instance. Itâs specified using ISO 4217 standard currency codes. At this time, the only supported currency is `USD` .

InstanceTenancy -> (string)

The tenancy of the instance.

OfferingClass -> (string)

The offering class of the Reserved Instance.

OfferingType -> (string)

The Reserved Instance offering type.

RecurringCharges -> (list)

The recurring charge tag assigned to the resource.

(structure)

Describes a recurring charge.

Amount -> (double)

The amount of the recurring charge.

Frequency -> (string)

The frequency of the recurring charge.

Scope -> (string)

The scope of the Reserved Instance.

Tags -> (list)

Any tags assigned to the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

AvailabilityZoneId -> (string)

The ID of the Availability Zone.

ReservedInstancesId -> (string)

The ID of the Reserved Instance.

InstanceType -> (string)

The instance type on which the Reserved Instance can be used.

AvailabilityZone -> (string)

The Availability Zone in which the Reserved Instance can be used.

Start -> (timestamp)

The date and time the Reserved Instance started.

End -> (timestamp)

The time when the Reserved Instance expires.

Duration -> (long)

The duration of the Reserved Instance, in seconds.

UsagePrice -> (float)

The usage price of the Reserved Instance, per hour.

FixedPrice -> (float)

The purchase price of the Reserved Instance.

InstanceCount -> (integer)

The number of reservations purchased.

ProductDescription -> (string)

The Reserved Instance product platform description.

State -> (string)

The state of the Reserved Instance purchase.