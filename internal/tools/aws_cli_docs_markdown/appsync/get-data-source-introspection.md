# get-data-source-introspectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-data-source-introspection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/get-data-source-introspection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appsync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/index.html#cli-aws-appsync) ]

# get-data-source-introspection

## Description

Retrieves the record of an existing introspection. If the retrieval is successful, the result of the instrospection will also be returned. If the retrieval fails the operation, an error message will be returned instead.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/GetDataSourceIntrospection)

## Synopsis

```
get-data-source-introspection
--introspection-id <value>
[--include-models-sdl | --no-include-models-sdl]
[--next-token <value>]
[--max-results <value>]
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

`--introspection-id` (string)

The introspection ID. Each introspection contains a unique ID that can be used to reference the instrospection record.

`--include-models-sdl` | `--no-include-models-sdl` (boolean)

A boolean flag that determines whether SDL should be generated for introspected types. If set to `true` , each model will contain an `sdl` property that contains the SDL for that type. The SDL only contains the type data and no additional metadata or directives.

`--next-token` (string)

Determines the number of types to be returned in a single response before paginating. This value is typically taken from `nextToken` value from the previous response.

`--max-results` (integer)

The maximum number of introspected types that will be returned in a single response.

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

introspectionId -> (string)

The introspection ID. Each introspection contains a unique ID that can be used to reference the instrospection record.

introspectionStatus -> (string)

The status of the introspection during retrieval. By default, when a new instrospection is being retrieved, the status will be set to `PROCESSING` . Once the operation has been completed, the status will change to `SUCCESS` or `FAILED` depending on how the data was parsed. A `FAILED` operation will return an error and its details as an `introspectionStatusDetail` .

introspectionStatusDetail -> (string)

The error detail field. When a `FAILED` `introspectionStatus` is returned, the `introspectionStatusDetail` will also return the exact error that was generated during the operation.

introspectionResult -> (structure)

The `DataSourceIntrospectionResult` object data.

models -> (list)

The array of `DataSourceIntrospectionModel` objects.

(structure)

Contains the introspected data that was retrieved from the data source.

name -> (string)

The name of the model. For example, this could be the name of a single table in a database.

fields -> (list)

The `DataSourceIntrospectionModelField` object data.

(structure)

Represents the fields that were retrieved from the introspected data.

name -> (string)

The name of the field that was retrieved from the introspected data.

type -> (structure)

The `DataSourceIntrospectionModelFieldType` object data.

kind -> (string)

Specifies the classification of data. For example, this could be set to values like `Scalar` or `NonNull` to indicate a fundamental property of the field.

Valid values include:

- `Scalar` : Indicates the value is a primitive type (scalar).
- `NonNull` : Indicates the field cannot be `null` .
- `List` : Indicates the field contains a list.

name -> (string)

The name of the data type that represents the field. For example, `String` is a valid `name` value.

type -> (structure)

The `DataSourceIntrospectionModelFieldType` object data. The `type` is only present if `DataSourceIntrospectionModelFieldType.kind` is set to `NonNull` or `List` .

The `type` typically contains its own `kind` and `name` fields to represent the actual type data. For instance, `type` could contain a `kind` value of `Scalar` with a `name` value of `String` . The values `Scalar` and `String` will be collectively stored in the `values` field.

kind -> (string)

Specifies the classification of data. For example, this could be set to values like `Scalar` or `NonNull` to indicate a fundamental property of the field.

Valid values include:

- `Scalar` : Indicates the value is a primitive type (scalar).
- `NonNull` : Indicates the field cannot be `null` .
- `List` : Indicates the field contains a list.

name -> (string)

The name of the data type that represents the field. For example, `String` is a valid `name` value.

( â¦ recursive â¦ )values -> (list)

The values of the `type` field. This field represents the AppSync data type equivalent of the introspected field.

(string)

values -> (list)

The values of the `type` field. This field represents the AppSync data type equivalent of the introspected field.

(string)

length -> (long)

The length value of the introspected field.

primaryKey -> (structure)

The primary key stored as a `DataSourceIntrospectionModelIndex` object.

name -> (string)

The name of the index.

fields -> (list)

The fields of the index.

(string)

indexes -> (list)

The array of `DataSourceIntrospectionModelIndex` objects.

(structure)

The index that was retrieved from the introspected data.

name -> (string)

The name of the index.

fields -> (list)

The fields of the index.

(string)

sdl -> (string)

Contains the output of the SDL that was generated from the introspected types. This is controlled by the `includeModelsSDL` parameter of the `GetDataSourceIntrospection` operation.

nextToken -> (string)

Determines the number of types to be returned in a single response before paginating. This value is typically taken from `nextToken` value from the previous response.