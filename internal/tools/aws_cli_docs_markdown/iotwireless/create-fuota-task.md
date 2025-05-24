# create-fuota-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-fuota-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/create-fuota-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotwireless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotwireless/index.html#cli-aws-iotwireless) ]

# create-fuota-task

## Description

Creates a FUOTA task.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotwireless-2020-11-22/CreateFuotaTask)

## Synopsis

```
create-fuota-task
[--name <value>]
[--description <value>]
[--client-request-token <value>]
--firmware-update-image <value>
--firmware-update-role <value>
[--tags <value>]
[--redundancy-percent <value>]
[--fragment-size-bytes <value>]
[--fragment-interval-ms <value>]
[--descriptor <value>]
[--lorawan <value>]
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

The name of a FUOTA task.

`--description` (string)

The description of the new resource.

`--client-request-token` (string)

Each resource must have a unique client request token. The client token is used to implement idempotency. It ensures that the request completes no more than one time. If you retry a request with the same token and the same parameters, the request will complete successfully. However, if you try to create a new resource using the same token but different parameters, an HTTP 409 conflict occurs. If you omit this value, AWS SDKs will automatically generate a unique client request. For more information about idempotency, see [Ensuring idempotency in Amazon EC2 API requests](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

`--firmware-update-image` (string)

The S3 URI points to a firmware update image that is to be used with a FUOTA task.

`--firmware-update-role` (string)

The firmware update role that is to be used with a FUOTA task.

`--tags` (list)

The tag to attach to the specified resource. Tags are metadata that you can use to manage a resource.

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

`--redundancy-percent` (integer)

The percentage of the added fragments that are redundant. For example, if the size of the firmware image file is 100 bytes and the fragment size is 10 bytes, with `RedundancyPercent` set to 50(%), the final number of encoded fragments is (100 / 10) + (100 / 10 * 50%) = 15.

`--fragment-size-bytes` (integer)

The size of each fragment in bytes. This parameter is supported only for FUOTA tasks with multicast groups.

`--fragment-interval-ms` (integer)

The interval for sending fragments in milliseconds, rounded to the nearest second.

### Note

This interval only determines the timing for when the Cloud sends down the fragments to yor device. There can be a delay for when your device will receive these fragments. This delay depends on the deviceâs class and the communication delay with the cloud.

`--descriptor` (string)

The descriptor is the metadata about the file that is transferred to the device using FUOTA, such as the software version. It is a binary field encoded in base64.

`--lorawan` (structure)

The LoRaWAN information used with a FUOTA task.

RfRegion -> (string)

Supported RfRegions

Shorthand Syntax:

```
RfRegion=string
```

JSON Syntax:

```
{
  "RfRegion": "EU868"|"US915"|"AU915"|"AS923-1"|"AS923-2"|"AS923-3"|"AS923-4"|"EU433"|"CN470"|"CN779"|"RU864"|"KR920"|"IN865"
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

## Output

Arn -> (string)

The arn of a FUOTA task.

Id -> (string)

The ID of a FUOTA task.