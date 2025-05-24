# modify-db-proxy-target-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-proxy-target-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/modify-db-proxy-target-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rds/index.html#cli-aws-rds) ]

# modify-db-proxy-target-group

## Description

Modifies the properties of a `DBProxyTargetGroup` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rds-2014-10-31/ModifyDBProxyTargetGroup)

## Synopsis

```
modify-db-proxy-target-group
--target-group-name <value>
--db-proxy-name <value>
[--connection-pool-config <value>]
[--new-name <value>]
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

`--target-group-name` (string)

The name of the target group to modify.

`--db-proxy-name` (string)

The name of the proxy.

`--connection-pool-config` (structure)

The settings that determine the size and behavior of the connection pool for the target group.

MaxConnectionsPercent -> (integer)

The maximum size of the connection pool for each target in a target group. The value is expressed as a percentage of the `max_connections` setting for the RDS DB instance or Aurora DB cluster used by the target group.

If you specify `MaxIdleConnectionsPercent` , then you must also include a value for this parameter.

Default: `10` for RDS for Microsoft SQL Server, and `100` for all other engines

Constraints:

- Must be between 1 and 100.

MaxIdleConnectionsPercent -> (integer)

A value that controls how actively the proxy closes idle database connections in the connection pool. The value is expressed as a percentage of the `max_connections` setting for the RDS DB instance or Aurora DB cluster used by the target group. With a high value, the proxy leaves a high percentage of idle database connections open. A low value causes the proxy to close more idle connections and return them to the database.

If you specify this parameter, then you must also include a value for `MaxConnectionsPercent` .

Default: The default value is half of the value of `MaxConnectionsPercent` . For example, if `MaxConnectionsPercent` is 80, then the default value of `MaxIdleConnectionsPercent` is 40. If the value of `MaxConnectionsPercent` isnât specified, then for SQL Server, `MaxIdleConnectionsPercent` is `5` , and for all other engines, the default is `50` .

Constraints:

- Must be between 0 and the value of `MaxConnectionsPercent` .

ConnectionBorrowTimeout -> (integer)

The number of seconds for a proxy to wait for a connection to become available in the connection pool. This setting only applies when the proxy has opened its maximum number of connections and all connections are busy with client sessions.

Default: `120`

Constraints:

- Must be between 0 and 3600.

SessionPinningFilters -> (list)

Each item in the list represents a class of SQL operations that normally cause all later statements in a session using a proxy to be pinned to the same underlying database connection. Including an item in the list exempts that class of SQL operations from the pinning behavior.

Default: no session pinning filters

(string)

InitQuery -> (string)

Add an initialization query, or modify the current one. You can specify one or more SQL statements for the proxy to run when opening each new database connection. The setting is typically used with `SET` statements to make sure that each connection has identical settings. Make sure that the query you add is valid. To include multiple variables in a single `SET` statement, use comma separators.

For example: `SET variable1=value1, variable2=value2`

For multiple statements, use semicolons as the separator.

Default: no initialization query

Shorthand Syntax:

```
MaxConnectionsPercent=integer,MaxIdleConnectionsPercent=integer,ConnectionBorrowTimeout=integer,SessionPinningFilters=string,string,InitQuery=string
```

JSON Syntax:

```
{
  "MaxConnectionsPercent": integer,
  "MaxIdleConnectionsPercent": integer,
  "ConnectionBorrowTimeout": integer,
  "SessionPinningFilters": ["string", ...],
  "InitQuery": "string"
}
```

`--new-name` (string)

The new name for the modified `DBProxyTarget` . An identifier must begin with a letter and must contain only ASCII letters, digits, and hyphens; it canât end with a hyphen or contain two consecutive hyphens.

You canât rename the `default` target group.

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

**To modify a DB proxy endpoints**

The following `modify-db-proxy-target-group` example modifies a DB proxy target group to set the maximum connections to 80 percent and maximum idle connections to 10 percent.

```
aws rds modify-db-proxy-target-group \
    --target-group-name default \
    --db-proxy-name proxyExample \
    --connection-pool-config MaxConnectionsPercent=80,MaxIdleConnectionsPercent=10
```

Output:

```
{
"DBProxyTargetGroup":
    {
        "DBProxyName": "proxyExample",
        "TargetGroupName": "default",
        "TargetGroupArn": "arn:aws:rds:us-east-1:123456789012:target-group:prx-tg-0123a01b12345c0ab",
        "IsDefault": true,
        "Status": "available",
        "ConnectionPoolConfig": {
            "MaxConnectionsPercent": 80,
            "MaxIdleConnectionsPercent": 10,
            "ConnectionBorrowTimeout": 120,
            "SessionPinningFilters": []
        },
        "CreatedDate": "2023-05-02T18:41:19.495000+00:00",
        "UpdatedDate": "2023-05-02T18:41:21.762000+00:00"
    }
}
```

For more information, see [Modifying an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-proxy-managing.html#rds-proxy-modifying-proxy) in the *Amazon RDS User Guide* and [Modifying an RDS Proxy](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/rds-proxy-managing.html#rds-proxy-modifying-proxy) in the *Amazon Aurora User Guide*.

## Output

DBProxyTargetGroup -> (structure)

The settings of the modified `DBProxyTarget` .

DBProxyName -> (string)

The identifier for the RDS proxy associated with this target group.

TargetGroupName -> (string)

The identifier for the target group. This name must be unique for all target groups owned by your Amazon Web Services account in the specified Amazon Web Services Region.

TargetGroupArn -> (string)

The Amazon Resource Name (ARN) representing the target group.

IsDefault -> (boolean)

Indicates whether this target group is the first one used for connection requests by the associated proxy. Because each proxy is currently associated with a single target group, currently this setting is always `true` .

Status -> (string)

The current status of this target group. A status of `available` means the target group is correctly associated with a database. Other values indicate that you must wait for the target group to be ready, or take some action to resolve an issue.

ConnectionPoolConfig -> (structure)

The settings that determine the size and behavior of the connection pool for the target group.

MaxConnectionsPercent -> (integer)

The maximum size of the connection pool for each target in a target group. The value is expressed as a percentage of the `max_connections` setting for the RDS DB instance or Aurora DB cluster used by the target group.

MaxIdleConnectionsPercent -> (integer)

Controls how actively the proxy closes idle database connections in the connection pool. The value is expressed as a percentage of the `max_connections` setting for the RDS DB instance or Aurora DB cluster used by the target group. With a high value, the proxy leaves a high percentage of idle database connections open. A low value causes the proxy to close more idle connections and return them to the database.

ConnectionBorrowTimeout -> (integer)

The number of seconds for a proxy to wait for a connection to become available in the connection pool. Only applies when the proxy has opened its maximum number of connections and all connections are busy with client sessions.

SessionPinningFilters -> (list)

Each item in the list represents a class of SQL operations that normally cause all later statements in a session using a proxy to be pinned to the same underlying database connection. Including an item in the list exempts that class of SQL operations from the pinning behavior. This setting is only supported for MySQL engine family databases. Currently, the only allowed value is `EXCLUDE_VARIABLE_SETS` .

(string)

InitQuery -> (string)

One or more SQL statements for the proxy to run when opening each new database connection. Typically used with `SET` statements to make sure that each connection has identical settings such as time zone and character set. This setting is empty by default. For multiple statements, use semicolons as the separator. You can also include multiple variables in a single `SET` statement, such as `SET x=1, y=2` .

CreatedDate -> (timestamp)

The date and time when the target group was first created.

UpdatedDate -> (timestamp)

The date and time when the target group was last updated.