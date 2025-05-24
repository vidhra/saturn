# create-data-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-data-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/create-data-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# create-data-source

## Description

Creates a data source.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/CreateDataSource)

## Synopsis

```
create-data-source
--aws-account-id <value>
--data-source-id <value>
--name <value>
--type <value>
[--data-source-parameters <value>]
[--credentials <value>]
[--permissions <value>]
[--vpc-connection-properties <value>]
[--ssl-properties <value>]
[--tags <value>]
[--folder-arns <value>]
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

`--aws-account-id` (string)

The Amazon Web Services account ID.

`--data-source-id` (string)

An ID for the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.

`--name` (string)

A display name for the data source.

`--type` (string)

The type of the data source. To return a list of all data sources, use `ListDataSources` .

Use `AMAZON_ELASTICSEARCH` for Amazon OpenSearch Service.

Possible values:

- `ADOBE_ANALYTICS`
- `AMAZON_ELASTICSEARCH`
- `ATHENA`
- `AURORA`
- `AURORA_POSTGRESQL`
- `AWS_IOT_ANALYTICS`
- `GITHUB`
- `JIRA`
- `MARIADB`
- `MYSQL`
- `ORACLE`
- `POSTGRESQL`
- `PRESTO`
- `REDSHIFT`
- `S3`
- `SALESFORCE`
- `SERVICENOW`
- `SNOWFLAKE`
- `SPARK`
- `SQLSERVER`
- `TERADATA`
- `TWITTER`
- `TIMESTREAM`
- `AMAZON_OPENSEARCH`
- `EXASOL`
- `DATABRICKS`
- `STARBURST`
- `TRINO`
- `BIGQUERY`

`--data-source-parameters` (structure)

The parameters that Amazon QuickSight uses to connect to your underlying source.

AmazonElasticsearchParameters -> (structure)

The parameters for OpenSearch.

Domain -> (string)

The OpenSearch domain.

AthenaParameters -> (structure)

The parameters for Amazon Athena.

WorkGroup -> (string)

The workgroup that Amazon Athena uses.

RoleArn -> (string)

Use the `RoleArn` structure to override an account-wide role for a specific Athena data source. For example, say an account administrator has turned off all Athena access with an account-wide role. The administrator can then use `RoleArn` to bypass the account-wide role and allow Athena access for the single Athena data source that is specified in the structure, even if the account-wide role forbidding Athena access is still active.

AuroraParameters -> (structure)

The parameters for Amazon Aurora MySQL.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

AuroraPostgreSqlParameters -> (structure)

The parameters for Amazon Aurora.

Host -> (string)

The Amazon Aurora PostgreSQL-Compatible host to connect to.

Port -> (integer)

The port that Amazon Aurora PostgreSQL is listening on.

Database -> (string)

The Amazon Aurora PostgreSQL database to connect to.

AwsIotAnalyticsParameters -> (structure)

The parameters for IoT Analytics.

DataSetName -> (string)

Dataset name.

JiraParameters -> (structure)

The parameters for Jira.

SiteBaseUrl -> (string)

The base URL of the Jira site.

MariaDbParameters -> (structure)

The parameters for MariaDB.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

MySqlParameters -> (structure)

The parameters for MySQL.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

OracleParameters -> (structure)

The parameters for Oracle.

Host -> (string)

An Oracle host.

Port -> (integer)

The port.

Database -> (string)

The database.

UseServiceName -> (boolean)

A Boolean value that indicates whether the `Database` uses a service name or an SID. If this value is left blank, the default value is `SID` . If this value is set to `false` , the value is `SID` .

PostgreSqlParameters -> (structure)

The parameters for PostgreSQL.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

PrestoParameters -> (structure)

The parameters for Presto.

Host -> (string)

Host.

Port -> (integer)

Port.

Catalog -> (string)

Catalog.

RdsParameters -> (structure)

The parameters for Amazon RDS.

InstanceId -> (string)

Instance ID.

Database -> (string)

Database.

RedshiftParameters -> (structure)

The parameters for Amazon Redshift.

Host -> (string)

Host. This field can be blank if `ClusterId` is provided.

Port -> (integer)

Port. This field can be blank if the `ClusterId` is provided.

Database -> (string)

Database.

ClusterId -> (string)

Cluster ID. This field can be blank if the `Host` and `Port` are provided.

IAMParameters -> (structure)

An optional parameter that uses IAM authentication to grant Amazon QuickSight access to your cluster. This parameter can be used instead of [DataSourceCredentials](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSourceCredentials.html) .

RoleArn -> (string)

Use the `RoleArn` structure to allow Amazon QuickSight to call `redshift:GetClusterCredentials` on your cluster. The calling principal must have `iam:PassRole` access to pass the role to Amazon QuickSight. The roleâs trust policy must allow the Amazon QuickSight service principal to assume the role.

DatabaseUser -> (string)

The user whose permissions and group memberships will be used by Amazon QuickSight to access the cluster. If this user already exists in your database, Amazon QuickSight is granted the same permissions that the user has. If the user doesnât exist, set the value of `AutoCreateDatabaseUser` to `True` to create a new user with PUBLIC permissions.

DatabaseGroups -> (list)

A list of groups whose permissions will be granted to Amazon QuickSight to access the cluster. These permissions are combined with the permissions granted to Amazon QuickSight by the `DatabaseUser` . If you choose to include this parameter, the `RoleArn` must grant access to `redshift:JoinGroup` .

(string)

AutoCreateDatabaseUser -> (boolean)

Automatically creates a database user. If your database doesnât have a `DatabaseUser` , set this parameter to `True` . If there is no `DatabaseUser` , Amazon QuickSight canât connect to your cluster. The `RoleArn` that you use for this operation must grant access to `redshift:CreateClusterUser` to successfully create the user.

IdentityCenterConfiguration -> (structure)

An optional parameter that configures IAM Identity Center authentication to grant Amazon QuickSight access to your cluster.

This parameter can only be specified if your Amazon QuickSight account is configured with IAM Identity Center.

EnableIdentityPropagation -> (boolean)

A Boolean option that controls whether Trusted Identity Propagation should be used.

S3Parameters -> (structure)

The parameters for S3.

ManifestFileLocation -> (structure)

Location of the Amazon S3 manifest file. This is NULL if the manifest file was uploaded into Amazon QuickSight.

Bucket -> (string)

Amazon S3 bucket.

Key -> (string)

Amazon S3 key that identifies an object.

RoleArn -> (string)

Use the `RoleArn` structure to override an account-wide role for a specific S3 data source. For example, say an account administrator has turned off all S3 access with an account-wide role. The administrator can then use `RoleArn` to bypass the account-wide role and allow S3 access for the single S3 data source that is specified in the structure, even if the account-wide role forbidding S3 access is still active.

ServiceNowParameters -> (structure)

The parameters for ServiceNow.

SiteBaseUrl -> (string)

URL of the base site.

SnowflakeParameters -> (structure)

The parameters for Snowflake.

Host -> (string)

Host.

Database -> (string)

Database.

Warehouse -> (string)

Warehouse.

AuthenticationType -> (string)

The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.

DatabaseAccessControlRole -> (string)

The database access control role.

OAuthParameters -> (structure)

An object that contains information needed to create a data source connection between an Amazon QuickSight account and Snowflake.

TokenProviderUrl -> (string)

The token endpoint URL of the identity provider.

OAuthScope -> (string)

The OAuth scope.

IdentityProviderVpcConnectionProperties -> (structure)

VPC connection properties.

VpcConnectionArn -> (string)

The Amazon Resource Name (ARN) for the VPC connection.

IdentityProviderResourceUri -> (string)

The resource uri of the identity provider.

SparkParameters -> (structure)

The parameters for Spark.

Host -> (string)

Host.

Port -> (integer)

Port.

SqlServerParameters -> (structure)

The parameters for SQL Server.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

TeradataParameters -> (structure)

The parameters for Teradata.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

TwitterParameters -> (structure)

The parameters for Twitter.

Query -> (string)

Twitter query string.

MaxRows -> (integer)

Maximum number of rows to query Twitter.

AmazonOpenSearchParameters -> (structure)

The parameters for OpenSearch.

Domain -> (string)

The OpenSearch domain.

ExasolParameters -> (structure)

The parameters for Exasol.

Host -> (string)

The hostname or IP address of the Exasol data source.

Port -> (integer)

The port for the Exasol data source.

DatabricksParameters -> (structure)

The parameters that are required to connect to a Databricks data source.

Host -> (string)

The host name of the Databricks data source.

Port -> (integer)

The port for the Databricks data source.

SqlEndpointPath -> (string)

The HTTP path of the Databricks data source.

StarburstParameters -> (structure)

The parameters that are required to connect to a Starburst data source.

Host -> (string)

The host name of the Starburst data source.

Port -> (integer)

The port for the Starburst data source.

Catalog -> (string)

The catalog name for the Starburst data source.

ProductType -> (string)

The product type for the Starburst data source.

DatabaseAccessControlRole -> (string)

The database access control role.

AuthenticationType -> (string)

The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.

OAuthParameters -> (structure)

An object that contains information needed to create a data source connection between an Amazon QuickSight account and Starburst.

TokenProviderUrl -> (string)

The token endpoint URL of the identity provider.

OAuthScope -> (string)

The OAuth scope.

IdentityProviderVpcConnectionProperties -> (structure)

VPC connection properties.

VpcConnectionArn -> (string)

The Amazon Resource Name (ARN) for the VPC connection.

IdentityProviderResourceUri -> (string)

The resource uri of the identity provider.

TrinoParameters -> (structure)

The parameters that are required to connect to a Trino data source.

Host -> (string)

The host name of the Trino data source.

Port -> (integer)

The port for the Trino data source.

Catalog -> (string)

The catalog name for the Trino data source.

BigQueryParameters -> (structure)

The parameters that are required to connect to a Google BigQuery data source.

ProjectId -> (string)

The Google Cloud Platform project ID where your datasource was created.

DataSetRegion -> (string)

The storage location where you create a Google BigQuery data source.

JSON Syntax:

```
{
  "AmazonElasticsearchParameters": {
    "Domain": "string"
  },
  "AthenaParameters": {
    "WorkGroup": "string",
    "RoleArn": "string"
  },
  "AuroraParameters": {
    "Host": "string",
    "Port": integer,
    "Database": "string"
  },
  "AuroraPostgreSqlParameters": {
    "Host": "string",
    "Port": integer,
    "Database": "string"
  },
  "AwsIotAnalyticsParameters": {
    "DataSetName": "string"
  },
  "JiraParameters": {
    "SiteBaseUrl": "string"
  },
  "MariaDbParameters": {
    "Host": "string",
    "Port": integer,
    "Database": "string"
  },
  "MySqlParameters": {
    "Host": "string",
    "Port": integer,
    "Database": "string"
  },
  "OracleParameters": {
    "Host": "string",
    "Port": integer,
    "Database": "string",
    "UseServiceName": true|false
  },
  "PostgreSqlParameters": {
    "Host": "string",
    "Port": integer,
    "Database": "string"
  },
  "PrestoParameters": {
    "Host": "string",
    "Port": integer,
    "Catalog": "string"
  },
  "RdsParameters": {
    "InstanceId": "string",
    "Database": "string"
  },
  "RedshiftParameters": {
    "Host": "string",
    "Port": integer,
    "Database": "string",
    "ClusterId": "string",
    "IAMParameters": {
      "RoleArn": "string",
      "DatabaseUser": "string",
      "DatabaseGroups": ["string", ...],
      "AutoCreateDatabaseUser": true|false
    },
    "IdentityCenterConfiguration": {
      "EnableIdentityPropagation": true|false
    }
  },
  "S3Parameters": {
    "ManifestFileLocation": {
      "Bucket": "string",
      "Key": "string"
    },
    "RoleArn": "string"
  },
  "ServiceNowParameters": {
    "SiteBaseUrl": "string"
  },
  "SnowflakeParameters": {
    "Host": "string",
    "Database": "string",
    "Warehouse": "string",
    "AuthenticationType": "PASSWORD"|"TOKEN"|"X509",
    "DatabaseAccessControlRole": "string",
    "OAuthParameters": {
      "TokenProviderUrl": "string",
      "OAuthScope": "string",
      "IdentityProviderVpcConnectionProperties": {
        "VpcConnectionArn": "string"
      },
      "IdentityProviderResourceUri": "string"
    }
  },
  "SparkParameters": {
    "Host": "string",
    "Port": integer
  },
  "SqlServerParameters": {
    "Host": "string",
    "Port": integer,
    "Database": "string"
  },
  "TeradataParameters": {
    "Host": "string",
    "Port": integer,
    "Database": "string"
  },
  "TwitterParameters": {
    "Query": "string",
    "MaxRows": integer
  },
  "AmazonOpenSearchParameters": {
    "Domain": "string"
  },
  "ExasolParameters": {
    "Host": "string",
    "Port": integer
  },
  "DatabricksParameters": {
    "Host": "string",
    "Port": integer,
    "SqlEndpointPath": "string"
  },
  "StarburstParameters": {
    "Host": "string",
    "Port": integer,
    "Catalog": "string",
    "ProductType": "GALAXY"|"ENTERPRISE",
    "DatabaseAccessControlRole": "string",
    "AuthenticationType": "PASSWORD"|"TOKEN"|"X509",
    "OAuthParameters": {
      "TokenProviderUrl": "string",
      "OAuthScope": "string",
      "IdentityProviderVpcConnectionProperties": {
        "VpcConnectionArn": "string"
      },
      "IdentityProviderResourceUri": "string"
    }
  },
  "TrinoParameters": {
    "Host": "string",
    "Port": integer,
    "Catalog": "string"
  },
  "BigQueryParameters": {
    "ProjectId": "string",
    "DataSetRegion": "string"
  }
}
```

`--credentials` (structure)

The credentials Amazon QuickSight that uses to connect to your underlying source. Currently, only credentials based on user name and password are supported.

CredentialPair -> (structure)

Credential pair. For more information, see `` [CredentialPair](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_CredentialPair.html) `` .

Username -> (string)

User name.

Password -> (string)

Password.

AlternateDataSourceParameters -> (list)

A set of alternate data source parameters that you want to share for these credentials. The credentials are applied in tandem with the data source parameters when you copy a data source by using a create or update request. The API operation compares the `DataSourceParameters` structure thatâs in the request with the structures in the `AlternateDataSourceParameters` allow list. If the structures are an exact match, the request is allowed to use the new data source with the existing credentials. If the `AlternateDataSourceParameters` list is null, the `DataSourceParameters` originally used with these `Credentials` is automatically allowed.

(structure)

The parameters that Amazon QuickSight uses to connect to your underlying data source. This is a variant type structure. For this structure to be valid, only one of the attributes can be non-null.

AmazonElasticsearchParameters -> (structure)

The parameters for OpenSearch.

Domain -> (string)

The OpenSearch domain.

AthenaParameters -> (structure)

The parameters for Amazon Athena.

WorkGroup -> (string)

The workgroup that Amazon Athena uses.

RoleArn -> (string)

Use the `RoleArn` structure to override an account-wide role for a specific Athena data source. For example, say an account administrator has turned off all Athena access with an account-wide role. The administrator can then use `RoleArn` to bypass the account-wide role and allow Athena access for the single Athena data source that is specified in the structure, even if the account-wide role forbidding Athena access is still active.

AuroraParameters -> (structure)

The parameters for Amazon Aurora MySQL.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

AuroraPostgreSqlParameters -> (structure)

The parameters for Amazon Aurora.

Host -> (string)

The Amazon Aurora PostgreSQL-Compatible host to connect to.

Port -> (integer)

The port that Amazon Aurora PostgreSQL is listening on.

Database -> (string)

The Amazon Aurora PostgreSQL database to connect to.

AwsIotAnalyticsParameters -> (structure)

The parameters for IoT Analytics.

DataSetName -> (string)

Dataset name.

JiraParameters -> (structure)

The parameters for Jira.

SiteBaseUrl -> (string)

The base URL of the Jira site.

MariaDbParameters -> (structure)

The parameters for MariaDB.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

MySqlParameters -> (structure)

The parameters for MySQL.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

OracleParameters -> (structure)

The parameters for Oracle.

Host -> (string)

An Oracle host.

Port -> (integer)

The port.

Database -> (string)

The database.

UseServiceName -> (boolean)

A Boolean value that indicates whether the `Database` uses a service name or an SID. If this value is left blank, the default value is `SID` . If this value is set to `false` , the value is `SID` .

PostgreSqlParameters -> (structure)

The parameters for PostgreSQL.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

PrestoParameters -> (structure)

The parameters for Presto.

Host -> (string)

Host.

Port -> (integer)

Port.

Catalog -> (string)

Catalog.

RdsParameters -> (structure)

The parameters for Amazon RDS.

InstanceId -> (string)

Instance ID.

Database -> (string)

Database.

RedshiftParameters -> (structure)

The parameters for Amazon Redshift.

Host -> (string)

Host. This field can be blank if `ClusterId` is provided.

Port -> (integer)

Port. This field can be blank if the `ClusterId` is provided.

Database -> (string)

Database.

ClusterId -> (string)

Cluster ID. This field can be blank if the `Host` and `Port` are provided.

IAMParameters -> (structure)

An optional parameter that uses IAM authentication to grant Amazon QuickSight access to your cluster. This parameter can be used instead of [DataSourceCredentials](https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DataSourceCredentials.html) .

RoleArn -> (string)

Use the `RoleArn` structure to allow Amazon QuickSight to call `redshift:GetClusterCredentials` on your cluster. The calling principal must have `iam:PassRole` access to pass the role to Amazon QuickSight. The roleâs trust policy must allow the Amazon QuickSight service principal to assume the role.

DatabaseUser -> (string)

The user whose permissions and group memberships will be used by Amazon QuickSight to access the cluster. If this user already exists in your database, Amazon QuickSight is granted the same permissions that the user has. If the user doesnât exist, set the value of `AutoCreateDatabaseUser` to `True` to create a new user with PUBLIC permissions.

DatabaseGroups -> (list)

A list of groups whose permissions will be granted to Amazon QuickSight to access the cluster. These permissions are combined with the permissions granted to Amazon QuickSight by the `DatabaseUser` . If you choose to include this parameter, the `RoleArn` must grant access to `redshift:JoinGroup` .

(string)

AutoCreateDatabaseUser -> (boolean)

Automatically creates a database user. If your database doesnât have a `DatabaseUser` , set this parameter to `True` . If there is no `DatabaseUser` , Amazon QuickSight canât connect to your cluster. The `RoleArn` that you use for this operation must grant access to `redshift:CreateClusterUser` to successfully create the user.

IdentityCenterConfiguration -> (structure)

An optional parameter that configures IAM Identity Center authentication to grant Amazon QuickSight access to your cluster.

This parameter can only be specified if your Amazon QuickSight account is configured with IAM Identity Center.

EnableIdentityPropagation -> (boolean)

A Boolean option that controls whether Trusted Identity Propagation should be used.

S3Parameters -> (structure)

The parameters for S3.

ManifestFileLocation -> (structure)

Location of the Amazon S3 manifest file. This is NULL if the manifest file was uploaded into Amazon QuickSight.

Bucket -> (string)

Amazon S3 bucket.

Key -> (string)

Amazon S3 key that identifies an object.

RoleArn -> (string)

Use the `RoleArn` structure to override an account-wide role for a specific S3 data source. For example, say an account administrator has turned off all S3 access with an account-wide role. The administrator can then use `RoleArn` to bypass the account-wide role and allow S3 access for the single S3 data source that is specified in the structure, even if the account-wide role forbidding S3 access is still active.

ServiceNowParameters -> (structure)

The parameters for ServiceNow.

SiteBaseUrl -> (string)

URL of the base site.

SnowflakeParameters -> (structure)

The parameters for Snowflake.

Host -> (string)

Host.

Database -> (string)

Database.

Warehouse -> (string)

Warehouse.

AuthenticationType -> (string)

The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.

DatabaseAccessControlRole -> (string)

The database access control role.

OAuthParameters -> (structure)

An object that contains information needed to create a data source connection between an Amazon QuickSight account and Snowflake.

TokenProviderUrl -> (string)

The token endpoint URL of the identity provider.

OAuthScope -> (string)

The OAuth scope.

IdentityProviderVpcConnectionProperties -> (structure)

VPC connection properties.

VpcConnectionArn -> (string)

The Amazon Resource Name (ARN) for the VPC connection.

IdentityProviderResourceUri -> (string)

The resource uri of the identity provider.

SparkParameters -> (structure)

The parameters for Spark.

Host -> (string)

Host.

Port -> (integer)

Port.

SqlServerParameters -> (structure)

The parameters for SQL Server.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

TeradataParameters -> (structure)

The parameters for Teradata.

Host -> (string)

Host.

Port -> (integer)

Port.

Database -> (string)

Database.

TwitterParameters -> (structure)

The parameters for Twitter.

Query -> (string)

Twitter query string.

MaxRows -> (integer)

Maximum number of rows to query Twitter.

AmazonOpenSearchParameters -> (structure)

The parameters for OpenSearch.

Domain -> (string)

The OpenSearch domain.

ExasolParameters -> (structure)

The parameters for Exasol.

Host -> (string)

The hostname or IP address of the Exasol data source.

Port -> (integer)

The port for the Exasol data source.

DatabricksParameters -> (structure)

The parameters that are required to connect to a Databricks data source.

Host -> (string)

The host name of the Databricks data source.

Port -> (integer)

The port for the Databricks data source.

SqlEndpointPath -> (string)

The HTTP path of the Databricks data source.

StarburstParameters -> (structure)

The parameters that are required to connect to a Starburst data source.

Host -> (string)

The host name of the Starburst data source.

Port -> (integer)

The port for the Starburst data source.

Catalog -> (string)

The catalog name for the Starburst data source.

ProductType -> (string)

The product type for the Starburst data source.

DatabaseAccessControlRole -> (string)

The database access control role.

AuthenticationType -> (string)

The authentication type that you want to use for your connection. This parameter accepts OAuth and non-OAuth authentication types.

OAuthParameters -> (structure)

An object that contains information needed to create a data source connection between an Amazon QuickSight account and Starburst.

TokenProviderUrl -> (string)

The token endpoint URL of the identity provider.

OAuthScope -> (string)

The OAuth scope.

IdentityProviderVpcConnectionProperties -> (structure)

VPC connection properties.

VpcConnectionArn -> (string)

The Amazon Resource Name (ARN) for the VPC connection.

IdentityProviderResourceUri -> (string)

The resource uri of the identity provider.

TrinoParameters -> (structure)

The parameters that are required to connect to a Trino data source.

Host -> (string)

The host name of the Trino data source.

Port -> (integer)

The port for the Trino data source.

Catalog -> (string)

The catalog name for the Trino data source.

BigQueryParameters -> (structure)

The parameters that are required to connect to a Google BigQuery data source.

ProjectId -> (string)

The Google Cloud Platform project ID where your datasource was created.

DataSetRegion -> (string)

The storage location where you create a Google BigQuery data source.

CopySourceArn -> (string)

The Amazon Resource Name (ARN) of a data source that has the credential pair that you want to use. When `CopySourceArn` is not null, the credential pair from the data source in the ARN is used as the credentials for the `DataSourceCredentials` structure.

SecretArn -> (string)

The Amazon Resource Name (ARN) of the secret associated with the data source in Amazon Secrets Manager.

JSON Syntax:

```
{
  "CredentialPair": {
    "Username": "string",
    "Password": "string",
    "AlternateDataSourceParameters": [
      {
        "AmazonElasticsearchParameters": {
          "Domain": "string"
        },
        "AthenaParameters": {
          "WorkGroup": "string",
          "RoleArn": "string"
        },
        "AuroraParameters": {
          "Host": "string",
          "Port": integer,
          "Database": "string"
        },
        "AuroraPostgreSqlParameters": {
          "Host": "string",
          "Port": integer,
          "Database": "string"
        },
        "AwsIotAnalyticsParameters": {
          "DataSetName": "string"
        },
        "JiraParameters": {
          "SiteBaseUrl": "string"
        },
        "MariaDbParameters": {
          "Host": "string",
          "Port": integer,
          "Database": "string"
        },
        "MySqlParameters": {
          "Host": "string",
          "Port": integer,
          "Database": "string"
        },
        "OracleParameters": {
          "Host": "string",
          "Port": integer,
          "Database": "string",
          "UseServiceName": true|false
        },
        "PostgreSqlParameters": {
          "Host": "string",
          "Port": integer,
          "Database": "string"
        },
        "PrestoParameters": {
          "Host": "string",
          "Port": integer,
          "Catalog": "string"
        },
        "RdsParameters": {
          "InstanceId": "string",
          "Database": "string"
        },
        "RedshiftParameters": {
          "Host": "string",
          "Port": integer,
          "Database": "string",
          "ClusterId": "string",
          "IAMParameters": {
            "RoleArn": "string",
            "DatabaseUser": "string",
            "DatabaseGroups": ["string", ...],
            "AutoCreateDatabaseUser": true|false
          },
          "IdentityCenterConfiguration": {
            "EnableIdentityPropagation": true|false
          }
        },
        "S3Parameters": {
          "ManifestFileLocation": {
            "Bucket": "string",
            "Key": "string"
          },
          "RoleArn": "string"
        },
        "ServiceNowParameters": {
          "SiteBaseUrl": "string"
        },
        "SnowflakeParameters": {
          "Host": "string",
          "Database": "string",
          "Warehouse": "string",
          "AuthenticationType": "PASSWORD"|"TOKEN"|"X509",
          "DatabaseAccessControlRole": "string",
          "OAuthParameters": {
            "TokenProviderUrl": "string",
            "OAuthScope": "string",
            "IdentityProviderVpcConnectionProperties": {
              "VpcConnectionArn": "string"
            },
            "IdentityProviderResourceUri": "string"
          }
        },
        "SparkParameters": {
          "Host": "string",
          "Port": integer
        },
        "SqlServerParameters": {
          "Host": "string",
          "Port": integer,
          "Database": "string"
        },
        "TeradataParameters": {
          "Host": "string",
          "Port": integer,
          "Database": "string"
        },
        "TwitterParameters": {
          "Query": "string",
          "MaxRows": integer
        },
        "AmazonOpenSearchParameters": {
          "Domain": "string"
        },
        "ExasolParameters": {
          "Host": "string",
          "Port": integer
        },
        "DatabricksParameters": {
          "Host": "string",
          "Port": integer,
          "SqlEndpointPath": "string"
        },
        "StarburstParameters": {
          "Host": "string",
          "Port": integer,
          "Catalog": "string",
          "ProductType": "GALAXY"|"ENTERPRISE",
          "DatabaseAccessControlRole": "string",
          "AuthenticationType": "PASSWORD"|"TOKEN"|"X509",
          "OAuthParameters": {
            "TokenProviderUrl": "string",
            "OAuthScope": "string",
            "IdentityProviderVpcConnectionProperties": {
              "VpcConnectionArn": "string"
            },
            "IdentityProviderResourceUri": "string"
          }
        },
        "TrinoParameters": {
          "Host": "string",
          "Port": integer,
          "Catalog": "string"
        },
        "BigQueryParameters": {
          "ProjectId": "string",
          "DataSetRegion": "string"
        }
      }
      ...
    ]
  },
  "CopySourceArn": "string",
  "SecretArn": "string"
}
```

`--permissions` (list)

A list of resource permissions on the data source.

(structure)

Permission for the resource.

Principal -> (string)

The Amazon Resource Name (ARN) of the principal. This can be one of the following:

- The ARN of an Amazon QuickSight user or group associated with a data source or dataset. (This is common.)
- The ARN of an Amazon QuickSight user, group, or namespace associated with an analysis, dashboard, template, or theme. (This is common.)
- The ARN of an Amazon Web Services account root: This is an IAM ARN rather than a QuickSight ARN. Use this option only to share resources (templates) across Amazon Web Services accounts. (This is less common.)

Actions -> (list)

The IAM action to grant or revoke permissions on.

(string)

Shorthand Syntax:

```
Principal=string,Actions=string,string ...
```

JSON Syntax:

```
[
  {
    "Principal": "string",
    "Actions": ["string", ...]
  }
  ...
]
```

`--vpc-connection-properties` (structure)

Use this parameter only when you want Amazon QuickSight to use a VPC connection when connecting to your underlying source.

VpcConnectionArn -> (string)

The Amazon Resource Name (ARN) for the VPC connection.

Shorthand Syntax:

```
VpcConnectionArn=string
```

JSON Syntax:

```
{
  "VpcConnectionArn": "string"
}
```

`--ssl-properties` (structure)

Secure Socket Layer (SSL) properties that apply when Amazon QuickSight connects to your underlying source.

DisableSsl -> (boolean)

A Boolean option to control whether SSL should be disabled.

Shorthand Syntax:

```
DisableSsl=boolean
```

JSON Syntax:

```
{
  "DisableSsl": true|false
}
```

`--tags` (list)

Contains a map of the key-value pairs for the resource tag or tags assigned to the data source.

(structure)

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key -> (string)

Tag key.

Value -> (string)

Tag value.

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

`--folder-arns` (list)

When you create the data source, Amazon QuickSight adds the data source to these folders.

(string)

Syntax:

```
"string" "string" ...
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

Arn -> (string)

The Amazon Resource Name (ARN) of the data source.

DataSourceId -> (string)

The ID of the data source. This ID is unique per Amazon Web Services Region for each Amazon Web Services account.

CreationStatus -> (string)

The status of creating the data source.

RequestId -> (string)

The Amazon Web Services request ID for this operation.

Status -> (integer)

The HTTP status of the request.