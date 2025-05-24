# batch-execute-statementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/batch-execute-statement.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/batch-execute-statement.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [redshift-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/redshift-data/index.html#cli-aws-redshift-data) ]

# batch-execute-statement

## Description

Runs one or more SQL statements, which can be data manipulation language (DML) or data definition language (DDL). Depending on the authorization method, use one of the following combinations of request parameters:

- Secrets Manager - when connecting to a cluster, provide the `secret-arn` of a secret stored in Secrets Manager which has `username` and `password` . The specified secret contains credentials to connect to the `database` you specify. When you are connecting to a cluster, you also supply the database name, If you provide a cluster identifier (`dbClusterIdentifier` ), it must match the cluster identifier stored in the secret. When you are connecting to a serverless workgroup, you also supply the database name.
- Temporary credentials - when connecting to your data warehouse, choose one of the following options:
- When connecting to a serverless workgroup, specify the workgroup name and database name. The database user name is derived from the IAM identity. For example, `arn:iam::123456789012:user:foo` has the database user name `IAM:foo` . Also, permission to call the `redshift-serverless:GetCredentials` operation is required.
- When connecting to a cluster as an IAM identity, specify the cluster identifier and the database name. The database user name is derived from the IAM identity. For example, `arn:iam::123456789012:user:foo` has the database user name `IAM:foo` . Also, permission to call the `redshift:GetClusterCredentialsWithIAM` operation is required.
- When connecting to a cluster as a database user, specify the cluster identifier, the database name, and the database user name. Also, permission to call the `redshift:GetClusterCredentials` operation is required.

For more information about the Amazon Redshift Data API and CLI usage examples, see [Using the Amazon Redshift Data API](https://docs.aws.amazon.com/redshift/latest/mgmt/data-api.html) in the *Amazon Redshift Management Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/redshift-data-2019-12-20/BatchExecuteStatement)

## Synopsis

```
batch-execute-statement
[--client-token <value>]
[--cluster-identifier <value>]
[--database <value>]
[--db-user <value>]
[--result-format <value>]
[--secret-arn <value>]
[--session-id <value>]
[--session-keep-alive-seconds <value>]
--sqls <value>
[--statement-name <value>]
[--with-event | --no-with-event]
[--workgroup-name <value>]
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

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--cluster-identifier` (string)

The cluster identifier. This parameter is required when connecting to a cluster and authenticating using either Secrets Manager or temporary credentials.

`--database` (string)

The name of the database. This parameter is required when authenticating using either Secrets Manager or temporary credentials.

`--db-user` (string)

The database user name. This parameter is required when connecting to a cluster as a database user and authenticating using temporary credentials.

`--result-format` (string)

The data format of the result of the SQL statement. If no format is specified, the default is JSON.

Possible values:

- `JSON`
- `CSV`

`--secret-arn` (string)

The name or ARN of the secret that enables access to the database. This parameter is required when authenticating using Secrets Manager.

`--session-id` (string)

The session identifier of the query.

`--session-keep-alive-seconds` (integer)

The number of seconds to keep the session alive after the query finishes. The maximum time a session can keep alive is 24 hours. After 24 hours, the session is forced closed and the query is terminated.

`--sqls` (list)

One or more SQL statements to run. `The SQL statements are run as a single transaction. They run serially in the order of the array. Subsequent SQL statements don't start until the previous statement in the array completes. If any SQL statement fails, then because they are run as one transaction, all work is rolled back.</p>`

(string)

Syntax:

```
"string" "string" ...
```

`--statement-name` (string)

The name of the SQL statements. You can name the SQL statements when you create them to identify the query.

`--with-event` | `--no-with-event` (boolean)

A value that indicates whether to send an event to the Amazon EventBridge event bus after the SQL statements run.

`--workgroup-name` (string)

The serverless workgroup name or Amazon Resource Name (ARN). This parameter is required when connecting to a serverless workgroup and authenticating using either Secrets Manager or temporary credentials.

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

ClusterIdentifier -> (string)

The cluster identifier. This element is not returned when connecting to a serverless workgroup.

CreatedAt -> (timestamp)

The date and time (UTC) the statement was created.

Database -> (string)

The name of the database.

DbGroups -> (list)

A list of colon (:) separated names of database groups.

(string)

DbUser -> (string)

The database user name.

Id -> (string)

The identifier of the SQL statement whose results are to be fetched. This value is a universally unique identifier (UUID) generated by Amazon Redshift Data API. This identifier is returned by `BatchExecuteStatment` .

SecretArn -> (string)

The name or ARN of the secret that enables access to the database.

SessionId -> (string)

The session identifier of the query.

WorkgroupName -> (string)

The serverless workgroup name or Amazon Resource Name (ARN). This element is not returned when connecting to a provisioned cluster.