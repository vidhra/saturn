# get-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/get-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/get-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [datazone](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/datazone/index.html#cli-aws-datazone) ]

# get-connection

## Description

Gets a connection. In Amazon DataZone, a connection enables you to connect your resources (domains, projects, and environments) to external resources and services.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/datazone-2018-05-10/GetConnection)

## Synopsis

```
get-connection
--domain-identifier <value>
--identifier <value>
[--with-secret | --no-with-secret]
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

`--domain-identifier` (string)

The ID of the domain where we get the connection.

`--identifier` (string)

The connection ID.

`--with-secret` | `--no-with-secret` (boolean)

Specifies whether a connection has a secret.

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

connectionCredentials -> (structure)

Connection credentials.

accessKeyId -> (string)

The access key ID of a connection.

expiration -> (timestamp)

The expiration of the connection credentials.

secretAccessKey -> (string)

The secret access key of a connection.

sessionToken -> (string)

The session token of a connection credentials.

connectionId -> (string)

The ID of the connection.

description -> (string)

Connection description.

domainId -> (string)

The domain ID of the connection.

domainUnitId -> (string)

The domain unit ID of the connection.

environmentId -> (string)

The ID of the environment.

environmentUserRole -> (string)

The environment user role.

name -> (string)

The name of the connection.

physicalEndpoints -> (list)

The physical endpoints of the connection.

(structure)

The physical endpoints of a connection.

awsLocation -> (structure)

The location of a connection.

accessRole -> (string)

The access role of a connection.

awsAccountId -> (string)

The account ID of a connection.

awsRegion -> (string)

The Region of a connection.

iamConnectionId -> (string)

The IAM connection ID of a connection.

glueConnection -> (structure)

The Amazon Web Services Glue connection.

athenaProperties -> (map)

The Amazon Athena properties of the Amazon Web Services Glue connection.

key -> (string)

value -> (string)

authenticationConfiguration -> (structure)

The authentication configuration of the Amazon Web Services Glue connection.

authenticationType -> (string)

The authentication type of a connection.

oAuth2Properties -> (structure)

The oAuth2 properties of a connection.

authorizationCodeProperties -> (structure)

The authorization code properties of the OAuth2 properties.

authorizationCode -> (string)

The authorization code of a connection.

redirectUri -> (string)

The redirect URI of a connection.

oAuth2ClientApplication -> (structure)

The OAuth2 client application of the OAuth2 properties.

aWSManagedClientApplicationReference -> (string)

The Amazon Web Services managed client application reference in the OAuth2Client application.

userManagedClientApplicationClientId -> (string)

The user managed client application client ID in the OAuth2Client application.

oAuth2Credentials -> (structure)

The OAuth2 credentials of the OAuth2 properties.

accessToken -> (string)

The access token of a connection.

jwtToken -> (string)

The jwt token of the connection.

refreshToken -> (string)

The refresh token of the connection.

userManagedClientApplicationClientSecret -> (string)

The user managed client application client secret of the connection.

oAuth2GrantType -> (string)

The OAuth2 grant type of the OAuth2 properties.

tokenUrl -> (string)

The OAuth2 token URL of the OAuth2 properties.

tokenUrlParametersMap -> (map)

The OAuth2 token URL parameter map of the OAuth2 properties.

key -> (string)

value -> (string)

secretArn -> (string)

The secret ARN of a connection.

compatibleComputeEnvironments -> (list)

The compatible compute environments of the Amazon Web Services Glue connection.

(string)

connectionProperties -> (map)

The properties of the Amazon Web Services Glue connection.

key -> (string)

value -> (string)

connectionSchemaVersion -> (integer)

The connection schema version of the Amazon Web Services Glue connection.

connectionType -> (string)

The type of the Amazon Web Services Glue connection.

creationTime -> (timestamp)

The creation time of the Amazon Web Services Glue connection.

description -> (string)

The description of the Amazon Web Services Glue connection.

lastConnectionValidationTime -> (timestamp)

The last validation time of the Amazon Web Services Glue connection.

lastUpdatedBy -> (string)

The user who last updated the Amazon Web Services Glue connection.

lastUpdatedTime -> (timestamp)

The timestamp at which the Amazon Web Services Glue connection was last updated.

matchCriteria -> (list)

The match criteria of the Amazon Web Services Glue connection.

(string)

name -> (string)

The name of the Amazon Web Services Glue connection.

physicalConnectionRequirements -> (structure)

The physical connection requirements of the Amazon Web Services Glue connection.

availabilityZone -> (string)

The availability zone of the physical connection requirements of a connection.

securityGroupIdList -> (list)

The group ID list of the physical connection requirements of a connection.

(string)

subnetId -> (string)

The subnet ID of the physical connection requirements of a connection.

subnetIdList -> (list)

The subnet ID list of the physical connection requirements of a connection.

(string)

pythonProperties -> (map)

The Python properties of the Amazon Web Services Glue connection.

key -> (string)

value -> (string)

sparkProperties -> (map)

The Spark properties of the Amazon Web Services Glue connection.

key -> (string)

value -> (string)

status -> (string)

The status of the Amazon Web Services Glue connection.

statusReason -> (string)

The status reason of the Amazon Web Services Glue connection.

glueConnectionName -> (string)

The Amazon Web Services Glue connection name.

host -> (string)

The host in the physical endpoints of a connection.

port -> (integer)

The port in the physical endpoints of a connection.

protocol -> (string)

The protocol in the physical endpoints of a connection.

stage -> (string)

The stage in the physical endpoints of a connection.

projectId -> (string)

The ID of the project.

props -> (tagged union structure)

Connection props.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `athenaProperties`, `glueProperties`, `hyperPodProperties`, `iamProperties`, `redshiftProperties`, `sparkEmrProperties`, `sparkGlueProperties`.

athenaProperties -> (structure)

The Amazon Athena properties of a connection.

workgroupName -> (string)

The Amazon Athena workgroup name of a connection.

glueProperties -> (structure)

The Amazon Web Services Glue properties of a connection.

errorMessage -> (string)

The error message generated if the action is not completed successfully.

status -> (string)

The status of a connection.

hyperPodProperties -> (structure)

The hyper pod properties of a connection.

clusterArn -> (string)

The cluster ARN of the hyper pod properties.

clusterName -> (string)

The cluster name the hyper pod properties.

orchestrator -> (string)

The orchestrator of the hyper pod properties.

iamProperties -> (structure)

The IAM properties of a connection.

environmentId -> (string)

The environment ID of the connection.

glueLineageSyncEnabled -> (boolean)

Specifies whether Amazon Web Services Glue lineage sync is enabled for a connection.

redshiftProperties -> (structure)

The Amazon Redshift properties of a connection.

credentials -> (tagged union structure)

The Amazon Redshift credentials.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `secretArn`, `usernamePassword`.

secretArn -> (string)

The secret ARN of the Amazon Redshift credentials of a connection.

usernamePassword -> (structure)

The username and password of the Amazon Redshift credentials of a connection.

password -> (string)

The password of a connection.

username -> (string)

The username of a connection.

databaseName -> (string)

The Amazon Redshift database name.

isProvisionedSecret -> (boolean)

Specifies whether Amaon Redshift properties has a provisioned secret.

jdbcIamUrl -> (string)

The jdbcIam URL of the Amazon Redshift properties.

jdbcUrl -> (string)

The jdbcURL of the Amazon Redshift properties.

lineageSync -> (structure)

The lineage syn of the Amazon Redshift properties.

enabled -> (boolean)

Specifies whether the Amaon Redshift lineage sync configuration is enabled.

lineageJobId -> (string)

The lineage job ID of the Amaon Redshift lineage sync configuration.

schedule -> (structure)

The schedule of teh Amaon Redshift lineage sync configuration.

schedule -> (string)

The lineage sync schedule.

redshiftTempDir -> (string)

The redshiftTempDir of the Amazon Redshift properties.

status -> (string)

The status in the Amazon Redshift properties.

storage -> (tagged union structure)

The storage in the Amazon Redshift properties.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `clusterName`, `workgroupName`.

clusterName -> (string)

The cluster name in the Amazon Redshift storage properties.

workgroupName -> (string)

The workgroup name in the Amazon Redshift storage properties.

sparkEmrProperties -> (structure)

The Spark EMR properties of a connection.

computeArn -> (string)

The compute ARN of the Spark EMR.

credentials -> (structure)

The credentials of the Spark EMR.

password -> (string)

The password of a connection.

username -> (string)

The username of a connection.

credentialsExpiration -> (timestamp)

The credential expiration of the Spark EMR.

governanceType -> (string)

The governance type of the Spark EMR.

instanceProfileArn -> (string)

The instance profile ARN of the Spark EMR.

javaVirtualEnv -> (string)

The Java virtual env of the Spark EMR.

livyEndpoint -> (string)

The livy endpoint of the Spark EMR.

logUri -> (string)

The log URI of the Spark EMR.

pythonVirtualEnv -> (string)

The Python virtual env of the Spark EMR.

runtimeRole -> (string)

The runtime role of the Spark EMR.

trustedCertificatesS3Uri -> (string)

The trusted certificate S3 URL of the Spark EMR.

sparkGlueProperties -> (structure)

The Spark Amazon Web Services Glue properties of a connection.

additionalArgs -> (structure)

The additional args in the Spark Amazon Web Services Glue properties.

connection -> (string)

The connection in the Spark Amazon Web Services Glue args.

glueConnectionName -> (string)

The Amazon Web Services Glue connection name in the Spark Amazon Web Services Glue properties.

glueVersion -> (string)

The Amazon Web Services Glue version in the Spark Amazon Web Services Glue properties.

idleTimeout -> (integer)

The idle timeout in the Spark Amazon Web Services Glue properties.

javaVirtualEnv -> (string)

The Java virtual env in the Spark Amazon Web Services Glue properties.

numberOfWorkers -> (integer)

The number of workers in the Spark Amazon Web Services Glue properties.

pythonVirtualEnv -> (string)

The Python virtual env in the Spark Amazon Web Services Glue properties.

workerType -> (string)

The worker type in the Spark Amazon Web Services Glue properties.

type -> (string)

The type of the connection.