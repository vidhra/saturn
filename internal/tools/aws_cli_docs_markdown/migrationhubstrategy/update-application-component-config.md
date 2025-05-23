# update-application-component-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/update-application-component-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/update-application-component-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [migrationhubstrategy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/index.html#cli-aws-migrationhubstrategy) ]

# update-application-component-config

## Description

Updates the configuration of an application component.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/migrationhubstrategy-2020-02-19/UpdateApplicationComponentConfig)

## Synopsis

```
update-application-component-config
[--app-type <value>]
--application-component-id <value>
[--configure-only | --no-configure-only]
[--inclusion-status <value>]
[--secrets-manager-key <value>]
[--source-code-list <value>]
[--strategy-option <value>]
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

`--app-type` (string)

The type of known component.

Possible values:

- `DotNetFramework`
- `Java`
- `SQLServer`
- `IIS`
- `Oracle`
- `Other`
- `Tomcat`
- `JBoss`
- `Spring`
- `Mongo DB`
- `DB2`
- `Maria DB`
- `MySQL`
- `Sybase`
- `PostgreSQLServer`
- `Cassandra`
- `IBM WebSphere`
- `Oracle WebLogic`
- `Visual Basic`
- `Unknown`
- `DotnetCore`
- `Dotnet`

`--application-component-id` (string)

The ID of the application component. The ID is unique within an AWS account.

`--configure-only` | `--no-configure-only` (boolean)

Update the configuration request of an application component. If it is set to true, the source code and/or database credentials are updated. If it is set to false, the source code and/or database credentials are updated and an analysis is initiated.

`--inclusion-status` (string)

Indicates whether the application component has been included for server recommendation or not.

Possible values:

- `excludeFromAssessment`
- `includeInAssessment`

`--secrets-manager-key` (string)

Database credentials.

`--source-code-list` (list)

The list of source code configurations to update for the application component.

(structure)

Object containing source code information that is linked to an application component.

location -> (string)

The repository name for the source code.

projectName -> (string)

The name of the project.

sourceVersion -> (string)

The branch of the source code.

versionControl -> (string)

The type of repository to use for the source code.

Shorthand Syntax:

```
location=string,projectName=string,sourceVersion=string,versionControl=string ...
```

JSON Syntax:

```
[
  {
    "location": "string",
    "projectName": "string",
    "sourceVersion": "string",
    "versionControl": "GITHUB"|"GITHUB_ENTERPRISE"|"AZURE_DEVOPS_GIT"
  }
  ...
]
```

`--strategy-option` (structure)

The preferred strategy options for the application component. Use values from the  GetApplicationComponentStrategies response.

isPreferred -> (boolean)

Indicates if a specific strategy is preferred for the application component.

strategy -> (string)

Type of transformation. For example, Rehost, Replatform, and so on.

targetDestination -> (string)

Destination information about where the application component can migrate to. For example, `EC2` , `ECS` , and so on.

toolName -> (string)

The name of the tool that can be used to transform an application component using this strategy.

Shorthand Syntax:

```
isPreferred=boolean,strategy=string,targetDestination=string,toolName=string
```

JSON Syntax:

```
{
  "isPreferred": true|false,
  "strategy": "Rehost"|"Retirement"|"Refactor"|"Replatform"|"Retain"|"Relocate"|"Repurchase",
  "targetDestination": "None specified"|"AWS Elastic BeanStalk"|"AWS Fargate"|"Amazon Elastic Cloud Compute (EC2)"|"Amazon Elastic Container Service (ECS)"|"Amazon Elastic Kubernetes Service (EKS)"|"Aurora MySQL"|"Aurora PostgreSQL"|"Amazon Relational Database Service on MySQL"|"Amazon Relational Database Service on PostgreSQL"|"Amazon DocumentDB"|"Amazon DynamoDB"|"Amazon Relational Database Service"|"Babelfish for Aurora PostgreSQL",
  "toolName": "App2Container"|"Porting Assistant For .NET"|"End of Support Migration"|"Windows Web Application Migration Assistant"|"Application Migration Service"|"Strategy Recommendation Support"|"In Place Operating System Upgrade"|"Schema Conversion Tool"|"Database Migration Service"|"Native SQL Server Backup/Restore"
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