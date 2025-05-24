# get-databasesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-databases.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-databases.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# get-databases

## Description

Retrieves all databases defined in a given Data Catalog.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetDatabases)

`get-databases` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `DatabaseList`

## Synopsis

```
get-databases
[--catalog-id <value>]
[--resource-share-type <value>]
[--attributes-to-get <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--catalog-id` (string)

The ID of the Data Catalog from which to retrieve `Databases` . If none is provided, the Amazon Web Services account ID is used by default.

`--resource-share-type` (string)

Allows you to specify that you want to list the databases shared with your account. The allowable values are `FEDERATED` , `FOREIGN` or `ALL` .

- If set to `FEDERATED` , will list the federated databases (referencing an external entity) shared with your account.
- If set to `FOREIGN` , will list the databases shared with your account.
- If set to `ALL` , will list the databases shared with your account, as well as the databases in yor local account.

Possible values:

- `FOREIGN`
- `ALL`
- `FEDERATED`

`--attributes-to-get` (list)

Specifies the database fields returned by the `GetDatabases` call. This parameter doesnât accept an empty list. The request must include the `NAME` .

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  NAME
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list the definitions of some or all of the databases in the AWS Glue Data Catalog**

The following `get-databases` example returns information about the databases in the Data Catalog.

```
aws glue get-databases
```

Output:

```
{
    "DatabaseList": [
        {
            "Name": "default",
            "Description": "Default Hive database",
            "LocationUri": "file:/spark-warehouse",
            "CreateTime": 1602084052.0,
            "CreateTableDefaultPermissions": [
                {
                    "Principal": {
                        "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
                    },
                    "Permissions": [
                        "ALL"
                    ]
                }
            ],
            "CatalogId": "111122223333"
        },
        {
            "Name": "flights-db",
            "CreateTime": 1587072847.0,
            "CreateTableDefaultPermissions": [
                {
                    "Principal": {
                        "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
                    },
                    "Permissions": [
                        "ALL"
                    ]
                }
            ],
            "CatalogId": "111122223333"
        },
        {
            "Name": "legislators",
            "CreateTime": 1601415625.0,
            "CreateTableDefaultPermissions": [
                {
                    "Principal": {
                        "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
                    },
                    "Permissions": [
                        "ALL"
                    ]
                }
            ],
            "CatalogId": "111122223333"
        },
        {
            "Name": "tempdb",
            "CreateTime": 1601498566.0,
            "CreateTableDefaultPermissions": [
                {
                    "Principal": {
                        "DataLakePrincipalIdentifier": "IAM_ALLOWED_PRINCIPALS"
                    },
                    "Permissions": [
                        "ALL"
                    ]
                }
            ],
            "CatalogId": "111122223333"
        }
    ]
}
```

For more information, see [Defining a Database in Your Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/define-database.html) in the *AWS Glue Developer Guide*.

## Output

DatabaseList -> (list)

A list of `Database` objects from the specified catalog.

(structure)

The `Database` object represents a logical grouping of tables that might reside in a Hive metastore or an RDBMS.

Name -> (string)

The name of the database. For Hive compatibility, this is folded to lowercase when it is stored.

Description -> (string)

A description of the database.

LocationUri -> (string)

The location of the database (for example, an HDFS path).

Parameters -> (map)

These key-value pairs define parameters and properties of the database.

key -> (string)

value -> (string)

CreateTime -> (timestamp)

The time at which the metadata database was created in the catalog.

CreateTableDefaultPermissions -> (list)

Creates a set of default permissions on the table for principals. Used by Lake Formation. Not used in the normal course of Glue operations.

(structure)

Permissions granted to a principal.

Principal -> (structure)

The principal who is granted permissions.

DataLakePrincipalIdentifier -> (string)

An identifier for the Lake Formation principal.

Permissions -> (list)

The permissions that are granted to the principal.

(string)

TargetDatabase -> (structure)

A `DatabaseIdentifier` structure that describes a target database for resource linking.

CatalogId -> (string)

The ID of the Data Catalog in which the database resides.

DatabaseName -> (string)

The name of the catalog database.

Region -> (string)

Region of the target database.

CatalogId -> (string)

The ID of the Data Catalog in which the database resides.

FederatedDatabase -> (structure)

A `FederatedDatabase` structure that references an entity outside the Glue Data Catalog.

Identifier -> (string)

A unique identifier for the federated database.

ConnectionName -> (string)

The name of the connection to the external metastore.

NextToken -> (string)

A continuation token for paginating the returned list of tokens, returned if the current segment of the list is not the last.