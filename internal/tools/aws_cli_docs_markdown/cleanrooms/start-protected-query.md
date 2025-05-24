# start-protected-queryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/start-protected-query.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/start-protected-query.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [cleanrooms](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cleanrooms/index.html#cli-aws-cleanrooms) ]

# start-protected-query

## Description

Creates a protected query that is started by Clean Rooms.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/cleanrooms-2022-02-17/StartProtectedQuery)

## Synopsis

```
start-protected-query
--type <value>
--membership-identifier <value>
--sql-parameters <value>
[--result-configuration <value>]
[--compute-configuration <value>]
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

`--type` (string)

The type of the protected query to be started.

Possible values:

- `SQL`

`--membership-identifier` (string)

A unique identifier for the membership to run this query against. Currently accepts a membership ID.

`--sql-parameters` (structure)

The protected SQL query parameters.

queryString -> (string)

The query string to be submitted.

analysisTemplateArn -> (string)

The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.

parameters -> (map)

The protected query SQL parameters.

key -> (string)

value -> (string)

Shorthand Syntax:

```
queryString=string,analysisTemplateArn=string,parameters={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "queryString": "string",
  "analysisTemplateArn": "string",
  "parameters": {"string": "string"
    ...}
}
```

`--result-configuration` (structure)

The details needed to write the query results.

outputConfiguration -> (tagged union structure)

Configuration for protected query results.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`, `member`, `distribute`.

s3 -> (structure)

Required configuration for a protected query with an `s3` output type.

resultFormat -> (string)

Intended file format of the result.

bucket -> (string)

The S3 bucket to unload the protected query results.

keyPrefix -> (string)

The S3 prefix to unload the protected query results.

singleFileOutput -> (boolean)

Indicates whether files should be output as a single file (`TRUE` ) or output as multiple files (`FALSE` ). This parameter is only supported for analyses with the Spark analytics engine.

member -> (structure)

Required configuration for a protected query with a `member` output type.

accountId -> (string)

The unique identifier for the account.

distribute -> (structure)

Required configuration for a protected query with a `distribute` output type.

locations -> (list)

A list of locations where you want to distribute the protected query results. Each location must specify either an S3 destination or a collaboration member destination.

### Warning

You canât specify more than one S3 location.

You canât specify the query runnerâs account as a member location.

You must include either an S3 or member output configuration for each location, but not both.

(tagged union structure)

Specifies where youâll distribute the results of your protected query. You must configure either an S3 destination or a collaboration member destination.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`, `member`.

s3 -> (structure)

Contains the configuration to write the query results to S3.

resultFormat -> (string)

Intended file format of the result.

bucket -> (string)

The S3 bucket to unload the protected query results.

keyPrefix -> (string)

The S3 prefix to unload the protected query results.

singleFileOutput -> (boolean)

Indicates whether files should be output as a single file (`TRUE` ) or output as multiple files (`FALSE` ). This parameter is only supported for analyses with the Spark analytics engine.

member -> (structure)

Contains configuration details for the protected query member output.

accountId -> (string)

The unique identifier for the account.

JSON Syntax:

```
{
  "outputConfiguration": {
    "s3": {
      "resultFormat": "CSV"|"PARQUET",
      "bucket": "string",
      "keyPrefix": "string",
      "singleFileOutput": true|false
    },
    "member": {
      "accountId": "string"
    },
    "distribute": {
      "locations": [
        {
          "s3": {
            "resultFormat": "CSV"|"PARQUET",
            "bucket": "string",
            "keyPrefix": "string",
            "singleFileOutput": true|false
          },
          "member": {
            "accountId": "string"
          }
        }
        ...
      ]
    }
  }
}
```

`--compute-configuration` (tagged union structure)

The compute configuration for the protected query.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `worker`.

worker -> (structure)

The worker configuration for the compute environment.

type -> (string)

The worker compute configuration type.

number -> (integer)

The number of workers.

Shorthand Syntax:

```
worker={type=string,number=integer}
```

JSON Syntax:

```
{
  "worker": {
    "type": "CR.1X"|"CR.4X",
    "number": integer
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

## Output

protectedQuery -> (structure)

The protected query.

id -> (string)

The identifier for a protected query instance.

membershipId -> (string)

The identifier for the membership.

membershipArn -> (string)

The ARN of the membership.

createTime -> (timestamp)

The time at which the protected query was created.

sqlParameters -> (structure)

The protected query SQL parameters.

queryString -> (string)

The query string to be submitted.

analysisTemplateArn -> (string)

The Amazon Resource Name (ARN) associated with the analysis template within a collaboration.

parameters -> (map)

The protected query SQL parameters.

key -> (string)

value -> (string)

status -> (string)

The status of the query.

resultConfiguration -> (structure)

Contains any details needed to write the query results.

outputConfiguration -> (tagged union structure)

Configuration for protected query results.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`, `member`, `distribute`.

s3 -> (structure)

Required configuration for a protected query with an `s3` output type.

resultFormat -> (string)

Intended file format of the result.

bucket -> (string)

The S3 bucket to unload the protected query results.

keyPrefix -> (string)

The S3 prefix to unload the protected query results.

singleFileOutput -> (boolean)

Indicates whether files should be output as a single file (`TRUE` ) or output as multiple files (`FALSE` ). This parameter is only supported for analyses with the Spark analytics engine.

member -> (structure)

Required configuration for a protected query with a `member` output type.

accountId -> (string)

The unique identifier for the account.

distribute -> (structure)

Required configuration for a protected query with a `distribute` output type.

locations -> (list)

A list of locations where you want to distribute the protected query results. Each location must specify either an S3 destination or a collaboration member destination.

### Warning

You canât specify more than one S3 location.

You canât specify the query runnerâs account as a member location.

You must include either an S3 or member output configuration for each location, but not both.

(tagged union structure)

Specifies where youâll distribute the results of your protected query. You must configure either an S3 destination or a collaboration member destination.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`, `member`.

s3 -> (structure)

Contains the configuration to write the query results to S3.

resultFormat -> (string)

Intended file format of the result.

bucket -> (string)

The S3 bucket to unload the protected query results.

keyPrefix -> (string)

The S3 prefix to unload the protected query results.

singleFileOutput -> (boolean)

Indicates whether files should be output as a single file (`TRUE` ) or output as multiple files (`FALSE` ). This parameter is only supported for analyses with the Spark analytics engine.

member -> (structure)

Contains configuration details for the protected query member output.

accountId -> (string)

The unique identifier for the account.

statistics -> (structure)

Statistics about protected query execution.

totalDurationInMillis -> (long)

The duration of the protected query, from creation until query completion, in milliseconds.

billedResourceUtilization -> (structure)

The billed resource utilization.

units -> (double)

The number of Clean Rooms Processing Unit (CRPU) hours that have been billed.

result -> (structure)

The result of the protected query.

output -> (tagged union structure)

The output of the protected query.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3`, `memberList`, `distribute`.

s3 -> (structure)

If present, the output for a protected query with an `S3` output type.

location -> (string)

The S3 location of the result.

memberList -> (list)

The list of member Amazon Web Services account(s) that received the results of the query.

(structure)

Details about the member who received the query result.

accountId -> (string)

The Amazon Web Services account ID of the member in the collaboration who can receive results for the query.

distribute -> (structure)

Contains output information for protected queries that use a `distribute` output type. This output type lets you send query results to multiple locations - either to S3 or to collaboration members.

### Note

You can only use the `distribute` output type with the Spark analytics engine.

s3 -> (structure)

Contains output information for protected queries with an S3 output type.

location -> (string)

The S3 location of the result.

memberList -> (list)

Contains the output results for each member location specified in the distribute output configuration. Each entry provides details about the result distribution to a specific collaboration member.

(structure)

Details about the member who received the query result.

accountId -> (string)

The Amazon Web Services account ID of the member in the collaboration who can receive results for the query.

error -> (structure)

An error thrown by the protected query.

message -> (string)

A description of why the query failed.

code -> (string)

An error code for the error.

differentialPrivacy -> (structure)

The sensitivity parameters of the differential privacy results of the protected query.

sensitivityParameters -> (list)

Provides the sensitivity parameters that you can use to better understand the total amount of noise in query results.

(structure)

Provides the sensitivity parameters.

aggregationType -> (string)

The type of aggregation function that was run.

aggregationExpression -> (string)

The aggregation expression that was run.

userContributionLimit -> (integer)

The maximum number of rows contributed by a user in a SQL query.

minColumnValue -> (float)

The lower bound of the aggregation expression.

maxColumnValue -> (float)

The upper bound of the aggregation expression.

computeConfiguration -> (tagged union structure)

The compute configuration for the protected query.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `worker`.

worker -> (structure)

The worker configuration for the compute environment.

type -> (string)

The worker compute configuration type.

number -> (integer)

The number of workers.