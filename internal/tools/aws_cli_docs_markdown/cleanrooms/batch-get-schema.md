# batch-get-schemaÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/batch-get-schema.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/batch-get-schema.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# batch-get-schema

## Description

Retrieves multiple schemas by their identifiers.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/BatchGetSchema)

## Synopsis

```
batch-get-schema
--collaboration-identifier <value>
--names <value>
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

`--collaboration-identifier` (string)

A unique identifier for the collaboration that the schemas belong to. Currently accepts collaboration ID.

`--names` (list)

The names for the schema objects to retrieve.

(string)

Syntax:

```
"string" "string" ...
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

schemas -> (list)

The retrieved list of schemas.

(structure)

A schema is a relation within a collaboration.

columns -> (list)

The columns for the relation that this schema represents.

(structure)

A column within a schema relation, derived from the underlying table.

name -> (string)

The name of the column.

type -> (string)

The type of the column.

partitionKeys -> (list)

The partition keys for the dataset underlying this schema.

(structure)

A column within a schema relation, derived from the underlying table.

name -> (string)

The name of the column.

type -> (string)

The type of the column.

analysisRuleTypes -> (list)

The analysis rule types that are associated with the schema. Currently, only one entry is present.

(string)

analysisMethod -> (string)

The analysis method for the schema.

`DIRECT_QUERY` allows SQL queries to be run directly on this table.

`DIRECT_JOB` allows PySpark jobs to be run directly on this table.

`MULTIPLE` allows both SQL queries and PySpark jobs to be run directly on this table.

selectedAnalysisMethods -> (list)

The selected analysis methods for the schema.

(string)

creatorAccountId -> (string)

The unique account ID for the Amazon Web Services account that owns the schema.

name -> (string)

A name for the schema. The schema relation is referred to by this name when queried by a protected query.

collaborationId -> (string)

The unique ID for the collaboration that the schema belongs to.

collaborationArn -> (string)

The unique Amazon Resource Name (ARN) for the collaboration that the schema belongs to.

description -> (string)

A description for the schema.

createTime -> (timestamp)

The time at which the schema was created.

updateTime -> (timestamp)

The most recent time at which the schema was updated.

type -> (string)

The type of schema.

schemaStatusDetails -> (list)

Details about the status of the schema. Currently, only one entry is present.

(structure)

Information about the schema status.

A status of `READY` means that based on the schema analysis rule, queries of the given analysis rule type are properly configured to run queries on this schema.

status -> (string)

The status of the schema, indicating if it is ready to query.

reasons -> (list)

The reasons why the schema status is set to its current state.

(structure)

A reason why the schema status is set to its current value.

code -> (string)

The schema status reason code.

message -> (string)

An explanation of the schema status reason code.

analysisRuleType -> (string)

The analysis rule type for which the schema status has been evaluated.

configurations -> (list)

The configuration details of the schema analysis rule for the given type.

(string)

analysisType -> (string)

The type of analysis that can be performed on the schema.

A schema can have an `analysisType` of `DIRECT_ANALYSIS` , `ADDITIONAL_ANALYSIS_FOR_AUDIENCE_GENERATION` , or both.

schemaTypeProperties -> (tagged union structure)

The schema type properties.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `idMappingTable`.

idMappingTable -> (structure)

The ID mapping table for the schema type properties.

idMappingTableInputSource -> (list)

Defines which ID namespace associations are used to create the ID mapping table.

(structure)

The input source of the ID mapping table.

idNamespaceAssociationId -> (string)

The unique identifier of the ID namespace association.

type -> (string)

The type of the input source of the ID mapping table.

errors -> (list)

Error reasons for schemas that could not be retrieved. One error is returned for every schema that could not be retrieved.

(structure)

An error describing why a schema could not be fetched.

name -> (string)

An error name for the error.

code -> (string)

An error code for the error.

message -> (string)

An error message for the error.