# list-ml-transformsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-ml-transforms.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/list-ml-transforms.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# list-ml-transforms

## Description

Retrieves a sortable, filterable list of existing Glue machine learning transforms in this Amazon Web Services account, or the resources with the specified tag. This operation takes the optional `Tags` field, which you can use as a filter of the responses so that tagged resources can be retrieved as a group. If you choose to use tag filtering, only resources with the tags are retrieved.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/ListMLTransforms)

## Synopsis

```
list-ml-transforms
[--next-token <value>]
[--max-results <value>]
[--filter <value>]
[--sort <value>]
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

`--next-token` (string)

A continuation token, if this is a continuation request.

`--max-results` (integer)

The maximum size of a list to return.

`--filter` (structure)

A `TransformFilterCriteria` used to filter the machine learning transforms.

Name -> (string)

A unique transform name that is used to filter the machine learning transforms.

TransformType -> (string)

The type of machine learning transform that is used to filter the machine learning transforms.

Status -> (string)

Filters the list of machine learning transforms by the last known status of the transforms (to indicate whether a transform can be used or not). One of âNOT_READYâ, âREADYâ, or âDELETINGâ.

GlueVersion -> (string)

This value determines which version of Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see [Glue Versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions) in the developer guide.

CreatedBefore -> (timestamp)

The time and date before which the transforms were created.

CreatedAfter -> (timestamp)

The time and date after which the transforms were created.

LastModifiedBefore -> (timestamp)

Filter on transforms last modified before this date.

LastModifiedAfter -> (timestamp)

Filter on transforms last modified after this date.

Schema -> (list)

Filters on datasets with a specific schema. The `Map<Column, Type>` object is an array of key-value pairs representing the schema this transform accepts, where `Column` is the name of a column, and `Type` is the type of the data such as an integer or string. Has an upper bound of 100 columns.

(structure)

A key-value pair representing a column and data type that this transform can run against. The `Schema` parameter of the `MLTransform` may contain up to 100 of these structures.

Name -> (string)

The name of the column.

DataType -> (string)

The type of data in the column.

Shorthand Syntax:

```
Name=string,TransformType=string,Status=string,GlueVersion=string,CreatedBefore=timestamp,CreatedAfter=timestamp,LastModifiedBefore=timestamp,LastModifiedAfter=timestamp,Schema=[{Name=string,DataType=string},{Name=string,DataType=string}]
```

JSON Syntax:

```
{
  "Name": "string",
  "TransformType": "FIND_MATCHES",
  "Status": "NOT_READY"|"READY"|"DELETING",
  "GlueVersion": "string",
  "CreatedBefore": timestamp,
  "CreatedAfter": timestamp,
  "LastModifiedBefore": timestamp,
  "LastModifiedAfter": timestamp,
  "Schema": [
    {
      "Name": "string",
      "DataType": "string"
    }
    ...
  ]
}
```

`--sort` (structure)

A `TransformSortCriteria` used to sort the machine learning transforms.

Column -> (string)

The column to be used in the sorting criteria that are associated with the machine learning transform.

SortDirection -> (string)

The sort direction to be used in the sorting criteria that are associated with the machine learning transform.

Shorthand Syntax:

```
Column=string,SortDirection=string
```

JSON Syntax:

```
{
  "Column": "NAME"|"TRANSFORM_TYPE"|"STATUS"|"CREATED"|"LAST_MODIFIED",
  "SortDirection": "DESCENDING"|"ASCENDING"
}
```

`--tags` (map)

Specifies to return only these tagged resources.

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

TransformIds -> (list)

The identifiers of all the machine learning transforms in the account, or the machine learning transforms with the specified tags.

(string)

NextToken -> (string)

A continuation token, if the returned list does not contain the last metric available.