# list-model-manifest-nodesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/list-model-manifest-nodes.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/list-model-manifest-nodes.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotfleetwise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotfleetwise/index.html#cli-aws-iotfleetwise) ]

# list-model-manifest-nodes

## Description

Lists information about nodes specified in a vehicle model (model manifest).

### Note

This API operation uses pagination. Specify the `nextToken` parameter in the request to return more results.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotfleetwise-2021-06-17/ListModelManifestNodes)

`list-model-manifest-nodes` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `nodes`

## Synopsis

```
list-model-manifest-nodes
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

The name of the vehicle model to list information about.

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

nodes -> (list)

A list of information about nodes.

(tagged union structure)

A general abstraction of a signal. A node can be specified as an actuator, attribute, branch, or sensor.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `branch`, `sensor`, `actuator`, `attribute`, `struct`, `property`.

branch -> (structure)

Information about a node specified as a branch.

### Note

A group of signals that are defined in a hierarchical structure.

fullyQualifiedName -> (string)

The fully qualified name of the branch. For example, the fully qualified name of a branch might be `Vehicle.Body.Engine` .

description -> (string)

A brief description of the branch.

deprecationMessage -> (string)

The deprecation message for the node or the branch that was moved or deleted.

comment -> (string)

A comment in addition to the description.

sensor -> (structure)

An input component that reports the environmental condition of a vehicle.

### Note

You can collect data about fluid levels, temperatures, vibrations, or battery voltage from sensors.

fullyQualifiedName -> (string)

The fully qualified name of the sensor. For example, the fully qualified name of a sensor might be `Vehicle.Body.Engine.Battery` .

dataType -> (string)

The specified data type of the sensor.

description -> (string)

A brief description of a sensor.

unit -> (string)

The scientific unit of measurement for data collected by the sensor.

allowedValues -> (list)

A list of possible values a sensor can take.

(string)

min -> (double)

The specified possible minimum value of the sensor.

max -> (double)

The specified possible maximum value of the sensor.

deprecationMessage -> (string)

The deprecation message for the node or the branch that was moved or deleted.

comment -> (string)

A comment in addition to the description.

structFullyQualifiedName -> (string)

The fully qualified name of the struct node for a sensor if the data type of the actuator is `Struct` or `StructArray` . For example, the struct fully qualified name of a sensor might be `Vehicle.ADAS.CameraStruct` .

actuator -> (structure)

Information about a node specified as an actuator.

### Note

An actuator is a digital representation of a vehicle device.

fullyQualifiedName -> (string)

The fully qualified name of the actuator. For example, the fully qualified name of an actuator might be `Vehicle.Front.Left.Door.Lock` .

dataType -> (string)

The specified data type of the actuator.

description -> (string)

A brief description of the actuator.

unit -> (string)

The scientific unit for the actuator.

allowedValues -> (list)

A list of possible values an actuator can take.

(string)

min -> (double)

The specified possible minimum value of an actuator.

max -> (double)

The specified possible maximum value of an actuator.

assignedValue -> (string)

A specified value for the actuator.

deprecationMessage -> (string)

The deprecation message for the node or the branch that was moved or deleted.

comment -> (string)

A comment in addition to the description.

structFullyQualifiedName -> (string)

The fully qualified name of the struct node for the actuator if the data type of the actuator is `Struct` or `StructArray` . For example, the struct fully qualified name of an actuator might be `Vehicle.Door.LockStruct` .

attribute -> (structure)

Information about a node specified as an attribute.

### Note

An attribute represents static information about a vehicle.

fullyQualifiedName -> (string)

The fully qualified name of the attribute. For example, the fully qualified name of an attribute might be `Vehicle.Body.Engine.Type` .

dataType -> (string)

The specified data type of the attribute.

description -> (string)

A brief description of the attribute.

unit -> (string)

The scientific unit for the attribute.

allowedValues -> (list)

A list of possible values an attribute can be assigned.

(string)

min -> (double)

The specified possible minimum value of the attribute.

max -> (double)

The specified possible maximum value of the attribute.

assignedValue -> (string)

A specified value for the attribute.

defaultValue -> (string)

The default value of the attribute.

deprecationMessage -> (string)

The deprecation message for the node or the branch that was moved or deleted.

comment -> (string)

A comment in addition to the description.

struct -> (structure)

Represents a complex or higher-order data structure.

fullyQualifiedName -> (string)

The fully qualified name of the custom structure. For example, the fully qualified name of a custom structure might be `ComplexDataTypes.VehicleDataTypes.SVMCamera` .

description -> (string)

A brief description of the custom structure.

deprecationMessage -> (string)

The deprecation message for the node or the branch that was moved or deleted.

comment -> (string)

A comment in addition to the description.

property -> (structure)

Represents a member of the complex data structure. The `datatype` of the property can be either primitive or another `struct` .

fullyQualifiedName -> (string)

The fully qualified name of the custom property. For example, the fully qualified name of a custom property might be `ComplexDataTypes.VehicleDataTypes.SVMCamera.FPS` .

dataType -> (string)

The data type for the custom property.

dataEncoding -> (string)

Indicates whether the property is binary data.

description -> (string)

A brief description of the custom property.

deprecationMessage -> (string)

The deprecation message for the node or the branch that was moved or deleted.

comment -> (string)

A comment in addition to the description.

structFullyQualifiedName -> (string)

The fully qualified name of the struct node for the custom property if the data type of the custom property is `Struct` or `StructArray` .

nextToken -> (string)

The token to retrieve the next set of results, or `null` if there are no more results.