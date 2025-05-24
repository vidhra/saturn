# get-propertygraph-streamÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/get-propertygraph-stream.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/get-propertygraph-stream.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptunedata](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/index.html#cli-aws-neptunedata) ]

# get-propertygraph-stream

## Description

Gets a stream for a property graph.

With the Neptune Streams feature, you can generate a complete sequence of change-log entries that record every change made to your graph data as it happens. `GetPropertygraphStream` lets you collect these change-log entries for a property graph.

The Neptune streams feature needs to be enabled on your Neptune DBcluster. To enable streams, set the [neptune_streams](https://docs.aws.amazon.com/neptune/latest/userguide/parameters.html#parameters-db-cluster-parameters-neptune_streams) DB cluster parameter to `1` .

See [Capturing graph changes in real time using Neptune streams](https://docs.aws.amazon.com/neptune/latest/userguide/streams.html) .

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that allows the [neptune-db:GetStreamRecords](https://docs.aws.amazon.com/neptune/latest/userguide/iam-dp-actions.html#getstreamrecords) IAM action in that cluster.

When invoking this operation in a Neptune cluster that has IAM authentication enabled, the IAM user or role making the request must have a policy attached that enables one of the following IAM actions, depending on the query:

Note that you can restrict property-graph queries using the following IAM context keys:

- [neptune-db:QueryLanguage:Gremlin](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys)
- [neptune-db:QueryLanguage:OpenCypher](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html#iam-neptune-condition-keys)

See [Condition keys available in Neptune IAM data-access policy statements](https://docs.aws.amazon.com/neptune/latest/userguide/iam-data-condition-keys.html) ).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptunedata-2023-08-01/GetPropertygraphStream)

`get-propertygraph-stream` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
get-propertygraph-stream
[--limit <value>]
[--iterator-type <value>]
[--commit-num <value>]
[--op-num <value>]
[--encoding <value>]
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

`--limit` (long)

Specifies the maximum number of records to return. There is also a size limit of 10 MB on the response that canât be modified and that takes precedence over the number of records specified in the `limit` parameter. The response does include a threshold-breaching record if the 10 MB limit was reached.

The range for `limit` is 1 to 100,000, with a default of 10.

`--iterator-type` (string)

Can be one of:

- `AT_SEQUENCE_NUMBER` â Indicates that reading should start from the event sequence number specified jointly by the `commitNum` and `opNum` parameters.
- `AFTER_SEQUENCE_NUMBER` â Indicates that reading should start right after the event sequence number specified jointly by the `commitNum` and `opNum` parameters.
- `TRIM_HORIZON` â Indicates that reading should start at the last untrimmed record in the system, which is the oldest unexpired (not yet deleted) record in the change-log stream.
- `LATEST` â Indicates that reading should start at the most recent record in the system, which is the latest unexpired (not yet deleted) record in the change-log stream.

Possible values:

- `AT_SEQUENCE_NUMBER`
- `AFTER_SEQUENCE_NUMBER`
- `TRIM_HORIZON`
- `LATEST`

`--commit-num` (long)

The commit number of the starting record to read from the change-log stream. This parameter is required when `iteratorType` is``AT_SEQUENCE_NUMBER`` or `AFTER_SEQUENCE_NUMBER` , and ignored when `iteratorType` is `TRIM_HORIZON` or `LATEST` .

`--op-num` (long)

The operation sequence number within the specified commit to start reading from in the change-log stream data. The default is `1` .

`--encoding` (string)

If set to TRUE, Neptune compresses the response using gzip encoding.

Possible values:

- `gzip`

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

lastEventId -> (map)

Sequence identifier of the last change in the stream response.

An event ID is composed of two fields: a `commitNum` , which identifies a transaction that changed the graph, and an `opNum` , which identifies a specific operation within that transaction:

key -> (string)

value -> (string)

lastTrxTimestampInMillis -> (long)

The time at which the commit for the transaction was requested, in milliseconds from the Unix epoch.

format -> (string)

Serialization format for the change records being returned. Currently, the only supported value is `PG_JSON` .

records -> (list)

An array of serialized change-log stream records included in the response.

(structure)

Structure of a property graph record.

commitTimestampInMillis -> (long)

The time at which the commit for the transaction was requested, in milliseconds from the Unix epoch.

eventId -> (map)

The sequence identifier of the stream change record.

key -> (string)

value -> (string)

data -> (structure)

The serialized Gremlin or openCypher change record.

id -> (string)

The ID of the Gremlin or openCypher element.

type -> (string)

The type of this Gremlin or openCypher element. Must be one of:

- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/get-propertygraph-stream.html#id1)`v1` ** - Vertex label for Gremlin, or node label for openCypher.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/get-propertygraph-stream.html#id3)`vp` ** - Vertex properties for Gremlin, or node properties for openCypher.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/get-propertygraph-stream.html#id5)`e` ** - Edge and edge label for Gremlin, or relationship and relationship type for openCypher.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptunedata/get-propertygraph-stream.html#id7)`ep` ** - Edge properties for Gremlin, or relationship properties for openCypher.

key -> (string)

The property name. For element labels, this is `label` .

value -> (document)

This is a JSON object that contains a value field for the value itself, and a datatype field for the JSON data type of that value:

from -> (string)

If this is an edge (type = `e` ), the ID of the corresponding `from` vertex or source node.

to -> (string)

If this is an edge (type = `e` ), the ID of the corresponding `to` vertex or target node.

op -> (string)

The operation that created the change.

isLastOp -> (boolean)

Only present if this operation is the last one in its transaction. If present, it is set to true. It is useful for ensuring that an entire transaction is consumed.

totalRecords -> (integer)

The total number of records in the response.