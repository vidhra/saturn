# start-query-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-query-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/start-query-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [athena](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/index.html#cli-aws-athena) ]

# start-query-execution

## Description

Runs the SQL query statements contained in the `Query` . Requires you to have access to the workgroup in which the query ran. Running queries against an external catalog requires  GetDataCatalog permission to the catalog. For code samples using the Amazon Web Services SDK for Java, see [Examples and Code Samples](http://docs.aws.amazon.com/athena/latest/ug/code-samples.html) in the *Amazon Athena User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/athena-2017-05-18/StartQueryExecution)

## Synopsis

```
start-query-execution
--query-string <value>
[--client-request-token <value>]
[--query-execution-context <value>]
[--result-configuration <value>]
[--work-group <value>]
[--execution-parameters <value>]
[--result-reuse-configuration <value>]
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

`--query-string` (string)

The SQL query statements to be executed.

`--client-request-token` (string)

A unique case-sensitive string used to ensure the request to create the query is idempotent (executes only once). If another `StartQueryExecution` request is received, the same response is returned and another query is not created. An error is returned if a parameter, such as `QueryString` , has changed. A call to `StartQueryExecution` that uses a previous client request token returns the same `QueryExecutionId` even if the requester doesnât have permission on the tables specified in `QueryString` .

### Warning

This token is listed as not required because Amazon Web Services SDKs (for example the Amazon Web Services SDK for Java) auto-generate the token for users. If you are not using the Amazon Web Services SDK or the Amazon Web Services CLI, you must provide this token or the action will fail.

`--query-execution-context` (structure)

The database within which the query executes.

Database -> (string)

The name of the database used in the query execution. The database must exist in the catalog.

Catalog -> (string)

The name of the data catalog used in the query execution.

Shorthand Syntax:

```
Database=string,Catalog=string
```

JSON Syntax:

```
{
  "Database": "string",
  "Catalog": "string"
}
```

`--result-configuration` (structure)

Specifies information about where and how to save the results of the query execution. If the query runs in a workgroup, then workgroupâs settings may override query settings. This affects the query results location. The workgroup settings override is specified in EnforceWorkGroupConfiguration (true/false) in the WorkGroupConfiguration. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

OutputLocation -> (string)

The location in Amazon S3 where your query and calculation results are stored, such as `s3://path/to/query/bucket/` . To run the query, you must specify the query results location using one of the ways: either for individual queries using either this setting (client-side), or in the workgroup, using  WorkGroupConfiguration . If none of them is set, Athena issues an error that no output location is provided. If workgroup settings override client-side settings, then the query uses the settings specified for the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration .

EncryptionConfiguration -> (structure)

If query and calculation results are encrypted in Amazon S3, indicates the encryption option used (for example, `SSE_KMS` or `CSE_KMS` ) and key information. This is a client-side setting. If workgroup settings override client-side settings, then the query uses the encryption configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

EncryptionOption -> (string)

Indicates whether Amazon S3 server-side encryption with Amazon S3-managed keys (`SSE_S3` ), server-side encryption with KMS-managed keys (`SSE_KMS` ), or client-side encryption with KMS-managed keys (`CSE_KMS` ) is used.

If a query runs in a workgroup and the workgroup overrides client-side settings, then the workgroupâs setting for encryption is used. It specifies whether query results must be encrypted, for all queries that run in this workgroup.

KmsKey -> (string)

For `SSE_KMS` and `CSE_KMS` , this is the KMS key ARN or ID.

ExpectedBucketOwner -> (string)

The Amazon Web Services account ID that you expect to be the owner of the Amazon S3 bucket specified by  ResultConfiguration$OutputLocation . If set, Athena uses the value for `ExpectedBucketOwner` when it makes Amazon S3 calls to your specified output location. If the `ExpectedBucketOwner` Amazon Web Services account ID does not match the actual owner of the Amazon S3 bucket, the call fails with a permissions error.

This is a client-side setting. If workgroup settings override client-side settings, then the query uses the `ExpectedBucketOwner` setting that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. See  WorkGroupConfiguration$EnforceWorkGroupConfiguration and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

AclConfiguration -> (structure)

Indicates that an Amazon S3 canned ACL should be set to control ownership of stored query results. Currently the only supported canned ACL is `BUCKET_OWNER_FULL_CONTROL` . This is a client-side setting. If workgroup settings override client-side settings, then the query uses the ACL configuration that is specified for the workgroup, and also uses the location for storing query results specified in the workgroup. For more information, see  WorkGroupConfiguration$EnforceWorkGroupConfiguration and [Workgroup Settings Override Client-Side Settings](https://docs.aws.amazon.com/athena/latest/ug/workgroups-settings-override.html) .

S3AclOption -> (string)

The Amazon S3 canned ACL that Athena should specify when storing query results, including data files inserted by Athena as the result of statements like CTAS or INSERT INTO. Currently the only supported canned ACL is `BUCKET_OWNER_FULL_CONTROL` . If a query runs in a workgroup and the workgroup overrides client-side settings, then the Amazon S3 canned ACL specified in the workgroupâs settings is used for all queries that run in the workgroup. For more information about Amazon S3 canned ACLs, see [Canned ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl) in the *Amazon S3 User Guide* .

Shorthand Syntax:

```
OutputLocation=string,EncryptionConfiguration={EncryptionOption=string,KmsKey=string},ExpectedBucketOwner=string,AclConfiguration={S3AclOption=string}
```

JSON Syntax:

```
{
  "OutputLocation": "string",
  "EncryptionConfiguration": {
    "EncryptionOption": "SSE_S3"|"SSE_KMS"|"CSE_KMS",
    "KmsKey": "string"
  },
  "ExpectedBucketOwner": "string",
  "AclConfiguration": {
    "S3AclOption": "BUCKET_OWNER_FULL_CONTROL"
  }
}
```

`--work-group` (string)

The name of the workgroup in which the query is being started.

`--execution-parameters` (list)

A list of values for the parameters in a query. The values are applied sequentially to the parameters in the query in the order in which the parameters occur.

(string)

Syntax:

```
"string" "string" ...
```

`--result-reuse-configuration` (structure)

Specifies the query result reuse behavior for the query.

ResultReuseByAgeConfiguration -> (structure)

Specifies whether previous query results are reused, and if so, their maximum age.

Enabled -> (boolean)

True if previous query results can be reused when the query is run; otherwise, false. The default is false.

MaxAgeInMinutes -> (integer)

Specifies, in minutes, the maximum age of a previous query result that Athena should consider for reuse. The default is 60.

Shorthand Syntax:

```
ResultReuseByAgeConfiguration={Enabled=boolean,MaxAgeInMinutes=integer}
```

JSON Syntax:

```
{
  "ResultReuseByAgeConfiguration": {
    "Enabled": true|false,
    "MaxAgeInMinutes": integer
  }
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**Example 1: To run a query in a workgroup on the specified table in the specified database and data catalog**

The following `start-query-execution` example uses the `AthenaAdmin` workgroup to run a query on the `cloudfront_logs` table in the `cflogsdatabase` in the `AwsDataCatalog` data catalog.

```
aws athena start-query-execution \
    --query-string "select date, location, browser, uri, status from cloudfront_logs where method = 'GET' and status = 200 and location like 'SFO%' limit 10" \
    --work-group "AthenaAdmin" \
    --query-execution-context Database=cflogsdatabase,Catalog=AwsDataCatalog
```

Output:

```
{
"QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```

For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.

**Example 2: To run a query that uses a specified workgroup to create a database in the specified data catalog**

The following `start-query-execution` example uses the `AthenaAdmin` workgroup to create the database `newdb` in the default data catalog `AwsDataCatalog`.

```
aws athena start-query-execution \
    --query-string "create database if not exists newdb" \
    --work-group "AthenaAdmin"
```

Output:

```
{
"QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11112"
}
```

For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.

**Example 3: To run a query that creates a view on a table in the specified database and data catalog**

The following `start-query-execution` example uses  a `SELECT` statement on the `cloudfront_logs` table in the `cflogsdatabase` to create the view `cf10`.

```
aws athena start-query-execution \
    --query-string  "CREATE OR REPLACE VIEW cf10 AS SELECT * FROM cloudfront_logs limit 10" \
    --query-execution-context Database=cflogsdatabase
```

Output:

```
{
"QueryExecutionId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11113"
}
```

For more information, see [Running SQL Queries Using Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/querying-athena-tables.html) in the *Amazon Athena User Guide*.

## Output

QueryExecutionId -> (string)

The unique ID of the query that ran as a result of this request.