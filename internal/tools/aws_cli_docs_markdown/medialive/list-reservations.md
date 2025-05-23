# list-reservationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-reservations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/list-reservations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medialive](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medialive/index.html#cli-aws-medialive) ]

# list-reservations

## Description

List purchased reservations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medialive-2017-10-14/ListReservations)

`list-reservations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Reservations`

## Synopsis

```
list-reservations
[--channel-class <value>]
[--codec <value>]
[--maximum-bitrate <value>]
[--maximum-framerate <value>]
[--resolution <value>]
[--resource-type <value>]
[--special-feature <value>]
[--video-quality <value>]
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

`--channel-class` (string)
Filter by channel class, âSTANDARDâ or âSINGLE_PIPELINEâ

`--codec` (string)
Filter by codec, âAVCâ, âHEVCâ, âMPEG2â, âAUDIOâ, âLINKâ, or âAV1â

`--maximum-bitrate` (string)
Filter by bitrate, âMAX_10_MBPSâ, âMAX_20_MBPSâ, or âMAX_50_MBPSâ

`--maximum-framerate` (string)
Filter by framerate, âMAX_30_FPSâ or âMAX_60_FPSâ

`--resolution` (string)
Filter by resolution, âSDâ, âHDâ, âFHDâ, or âUHDâ

`--resource-type` (string)
Filter by resource type, âINPUTâ, âOUTPUTâ, âMULTIPLEXâ, or âCHANNELâ

`--special-feature` (string)
Filter by special feature, âADVANCED_AUDIOâ or âAUDIO_NORMALIZATIONâ

`--video-quality` (string)
Filter by video quality, âSTANDARDâ, âENHANCEDâ, or âPREMIUMâ

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

NextToken -> (string)

Token to retrieve the next page of results

Reservations -> (list)

List of reservations

(structure)

Reserved resources available to use

Arn -> (string)

Unique reservation ARN, e.g. âarn:aws:medialive:us-west-2:123456789012:reservation:1234567â

Count -> (integer)

Number of reserved resources

CurrencyCode -> (string)

Currency code for usagePrice and fixedPrice in ISO-4217 format, e.g. âUSDâ

Duration -> (integer)

Lease duration, e.g. â12â

DurationUnits -> (string)

Units for duration, e.g. âMONTHSâ

End -> (string)

Reservation UTC end date and time in ISO-8601 format, e.g. â2019-03-01T00:00:00â

FixedPrice -> (double)

One-time charge for each reserved resource, e.g. â0.0â for a NO_UPFRONT offering

Name -> (string)

User specified reservation name

OfferingDescription -> (string)

Offering description, e.g. âHD AVC output at 10-20 Mbps, 30 fps, and standard VQ in US West (Oregon)â

OfferingId -> (string)

Unique offering ID, e.g. â87654321â

OfferingType -> (string)

Offering type, e.g. âNO_UPFRONTâ

Region -> (string)

AWS region, e.g. âus-west-2â

RenewalSettings -> (structure)

Renewal settings for the reservation

AutomaticRenewal -> (string)

Automatic renewal status for the reservation

RenewalCount -> (integer)

Count for the reservation renewal

ReservationId -> (string)

Unique reservation ID, e.g. â1234567â

ResourceSpecification -> (structure)

Resource configuration details

ChannelClass -> (string)

Channel class, e.g. âSTANDARDâ

Codec -> (string)

Codec, e.g. âAVCâ

MaximumBitrate -> (string)

Maximum bitrate, e.g. âMAX_20_MBPSâ

MaximumFramerate -> (string)

Maximum framerate, e.g. âMAX_30_FPSâ (Outputs only)

Resolution -> (string)

Resolution, e.g. âHDâ

ResourceType -> (string)

Resource type, âINPUTâ, âOUTPUTâ, âMULTIPLEXâ, or âCHANNELâ

SpecialFeature -> (string)

Special feature, e.g. âAUDIO_NORMALIZATIONâ (Channels only)

VideoQuality -> (string)

Video quality, e.g. âSTANDARDâ (Outputs only)

Start -> (string)

Reservation UTC start date and time in ISO-8601 format, e.g. â2018-03-01T00:00:00â

State -> (string)

Current state of reservation, e.g. âACTIVEâ

Tags -> (map)

A collection of key-value pairs

key -> (string)

Placeholder documentation for __string

value -> (string)

Placeholder documentation for __string

UsagePrice -> (double)

Recurring usage charge for each reserved resource, e.g. â157.0â