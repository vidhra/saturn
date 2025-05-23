# publishÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/publish.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/publish.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-data/index.html#cli-aws-iot-data) ]

# publish

## Description

Publishes an MQTT message.

Requires permission to access the [Publish](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

For more information about MQTT messages, see [MQTT Protocol](http://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) in the IoT Developer Guide.

For more information about messaging costs, see [Amazon Web Services IoT Core pricing - Messaging](http://aws.amazon.com/iot-core/pricing/#Messaging) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-data-2015-05-28/Publish)

### Note

For production code it is strongly recommended to use the custom endpoint for your account (retrievable via the iot describe-endpoint command) to ensure best availability and reachability of the service. The default endpoints (intended for testing purposes only) can be found at [https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#iot-core-data-plane-endpoints)

## Synopsis

```
publish
--topic <value>
[--qos <value>]
[--retain | --no-retain]
[--payload <value>]
[--user-properties <value>]
[--payload-format-indicator <value>]
[--content-type <value>]
[--response-topic <value>]
[--correlation-data <value>]
[--message-expiry <value>]
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

`--topic` (string)

The name of the MQTT topic.

`--qos` (integer)

The Quality of Service (QoS) level. The default QoS level is 0.

`--retain` | `--no-retain` (boolean)

A Boolean value that determines whether to set the RETAIN flag when the message is published.

Setting the RETAIN flag causes the message to be retained and sent to new subscribers to the topic.

Valid values: `true` | `false`

Default value: `false`

`--payload` (blob)

The message body. MQTT accepts text, binary, and empty (null) message payloads.

Publishing an empty (null) payload with **retain** = `true` deletes the retained message identified by **topic** from Amazon Web Services IoT Core.

`--user-properties` (JSON)

A JSON string that contains an array of JSON objects. If you donât use Amazon Web Services SDK or CLI, you must encode the JSON string to base64 format before adding it to the HTTP header. `userProperties` is an HTTP header value in the API.

The following example `userProperties` parameter is a JSON string which represents two User Properties. Note that it needs to be base64-encoded:

`[{"deviceName": "alpha"}, {"deviceCnt": "45"}]`

`--payload-format-indicator` (string)

An `Enum` string value that indicates whether the payload is formatted as UTF-8. `payloadFormatIndicator` is an HTTP header value in the API.

Possible values:

- `UNSPECIFIED_BYTES`
- `UTF8_DATA`

`--content-type` (string)

A UTF-8 encoded string that describes the content of the publishing message.

`--response-topic` (string)

A UTF-8 encoded string thatâs used as the topic name for a response message. The response topic is used to describe the topic which the receiver should publish to as part of the request-response flow. The topic must not contain wildcard characters.

`--correlation-data` (string)

The base64-encoded binary data used by the sender of the request message to identify which request the response message is for when itâs received. `correlationData` is an HTTP header value in the API.

`--message-expiry` (long)

A user-defined integer value that represents the message expiry interval in seconds. If absent, the message doesnât expire. For more information about the limits of `messageExpiry` , see [Amazon Web Services IoT Core message broker and protocol limits and quotas](https://docs.aws.amazon.com/general/latest/gr/iot-core.html#message-broker-limits) from the Amazon Web Services Reference Guide.

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

None