# describe-data-sourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-data-sources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/describe-data-sources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [machinelearning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/index.html#cli-aws-machinelearning) ]

# describe-data-sources

## Description

Returns a list of `DataSource` that match the search criteria in the request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/DescribeDataSources)

`describe-data-sources` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Results`

## Synopsis

```
describe-data-sources
[--filter-variable <value>]
[--eq <value>]
[--gt <value>]
[--lt <value>]
[--ge <value>]
[--le <value>]
[--ne <value>]
[--prefix <value>]
[--sort-order <value>]
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

`--filter-variable` (string)

Use one of the following variables to filter a list of `DataSource` :

- `CreatedAt` - Sets the search criteria to `DataSource` creation dates.
- `Status` - Sets the search criteria to `DataSource` statuses.
- `Name` - Sets the search criteria to the contents of `DataSource` `Name` .
- `DataUri` - Sets the search criteria to the URI of data files used to create the `DataSource` . The URI can identify either a file or an Amazon Simple Storage Service (Amazon S3) bucket or directory.
- `IAMUser` - Sets the search criteria to the user account that invoked the `DataSource` creation.

Possible values:

- `CreatedAt`
- `LastUpdatedAt`
- `Status`
- `Name`
- `DataLocationS3`
- `IAMUser`

`--eq` (string)

The equal to operator. The `DataSource` results will have `FilterVariable` values that exactly match the value specified with `EQ` .

`--gt` (string)

The greater than operator. The `DataSource` results will have `FilterVariable` values that are greater than the value specified with `GT` .

`--lt` (string)

The less than operator. The `DataSource` results will have `FilterVariable` values that are less than the value specified with `LT` .

`--ge` (string)

The greater than or equal to operator. The `DataSource` results will have `FilterVariable` values that are greater than or equal to the value specified with `GE` .

`--le` (string)

The less than or equal to operator. The `DataSource` results will have `FilterVariable` values that are less than or equal to the value specified with `LE` .

`--ne` (string)

The not equal to operator. The `DataSource` results will have `FilterVariable` values not equal to the value specified with `NE` .

`--prefix` (string)

A string that is found at the beginning of a variable, such as `Name` or `Id` .

For example, a `DataSource` could have the `Name` `2014-09-09-HolidayGiftMailer` . To search for this `DataSource` , select `Name` for the `FilterVariable` and any of the following strings for the `Prefix` :

- 2014-09
- 2014-09-09
- 2014-09-09-Holiday

`--sort-order` (string)

A two-value parameter that determines the sequence of the resulting list of `DataSource` .

- `asc` - Arranges the list in ascending order (A-Z, 0-9).
- `dsc` - Arranges the list in descending order (Z-A, 9-0).

Results are sorted by `FilterVariable` .

Possible values:

- `asc`
- `dsc`

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

Results -> (list)

A list of `DataSource` that meet the search criteria.

(structure)

Represents the output of the `GetDataSource` operation.

The content consists of the detailed metadata and data file information and the current status of the `DataSource` .

DataSourceId -> (string)

The ID that is assigned to the `DataSource` during creation.

DataLocationS3 -> (string)

The location and name of the data in Amazon Simple Storage Service (Amazon S3) that is used by a `DataSource` .

DataRearrangement -> (string)

A JSON string that represents the splitting and rearrangement requirement used when this `DataSource` was created.

CreatedByIamUser -> (string)

The AWS user account from which the `DataSource` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

CreatedAt -> (timestamp)

The time that the `DataSource` was created. The time is expressed in epoch time.

LastUpdatedAt -> (timestamp)

The time of the most recent edit to the `BatchPrediction` . The time is expressed in epoch time.

DataSizeInBytes -> (long)

The total number of observations contained in the data files that the `DataSource` references.

NumberOfFiles -> (long)

The number of data files referenced by the `DataSource` .

Name -> (string)

A user-supplied name or description of the `DataSource` .

Status -> (string)

The current status of the `DataSource` . This element can have one of the following values:

- PENDING - Amazon Machine Learning (Amazon ML) submitted a request to create a `DataSource` .
- INPROGRESS - The creation process is underway.
- FAILED - The request to create a `DataSource` did not run to completion. It is not usable.
- COMPLETED - The creation process completed successfully.
- DELETED - The `DataSource` is marked as deleted. It is not usable.

Message -> (string)

A description of the most recent details about creating the `DataSource` .

RedshiftMetadata -> (structure)

Describes the `DataSource` details specific to Amazon Redshift.

RedshiftDatabase -> (structure)

Describes the database details required to connect to an Amazon Redshift database.

DatabaseName -> (string)

The name of a database hosted on an Amazon Redshift cluster.

ClusterIdentifier -> (string)

The ID of an Amazon Redshift cluster.

DatabaseUserName -> (string)

A username to be used by Amazon Machine Learning (Amazon ML)to connect to a database on an Amazon Redshift cluster. The username should have sufficient permissions to execute the `RedshiftSelectSqlQuery` query. The username should be valid for an Amazon Redshift [USER](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html) .

SelectSqlQuery -> (string)

The SQL query that is specified during  CreateDataSourceFromRedshift . Returns only if `Verbose` is true in GetDataSourceInput.

RDSMetadata -> (structure)

The datasource details that are specific to Amazon RDS.

Database -> (structure)

The database details required to connect to an Amazon RDS.

InstanceIdentifier -> (string)

The ID of an RDS DB instance.

DatabaseName -> (string)

The name of a database hosted on an RDS DB instance.

DatabaseUserName -> (string)

The username to be used by Amazon ML to connect to database on an Amazon RDS instance. The username should have sufficient permissions to execute an `RDSSelectSqlQuery` query.

SelectSqlQuery -> (string)

The SQL query that is supplied during  CreateDataSourceFromRDS . Returns only if `Verbose` is true in `GetDataSourceInput` .

ResourceRole -> (string)

The role (DataPipelineDefaultResourceRole) assumed by an Amazon EC2 instance to carry out the copy task from Amazon RDS to Amazon S3. For more information, see [Role templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html) for data pipelines.

ServiceRole -> (string)

The role (DataPipelineDefaultRole) assumed by the Data Pipeline service to monitor the progress of the copy task from Amazon RDS to Amazon S3. For more information, see [Role templates](https://docs.aws.amazon.com/datapipeline/latest/DeveloperGuide/dp-iam-roles.html) for data pipelines.

DataPipelineId -> (string)

The ID of the Data Pipeline instance that is used to carry to copy data from Amazon RDS to Amazon S3. You can use the ID to find details about the instance in the Data Pipeline console.

RoleARN -> (string)

The Amazon Resource Name (ARN) of an [AWS IAM Role](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-toplevel.html#roles-about-termsandconcepts) , such as the following: arn:aws:iam::account:role/rolename.

ComputeStatistics -> (boolean)

The parameter is `true` if statistics need to be generated from the observation data.

ComputeTime -> (long)

Long integer type that is a 64-bit signed number.

FinishedAt -> (timestamp)

A timestamp represented in epoch time.

StartedAt -> (timestamp)

A timestamp represented in epoch time.

NextToken -> (string)

An ID of the next page in the paginated results that indicates at least one more page follows.