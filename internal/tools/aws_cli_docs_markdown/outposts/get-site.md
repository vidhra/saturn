# get-siteÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/get-site.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/get-site.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [outposts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/outposts/index.html#cli-aws-outposts) ]

# get-site

## Description

Gets information about the specified Outpost site.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/outposts-2019-12-03/GetSite)

## Synopsis

```
get-site
--site-id <value>
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

`--site-id` (string)

The ID or the Amazon Resource Name (ARN) of the site.

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

Site -> (structure)

Information about a site.

SiteId -> (string)

The ID of the site.

AccountId -> (string)

The ID of the Amazon Web Services account.

Name -> (string)

The name of the site.

Description -> (string)

The description of the site.

Tags -> (map)

The site tags.

key -> (string)

value -> (string)

SiteArn -> (string)

The Amazon Resource Name (ARN) of the site.

Notes -> (string)

Notes about a site.

OperatingAddressCountryCode -> (string)

The ISO-3166 two-letter country code where the hardware is installed and powered on.

OperatingAddressStateOrRegion -> (string)

State or region where the hardware is installed and powered on.

OperatingAddressCity -> (string)

City where the hardware is installed and powered on.

RackPhysicalProperties -> (structure)

Information about the physical and logistical details for a rack at the site.

PowerDrawKva -> (string)

The power draw available at the hardware placement position for the rack.

PowerPhase -> (string)

The power option that you can provide for hardware.

PowerConnector -> (string)

The power connector for the hardware.

PowerFeedDrop -> (string)

The position of the power feed.

UplinkGbps -> (string)

The uplink speed the rack supports for the connection to the Region.

UplinkCount -> (string)

The number of uplinks each Outpost network device.

FiberOpticCableType -> (string)

The type of fiber used to attach the Outpost to the network.

OpticalStandard -> (string)

The type of optical standard used to attach the Outpost to the network. This field is dependent on uplink speed, fiber type, and distance to the upstream device. For more information about networking requirements for racks, see [Network](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-requirements.html#facility-networking) in the Amazon Web Services Outposts User Guide.

MaximumSupportedWeightLbs -> (string)

The maximum rack weight that this site can support. `NO_LIMIT` is over 2000 lbs (907 kg).