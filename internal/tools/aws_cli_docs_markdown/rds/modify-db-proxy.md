# modify-db-proxyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-proxy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-proxy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# modify-db-proxy

## Description

Changes the settings for an existing DB proxy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/ModifyDBProxy)

## Synopsis

```
modify-db-proxy
--db-proxy-name <value>
[--new-db-proxy-name <value>]
[--auth <value>]
[--require-tls | --no-require-tls]
[--idle-client-timeout <value>]
[--debug-logging | --no-debug-logging]
[--role-arn <value>]
[--security-groups <value>]
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

`--db-proxy-name` (string)

The identifier for the `DBProxy` to modify.

`--new-db-proxy-name` (string)

The new identifier for the `DBProxy` . An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it canât end with a hyphen or contain two consecutive hyphens.

`--auth` (list)

The new authentication settings for the `DBProxy` .

(structure)

Specifies the details of authentication used by a proxy to log in as a specific database user.

Description -> (string)

A user-specified description about the authentication used by a proxy to log in as a specific database user.

UserName -> (string)

The name of the database user to which the proxy connects.

AuthScheme -> (string)

The type of authentication that the proxy uses for connections from the proxy to the underlying database.

SecretArn -> (string)

The Amazon Resource Name (ARN) representing the secret that the proxy uses to authenticate to the RDS DB instance or Aurora DB cluster. These secrets are stored within Amazon Secrets Manager.

IAMAuth -> (string)

A value that indicates whether to require or disallow Amazon Web Services Identity and Access Management (IAM) authentication for connections to the proxy. The `ENABLED` value is valid only for proxies with RDS for Microsoft SQL Server.

ClientPasswordAuthType -> (string)

The type of authentication the proxy uses for connections from clients. The following values are defaults for the corresponding engines:

- RDS for MySQL: `MYSQL_CACHING_SHA2_PASSWORD`
- RDS for SQL Server: `SQL_SERVER_AUTHENTICATION`
- RDS for PostgreSQL: `POSTGRES_SCRAM_SHA2_256`

Shorthand Syntax:

```
Description=string,UserName=string,AuthScheme=string,SecretArn=string,IAMAuth=string,ClientPasswordAuthType=string ...
```

JSON Syntax:

```
[
  {
    "Description": "string",
    "UserName": "string",
    "AuthScheme": "SECRETS",
    "SecretArn": "string",
    "IAMAuth": "DISABLED"|"REQUIRED"|"ENABLED",
    "ClientPasswordAuthType": "MYSQL_NATIVE_PASSWORD"|"MYSQL_CACHING_SHA2_PASSWORD"|"POSTGRES_SCRAM_SHA_256"|"POSTGRES_MD5"|"SQL_SERVER_AUTHENTICATION"
  }
  ...
]
```

`--require-tls` | `--no-require-tls` (boolean)

Whether Transport Layer Security (TLS) encryption is required for connections to the proxy. By enabling this setting, you can enforce encrypted TLS connections to the proxy, even if the associated database doesnât use TLS.

`--idle-client-timeout` (integer)

The number of seconds that a connection to the proxy can be inactive before the proxy disconnects it. You can set this value higher or lower than the connection timeout limit for the associated database.

`--debug-logging` | `--no-debug-logging` (boolean)

Whether the proxy includes detailed information about SQL statements in its logs. This information helps you to debug issues involving SQL behavior or the performance and scalability of the proxy connections. The debug information includes the text of SQL statements that you submit through the proxy. Thus, only enable this setting when needed for debugging, and only when you have security measures in place to safeguard any sensitive information that appears in the logs.

`--role-arn` (string)

The Amazon Resource Name (ARN) of the IAM role that the proxy uses to access secrets in Amazon Web Services Secrets Manager.

`--security-groups` (list)

The new list of security groups for the `DBProxy` .

(string)

Syntax:

```
"string" "string" ...
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To modify a DB proxy for an RDS database**

The following `modify-db-proxy` example modifies a DB proxy named `proxyExample` to require SSL for its connections.

```
aws rds modify-db-proxy \
    --db-proxy-name proxyExample \
    --require-tls
```

Output:

```
{
"DBProxy":
    {
        "DBProxyName": "proxyExample",
        "DBProxyArn": "arn:aws:rds:us-east-1:123456789012:db-proxy:prx-0123a01b12345c0ab",
        "Status": "modifying"
        "EngineFamily": "PostgreSQL",
        "VpcId": "sg-1234567",
        "VpcSecurityGroupIds": [
            "sg-1234"
        ],
        "VpcSubnetIds": [
            "subnetgroup1",
            "subnetgroup2"
        ],
        "Auth": "[
            {
                "Description": "proxydescription1",
                "AuthScheme": "SECRETS",
                "SecretArn": "arn:aws:secretsmanager:us-west-2:123456789123:secret:proxysecret1-Abcd1e",
                "IAMAuth": "DISABLED"
            }
        ]",
        "RoleArn": "arn:aws:iam::12345678912:role/ProxyPostgreSQLRole",
        "Endpoint": "proxyExample.proxy-ab0cd1efghij.us-east-1.rds.amazonaws.com",
        "RequireTLS": true,
        "IdleClientTimeout": 1800,
        "DebuggingLogging": false,
        "CreatedDate": "2023-04-05T16:09:33.452000+00:00",
        "UpdatedDate": "2023-04-13T01:49:38.568000+00:00"
    }
}
```

For more information, see [Modify an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html#rds-proxy-modifying-proxy) in the *Amazon RDS User Guide* and [Creating an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-managing.html#rds-proxy-modifying-proxy) in the *Amazon Aurora User Guide*.

## Output

DBProxy -> (structure)

The `DBProxy` object representing the new settings for the proxy.

DBProxyName -> (string)

The identifier for the proxy. This name must be unique for all proxies owned by your Amazon Web Services account in the specified Amazon Web Services Region.

DBProxyArn -> (string)

The Amazon Resource Name (ARN) for the proxy.

Status -> (string)

The current status of this proxy. A status of `available` means the proxy is ready to handle requests. Other values indicate that you must wait for the proxy to be ready, or take some action to resolve an issue.

EngineFamily -> (string)

The kinds of databases that the proxy can connect to. This value determines which database network protocol the proxy recognizes when it interprets network traffic to and from the database. `MYSQL` supports Aurora MySQL, RDS for MariaDB, and RDS for MySQL databases. `POSTGRESQL` supports Aurora PostgreSQL and RDS for PostgreSQL databases. `SQLSERVER` supports RDS for Microsoft SQL Server databases.

VpcId -> (string)

Provides the VPC ID of the DB proxy.

VpcSecurityGroupIds -> (list)

Provides a list of VPC security groups that the proxy belongs to.

(string)

VpcSubnetIds -> (list)

The EC2 subnet IDs for the proxy.

(string)

Auth -> (list)

One or more data structures specifying the authorization mechanism to connect to the associated RDS DB instance or Aurora DB cluster.

(structure)

Returns the details of authentication used by a proxy to log in as a specific database user.

Description -> (string)

A user-specified description about the authentication used by a proxy to log in as a specific database user.

UserName -> (string)

The name of the database user to which the proxy connects.

AuthScheme -> (string)

The type of authentication that the proxy uses for connections from the proxy to the underlying database.

SecretArn -> (string)

The Amazon Resource Name (ARN) representing the secret that the proxy uses to authenticate to the RDS DB instance or Aurora DB cluster. These secrets are stored within Amazon Secrets Manager.

IAMAuth -> (string)

Whether to require or disallow Amazon Web Services Identity and Access Management (IAM) authentication for connections to the proxy.

ClientPasswordAuthType -> (string)

The type of authentication the proxy uses for connections from clients.

RoleArn -> (string)

The Amazon Resource Name (ARN) for the IAM role that the proxy uses to access Amazon Secrets Manager.

Endpoint -> (string)

The endpoint that you can use to connect to the DB proxy. You include the endpoint value in the connection string for a database client application.

RequireTLS -> (boolean)

Indicates whether Transport Layer Security (TLS) encryption is required for connections to the proxy.

IdleClientTimeout -> (integer)

The number of seconds a connection to the proxy can have no activity before the proxy drops the client connection. The proxy keeps the underlying database connection open and puts it back into the connection pool for reuse by later connection requests.

Default: 1800 (30 minutes)

Constraints: 1 to 28,800

DebugLogging -> (boolean)

Indicates whether the proxy includes detailed information about SQL statements in its logs. This information helps you to debug issues involving SQL behavior or the performance and scalability of the proxy connections. The debug information includes the text of SQL statements that you submit through the proxy. Thus, only enable this setting when needed for debugging, and only when you have security measures in place to safeguard any sensitive information that appears in the logs.

CreatedDate -> (timestamp)

The date and time when the proxy was first created.

UpdatedDate -> (timestamp)

The date and time when the proxy was last updated.