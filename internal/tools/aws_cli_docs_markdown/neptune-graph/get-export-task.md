# get-export-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/get-export-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/get-export-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune-graph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/index.html#cli-aws-neptune-graph) ]

# get-export-task

## Description

Retrieves a specified export task.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-graph-2023-11-29/GetExportTask)

## Synopsis

```
get-export-task
--task-identifier <value>
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

`--task-identifier` (string)

The unique identifier of the export task.

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

graphId -> (string)

The source graph identifier of the export task.

roleArn -> (string)

The ARN of the IAM role that will allow data to be exported to the destination.

taskId -> (string)

The unique identifier of the export task.

status -> (string)

The current status of the export task.

format -> (string)

The format of the export task.

destination -> (string)

The Amazon S3 URI of the export task where data will be exported.

kmsKeyIdentifier -> (string)

The KMS key identifier of the export task.

parquetType -> (string)

The parquet type of the export task.

statusReason -> (string)

The reason that the export task has this status value.

exportTaskDetails -> (structure)

The details of the export task.

startTime -> (timestamp)

The start time of the export task.

timeElapsedSeconds -> (long)

The time elapsed, in seconds, since the start time of the export task.

progressPercentage -> (integer)

The number of progress percentage of the export task.

numVerticesWritten -> (long)

The number of exported vertices.

numEdgesWritten -> (long)

The number of exported edges.

exportFilter -> (structure)

The export filter of the export task.

vertexFilter -> (map)

Used to specify filters on a per-label basis for vertices. This allows you to control which vertex labels and properties are included in the export.

key -> (string)

value -> (structure)

Specifies whihc properties of that label should be included in the export.

properties -> (map)

Each property is defined by a key-value pair, where the key is the desired output property name (e.g. ânameâ), and the value is an object.

key -> (string)

value -> (structure)

A structure representing a propertyâs attributes. It is a map object of outputType, sourcePropertyName and multiValueHandling.

outputType -> (string)

Specifies the data type to use for the property in the exported data (e.g. âStringâ, âIntâ, âFloatâ). If a type is not provided, the export process will determine the type. If a given property is present as multiple types (e.g. one vertex has âheightâ stored as a double, and another edge has it stored as a string), the type will be of Any type, otherwise, it will be the type of the property as present in vertices.

sourcePropertyName -> (string)

The name of the property as it exists in the original graph data. If not provided, it is assumed that the key matches the desired sourcePropertyName.

multiValueHandling -> (string)

Specifies how to handle properties that have multiple values. Can be either `TO_LIST` to export all values as a list, or `PICK_FIRST` to export the first value encountered. If not specified, the default value is `PICK_FIRST` .

edgeFilter -> (map)

Used to specify filters on a per-label basis for edges. This allows you to control which edge labels and properties are included in the export.

key -> (string)

value -> (structure)

Specifies whihc properties of that label should be included in the export.

properties -> (map)

Each property is defined by a key-value pair, where the key is the desired output property name (e.g. ânameâ), and the value is an object.

key -> (string)

value -> (structure)

A structure representing a propertyâs attributes. It is a map object of outputType, sourcePropertyName and multiValueHandling.

outputType -> (string)

Specifies the data type to use for the property in the exported data (e.g. âStringâ, âIntâ, âFloatâ). If a type is not provided, the export process will determine the type. If a given property is present as multiple types (e.g. one vertex has âheightâ stored as a double, and another edge has it stored as a string), the type will be of Any type, otherwise, it will be the type of the property as present in vertices.

sourcePropertyName -> (string)

The name of the property as it exists in the original graph data. If not provided, it is assumed that the key matches the desired sourcePropertyName.

multiValueHandling -> (string)

Specifies how to handle properties that have multiple values. Can be either `TO_LIST` to export all values as a list, or `PICK_FIRST` to export the first value encountered. If not specified, the default value is `PICK_FIRST` .