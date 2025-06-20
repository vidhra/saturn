# create-data-catalogÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [athena](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/index.html#cli-aws-athena) ]

# create-data-catalog

## Description

Creates (registers) a data catalog with the specified name and properties. Catalogs created are visible to all users of the same Amazon Web Services account.

For a `FEDERATED` catalog, this API operation creates the following resources.

- CFN Stack Name with a maximum length of 128 characters and prefix `athenafederatedcatalog-CATALOG_NAME_SANITIZED` with length 23 characters.
- Lambda Function Name with a maximum length of 64 characters and prefix `athenafederatedcatalog_CATALOG_NAME_SANITIZED` with length 23 characters.
- Glue Connection Name with a maximum length of 255 characters and a prefix `athenafederatedcatalog_CATALOG_NAME_SANITIZED` with length 23 characters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/CreateDataCatalog)

## Synopsis

```
create-data-catalog
--name <value>
--type <value>
[--description <value>]
[--parameters <value>]
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

`--name` (string)

The name of the data catalog to create. The catalog name must be unique for the Amazon Web Services account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.

For `FEDERATED` type the catalog name has following considerations and limits:

- The catalog name allows special characters such as `_ , @ , \ , -` . These characters are replaced with a hyphen (-) when creating the CFN Stack Name and with an underscore (_) when creating the Lambda Function and Glue Connection Name.
- The catalog name has a theoretical limit of 128 characters. However, since we use it to create other resources that allow less characters and we prepend a prefix to it, the actual catalog name limit for `FEDERATED` catalog is 64 - 23 = 41 characters.

`--type` (string)

The type of data catalog to create: `LAMBDA` for a federated catalog, `GLUE` for an Glue Data Catalog, and `HIVE` for an external Apache Hive metastore. `FEDERATED` is a federated catalog for which Athena creates the connection and the Lambda function for you based on the parameters that you pass.

For `FEDERATED` type, we do not support IAM identity center.

Possible values:

- `LAMBDA`
- `GLUE`
- `HIVE`
- `FEDERATED`

`--description` (string)

A description of the data catalog to be created.

`--parameters` (map)

Specifies the Lambda function or functions to use for creating the data catalog. This is a mapping whose values depend on the catalog type.

- For the `HIVE` data catalog type, use the following syntax. The `metadata-function` parameter is required. `The sdk-version` parameter is optional and defaults to the currently supported version.  [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html#id1)metadata-function=*lambda_arn* , sdk-version=*version_number* ``
- For the `LAMBDA` data catalog type, use one of the following sets of required parameters, but not both.
- If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.  [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html#id3)metadata-function=*lambda_arn* , record-function=*lambda_arn* ``
- If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.  [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html#id5)function=*lambda_arn* ``
- The `GLUE` type takes a catalog ID parameter and is required. The `` *catalog_id* `` is the account ID of the Amazon Web Services account to which the Glue Data Catalog belongs.  [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html#id7)catalog-id=*catalog_id* ``
- The `GLUE` data catalog type also applies to the default `AwsDataCatalog` that already exists in your account, of which you can have only one and cannot modify.
- The `FEDERATED` data catalog type uses one of the following parameters, but not both. Use `connection-arn` for an existing Glue connection. Use `connection-type` and `connection-properties` to specify the configuration setting for a new connection.
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html#id9)connection-arn:*<glue_connection_arn_to_reuse>* ``
- `lambda-role-arn` (optional): The execution role to use for the Lambda function. If not provided, one is created.
- `connection-type:MYSQL|REDSHIFT|...., connection-properties:"*<json_string>* "`   For * `<json_string>` * , use escaped JSON text, as in the following example.  `"{\"spill_bucket\":\"my_spill\",\"spill_prefix\":\"athena-spill\",\"host\":\"abc12345.snowflakecomputing.com\",\"port\":\"1234\",\"warehouse\":\"DEV_WH\",\"database\":\"TEST\",\"schema\":\"PUBLIC\",\"SecretArn\":\"arn:aws:secretsmanager:ap-south-1:111122223333:secret:snowflake-XHb67j\"}"`

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

`--tags` (list)

A list of comma separated tags to add to the data catalog that is created. All the resources that are created by the `CreateDataCatalog` API operation with `FEDERATED` type will have the tag `federated_athena_datacatalog="true"` . This includes the CFN Stack, Glue Connection, Athena DataCatalog, and all the resources created as part of the CFN Stack (Lambda Function, IAM policies/roles).

(structure)

A label that you assign to a resource. Athena resources include workgroups, data catalogs, and capacity reservations. Each tag consists of a key and an optional value, both of which you define. For example, you can use tags to categorize Athena resources by purpose, owner, or environment. Use a consistent set of tag keys to make it easier to search and filter the resources in your account. For best practices, see [Tagging Best Practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) . Tag keys can be from 1 to 128 UTF-8 Unicode characters, and tag values can be from 0 to 256 UTF-8 Unicode characters. Tags can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys and values are case-sensitive. Tag keys must be unique per resource. If you specify more than one tag, separate them by commas.

Key -> (string)

A tag key. The tag key length is from 1 to 128 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag keys are case-sensitive and must be unique per resource.

Value -> (string)

A tag value. The tag value length is from 0 to 256 Unicode characters in UTF-8. You can use letters and numbers representable in UTF-8, and the following characters: + - = . _ : / @. Tag values are case-sensitive.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a data catalog**

The following `create-data-catalog` example creates the `dynamo_db_catalog` data catalog.

```
aws athena create-data-catalog \
    --name dynamo_db_catalog \
    --type LAMBDA \
    --description "DynamoDB Catalog" \
    --parameters function=arn:aws:lambda:us-west-2:111122223333:function:dynamo_db_lambda
```

This command produces no output. To see the result, use `aws athena get-data-catalog --name dynamo_db_catalog`.

For more information, see [Registering a Catalog: create-data-catalog](https://docs.aws.amazon.com/athena/latest/ug/datastores-hive-cli.html#datastores-hive-cli-registering-a-catalog) in the *Amazon Athena User Guide*.

## Output

DataCatalog -> (structure)

Contains information about a data catalog in an Amazon Web Services account.

### Note

In the Athena console, data catalogs are listed as âdata sourcesâ on the **Data sources** page under the **Data source name** column.

Name -> (string)

The name of the data catalog. The catalog name must be unique for the Amazon Web Services account and can use a maximum of 127 alphanumeric, underscore, at sign, or hyphen characters. The remainder of the length constraint of 256 is reserved for use by Athena.

Description -> (string)

An optional description of the data catalog.

Type -> (string)

The type of data catalog to create: `LAMBDA` for a federated catalog, `GLUE` for an Glue Data Catalog, and `HIVE` for an external Apache Hive metastore. `FEDERATED` is a federated catalog for which Athena creates the connection and the Lambda function for you based on the parameters that you pass.

Parameters -> (map)

Specifies the Lambda function or functions to use for the data catalog. This is a mapping whose values depend on the catalog type.

- For the `HIVE` data catalog type, use the following syntax. The `metadata-function` parameter is required. `The sdk-version` parameter is optional and defaults to the currently supported version.  [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html#id11)metadata-function=*lambda_arn* , sdk-version=*version_number* ``
- For the `LAMBDA` data catalog type, use one of the following sets of required parameters, but not both.
- If you have one Lambda function that processes metadata and another for reading the actual data, use the following syntax. Both parameters are required.  [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html#id13)metadata-function=*lambda_arn* , record-function=*lambda_arn* ``
- If you have a composite Lambda function that processes both metadata and data, use the following syntax to specify your Lambda function.  [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html#id15)function=*lambda_arn* ``
- The `GLUE` type takes a catalog ID parameter and is required. The `` *catalog_id* `` is the account ID of the Amazon Web Services account to which the Glue catalog belongs.  [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html#id17)catalog-id=*catalog_id* ``
- The `GLUE` data catalog type also applies to the default `AwsDataCatalog` that already exists in your account, of which you can have only one and cannot modify.
- The `FEDERATED` data catalog type uses one of the following parameters, but not both. Use `connection-arn` for an existing Glue connection. Use `connection-type` and `connection-properties` to specify the configuration setting for a new connection.
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-data-catalog.html#id19)connection-arn:*<glue_connection_arn_to_reuse>* ``
- `connection-type:MYSQL|REDSHIFT|...., connection-properties:"*<json_string>* "`   For * `<json_string>` * , use escaped JSON text, as in the following example.  `"{\"spill_bucket\":\"my_spill\",\"spill_prefix\":\"athena-spill\",\"host\":\"abc12345.snowflakecomputing.com\",\"port\":\"1234\",\"warehouse\":\"DEV_WH\",\"database\":\"TEST\",\"schema\":\"PUBLIC\",\"SecretArn\":\"arn:aws:secretsmanager:ap-south-1:111122223333:secret:snowflake-XHb67j\"}"`

key -> (string)

value -> (string)

Status -> (string)

The status of the creation or deletion of the data catalog.

- The `LAMBDA` , `GLUE` , and `HIVE` data catalog types are created synchronously. Their status is either `CREATE_COMPLETE` or `CREATE_FAILED` .
- The `FEDERATED` data catalog type is created asynchronously.

Data catalog creation status:

- `CREATE_IN_PROGRESS` : Federated data catalog creation in progress.
- `CREATE_COMPLETE` : Data catalog creation complete.
- `CREATE_FAILED` : Data catalog could not be created.
- `CREATE_FAILED_CLEANUP_IN_PROGRESS` : Federated data catalog creation failed and is being removed.
- `CREATE_FAILED_CLEANUP_COMPLETE` : Federated data catalog creation failed and was removed.
- `CREATE_FAILED_CLEANUP_FAILED` : Federated data catalog creation failed but could not be removed.

Data catalog deletion status:

- `DELETE_IN_PROGRESS` : Federated data catalog deletion in progress.
- `DELETE_COMPLETE` : Federated data catalog deleted.
- `DELETE_FAILED` : Federated data catalog could not be deleted.

ConnectionType -> (string)

The type of connection for a `FEDERATED` data catalog (for example, `REDSHIFT` , `MYSQL` , or `SQLSERVER` ). For information about individual connectors, see [Available data source connectors](https://docs.aws.amazon.com/athena/latest/ug/connectors-available.html) .

Error -> (string)

Text of the error that occurred during data catalog creation or deletion.