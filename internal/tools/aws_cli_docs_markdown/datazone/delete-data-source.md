# delete-data-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/delete-data-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/delete-data-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datazone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/index.html#cli-aws-datazone) ]

# delete-data-source

## Description

Deletes a data source in Amazon DataZone.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/DeleteDataSource)

## Synopsis

```
delete-data-source
[--client-token <value>]
--domain-identifier <value>
--identifier <value>
[--retain-permissions-on-revoke-failure | --no-retain-permissions-on-revoke-failure]
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

`--client-token` (string)

A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.

`--domain-identifier` (string)

The ID of the Amazon DataZone domain in which the data source is deleted.

`--identifier` (string)

The identifier of the data source that is deleted.

`--retain-permissions-on-revoke-failure` | `--no-retain-permissions-on-revoke-failure` (boolean)

Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.

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

assetFormsOutput -> (list)

The asset data forms associated with this data source.

(structure)

The details of a metadata form.

content -> (string)

The content of the metadata form.

formName -> (string)

The name of the metadata form.

typeName -> (string)

The name of the metadata form type.

typeRevision -> (string)

The revision of the metadata form type.

configuration -> (tagged union structure)

The configuration of the data source that is deleted.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `glueRunConfiguration`, `redshiftRunConfiguration`, `sageMakerRunConfiguration`.

glueRunConfiguration -> (structure)

The configuration of the Amazon Web Services Glue data source.

accountId -> (string)

The Amazon Web Services account ID included in the configuration details of the Amazon Web Services Glue data source.

autoImportDataQualityResult -> (boolean)

Specifies whether to automatically import data quality metrics as part of the data source run.

catalogName -> (string)

The catalog name in the Amazon Web Services Glue run configuration.

dataAccessRole -> (string)

The data access role included in the configuration details of the Amazon Web Services Glue data source.

region -> (string)

The Amazon Web Services region included in the configuration details of the Amazon Web Services Glue data source.

relationalFilterConfigurations -> (list)

The relational filter configurations included in the configuration details of the Amazon Web Services Glue data source.

(structure)

The relational filter configuration for the data source.

databaseName -> (string)

The database name specified in the relational filter configuration for the data source.

filterExpressions -> (list)

The filter expressions specified in the relational filter configuration for the data source.

(structure)

A filter expression in Amazon DataZone.

expression -> (string)

The search filter expression.

type -> (string)

The search filter explresison type.

schemaName -> (string)

The schema name specified in the relational filter configuration for the data source.

redshiftRunConfiguration -> (structure)

The configuration of the Amazon Redshift data source.

accountId -> (string)

The ID of the Amazon Web Services account included in the configuration details of the Amazon Redshift data source.

dataAccessRole -> (string)

The data access role included in the configuration details of the Amazon Redshift data source.

redshiftCredentialConfiguration -> (structure)

The details of the credentials required to access an Amazon Redshift cluster.

secretManagerArn -> (string)

The ARN of a secret manager for an Amazon Redshift cluster.

redshiftStorage -> (tagged union structure)

The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `redshiftClusterSource`, `redshiftServerlessSource`.

redshiftClusterSource -> (structure)

The details of the Amazon Redshift cluster source.

clusterName -> (string)

The name of an Amazon Redshift cluster.

redshiftServerlessSource -> (structure)

The details of the Amazon Redshift Serverless workgroup source.

workgroupName -> (string)

The name of the Amazon Redshift Serverless workgroup.

region -> (string)

The Amazon Web Services region included in the configuration details of the Amazon Redshift data source.

relationalFilterConfigurations -> (list)

The relational filger configurations included in the configuration details of the Amazon Redshift data source.

(structure)

The relational filter configuration for the data source.

databaseName -> (string)

The database name specified in the relational filter configuration for the data source.

filterExpressions -> (list)

The filter expressions specified in the relational filter configuration for the data source.

(structure)

A filter expression in Amazon DataZone.

expression -> (string)

The search filter expression.

type -> (string)

The search filter explresison type.

schemaName -> (string)

The schema name specified in the relational filter configuration for the data source.

sageMakerRunConfiguration -> (structure)

The Amazon SageMaker run configuration.

accountId -> (string)

The Amazon SageMaker account ID.

region -> (string)

The Amazon SageMaker Region.

trackingAssets -> (map)

The tracking assets of the Amazon SageMaker.

key -> (string)

value -> (list)

(string)

connectionId -> (string)

The ID of the connection that is deleted.

createdAt -> (timestamp)

The timestamp of when this data source was created.

description -> (string)

The description of the data source that is deleted.

domainId -> (string)

The ID of the Amazon DataZone domain in which the data source is deleted.

enableSetting -> (string)

The enable setting of the data source that specifies whether the data source is enabled or disabled.

environmentId -> (string)

The ID of the environemnt associated with this data source.

errorMessage -> (structure)

Specifies the error message that is returned if the operation cannot be successfully completed.

errorDetail -> (string)

The details of the error message that is returned if the operation cannot be successfully completed.

errorType -> (string)

The type of the error message that is returned if the operation cannot be successfully completed.

id -> (string)

The ID of the data source that is deleted.

lastRunAt -> (timestamp)

The timestamp of when the data source was last run.

lastRunErrorMessage -> (structure)

Specifies the error message that is returned if the operation cannot be successfully completed.

errorDetail -> (string)

The details of the error message that is returned if the operation cannot be successfully completed.

errorType -> (string)

The type of the error message that is returned if the operation cannot be successfully completed.

lastRunStatus -> (string)

The status of the last run of this data source.

name -> (string)

The name of the data source that is deleted.

projectId -> (string)

The ID of the project in which this data source exists and from which itâs deleted.

publishOnImport -> (boolean)

Specifies whether the assets that this data source creates in the inventory are to be also automatically published to the catalog.

retainPermissionsOnRevokeFailure -> (boolean)

Specifies that the granted permissions are retained in case of a self-subscribe functionality failure for a data source.

schedule -> (structure)

The schedule of runs for this data source.

schedule -> (string)

The schedule of the data source runs.

timezone -> (string)

The timezone of the data source run.

selfGrantStatus -> (tagged union structure)

Specifies the status of the self-granting functionality.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `glueSelfGrantStatus`, `redshiftSelfGrantStatus`.

glueSelfGrantStatus -> (structure)

The details for the self granting status for a Glue data source.

selfGrantStatusDetails -> (list)

The details for the self granting status for a Glue data source.

(structure)

The details for the self granting status.

databaseName -> (string)

The name of the database used for the data source.

failureCause -> (string)

The reason for why the operation failed.

schemaName -> (string)

The name of the schema used in the data source.

status -> (string)

The self granting status of the data source.

redshiftSelfGrantStatus -> (structure)

The details for the self granting status for an Amazon Redshift data source.

selfGrantStatusDetails -> (list)

The details for the self granting status for an Amazon Redshift data source.

(structure)

The details for the self granting status.

databaseName -> (string)

The name of the database used for the data source.

failureCause -> (string)

The reason for why the operation failed.

schemaName -> (string)

The name of the schema used in the data source.

status -> (string)

The self granting status of the data source.

status -> (string)

The status of this data source.

type -> (string)

The type of this data source.

updatedAt -> (timestamp)

The timestamp of when this data source was updated.