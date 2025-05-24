# delete-tenant-databaseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-tenant-database.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/delete-tenant-database.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# delete-tenant-database

## Description

Deletes a tenant database from your DB instance. This command only applies to RDS for Oracle container database (CDB) instances.

You canât delete a tenant database when it is the only tenant in the DB instance.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/DeleteTenantDatabase)

## Synopsis

```
delete-tenant-database
--db-instance-identifier <value>
--tenant-db-name <value>
[--skip-final-snapshot | --no-skip-final-snapshot]
[--final-db-snapshot-identifier <value>]
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

`--db-instance-identifier` (string)

The user-supplied identifier for the DB instance that contains the tenant database that you want to delete.

`--tenant-db-name` (string)

The user-supplied name of the tenant database that you want to remove from your DB instance. Amazon RDS deletes the tenant database with this name. This parameter isnât case-sensitive.

`--skip-final-snapshot` | `--no-skip-final-snapshot` (boolean)

Specifies whether to skip the creation of a final DB snapshot before removing the tenant database from your DB instance. If you enable this parameter, RDS doesnât create a DB snapshot. If you donât enable this parameter, RDS creates a DB snapshot before it deletes the tenant database. By default, RDS doesnât skip the final snapshot. If you donât enable this parameter, you must specify the `FinalDBSnapshotIdentifier` parameter.

`--final-db-snapshot-identifier` (string)

The `DBSnapshotIdentifier` of the new `DBSnapshot` created when the `SkipFinalSnapshot` parameter is disabled.

### Note

If you enable this parameter and also enable `SkipFinalShapshot` , the command results in an error.

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

TenantDatabase -> (structure)

A tenant database in the DB instance. This data type is an element in the response to the `DescribeTenantDatabases` action.

TenantDatabaseCreateTime -> (timestamp)

The creation time of the tenant database.

DBInstanceIdentifier -> (string)

The ID of the DB instance that contains the tenant database.

TenantDBName -> (string)

The database name of the tenant database.

Status -> (string)

The status of the tenant database.

MasterUsername -> (string)

The master username of the tenant database.

DbiResourceId -> (string)

The Amazon Web Services Region-unique, immutable identifier for the DB instance.

TenantDatabaseResourceId -> (string)

The Amazon Web Services Region-unique, immutable identifier for the tenant database.

TenantDatabaseARN -> (string)

The Amazon Resource Name (ARN) for the tenant database.

CharacterSetName -> (string)

The character set of the tenant database.

NcharCharacterSetName -> (string)

The `NCHAR` character set name of the tenant database.

DeletionProtection -> (boolean)

Specifies whether deletion protection is enabled for the DB instance.

PendingModifiedValues -> (structure)

Information about pending changes for a tenant database.

MasterUserPassword -> (string)

The master password for the tenant database.

TenantDBName -> (string)

The name of the tenant database.

MasterUserSecret -> (structure)

Contains the secret managed by RDS in Amazon Web Services Secrets Manager for the master user password.

For more information, see [Password management with Amazon Web Services Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-secrets-manager.html) in the *Amazon RDS User Guide* and [Password management with Amazon Web Services Secrets Manager](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-secrets-manager.html) in the *Amazon Aurora User Guide.*

SecretArn -> (string)

The Amazon Resource Name (ARN) of the secret.

SecretStatus -> (string)

The status of the secret.

The possible status values include the following:

- `creating` - The secret is being created.
- `active` - The secret is available for normal use and rotation.
- `rotating` - The secret is being rotated.
- `impaired` - The secret can be used to access database credentials, but it canât be rotated. A secret might have this status if, for example, permissions are changed so that RDS can no longer access either the secret or the KMS key for the secret. When a secret has this status, you can correct the condition that caused the status. Alternatively, modify the DB instance to turn off automatic management of database credentials, and then modify the DB instance again to turn on automatic management of database credentials.

KmsKeyId -> (string)

The Amazon Web Services KMS key identifier that is used to encrypt the secret.

TagList -> (list)

A list of tags.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

(structure)

Metadata assigned to an Amazon RDS resource consisting of a key-value pair.

For more information, see [Tagging Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Tagging.html) in the *Amazon RDS User Guide* or [Tagging Amazon Aurora and Amazon RDS resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_Tagging.html) in the *Amazon Aurora User Guide* .

Key -> (string)

A key is the required name of the tag. The string value can be from 1 to 128 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).

Value -> (string)

A value is the optional value of the tag. The string value can be from 1 to 256 Unicode characters in length and canât be prefixed with `aws:` or `rds:` . The string can only contain only the set of Unicode letters, digits, white-space, â_â, â.â, â:â, â/â, â=â, â+â, â-â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$â).