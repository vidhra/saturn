# start-import-taskÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/start-import-task.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/start-import-task.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [neptune-graph](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/neptune-graph/index.html#cli-aws-neptune-graph) ]

# start-import-task

## Description

Import data into existing Neptune Analytics graph from Amazon Simple Storage Service (S3). The graph needs to be empty and in the AVAILABLE state.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/neptune-graph-2023-11-29/StartImportTask)

## Synopsis

```
start-import-task
[--import-options <value>]
[--fail-on-error | --no-fail-on-error]
--source <value>
[--format <value>]
[--parquet-type <value>]
[--blank-node-handling <value>]
--graph-identifier <value>
--role-arn <value>
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

`--import-options` (tagged union structure)

Options for how to perform an import.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `neptune`.

neptune -> (structure)

Options for importing data from a Neptune database.

s3ExportPath -> (string)

The path to an S3 bucket from which to import data.

s3ExportKmsKeyId -> (string)

The KMS key to use to encrypt data in the S3 bucket where the graph data is exported

preserveDefaultVertexLabels -> (boolean)

Neptune Analytics supports label-less vertices and no labels are assigned unless one is explicitly provided. Neptune assigns default labels when none is explicitly provided. When importing the data into Neptune Analytics, the default vertex labels can be omitted by setting *preserveDefaultVertexLabels* to false. Note that if the vertex only has default labels, and has no other properties or edges, then the vertex will effectively not get imported into Neptune Analytics when preserveDefaultVertexLabels is set to false.

preserveEdgeIds -> (boolean)

Neptune Analytics currently does not support user defined edge ids. The edge ids are not imported by default. They are imported if *preserveEdgeIds* is set to true, and ids are stored as properties on the relationships with the property name *neptuneEdgeId* .

Shorthand Syntax:

```
neptune={s3ExportPath=string,s3ExportKmsKeyId=string,preserveDefaultVertexLabels=boolean,preserveEdgeIds=boolean}
```

JSON Syntax:

```
{
  "neptune": {
    "s3ExportPath": "string",
    "s3ExportKmsKeyId": "string",
    "preserveDefaultVertexLabels": true|false,
    "preserveEdgeIds": true|false
  }
}
```

`--fail-on-error` | `--no-fail-on-error` (boolean)

If set to true, the task halts when an import error is encountered. If set to false, the task skips the data that caused the error and continues if possible.

`--source` (string)

A URL identifying the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.

`--format` (string)

Specifies the format of Amazon S3 data to be imported. Valid values are CSV, which identifies the Gremlin CSV format or OPENCYPHER, which identies the openCypher load format.

Possible values:

- `CSV`
- `OPEN_CYPHER`
- `PARQUET`
- `NTRIPLES`

`--parquet-type` (string)

The parquet type of the import task.

Possible values:

- `COLUMNAR`

`--blank-node-handling` (string)

The method to handle blank nodes in the dataset. Currently, only `convertToIri` is supported, meaning blank nodes are converted to unique IRIs at load time. Must be provided when format is `ntriples` . For more information, see [Handling RDF values](https://docs.aws.amazon.com/neptune-analytics/latest/userguide/using-rdf-data.html#rdf-handling) .

Possible values:

- `convertToIri`

`--graph-identifier` (string)

The unique identifier of the Neptune Analytics graph.

`--role-arn` (string)

The ARN of the IAM role that will allow access to the data that is to be imported.

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

The unique identifier of the Neptune Analytics graph.

taskId -> (string)

The unique identifier of the import task.

source -> (string)

A URL identifying the location of the data to be imported. This can be an Amazon S3 path, or can point to a Neptune database endpoint or snapshot.

format -> (string)

Specifies the format of Amazon S3 data to be imported. Valid values are CSV, which identifies the Gremlin CSV format or OPENCYPHER, which identies the openCypher load format.

parquetType -> (string)

The parquet type of the import task.

roleArn -> (string)

The ARN of the IAM role that will allow access to the data that is to be imported.

status -> (string)

The status of the import task.

importOptions -> (tagged union structure)

Options for how to perform an import.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `neptune`.

neptune -> (structure)

Options for importing data from a Neptune database.

s3ExportPath -> (string)

The path to an S3 bucket from which to import data.

s3ExportKmsKeyId -> (string)

The KMS key to use to encrypt data in the S3 bucket where the graph data is exported

preserveDefaultVertexLabels -> (boolean)

Neptune Analytics supports label-less vertices and no labels are assigned unless one is explicitly provided. Neptune assigns default labels when none is explicitly provided. When importing the data into Neptune Analytics, the default vertex labels can be omitted by setting *preserveDefaultVertexLabels* to false. Note that if the vertex only has default labels, and has no other properties or edges, then the vertex will effectively not get imported into Neptune Analytics when preserveDefaultVertexLabels is set to false.

preserveEdgeIds -> (boolean)

Neptune Analytics currently does not support user defined edge ids. The edge ids are not imported by default. They are imported if *preserveEdgeIds* is set to true, and ids are stored as properties on the relationships with the property name *neptuneEdgeId* .