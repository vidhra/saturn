# get-resource-lf-tagsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-resource-lf-tags.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/get-resource-lf-tags.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lakeformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/index.html#cli-aws-lakeformation) ]

# get-resource-lf-tags

## Description

Returns the LF-tags applied to a resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/GetResourceLFTags)

## Synopsis

```
get-resource-lf-tags
[--catalog-id <value>]
--resource <value>
[--show-assigned-lf-tags | --no-show-assigned-lf-tags]
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

`--catalog-id` (string)

The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

`--resource` (structure)

The database, table, or column resource for which you want to return LF-tags.

Catalog -> (structure)

The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

Id -> (string)

An identifier for the catalog resource.

Database -> (structure)

The database for the resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database permissions to a principal.

CatalogId -> (string)

The identifier for the Data Catalog. By default, it is the account ID of the caller.

Name -> (string)

The name of the database resource. Unique to the Data Catalog.

Table -> (structure)

The table for the resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

CatalogId -> (string)

The identifier for the Data Catalog. By default, it is the account ID of the caller.

DatabaseName -> (string)

The name of the database for the table. Unique to a Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name -> (string)

The name of the table.

TableWildcard -> (structure)

A wildcard object representing every table under a database.

At least one of `TableResource$Name` or `TableResource$TableWildcard` is required.

TableWithColumns -> (structure)

The table with columns for the resource. A principal with permissions to this resource can select metadata from the columns of a table in the Data Catalog and the underlying data in Amazon S3.

CatalogId -> (string)

The identifier for the Data Catalog. By default, it is the account ID of the caller.

DatabaseName -> (string)

The name of the database for the table with columns resource. Unique to the Data Catalog. A database is a set of associated table definitions organized into a logical group. You can Grant and Revoke database privileges to a principal.

Name -> (string)

The name of the table resource. A table is a metadata definition that represents your data. You can Grant and Revoke table privileges to a principal.

ColumnNames -> (list)

The list of column names for the table. At least one of `ColumnNames` or `ColumnWildcard` is required.

(string)

ColumnWildcard -> (structure)

A wildcard specified by a `ColumnWildcard` object. At least one of `ColumnNames` or `ColumnWildcard` is required.

ExcludedColumnNames -> (list)

Excludes column names. Any column with this name will be excluded.

(string)

DataLocation -> (structure)

The location of an Amazon S3 path where permissions are granted or revoked.

CatalogId -> (string)

The identifier for the Data Catalog where the location is registered with Lake Formation. By default, it is the account ID of the caller.

ResourceArn -> (string)

The Amazon Resource Name (ARN) that uniquely identifies the data location resource.

DataCellsFilter -> (structure)

A data cell filter.

TableCatalogId -> (string)

The ID of the catalog to which the table belongs.

DatabaseName -> (string)

A database in the Glue Data Catalog.

TableName -> (string)

The name of the table.

Name -> (string)

The name of the data cells filter.

LFTag -> (structure)

The LF-tag key and values attached to a resource.

CatalogId -> (string)

The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

TagKey -> (string)

The key-name for the LF-tag.

TagValues -> (list)

A list of possible values an attribute can take.

(string)

LFTagPolicy -> (structure)

A list of LF-tag conditions or saved LF-Tag expressions that define a resourceâs LF-tag policy.

CatalogId -> (string)

The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

ResourceType -> (string)

The resource type for which the LF-tag policy applies.

Expression -> (list)

A list of LF-tag conditions or a saved expression that apply to the resourceâs LF-tag policy.

(structure)

A structure that allows an admin to grant user permissions on certain conditions. For example, granting a role access to all columns that do not have the LF-tag âPIIâ in tables that have the LF-tag âProdâ.

TagKey -> (string)

The key-name for the LF-tag.

TagValues -> (list)

A list of possible values an attribute can take.

The maximum number of values that can be defined for a LF-Tag is 1000. A single API call supports 50 values. You can use multiple API calls to add more values.

(string)

ExpressionName -> (string)

If provided, permissions are granted to the Data Catalog resources whose assigned LF-Tags match the expression body of the saved expression under the provided `ExpressionName` .

LFTagExpression -> (structure)

LF-Tag expression resource. A logical expression composed of one or more LF-Tag key:value pairs.

CatalogId -> (string)

The identifier for the Data Catalog. By default, the account ID.

Name -> (string)

The name of the LF-Tag expression to grant permissions on.

JSON Syntax:

```
{
  "Catalog": {
    "Id": "string"
  },
  "Database": {
    "CatalogId": "string",
    "Name": "string"
  },
  "Table": {
    "CatalogId": "string",
    "DatabaseName": "string",
    "Name": "string",
    "TableWildcard": {

    }
  },
  "TableWithColumns": {
    "CatalogId": "string",
    "DatabaseName": "string",
    "Name": "string",
    "ColumnNames": ["string", ...],
    "ColumnWildcard": {
      "ExcludedColumnNames": ["string", ...]
    }
  },
  "DataLocation": {
    "CatalogId": "string",
    "ResourceArn": "string"
  },
  "DataCellsFilter": {
    "TableCatalogId": "string",
    "DatabaseName": "string",
    "TableName": "string",
    "Name": "string"
  },
  "LFTag": {
    "CatalogId": "string",
    "TagKey": "string",
    "TagValues": ["string", ...]
  },
  "LFTagPolicy": {
    "CatalogId": "string",
    "ResourceType": "DATABASE"|"TABLE",
    "Expression": [
      {
        "TagKey": "string",
        "TagValues": ["string", ...]
      }
      ...
    ],
    "ExpressionName": "string"
  },
  "LFTagExpression": {
    "CatalogId": "string",
    "Name": "string"
  }
}
```

`--show-assigned-lf-tags` | `--no-show-assigned-lf-tags` (boolean)

Indicates whether to show the assigned LF-tags.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list LF-tags**

The following `list-lf-tags` example returns list of LF-tags that the requester has permission to view.

```
aws lakeformation list-lf-tags \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "CatalogId": "123456789111",
    "ResourceShareType": "ALL",
    "MaxResults": 2
}
```

Output:

```
{
"LFTags": [{
        "CatalogId": "123456789111",
        "TagKey": "category",
        "TagValues": [
            "private",
            "public"
        ]
    },
    {
        "CatalogId": "123456789111",
        "TagKey": "group",
        "TagValues": [
            "analyst",
            "campaign",
            "developer"
        ]
    }],
    "NextToken": "kIiwiZXhwaXJhdGlvbiI6eyJzZWNvbmRzIjoxNjYwMDY4dCI6ZmFsc2V9"
}
```

For more information, see [Managing LF-Tags for metadata access control](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-tags.html) in the *AWS Lake Formation Developer Guide*.

## Output

LFTagOnDatabase -> (list)

A list of LF-tags applied to a database resource.

(structure)

A structure containing an LF-tag key-value pair.

CatalogId -> (string)

The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

TagKey -> (string)

The key-name for the LF-tag.

TagValues -> (list)

A list of possible values an attribute can take.

(string)

LFTagsOnTable -> (list)

A list of LF-tags applied to a table resource.

(structure)

A structure containing an LF-tag key-value pair.

CatalogId -> (string)

The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

TagKey -> (string)

The key-name for the LF-tag.

TagValues -> (list)

A list of possible values an attribute can take.

(string)

LFTagsOnColumns -> (list)

A list of LF-tags applied to a column resource.

(structure)

A structure containing the name of a column resource and the LF-tags attached to it.

Name -> (string)

The name of a column resource.

LFTags -> (list)

The LF-tags attached to a column resource.

(structure)

A structure containing an LF-tag key-value pair.

CatalogId -> (string)

The identifier for the Data Catalog. By default, the account ID. The Data Catalog is the persistent metadata store. It contains database definitions, table definitions, and other control information to manage your Lake Formation environment.

TagKey -> (string)

The key-name for the LF-tag.

TagValues -> (list)

A list of possible values an attribute can take.

(string)