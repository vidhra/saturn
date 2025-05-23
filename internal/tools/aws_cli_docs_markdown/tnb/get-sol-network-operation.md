# get-sol-network-operationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/tnb/get-sol-network-operation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/tnb/get-sol-network-operation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [tnb](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/tnb/index.html#cli-aws-tnb) ]

# get-sol-network-operation

## Description

Gets the details of a network operation, including the tasks involved in the network operation and the status of the tasks.

A network operation is any operation that is done to your network, such as network instance instantiation or termination.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/tnb-2008-10-21/GetSolNetworkOperation)

`get-sol-network-operation` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
get-sol-network-operation
--ns-lcm-op-occ-id <value>
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

`--ns-lcm-op-occ-id` (string)

The identifier of the network operation.

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

arn -> (string)

Network operation ARN.

error -> (structure)

Error related to this specific network operation occurrence.

detail -> (string)

A human-readable explanation specific to this occurrence of the problem.

title -> (string)

A human-readable title of the problem type.

id -> (string)

ID of this network operation occurrence.

lcmOperationType -> (string)

Type of the operation represented by this occurrence.

metadata -> (structure)

Metadata of this network operation occurrence.

createdAt -> (timestamp)

The date that the resource was created.

instantiateMetadata -> (structure)

Metadata related to the network operation occurrence for network instantiation. This is populated only if the lcmOperationType is `INSTANTIATE` .

additionalParamsForNs -> (document)

The configurable properties used during instantiation.

nsdInfoId -> (string)

The network service descriptor used for instantiating the network instance.

lastModified -> (timestamp)

The date that the resource was last modified.

modifyVnfInfoMetadata -> (structure)

Metadata related to the network operation occurrence for network function updates in a network instance. This is populated only if the lcmOperationType is `UPDATE` and the updateType is `MODIFY_VNF_INFORMATION` .

vnfConfigurableProperties -> (document)

The configurable properties used during update of the network function instance.

vnfInstanceId -> (string)

The network function instance that was updated in the network instance.

updateNsMetadata -> (structure)

Metadata related to the network operation occurrence for network instance updates. This is populated only if the lcmOperationType is `UPDATE` and the updateType is `UPDATE_NS` .

additionalParamsForNs -> (document)

The configurable properties used during update.

nsdInfoId -> (string)

The network service descriptor used for updating the network instance.

nsInstanceId -> (string)

ID of the network operation instance.

operationState -> (string)

The state of the network operation.

tags -> (map)

A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.

key -> (string)

value -> (string)

tasks -> (list)

All tasks associated with this operation occurrence.

(structure)

Gets the details of a network operation.

A network operation is any operation that is done to your network, such as network instance instantiation or termination.

taskContext -> (map)

Context for the network operation task.

key -> (string)

value -> (string)

taskEndTime -> (timestamp)

Task end time.

taskErrorDetails -> (structure)

Task error details.

cause -> (string)

Error cause.

details -> (string)

Error details.

taskName -> (string)

Task name.

taskStartTime -> (timestamp)

Task start time.

taskStatus -> (string)

Task status.

updateType -> (string)

Type of the update. Only present if the network operation lcmOperationType is `UPDATE` .