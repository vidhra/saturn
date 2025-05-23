# modify-data-providerÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-data-provider.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/modify-data-provider.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dms/index.html#cli-aws-dms) ]

# modify-data-provider

## Description

Modifies the specified data provider using the provided settings.

### Note

You must remove the data provider from all migration projects before you can modify it.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dms-2016-01-01/ModifyDataProvider)

## Synopsis

```
modify-data-provider
--data-provider-identifier <value>
[--data-provider-name <value>]
[--description <value>]
[--engine <value>]
[--exact-settings | --no-exact-settings]
[--settings <value>]
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

`--data-provider-identifier` (string)

The identifier of the data provider. Identifiers must begin with a letter and must contain only ASCII letters, digits, and hyphens. They canât end with a hyphen, or contain two consecutive hyphens.

`--data-provider-name` (string)

The name of the data provider.

`--description` (string)

A user-friendly description of the data provider.

`--engine` (string)

The type of database engine for the data provider. Valid values include `"aurora"` , `"aurora-postgresql"` , `"mysql"` , `"oracle"` , `"postgres"` , `"sqlserver"` , `redshift` , `mariadb` , `mongodb` , `db2` , `db2-zos` and `docdb` . A value of `"aurora"` represents Amazon Aurora MySQL-Compatible Edition.

`--exact-settings` | `--no-exact-settings` (boolean)

If this attribute is Y, the current call to `ModifyDataProvider` replaces all existing data provider settings with the exact settings that you specify in this call. If this attribute is N, the current call to `ModifyDataProvider` does two things:

- It replaces any data provider settings that already exist with new values, for settings with the same names.
- It creates new data provider settings that you specify in the call, for settings with different names.

`--settings` (tagged union structure)

The settings in JSON format for a data provider.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `RedshiftSettings`, `PostgreSqlSettings`, `MySqlSettings`, `OracleSettings`, `MicrosoftSqlServerSettings`, `DocDbSettings`, `MariaDbSettings`, `IbmDb2LuwSettings`, `IbmDb2zOsSettings`, `MongoDbSettings`.

RedshiftSettings -> (structure)

Provides information that defines an Amazon Redshift data provider.

ServerName -> (string)

The name of the Amazon Redshift server.

Port -> (integer)

The port value for the Amazon Redshift data provider.

DatabaseName -> (string)

The database name on the Amazon Redshift data provider.

PostgreSqlSettings -> (structure)

Provides information that defines a PostgreSQL data provider.

ServerName -> (string)

The name of the PostgreSQL server.

Port -> (integer)

The port value for the PostgreSQL data provider.

DatabaseName -> (string)

The database name on the PostgreSQL data provider.

SslMode -> (string)

The SSL mode used to connect to the PostgreSQL data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

MySqlSettings -> (structure)

Provides information that defines a MySQL data provider.

ServerName -> (string)

The name of the MySQL server.

Port -> (integer)

The port value for the MySQL data provider.

SslMode -> (string)

The SSL mode used to connect to the MySQL data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

OracleSettings -> (structure)

Provides information that defines an Oracle data provider.

ServerName -> (string)

The name of the Oracle server.

Port -> (integer)

The port value for the Oracle data provider.

DatabaseName -> (string)

The database name on the Oracle data provider.

SslMode -> (string)

The SSL mode used to connect to the Oracle data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

AsmServer -> (string)

The address of your Oracle Automatic Storage Management (ASM) server. You can set this value from the `asm_server` value. You set `asm_server` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration) .

SecretsManagerOracleAsmSecretId -> (string)

The identifier of the secret in Secrets Manager that contains the Oracle ASM connection details.

Required only if your data provider uses the Oracle ASM server.

SecretsManagerOracleAsmAccessRoleArn -> (string)

The ARN of the IAM role that provides access to the secret in Secrets Manager that contains the Oracle ASM connection details.

SecretsManagerSecurityDbEncryptionSecretId -> (string)

The identifier of the secret in Secrets Manager that contains the transparent data encryption (TDE) password. DMS requires this password to access Oracle redo logs encrypted by TDE using Binary Reader.

SecretsManagerSecurityDbEncryptionAccessRoleArn -> (string)

The ARN of the IAM role that provides access to the secret in Secrets Manager that contains the TDE password.

MicrosoftSqlServerSettings -> (structure)

Provides information that defines a Microsoft SQL Server data provider.

ServerName -> (string)

The name of the Microsoft SQL Server server.

Port -> (integer)

The port value for the Microsoft SQL Server data provider.

DatabaseName -> (string)

The database name on the Microsoft SQL Server data provider.

SslMode -> (string)

The SSL mode used to connect to the Microsoft SQL Server data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

DocDbSettings -> (structure)

Provides information that defines a DocumentDB data provider.

ServerName -> (string)

The name of the source DocumentDB server.

Port -> (integer)

The port value for the DocumentDB data provider.

DatabaseName -> (string)

The database name on the DocumentDB data provider.

SslMode -> (string)

The SSL mode used to connect to the DocumentDB data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

MariaDbSettings -> (structure)

Provides information that defines a MariaDB data provider.

ServerName -> (string)

The name of the MariaDB server.

Port -> (integer)

The port value for the MariaDB data provider

SslMode -> (string)

The SSL mode used to connect to the MariaDB data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

IbmDb2LuwSettings -> (structure)

Provides information that defines an IBM DB2 LUW data provider.

ServerName -> (string)

The name of the DB2 LUW server.

Port -> (integer)

The port value for the DB2 LUW data provider.

DatabaseName -> (string)

The database name on the DB2 LUW data provider.

SslMode -> (string)

The SSL mode used to connect to the DB2 LUW data provider. The default value is `none` . Valid Values: `none` and `verify-ca` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

IbmDb2zOsSettings -> (structure)

Provides information that defines an IBM DB2 for z/OS data provider.

ServerName -> (string)

The name of the DB2 for z/OS server.

Port -> (integer)

The port value for the DB2 for z/OS data provider.

DatabaseName -> (string)

The database name on the DB2 for z/OS data provider.

SslMode -> (string)

The SSL mode used to connect to the DB2 for z/OS data provider. The default value is `none` . Valid Values: `none` and `verify-ca` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

MongoDbSettings -> (structure)

Provides information that defines a MongoDB data provider.

ServerName -> (string)

The name of the MongoDB server.

Port -> (integer)

The port value for the MongoDB data provider.

DatabaseName -> (string)

The database name on the MongoDB data provider.

SslMode -> (string)

The SSL mode used to connect to the MongoDB data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

AuthType -> (string)

The authentication type for the database connection. Valid values are PASSWORD or NO.

AuthSource -> (string)

The MongoDB database name. This setting isnât used when `AuthType` is set to `"no"` .

The default is `"admin"` .

AuthMechanism -> (string)

The authentication method for connecting to the data provider. Valid values are DEFAULT, MONGODB_CR, or SCRAM_SHA_1.

Shorthand Syntax:

```
RedshiftSettings={ServerName=string,Port=integer,DatabaseName=string},PostgreSqlSettings={ServerName=string,Port=integer,DatabaseName=string,SslMode=string,CertificateArn=string},MySqlSettings={ServerName=string,Port=integer,SslMode=string,CertificateArn=string},OracleSettings={ServerName=string,Port=integer,DatabaseName=string,SslMode=string,CertificateArn=string,AsmServer=string,SecretsManagerOracleAsmSecretId=string,SecretsManagerOracleAsmAccessRoleArn=string,SecretsManagerSecurityDbEncryptionSecretId=string,SecretsManagerSecurityDbEncryptionAccessRoleArn=string},MicrosoftSqlServerSettings={ServerName=string,Port=integer,DatabaseName=string,SslMode=string,CertificateArn=string},DocDbSettings={ServerName=string,Port=integer,DatabaseName=string,SslMode=string,CertificateArn=string},MariaDbSettings={ServerName=string,Port=integer,SslMode=string,CertificateArn=string},IbmDb2LuwSettings={ServerName=string,Port=integer,DatabaseName=string,SslMode=string,CertificateArn=string},IbmDb2zOsSettings={ServerName=string,Port=integer,DatabaseName=string,SslMode=string,CertificateArn=string},MongoDbSettings={ServerName=string,Port=integer,DatabaseName=string,SslMode=string,CertificateArn=string,AuthType=string,AuthSource=string,AuthMechanism=string}
```

JSON Syntax:

```
{
  "RedshiftSettings": {
    "ServerName": "string",
    "Port": integer,
    "DatabaseName": "string"
  },
  "PostgreSqlSettings": {
    "ServerName": "string",
    "Port": integer,
    "DatabaseName": "string",
    "SslMode": "none"|"require"|"verify-ca"|"verify-full",
    "CertificateArn": "string"
  },
  "MySqlSettings": {
    "ServerName": "string",
    "Port": integer,
    "SslMode": "none"|"require"|"verify-ca"|"verify-full",
    "CertificateArn": "string"
  },
  "OracleSettings": {
    "ServerName": "string",
    "Port": integer,
    "DatabaseName": "string",
    "SslMode": "none"|"require"|"verify-ca"|"verify-full",
    "CertificateArn": "string",
    "AsmServer": "string",
    "SecretsManagerOracleAsmSecretId": "string",
    "SecretsManagerOracleAsmAccessRoleArn": "string",
    "SecretsManagerSecurityDbEncryptionSecretId": "string",
    "SecretsManagerSecurityDbEncryptionAccessRoleArn": "string"
  },
  "MicrosoftSqlServerSettings": {
    "ServerName": "string",
    "Port": integer,
    "DatabaseName": "string",
    "SslMode": "none"|"require"|"verify-ca"|"verify-full",
    "CertificateArn": "string"
  },
  "DocDbSettings": {
    "ServerName": "string",
    "Port": integer,
    "DatabaseName": "string",
    "SslMode": "none"|"require"|"verify-ca"|"verify-full",
    "CertificateArn": "string"
  },
  "MariaDbSettings": {
    "ServerName": "string",
    "Port": integer,
    "SslMode": "none"|"require"|"verify-ca"|"verify-full",
    "CertificateArn": "string"
  },
  "IbmDb2LuwSettings": {
    "ServerName": "string",
    "Port": integer,
    "DatabaseName": "string",
    "SslMode": "none"|"require"|"verify-ca"|"verify-full",
    "CertificateArn": "string"
  },
  "IbmDb2zOsSettings": {
    "ServerName": "string",
    "Port": integer,
    "DatabaseName": "string",
    "SslMode": "none"|"require"|"verify-ca"|"verify-full",
    "CertificateArn": "string"
  },
  "MongoDbSettings": {
    "ServerName": "string",
    "Port": integer,
    "DatabaseName": "string",
    "SslMode": "none"|"require"|"verify-ca"|"verify-full",
    "CertificateArn": "string",
    "AuthType": "no"|"password",
    "AuthSource": "string",
    "AuthMechanism": "default"|"mongodb_cr"|"scram_sha_1"
  }
}
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

DataProvider -> (structure)

The data provider that was modified.

DataProviderName -> (string)

The name of the data provider.

DataProviderArn -> (string)

The Amazon Resource Name (ARN) string that uniquely identifies the data provider.

DataProviderCreationTime -> (timestamp)

The time the data provider was created.

Description -> (string)

A description of the data provider. Descriptions can have up to 31 characters. A description can contain only ASCII letters, digits, and hyphens (â-â). Also, it canât end with a hyphen or contain two consecutive hyphens, and can only begin with a letter.

Engine -> (string)

The type of database engine for the data provider. Valid values include `"aurora"` , `"aurora-postgresql"` , `"mysql"` , `"oracle"` , `"postgres"` , `"sqlserver"` , `redshift` , `mariadb` , `mongodb` , `db2` , `db2-zos` and `docdb` . A value of `"aurora"` represents Amazon Aurora MySQL-Compatible Edition.

Settings -> (tagged union structure)

The settings in JSON format for a data provider.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `RedshiftSettings`, `PostgreSqlSettings`, `MySqlSettings`, `OracleSettings`, `MicrosoftSqlServerSettings`, `DocDbSettings`, `MariaDbSettings`, `IbmDb2LuwSettings`, `IbmDb2zOsSettings`, `MongoDbSettings`.

RedshiftSettings -> (structure)

Provides information that defines an Amazon Redshift data provider.

ServerName -> (string)

The name of the Amazon Redshift server.

Port -> (integer)

The port value for the Amazon Redshift data provider.

DatabaseName -> (string)

The database name on the Amazon Redshift data provider.

PostgreSqlSettings -> (structure)

Provides information that defines a PostgreSQL data provider.

ServerName -> (string)

The name of the PostgreSQL server.

Port -> (integer)

The port value for the PostgreSQL data provider.

DatabaseName -> (string)

The database name on the PostgreSQL data provider.

SslMode -> (string)

The SSL mode used to connect to the PostgreSQL data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

MySqlSettings -> (structure)

Provides information that defines a MySQL data provider.

ServerName -> (string)

The name of the MySQL server.

Port -> (integer)

The port value for the MySQL data provider.

SslMode -> (string)

The SSL mode used to connect to the MySQL data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

OracleSettings -> (structure)

Provides information that defines an Oracle data provider.

ServerName -> (string)

The name of the Oracle server.

Port -> (integer)

The port value for the Oracle data provider.

DatabaseName -> (string)

The database name on the Oracle data provider.

SslMode -> (string)

The SSL mode used to connect to the Oracle data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

AsmServer -> (string)

The address of your Oracle Automatic Storage Management (ASM) server. You can set this value from the `asm_server` value. You set `asm_server` as part of the extra connection attribute string to access an Oracle server with Binary Reader that uses ASM. For more information, see [Configuration for change data capture (CDC) on an Oracle source database](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.Oracle.html#dms/latest/userguide/CHAP_Source.Oracle.html#CHAP_Source.Oracle.CDC.Configuration) .

SecretsManagerOracleAsmSecretId -> (string)

The identifier of the secret in Secrets Manager that contains the Oracle ASM connection details.

Required only if your data provider uses the Oracle ASM server.

SecretsManagerOracleAsmAccessRoleArn -> (string)

The ARN of the IAM role that provides access to the secret in Secrets Manager that contains the Oracle ASM connection details.

SecretsManagerSecurityDbEncryptionSecretId -> (string)

The identifier of the secret in Secrets Manager that contains the transparent data encryption (TDE) password. DMS requires this password to access Oracle redo logs encrypted by TDE using Binary Reader.

SecretsManagerSecurityDbEncryptionAccessRoleArn -> (string)

The ARN of the IAM role that provides access to the secret in Secrets Manager that contains the TDE password.

MicrosoftSqlServerSettings -> (structure)

Provides information that defines a Microsoft SQL Server data provider.

ServerName -> (string)

The name of the Microsoft SQL Server server.

Port -> (integer)

The port value for the Microsoft SQL Server data provider.

DatabaseName -> (string)

The database name on the Microsoft SQL Server data provider.

SslMode -> (string)

The SSL mode used to connect to the Microsoft SQL Server data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

DocDbSettings -> (structure)

Provides information that defines a DocumentDB data provider.

ServerName -> (string)

The name of the source DocumentDB server.

Port -> (integer)

The port value for the DocumentDB data provider.

DatabaseName -> (string)

The database name on the DocumentDB data provider.

SslMode -> (string)

The SSL mode used to connect to the DocumentDB data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

MariaDbSettings -> (structure)

Provides information that defines a MariaDB data provider.

ServerName -> (string)

The name of the MariaDB server.

Port -> (integer)

The port value for the MariaDB data provider

SslMode -> (string)

The SSL mode used to connect to the MariaDB data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

IbmDb2LuwSettings -> (structure)

Provides information that defines an IBM DB2 LUW data provider.

ServerName -> (string)

The name of the DB2 LUW server.

Port -> (integer)

The port value for the DB2 LUW data provider.

DatabaseName -> (string)

The database name on the DB2 LUW data provider.

SslMode -> (string)

The SSL mode used to connect to the DB2 LUW data provider. The default value is `none` . Valid Values: `none` and `verify-ca` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

IbmDb2zOsSettings -> (structure)

Provides information that defines an IBM DB2 for z/OS data provider.

ServerName -> (string)

The name of the DB2 for z/OS server.

Port -> (integer)

The port value for the DB2 for z/OS data provider.

DatabaseName -> (string)

The database name on the DB2 for z/OS data provider.

SslMode -> (string)

The SSL mode used to connect to the DB2 for z/OS data provider. The default value is `none` . Valid Values: `none` and `verify-ca` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

MongoDbSettings -> (structure)

Provides information that defines a MongoDB data provider.

ServerName -> (string)

The name of the MongoDB server.

Port -> (integer)

The port value for the MongoDB data provider.

DatabaseName -> (string)

The database name on the MongoDB data provider.

SslMode -> (string)

The SSL mode used to connect to the MongoDB data provider. The default value is `none` .

CertificateArn -> (string)

The Amazon Resource Name (ARN) of the certificate used for SSL connection.

AuthType -> (string)

The authentication type for the database connection. Valid values are PASSWORD or NO.

AuthSource -> (string)

The MongoDB database name. This setting isnât used when `AuthType` is set to `"no"` .

The default is `"admin"` .

AuthMechanism -> (string)

The authentication method for connecting to the data provider. Valid values are DEFAULT, MONGODB_CR, or SCRAM_SHA_1.