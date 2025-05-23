# create-schema-mappingÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/create-schema-mapping.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/create-schema-mapping.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [entityresolution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/index.html#cli-aws-entityresolution) ]

# create-schema-mapping

## Description

Creates a schema mapping, which defines the schema of the input customer records table. The `SchemaMapping` also provides Entity Resolution with some metadata about the table, such as the attribute types of the columns and which columns to match on.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/entityresolution-2018-05-10/CreateSchemaMapping)

## Synopsis

```
create-schema-mapping
--schema-name <value>
[--description <value>]
--mapped-input-fields <value>
[--tags <value>]
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

`--schema-name` (string)

The name of the schema. There canât be multiple `SchemaMappings` with the same name.

`--description` (string)

A description of the schema.

`--mapped-input-fields` (list)

A list of `MappedInputFields` . Each `MappedInputField` corresponds to a column the source data table, and contains column name plus additional information that Entity Resolution uses for matching.

(structure)

A configuration object for defining input data fields in Entity Resolution. The `SchemaInputAttribute` specifies how individual fields in your input data should be processed and matched.

fieldName -> (string)

A string containing the field name.

type -> (string)

The type of the attribute, selected from a list of values.

LiveRamp supports: `NAME` | `NAME_FIRST` | `NAME_MIDDLE` | `NAME_LAST` | `ADDRESS` | `ADDRESS_STREET1` | `ADDRESS_STREET2` | `ADDRESS_STREET3` | `ADDRESS_CITY` | `ADDRESS_STATE` | `ADDRESS_COUNTRY` | `ADDRESS_POSTALCODE` | `PHONE` | `PHONE_NUMBER` | `EMAIL_ADDRESS` | `UNIQUE_ID` | `PROVIDER_ID`

TransUnion supports: `NAME` | `NAME_FIRST` | `NAME_LAST` | `ADDRESS` | `ADDRESS_CITY` | `ADDRESS_STATE` | `ADDRESS_COUNTRY` | `ADDRESS_POSTALCODE` | `PHONE_NUMBER` | `EMAIL_ADDRESS` | `UNIQUE_ID` | `IPV4` | `IPV6` | `MAID`

Unified ID 2.0 supports: `PHONE_NUMBER` | `EMAIL_ADDRESS` | `UNIQUE_ID`

### Note

Normalization is only supported for `NAME` , `ADDRESS` , `PHONE` , and `EMAIL_ADDRESS` .

If you want to normalize `NAME_FIRST` , `NAME_MIDDLE` , and `NAME_LAST` , you must group them by assigning them to the `NAME` `groupName` .

If you want to normalize `ADDRESS_STREET1` , `ADDRESS_STREET2` , `ADDRESS_STREET3` , `ADDRESS_CITY` , `ADDRESS_STATE` , `ADDRESS_COUNTRY` , and `ADDRESS_POSTALCODE` , you must group them by assigning them to the `ADDRESS` `groupName` .

If you want to normalize `PHONE_NUMBER` and `PHONE_COUNTRYCODE` , you must group them by assigning them to the `PHONE` `groupName` .

groupName -> (string)

A string that instructs Entity Resolution to combine several columns into a unified column with the identical attribute type.

For example, when working with columns such as `NAME_FIRST` , `NAME_MIDDLE` , and `NAME_LAST` , assigning them a common `groupName` will prompt Entity Resolution to concatenate them into a single value.

matchKey -> (string)

A key that allows grouping of multiple input attributes into a unified matching group.

For example, consider a scenario where the source table contains various addresses, such as `business_address` and `shipping_address` . By assigning a `matchKey` called `address` to both attributes, Entity Resolution will match records across these fields to create a consolidated matching group.

If no `matchKey` is specified for a column, it wonât be utilized for matching purposes but will still be included in the output table.

subType -> (string)

The subtype of the attribute, selected from a list of values.

hashed -> (boolean)

Indicates if the column values are hashed in the schema input.

If the value is set to `TRUE` , the column values are hashed.

If the value is set to `FALSE` , the column values are cleartext.

Shorthand Syntax:

```
fieldName=string,type=string,groupName=string,matchKey=string,subType=string,hashed=boolean ...
```

JSON Syntax:

```
[
  {
    "fieldName": "string",
    "type": "NAME"|"NAME_FIRST"|"NAME_MIDDLE"|"NAME_LAST"|"ADDRESS"|"ADDRESS_STREET1"|"ADDRESS_STREET2"|"ADDRESS_STREET3"|"ADDRESS_CITY"|"ADDRESS_STATE"|"ADDRESS_COUNTRY"|"ADDRESS_POSTALCODE"|"PHONE"|"PHONE_NUMBER"|"PHONE_COUNTRYCODE"|"EMAIL_ADDRESS"|"UNIQUE_ID"|"DATE"|"STRING"|"PROVIDER_ID"|"IPV4"|"IPV6"|"MAID",
    "groupName": "string",
    "matchKey": "string",
    "subType": "string",
    "hashed": true|false
  }
  ...
]
```

`--tags` (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

schemaName -> (string)

The name of the schema.

schemaArn -> (string)

The ARN (Amazon Resource Name) that Entity Resolution generated for the `SchemaMapping` .

description -> (string)

A description of the schema.

mappedInputFields -> (list)

A list of `MappedInputFields` . Each `MappedInputField` corresponds to a column the source data table, and contains column name plus additional information that Entity Resolution uses for matching.

(structure)

A configuration object for defining input data fields in Entity Resolution. The `SchemaInputAttribute` specifies how individual fields in your input data should be processed and matched.

fieldName -> (string)

A string containing the field name.

type -> (string)

The type of the attribute, selected from a list of values.

LiveRamp supports: `NAME` | `NAME_FIRST` | `NAME_MIDDLE` | `NAME_LAST` | `ADDRESS` | `ADDRESS_STREET1` | `ADDRESS_STREET2` | `ADDRESS_STREET3` | `ADDRESS_CITY` | `ADDRESS_STATE` | `ADDRESS_COUNTRY` | `ADDRESS_POSTALCODE` | `PHONE` | `PHONE_NUMBER` | `EMAIL_ADDRESS` | `UNIQUE_ID` | `PROVIDER_ID`

TransUnion supports: `NAME` | `NAME_FIRST` | `NAME_LAST` | `ADDRESS` | `ADDRESS_CITY` | `ADDRESS_STATE` | `ADDRESS_COUNTRY` | `ADDRESS_POSTALCODE` | `PHONE_NUMBER` | `EMAIL_ADDRESS` | `UNIQUE_ID` | `IPV4` | `IPV6` | `MAID`

Unified ID 2.0 supports: `PHONE_NUMBER` | `EMAIL_ADDRESS` | `UNIQUE_ID`

### Note

Normalization is only supported for `NAME` , `ADDRESS` , `PHONE` , and `EMAIL_ADDRESS` .

If you want to normalize `NAME_FIRST` , `NAME_MIDDLE` , and `NAME_LAST` , you must group them by assigning them to the `NAME` `groupName` .

If you want to normalize `ADDRESS_STREET1` , `ADDRESS_STREET2` , `ADDRESS_STREET3` , `ADDRESS_CITY` , `ADDRESS_STATE` , `ADDRESS_COUNTRY` , and `ADDRESS_POSTALCODE` , you must group them by assigning them to the `ADDRESS` `groupName` .

If you want to normalize `PHONE_NUMBER` and `PHONE_COUNTRYCODE` , you must group them by assigning them to the `PHONE` `groupName` .

groupName -> (string)

A string that instructs Entity Resolution to combine several columns into a unified column with the identical attribute type.

For example, when working with columns such as `NAME_FIRST` , `NAME_MIDDLE` , and `NAME_LAST` , assigning them a common `groupName` will prompt Entity Resolution to concatenate them into a single value.

matchKey -> (string)

A key that allows grouping of multiple input attributes into a unified matching group.

For example, consider a scenario where the source table contains various addresses, such as `business_address` and `shipping_address` . By assigning a `matchKey` called `address` to both attributes, Entity Resolution will match records across these fields to create a consolidated matching group.

If no `matchKey` is specified for a column, it wonât be utilized for matching purposes but will still be included in the output table.

subType -> (string)

The subtype of the attribute, selected from a list of values.

hashed -> (boolean)

Indicates if the column values are hashed in the schema input.

If the value is set to `TRUE` , the column values are hashed.

If the value is set to `FALSE` , the column values are cleartext.