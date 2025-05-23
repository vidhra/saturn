# delete-index-fieldÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/delete-index-field.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/delete-index-field.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cloudsearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudsearch/index.html#cli-aws-cloudsearch) ]

# delete-index-field

## Description

Removes an `` IndexField`` from the search domain. For more information, see [Configuring Index Fields](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html) in the *Amazon CloudSearch Developer Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cloudsearch-2013-01-01/DeleteIndexField)

## Synopsis

```
delete-index-field
--domain-name <value>
--index-field-name <value>
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

`--domain-name` (string)

A string that represents the name of a domain. Domain names are unique across the domains owned by an account within an AWS region. Domain names start with a letter or number and can contain the following characters: a-z (lowercase), 0-9, and - (hyphen).

`--index-field-name` (string)

The name of the index field your want to remove from the domainâs indexing options.

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

IndexField -> (structure)

The status of the index field being deleted.

Options -> (structure)

Configuration information for a field in the index, including its name, type, and options. The supported options depend on the `` IndexFieldType`` .

IndexFieldName -> (string)

A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic fieldâs name defines a pattern that begins or ends with a wildcard. Any document fields that donât map to a regular index field but do match a dynamic fieldâs pattern are configured with the dynamic fieldâs indexing options.

Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.

The name `score` is reserved and cannot be used as a field name. To reference a documentâs ID, you can use the name `_id` .

IndexFieldType -> (string)

The type of field. The valid options for a field depend on the field type. For more information about the supported field types, see [Configuring Index Fields](http://docs.aws.amazon.com/cloudsearch/latest/developerguide/configuring-index-fields.html) in the *Amazon CloudSearch Developer Guide* .

IntOptions -> (structure)

Options for a 64-bit signed integer field. Present if `IndexFieldType` specifies the field is of type `int` . All options are enabled by default.

DefaultValue -> (long)

A value to use for the field if the field isnât specified for a document. This can be important if you are using the field in an expression and that field is not present in every document.

SourceField -> (string)

The name of the source field to map to the field.

FacetEnabled -> (boolean)

Whether facet information can be returned for the field.

SearchEnabled -> (boolean)

Whether the contents of the field are searchable.

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

SortEnabled -> (boolean)

Whether the field can be used to sort the search results.

DoubleOptions -> (structure)

Options for a double-precision 64-bit floating point field. Present if `IndexFieldType` specifies the field is of type `double` . All options are enabled by default.

DefaultValue -> (double)

A value to use for the field if the field isnât specified for a document. This can be important if you are using the field in an expression and that field is not present in every document.

SourceField -> (string)

The name of the source field to map to the field.

FacetEnabled -> (boolean)

Whether facet information can be returned for the field.

SearchEnabled -> (boolean)

Whether the contents of the field are searchable.

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

SortEnabled -> (boolean)

Whether the field can be used to sort the search results.

LiteralOptions -> (structure)

Options for literal field. Present if `IndexFieldType` specifies the field is of type `literal` . All options are enabled by default.

DefaultValue -> (string)

A value to use for the field if the field isnât specified for a document.

SourceField -> (string)

A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic fieldâs name defines a pattern that begins or ends with a wildcard. Any document fields that donât map to a regular index field but do match a dynamic fieldâs pattern are configured with the dynamic fieldâs indexing options.

Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.

The name `score` is reserved and cannot be used as a field name. To reference a documentâs ID, you can use the name `_id` .

FacetEnabled -> (boolean)

Whether facet information can be returned for the field.

SearchEnabled -> (boolean)

Whether the contents of the field are searchable.

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

SortEnabled -> (boolean)

Whether the field can be used to sort the search results.

TextOptions -> (structure)

Options for text field. Present if `IndexFieldType` specifies the field is of type `text` . A `text` field is always searchable. All options are enabled by default.

DefaultValue -> (string)

A value to use for the field if the field isnât specified for a document.

SourceField -> (string)

A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic fieldâs name defines a pattern that begins or ends with a wildcard. Any document fields that donât map to a regular index field but do match a dynamic fieldâs pattern are configured with the dynamic fieldâs indexing options.

Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.

The name `score` is reserved and cannot be used as a field name. To reference a documentâs ID, you can use the name `_id` .

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

SortEnabled -> (boolean)

Whether the field can be used to sort the search results.

HighlightEnabled -> (boolean)

Whether highlights can be returned for the field.

AnalysisScheme -> (string)

The name of an analysis scheme for a `text` field.

DateOptions -> (structure)

Options for a date field. Dates and times are specified in UTC (Coordinated Universal Time) according to IETF RFC3339: yyyy-mm-ddT00:00:00Z. Present if `IndexFieldType` specifies the field is of type `date` . All options are enabled by default.

DefaultValue -> (string)

A value to use for the field if the field isnât specified for a document.

SourceField -> (string)

A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic fieldâs name defines a pattern that begins or ends with a wildcard. Any document fields that donât map to a regular index field but do match a dynamic fieldâs pattern are configured with the dynamic fieldâs indexing options.

Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.

The name `score` is reserved and cannot be used as a field name. To reference a documentâs ID, you can use the name `_id` .

FacetEnabled -> (boolean)

Whether facet information can be returned for the field.

SearchEnabled -> (boolean)

Whether the contents of the field are searchable.

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

SortEnabled -> (boolean)

Whether the field can be used to sort the search results.

LatLonOptions -> (structure)

Options for a latlon field. A latlon field contains a location stored as a latitude and longitude value pair. Present if `IndexFieldType` specifies the field is of type `latlon` . All options are enabled by default.

DefaultValue -> (string)

A value to use for the field if the field isnât specified for a document.

SourceField -> (string)

A string that represents the name of an index field. CloudSearch supports regular index fields as well as dynamic fields. A dynamic fieldâs name defines a pattern that begins or ends with a wildcard. Any document fields that donât map to a regular index field but do match a dynamic fieldâs pattern are configured with the dynamic fieldâs indexing options.

Regular field names begin with a letter and can contain the following characters: a-z (lowercase), 0-9, and _ (underscore). Dynamic field names must begin or end with a wildcard (*). The wildcard can also be the only character in a dynamic field name. Multiple wildcards, and wildcards embedded within a string are not supported.

The name `score` is reserved and cannot be used as a field name. To reference a documentâs ID, you can use the name `_id` .

FacetEnabled -> (boolean)

Whether facet information can be returned for the field.

SearchEnabled -> (boolean)

Whether the contents of the field are searchable.

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

SortEnabled -> (boolean)

Whether the field can be used to sort the search results.

IntArrayOptions -> (structure)

Options for a field that contains an array of 64-bit signed integers. Present if `IndexFieldType` specifies the field is of type `int-array` . All options are enabled by default.

DefaultValue -> (long)

A value to use for the field if the field isnât specified for a document.

SourceFields -> (string)

A list of source fields to map to the field.

FacetEnabled -> (boolean)

Whether facet information can be returned for the field.

SearchEnabled -> (boolean)

Whether the contents of the field are searchable.

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

DoubleArrayOptions -> (structure)

Options for a field that contains an array of double-precision 64-bit floating point values. Present if `IndexFieldType` specifies the field is of type `double-array` . All options are enabled by default.

DefaultValue -> (double)

A value to use for the field if the field isnât specified for a document.

SourceFields -> (string)

A list of source fields to map to the field.

FacetEnabled -> (boolean)

Whether facet information can be returned for the field.

SearchEnabled -> (boolean)

Whether the contents of the field are searchable.

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

LiteralArrayOptions -> (structure)

Options for a field that contains an array of literal strings. Present if `IndexFieldType` specifies the field is of type `literal-array` . All options are enabled by default.

DefaultValue -> (string)

A value to use for the field if the field isnât specified for a document.

SourceFields -> (string)

A list of source fields to map to the field.

FacetEnabled -> (boolean)

Whether facet information can be returned for the field.

SearchEnabled -> (boolean)

Whether the contents of the field are searchable.

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

TextArrayOptions -> (structure)

Options for a field that contains an array of text strings. Present if `IndexFieldType` specifies the field is of type `text-array` . A `text-array` field is always searchable. All options are enabled by default.

DefaultValue -> (string)

A value to use for the field if the field isnât specified for a document.

SourceFields -> (string)

A list of source fields to map to the field.

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

HighlightEnabled -> (boolean)

Whether highlights can be returned for the field.

AnalysisScheme -> (string)

The name of an analysis scheme for a `text-array` field.

DateArrayOptions -> (structure)

Options for a field that contains an array of dates. Present if `IndexFieldType` specifies the field is of type `date-array` . All options are enabled by default.

DefaultValue -> (string)

A value to use for the field if the field isnât specified for a document.

SourceFields -> (string)

A list of source fields to map to the field.

FacetEnabled -> (boolean)

Whether facet information can be returned for the field.

SearchEnabled -> (boolean)

Whether the contents of the field are searchable.

ReturnEnabled -> (boolean)

Whether the contents of the field can be returned in the search results.

Status -> (structure)

The status of domain configuration option.

CreationDate -> (timestamp)

A timestamp for when this option was created.

UpdateDate -> (timestamp)

A timestamp for when this option was last updated.

UpdateVersion -> (integer)

A unique integer that indicates when this option was last updated.

State -> (string)

The state of processing a change to an option. Possible values:

- `RequiresIndexDocuments` : the optionâs latest value will not be deployed until  IndexDocuments has been called and indexing is complete.
- `Processing` : the optionâs latest value is in the process of being activated.
- `Active` : the optionâs latest value is completely deployed.
- `FailedToValidate` : the option value is not compatible with the domainâs data and cannot be used to index the data. You must either modify the option value or update or remove the incompatible documents.

PendingDeletion -> (boolean)

Indicates that the option will be deleted once processing is complete.