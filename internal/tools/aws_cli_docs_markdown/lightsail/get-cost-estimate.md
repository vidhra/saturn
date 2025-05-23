# get-cost-estimateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-cost-estimate.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/get-cost-estimate.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# get-cost-estimate

## Description

Retrieves information about the cost estimate for a specified resource. A cost estimate will not generate for a resource that has been deleted.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/GetCostEstimate)

## Synopsis

```
get-cost-estimate
--resource-name <value>
--start-time <value>
--end-time <value>
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

`--resource-name` (string)

The resource name.

`--start-time` (timestamp)

The cost estimate start time.

Constraints:

- Specified in Coordinated Universal Time (UTC).
- Specified in the Unix time format. For example, if you want to use a start time of October 1, 2018, at 8 PM UTC, specify `1538424000` as the start time.

You can convert a human-friendly time to Unix time format using a converter like [Epoch converter](https://www.epochconverter.com/) .

`--end-time` (timestamp)

The cost estimate end time.

Constraints:

- Specified in Coordinated Universal Time (UTC).
- Specified in the Unix time format. For example, if you want to use an end time of October 1, 2018, at 9 PM UTC, specify `1538427600` as the end time.

You can convert a human-friendly time to Unix time format using a converter like [Epoch converter](https://www.epochconverter.com/) .

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

resourcesBudgetEstimate -> (list)

Returns the estimateâs forecasted cost or usage.

(structure)

Describes the estimated cost or usage that a budget tracks.

resourceName -> (string)

The resource name.

resourceType -> (string)

The type of resource the budget will track.

costEstimates -> (list)

The cost estimate for the specified budget.

(structure)

Describes the estimated cost for resources in your Lightsail for Research account.

usageType -> (string)

The types of usage that are included in the estimate, such as costs, usage, or data transfer.

resultsByTime -> (list)

The cost estimate result thatâs associated with a time period.

(structure)

An estimate thatâs associated with a time period.

usageCost -> (double)

The amount of cost or usage thatâs measured for the cost estimate.

pricingUnit -> (string)

The unit of measurement thatâs used for the cost estimate.

unit -> (double)

The number of pricing units used to calculate the total number of hours. For example, 1 unit equals 1 hour.

currency -> (string)

The currency of the estimate in USD.

timePeriod -> (structure)

The period of time, in days, that an estimate covers. The period has a start date and an end date. The start date must come before the end date.

start -> (timestamp)

The beginning of the time period. The start date is inclusive. For example, if `start` is `2017-01-01` , Lightsail for Research retrieves cost and usage data starting at `2017-01-01` up to the end date. The start date must be equal to or no later than the current date to avoid a validation error.

end -> (timestamp)

The end of the time period. The end date is exclusive. For example, if `end` is `2017-05-01` , Lightsail for Research retrieves cost and usage data from the start date up to, but not including, `2017-05-01` .

startTime -> (timestamp)

The estimate start time.

endTime -> (timestamp)

The estimate end time.