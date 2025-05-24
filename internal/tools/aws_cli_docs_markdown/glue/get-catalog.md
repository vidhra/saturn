# get-catalogÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-catalog.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-catalog.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# get-catalog

## Description

The name of the Catalog to retrieve. This should be all lowercase.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetCatalog)

## Synopsis

```
get-catalog
--catalog-id <value>
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

The ID of the parent catalog in which the catalog resides. If none is provided, the Amazon Web Services Account Number is used by default.

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

Catalog -> (structure)

A `Catalog` object. The definition of the specified catalog in the Glue Data Catalog.

CatalogId -> (string)

The ID of the catalog. To grant access to the default catalog, this field should not be provided.

Name -> (string)

The name of the catalog. Cannot be the same as the account ID.

ResourceArn -> (string)

The Amazon Resource Name (ARN) assigned to the catalog resource.

Description -> (string)

Description string, not more than 2048 bytes long, matching the URI address multi-line string pattern. A description of the catalog.

Parameters -> (map)

A map array of key-value pairs that define parameters and properties of the catalog.

key -> (string)

value -> (string)

CreateTime -> (timestamp)

The time at which the catalog was created.

UpdateTime -> (timestamp)

The time at which the catalog was last updated.

TargetRedshiftCatalog -> (structure)

A `TargetRedshiftCatalog` object that describes a target catalog for database resource linking.

CatalogArn -> (string)

The Amazon Resource Name (ARN) of the catalog resource.

FederatedCatalog -> (structure)

A `FederatedCatalog` object that points to an entity outside the Glue Data Catalog.

Identifier -> (string)

A unique identifier for the federated catalog.

ConnectionName -> (string)

The name of the connection to an external data source, for example a Redshift-federated catalog.

CatalogProperties -> (structure)

A `CatalogProperties` object that specifies data lake access properties and other custom properties.

DataLakeAccessProperties -> (structure)

A `DataLakeAccessProperties` object with input properties to configure data lake access for your catalog resource in the Glue Data Catalog.

DataLakeAccess -> (boolean)

Turns on or off data lake access for Apache Spark applications that access Amazon Redshift databases in the Data Catalog.

DataTransferRole -> (string)

A role that will be assumed by Glue for transferring data into/out of the staging bucket during a query.

KmsKey -> (string)

An encryption key that will be used for the staging bucket that will be created along with the catalog.

ManagedWorkgroupName -> (string)

The managed Redshift Serverless compute name that is created for your catalog resource.

ManagedWorkgroupStatus -> (string)

The managed Redshift Serverless compute status.

RedshiftDatabaseName -> (string)

The default Redshift database resource name in the managed compute.

StatusMessage -> (string)

A message that gives more detailed information about the managed workgroup status.

CatalogType -> (string)

Specifies a federated catalog type for the native catalog resource. The currently supported type is `aws:redshift` .

CustomProperties -> (map)

Additional key-value properties for the catalog, such as column statistics optimizations.

key -> (string)

value -> (string)

CreateTableDefaultPermissions -> (list)

An array of `PrincipalPermissions` objects. Creates a set of default permissions on the table(s) for principals. Used by Amazon Web Services Lake Formation. Not used in the normal course of Glue operations.

(structure)

Permissions granted to a principal.

Principal -> (structure)

The principal who is granted permissions.

DataLakePrincipalIdentifier -> (string)

An identifier for the Lake Formation principal.

Permissions -> (list)

The permissions that are granted to the principal.

(string)

CreateDatabaseDefaultPermissions -> (list)

An array of `PrincipalPermissions` objects. Creates a set of default permissions on the database(s) for principals. Used by Amazon Web Services Lake Formation. Not used in the normal course of Glue operations.

(structure)

Permissions granted to a principal.

Principal -> (structure)

The principal who is granted permissions.

DataLakePrincipalIdentifier -> (string)

An identifier for the Lake Formation principal.

Permissions -> (list)

The permissions that are granted to the principal.

(string)

AllowFullTableExternalDataAccess -> (string)

Allows third-party engines to access data in Amazon S3 locations that are registered with Lake Formation.