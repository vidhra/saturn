# get-connectionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-connections.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/get-connections.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# get-connections

## Description

Retrieves a list of connection definitions from the Data Catalog.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/GetConnections)

`get-connections` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ConnectionList`

## Synopsis

```
get-connections
[--catalog-id <value>]
[--filter <value>]
[--hide-password | --no-hide-password]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

The ID of the Data Catalog in which the connections reside. If none is provided, the Amazon Web Services account ID is used by default.

`--filter` (structure)

A filter that controls which connections are returned.

MatchCriteria -> (list)

A criteria string that must match the criteria recorded in the connection definition for that connection definition to be returned.

(string)

ConnectionType -> (string)

The type of connections to return. Currently, SFTP is not supported.

ConnectionSchemaVersion -> (integer)

Denotes if the connection was created with schema version 1 or 2.

Shorthand Syntax:

```
MatchCriteria=string,string,ConnectionType=string,ConnectionSchemaVersion=integer
```

JSON Syntax:

```
{
  "MatchCriteria": ["string", ...],
  "ConnectionType": "JDBC"|"SFTP"|"MONGODB"|"KAFKA"|"NETWORK"|"MARKETPLACE"|"CUSTOM"|"SALESFORCE"|"VIEW_VALIDATION_REDSHIFT"|"VIEW_VALIDATION_ATHENA"|"GOOGLEADS"|"GOOGLESHEETS"|"GOOGLEANALYTICS4"|"SERVICENOW"|"MARKETO"|"SAPODATA"|"ZENDESK"|"JIRACLOUD"|"NETSUITEERP"|"HUBSPOT"|"FACEBOOKADS"|"INSTAGRAMADS"|"ZOHOCRM"|"SALESFORCEPARDOT"|"SALESFORCEMARKETINGCLOUD"|"SLACK"|"STRIPE"|"INTERCOM"|"SNAPCHATADS",
  "ConnectionSchemaVersion": integer
}
```

`--hide-password` | `--no-hide-password` (boolean)

Allows you to retrieve the connection metadata without returning the password. For instance, the Glue console uses this flag to retrieve the connection, and does not display the password. Set this parameter when the caller might not have permission to use the KMS key to decrypt the password, but it does have permission to access the rest of the connection properties.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

ConnectionList -> (list)

A list of requested connection definitions.

(structure)

Defines a connection to a data source.

Name -> (string)

The name of the connection definition.

Description -> (string)

The description of the connection.

ConnectionType -> (string)

The type of the connection. Currently, SFTP is not supported.

MatchCriteria -> (list)

A list of criteria that can be used in selecting this connection.

(string)

ConnectionProperties -> (map)

These key-value pairs define parameters for the connection when using the version 1 Connection schema:

- `HOST` - The host URI: either the fully qualified domain name (FQDN) or the IPv4 address of the database host.
- `PORT` - The port number, between 1024 and 65535, of the port on which the database host is listening for database connections.
- `USER_NAME` - The name under which to log in to the database. The value string for `USER_NAME` is â`USERNAME` â.
- `PASSWORD` - A password, if one is used, for the user name.
- `ENCRYPTED_PASSWORD` - When you enable connection password protection by setting `ConnectionPasswordEncryption` in the Data Catalog encryption settings, this field stores the encrypted password.
- `JDBC_DRIVER_JAR_URI` - The Amazon Simple Storage Service (Amazon S3) path of the JAR file that contains the JDBC driver to use.
- `JDBC_DRIVER_CLASS_NAME` - The class name of the JDBC driver to use.
- `JDBC_ENGINE` - The name of the JDBC engine to use.
- `JDBC_ENGINE_VERSION` - The version of the JDBC engine to use.
- `CONFIG_FILES` - (Reserved for future use.)
- `INSTANCE_ID` - The instance ID to use.
- `JDBC_CONNECTION_URL` - The URL for connecting to a JDBC data source.
- `JDBC_ENFORCE_SSL` - A Boolean string (true, false) specifying whether Secure Sockets Layer (SSL) with hostname matching is enforced for the JDBC connection on the client. The default is false.
- `CUSTOM_JDBC_CERT` - An Amazon S3 location specifying the customerâs root certificate. Glue uses this root certificate to validate the customerâs certificate when connecting to the customer database. Glue only handles X.509 certificates. The certificate provided must be DER-encoded and supplied in Base64 encoding PEM format.
- `SKIP_CUSTOM_JDBC_CERT_VALIDATION` - By default, this is `false` . Glue validates the Signature algorithm and Subject Public Key Algorithm for the customer certificate. The only permitted algorithms for the Signature algorithm are SHA256withRSA, SHA384withRSA or SHA512withRSA. For the Subject Public Key Algorithm, the key length must be at least 2048. You can set the value of this property to `true` to skip Glueâs validation of the customer certificate.
- `CUSTOM_JDBC_CERT_STRING` - A custom JDBC certificate string which is used for domain match or distinguished name match to prevent a man-in-the-middle attack. In Oracle database, this is used as the `SSL_SERVER_CERT_DN` ; in Microsoft SQL Server, this is used as the `hostNameInCertificate` .
- `CONNECTION_URL` - The URL for connecting to a general (non-JDBC) data source.
- `SECRET_ID` - The secret ID used for the secret manager of credentials.
- `CONNECTOR_URL` - The connector URL for a MARKETPLACE or CUSTOM connection.
- `CONNECTOR_TYPE` - The connector type for a MARKETPLACE or CUSTOM connection.
- `CONNECTOR_CLASS_NAME` - The connector class name for a MARKETPLACE or CUSTOM connection.
- `KAFKA_BOOTSTRAP_SERVERS` - A comma-separated list of host and port pairs that are the addresses of the Apache Kafka brokers in a Kafka cluster to which a Kafka client will connect to and bootstrap itself.
- `KAFKA_SSL_ENABLED` - Whether to enable or disable SSL on an Apache Kafka connection. Default value is âtrueâ.
- `KAFKA_CUSTOM_CERT` - The Amazon S3 URL for the private CA cert file (.pem format). The default is an empty string.
- `KAFKA_SKIP_CUSTOM_CERT_VALIDATION` - Whether to skip the validation of the CA cert file or not. Glue validates for three algorithms: SHA256withRSA, SHA384withRSA and SHA512withRSA. Default value is âfalseâ.
- `KAFKA_CLIENT_KEYSTORE` - The Amazon S3 location of the client keystore file for Kafka client side authentication (Optional).
- `KAFKA_CLIENT_KEYSTORE_PASSWORD` - The password to access the provided keystore (Optional).
- `KAFKA_CLIENT_KEY_PASSWORD` - A keystore can consist of multiple keys, so this is the password to access the client key to be used with the Kafka server side key (Optional).
- `ENCRYPTED_KAFKA_CLIENT_KEYSTORE_PASSWORD` - The encrypted version of the Kafka client keystore password (if the user has the Glue encrypt passwords setting selected).
- `ENCRYPTED_KAFKA_CLIENT_KEY_PASSWORD` - The encrypted version of the Kafka client key password (if the user has the Glue encrypt passwords setting selected).
- `KAFKA_SASL_MECHANISM` - `"SCRAM-SHA-512"` , `"GSSAPI"` , `"AWS_MSK_IAM"` , or `"PLAIN"` . These are the supported [SASL Mechanisms](https://www.iana.org/assignments/sasl-mechanisms/sasl-mechanisms.xhtml) .
- `KAFKA_SASL_PLAIN_USERNAME` - A plaintext username used to authenticate with the âPLAINâ mechanism.
- `KAFKA_SASL_PLAIN_PASSWORD` - A plaintext password used to authenticate with the âPLAINâ mechanism.
- `ENCRYPTED_KAFKA_SASL_PLAIN_PASSWORD` - The encrypted version of the Kafka SASL PLAIN password (if the user has the Glue encrypt passwords setting selected).
- `KAFKA_SASL_SCRAM_USERNAME` - A plaintext username used to authenticate with the âSCRAM-SHA-512â mechanism.
- `KAFKA_SASL_SCRAM_PASSWORD` - A plaintext password used to authenticate with the âSCRAM-SHA-512â mechanism.
- `ENCRYPTED_KAFKA_SASL_SCRAM_PASSWORD` - The encrypted version of the Kafka SASL SCRAM password (if the user has the Glue encrypt passwords setting selected).
- `KAFKA_SASL_SCRAM_SECRETS_ARN` - The Amazon Resource Name of a secret in Amazon Web Services Secrets Manager.
- `KAFKA_SASL_GSSAPI_KEYTAB` - The S3 location of a Kerberos `keytab` file. A keytab stores long-term keys for one or more principals. For more information, see [MIT Kerberos Documentation: Keytab](https://web.mit.edu/kerberos/krb5-latest/doc/basic/keytab_def.html) .
- `KAFKA_SASL_GSSAPI_KRB5_CONF` - The S3 location of a Kerberos `krb5.conf` file. A krb5.conf stores Kerberos configuration information, such as the location of the KDC server. For more information, see [MIT Kerberos Documentation: krb5.conf](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html) .
- `KAFKA_SASL_GSSAPI_SERVICE` - The Kerberos service name, as set with `sasl.kerberos.service.name` in your [Kafka Configuration](https://kafka.apache.org/documentation/#brokerconfigs_sasl.kerberos.service.name) .
- `KAFKA_SASL_GSSAPI_PRINCIPAL` - The name of the Kerberos princial used by Glue. For more information, see [Kafka Documentation: Configuring Kafka Brokers](https://kafka.apache.org/documentation/#security_sasl_kerberos_clientconfig) .
- `ROLE_ARN` - The role to be used for running queries.
- `REGION` - The Amazon Web Services Region where queries will be run.
- `WORKGROUP_NAME` - The name of an Amazon Redshift serverless workgroup or Amazon Athena workgroup in which queries will run.
- `CLUSTER_IDENTIFIER` - The cluster identifier of an Amazon Redshift cluster in which queries will run.
- `DATABASE` - The Amazon Redshift database that you are connecting to.

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

The physical connection requirements, such as virtual private cloud (VPC) and `SecurityGroup` , that are needed to make this connection successfully.

SubnetId -> (string)

The subnet ID used by the connection.

SecurityGroupIdList -> (list)

The security group ID list used by the connection.

(string)

AvailabilityZone -> (string)

The connectionâs Availability Zone.

CreationTime -> (timestamp)

The timestamp of the time that this connection definition was created.

LastUpdatedTime -> (timestamp)

The timestamp of the last time the connection definition was updated.

LastUpdatedBy -> (string)

The user, group, or role that last updated this connection definition.

Status -> (string)

The status of the connection. Can be one of: `READY` , `IN_PROGRESS` , or `FAILED` .

StatusReason -> (string)

The reason for the connection status.

LastConnectionValidationTime -> (timestamp)

A timestamp of the time this connection was last validated.

AuthenticationConfiguration -> (structure)

The authentication properties of the connection.

AuthenticationType -> (string)

A structure containing the authentication configuration.

SecretArn -> (string)

The secret manager ARN to store credentials.

OAuth2Properties -> (structure)

The properties for OAuth2 authentication.

OAuth2GrantType -> (string)

The OAuth2 grant type. For example, `AUTHORIZATION_CODE` , `JWT_BEARER` , or `CLIENT_CREDENTIALS` .

OAuth2ClientApplication -> (structure)

The client application type. For example, AWS_MANAGED or USER_MANAGED.

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

ConnectionSchemaVersion -> (integer)

The version of the connection schema for this connection. Version 2 supports properties for specific compute environments.

CompatibleComputeEnvironments -> (list)

A list of compute environments compatible with the connection.

(string)

NextToken -> (string)

A continuation token, if the list of connections returned does not include the last of the filtered connections.