# create-wireless-gatewayÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-gateway.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-wireless-gateway.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotwireless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html#cli-aws-iotwireless) ]

# create-wireless-gateway

## Description

Provisions a wireless gateway.

### Note

When provisioning a wireless gateway, you might run into duplication errors for the following reasons.

- If you specify a `GatewayEui` value that already exists.
- If you used a `ClientRequestToken` with the same parameters within the last 10 minutes.

To avoid this error, make sure that you use unique identifiers and parameters for each request within the specified time period.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotwireless-2020-11-22/CreateWirelessGateway)

## Synopsis

```
create-wireless-gateway
[--name <value>]
[--description <value>]
[--tags <value>]
[--client-request-token <value>]
--lorawan <value>
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

`--name` (string)

The name of the new resource.

`--description` (string)

The description of the new resource.

`--tags` (list)

The tags to attach to the new wireless gateway. Tags are metadata that you can use to manage a resource.

(structure)

A simple label consisting of a customer-defined key-value pair

Key -> (string)

The tagâs key value.

Value -> (string)

The tagâs value.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--client-request-token` (string)

Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

`--lorawan` (structure)

The gateway configuration information to use to create the wireless gateway.

GatewayEui -> (string)

The gatewayâs EUI value.

RfRegion -> (string)

The frequency band (RFRegion) value.

JoinEuiFilters -> (list)

A list of JoinEuiRange used by LoRa gateways to filter LoRa frames.

(list)

A pair of join EUI describing a range [BegEui, EndEui], both ends are inclusive.

(string)

NetIdFilters -> (list)

A list of NetId values that are used by LoRa gateways to filter the uplink frames.

(string)

LoRaWAN network ID.

SubBands -> (list)

A list of integer indicating which sub bands are supported by LoRa gateway.

(integer)

A subset of supported frequency channels in a certain RFRegion.

Beaconing -> (structure)

Beaconing object information, which consists of the data rate and frequency parameters.

DataRate -> (integer)

The data rate for gateways that are sending the beacons.

Frequencies -> (list)

The frequency list for the gateways to send the beacons.

(integer)

MaxEirp -> (float)

The MaxEIRP value.

Shorthand Syntax:

```
GatewayEui=string,RfRegion=string,JoinEuiFilters=[[string,string],[string,string]],NetIdFilters=string,string,SubBands=integer,integer,Beaconing={DataRate=integer,Frequencies=[integer,integer]},MaxEirp=float
```

JSON Syntax:

```
{
  "GatewayEui": "string",
  "RfRegion": "string",
  "JoinEuiFilters": [
    ["string", ...]
    ...
  ],
  "NetIdFilters": ["string", ...],
  "SubBands": [integer, ...],
  "Beaconing": {
    "DataRate": integer,
    "Frequencies": [integer, ...]
  },
  "MaxEirp": float
}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a wireless gateway**

The following `create-wireless-gateway` example creates a wireless LoRaWAN device gateway.

```
aws iotwireless create-wireless-gateway \
    --lorawan GatewayEui="a1b2c3d4567890ab",RfRegion="US915" \
    --name "myFirstLoRaWANGateway" \
    --description "Using my first LoRaWAN gateway"
```

Output:

```
{
    "Arn": "arn:aws:iotwireless:us-east-1:123456789012:WirelessGateway/12345678-a1b2-3c45-67d8-e90fa1b2c34d",
    "Id": "12345678-a1b2-3c45-67d8-e90fa1b2c34d"
}
```

For more information, see [Connecting devices and gateways to AWS IoT Core for LoRaWAN](https://docs.aws.amazon.com/iot/latest/developerguide/connect-iot-lorawan.html) in the *AWS IoT Developers Guide*.

## Output

Arn -> (string)

The Amazon Resource Name of the new resource.

Id -> (string)

The ID of the new wireless gateway.