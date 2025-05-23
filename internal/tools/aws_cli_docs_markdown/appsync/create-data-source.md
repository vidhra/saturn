# create-data-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-data-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/create-data-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appsync](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appsync/index.html#cli-aws-appsync) ]

# create-data-source

## Description

Creates a `DataSource` object.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appsync-2017-07-25/CreateDataSource)

## Synopsis

```
create-data-source
--api-id <value>
--name <value>
[--description <value>]
--type <value>
[--service-role-arn <value>]
[--dynamodb-config <value>]
[--lambda-config <value>]
[--elasticsearch-config <value>]
[--open-search-service-config <value>]
[--http-config <value>]
[--relational-database-config <value>]
[--event-bridge-config <value>]
[--metrics-config <value>]
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

`--api-id` (string)

The API ID for the GraphQL API for the `DataSource` .

`--name` (string)

A user-supplied name for the `DataSource` .

`--description` (string)

A description of the `DataSource` .

`--type` (string)

The type of the `DataSource` .

Possible values:

- `AWS_LAMBDA`
- `AMAZON_DYNAMODB`
- `AMAZON_ELASTICSEARCH`
- `NONE`
- `HTTP`
- `RELATIONAL_DATABASE`
- `AMAZON_OPENSEARCH_SERVICE`
- `AMAZON_EVENTBRIDGE`
- `AMAZON_BEDROCK_RUNTIME`

`--service-role-arn` (string)

The Identity and Access Management (IAM) service role Amazon Resource Name (ARN) for the data source. The system assumes this role when accessing the data source.

`--dynamodb-config` (structure)

Amazon DynamoDB settings.

tableName -> (string)

The table name.

awsRegion -> (string)

The Amazon Web Services Region.

useCallerCredentials -> (boolean)

Set to TRUE to use Amazon Cognito credentials with this data source.

deltaSyncConfig -> (structure)

The `DeltaSyncConfig` for a versioned data source.

baseTableTTL -> (long)

The number of minutes that an Item is stored in the data source.

deltaSyncTableName -> (string)

The Delta Sync table name.

deltaSyncTableTTL -> (long)

The number of minutes that a Delta Sync log entry is stored in the Delta Sync table.

versioned -> (boolean)

Set to TRUE to use Conflict Detection and Resolution with this data source.

Shorthand Syntax:

```
tableName=string,awsRegion=string,useCallerCredentials=boolean,deltaSyncConfig={baseTableTTL=long,deltaSyncTableName=string,deltaSyncTableTTL=long},versioned=boolean
```

JSON Syntax:

```
{
  "tableName": "string",
  "awsRegion": "string",
  "useCallerCredentials": true|false,
  "deltaSyncConfig": {
    "baseTableTTL": long,
    "deltaSyncTableName": "string",
    "deltaSyncTableTTL": long
  },
  "versioned": true|false
}
```

`--lambda-config` (structure)

Lambda settings.

lambdaFunctionArn -> (string)

The Amazon Resource Name (ARN) for the Lambda function.

Shorthand Syntax:

```
lambdaFunctionArn=string
```

JSON Syntax:

```
{
  "lambdaFunctionArn": "string"
}
```

`--elasticsearch-config` (structure)

Amazon OpenSearch Service settings.

As of September 2021, Amazon Elasticsearch service is Amazon OpenSearch Service. This configuration is deprecated. For new data sources, use  CreateDataSourceRequest$openSearchServiceConfig to create an OpenSearch data source.

endpoint -> (string)

The endpoint.

awsRegion -> (string)

The Amazon Web Services Region.

Shorthand Syntax:

```
endpoint=string,awsRegion=string
```

JSON Syntax:

```
{
  "endpoint": "string",
  "awsRegion": "string"
}
```

`--open-search-service-config` (structure)

Amazon OpenSearch Service settings.

endpoint -> (string)

The endpoint.

awsRegion -> (string)

The Amazon Web Services Region.

Shorthand Syntax:

```
endpoint=string,awsRegion=string
```

JSON Syntax:

```
{
  "endpoint": "string",
  "awsRegion": "string"
}
```

`--http-config` (structure)

HTTP endpoint settings.

endpoint -> (string)

The HTTP URL endpoint. You can specify either the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If you donât specify the port, AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.

authorizationConfig -> (structure)

The authorization configuration in case the HTTP endpoint requires authorization.

authorizationType -> (string)

The authorization type that the HTTP endpoint requires.

- **AWS_IAM** : The authorization type is Signature Version 4 (SigV4).

awsIamConfig -> (structure)

The Identity and Access Management (IAM) settings.

signingRegion -> (string)

The signing Amazon Web Services Region for IAM authorization.

signingServiceName -> (string)

The signing service name for IAM authorization.

Shorthand Syntax:

```
endpoint=string,authorizationConfig={authorizationType=string,awsIamConfig={signingRegion=string,signingServiceName=string}}
```

JSON Syntax:

```
{
  "endpoint": "string",
  "authorizationConfig": {
    "authorizationType": "AWS_IAM",
    "awsIamConfig": {
      "signingRegion": "string",
      "signingServiceName": "string"
    }
  }
}
```

`--relational-database-config` (structure)

Relational database settings.

relationalDatabaseSourceType -> (string)

Source type for the relational database.

- **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon Relational Database Service (Amazon RDS) HTTP endpoint.

rdsHttpEndpointConfig -> (structure)

Amazon RDS HTTP endpoint settings.

awsRegion -> (string)

Amazon Web Services Region for Amazon RDS HTTP endpoint.

dbClusterIdentifier -> (string)

Amazon RDS cluster Amazon Resource Name (ARN).

databaseName -> (string)

Logical database name.

schema -> (string)

Logical schema name.

awsSecretStoreArn -> (string)

Amazon Web Services secret store Amazon Resource Name (ARN) for database credentials.

Shorthand Syntax:

```
relationalDatabaseSourceType=string,rdsHttpEndpointConfig={awsRegion=string,dbClusterIdentifier=string,databaseName=string,schema=string,awsSecretStoreArn=string}
```

JSON Syntax:

```
{
  "relationalDatabaseSourceType": "RDS_HTTP_ENDPOINT",
  "rdsHttpEndpointConfig": {
    "awsRegion": "string",
    "dbClusterIdentifier": "string",
    "databaseName": "string",
    "schema": "string",
    "awsSecretStoreArn": "string"
  }
}
```

`--event-bridge-config` (structure)

Amazon EventBridge settings.

eventBusArn -> (string)

The ARN of the event bus. For more information about event buses, see [Amazon EventBridge event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html) .

Shorthand Syntax:

```
eventBusArn=string
```

JSON Syntax:

```
{
  "eventBusArn": "string"
}
```

`--metrics-config` (string)

Enables or disables enhanced data source metrics for specified data sources. Note that `metricsConfig` wonât be used unless the `dataSourceLevelMetricsBehavior` value is set to `PER_DATA_SOURCE_METRICS` . If the `dataSourceLevelMetricsBehavior` is set to `FULL_REQUEST_DATA_SOURCE_METRICS` instead, `metricsConfig` will be ignored. However, you can still set its value.

`metricsConfig` can be `ENABLED` or `DISABLED` .

Possible values:

- `ENABLED`
- `DISABLED`

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

dataSource -> (structure)

The `DataSource` object.

dataSourceArn -> (string)

The data source Amazon Resource Name (ARN).

name -> (string)

The name of the data source.

description -> (string)

The description of the data source.

type -> (string)

The type of the data source.

- **AWS_LAMBDA** : The data source is an Lambda function.
- **AMAZON_DYNAMODB** : The data source is an Amazon DynamoDB table.
- **AMAZON_ELASTICSEARCH** : The data source is an Amazon OpenSearch Service domain.
- **AMAZON_OPENSEARCH_SERVICE** : The data source is an Amazon OpenSearch Service domain.
- **AMAZON_EVENTBRIDGE** : The data source is an Amazon EventBridge configuration.
- **AMAZON_BEDROCK_RUNTIME** : The data source is the Amazon Bedrock runtime.
- **NONE** : There is no data source. Use this type when you want to invoke a GraphQL operation without connecting to a data source, such as when youâre performing data transformation with resolvers or invoking a subscription from a mutation.
- **HTTP** : The data source is an HTTP endpoint.
- **RELATIONAL_DATABASE** : The data source is a relational database.

serviceRoleArn -> (string)

The Identity and Access Management (IAM) service role Amazon Resource Name (ARN) for the data source. The system assumes this role when accessing the data source.

dynamodbConfig -> (structure)

DynamoDB settings.

tableName -> (string)

The table name.

awsRegion -> (string)

The Amazon Web Services Region.

useCallerCredentials -> (boolean)

Set to TRUE to use Amazon Cognito credentials with this data source.

deltaSyncConfig -> (structure)

The `DeltaSyncConfig` for a versioned data source.

baseTableTTL -> (long)

The number of minutes that an Item is stored in the data source.

deltaSyncTableName -> (string)

The Delta Sync table name.

deltaSyncTableTTL -> (long)

The number of minutes that a Delta Sync log entry is stored in the Delta Sync table.

versioned -> (boolean)

Set to TRUE to use Conflict Detection and Resolution with this data source.

lambdaConfig -> (structure)

Lambda settings.

lambdaFunctionArn -> (string)

The Amazon Resource Name (ARN) for the Lambda function.

elasticsearchConfig -> (structure)

Amazon OpenSearch Service settings.

endpoint -> (string)

The endpoint.

awsRegion -> (string)

The Amazon Web Services Region.

openSearchServiceConfig -> (structure)

Amazon OpenSearch Service settings.

endpoint -> (string)

The endpoint.

awsRegion -> (string)

The Amazon Web Services Region.

httpConfig -> (structure)

HTTP endpoint settings.

endpoint -> (string)

The HTTP URL endpoint. You can specify either the domain name or IP, and port combination, and the URL scheme must be HTTP or HTTPS. If you donât specify the port, AppSync uses the default port 80 for the HTTP endpoint and port 443 for HTTPS endpoints.

authorizationConfig -> (structure)

The authorization configuration in case the HTTP endpoint requires authorization.

authorizationType -> (string)

The authorization type that the HTTP endpoint requires.

- **AWS_IAM** : The authorization type is Signature Version 4 (SigV4).

awsIamConfig -> (structure)

The Identity and Access Management (IAM) settings.

signingRegion -> (string)

The signing Amazon Web Services Region for IAM authorization.

signingServiceName -> (string)

The signing service name for IAM authorization.

relationalDatabaseConfig -> (structure)

Relational database settings.

relationalDatabaseSourceType -> (string)

Source type for the relational database.

- **RDS_HTTP_ENDPOINT** : The relational database source type is an Amazon Relational Database Service (Amazon RDS) HTTP endpoint.

rdsHttpEndpointConfig -> (structure)

Amazon RDS HTTP endpoint settings.

awsRegion -> (string)

Amazon Web Services Region for Amazon RDS HTTP endpoint.

dbClusterIdentifier -> (string)

Amazon RDS cluster Amazon Resource Name (ARN).

databaseName -> (string)

Logical database name.

schema -> (string)

Logical schema name.

awsSecretStoreArn -> (string)

Amazon Web Services secret store Amazon Resource Name (ARN) for database credentials.

eventBridgeConfig -> (structure)

Amazon EventBridge settings.

eventBusArn -> (string)

The ARN of the event bus. For more information about event buses, see [Amazon EventBridge event buses](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html) .

metricsConfig -> (string)

Enables or disables enhanced data source metrics for specified data sources. Note that `metricsConfig` wonât be used unless the `dataSourceLevelMetricsBehavior` value is set to `PER_DATA_SOURCE_METRICS` . If the `dataSourceLevelMetricsBehavior` is set to `FULL_REQUEST_DATA_SOURCE_METRICS` instead, `metricsConfig` will be ignored. However, you can still set its value.

`metricsConfig` can be `ENABLED` or `DISABLED` .