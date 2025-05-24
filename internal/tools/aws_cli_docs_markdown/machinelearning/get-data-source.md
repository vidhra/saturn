# get-data-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-data-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/get-data-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [machinelearning](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/machinelearning/index.html#cli-aws-machinelearning) ]

# get-data-source

## Description

Returns a `DataSource` that includes metadata and data file information, as well as the current status of the `DataSource` .

`GetDataSource` provides results in normal or verbose format. The verbose format adds the schema description and the list of files pointed to by the DataSource to the normal format.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/machinelearning-2014-12-12/GetDataSource)

## Synopsis

```
get-data-source
--data-source-id <value>
[--verbose | --no-verbose]
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

`--data-source-id` (string)

The ID assigned to the `DataSource` at creation.

`--verbose` | `--no-verbose` (boolean)

Specifies whether the `GetDataSource` operation should return `DataSourceSchema` .

If true, `DataSourceSchema` is returned.

If false, `DataSourceSchema` is not returned.

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

DataSourceId -> (string)

The ID assigned to the `DataSource` at creation. This value should be identical to the value of the `DataSourceId` in the request.

DataLocationS3 -> (string)

The location of the data file or directory in Amazon Simple Storage Service (Amazon S3).

DataRearrangement -> (string)

A JSON string that represents the splitting and rearrangement requirement used when this `DataSource` was created.

CreatedByIamUser -> (string)

The AWS user account from which the `DataSource` was created. The account type can be either an AWS root account or an AWS Identity and Access Management (IAM) user account.

CreatedAt -> (timestamp)

The time that the `DataSource` was created. The time is expressed in epoch time.

LastUpdatedAt -> (timestamp)

The time of the most recent edit to the `DataSource` . The time is expressed in epoch time.

DataSizeInBytes -> (long)

The total size of observations in the data files.

NumberOfFiles -> (long)

The number of data files referenced by the `DataSource` .

Name -> (string)

A user-supplied name or description of the `DataSource` .

Status -> (string)

The current status of the `DataSource` . This element can have one of the following values:

- `PENDING` - Amazon ML submitted a request to create a `DataSource` .
- `INPROGRESS` - The creation process is underway.
- `FAILED` - The request to create a `DataSource` did not run to completion. It is not usable.
- `COMPLETED` - The creation process completed successfully.
- `DELETED` - The `DataSource` is marked as deleted. It is not usable.

LogUri -> (string)

A link to the file containing logs of `CreateDataSourceFrom*` operations.

Message -> (string)

The user-supplied description of the most recent details about creating the `DataSource` .

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

The approximate CPU time in milliseconds that Amazon Machine Learning spent processing the `DataSource` , normalized and scaled on computation resources. `ComputeTime` is only available if the `DataSource` is in the `COMPLETED` state and the `ComputeStatistics` is set to true.

FinishedAt -> (timestamp)

The epoch time when Amazon Machine Learning marked the `DataSource` as `COMPLETED` or `FAILED` . `FinishedAt` is only available when the `DataSource` is in the `COMPLETED` or `FAILED` state.

StartedAt -> (timestamp)

The epoch time when Amazon Machine Learning marked the `DataSource` as `INPROGRESS` . `StartedAt` isnât available if the `DataSource` is in the `PENDING` state.

DataSourceSchema -> (string)

The schema used by all of the data files of this `DataSource` .

**Note:** This parameter is provided as part of the verbose format.