# update-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# update-connection

## Description

Updates a connection definition in the Data Catalog.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateConnection)

## Synopsis

```
update-connection
[--catalog-id <value>]
--name <value>
--connection-input <value>
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

`--catalog-id` (string)

The ID of the Data Catalog in which the connection resides. If none is provided, the Amazon Web Services account ID is used by default.

`--name` (string)

The name of the connection definition to update.

`--connection-input` (structure)

A `ConnectionInput` object that redefines the connection in question.

Name -> (string)

The name of the connection.

Description -> (string)

The description of the connection.

ConnectionType -> (string)

The type of the connection. Currently, these types are supported:

- `JDBC` - Designates a connection to a database through Java Database Connectivity (JDBC).  `JDBC` Connections use the following ConnectionParameters.
- Required: All of (`HOST` , `PORT` , `JDBC_ENGINE` ) or `JDBC_CONNECTION_URL` .
- Required: All of (`USERNAME` , `PASSWORD` ) or `SECRET_ID` .
- Optional: `JDBC_ENFORCE_SSL` , `CUSTOM_JDBC_CERT` , `CUSTOM_JDBC_CERT_STRING` , `SKIP_CUSTOM_JDBC_CERT_VALIDATION` . These parameters are used to configure SSL with JDBC.
- `KAFKA` - Designates a connection to an Apache Kafka streaming platform.  `KAFKA` Connections use the following ConnectionParameters.
- Required: `KAFKA_BOOTSTRAP_SERVERS` .
- Optional: `KAFKA_SSL_ENABLED` , `KAFKA_CUSTOM_CERT` , `KAFKA_SKIP_CUSTOM_CERT_VALIDATION` . These parameters are used to configure SSL with `KAFKA` .
- Optional: `KAFKA_CLIENT_KEYSTORE` , `KAFKA_CLIENT_KEYSTORE_PASSWORD` , `KAFKA_CLIENT_KEY_PASSWORD` , `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD` , `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD` . These parameters are used to configure TLS client configuration with SSL in `KAFKA` .
- Optional: `KAFKA_SASL_MECHANISM` . Can be specified as `SCRAM-SHA-512` , `GSSAPI` , or `AWS_MSK_IAM` .
- Optional: `KAFKA_SASL_SCRAM_USERNAME` , `KAFKA_SASL_SCRAM_PASSWORD` , `ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD` . These parameters are used to configure SASL/SCRAM-SHA-512 authentication with `KAFKA` .
- Optional: `KAFKA_SASL_GSSAPI_KEYTAB` , `KAFKA_SASL_GSSAPI_KRB5_CONF` , `KAFKA_SASL_GSSAPI_SERVICE` , `KAFKA_SASL_GSSAPI_PRINCIPAL` . These parameters are used to configure SASL/GSSAPI authentication with `KAFKA` .
- `MONGODB` - Designates a connection to a MongoDB document database.  `MONGODB` Connections use the following ConnectionParameters.
- Required: `CONNECTION_URL` .
- Required: All of (`USERNAME` , `PASSWORD` ) or `SECRET_ID` .
- `VIEW_VALIDATION_REDSHIFT` - Designates a connection used for view validation by Amazon Redshift.
- `VIEW_VALIDATION_ATHENA` - Designates a connection used for view validation by Amazon Athena.
- `NETWORK` - Designates a network connection to a data source within an Amazon Virtual Private Cloud environment (Amazon VPC).  `NETWORK` Connections do not require ConnectionParameters. Instead, provide a PhysicalConnectionRequirements.
- `MARKETPLACE` - Uses configuration settings contained in a connector purchased from Amazon Web Services Marketplace to read from and write to data stores that are not natively supported by Glue.  `MARKETPLACE` Connections use the following ConnectionParameters.
- Required: `CONNECTOR_TYPE` , `CONNECTOR_URL` , `CONNECTOR_CLASS_NAME` , `CONNECTION_URL` .
- Required for `JDBC` `CONNECTOR_TYPE` connections: All of (`USERNAME` , `PASSWORD` ) or `SECRET_ID` .
- `CUSTOM` - Uses configuration settings contained in a custom connector to read from and write to data stores that are not natively supported by Glue.

Additionally, a `ConnectionType` for the following SaaS connectors is supported:

- `FACEBOOKADS` - Designates a connection to Facebook Ads.
- `GOOGLEADS` - Designates a connection to Google Ads.
- `GOOGLESHEETS` - Designates a connection to Google Sheets.
- `GOOGLEANALYTICS4` - Designates a connection to Google Analytics 4.
- `HUBSPOT` - Designates a connection to HubSpot.
- `INSTAGRAMADS` - Designates a connection to Instagram Ads.
- `INTERCOM` - Designates a connection to Intercom.
- `JIRACLOUD` - Designates a connection to Jira Cloud.
- `MARKETO` - Designates a connection to Adobe Marketo Engage.
- `NETSUITEERP` - Designates a connection to Oracle NetSuite.
- `SALESFORCE` - Designates a connection to Salesforce using OAuth authentication.
- `SALESFORCEMARKETINGCLOUD` - Designates a connection to Salesforce Marketing Cloud.
- `SALESFORCEPARDOT` - Designates a connection to Salesforce Marketing Cloud Account Engagement (MCAE).
- `SAPODATA` - Designates a connection to SAP OData.
- `SERVICENOW` - Designates a connection to ServiceNow.
- `SLACK` - Designates a connection to Slack.
- `SNAPCHATADS` - Designates a connection to Snapchat Ads.
- `STRIPE` - Designates a connection to Stripe.
- `ZENDESK` - Designates a connection to Zendesk.
- `ZOHOCRM` - Designates a connection to Zoho CRM.

For more information on the connection parameters needed for a particular connector, see the documentation for the connector in [Adding an Glue connection](https://docs.aws.amazon.com/glue/latest/dg/console-connections.html) in the Glue User Guide.

`SFTP` is not supported.

For more information about how optional ConnectionProperties are used to configure features in Glue, consult [Glue connection properties](https://docs.aws.amazon.com/glue/latest/dg/connection-defining.html) .

For more information about how optional ConnectionProperties are used to configure features in Glue Studio, consult [Using connectors and connections](https://docs.aws.amazon.com/glue/latest/ug/connectors-chapter.html) .

MatchCriteria -> (list)

A list of criteria that can be used in selecting this connection.

(string)

ConnectionProperties -> (map)

These key-value pairs define parameters for the connection.

key -> (string)

value -> (string)

SparkProperties -> (map)

Connection properties specific to the Spark compute environment.

key -> (string)

value -> (string)

AthenaProperties -> (map)

Connection properties specific to the Athena compute environment.

key -> (string)

value -> (string)

PythonProperties -> (map)

Connection properties specific to the Python compute environment.

key -> (string)

value -> (string)

PhysicalConnectionRequirements -> (structure)

The physical connection requirements, such as virtual private cloud (VPC) and `SecurityGroup` , that are needed to successfully make this connection.

SubnetId -> (string)

The subnet ID used by the connection.

SecurityGroupIdList -> (list)

The security group ID list used by the connection.

(string)

AvailabilityZone -> (string)

The connectionâs Availability Zone.

AuthenticationConfiguration -> (structure)

The authentication properties of the connection.

AuthenticationType -> (string)

A structure containing the authentication configuration in the CreateConnection request.

OAuth2Properties -> (structure)

The properties for OAuth2 authentication in the CreateConnection request.

OAuth2GrantType -> (string)

The OAuth2 grant type in the CreateConnection request. For example, `AUTHORIZATION_CODE` , `JWT_BEARER` , or `CLIENT_CREDENTIALS` .

OAuth2ClientApplication -> (structure)

The client application type in the CreateConnection request. For example, `AWS_MANAGED` or `USER_MANAGED` .

UserManagedClientApplicationClientId -> (string)

The client application clientID if the ClientAppType is `USER_MANAGED` .

AWSManagedClientApplicationReference -> (string)

The reference to the SaaS-side client app that is Amazon Web Services managed.

TokenUrl -> (string)

The URL of the providerâs authentication server, to exchange an authorization code for an access token.

TokenUrlParametersMap -> (map)

A map of parameters that are added to the token `GET` request.

key -> (string)

value -> (string)

AuthorizationCodeProperties -> (structure)

The set of properties required for the the OAuth2 `AUTHORIZATION_CODE` grant type.

AuthorizationCode -> (string)

An authorization code to be used in the third leg of the `AUTHORIZATION_CODE` grant workflow. This is a single-use code which becomes invalid once exchanged for an access token, thus it is acceptable to have this value as a request parameter.

RedirectUri -> (string)

The redirect URI where the user gets redirected to by authorization server when issuing an authorization code. The URI is subsequently used when the authorization code is exchanged for an access token.

OAuth2Credentials -> (structure)

The credentials used when the authentication type is OAuth2 authentication.

UserManagedClientApplicationClientSecret -> (string)

The client application client secret if the client application is user managed.

AccessToken -> (string)

The access token used when the authentication type is OAuth2.

RefreshToken -> (string)

The refresh token used when the authentication type is OAuth2.

JwtToken -> (string)

The JSON Web Token (JWT) used when the authentication type is OAuth2.

SecretArn -> (string)

The secret manager ARN to store credentials in the CreateConnection request.

KmsKeyArn -> (string)

The ARN of the KMS key used to encrypt the connection. Only taken an as input in the request and stored in the Secret Manager.

BasicAuthenticationCredentials -> (structure)

The credentials used when the authentication type is basic authentication.

Username -> (string)

The username to connect to the data source.

Password -> (string)

The password to connect to the data source.

CustomAuthenticationCredentials -> (map)

The credentials used when the authentication type is custom authentication.

key -> (string)

value -> (string)

ValidateCredentials -> (boolean)

A flag to validate the credentials during create connection. Default is true.

ValidateForComputeEnvironments -> (list)

The compute environments that the specified connection properties are validated against.

(string)

JSON Syntax:

```
{
  "Name": "string",
  "Description": "string",
  "ConnectionType": "JDBC"|"SFTP"|"MONGODB"|"KAFKA"|"NETWORK"|"MARKETPLACE"|"CUSTOM"|"SALESFORCE"|"VIEW_VALIDATION_REDSHIFT"|"VIEW_VALIDATION_ATHENA"|"GOOGLEADS"|"GOOGLESHEETS"|"GOOGLEANALYTICS4"|"SERVICENOW"|"MARKETO"|"SAPODATA"|"ZENDESK"|"JIRACLOUD"|"NETSUITEERP"|"HUBSPOT"|"FACEBOOKADS"|"INSTAGRAMADS"|"ZOHOCRM"|"SALESFORCEPARDOT"|"SALESFORCEMARKETINGCLOUD"|"SLACK"|"STRIPE"|"INTERCOM"|"SNAPCHATADS",
  "MatchCriteria": ["string", ...],
  "ConnectionProperties": {"HOST"|"PORT"|"USERNAME"|"PASSWORD"|"ENCRYPTED_PASSWORD"|"JDBC_DRIVER_JAR_URI"|"JDBC_DRIVER_CLASS_NAME"|"JDBC_ENGINE"|"JDBC_ENGINE_VERSION"|"CONFIG_FILES"|"INSTANCE_ID"|"JDBC_CONNECTION_URL"|"JDBC_ENFORCE_SSL"|"CUSTOM_JDBC_CERT"|"SKIP_CUSTOM_JDBC_CERT_VALIDATION"|"CUSTOM_JDBC_CERT_STRING"|"CONNECTION_URL"|"KAFKA_BOOTSTRAP_SERVERS"|"KAFKA_SSL_ENABLED"|"KAFKA_CUSTOM_CERT"|"KAFKA_SKIP_CUSTOM_CERT_VALIDATION"|"KAFKA_CLIENT_KEYSTORE"|"KAFKA_CLIENT_KEYSTORE_PASSWORD"|"KAFKA_CLIENT_KEY_PASSWORD"|"ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD"|"ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD"|"KAFKA_SASL_MECHANISM"|"KAFKA_SASL_PLAIN_USERNAME"|"KAFKA_SASL_PLAIN_PASSWORD"|"ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD"|"KAFKA_SASL_SCRAM_USERNAME"|"KAFKA_SASL_SCRAM_PASSWORD"|"KAFKA_SASL_SCRAM_SECRETS_ARN"|"ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD"|"KAFKA_SASL_GSSAPI_KEYTAB"|"KAFKA_SASL_GSSAPI_KRB5_CONF"|"KAFKA_SASL_GSSAPI_SERVICE"|"KAFKA_SASL_GSSAPI_PRINCIPAL"|"SECRET_ID"|"CONNECTOR_URL"|"CONNECTOR_TYPE"|"CONNECTOR_CLASS_NAME"|"ENDPOINT"|"ENDPOINT_TYPE"|"ROLE_ARN"|"REGION"|"WORKGROUP_NAME"|"CLUSTER_IDENTIFIER"|"DATABASE": "string"
    ...},
  "SparkProperties": {"string": "string"
    ...},
  "AthenaProperties": {"string": "string"
    ...},
  "PythonProperties": {"string": "string"
    ...},
  "PhysicalConnectionRequirements": {
    "SubnetId": "string",
    "SecurityGroupIdList": ["string", ...],
    "AvailabilityZone": "string"
  },
  "AuthenticationConfiguration": {
    "AuthenticationType": "BASIC"|"OAUTH2"|"CUSTOM"|"IAM",
    "OAuth2Properties": {
      "OAuth2GrantType": "AUTHORIZATION_CODE"|"CLIENT_CREDENTIALS"|"JWT_BEARER",
      "OAuth2ClientApplication": {
        "UserManagedClientApplicationClientId": "string",
        "AWSManagedClientApplicationReference": "string"
      },
      "TokenUrl": "string",
      "TokenUrlParametersMap": {"string": "string"
        ...},
      "AuthorizationCodeProperties": {
        "AuthorizationCode": "string",
        "RedirectUri": "string"
      },
      "OAuth2Credentials": {
        "UserManagedClientApplicationClientSecret": "string",
        "AccessToken": "string",
        "RefreshToken": "string",
        "JwtToken": "string"
      }
    },
    "SecretArn": "string",
    "KmsKeyArn": "string",
    "BasicAuthenticationCredentials": {
      "Username": "string",
      "Password": "string"
    },
    "CustomAuthenticationCredentials": {"string": "string"
      ...}
  },
  "ValidateCredentials": true|false,
  "ValidateForComputeEnvironments": ["SPARK"|"ATHENA"|"PYTHON", ...]
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