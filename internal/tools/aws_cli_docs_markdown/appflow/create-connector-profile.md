# create-connector-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/create-connector-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/create-connector-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html#cli-aws-appflow) ]

# create-connector-profile

## Description

Creates a new connector profile associated with your Amazon Web Services account. There is a soft quota of 100 connector profiles per Amazon Web Services account. If you need more connector profiles than this quota allows, you can submit a request to the Amazon AppFlow team through the Amazon AppFlow support channel. In each connector profile that you create, you can provide the credentials and properties for only one connector.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appflow-2020-08-23/CreateConnectorProfile)

## Synopsis

```
create-connector-profile
--connector-profile-name <value>
[--kms-arn <value>]
--connector-type <value>
[--connector-label <value>]
--connection-mode <value>
--connector-profile-config <value>
[--client-token <value>]
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

`--connector-profile-name` (string)

The name of the connector profile. The name is unique for each `ConnectorProfile` in your Amazon Web Services account.

`--kms-arn` (string)

The ARN (Amazon Resource Name) of the Key Management Service (KMS) key you provide for encryption. This is required if you do not want to use the Amazon AppFlow-managed KMS key. If you donât provide anything here, Amazon AppFlow uses the Amazon AppFlow-managed KMS key.

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

The label of the connector. The label is unique for each `ConnectorRegistration` in your Amazon Web Services account. Only needed if calling for CUSTOMCONNECTOR connector type/.

`--connection-mode` (string)

Indicates the connection mode and specifies whether it is public or private. Private flows use Amazon Web Services PrivateLink to route data over Amazon Web Services infrastructure without exposing it to the public internet.

Possible values:

- `Public`
- `Private`

`--connector-profile-config` (structure)

Defines the connector-specific configuration and credentials.

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

connectorProfileCredentials -> (structure)

The connector-specific credentials required by each connector.

Amplitude -> (structure)

The connector-specific credentials required when using Amplitude.

apiKey -> (string)

A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.

secretKey -> (string)

The Secret Access Key portion of the credentials.

Datadog -> (structure)

The connector-specific credentials required when using Datadog.

apiKey -> (string)

A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.

applicationKey -> (string)

Application keys, in conjunction with your API key, give you full access to Datadogâs programmatic API. Application keys are associated with the user account that created them. The application key is used to log all requests made to the API.

Dynatrace -> (structure)

The connector-specific credentials required when using Dynatrace.

apiToken -> (string)

The API tokens used by Dynatrace API to authenticate various API calls.

GoogleAnalytics -> (structure)

The connector-specific credentials required when using Google Analytics.

clientId -> (string)

The identifier for the desired client.

clientSecret -> (string)

The client secret used by the OAuth client to authenticate to the authorization server.

accessToken -> (string)

The credentials used to access protected Google Analytics resources.

refreshToken -> (string)

The credentials used to acquire new access tokens. This is required only for OAuth2 access tokens, and is not required for OAuth1 access tokens.

oAuthRequest -> (structure)

The OAuth requirement needed to request security tokens from the connector endpoint.

authCode -> (string)

The code provided by the connector when it has been authenticated via the connected app.

redirectUri -> (string)

The URL to which the authentication server redirects the browser after authorization has been granted.

Honeycode -> (structure)

The connector-specific credentials required when using Amazon Honeycode.

accessToken -> (string)

The credentials used to access protected Amazon Honeycode resources.

refreshToken -> (string)

The credentials used to acquire new access tokens.

oAuthRequest -> (structure)

Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

authCode -> (string)

The code provided by the connector when it has been authenticated via the connected app.

redirectUri -> (string)

The URL to which the authentication server redirects the browser after authorization has been granted.

InforNexus -> (structure)

The connector-specific credentials required when using Infor Nexus.

accessKeyId -> (string)

The Access Key portion of the credentials.

userId -> (string)

The identifier for the user.

secretAccessKey -> (string)

The secret key used to sign requests.

datakey -> (string)

The encryption keys used to encrypt data.

Marketo -> (structure)

The connector-specific credentials required when using Marketo.

clientId -> (string)

The identifier for the desired client.

clientSecret -> (string)

The client secret used by the OAuth client to authenticate to the authorization server.

accessToken -> (string)

The credentials used to access protected Marketo resources.

oAuthRequest -> (structure)

The OAuth requirement needed to request security tokens from the connector endpoint.

authCode -> (string)

The code provided by the connector when it has been authenticated via the connected app.

redirectUri -> (string)

The URL to which the authentication server redirects the browser after authorization has been granted.

Redshift -> (structure)

The connector-specific credentials required when using Amazon Redshift.

username -> (string)

The name of the user.

password -> (string)

The password that corresponds to the user name.

Salesforce -> (structure)

The connector-specific credentials required when using Salesforce.

accessToken -> (string)

The credentials used to access protected Salesforce resources.

refreshToken -> (string)

The credentials used to acquire new access tokens.

oAuthRequest -> (structure)

The OAuth requirement needed to request security tokens from the connector endpoint.

authCode -> (string)

The code provided by the connector when it has been authenticated via the connected app.

redirectUri -> (string)

The URL to which the authentication server redirects the browser after authorization has been granted.

clientCredentialsArn -> (string)

The secret manager ARN, which contains the client ID and client secret of the connected app.

oAuth2GrantType -> (string)

Specifies the OAuth 2.0 grant type that Amazon AppFlow uses when it requests an access token from Salesforce. Amazon AppFlow requires an access token each time it attempts to access your Salesforce records.

You can specify one of the following values:

AUTHORIZATION_CODE

Amazon AppFlow passes an authorization code when it requests the access token from Salesforce. Amazon AppFlow receives the authorization code from Salesforce after you log in to your Salesforce account and authorize Amazon AppFlow to access your records.

JWT_BEARER

Amazon AppFlow passes a JSON web token (JWT) when it requests the access token from Salesforce. You provide the JWT to Amazon AppFlow when you define the connection to your Salesforce account. When you use this grant type, you donât need to log in to your Salesforce account to authorize Amazon AppFlow to access your records.

### Note

The CLIENT_CREDENTIALS value is not supported for Salesforce.

jwtToken -> (string)

A JSON web token (JWT) that authorizes Amazon AppFlow to access your Salesforce records.

ServiceNow -> (structure)

The connector-specific credentials required when using ServiceNow.

username -> (string)

The name of the user.

password -> (string)

The password that corresponds to the user name.

oAuth2Credentials -> (structure)

The OAuth 2.0 credentials required to authenticate the user.

clientId -> (string)

The identifier for the desired client.

clientSecret -> (string)

The client secret used by the OAuth client to authenticate to the authorization server.

accessToken -> (string)

The access token used to access the connector on your behalf.

refreshToken -> (string)

The refresh token used to refresh an expired access token.

oAuthRequest -> (structure)

Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

authCode -> (string)

The code provided by the connector when it has been authenticated via the connected app.

redirectUri -> (string)

The URL to which the authentication server redirects the browser after authorization has been granted.

Singular -> (structure)

The connector-specific credentials required when using Singular.

apiKey -> (string)

A unique alphanumeric identifier used to authenticate a user, developer, or calling program to your API.

Slack -> (structure)

The connector-specific credentials required when using Slack.

clientId -> (string)

The identifier for the client.

clientSecret -> (string)

The client secret used by the OAuth client to authenticate to the authorization server.

accessToken -> (string)

The credentials used to access protected Slack resources.

oAuthRequest -> (structure)

The OAuth requirement needed to request security tokens from the connector endpoint.

authCode -> (string)

The code provided by the connector when it has been authenticated via the connected app.

redirectUri -> (string)

The URL to which the authentication server redirects the browser after authorization has been granted.

Snowflake -> (structure)

The connector-specific credentials required when using Snowflake.

username -> (string)

The name of the user.

password -> (string)

The password that corresponds to the user name.

Trendmicro -> (structure)

The connector-specific credentials required when using Trend Micro.

apiSecretKey -> (string)

The Secret Access Key portion of the credentials.

Veeva -> (structure)

The connector-specific credentials required when using Veeva.

username -> (string)

The name of the user.

password -> (string)

The password that corresponds to the user name.

Zendesk -> (structure)

The connector-specific credentials required when using Zendesk.

clientId -> (string)

The identifier for the desired client.

clientSecret -> (string)

The client secret used by the OAuth client to authenticate to the authorization server.

accessToken -> (string)

The credentials used to access protected Zendesk resources.

oAuthRequest -> (structure)

The OAuth requirement needed to request security tokens from the connector endpoint.

authCode -> (string)

The code provided by the connector when it has been authenticated via the connected app.

redirectUri -> (string)

The URL to which the authentication server redirects the browser after authorization has been granted.

SAPOData -> (structure)

The connector-specific profile credentials required when using SAPOData.

basicAuthCredentials -> (structure)

The SAPOData basic authentication credentials.

username -> (string)

The username to use to connect to a resource.

password -> (string)

The password to use to connect to a resource.

oAuthCredentials -> (structure)

The SAPOData OAuth type authentication credentials.

clientId -> (string)

The identifier for the desired client.

clientSecret -> (string)

The client secret used by the OAuth client to authenticate to the authorization server.

accessToken -> (string)

The access token used to access protected SAPOData resources.

refreshToken -> (string)

The refresh token used to refresh expired access token.

oAuthRequest -> (structure)

The OAuth requirement needed to request security tokens from the connector endpoint.

authCode -> (string)

The code provided by the connector when it has been authenticated via the connected app.

redirectUri -> (string)

The URL to which the authentication server redirects the browser after authorization has been granted.

CustomConnector -> (structure)

The connector-specific profile credentials that are required when using the custom connector.

authenticationType -> (string)

The authentication type that the custom connector uses for authenticating while creating a connector profile.

basic -> (structure)

The basic credentials that are required for the authentication of the user.

username -> (string)

The username to use to connect to a resource.

password -> (string)

The password to use to connect to a resource.

oauth2 -> (structure)

The OAuth 2.0 credentials required for the authentication of the user.

clientId -> (string)

The identifier for the desired client.

clientSecret -> (string)

The client secret used by the OAuth client to authenticate to the authorization server.

accessToken -> (string)

The access token used to access the connector on your behalf.

refreshToken -> (string)

The refresh token used to refresh an expired access token.

oAuthRequest -> (structure)

Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

authCode -> (string)

The code provided by the connector when it has been authenticated via the connected app.

redirectUri -> (string)

The URL to which the authentication server redirects the browser after authorization has been granted.

apiKey -> (structure)

The API keys required for the authentication of the user.

apiKey -> (string)

The API key required for API key authentication.

apiSecretKey -> (string)

The API secret key required for API key authentication.

custom -> (structure)

If the connector uses the custom authentication mechanism, this holds the required credentials.

customAuthenticationType -> (string)

The custom authentication type that the connector uses.

credentialsMap -> (map)

A map that holds custom authentication credentials.

key -> (string)

value -> (string)

Pardot -> (structure)

The connector-specific credentials required when using Salesforce Pardot.

accessToken -> (string)

The credentials used to access protected Salesforce Pardot resources.

refreshToken -> (string)

The credentials used to acquire new access tokens.

oAuthRequest -> (structure)

Used by select connectors for which the OAuth workflow is supported, such as Salesforce, Google Analytics, Marketo, Zendesk, and Slack.

authCode -> (string)

The code provided by the connector when it has been authenticated via the connected app.

redirectUri -> (string)

The URL to which the authentication server redirects the browser after authorization has been granted.

clientCredentialsArn -> (string)

The secret manager ARN, which contains the client ID and client secret of the connected app.

JSON Syntax:

```
{
  "connectorProfileProperties": {
    "Amplitude": {

    },
    "Datadog": {
      "instanceUrl": "string"
    },
    "Dynatrace": {
      "instanceUrl": "string"
    },
    "GoogleAnalytics": {

    },
    "Honeycode": {

    },
    "InforNexus": {
      "instanceUrl": "string"
    },
    "Marketo": {
      "instanceUrl": "string"
    },
    "Redshift": {
      "databaseUrl": "string",
      "bucketName": "string",
      "bucketPrefix": "string",
      "roleArn": "string",
      "dataApiRoleArn": "string",
      "isRedshiftServerless": true|false,
      "clusterIdentifier": "string",
      "workgroupName": "string",
      "databaseName": "string"
    },
    "Salesforce": {
      "instanceUrl": "string",
      "isSandboxEnvironment": true|false,
      "usePrivateLinkForMetadataAndAuthorization": true|false
    },
    "ServiceNow": {
      "instanceUrl": "string"
    },
    "Singular": {

    },
    "Slack": {
      "instanceUrl": "string"
    },
    "Snowflake": {
      "warehouse": "string",
      "stage": "string",
      "bucketName": "string",
      "bucketPrefix": "string",
      "privateLinkServiceName": "string",
      "accountName": "string",
      "region": "string"
    },
    "Trendmicro": {

    },
    "Veeva": {
      "instanceUrl": "string"
    },
    "Zendesk": {
      "instanceUrl": "string"
    },
    "SAPOData": {
      "applicationHostUrl": "string",
      "applicationServicePath": "string",
      "portNumber": integer,
      "clientNumber": "string",
      "logonLanguage": "string",
      "privateLinkServiceName": "string",
      "oAuthProperties": {
        "tokenUrl": "string",
        "authCodeUrl": "string",
        "oAuthScopes": ["string", ...]
      },
      "disableSSO": true|false
    },
    "CustomConnector": {
      "profileProperties": {"string": "string"
        ...},
      "oAuth2Properties": {
        "tokenUrl": "string",
        "oAuth2GrantType": "CLIENT_CREDENTIALS"|"AUTHORIZATION_CODE"|"JWT_BEARER",
        "tokenUrlCustomProperties": {"string": "string"
          ...}
      }
    },
    "Pardot": {
      "instanceUrl": "string",
      "isSandboxEnvironment": true|false,
      "businessUnitId": "string"
    }
  },
  "connectorProfileCredentials": {
    "Amplitude": {
      "apiKey": "string",
      "secretKey": "string"
    },
    "Datadog": {
      "apiKey": "string",
      "applicationKey": "string"
    },
    "Dynatrace": {
      "apiToken": "string"
    },
    "GoogleAnalytics": {
      "clientId": "string",
      "clientSecret": "string",
      "accessToken": "string",
      "refreshToken": "string",
      "oAuthRequest": {
        "authCode": "string",
        "redirectUri": "string"
      }
    },
    "Honeycode": {
      "accessToken": "string",
      "refreshToken": "string",
      "oAuthRequest": {
        "authCode": "string",
        "redirectUri": "string"
      }
    },
    "InforNexus": {
      "accessKeyId": "string",
      "userId": "string",
      "secretAccessKey": "string",
      "datakey": "string"
    },
    "Marketo": {
      "clientId": "string",
      "clientSecret": "string",
      "accessToken": "string",
      "oAuthRequest": {
        "authCode": "string",
        "redirectUri": "string"
      }
    },
    "Redshift": {
      "username": "string",
      "password": "string"
    },
    "Salesforce": {
      "accessToken": "string",
      "refreshToken": "string",
      "oAuthRequest": {
        "authCode": "string",
        "redirectUri": "string"
      },
      "clientCredentialsArn": "string",
      "oAuth2GrantType": "CLIENT_CREDENTIALS"|"AUTHORIZATION_CODE"|"JWT_BEARER",
      "jwtToken": "string"
    },
    "ServiceNow": {
      "username": "string",
      "password": "string",
      "oAuth2Credentials": {
        "clientId": "string",
        "clientSecret": "string",
        "accessToken": "string",
        "refreshToken": "string",
        "oAuthRequest": {
          "authCode": "string",
          "redirectUri": "string"
        }
      }
    },
    "Singular": {
      "apiKey": "string"
    },
    "Slack": {
      "clientId": "string",
      "clientSecret": "string",
      "accessToken": "string",
      "oAuthRequest": {
        "authCode": "string",
        "redirectUri": "string"
      }
    },
    "Snowflake": {
      "username": "string",
      "password": "string"
    },
    "Trendmicro": {
      "apiSecretKey": "string"
    },
    "Veeva": {
      "username": "string",
      "password": "string"
    },
    "Zendesk": {
      "clientId": "string",
      "clientSecret": "string",
      "accessToken": "string",
      "oAuthRequest": {
        "authCode": "string",
        "redirectUri": "string"
      }
    },
    "SAPOData": {
      "basicAuthCredentials": {
        "username": "string",
        "password": "string"
      },
      "oAuthCredentials": {
        "clientId": "string",
        "clientSecret": "string",
        "accessToken": "string",
        "refreshToken": "string",
        "oAuthRequest": {
          "authCode": "string",
          "redirectUri": "string"
        }
      }
    },
    "CustomConnector": {
      "authenticationType": "OAUTH2"|"APIKEY"|"BASIC"|"CUSTOM",
      "basic": {
        "username": "string",
        "password": "string"
      },
      "oauth2": {
        "clientId": "string",
        "clientSecret": "string",
        "accessToken": "string",
        "refreshToken": "string",
        "oAuthRequest": {
          "authCode": "string",
          "redirectUri": "string"
        }
      },
      "apiKey": {
        "apiKey": "string",
        "apiSecretKey": "string"
      },
      "custom": {
        "customAuthenticationType": "string",
        "credentialsMap": {"string": "string"
          ...}
      }
    },
    "Pardot": {
      "accessToken": "string",
      "refreshToken": "string",
      "oAuthRequest": {
        "authCode": "string",
        "redirectUri": "string"
      },
      "clientCredentialsArn": "string"
    }
  }
}
```

`--client-token` (string)

The `clientToken` parameter is an idempotency token. It ensures that your `CreateConnectorProfile` request completes only once. You choose the value to pass. For example, if you donât receive a response from your request, you can safely retry the request with the same `clientToken` parameter value.

If you omit a `clientToken` value, the Amazon Web Services SDK that you are using inserts a value for you. This way, the SDK can safely retry requests multiple times after a network error. You must provide your own value for other use cases.

If you specify input parameters that differ from your first request, an error occurs. If you use a different value for `clientToken` , Amazon AppFlow considers it a new call to `CreateConnectorProfile` . The token is active for 8 hours.

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

connectorProfileArn -> (string)

The Amazon Resource Name (ARN) of the connector profile.