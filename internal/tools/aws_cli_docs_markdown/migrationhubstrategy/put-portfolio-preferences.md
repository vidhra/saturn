# put-portfolio-preferencesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/put-portfolio-preferences.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/put-portfolio-preferences.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [migrationhubstrategy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/index.html#cli-aws-migrationhubstrategy) ]

# put-portfolio-preferences

## Description

Saves the specified migration and modernization preferences.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/migrationhubstrategy-2020-02-19/PutPortfolioPreferences)

## Synopsis

```
put-portfolio-preferences
[--application-mode <value>]
[--application-preferences <value>]
[--database-preferences <value>]
[--prioritize-business-goals <value>]
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

`--application-mode` (string)

The classification for application component types.

Possible values:

- `ALL`
- `KNOWN`
- `UNKNOWN`

`--application-preferences` (structure)

The transformation preferences for non-database applications.

managementPreference -> (tagged union structure)

Application preferences that you specify to prefer managed environment.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `awsManagedResources`, `noPreference`, `selfManageResources`.

awsManagedResources -> (structure)

Indicates interest in solutions that are managed by AWS.

targetDestination -> (list)

The choice of application destination that you specify.

(string)

noPreference -> (structure)

No specific preference.

targetDestination -> (list)

The choice of application destination that you specify.

(string)

selfManageResources -> (structure)

Indicates interest in managing your own resources on AWS.

targetDestination -> (list)

Self-managed resources target destination.

(string)

JSON Syntax:

```
{
  "managementPreference": {
    "awsManagedResources": {
      "targetDestination": ["None specified"|"AWS Elastic BeanStalk"|"AWS Fargate", ...]
    },
    "noPreference": {
      "targetDestination": ["None specified"|"AWS Elastic BeanStalk"|"AWS Fargate"|"Amazon Elastic Cloud Compute (EC2)"|"Amazon Elastic Container Service (ECS)"|"Amazon Elastic Kubernetes Service (EKS)", ...]
    },
    "selfManageResources": {
      "targetDestination": ["None specified"|"Amazon Elastic Cloud Compute (EC2)"|"Amazon Elastic Container Service (ECS)"|"Amazon Elastic Kubernetes Service (EKS)", ...]
    }
  }
}
```

`--database-preferences` (structure)

The transformation preferences for database applications.

databaseManagementPreference -> (string)

Specifies whether youâre interested in self-managed databases or databases managed by AWS.

databaseMigrationPreference -> (tagged union structure)

Specifies your preferred migration path.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `heterogeneous`, `homogeneous`, `noPreference`.

heterogeneous -> (structure)

Indicates whether you are interested in moving from one type of database to another. For example, from SQL Server to Amazon Aurora MySQL-Compatible Edition.

targetDatabaseEngine -> (list)

The target database engine for heterogeneous database migration preference.

(string)

homogeneous -> (structure)

Indicates whether you are interested in moving to the same type of database into AWS. For example, from SQL Server in your environment to SQL Server on AWS.

targetDatabaseEngine -> (list)

The target database engine for homogeneous database migration preferences.

(string)

noPreference -> (structure)

Indicated that you do not prefer heterogeneous or homogeneous.

targetDatabaseEngine -> (list)

The target database engine for database migration preference that you specify.

(string)

JSON Syntax:

```
{
  "databaseManagementPreference": "AWS-managed"|"Self-manage"|"No preference",
  "databaseMigrationPreference": {
    "heterogeneous": {
      "targetDatabaseEngine": ["None specified"|"Amazon Aurora"|"AWS PostgreSQL"|"MySQL"|"Microsoft SQL Server"|"Oracle Database"|"MariaDB"|"SAP"|"Db2 LUW"|"MongoDB", ...]
    },
    "homogeneous": {
      "targetDatabaseEngine": ["None specified", ...]
    },
    "noPreference": {
      "targetDatabaseEngine": ["None specified"|"Amazon Aurora"|"AWS PostgreSQL"|"MySQL"|"Microsoft SQL Server"|"Oracle Database"|"MariaDB"|"SAP"|"Db2 LUW"|"MongoDB", ...]
    }
  }
}
```

`--prioritize-business-goals` (structure)

The rank of the business goals based on priority.

businessGoals -> (structure)

Rank of business goals based on priority.

licenseCostReduction -> (integer)

Business goal to reduce license costs.

modernizeInfrastructureWithCloudNativeTechnologies -> (integer)

Business goal to modernize infrastructure by moving to cloud native technologies.

reduceOperationalOverheadWithManagedServices -> (integer)

Business goal to reduce the operational overhead on the team by moving into managed services.

speedOfMigration -> (integer)

Business goal to achieve migration at a fast pace.

Shorthand Syntax:

```
businessGoals={licenseCostReduction=integer,modernizeInfrastructureWithCloudNativeTechnologies=integer,reduceOperationalOverheadWithManagedServices=integer,speedOfMigration=integer}
```

JSON Syntax:

```
{
  "businessGoals": {
    "licenseCostReduction": integer,
    "modernizeInfrastructureWithCloudNativeTechnologies": integer,
    "reduceOperationalOverheadWithManagedServices": integer,
    "speedOfMigration": integer
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

None