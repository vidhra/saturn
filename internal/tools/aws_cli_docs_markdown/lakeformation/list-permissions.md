# list-permissionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-permissions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/list-permissions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lakeformation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lakeformation/index.html#cli-aws-lakeformation) ]

# list-permissions

## Description

Returns a list of the principal permissions on the resource, filtered by the permissions of the caller. For example, if you are granted an ALTER permission, you are able to see only the principal permissions for ALTER.

This operation returns only those permissions that have been explicitly granted.

For information about permissions, see [Security and Access Control to Metadata and Data](https://docs.aws.amazon.com/lake-formation/latest/dg/security-data-access.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lakeformation-2017-03-31/ListPermissions)

## Synopsis

```
list-permissions
[--catalog-id <value>]
[--principal <value>]
[--resource-type <value>]
[--resource <value>]
[--next-token <value>]
[--max-results <value>]
[--include-related <value>]
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

`--principal` (structure)

Specifies a principal to filter the permissions returned.

DataLakePrincipalIdentifier -> (string)

An identifier for the Lake Formation principal.

Shorthand Syntax:

```
DataLakePrincipalIdentifier=string
```

JSON Syntax:

```
{
  "DataLakePrincipalIdentifier": "string"
}
```

`--resource-type` (string)

Specifies a resource type to filter the permissions returned.

Possible values:

- `CATALOG`
- `DATABASE`
- `TABLE`
- `DATA_LOCATION`
- `LF_TAG`
- `LF_TAG_POLICY`
- `LF_TAG_POLICY_DATABASE`
- `LF_TAG_POLICY_TABLE`
- `LF_NAMED_TAG_EXPRESSION`

`--resource` (structure)

A resource where you will get a list of the principal permissions.

This operation does not support getting privileges on a table with columns. Instead, call this operation on the table, and the operation returns the table and the table w columns.

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

`--next-token` (string)

A continuation token, if this is not the first call to retrieve this list.

`--max-results` (integer)

The maximum number of results to return.

`--include-related` (string)

Indicates that related permissions should be included in the results.

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

**Example 1: To retrieve list of principal permissions on the resource**

The following `list-permissions` example returns a list of principal permissions on the database resources.

```
aws lakeformation list-permissions \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "CatalogId": "123456789111",
    "ResourceType": "DATABASE",
    "MaxResults": 2
}
```

Output:

```
{
    "PrincipalResourcePermissions": [{
        "Principal": {
            "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-campaign-manager"
        },
        "Resource": {
            "Database": {
                "CatalogId": "123456789111",
                "Name": "tpc"
            }
        },
        "Permissions": [
            "DESCRIBE"
        ],
        "PermissionsWithGrantOption": []
    }],
    "NextToken": "E5SlJDSTZleUp6SWpvaU9UQTNORE0zTXpFeE5Ua3pJbjE5TENKbGVIQnBjbUYwYVc5dUlqcDdJbk5sWTI5dVpITWlPakUyTm"
}
```

For more information, see [Managing Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html) in the *AWS Lake Formation Developer Guide*.

**Example 2: To retrieve list of principal permissions on the table with data filters**

The following `list-permissions` example list the permissions on the table with related data filters granted to the principal.

```
aws lakeformation list-permissions \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "CatalogId": "123456789111",
    "Resource": {
        "Table": {
            "CatalogId": "123456789111",
            "DatabaseName": "tpc",
            "Name": "dl_tpc_customer"
        }
    },
    "IncludeRelated": "TRUE",
    "MaxResults": 10
}
```

Output:

```
{
    "PrincipalResourcePermissions": [{
            "Principal": {
                "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:role/Admin"
            },
            "Resource": {
                "Table": {
                    "CatalogId": "123456789111",
                    "DatabaseName": "customer",
                    "Name": "customer_invoice"
                }
            },
            "Permissions": [
                "ALL",
                "ALTER",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT"
            ],
            "PermissionsWithGrantOption": [
                "ALL",
                "ALTER",
                "DELETE",
                "DESCRIBE",
                "DROP",
                "INSERT"
            ]
        },
        {
            "Principal": {
                "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:role/Admin"
            },
            "Resource": {
                "TableWithColumns": {
                    "CatalogId": "123456789111",
                    "DatabaseName": "customer",
                    "Name": "customer_invoice",
                    "ColumnWildcard": {}
                }
            },
            "Permissions": [
                "SELECT"
            ],
            "PermissionsWithGrantOption": [
                "SELECT"
            ]
        },
        {
            "Principal": {
                "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:role/Admin"
            },
            "Resource": {
                "DataCellsFilter": {
                    "TableCatalogId": "123456789111",
                    "DatabaseName": "customer",
                    "TableName": "customer_invoice",
                    "Name": "dl_us_customer"
                }
            },
            "Permissions": [
                "DESCRIBE",
                "SELECT",
                "DROP"
            ],
            "PermissionsWithGrantOption": []
        }
    ],
    "NextToken": "VyeUFjY291bnRQZXJtaXNzaW9ucyI6ZmFsc2V9"
}
```

For more information, see [Managing Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html) in the *AWS Lake Formation Developer Guide*.

**Example 3: To retrieve list of principal permissions on the LF-Tags**

The following `list-permissions` example list the permissions on the LF-Tags granted to the principal.

```
aws lakeformation list-permissions \
    --cli-input-json file://input.json
```

Contents of `input.json`:

```
{
    "CatalogId": "123456789111",
    "Resource": {
        "LFTag": {
            "CatalogId": "123456789111",
            "TagKey": "category",
            "TagValues": [
                "private"
            ]
        }
    },
    "MaxResults": 10
}
```

Output:

```
{
    "PrincipalResourcePermissions": [{
            "Principal": {
                "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-admin"
            },
            "Resource": {
                "LFTag": {
                    "CatalogId": "123456789111",
                    "TagKey": "category",
                    "TagValues": [
                        "*"
                    ]
                }
            },
            "Permissions": [
                "DESCRIBE"
            ],
            "PermissionsWithGrantOption": [
                "DESCRIBE"
            ]
        },
        {
            "Principal": {
                "DataLakePrincipalIdentifier": "arn:aws:iam::123456789111:user/lf-admin"
            },
            "Resource": {
                "LFTag": {
                    "CatalogId": "123456789111",
                    "TagKey": "category",
                    "TagValues": [
                        "*"
                    ]
                }
            },
            "Permissions": [
                "ASSOCIATE"
            ],
            "PermissionsWithGrantOption": [
                "ASSOCIATE"
            ]
        }
    ],
    "NextToken": "EJwY21GMGFXOXVJanA3SW5Ocm1pc3Npb25zIjpmYWxzZX0="
}
```

For more information, see [Managing Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/managing-permissions.html) in the *AWS Lake Formation Developer Guide*.

## Output

PrincipalResourcePermissions -> (list)

A list of principals and their permissions on the resource for the specified principal and resource types.

(structure)

The permissions granted or revoked on a resource.

Principal -> (structure)

The Data Lake principal to be granted or revoked permissions.

DataLakePrincipalIdentifier -> (string)

An identifier for the Lake Formation principal.

Resource -> (structure)

The resource where permissions are to be granted or revoked.

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

Condition -> (structure)

A Lake Formation condition, which applies to permissions and opt-ins that contain an expression.

Expression -> (string)

An expression written based on the Cedar Policy Language used to match the principal attributes.

Permissions -> (list)

The permissions to be granted or revoked on the resource.

(string)

PermissionsWithGrantOption -> (list)

Indicates whether to grant the ability to grant permissions (as a subset of permissions granted).

(string)

AdditionalDetails -> (structure)

This attribute can be used to return any additional details of `PrincipalResourcePermissions` . Currently returns only as a RAM resource share ARN.

ResourceShare -> (list)

A resource share ARN for a catalog resource shared through RAM.

(string)

LastUpdated -> (timestamp)

The date and time when the resource was last updated.

LastUpdatedBy -> (string)

The user who updated the record.

NextToken -> (string)

A continuation token, if this is not the first call to retrieve this list.