# get-codegen-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifyuibuilder/get-codegen-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifyuibuilder/get-codegen-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [amplifyuibuilder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/amplifyuibuilder/index.html#cli-aws-amplifyuibuilder) ]

# get-codegen-job

## Description

Returns an existing code generation job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/amplifyuibuilder-2021-08-11/GetCodegenJob)

## Synopsis

```
get-codegen-job
--app-id <value>
--environment-name <value>
--id <value>
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

`--app-id` (string)

The unique ID of the Amplify app associated with the code generation job.

`--environment-name` (string)

The name of the backend environment that is a part of the Amplify app associated with the code generation job.

`--id` (string)

The unique ID of the code generation job.

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

job -> (structure)

The configuration settings for the code generation job.

id -> (string)

The unique ID for the code generation job.

appId -> (string)

The ID of the Amplify app associated with the code generation job.

environmentName -> (string)

The name of the backend environment associated with the code generation job.

renderConfig -> (tagged union structure)

Describes the configuration information for rendering the UI component associated with the code generation job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `react`.

react -> (structure)

The name of the `ReactStartCodegenJobData` object.

module -> (string)

The JavaScript module type.

target -> (string)

The ECMAScript specification to use.

script -> (string)

The file type to use for a JavaScript project.

renderTypeDeclarations -> (boolean)

Specifies whether the code generation job should render type declaration files.

inlineSourceMap -> (boolean)

Specifies whether the code generation job should render inline source maps.

apiConfiguration -> (tagged union structure)

The API configuration for the code generation job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `graphQLConfig`, `dataStoreConfig`, `noApiConfig`.

graphQLConfig -> (structure)

The configuration for an application using GraphQL APIs.

typesFilePath -> (string)

The path to the GraphQL types file, relative to the component output directory.

queriesFilePath -> (string)

The path to the GraphQL queries file, relative to the component output directory.

mutationsFilePath -> (string)

The path to the GraphQL mutations file, relative to the component output directory.

subscriptionsFilePath -> (string)

The path to the GraphQL subscriptions file, relative to the component output directory.

fragmentsFilePath -> (string)

The path to the GraphQL fragments file, relative to the component output directory.

dataStoreConfig -> (structure)

The configuration for an application using DataStore APIs.

noApiConfig -> (structure)

The configuration for an application with no API being used.

dependencies -> (map)

Lists the dependency packages that may be required for the project code to run.

key -> (string)

value -> (string)

genericDataSchema -> (structure)

Describes the data schema for a code generation job.

dataSourceType -> (string)

The type of the data source for the schema. Currently, the only valid value is an Amplify `DataStore` .

models -> (map)

The name of a `CodegenGenericDataModel` .

key -> (string)

value -> (structure)

Describes a model in a generic data schema.

fields -> (map)

The fields in the generic data model.

key -> (string)

value -> (structure)

Describes a field in a generic data schema.

dataType -> (string)

The data type for the generic data field.

dataTypeValue -> (string)

The value of the data type for the generic data field.

required -> (boolean)

Specifies whether the generic data field is required.

readOnly -> (boolean)

Specifies whether the generic data field is read-only.

isArray -> (boolean)

Specifies whether the generic data field is an array.

relationship -> (structure)

The relationship of the generic data schema.

type -> (string)

The data relationship type.

relatedModelName -> (string)

The name of the related model in the data relationship.

relatedModelFields -> (list)

The related model fields in the data relationship.

(string)

canUnlinkAssociatedModel -> (boolean)

Specifies whether the relationship can unlink the associated model.

relatedJoinFieldName -> (string)

The name of the related join field in the data relationship.

relatedJoinTableName -> (string)

The name of the related join table in the data relationship.

belongsToFieldOnRelatedModel -> (string)

The value of the `belongsTo` field on the related data model.

associatedFields -> (list)

The associated fields of the data relationship.

(string)

isHasManyIndex -> (boolean)

Specifies whether the `@index` directive is supported for a `hasMany` data relationship.

isJoinTable -> (boolean)

Specifies whether the generic data model is a join table.

primaryKeys -> (list)

The primary keys of the generic data model.

(string)

enums -> (map)

The name of a `CodegenGenericDataEnum` .

key -> (string)

value -> (structure)

Describes the enums in a generic data schema.

values -> (list)

The list of enum values in the generic data schema.

(string)

nonModels -> (map)

The name of a `CodegenGenericDataNonModel` .

key -> (string)

value -> (structure)

Describes a non-model in a generic data schema.

fields -> (map)

The fields in a generic data schema non model.

key -> (string)

value -> (structure)

Describes a field in a generic data schema.

dataType -> (string)

The data type for the generic data field.

dataTypeValue -> (string)

The value of the data type for the generic data field.

required -> (boolean)

Specifies whether the generic data field is required.

readOnly -> (boolean)

Specifies whether the generic data field is read-only.

isArray -> (boolean)

Specifies whether the generic data field is an array.

relationship -> (structure)

The relationship of the generic data schema.

type -> (string)

The data relationship type.

relatedModelName -> (string)

The name of the related model in the data relationship.

relatedModelFields -> (list)

The related model fields in the data relationship.

(string)

canUnlinkAssociatedModel -> (boolean)

Specifies whether the relationship can unlink the associated model.

relatedJoinFieldName -> (string)

The name of the related join field in the data relationship.

relatedJoinTableName -> (string)

The name of the related join table in the data relationship.

belongsToFieldOnRelatedModel -> (string)

The value of the `belongsTo` field on the related data model.

associatedFields -> (list)

The associated fields of the data relationship.

(string)

isHasManyIndex -> (boolean)

Specifies whether the `@index` directive is supported for a `hasMany` data relationship.

autoGenerateForms -> (boolean)

Specifies whether to autogenerate forms in the code generation job.

features -> (structure)

Describes the feature flags that you can specify for a code generation job.

isRelationshipSupported -> (boolean)

Specifes whether a code generation job supports data relationships.

isNonModelSupported -> (boolean)

Specifies whether a code generation job supports non models.

status -> (string)

The status of the code generation job.

statusMessage -> (string)

The customized status message for the code generation job.

asset -> (structure)

The `CodegenJobAsset` to use for the code generation job.

downloadUrl -> (string)

The URL to use to access the asset.

tags -> (map)

One or more key-value pairs to use when tagging the code generation job.

key -> (string)

value -> (string)

createdAt -> (timestamp)

The time that the code generation job was created.

modifiedAt -> (timestamp)

The time that the code generation job was modified.

dependencies -> (list)

Lists the dependency packages that may be required for the project code to run.

(structure)

Dependency package that may be required for the project code to run.

name -> (string)

Name of the dependency package.

supportedVersion -> (string)

Indicates the version of the supported dependency package.

isSemVer -> (boolean)

Determines if the dependency package is using Semantic versioning. If set to true, it indicates that the dependency package uses Semantic versioning.

reason -> (string)

Indicates the reason to include the dependency package in your project code.