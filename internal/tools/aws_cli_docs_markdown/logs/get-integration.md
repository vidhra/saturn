# get-integrationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/get-integration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/get-integration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# get-integration

## Description

Returns information about one integration between CloudWatch Logs and OpenSearch Service.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/GetIntegration)

## Synopsis

```
get-integration
--integration-name <value>
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

`--integration-name` (string)

The name of the integration that you want to find information about. To find the name of your integration, use [ListIntegrations](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListIntegrations.html)

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

integrationName -> (string)

The name of the integration.

integrationType -> (string)

The type of integration. Integrations with OpenSearch Service have the type `OPENSEARCH` .

integrationStatus -> (string)

The current status of this integration.

integrationDetails -> (tagged union structure)

A structure that contains information about the integration configuration. For an integration with OpenSearch Service, this includes information about OpenSearch Service resources such as the collection, the workspace, and policies.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `openSearchIntegrationDetails`.

openSearchIntegrationDetails -> (structure)

This structure contains complete information about one integration between CloudWatch Logs and OpenSearch Service.

dataSource -> (structure)

This structure contains information about the OpenSearch Service data source used for this integration. This data source was created as part of the integration setup. An OpenSearch Service data source defines the source and destination for OpenSearch Service queries. It includes the role required to execute queries and write to collections.

For more information about OpenSearch Service data sources , see [Creating OpenSearch Service data source integrations with Amazon S3.](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/direct-query-s3-creating.html)

dataSourceName -> (string)

The name of the OpenSearch Service data source.

status -> (structure)

This structure contains information about the status of this OpenSearch Service resource.

status -> (string)

The current status of this resource.

statusMessage -> (string)

A message with additional information about the status of this resource.

application -> (structure)

This structure contains information about the OpenSearch Service application used for this integration. An OpenSearch Service application is the web application that was created by the integration with CloudWatch Logs. It hosts the vended logs dashboards.

applicationEndpoint -> (string)

The endpoint of the application.

applicationArn -> (string)

The Amazon Resource Name (ARN) of the application.

applicationId -> (string)

The ID of the application.

status -> (structure)

This structure contains information about the status of this OpenSearch Service resource.

status -> (string)

The current status of this resource.

statusMessage -> (string)

A message with additional information about the status of this resource.

collection -> (structure)

This structure contains information about the OpenSearch Service collection used for this integration. This collection was created as part of the integration setup. An OpenSearch Service collection is a logical grouping of one or more indexes that represent an analytics workload. For more information, see [Creating and managing OpenSearch Service Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-collections.html) .

collectionEndpoint -> (string)

The endpoint of the collection.

collectionArn -> (string)

The ARN of the collection.

status -> (structure)

This structure contains information about the status of this OpenSearch Service resource.

status -> (string)

The current status of this resource.

statusMessage -> (string)

A message with additional information about the status of this resource.

workspace -> (structure)

This structure contains information about the OpenSearch Service workspace used for this integration. An OpenSearch Service workspace is the collection of dashboards along with other OpenSearch Service tools. This workspace was created automatically as part of the integration setup. For more information, see [Centralized OpenSearch user interface (Dashboards) with OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html) .

workspaceId -> (string)

The ID of this workspace.

status -> (structure)

This structure contains information about the status of an OpenSearch Service resource.

status -> (string)

The current status of this resource.

statusMessage -> (string)

A message with additional information about the status of this resource.

encryptionPolicy -> (structure)

This structure contains information about the OpenSearch Service encryption policy used for this integration. The encryption policy was created automatically when you created the integration. For more information, see [Encryption policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-encryption.html#serverless-encryption-policies) in the OpenSearch Service Developer Guide.

policyName -> (string)

The name of the encryption policy.

status -> (structure)

This structure contains information about the status of this OpenSearch Service resource.

status -> (string)

The current status of this resource.

statusMessage -> (string)

A message with additional information about the status of this resource.

networkPolicy -> (structure)

This structure contains information about the OpenSearch Service network policy used for this integration. The network policy assigns network access settings to collections. For more information, see [Network policies](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-network.html#serverless-network-policies) in the OpenSearch Service Developer Guide.

policyName -> (string)

The name of the network policy.

status -> (structure)

This structure contains information about the status of this OpenSearch Service resource.

status -> (string)

The current status of this resource.

statusMessage -> (string)

A message with additional information about the status of this resource.

accessPolicy -> (structure)

This structure contains information about the OpenSearch Service data access policy used for this integration. The access policy defines the access controls for the collection. This data access policy was automatically created as part of the integration setup. For more information about OpenSearch Service data access policies, see [Data access control for Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-data-access.html) in the OpenSearch Service Developer Guide.

policyName -> (string)

The name of the data access policy.

status -> (structure)

This structure contains information about the status of this OpenSearch Service resource.

status -> (string)

The current status of this resource.

statusMessage -> (string)

A message with additional information about the status of this resource.

lifecyclePolicy -> (structure)

This structure contains information about the OpenSearch Service data lifecycle policy used for this integration. The lifecycle policy determines the lifespan of the data in the collection. It was automatically created as part of the integration setup.

For more information, see [Using data lifecycle policies with OpenSearch Service Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-lifecycle.html) in the OpenSearch Service Developer Guide.

policyName -> (string)

The name of the lifecycle policy.

status -> (structure)

This structure contains information about the status of this OpenSearch Service resource.

status -> (string)

The current status of this resource.

statusMessage -> (string)

A message with additional information about the status of this resource.