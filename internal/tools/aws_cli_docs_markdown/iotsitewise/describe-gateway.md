# describe-gatewayÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-gateway.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-gateway.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotsitewise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/index.html#cli-aws-iotsitewise) ]

# describe-gateway

## Description

Retrieves information about a gateway.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotsitewise-2019-12-02/DescribeGateway)

## Synopsis

```
describe-gateway
--gateway-id <value>
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

`--gateway-id` (string)

The ID of the gateway device.

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

**To describe a gateway**

The following `describe-gateway` example describes a gateway.

```
aws iotsitewise describe-gateway \
    --gateway-id a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE
```

Output:

```
{
    "gatewayId": "a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE",
    "gatewayName": "ExampleCorpGateway",
    "gatewayArn": "arn:aws:iotsitewise:us-west-2:123456789012:gateway/a1b2c3d4-5678-90ab-cdef-1a1a1EXAMPLE",
    "gatewayPlatform": {
        "greengrass": {
            "groupArn": "arn:aws:greengrass:us-west-2:123456789012:/greengrass/groups/a1b2c3d4-5678-90ab-cdef-1b1b1EXAMPLE"
        }
    },
    "gatewayCapabilitySummaries": [
        {
            "capabilityNamespace": "iotsitewise:opcuacollector:1",
            "capabilitySyncStatus": "IN_SYNC"
        }
    ],
    "creationDate": 1588369971.457,
    "lastUpdateDate": 1588369971.457
}
```

For more information, see [Ingesting data using a gateway](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/gateways.html) in the *AWS IoT SiteWise User Guide*.

## Output

gatewayId -> (string)

The ID of the gateway device.

gatewayName -> (string)

The name of the gateway.

gatewayArn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the gateway, which has the following format.

`arn:${Partition}:iotsitewise:${Region}:${Account}:gateway/${GatewayId}`

gatewayPlatform -> (structure)

The gatewayâs platform.

greengrass -> (structure)

A gateway that runs on IoT Greengrass.

groupArn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the Greengrass group. For more information about how to find a groupâs ARN, see [ListGroups](https://docs.aws.amazon.com/greengrass/v1/apireference/listgroups-get.html) and [GetGroup](https://docs.aws.amazon.com/greengrass/v1/apireference/getgroup-get.html) in the *IoT Greengrass V1 API Reference* .

greengrassV2 -> (structure)

A gateway that runs on IoT Greengrass V2.

coreDeviceThingName -> (string)

The name of the IoT thing for your IoT Greengrass V2 core device.

coreDeviceOperatingSystem -> (string)

The operating system of the core device in IoT Greengrass V2.

siemensIE -> (structure)

A SiteWise Edge gateway that runs on a Siemens Industrial Edge Device.

iotCoreThingName -> (string)

The name of the IoT Thing for your SiteWise Edge gateway.

gatewayVersion -> (string)

The version of the gateway. A value of `3` indicates an MQTT-enabled, V3 gateway, while `2` indicates a Classic streams, V2 gateway.

gatewayCapabilitySummaries -> (list)

A list of gateway capability summaries that each contain a namespace and status. Each gateway capability defines data sources for the gateway. To retrieve a capability configurationâs definition, use [DescribeGatewayCapabilityConfiguration](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeGatewayCapabilityConfiguration.html) .

(structure)

Contains a summary of a gateway capability configuration.

capabilityNamespace -> (string)

The namespace of the capability configuration. For example, if you configure OPC-UA sources from the IoT SiteWise console, your OPC-UA capability configuration has the namespace `iotsitewise:opcuacollector:version` , where `version` is a number such as `1` .

capabilitySyncStatus -> (string)

The synchronization status of the capability configuration. The sync status can be one of the following:

- `IN_SYNC` â The gateway is running the capability configuration.
- `NOT_APPLICABLE` â Synchronization is not required for this capability configuration. This is most common when integrating partner data sources, because the data integration is handled externally by the partner.
- `OUT_OF_SYNC` â The gateway hasnât received the capability configuration.
- `SYNC_FAILED` â The gateway rejected the capability configuration.
- `UNKNOWN` â The synchronization status is currently unknown due to an undetermined or temporary error.

creationDate -> (timestamp)

The date the gateway was created, in Unix epoch time.

lastUpdateDate -> (timestamp)

The date the gateway was last updated, in Unix epoch time.