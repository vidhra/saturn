# describe-connector-profilesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connector-profiles.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-connector-profiles.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html#cli-aws-appflow) ]

# describe-connector-profiles

## Description

Returns a list of `connector-profile` details matching the provided `connector-profile` names and `connector-types` . Both input lists are optional, and you can use them to filter the result.

If no names or `connector-types` are provided, returns all connector profiles in a paginated form. If there is no match, this operation returns an empty list.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appflow-2020-08-23/DescribeConnectorProfiles)

## Synopsis

```
describe-connector-profiles
[--connector-profile-names <value>]
[--connector-type <value>]
[--connector-label <value>]
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

`--connector-profile-names` (list)

The name of the connector profile. The name is unique for each `ConnectorProfile` in the Amazon Web Services account.

(string)

Syntax:

```
"string" "string" ...
```

`--connector-type` (string)

The type of connector, such as Salesforce, Amplitude, and so on.

Possible values:

- `Salesforce`
- `Singular`
- `Slack`
- `Redshift`
- `S3`
- `Marketo`
- `Googleanalytics`
- `Zendesk`
- `Servicenow`
- `Datadog`
- `Trendmicro`
- `Snowflake`
- `Dynatrace`
- `Infornexus`
- `Amplitude`
- `Veeva`
- `EventBridge`
- `LookoutMetrics`
- `Upsolver`
- `Honeycode`
- `CustomerProfiles`
- `SAPOData`
- `CustomConnector`
- `Pardot`

`--connector-label` (string)

The name of the connector. The name is unique for each `ConnectorRegistration` in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/.

`--max-results` (integer)

Specifies the maximum number of items that should be returned in the result set. The default for `maxResults` is 20 (for all paginated API operations).

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

connectorProfileDetails -> (list)

Returns information about the connector profiles associated with the flow.

(structure)

Describes an instance of a connector. This includes the provided name, credentials ARN, connection-mode, and so on. To keep the API intuitive and extensible, the fields that are common to all types of connector profiles are explicitly specified at the top level. The rest of the connector-specific properties are available via the `connectorProfileProperties` field.

connectorProfileArn -> (string)

The Amazon Resource Name (ARN) of the connector profile.

connectorProfileName -> (string)

The name of the connector profile. The name is unique for each `ConnectorProfile` in the Amazon Web Services account.

connectorType -> (string)

The type of connector, such as Salesforce, Amplitude, and so on.

connectorLabel -> (string)

The label for the connector profile being created.

connectionMode -> (string)

Indicates the connection mode and if it is public or private.

credentialsArn -> (string)

The Amazon Resource Name (ARN) of the connector profile credentials.

connectorProfileProperties -> (structure)

The connector-specific properties of the profile configuration.

Amplitude -> (structure)

The connector-specific properties required by Amplitude.

Datadog -> (structure)

The connector-specific properties required by Datadog.

instanceUrl -> (string)

The location of the Datadog resource.

Dynatrace -> (structure)

The connector-specific properties required by Dynatrace.

instanceUrl -> (string)

The location of the Dynatrace resource.

GoogleAnalytics -> (structure)

The connector-specific properties required Google Analytics.

Honeycode -> (structure)

The connector-specific properties required by Amazon Honeycode.

InforNexus -> (structure)

The connector-specific properties required by Infor Nexus.

instanceUrl -> (string)

The location of the Infor Nexus resource.

Marketo -> (structure)

The connector-specific properties required by Marketo.

instanceUrl -> (string)

The location of the Marketo resource.

Redshift -> (structure)

The connector-specific properties required by Amazon Redshift.

databaseUrl -> (string)

The JDBC URL of the Amazon Redshift cluster.

bucketName -> (string)

A name for the associated Amazon S3 bucket.

bucketPrefix -> (string)

The object key for the destination bucket in which Amazon AppFlow places the files.

roleArn -> (string)

The Amazon Resource Name (ARN) of IAM role that grants Amazon Redshift read-only access to Amazon S3. For more information, and for the polices that you attach to this role, see [Allow Amazon Redshift to access your Amazon AppFlow data in Amazon S3](https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#redshift-access-s3) .

dataApiRoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role that permits Amazon AppFlow to access your Amazon Redshift database through the Data API. For more information, and for the polices that you attach to this role, see [Allow Amazon AppFlow to access Amazon Redshift databases with the Data API](https://docs.aws.amazon.com/appflow/latest/userguide/security_iam_service-role-policies.html#access-redshift) .

isRedshiftServerless -> (boolean)

Indicates whether the connector profile defines a connection to an Amazon Redshift Serverless data warehouse.

clusterIdentifier -> (string)

The unique ID thatâs assigned to an Amazon Redshift cluster.

workgroupName -> (string)

The name of an Amazon Redshift workgroup.

databaseName -> (string)

The name of an Amazon Redshift database.

Salesforce -> (structure)

The connector-specific properties required by Salesforce.

instanceUrl -> (string)

The location of the Salesforce resource.

isSandboxEnvironment -> (boolean)

Indicates whether the connector profile applies to a sandbox or production environment.

usePrivateLinkForMetadataAndAuthorization -> (boolean)

If the connection mode for the connector profile is private, this parameter sets whether Amazon AppFlow uses the private network to send metadata and authorization calls to Salesforce. Amazon AppFlow sends private calls through Amazon Web Services PrivateLink. These calls travel through Amazon Web Services infrastructure without being exposed to the public internet.

Set either of the following values:

true

Amazon AppFlow sends all calls to Salesforce over the private network.

These private calls are:

- Calls to get metadata about your Salesforce records. This metadata describes your Salesforce objects and their fields.
- Calls to get or refresh access tokens that allow Amazon AppFlow to access your Salesforce records.
- Calls to transfer your Salesforce records as part of a flow run.

false

The default value. Amazon AppFlow sends some calls to Salesforce privately and other calls over the public internet.

The public calls are:

- Calls to get metadata about your Salesforce records.
- Calls to get or refresh access tokens.

The private calls are:

- Calls to transfer your Salesforce records as part of a flow run.

ServiceNow -> (structure)

The connector-specific properties required by serviceNow.

instanceUrl -> (string)

The location of the ServiceNow resource.

Singular -> (structure)

The connector-specific properties required by Singular.

Slack -> (structure)

The connector-specific properties required by Slack.

instanceUrl -> (string)

The location of the Slack resource.

Snowflake -> (structure)

The connector-specific properties required by Snowflake.

warehouse -> (string)

The name of the Snowflake warehouse.

stage -> (string)

The name of the Amazon S3 stage that was created while setting up an Amazon S3 stage in the Snowflake account. This is written in the following format: < Database>< Schema><Stage Name>.

bucketName -> (string)

The name of the Amazon S3 bucket associated with Snowflake.

bucketPrefix -> (string)

The bucket path that refers to the Amazon S3 bucket associated with Snowflake.

privateLinkServiceName -> (string)

The Snowflake Private Link service name to be used for private data transfers.

accountName -> (string)

The name of the account.

region -> (string)

The Amazon Web Services Region of the Snowflake account.

Trendmicro -> (structure)

The connector-specific properties required by Trend Micro.

Veeva -> (structure)

The connector-specific properties required by Veeva.

instanceUrl -> (string)

The location of the Veeva resource.

Zendesk -> (structure)

The connector-specific properties required by Zendesk.

instanceUrl -> (string)

The location of the Zendesk resource.

SAPOData -> (structure)

The connector-specific profile properties required when using SAPOData.

applicationHostUrl -> (string)

The location of the SAPOData resource.

applicationServicePath -> (string)

The application path to catalog service.

portNumber -> (integer)

The port number of the SAPOData instance.

clientNumber -> (string)

The client number for the client creating the connection.

logonLanguage -> (string)

The logon language of SAPOData instance.

privateLinkServiceName -> (string)

The SAPOData Private Link service name to be used for private data transfers.

oAuthProperties -> (structure)

The SAPOData OAuth properties required for OAuth type authentication.

tokenUrl -> (string)

The token url required to fetch access/refresh tokens using authorization code and also to refresh expired access token using refresh token.

authCodeUrl -> (string)

The authorization code url required to redirect to SAP Login Page to fetch authorization code for OAuth type authentication.

oAuthScopes -> (list)

The OAuth scopes required for OAuth type authentication.

(string)

disableSSO -> (boolean)

If you set this parameter to `true` , Amazon AppFlow bypasses the single sign-on (SSO) settings in your SAP account when it accesses your SAP OData instance.

Whether you need this option depends on the types of credentials that you applied to your SAP OData connection profile. If your profile uses basic authentication credentials, SAP SSO can prevent Amazon AppFlow from connecting to your account with your username and password. In this case, bypassing SSO makes it possible for Amazon AppFlow to connect successfully. However, if your profile uses OAuth credentials, this parameter has no affect.

CustomConnector -> (structure)

The properties required by the custom connector.

profileProperties -> (map)

A map of properties that are required to create a profile for the custom connector.

key -> (string)

value -> (string)

oAuth2Properties -> (structure)

The OAuth 2.0 properties required for OAuth 2.0 authentication.

tokenUrl -> (string)

The token URL required for OAuth 2.0 authentication.

oAuth2GrantType -> (string)

The OAuth 2.0 grant type used by connector for OAuth 2.0 authentication.

tokenUrlCustomProperties -> (map)

Associates your token URL with a map of properties that you define. Use this parameter to provide any additional details that the connector requires to authenticate your request.

key -> (string)

value -> (string)

Pardot -> (structure)

The connector-specific properties required by Salesforce Pardot.

instanceUrl -> (string)

The location of the Salesforce Pardot resource.

isSandboxEnvironment -> (boolean)

Indicates whether the connector profile applies to a sandbox or production environment.

businessUnitId -> (string)

The business unit id of Salesforce Pardot instance.

createdAt -> (timestamp)

Specifies when the connector profile was created.

lastUpdatedAt -> (timestamp)

Specifies when the connector profile was last updated.

privateConnectionProvisioningState -> (structure)

Specifies the private connection provisioning state.

status -> (string)

Specifies the private connection provisioning status.

failureMessage -> (string)

Specifies the private connection provisioning failure reason.

failureCause -> (string)

Specifies the private connection provisioning failure cause.

nextToken -> (string)

The pagination token for the next page of data. If `nextToken=null` , this means that all records have been fetched.