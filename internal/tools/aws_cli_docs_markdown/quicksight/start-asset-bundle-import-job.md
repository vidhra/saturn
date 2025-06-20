# start-asset-bundle-import-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/start-asset-bundle-import-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/start-asset-bundle-import-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [quicksight](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/quicksight/index.html#cli-aws-quicksight) ]

# start-asset-bundle-import-job

## Description

Starts an Asset Bundle import job.

An Asset Bundle import job imports specified Amazon QuickSight assets into an Amazon QuickSight account. You can also choose to import a naming prefix and specified configuration overrides. The assets that are contained in the bundle file that you provide are used to create or update a new or existing asset in your Amazon QuickSight account. Each Amazon QuickSight account can run up to 5 import jobs concurrently.

The API caller must have the necessary `"create"` , `"describe"` , and `"update"` permissions in their IAM role to access each resource type that is contained in the bundle file before the resources can be imported.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/quicksight-2018-04-01/StartAssetBundleImportJob)

## Synopsis

```
start-asset-bundle-import-job
--aws-account-id <value>
--asset-bundle-import-job-id <value>
[--asset-bundle-import-source <value>]
[--override-parameters <value>]
[--failure-action <value>]
[--override-permissions <value>]
[--override-tags <value>]
[--override-validation-strategy <value>]
[--asset-bundle-import-source-bytes <value>]
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

The ID of the Amazon Web Services account to import assets into.

`--asset-bundle-import-job-id` (string)

The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.

`--asset-bundle-import-source` (structure)

The source of the asset bundle zip file that contains the data that you want to import. The file must be in `QUICKSIGHT_JSON` format.

To specify a local file use `--asset-bundle-import-source-bytes` instead.

Body -> (blob)

The bytes of the base64 encoded asset bundle import zip file. This file canât exceed 20 MB. If the size of the file that you want to upload is more than 20 MB, add the file to your Amazon S3 bucket and use `S3Uri` of the file for this operation.

If you are calling the API operations from the Amazon Web Services SDK for Java, JavaScript, Python, or PHP, the SDK encodes base64 automatically to allow the direct setting of the zip fileâs bytes. If you are using an SDK for a different language or receiving related errors, try to base64 encode your data.

S3Uri -> (string)

The Amazon S3 URI for an asset bundle import file that exists in an Amazon S3 bucket that the caller has read access to. The file must be a zip format file and canât exceed 1 GB.

Shorthand Syntax:

```
Body=blob,S3Uri=string
```

JSON Syntax:

```
{
  "Body": blob,
  "S3Uri": "string"
}
```

`--override-parameters` (structure)

Optional overrides that are applied to the resource configuration before import.

ResourceIdOverrideConfiguration -> (structure)

An optional structure that configures resource ID overrides to be applied within the import job.

PrefixForAllResources -> (string)

An option to request a CloudFormation variable for a prefix to be prepended to each resourceâs ID before import. The prefix is only added to the asset IDs and does not change the name of the asset.

VPCConnections -> (list)

A list of overrides for any `VPCConnection` resources that are present in the asset bundle that is imported.

(structure)

The override parameters for a single VPC connection that is imported.

VPCConnectionId -> (string)

The ID of the VPC Connection to apply overrides to.

Name -> (string)

A new name for the VPC connection.

SubnetIds -> (list)

A list of new subnet IDs for the VPC connection you are importing. This field is required if you are importing the VPC connection from another Amazon Web Services account or Region.

(string)

SecurityGroupIds -> (list)

A new security group ID for the VPC connection you are importing. This field is required if you are importing the VPC connection from another Amazon Web Services account or Region.

(string)

DnsResolvers -> (list)

An optional override of DNS resolvers to be used by the VPC connection.

(string)

RoleArn -> (string)

An optional override of the role ARN to be used by the VPC connection.

RefreshSchedules -> (list)

A list of overrides for any `RefreshSchedule` resources that are present in the asset bundle that is imported.

(structure)

A list of overrides for a specific `RefreshsSchedule` resource that is present in the asset bundle that is imported.

DataSetId -> (string)

A partial identifier for the specific `RefreshSchedule` resource that is being overridden. This structure is used together with the `ScheduleID` structure.

ScheduleId -> (string)

A partial identifier for the specific `RefreshSchedule` resource being overridden. This structure is used together with the `DataSetId` structure.

StartAfterDateTime -> (timestamp)

An override for the `StartAfterDateTime` of a `RefreshSchedule` . Make sure that the `StartAfterDateTime` is set to a time that takes place in the future.

DataSources -> (list)

A list of overrides for any `DataSource` resources that are present in the asset bundle that is imported.

(structure)

The override parameters for a single data source that is being imported.

DataSourceId -> (string)

The ID of the data source to apply overrides to.

Name -> (string)

A new name for the data source.

DataSourceParameters -> (structure)

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

VpcConnectionProperties -> (structure)

VPC connection properties.

VpcConnectionArn -> (string)

The Amazon Resource Name (ARN) for the VPC connection.

SslProperties -> (structure)

Secure Socket Layer (SSL) properties that apply when Amazon QuickSight connects to your underlying data source.

DisableSsl -> (boolean)

A Boolean option to control whether SSL should be disabled.

Credentials -> (structure)

An optional structure that provides the credentials to be used to create the imported data source.

CredentialPair -> (structure)

A username and password credential pair to be used to create the imported data source. Keep this field blank if you are using a Secrets Manager secret to provide credentials.

Username -> (string)

The username for the data source connection.

Password -> (string)

The password for the data source connection.

SecretArn -> (string)

The ARN of the Secrets Manager secret thatâs used to create the imported data source. Keep this field blank, unless you are using a secret in place of a credential pair.

DataSets -> (list)

A list of overrides for any `DataSet` resources that are present in the asset bundle that is imported.

(structure)

The override parameters for a single dataset that is being imported.

DataSetId -> (string)

The ID of the dataset to apply overrides to.

Name -> (string)

A new name for the dataset.

DataSetRefreshProperties -> (structure)

The refresh properties of a dataset.

RefreshConfiguration -> (structure)

The refresh configuration for a dataset.

IncrementalRefresh -> (structure)

The incremental refresh for the dataset.

LookbackWindow -> (structure)

The lookback window setup for an incremental refresh configuration.

ColumnName -> (string)

The name of the lookback window column.

Size -> (long)

The lookback window column size.

SizeUnit -> (string)

The size unit that is used for the lookback window column. Valid values for this structure are `HOUR` , `DAY` , and `WEEK` .

FailureConfiguration -> (structure)

The failure configuration for a dataset.

EmailAlert -> (structure)

The email alert configuration for a dataset refresh failure.

AlertStatus -> (string)

The status value that determines if email alerts are sent.

Themes -> (list)

A list of overrides for any `Theme` resources that are present in the asset bundle that is imported.

(structure)

The override parameters for a single theme that is imported.

ThemeId -> (string)

The ID of the theme to apply overrides to.

Name -> (string)

A new name for the theme.

Analyses -> (list)

A list of overrides for any `Analysis` resources that are present in the asset bundle that is imported.

(structure)

The override parameters for a single analysis that is being imported.

AnalysisId -> (string)

The ID of the analysis that you ant to apply overrides to.

Name -> (string)

A new name for the analysis.

Dashboards -> (list)

A list of overrides for any `Dashboard` resources that are present in the asset bundle that is imported.

(structure)

The override parameters for a single dashboard that is being imported.

DashboardId -> (string)

The ID of the dashboard that you want to apply overrides to.

Name -> (string)

A new name for the dashboard.

Folders -> (list)

A list of overrides for any `Folder` resources that are present in the asset bundle that is imported.

(structure)

The override parameters for a single folder that is being imported.

FolderId -> (string)

The ID of the folder that you want to apply overrides to.

Name -> (string)

A new name for the folder.

ParentFolderArn -> (string)

A new parent folder arn. This change can only be applied if the import creates a brand new folder. Existing folders cannot be moved.

JSON Syntax:

```
{
  "ResourceIdOverrideConfiguration": {
    "PrefixForAllResources": "string"
  },
  "VPCConnections": [
    {
      "VPCConnectionId": "string",
      "Name": "string",
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...],
      "DnsResolvers": ["string", ...],
      "RoleArn": "string"
    }
    ...
  ],
  "RefreshSchedules": [
    {
      "DataSetId": "string",
      "ScheduleId": "string",
      "StartAfterDateTime": timestamp
    }
    ...
  ],
  "DataSources": [
    {
      "DataSourceId": "string",
      "Name": "string",
      "DataSourceParameters": {
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
      },
      "VpcConnectionProperties": {
        "VpcConnectionArn": "string"
      },
      "SslProperties": {
        "DisableSsl": true|false
      },
      "Credentials": {
        "CredentialPair": {
          "Username": "string",
          "Password": "string"
        },
        "SecretArn": "string"
      }
    }
    ...
  ],
  "DataSets": [
    {
      "DataSetId": "string",
      "Name": "string",
      "DataSetRefreshProperties": {
        "RefreshConfiguration": {
          "IncrementalRefresh": {
            "LookbackWindow": {
              "ColumnName": "string",
              "Size": long,
              "SizeUnit": "HOUR"|"DAY"|"WEEK"
            }
          }
        },
        "FailureConfiguration": {
          "EmailAlert": {
            "AlertStatus": "ENABLED"|"DISABLED"
          }
        }
      }
    }
    ...
  ],
  "Themes": [
    {
      "ThemeId": "string",
      "Name": "string"
    }
    ...
  ],
  "Analyses": [
    {
      "AnalysisId": "string",
      "Name": "string"
    }
    ...
  ],
  "Dashboards": [
    {
      "DashboardId": "string",
      "Name": "string"
    }
    ...
  ],
  "Folders": [
    {
      "FolderId": "string",
      "Name": "string",
      "ParentFolderArn": "string"
    }
    ...
  ]
}
```

`--failure-action` (string)

The failure action for the import job.

If you choose `ROLLBACK` , failed import jobs will attempt to undo any asset changes caused by the failed job.

If you choose `DO_NOTHING` , failed import jobs will not attempt to roll back any asset changes caused by the failed job, possibly keeping the Amazon QuickSight account in an inconsistent state.

Possible values:

- `DO_NOTHING`
- `ROLLBACK`

`--override-permissions` (structure)

Optional permission overrides that are applied to the resource configuration before import.

DataSources -> (list)

A list of permissions overrides for any `DataSource` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of permissions to be applied to a list of data source IDs.

DataSourceIds -> (list)

A list of data source IDs that you want to apply overrides to. You can use `*` to override all data sources in this asset bundle.

(string)

Permissions -> (structure)

A list of permissions for the data source that you want to apply overrides to.

Principals -> (list)

A list of principals to grant permissions on.

(string)

Actions -> (list)

A list of IAM actions to grant permissions on.

(string)

DataSets -> (list)

A list of permissions overrides for any `DataSet` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of permissions to be applied to a list of dataset IDs.

DataSetIds -> (list)

A list of dataset IDs that you want to apply overrides to. You can use `*` to override all datasets in this asset bundle.

(string)

Permissions -> (structure)

A list of permissions for the datasets that you want to apply overrides to.

Principals -> (list)

A list of principals to grant permissions on.

(string)

Actions -> (list)

A list of IAM actions to grant permissions on.

(string)

Themes -> (list)

A list of permissions overrides for any `Theme` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of permissions to be applied to a list of theme IDs.

ThemeIds -> (list)

A list of theme IDs that you want to apply overrides to. You can use `*` to override all themes in this asset bundle.

(string)

Permissions -> (structure)

A list of permissions for the themes that you want to apply overrides to.

Principals -> (list)

A list of principals to grant permissions on.

(string)

Actions -> (list)

A list of IAM actions to grant permissions on.

(string)

Analyses -> (list)

A list of permissions overrides for any `Analysis` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of permissions to be applied to a list of analysis IDs.

AnalysisIds -> (list)

A list of analysis IDs that you want to apply overrides to. You can use `*` to override all analyses in this asset bundle.

(string)

Permissions -> (structure)

A list of permissions for the analyses that you want to apply overrides to.

Principals -> (list)

A list of principals to grant permissions on.

(string)

Actions -> (list)

A list of IAM actions to grant permissions on.

(string)

Dashboards -> (list)

A list of permissions overrides for any `Dashboard` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of permissions to be applied to a list of dashboard IDs.

DashboardIds -> (list)

A list of dashboard IDs that you want to apply overrides to. You can use `*` to override all dashboards in this asset bundle.

(string)

Permissions -> (structure)

A list of permissions for the dashboards that you want to apply overrides to.

Principals -> (list)

A list of principals to grant permissions on.

(string)

Actions -> (list)

A list of IAM actions to grant permissions on.

(string)

LinkSharingConfiguration -> (structure)

A structure that contains the link sharing configurations that you want to apply overrides to.

Permissions -> (structure)

A list of link sharing permissions for the dashboards that you want to apply overrides to.

Principals -> (list)

A list of principals to grant permissions on.

(string)

Actions -> (list)

A list of IAM actions to grant permissions on.

(string)

Folders -> (list)

A list of permissions for the folders that you want to apply overrides to.

(structure)

An object that contains a list of permissions to be applied to a list of folder IDs.

FolderIds -> (list)

A list of folder IDs that you want to apply overrides to. You can use `*` to override all folders in this asset bundle.

(string)

Permissions -> (structure)

A structure that contains the permissions for the resource that you want to override in an asset bundle import job.

Principals -> (list)

A list of principals to grant permissions on.

(string)

Actions -> (list)

A list of IAM actions to grant permissions on.

(string)

JSON Syntax:

```
{
  "DataSources": [
    {
      "DataSourceIds": ["string", ...],
      "Permissions": {
        "Principals": ["string", ...],
        "Actions": ["string", ...]
      }
    }
    ...
  ],
  "DataSets": [
    {
      "DataSetIds": ["string", ...],
      "Permissions": {
        "Principals": ["string", ...],
        "Actions": ["string", ...]
      }
    }
    ...
  ],
  "Themes": [
    {
      "ThemeIds": ["string", ...],
      "Permissions": {
        "Principals": ["string", ...],
        "Actions": ["string", ...]
      }
    }
    ...
  ],
  "Analyses": [
    {
      "AnalysisIds": ["string", ...],
      "Permissions": {
        "Principals": ["string", ...],
        "Actions": ["string", ...]
      }
    }
    ...
  ],
  "Dashboards": [
    {
      "DashboardIds": ["string", ...],
      "Permissions": {
        "Principals": ["string", ...],
        "Actions": ["string", ...]
      },
      "LinkSharingConfiguration": {
        "Permissions": {
          "Principals": ["string", ...],
          "Actions": ["string", ...]
        }
      }
    }
    ...
  ],
  "Folders": [
    {
      "FolderIds": ["string", ...],
      "Permissions": {
        "Principals": ["string", ...],
        "Actions": ["string", ...]
      }
    }
    ...
  ]
}
```

`--override-tags` (structure)

Optional tag overrides that are applied to the resource configuration before import.

VPCConnections -> (list)

A list of tag overrides for any `VPCConnection` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of tags to be assigned to a list of VPC connection IDs.

VPCConnectionIds -> (list)

A list of VPC connection IDs that you want to apply overrides to. You can use `*` to override all VPC connections in this asset bundle.

(string)

Tags -> (list)

A list of tags for the VPC connections that you want to apply overrides to.

(structure)

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key -> (string)

Tag key.

Value -> (string)

Tag value.

DataSources -> (list)

A list of tag overrides for any `DataSource` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of tags to be assigned to a list of data source IDs.

DataSourceIds -> (list)

A list of data source IDs that you want to apply overrides to. You can use `*` to override all data sources in this asset bundle.

(string)

Tags -> (list)

A list of tags for the data source that you want to apply overrides to.

(structure)

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key -> (string)

Tag key.

Value -> (string)

Tag value.

DataSets -> (list)

A list of tag overrides for any `DataSet` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of tags to be assigned to a list of dataset IDs.

DataSetIds -> (list)

A list of dataset IDs that you want to apply overrides to. You can use `*` to override all datasets in this asset bundle.

(string)

Tags -> (list)

A list of tags for the datasets that you want to apply overrides to.

(structure)

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key -> (string)

Tag key.

Value -> (string)

Tag value.

Themes -> (list)

A list of tag overrides for any `Theme` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of tags to be assigned to a list of theme IDs.

ThemeIds -> (list)

A list of theme IDs that you want to apply overrides to. You can use `*` to override all themes in this asset bundle.

(string)

Tags -> (list)

A list of tags for the themes that you want to apply overrides to.

(structure)

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key -> (string)

Tag key.

Value -> (string)

Tag value.

Analyses -> (list)

A list of tag overrides for any `Analysis` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of tags to be assigned to a list of analysis IDs.

AnalysisIds -> (list)

A list of analysis IDs that you want to apply overrides to. You can use `*` to override all analyses in this asset bundle.

(string)

Tags -> (list)

A list of tags for the analyses that you want to apply overrides to.

(structure)

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key -> (string)

Tag key.

Value -> (string)

Tag value.

Dashboards -> (list)

A list of tag overrides for any `Dashboard` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of tags to be assigned to a list of dashboard IDs.

DashboardIds -> (list)

A list of dashboard IDs that you want to apply overrides to. You can use `*` to override all dashboards in this asset bundle.

(string)

Tags -> (list)

A list of tags for the dashboards that you want to apply overrides to.

(structure)

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key -> (string)

Tag key.

Value -> (string)

Tag value.

Folders -> (list)

A list of tag overrides for any `Folder` resources that are present in the asset bundle that is imported.

(structure)

An object that contains a list of tags to be assigned to a list of folder IDs.

FolderIds -> (list)

A list of folder IDs that you want to apply overrides to. You can use `*` to override all folders in this asset bundle.

(string)

Tags -> (list)

A list of tags for the folders that you want to apply overrides to.

(structure)

The key or keys of the key-value pairs for the resource tag or tags assigned to the resource.

Key -> (string)

Tag key.

Value -> (string)

Tag value.

JSON Syntax:

```
{
  "VPCConnections": [
    {
      "VPCConnectionIds": ["string", ...],
      "Tags": [
        {
          "Key": "string",
          "Value": "string"
        }
        ...
      ]
    }
    ...
  ],
  "DataSources": [
    {
      "DataSourceIds": ["string", ...],
      "Tags": [
        {
          "Key": "string",
          "Value": "string"
        }
        ...
      ]
    }
    ...
  ],
  "DataSets": [
    {
      "DataSetIds": ["string", ...],
      "Tags": [
        {
          "Key": "string",
          "Value": "string"
        }
        ...
      ]
    }
    ...
  ],
  "Themes": [
    {
      "ThemeIds": ["string", ...],
      "Tags": [
        {
          "Key": "string",
          "Value": "string"
        }
        ...
      ]
    }
    ...
  ],
  "Analyses": [
    {
      "AnalysisIds": ["string", ...],
      "Tags": [
        {
          "Key": "string",
          "Value": "string"
        }
        ...
      ]
    }
    ...
  ],
  "Dashboards": [
    {
      "DashboardIds": ["string", ...],
      "Tags": [
        {
          "Key": "string",
          "Value": "string"
        }
        ...
      ]
    }
    ...
  ],
  "Folders": [
    {
      "FolderIds": ["string", ...],
      "Tags": [
        {
          "Key": "string",
          "Value": "string"
        }
        ...
      ]
    }
    ...
  ]
}
```

`--override-validation-strategy` (structure)

An optional validation strategy override for all analyses and dashboards that is applied to the resource configuration before import.

StrictModeForAllResources -> (boolean)

A Boolean value that indicates whether to import all analyses and dashboards under strict or lenient mode.

Shorthand Syntax:

```
StrictModeForAllResources=boolean
```

JSON Syntax:

```
{
  "StrictModeForAllResources": true|false
}
```

`--asset-bundle-import-source-bytes` (blob)

The content of the asset bundle to be uploaded. To specify the content of a local file use the fileb:// prefix. Example: fileb://asset-bundle.zip

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

The Amazon Resource Name (ARN) for the import job.

AssetBundleImportJobId -> (string)

The ID of the job. This ID is unique while the job is running. After the job is completed, you can reuse this ID for another job.

RequestId -> (string)

The Amazon Web Services response ID for this operation.

Status -> (integer)

The HTTP status of the response.