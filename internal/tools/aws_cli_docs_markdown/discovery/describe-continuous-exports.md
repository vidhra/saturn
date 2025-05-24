# describe-continuous-exportsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-continuous-exports.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/describe-continuous-exports.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [discovery](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/discovery/index.html#cli-aws-discovery) ]

# describe-continuous-exports

## Description

Lists exports as specified by ID. All continuous exports associated with your user can be listed if you call `DescribeContinuousExports` as is without passing any parameters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/discovery-2015-11-01/DescribeContinuousExports)

`describe-continuous-exports` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `descriptions`

## Synopsis

```
describe-continuous-exports
[--export-ids <value>]
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

`--export-ids` (list)

The unique IDs assigned to the exports.

(string)

Syntax:

```
"string" "string" ...
```

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

descriptions -> (list)

A list of continuous export descriptions.

(structure)

A list of continuous export descriptions.

exportId -> (string)

The unique ID assigned to this export.

status -> (string)

Describes the status of the export. Can be one of the following values:

- START_IN_PROGRESS - setting up resources to start continuous export.
- START_FAILED - an error occurred setting up continuous export. To recover, call start-continuous-export again.
- ACTIVE - data is being exported to the customer bucket.
- ERROR - an error occurred during export. To fix the issue, call stop-continuous-export and start-continuous-export.
- STOP_IN_PROGRESS - stopping the export.
- STOP_FAILED - an error occurred stopping the export. To recover, call stop-continuous-export again.
- INACTIVE - the continuous export has been stopped. Data is no longer being exported to the customer bucket.

statusDetail -> (string)

Contains information about any errors that have occurred. This data type can have the following values:

- ACCESS_DENIED - You donât have permission to start Data Exploration in Amazon Athena. Contact your Amazon Web Services administrator for help. For more information, see [Setting Up Amazon Web Services Application Discovery Service](http://docs.aws.amazon.com/application-discovery/latest/userguide/setting-up.html) in the Application Discovery Service User Guide.
- DELIVERY_STREAM_LIMIT_FAILURE - You reached the limit for Amazon Kinesis Data Firehose delivery streams. Reduce the number of streams or request a limit increase and try again. For more information, see [Kinesis Data Streams Limits](http://docs.aws.amazon.com/streams/latest/dev/service-sizes-and-limits.html) in the Amazon Kinesis Data Streams Developer Guide.
- FIREHOSE_ROLE_MISSING - The Data Exploration feature is in an error state because your user is missing the Amazon Web ServicesApplicationDiscoveryServiceFirehose role. Turn on Data Exploration in Amazon Athena and try again. For more information, see [Creating the Amazon Web ServicesApplicationDiscoveryServiceFirehose Role](https://docs.aws.amazon.com/application-discovery/latest/userguide/security-iam-awsmanpol.html#security-iam-awsmanpol-create-firehose-role) in the Application Discovery Service User Guide.
- FIREHOSE_STREAM_DOES_NOT_EXIST - The Data Exploration feature is in an error state because your user is missing one or more of the Kinesis data delivery streams.
- INTERNAL_FAILURE - The Data Exploration feature is in an error state because of an internal failure. Try again later. If this problem persists, contact Amazon Web Services Support.
- LAKE_FORMATION_ACCESS_DENIED - You donât have sufficient lake formation permissions to start continuous export. For more information, see [Upgrading Amazon Web Services Glue Data Permissions to the Amazon Web Services Lake Formation Model](http://docs.aws.amazon.com/lake-formation/latest/dg/upgrade-glue-lake-formation.html) in the Amazon Web Services *Lake Formation Developer Guide* .  You can use one of the following two ways to resolve this issue.
- If you donât want to use the Lake Formation permission model, you can change the default Data Catalog settings to use only Amazon Web Services Identity and Access Management (IAM) access control for new databases. For more information, see [Change Data Catalog Settings](https://docs.aws.amazon.com/lake-formation/latest/dg/getting-started-setup.html#setup-change-cat-settings) in the *Lake Formation Developer Guide* .
- You can give the service-linked IAM roles AWSServiceRoleForApplicationDiscoveryServiceContinuousExport and AWSApplicationDiscoveryServiceFirehose the required Lake Formation permissions. For more information, see [Granting Database Permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/granting-database-permissions.html) in the *Lake Formation Developer Guide* .
- AWSServiceRoleForApplicationDiscoveryServiceContinuousExport - Grant database creator permissions, which gives the role database creation ability and implicit permissions for any created tables. For more information, see [Implicit Lake Formation Permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/implicit-permissions.html) in the *Lake Formation Developer Guide* .
- AWSApplicationDiscoveryServiceFirehose - Grant describe permissions for all tables in the database.
- S3_BUCKET_LIMIT_FAILURE - You reached the limit for Amazon S3 buckets. Reduce the number of S3 buckets or request a limit increase and try again. For more information, see [Bucket Restrictions and Limitations](http://docs.aws.amazon.com/AmazonS3/latest/dev/BucketRestrictions.html) in the Amazon Simple Storage Service Developer Guide.
- S3_NOT_SIGNED_UP - Your account is not signed up for the Amazon S3 service. You must sign up before you can use Amazon S3. You can sign up at the following URL: [https://aws.amazon.com/s3](https://aws.amazon.com/s3) .

s3Bucket -> (string)

The name of the s3 bucket where the export data parquet files are stored.

startTime -> (timestamp)

The timestamp representing when the continuous export was started.

stopTime -> (timestamp)

The timestamp that represents when this continuous export was stopped.

dataSource -> (string)

The type of data collector used to gather this data (currently only offered for AGENT).

schemaStorageConfig -> (map)

An object which describes how the data is stored.

- `databaseName` - the name of the Glue database used to store the schema.

key -> (string)

value -> (string)

nextToken -> (string)

The token from the previous call to `DescribeExportTasks` .