# describe-connector-entityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connector-entity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connector-entity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html#cli-aws-appflow) ]

# describe-connector-entity

## Description

Provides details regarding the entity used with the connector, with a description of the data model for each field in that entity.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appflow-2020-08-23/DescribeConnectorEntity)

## Synopsis

```
describe-connector-entity
--connector-entity-name <value>
[--connector-type <value>]
[--connector-profile-name <value>]
[--api-version <value>]
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

`--connector-entity-name` (string)

The entity name for that connector.

`--connector-type` (string)

The type of connector application, such as Salesforce, Amplitude, and so on.

Possible values:

- `Salesforce`
- `Singular`
- `Slack`
- `Redshift`
- `S3`
- `Marketo`
- `Googleanalytics`
- `Zendesk`
- `Servicenow`
- `Datadog`
- `Trendmicro`
- `Snowflake`
- `Dynatrace`
- `Infornexus`
- `Amplitude`
- `Veeva`
- `EventBridge`
- `LookoutMetrics`
- `Upsolver`
- `Honeycode`
- `CustomerProfiles`
- `SAPOData`
- `CustomConnector`
- `Pardot`

`--connector-profile-name` (string)

The name of the connector profile. The name is unique for each `ConnectorProfile` in the Amazon Web Services account.

`--api-version` (string)

The version of the API thatâs used by the connector.

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

connectorEntityFields -> (list)

Describes the fields for that connector entity. For example, for an *account* entity, the fields would be *account name* , *account ID* , and so on.

(structure)

Describes the data model of a connector field. For example, for an *account* entity, the fields would be *account name* , *account ID* , and so on.

identifier -> (string)

The unique identifier of the connector field.

parentIdentifier -> (string)

The parent identifier of the connector field.

label -> (string)

The label applied to a connector entity field.

isPrimaryKey -> (boolean)

Booelan value that indicates whether this field can be used as a primary key.

defaultValue -> (string)

Default value that can be assigned to this field.

isDeprecated -> (boolean)

Booelan value that indicates whether this field is deprecated or not.

supportedFieldTypeDetails -> (structure)

Contains details regarding the supported `FieldType` , including the corresponding `filterOperators` and `supportedValues` .

v1 -> (structure)

The initial supported version for `fieldType` . If this is later changed to a different version, v2 will be introduced.

fieldType -> (string)

The type of field, such as string, integer, date, and so on.

filterOperators -> (list)

The list of operators supported by a field.

(string)

supportedValues -> (list)

The list of values that a field can contain. For example, a Boolean `fieldType` can have two values: âtrueâ and âfalseâ.

(string)

valueRegexPattern -> (string)

The regular expression pattern for the field name.

supportedDateFormat -> (string)

The date format that the field supports.

fieldValueRange -> (structure)

The range of values this field can hold.

maximum -> (double)

Maximum value supported by the field.

minimum -> (double)

Minimum value supported by the field.

fieldLengthRange -> (structure)

This is the allowable length range for this fieldâs value.

maximum -> (double)

Maximum value supported by the field.

minimum -> (double)

Minimum value supported by the field.

description -> (string)

A description of the connector entity field.

sourceProperties -> (structure)

The properties that can be applied to a field when the connector is being used as a source.

isRetrievable -> (boolean)

Indicates whether the field can be returned in a search result.

isQueryable -> (boolean)

Indicates if the field can be queried.

isTimestampFieldForIncrementalQueries -> (boolean)

Indicates if this timestamp field can be used for incremental queries.

destinationProperties -> (structure)

The properties applied to a field when the connector is being used as a destination.

isCreatable -> (boolean)

Specifies if the destination field can be created by the current user.

isNullable -> (boolean)

Specifies if the destination field can have a null value.

isUpsertable -> (boolean)

Specifies if the flow run can either insert new rows in the destination field if they do not already exist, or update them if they do.

isUpdatable -> (boolean)

Specifies whether the field can be updated during an `UPDATE` or `UPSERT` write operation.

isDefaultedOnCreate -> (boolean)

Specifies whether the field can use the default value during a Create operation.

supportedWriteOperations -> (list)

A list of supported write operations. For each write operation listed, this field can be used in `idFieldNames` when that write operation is present as a destination option.

(string)

The possible write operations in the destination connector. When this value is not provided, this defaults to the `INSERT` operation.

customProperties -> (map)

A map that has specific properties related to the ConnectorEntityField.

key -> (string)

value -> (string)