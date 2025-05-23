# describe-connectorsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connectors.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connectors.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html#cli-aws-appflow) ]

# describe-connectors

## Description

Describes the connectors vended by Amazon AppFlow for specified connector types. If you donât specify a connector type, this operation describes all connectors vended by Amazon AppFlow. If there are more connectors than can be returned in one page, the response contains a `nextToken` object, which can be be passed in to the next call to the `DescribeConnectors` API operation to retrieve the next page.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appflow-2020-08-23/DescribeConnectors)

## Synopsis

```
describe-connectors
[--connector-types <value>]
[--max-results <value>]
[--next-token <value>]
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

`--connector-types` (list)

The type of connector, such as Salesforce, Amplitude, and so on.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  Salesforce
  Singular
  Slack
  Redshift
  S3
  Marketo
  Googleanalytics
  Zendesk
  Servicenow
  Datadog
  Trendmicro
  Snowflake
  Dynatrace
  Infornexus
  Amplitude
  Veeva
  EventBridge
  LookoutMetrics
  Upsolver
  Honeycode
  CustomerProfiles
  SAPOData
  CustomConnector
  Pardot
```

`--max-results` (integer)

The maximum number of items that should be returned in the result set. The default is 20.

`--next-token` (string)

The pagination token for the next page of data.

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

connectorConfigurations -> (map)

The configuration that is applied to the connectors used in the flow.

key -> (string)

value -> (structure)

The configuration settings related to a given connector.

canUseAsSource -> (boolean)

Specifies whether the connector can be used as a source.

canUseAsDestination -> (boolean)

Specifies whether the connector can be used as a destination.

supportedDestinationConnectors -> (list)

Lists the connectors that are available for use as destinations.

(string)

supportedSchedulingFrequencies -> (list)

Specifies the supported flow frequency for that connector.

(string)

isPrivateLinkEnabled -> (boolean)

Specifies if PrivateLink is enabled for that connector.

isPrivateLinkEndpointUrlRequired -> (boolean)

Specifies if a PrivateLink endpoint URL is required.

supportedTriggerTypes -> (list)

Specifies the supported trigger types for the flow.

(string)

connectorMetadata -> (structure)

Specifies connector-specific metadata such as `oAuthScopes` , `supportedRegions` , `privateLinkServiceUrl` , and so on.

Amplitude -> (structure)

The connector metadata specific to Amplitude.

Datadog -> (structure)

The connector metadata specific to Datadog.

Dynatrace -> (structure)

The connector metadata specific to Dynatrace.

GoogleAnalytics -> (structure)

The connector metadata specific to Google Analytics.

oAuthScopes -> (list)

The desired authorization scope for the Google Analytics account.

(string)

InforNexus -> (structure)

The connector metadata specific to Infor Nexus.

Marketo -> (structure)

The connector metadata specific to Marketo.

Redshift -> (structure)

The connector metadata specific to Amazon Redshift.

S3 -> (structure)

The connector metadata specific to Amazon S3.

Salesforce -> (structure)

The connector metadata specific to Salesforce.

oAuthScopes -> (list)

The desired authorization scope for the Salesforce account.

(string)

dataTransferApis -> (list)

The Salesforce APIs that you can have Amazon AppFlow use when your flows transfers data to or from Salesforce.

(string)

oauth2GrantTypesSupported -> (list)

The OAuth 2.0 grant types that Amazon AppFlow can use when it requests an access token from Salesforce. Amazon AppFlow requires an access token each time it attempts to access your Salesforce records.

AUTHORIZATION_CODE

Amazon AppFlow passes an authorization code when it requests the access token from Salesforce. Amazon AppFlow receives the authorization code from Salesforce after you log in to your Salesforce account and authorize Amazon AppFlow to access your records.

JWT_BEARER

Amazon AppFlow passes a JSON web token (JWT) when it requests the access token from Salesforce. You provide the JWT to Amazon AppFlow when you define the connection to your Salesforce account. When you use this grant type, you donât need to log in to your Salesforce account to authorize Amazon AppFlow to access your records.

### Note

The CLIENT_CREDENTIALS value is not supported for Salesforce.

(string)

ServiceNow -> (structure)

The connector metadata specific to ServiceNow.

Singular -> (structure)

The connector metadata specific to Singular.

Slack -> (structure)

The connector metadata specific to Slack.

oAuthScopes -> (list)

The desired authorization scope for the Slack account.

(string)

Snowflake -> (structure)

The connector metadata specific to Snowflake.

supportedRegions -> (list)

Specifies the supported Amazon Web Services Regions when using Snowflake.

(string)

Trendmicro -> (structure)

The connector metadata specific to Trend Micro.

Veeva -> (structure)

The connector metadata specific to Veeva.

Zendesk -> (structure)

The connector metadata specific to Zendesk.

oAuthScopes -> (list)

The desired authorization scope for the Zendesk account.

(string)

EventBridge -> (structure)

The connector metadata specific to Amazon EventBridge.

Upsolver -> (structure)

The connector metadata specific to Upsolver.

CustomerProfiles -> (structure)

The connector metadata specific to Amazon Connect Customer Profiles.

Honeycode -> (structure)

The connector metadata specific to Amazon Honeycode.

oAuthScopes -> (list)

The desired authorization scope for the Amazon Honeycode account.

(string)

SAPOData -> (structure)

The connector metadata specific to SAPOData.

Pardot -> (structure)

The connector metadata specific to Salesforce Pardot.

connectorType -> (string)

The connector type.

connectorLabel -> (string)

The label used for registering the connector.

connectorDescription -> (string)

A description about the connector.

connectorOwner -> (string)

The owner who developed the connector.

connectorName -> (string)

The connector name.

connectorVersion -> (string)

The connector version.

connectorArn -> (string)

The Amazon Resource Name (ARN) for the registered connector.

connectorModes -> (list)

The connection modes that the connector supports.

(string)

authenticationConfig -> (structure)

The authentication config required for the connector.

isBasicAuthSupported -> (boolean)

Indicates whether basic authentication is supported by the connector.

isApiKeyAuthSupported -> (boolean)

Indicates whether API key authentication is supported by the connector

isOAuth2Supported -> (boolean)

Indicates whether OAuth 2.0 authentication is supported by the connector.

isCustomAuthSupported -> (boolean)

Indicates whether custom authentication is supported by the connector

oAuth2Defaults -> (structure)

Contains the default values required for OAuth 2.0 authentication.

oauthScopes -> (list)

OAuth 2.0 scopes that the connector supports.

(string)

tokenUrls -> (list)

Token URLs that can be used for OAuth 2.0 authentication.

(string)

authCodeUrls -> (list)

Auth code URLs that can be used for OAuth 2.0 authentication.

(string)

oauth2GrantTypesSupported -> (list)

OAuth 2.0 grant types supported by the connector.

(string)

oauth2CustomProperties -> (list)

List of custom parameters required for OAuth 2.0 authentication.

(structure)

Custom parameter required for OAuth 2.0 authentication.

key -> (string)

The key of the custom parameter required for OAuth 2.0 authentication.

isRequired -> (boolean)

Indicates whether the custom parameter for OAuth 2.0 authentication is required.

label -> (string)

The label of the custom parameter used for OAuth 2.0 authentication.

description -> (string)

A description about the custom parameter used for OAuth 2.0 authentication.

isSensitiveField -> (boolean)

Indicates whether this authentication custom parameter is a sensitive field.

connectorSuppliedValues -> (list)

Contains default values for this authentication parameter that are supplied by the connector.

(string)

type -> (string)

Indicates whether custom parameter is used with TokenUrl or AuthUrl.

customAuthConfigs -> (list)

Contains information required for custom authentication.

(structure)

Configuration information required for custom authentication.

customAuthenticationType -> (string)

The authentication type that the custom connector uses.

authParameters -> (list)

Information about authentication parameters required for authentication.

(structure)

Information about required authentication parameters.

key -> (string)

The authentication key required to authenticate with the connector.

isRequired -> (boolean)

Indicates whether this authentication parameter is required.

label -> (string)

Label used for authentication parameter.

description -> (string)

A description about the authentication parameter.

isSensitiveField -> (boolean)

Indicates whether this authentication parameter is a sensitive field.

connectorSuppliedValues -> (list)

Contains default values for this authentication parameter that are supplied by the connector.

(string)

connectorRuntimeSettings -> (list)

The required connector runtime settings.

(structure)

Contains information about the connector runtime settings that are required for flow execution.

key -> (string)

Contains value information about the connector runtime setting.

dataType -> (string)

Data type of the connector runtime setting.

isRequired -> (boolean)

Indicates whether this connector runtime setting is required.

label -> (string)

A label used for connector runtime setting.

description -> (string)

A description about the connector runtime setting.

scope -> (string)

Indicates the scope of the connector runtime setting.

connectorSuppliedValueOptions -> (list)

Contains default values for the connector runtime setting that are supplied by the connector.

(string)

supportedApiVersions -> (list)

A list of API versions that are supported by the connector.

(string)

supportedOperators -> (list)

A list of operators supported by the connector.

(string)

supportedWriteOperations -> (list)

A list of write operations supported by the connector.

(string)

The possible write operations in the destination connector. When this value is not provided, this defaults to the `INSERT` operation.

connectorProvisioningType -> (string)

The provisioning type used to register the connector.

connectorProvisioningConfig -> (structure)

The configuration required for registering the connector.

lambda -> (structure)

Contains information about the configuration of the lambda which is being registered as the connector.

lambdaArn -> (string)

Lambda ARN of the connector being registered.

logoURL -> (string)

Logo URL of the connector.

registeredAt -> (timestamp)

The date on which the connector was registered.

registeredBy -> (string)

Information about who registered the connector.

supportedDataTransferTypes -> (list)

The data transfer types that the connector supports.

RECORD

Structured records.

FILE

Files or binary data.

(string)

supportedDataTransferApis -> (list)

The APIs of the connector application that Amazon AppFlow can use to transfer your data.

(structure)

The API of the connector application that Amazon AppFlow uses to transfer your data.

Name -> (string)

The name of the connector application API.

Type -> (string)

You can specify one of the following types:

AUTOMATIC

The default. Optimizes a flow for datasets that fluctuate in size from small to large. For each flow run, Amazon AppFlow chooses to use the SYNC or ASYNC API type based on the amount of data that the run transfers.

SYNC

A synchronous API. This type of API optimizes a flow for small to medium-sized datasets.

ASYNC

An asynchronous API. This type of API optimizes a flow for large datasets.

connectors -> (list)

Information about the connectors supported in Amazon AppFlow.

(structure)

Information about the registered connector.

connectorDescription -> (string)

A description about the registered connector.

connectorName -> (string)

The name of the connector.

connectorOwner -> (string)

The owner of the connector.

connectorVersion -> (string)

The connector version.

applicationType -> (string)

The application type of the connector.

connectorType -> (string)

The connector type.

connectorLabel -> (string)

A label used for the connector.

registeredAt -> (timestamp)

The time at which the connector was registered.

registeredBy -> (string)

The user who registered the connector.

connectorProvisioningType -> (string)

The provisioning type that the connector uses.

connectorModes -> (list)

The connection mode that the connector supports.

(string)

supportedDataTransferTypes -> (list)

The data transfer types that the connector supports.

RECORD

Structured records.

FILE

Files or binary data.

(string)

nextToken -> (string)

The pagination token for the next page of data.