# describe-entityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/describe-entity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/describe-entity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# describe-entity

## Description

Provides details regarding the entity used with the connection type, with a description of the data model for each field in the selected entity.

The response includes all the fields which make up the entity.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/DescribeEntity)

`describe-entity` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Fields`

## Synopsis

```
describe-entity
--connection-name <value>
[--catalog-id <value>]
--entity-name <value>
[--data-store-api-version <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--connection-name` (string)

The name of the connection that contains the connection type credentials.

`--catalog-id` (string)

The catalog ID of the catalog that contains the connection. This can be null, By default, the Amazon Web Services Account ID is the catalog ID.

`--entity-name` (string)

The name of the entity that you want to describe from the connection type.

`--data-store-api-version` (string)

The version of the API used for the data store.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

Fields -> (list)

Describes the fields for that connector entity. This is the list of `Field` objects. `Field` is very similar to column in a database. The `Field` object has information about different properties associated with fields in the connector.

(structure)

The `Field` object has information about the different properties associated with a field in the connector.

FieldName -> (string)

A unique identifier for the field.

Label -> (string)

A readable label used for the field.

Description -> (string)

A description of the field.

FieldType -> (string)

The type of data in the field.

IsPrimaryKey -> (boolean)

Indicates whether this field can used as a primary key for the given entity.

IsNullable -> (boolean)

Indicates whether this field can be nullable or not.

IsRetrievable -> (boolean)

Indicates whether this field can be added in Select clause of SQL query or whether it is retrievable or not.

IsFilterable -> (boolean)

Indicates whether this field can used in a filter clause (`WHERE` clause) of a SQL statement when querying data.

IsPartitionable -> (boolean)

Indicates whether a given field can be used in partitioning the query made to SaaS.

IsCreateable -> (boolean)

Indicates whether this field can be created as part of a destination write.

IsUpdateable -> (boolean)

Indicates whether this field can be updated as part of a destination write.

IsUpsertable -> (boolean)

Indicates whether this field can be upserted as part of a destination write.

IsDefaultOnCreate -> (boolean)

Indicates whether this field is populated automatically when the object is created, such as a created at timestamp.

SupportedValues -> (list)

A list of supported values for the field.

(string)

SupportedFilterOperators -> (list)

Indicates the support filter operators for this field.

(string)

ParentField -> (string)

A parent field name for a nested field.

NativeDataType -> (string)

The data type returned by the SaaS API, such as âpicklistâ or âtextareaâ from Salesforce.

CustomProperties -> (map)

Optional map of keys which may be returned.

key -> (string)

value -> (string)

NextToken -> (string)

A continuation token, present if the current segment is not the last.