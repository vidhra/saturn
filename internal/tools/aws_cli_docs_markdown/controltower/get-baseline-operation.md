# get-baseline-operationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-baseline-operation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/get-baseline-operation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [controltower](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/index.html#cli-aws-controltower) ]

# get-baseline-operation

## Description

Returns the details of an asynchronous baseline operation, as initiated by any of these APIs: `EnableBaseline` , `DisableBaseline` , `UpdateEnabledBaseline` , `ResetEnabledBaseline` . A status message is displayed in case of operation failure. For usage examples, see ` *the Amazon Web Services Control Tower User Guide* [https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples](https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples).html`__ .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/controltower-2018-05-10/GetBaselineOperation)

## Synopsis

```
get-baseline-operation
--operation-identifier <value>
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

`--operation-identifier` (string)

The operation ID returned from mutating asynchronous APIs (Enable, Disable, Update, Reset).

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

baselineOperation -> (structure)

A `baselineOperation` object that shows information about the specified operation ID.

endTime -> (timestamp)

The end time of the operation (if applicable), in ISO 8601 format.

operationIdentifier -> (string)

The identifier of the specified operation.

operationType -> (string)

An enumerated type (`enum` ) with possible values of `ENABLE_BASELINE` , `DISABLE_BASELINE` , `UPDATE_ENABLED_BASELINE` , or `RESET_ENABLED_BASELINE` .

startTime -> (timestamp)

The start time of the operation, in ISO 8601 format.

status -> (string)

An enumerated type (`enum` ) with possible values of `SUCCEEDED` , `FAILED` , or `IN_PROGRESS` .

statusMessage -> (string)

A status message that gives more information about the operationâs status, if applicable.