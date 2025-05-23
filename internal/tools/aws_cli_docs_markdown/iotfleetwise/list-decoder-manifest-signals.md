# list-decoder-manifest-signalsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/list-decoder-manifest-signals.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/list-decoder-manifest-signals.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotfleetwise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/index.html#cli-aws-iotfleetwise) ]

# list-decoder-manifest-signals

## Description

A list of information about signal decoders specified in a decoder manifest.

### Note

This API operation uses pagination. Specify the `nextToken` parameter in the request to return more results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotfleetwise-2021-06-17/ListDecoderManifestSignals)

`list-decoder-manifest-signals` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `signalDecoders`

## Synopsis

```
list-decoder-manifest-signals
--name <value>
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

`--name` (string)

The name of the decoder manifest to list information about.

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

signalDecoders -> (list)

Information about a list of signals to decode.

(structure)

Information about a signal decoder.

fullyQualifiedName -> (string)

The fully qualified name of a signal decoder as defined in a vehicle model.

type -> (string)

The network protocol for the vehicle. For example, `CAN_SIGNAL` specifies a protocol that defines how data is communicated between electronic control units (ECUs). `OBD_SIGNAL` specifies a protocol that defines how self-diagnostic data is communicated between ECUs.

interfaceId -> (string)

The ID of a network interface that specifies what network protocol a vehicle follows.

canSignal -> (structure)

Information about signal decoder using the Controller Area Network (CAN) protocol.

messageId -> (integer)

The ID of the message.

isBigEndian -> (boolean)

Whether the byte ordering of a CAN message is big-endian.

isSigned -> (boolean)

Determines whether the message is signed (`true` ) or not (`false` ). If itâs signed, the message can represent both positive and negative numbers. The `isSigned` parameter only applies to the `INTEGER` raw signal type, and it doesnât affect the `FLOATING_POINT` raw signal type.

startBit -> (integer)

Indicates the beginning of the CAN signal. This should always be the least significant bit (LSB).

This value might be different from the value in a DBC file. For little endian signals, `startBit` is the same value as in the DBC file. For big endian signals in a DBC file, the start bit is the most significant bit (MSB). You will have to calculate the LSB instead and pass it as the `startBit` .

offset -> (double)

The offset used to calculate the signal value. Combined with factor, the calculation is `value = raw_value * factor + offset` .

factor -> (double)

A multiplier used to decode the CAN message.

length -> (integer)

How many bytes of data are in the message.

name -> (string)

The name of the signal.

signalValueType -> (string)

The value type of the signal. The default value is `INTEGER` .

obdSignal -> (structure)

Information about signal decoder using the on-board diagnostic (OBD) II protocol.

pidResponseLength -> (integer)

The length of the requested data.

serviceMode -> (integer)

The mode of operation (diagnostic service) in a message.

pid -> (integer)

The diagnostic code used to request data from a vehicle for this signal.

scaling -> (double)

A multiplier used to decode the message.

offset -> (double)

The offset used to calculate the signal value. Combined with scaling, the calculation is `value = raw_value * scaling + offset` .

startByte -> (integer)

Indicates the beginning of the message.

byteLength -> (integer)

The length of a message.

bitRightShift -> (integer)

The number of positions to shift bits in the message.

bitMaskLength -> (integer)

The number of bits to mask in a message.

isSigned -> (boolean)

Determines whether the message is signed (`true` ) or not (`false` ). If itâs signed, the message can represent both positive and negative numbers. The `isSigned` parameter only applies to the `INTEGER` raw signal type, and it doesnât affect the `FLOATING_POINT` raw signal type. The default value is `false` .

signalValueType -> (string)

The value type of the signal. The default value is `INTEGER` .

messageSignal -> (structure)

The decoding information for a specific message which supports higher order data types.

topicName -> (string)

The topic name for the message signal. It corresponds to topics in ROS 2.

structuredMessage -> (tagged union structure)

The structured message for the message signal. It can be defined with either a `primitiveMessageDefinition` , `structuredMessageListDefinition` , or `structuredMessageDefinition` recursively.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `primitiveMessageDefinition`, `structuredMessageListDefinition`, `structuredMessageDefinition`.

primitiveMessageDefinition -> (tagged union structure)

Represents a primitive type node of the complex data structure.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ros2PrimitiveMessageDefinition`.

ros2PrimitiveMessageDefinition -> (structure)

Information about a `PrimitiveMessage` using a ROS 2 compliant primitive type message of the complex data structure.

primitiveType -> (string)

The primitive type (integer, floating point, boolean, etc.) for the ROS 2 primitive message definition.

offset -> (double)

The offset used to calculate the signal value. Combined with scaling, the calculation is `value = raw_value * scaling + offset` .

scaling -> (double)

A multiplier used to decode the message.

upperBound -> (long)

An optional attribute specifying the upper bound for `STRING` and `WSTRING` .

structuredMessageListDefinition -> (structure)

Represents a list type node of the complex data structure.

name -> (string)

The name of the structured message list definition.

memberType -> (tagged union structure)

The member type of the structured message list definition.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `primitiveMessageDefinition`, `structuredMessageListDefinition`, `structuredMessageDefinition`.

primitiveMessageDefinition -> (tagged union structure)

Represents a primitive type node of the complex data structure.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ros2PrimitiveMessageDefinition`.

ros2PrimitiveMessageDefinition -> (structure)

Information about a `PrimitiveMessage` using a ROS 2 compliant primitive type message of the complex data structure.

primitiveType -> (string)

The primitive type (integer, floating point, boolean, etc.) for the ROS 2 primitive message definition.

offset -> (double)

The offset used to calculate the signal value. Combined with scaling, the calculation is `value = raw_value * scaling + offset` .

scaling -> (double)

A multiplier used to decode the message.

upperBound -> (long)

An optional attribute specifying the upper bound for `STRING` and `WSTRING` .

structuredMessageListDefinition -> (structure)

Represents a list type node of the complex data structure.

name -> (string)

The name of the structured message list definition.

( â¦ recursive â¦ )listType -> (string)

The type of list of the structured message list definition.

capacity -> (integer)

The capacity of the structured message list definition when the list type is `FIXED_CAPACITY` or `DYNAMIC_BOUNDED_CAPACITY` .

structuredMessageDefinition -> (list)

Represents a struct type node of the complex data structure.

(structure)

Represents a `StructureMessageName` to `DataType` map element.

fieldName -> (string)

The field name of the structured message. It determines how a data value is referenced in the target language.

( â¦ recursive â¦ )

listType -> (string)

The type of list of the structured message list definition.

capacity -> (integer)

The capacity of the structured message list definition when the list type is `FIXED_CAPACITY` or `DYNAMIC_BOUNDED_CAPACITY` .

structuredMessageDefinition -> (list)

Represents a struct type node of the complex data structure.

(structure)

Represents a `StructureMessageName` to `DataType` map element.

fieldName -> (string)

The field name of the structured message. It determines how a data value is referenced in the target language.

dataType -> (tagged union structure)

The data type.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `primitiveMessageDefinition`, `structuredMessageListDefinition`, `structuredMessageDefinition`.

primitiveMessageDefinition -> (tagged union structure)

Represents a primitive type node of the complex data structure.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `ros2PrimitiveMessageDefinition`.

ros2PrimitiveMessageDefinition -> (structure)

Information about a `PrimitiveMessage` using a ROS 2 compliant primitive type message of the complex data structure.

primitiveType -> (string)

The primitive type (integer, floating point, boolean, etc.) for the ROS 2 primitive message definition.

offset -> (double)

The offset used to calculate the signal value. Combined with scaling, the calculation is `value = raw_value * scaling + offset` .

scaling -> (double)

A multiplier used to decode the message.

upperBound -> (long)

An optional attribute specifying the upper bound for `STRING` and `WSTRING` .

structuredMessageListDefinition -> (structure)

Represents a list type node of the complex data structure.

name -> (string)

The name of the structured message list definition.

( â¦ recursive â¦ )listType -> (string)

The type of list of the structured message list definition.

capacity -> (integer)

The capacity of the structured message list definition when the list type is `FIXED_CAPACITY` or `DYNAMIC_BOUNDED_CAPACITY` .

structuredMessageDefinition -> (list)

Represents a struct type node of the complex data structure.

(structure)

Represents a `StructureMessageName` to `DataType` map element.

fieldName -> (string)

The field name of the structured message. It determines how a data value is referenced in the target language.

( â¦ recursive â¦ )

customDecodingSignal -> (structure)

Information about a [custom signal decoder](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_CustomDecodingSignal.html) .

### Warning

Access to certain Amazon Web Services IoT FleetWise features is currently gated. For more information, see [Amazon Web Services Region and feature availability](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/fleetwise-regions.html) in the *Amazon Web Services IoT FleetWise Developer Guide* .

id -> (string)

The ID of the signal.

nextToken -> (string)

The token to retrieve the next set of results, or `null` if there are no more results.