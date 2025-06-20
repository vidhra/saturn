# describe-capacity-block-offeringsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-capacity-block-offerings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-capacity-block-offerings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-capacity-block-offerings

## Description

Describes Capacity Block offerings available for purchase in the Amazon Web Services Region that youâre currently using. With Capacity Blocks, you purchase a specific instance type for a period of time.

To search for an available Capacity Block offering, you specify a reservation duration and instance count.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeCapacityBlockOfferings)

`describe-capacity-block-offerings` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `CapacityBlockOfferings`

## Synopsis

```
describe-capacity-block-offerings
[--dry-run | --no-dry-run]
[--instance-type <value>]
[--instance-count <value>]
[--start-date-range <value>]
[--end-date-range <value>]
--capacity-duration-hours <value>
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--instance-type` (string)

The type of instance for which the Capacity Block offering reserves capacity.

`--instance-count` (integer)

The number of instances for which to reserve capacity. Each Capacity Block can have up to 64 instances, and you can have up to 256 instances across Capacity Blocks.

`--start-date-range` (timestamp)

The earliest start date for the Capacity Block offering.

`--end-date-range` (timestamp)

The latest end date for the Capacity Block offering.

`--capacity-duration-hours` (integer)

The reservation duration for the Capacity Block, in hours. You must specify the duration in 1-day increments up 14 days, and in 7-day increments up to 182 days.

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

CapacityBlockOfferings -> (list)

The recommended Capacity Block offering for the dates specified.

(structure)

The recommended Capacity Block that fits your search requirements.

CapacityBlockOfferingId -> (string)

The ID of the Capacity Block offering.

InstanceType -> (string)

The instance type of the Capacity Block offering.

AvailabilityZone -> (string)

The Availability Zone of the Capacity Block offering.

InstanceCount -> (integer)

The number of instances in the Capacity Block offering.

StartDate -> (timestamp)

The start date of the Capacity Block offering.

EndDate -> (timestamp)

The end date of the Capacity Block offering.

CapacityBlockDurationHours -> (integer)

The number of hours (in addition to `capacityBlockDurationMinutes` ) for the duration of the Capacity Block reservation. For example, if a Capacity Block starts at **04:55** and ends at **11:30** , the hours field would be **6** .

UpfrontFee -> (string)

The total price to be paid up front.

CurrencyCode -> (string)

The currency of the payment for the Capacity Block.

Tenancy -> (string)

The tenancy of the Capacity Block.

CapacityBlockDurationMinutes -> (integer)

The number of minutes (in addition to `capacityBlockDurationHours` ) for the duration of the Capacity Block reservation. For example, if a Capacity Block starts at **08:55** and ends at **11:30** , the minutes field would be **35** .

NextToken -> (string)

The token to use to retrieve the next page of results. This value is `null` when there are no more results to return.