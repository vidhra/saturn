# update-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [glue](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/index.html#cli-aws-glue) ]

# update-job

## Description

Updates an existing job definition. The previous job definition is completely overwritten by this information.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/glue-2017-03-31/UpdateJob)

## Synopsis

```
update-job
--job-name <value>
--job-update <value>
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

`--job-name` (string)

The name of the job definition to update.

`--job-update` (structure)

Specifies the values with which to update the job definition. Unspecified configuration is removed or reset to default values.

JobMode -> (string)

A mode that describes how a job was created. Valid values are:

- `SCRIPT` - The job was created using the Glue Studio script editor.
- `VISUAL` - The job was created using the Glue Studio visual editor.
- `NOTEBOOK` - The job was created using an interactive sessions notebook.

When the `JobMode` field is missing or null, `SCRIPT` is assigned as the default value.

JobRunQueuingEnabled -> (boolean)

Specifies whether job run queuing is enabled for the job runs for this job.

A value of true means job run queuing is enabled for the job runs. If false or not populated, the job runs will not be considered for queueing.

If this field does not match the value set in the job run, then the value from the job run field will be used.

Description -> (string)

Description of the job being defined.

LogUri -> (string)

This field is reserved for future use.

Role -> (string)

The name or Amazon Resource Name (ARN) of the IAM role associated with this job (required).

ExecutionProperty -> (structure)

An `ExecutionProperty` specifying the maximum number of concurrent runs allowed for this job.

MaxConcurrentRuns -> (integer)

The maximum number of concurrent runs allowed for the job. The default is 1. An error is returned when this threshold is reached. The maximum value you can specify is controlled by a service limit.

Command -> (structure)

The `JobCommand` that runs this job (required).

Name -> (string)

The name of the job command. For an Apache Spark ETL job, this must be `glueetl` . For a Python shell job, it must be `pythonshell` . For an Apache Spark streaming ETL job, this must be `gluestreaming` . For a Ray job, this must be `glueray` .

ScriptLocation -> (string)

Specifies the Amazon Simple Storage Service (Amazon S3) path to a script that runs a job.

PythonVersion -> (string)

The Python version being used to run a Python shell job. Allowed values are 2 or 3.

Runtime -> (string)

In Ray jobs, Runtime is used to specify the versions of Ray, Python and additional libraries available in your environment. This field is not used in other job types. For supported runtime environment values, see [Supported Ray runtime environments](https://docs.aws.amazon.com/glue/latest/dg/ray-jobs-section.html) in the Glue Developer Guide.

DefaultArguments -> (map)

The default arguments for every run of this job, specified as name-value pairs.

You can specify arguments here that your own job-execution script consumes, as well as arguments that Glue itself consumes.

Job arguments may be logged. Do not pass plaintext secrets as arguments. Retrieve secrets from a Glue Connection, Secrets Manager or other secret management mechanism if you intend to keep them within the Job.

For information about how to specify and consume your own Job arguments, see the [Calling Glue APIs in Python](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-python-calling.html) topic in the developer guide.

For information about the arguments you can provide to this field when configuring Spark jobs, see the [Special Parameters Used by Glue](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-glue-arguments.html) topic in the developer guide.

For information about the arguments you can provide to this field when configuring Ray jobs, see [Using job parameters in Ray jobs](https://docs.aws.amazon.com/glue/latest/dg/author-job-ray-job-parameters.html) in the developer guide.

key -> (string)

value -> (string)

NonOverridableArguments -> (map)

Arguments for this job that are not overridden when providing job arguments in a job run, specified as name-value pairs.

key -> (string)

value -> (string)

Connections -> (structure)

The connections used for this job.

Connections -> (list)

A list of connections used by the job.

(string)

MaxRetries -> (integer)

The maximum number of times to retry this job if it fails.

AllocatedCapacity -> (integer)

This field is deprecated. Use `MaxCapacity` instead.

The number of Glue data processing units (DPUs) to allocate to this job. You can allocate a minimum of 2 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [Glue pricing page](https://aws.amazon.com/glue/pricing/) .

Timeout -> (integer)

The job timeout in minutes. This is the maximum time that a job run can consume resources before it is terminated and enters `TIMEOUT` status.

Jobs must have timeout values less than 7 days or 10080 minutes. Otherwise, the jobs will throw an exception.

When the value is left blank, the timeout is defaulted to 2880 minutes.

Any existing Glue jobs that had a timeout value greater than 7 days will be defaulted to 7 days. For instance if you have specified a timeout of 20 days for a batch job, it will be stopped on the 7th day.

For streaming jobs, if you have set up a maintenance window, it will be restarted during the maintenance window after 7 days.

MaxCapacity -> (double)

For Glue version 1.0 or earlier jobs, using the standard worker type, the number of Glue data processing units (DPUs) that can be allocated when this job runs. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [Glue pricing page](https://aws.amazon.com/glue/pricing/) .

For Glue version 2.0+ jobs, you cannot specify a `Maximum capacity` . Instead, you should specify a `Worker type` and the `Number of workers` .

Do not set `MaxCapacity` if using `WorkerType` and `NumberOfWorkers` .

The value that can be allocated for `MaxCapacity` depends on whether you are running a Python shell job, an Apache Spark ETL job, or an Apache Spark streaming ETL job:

- When you specify a Python shell job (`JobCommand.Name` =âpythonshellâ), you can allocate either 0.0625 or 1 DPU. The default is 0.0625 DPU.
- When you specify an Apache Spark ETL job (`JobCommand.Name` =âglueetlâ) or Apache Spark streaming ETL job (`JobCommand.Name` =âgluestreamingâ), you can allocate from 2 to 100 DPUs. The default is 10 DPUs. This job type cannot have a fractional DPU allocation.

WorkerType -> (string)

The type of predefined worker that is allocated when a job runs. Accepts a value of G.1X, G.2X, G.4X, G.8X or G.025X for Spark jobs. Accepts the value Z.2X for Ray jobs.

- For the `G.1X` worker type, each worker maps to 1 DPU (4 vCPUs, 16 GB of memory) with 94GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
- For the `G.2X` worker type, each worker maps to 2 DPU (8 vCPUs, 32 GB of memory) with 138GB disk, and provides 1 executor per worker. We recommend this worker type for workloads such as data transforms, joins, and queries, to offers a scalable and cost effective way to run most jobs.
- For the `G.4X` worker type, each worker maps to 4 DPU (16 vCPUs, 64 GB of memory) with 256GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs in the following Amazon Web Services Regions: US East (Ohio), US East (N. Virginia), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Asia Pacific (Tokyo), Canada (Central), Europe (Frankfurt), Europe (Ireland), and Europe (Stockholm).
- For the `G.8X` worker type, each worker maps to 8 DPU (32 vCPUs, 128 GB of memory) with 512GB disk, and provides 1 executor per worker. We recommend this worker type for jobs whose workloads contain your most demanding transforms, aggregations, joins, and queries. This worker type is available only for Glue version 3.0 or later Spark ETL jobs, in the same Amazon Web Services Regions as supported for the `G.4X` worker type.
- For the `G.025X` worker type, each worker maps to 0.25 DPU (2 vCPUs, 4 GB of memory) with 84GB disk, and provides 1 executor per worker. We recommend this worker type for low volume streaming jobs. This worker type is only available for Glue version 3.0 or later streaming jobs.
- For the `Z.2X` worker type, each worker maps to 2 M-DPU (8vCPUs, 64 GB of memory) with 128 GB disk, and provides up to 8 Ray workers based on the autoscaler.

NumberOfWorkers -> (integer)

The number of workers of a defined `workerType` that are allocated when a job runs.

SecurityConfiguration -> (string)

The name of the `SecurityConfiguration` structure to be used with this job.

NotificationProperty -> (structure)

Specifies the configuration properties of a job notification.

NotifyDelayAfter -> (integer)

After a job run starts, the number of minutes to wait before sending a job run delay notification.

GlueVersion -> (string)

In Spark jobs, `GlueVersion` determines the versions of Apache Spark and Python that Glue available in a job. The Python version indicates the version supported for jobs of type Spark.

Ray jobs should set `GlueVersion` to `4.0` or greater. However, the versions of Ray, Python and additional libraries available in your Ray job are determined by the `Runtime` parameter of the Job command.

For more information about the available Glue versions and corresponding Spark and Python versions, see [Glue version](https://docs.aws.amazon.com/glue/latest/dg/add-job.html) in the developer guide.

Jobs that are created without specifying a Glue version default to Glue 0.9.

CodeGenConfigurationNodes -> (map)

The representation of a directed acyclic graph on which both the Glue Studio visual component and Glue Studio code generation is based.

key -> (string)

value -> (structure)

`CodeGenConfigurationNode` enumerates all valid Node types. One and only one of its member variables can be populated.

AthenaConnectorSource -> (structure)

Specifies a connector to an Amazon Athena data source.

Name -> (string)

The name of the data source.

ConnectionName -> (string)

The name of the connection that is associated with the connector.

ConnectorName -> (string)

The name of a connector that assists with accessing the data store in Glue Studio.

ConnectionType -> (string)

The type of connection, such as marketplace.athena or custom.athena, designating a connection to an Amazon Athena data store.

ConnectionTable -> (string)

The name of the table in the data source.

SchemaName -> (string)

The name of the Cloudwatch log group to read from. For example, `/aws-glue/jobs/output` .

OutputSchemas -> (list)

Specifies the data schema for the custom Athena source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

JDBCConnectorSource -> (structure)

Specifies a connector to a JDBC data source.

Name -> (string)

The name of the data source.

ConnectionName -> (string)

The name of the connection that is associated with the connector.

ConnectorName -> (string)

The name of a connector that assists with accessing the data store in Glue Studio.

ConnectionType -> (string)

The type of connection, such as marketplace.jdbc or custom.jdbc, designating a connection to a JDBC data store.

AdditionalOptions -> (structure)

Additional connection options for the connector.

FilterPredicate -> (string)

Extra condition clause to filter data from source. For example:

`BillingCity='Mountain View'`

When using a query instead of a table name, you should validate that the query works with the specified `filterPredicate` .

PartitionColumn -> (string)

The name of an integer column that is used for partitioning. This option works only when itâs included with `lowerBound` , `upperBound` , and `numPartitions` . This option works the same way as in the Spark SQL JDBC reader.

LowerBound -> (long)

The minimum value of `partitionColumn` that is used to decide partition stride.

UpperBound -> (long)

The maximum value of `partitionColumn` that is used to decide partition stride.

NumPartitions -> (long)

The number of partitions. This value, along with `lowerBound` (inclusive) and `upperBound` (exclusive), form partition strides for generated `WHERE` clause expressions that are used to split the `partitionColumn` .

JobBookmarkKeys -> (list)

The name of the job bookmark keys on which to sort.

(string)

JobBookmarkKeysSortOrder -> (string)

Specifies an ascending or descending sort order.

DataTypeMapping -> (map)

Custom data type mapping that builds a mapping from a JDBC data type to an Glue data type. For example, the option `"dataTypeMapping":{"FLOAT":"STRING"}` maps data fields of JDBC type `FLOAT` into the Java `String` type by calling the `ResultSet.getString()` method of the driver, and uses it to build the Glue record. The `ResultSet` object is implemented by each driver, so the behavior is specific to the driver you use. Refer to the documentation for your JDBC driver to understand how the driver performs the conversions.

key -> (string)

value -> (string)

ConnectionTable -> (string)

The name of the table in the data source.

Query -> (string)

The table or SQL query to get the data from. You can specify either `ConnectionTable` or `query` , but not both.

OutputSchemas -> (list)

Specifies the data schema for the custom JDBC source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

SparkConnectorSource -> (structure)

Specifies a connector to an Apache Spark data source.

Name -> (string)

The name of the data source.

ConnectionName -> (string)

The name of the connection that is associated with the connector.

ConnectorName -> (string)

The name of a connector that assists with accessing the data store in Glue Studio.

ConnectionType -> (string)

The type of connection, such as marketplace.spark or custom.spark, designating a connection to an Apache Spark data store.

AdditionalOptions -> (map)

Additional connection options for the connector.

key -> (string)

value -> (string)

OutputSchemas -> (list)

Specifies data schema for the custom spark source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

CatalogSource -> (structure)

Specifies a data store in the Glue Data Catalog.

Name -> (string)

The name of the data store.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

RedshiftSource -> (structure)

Specifies an Amazon Redshift data store.

Name -> (string)

The name of the Amazon Redshift data store.

Database -> (string)

The database to read from.

Table -> (string)

The database table to read from.

RedshiftTmpDir -> (string)

The Amazon S3 path where temporary data can be staged when copying out of the database.

TmpDirIAMRole -> (string)

The IAM role with permissions.

S3CatalogSource -> (structure)

Specifies an Amazon S3 data store in the Glue Data Catalog.

Name -> (string)

The name of the data store.

Database -> (string)

The database to read from.

Table -> (string)

The database table to read from.

PartitionPredicate -> (string)

Partitions satisfying this predicate are deleted. Files within the retention period in these partitions are not deleted. Set to `""` â empty by default.

AdditionalOptions -> (structure)

Specifies additional connection options.

BoundedSize -> (long)

Sets the upper limit for the target size of the dataset in bytes that will be processed.

BoundedFiles -> (long)

Sets the upper limit for the target number of files that will be processed.

S3CsvSource -> (structure)

Specifies a command-separated value (CSV) data store stored in Amazon S3.

Name -> (string)

The name of the data store.

Paths -> (list)

A list of the Amazon S3 paths to read from.

(string)

CompressionType -> (string)

Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"` ).

Exclusions -> (list)

A string containing a JSON list of Unix-style glob patterns to exclude. For example, â["[**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-job.html#id1).pdf"]â excludes all PDF files.

(string)

GroupSize -> (string)

The target group size in bytes. The default is computed based on the input data size and the size of your cluster. When there are fewer than 50,000 input files, `"groupFiles"` must be set to `"inPartition"` for this to take effect.

GroupFiles -> (string)

Grouping files is turned on by default when the input contains more than 50,000 files. To turn on grouping with fewer than 50,000 files, set this parameter to âinPartitionâ. To disable grouping when there are more than 50,000 files, set this parameter to `"none"` .

Recurse -> (boolean)

If set to true, recursively reads files in all subdirectories under the specified paths.

MaxBand -> (integer)

This option controls the duration in milliseconds after which the s3 listing is likely to be consistent. Files with modification timestamps falling within the last maxBand milliseconds are tracked specially when using JobBookmarks to account for Amazon S3 eventual consistency. Most users donât need to set this option. The default is 900000 milliseconds, or 15 minutes.

MaxFilesInBand -> (integer)

This option specifies the maximum number of files to save from the last maxBand seconds. If this number is exceeded, extra files are skipped and only processed in the next job run.

AdditionalOptions -> (structure)

Specifies additional connection options.

BoundedSize -> (long)

Sets the upper limit for the target size of the dataset in bytes that will be processed.

BoundedFiles -> (long)

Sets the upper limit for the target number of files that will be processed.

EnableSamplePath -> (boolean)

Sets option to enable a sample path.

SamplePath -> (string)

If enabled, specifies the sample path.

Separator -> (string)

Specifies the delimiter character. The default is a comma: â,â, but any other character can be specified.

Escaper -> (string)

Specifies a character to use for escaping. This option is used only when reading CSV files. The default value is `none` . If enabled, the character which immediately follows is used as-is, except for a small set of well-known escapes (`\n` , `\r` , `\t` , and `\0` ).

QuoteChar -> (string)

Specifies the character to use for quoting. The default is a double quote: `'"'` . Set this to `-1` to turn off quoting entirely.

Multiline -> (boolean)

A Boolean value that specifies whether a single record can span multiple lines. This can occur when a field contains a quoted new-line character. You must set this option to True if any record spans multiple lines. The default value is `False` , which allows for more aggressive file-splitting during parsing.

WithHeader -> (boolean)

A Boolean value that specifies whether to treat the first line as a header. The default value is `False` .

WriteHeader -> (boolean)

A Boolean value that specifies whether to write the header to output. The default value is `True` .

SkipFirst -> (boolean)

A Boolean value that specifies whether to skip the first data line. The default value is `False` .

OptimizePerformance -> (boolean)

A Boolean value that specifies whether to use the advanced SIMD CSV reader along with Apache Arrow based columnar memory formats. Only available in Glue version 3.0.

OutputSchemas -> (list)

Specifies the data schema for the S3 CSV source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

S3ExcelSource -> (structure)

Defines configuration parameters for reading Excel files from Amazon S3.

Name -> (string)

The name of the S3 Excel data source.

Paths -> (list)

The S3 paths where the Excel files are located.

(string)

CompressionType -> (string)

The compression format used for the Excel files.

Exclusions -> (list)

Patterns to exclude specific files or paths from processing.

(string)

GroupSize -> (string)

Defines the size of file groups for batch processing.

GroupFiles -> (string)

Specifies how files should be grouped for processing.

Recurse -> (boolean)

Indicates whether to recursively process subdirectories.

MaxBand -> (integer)

The maximum number of processing bands to use.

MaxFilesInBand -> (integer)

The maximum number of files to process in each band.

AdditionalOptions -> (structure)

Additional configuration options for S3 direct source processing.

BoundedSize -> (long)

Sets the upper limit for the target size of the dataset in bytes that will be processed.

BoundedFiles -> (long)

Sets the upper limit for the target number of files that will be processed.

EnableSamplePath -> (boolean)

Sets option to enable a sample path.

SamplePath -> (string)

If enabled, specifies the sample path.

NumberRows -> (long)

The number of rows to process from each Excel file.

SkipFooter -> (integer)

The number of rows to skip at the end of each Excel file.

OutputSchemas -> (list)

The AWS Glue schemas to apply to the processed data.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

S3JsonSource -> (structure)

Specifies a JSON data store stored in Amazon S3.

Name -> (string)

The name of the data store.

Paths -> (list)

A list of the Amazon S3 paths to read from.

(string)

CompressionType -> (string)

Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"` ).

Exclusions -> (list)

A string containing a JSON list of Unix-style glob patterns to exclude. For example, â["[**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-job.html#id3).pdf"]â excludes all PDF files.

(string)

GroupSize -> (string)

The target group size in bytes. The default is computed based on the input data size and the size of your cluster. When there are fewer than 50,000 input files, `"groupFiles"` must be set to `"inPartition"` for this to take effect.

GroupFiles -> (string)

Grouping files is turned on by default when the input contains more than 50,000 files. To turn on grouping with fewer than 50,000 files, set this parameter to âinPartitionâ. To disable grouping when there are more than 50,000 files, set this parameter to `"none"` .

Recurse -> (boolean)

If set to true, recursively reads files in all subdirectories under the specified paths.

MaxBand -> (integer)

This option controls the duration in milliseconds after which the s3 listing is likely to be consistent. Files with modification timestamps falling within the last maxBand milliseconds are tracked specially when using JobBookmarks to account for Amazon S3 eventual consistency. Most users donât need to set this option. The default is 900000 milliseconds, or 15 minutes.

MaxFilesInBand -> (integer)

This option specifies the maximum number of files to save from the last maxBand seconds. If this number is exceeded, extra files are skipped and only processed in the next job run.

AdditionalOptions -> (structure)

Specifies additional connection options.

BoundedSize -> (long)

Sets the upper limit for the target size of the dataset in bytes that will be processed.

BoundedFiles -> (long)

Sets the upper limit for the target number of files that will be processed.

EnableSamplePath -> (boolean)

Sets option to enable a sample path.

SamplePath -> (string)

If enabled, specifies the sample path.

JsonPath -> (string)

A JsonPath string defining the JSON data.

Multiline -> (boolean)

A Boolean value that specifies whether a single record can span multiple lines. This can occur when a field contains a quoted new-line character. You must set this option to True if any record spans multiple lines. The default value is `False` , which allows for more aggressive file-splitting during parsing.

OutputSchemas -> (list)

Specifies the data schema for the S3 JSON source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

S3ParquetSource -> (structure)

Specifies an Apache Parquet data store stored in Amazon S3.

Name -> (string)

The name of the data store.

Paths -> (list)

A list of the Amazon S3 paths to read from.

(string)

CompressionType -> (string)

Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"` ).

Exclusions -> (list)

A string containing a JSON list of Unix-style glob patterns to exclude. For example, â["[**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/glue/update-job.html#id5).pdf"]â excludes all PDF files.

(string)

GroupSize -> (string)

The target group size in bytes. The default is computed based on the input data size and the size of your cluster. When there are fewer than 50,000 input files, `"groupFiles"` must be set to `"inPartition"` for this to take effect.

GroupFiles -> (string)

Grouping files is turned on by default when the input contains more than 50,000 files. To turn on grouping with fewer than 50,000 files, set this parameter to âinPartitionâ. To disable grouping when there are more than 50,000 files, set this parameter to `"none"` .

Recurse -> (boolean)

If set to true, recursively reads files in all subdirectories under the specified paths.

MaxBand -> (integer)

This option controls the duration in milliseconds after which the s3 listing is likely to be consistent. Files with modification timestamps falling within the last maxBand milliseconds are tracked specially when using JobBookmarks to account for Amazon S3 eventual consistency. Most users donât need to set this option. The default is 900000 milliseconds, or 15 minutes.

MaxFilesInBand -> (integer)

This option specifies the maximum number of files to save from the last maxBand seconds. If this number is exceeded, extra files are skipped and only processed in the next job run.

AdditionalOptions -> (structure)

Specifies additional connection options.

BoundedSize -> (long)

Sets the upper limit for the target size of the dataset in bytes that will be processed.

BoundedFiles -> (long)

Sets the upper limit for the target number of files that will be processed.

EnableSamplePath -> (boolean)

Sets option to enable a sample path.

SamplePath -> (string)

If enabled, specifies the sample path.

OutputSchemas -> (list)

Specifies the data schema for the S3 Parquet source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

RelationalCatalogSource -> (structure)

Specifies a relational catalog data store in the Glue Data Catalog.

Name -> (string)

The name of the data source.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

DynamoDBCatalogSource -> (structure)

Specifies a DynamoDBC Catalog data store in the Glue Data Catalog.

Name -> (string)

The name of the data source.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

JDBCConnectorTarget -> (structure)

Specifies a data target that writes to Amazon S3 in Apache Parquet columnar storage.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

ConnectionName -> (string)

The name of the connection that is associated with the connector.

ConnectionTable -> (string)

The name of the table in the data target.

ConnectorName -> (string)

The name of a connector that will be used.

ConnectionType -> (string)

The type of connection, such as marketplace.jdbc or custom.jdbc, designating a connection to a JDBC data target.

AdditionalOptions -> (map)

Additional connection options for the connector.

key -> (string)

value -> (string)

OutputSchemas -> (list)

Specifies the data schema for the JDBC target.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

SparkConnectorTarget -> (structure)

Specifies a target that uses an Apache Spark connector.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

ConnectionName -> (string)

The name of a connection for an Apache Spark connector.

ConnectorName -> (string)

The name of an Apache Spark connector.

ConnectionType -> (string)

The type of connection, such as marketplace.spark or custom.spark, designating a connection to an Apache Spark data store.

AdditionalOptions -> (map)

Additional connection options for the connector.

key -> (string)

value -> (string)

OutputSchemas -> (list)

Specifies the data schema for the custom spark target.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

CatalogTarget -> (structure)

Specifies a target that uses a Glue Data Catalog table.

Name -> (string)

The name of your data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

PartitionKeys -> (list)

The partition keys used to distribute data across multiple partitions or shards based on a specific key or set of key.

(list)

(string)

Database -> (string)

The database that contains the table you want to use as the target. This database must already exist in the Data Catalog.

Table -> (string)

The table that defines the schema of your output data. This table must already exist in the Data Catalog.

RedshiftTarget -> (structure)

Specifies a target that uses Amazon Redshift.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

Database -> (string)

The name of the database to write to.

Table -> (string)

The name of the table in the database to write to.

RedshiftTmpDir -> (string)

The Amazon S3 path where temporary data can be staged when copying out of the database.

TmpDirIAMRole -> (string)

The IAM role with permissions.

UpsertRedshiftOptions -> (structure)

The set of options to configure an upsert operation when writing to a Redshift target.

TableLocation -> (string)

The physical location of the Redshift table.

ConnectionName -> (string)

The name of the connection to use to write to Redshift.

UpsertKeys -> (list)

The keys used to determine whether to perform an update or insert.

(string)

S3CatalogTarget -> (structure)

Specifies a data target that writes to Amazon S3 using the Glue Data Catalog.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

PartitionKeys -> (list)

Specifies native partitioning using a sequence of keys.

(list)

(string)

Table -> (string)

The name of the table in the database to write to.

Database -> (string)

The name of the database to write to.

SchemaChangePolicy -> (structure)

A policy that specifies update behavior for the crawler.

EnableUpdateCatalog -> (boolean)

Whether to use the specified update behavior when the crawler finds a changed schema.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

S3GlueParquetTarget -> (structure)

Specifies a data target that writes to Amazon S3 in Apache Parquet columnar storage.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

PartitionKeys -> (list)

Specifies native partitioning using a sequence of keys.

(list)

(string)

Path -> (string)

A single Amazon S3 path to write to.

Compression -> (string)

Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"` ).

NumberTargetPartitions -> (string)

Specifies the number of target partitions for Parquet files when writing to Amazon S3 using AWS Glue.

SchemaChangePolicy -> (structure)

A policy that specifies update behavior for the crawler.

EnableUpdateCatalog -> (boolean)

Whether to use the specified update behavior when the crawler finds a changed schema.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

Table -> (string)

Specifies the table in the database that the schema change policy applies to.

Database -> (string)

Specifies the database that the schema change policy applies to.

S3HyperDirectTarget -> (structure)

Defines configuration parameters for writing data to Amazon S3 using HyperDirect optimization.

Name -> (string)

The unique identifier for the HyperDirect target node.

Inputs -> (list)

Specifies the input source for the HyperDirect target.

(string)

PartitionKeys -> (list)

Defines the partitioning strategy for the output data.

(list)

(string)

Path -> (string)

The S3 location where the output data will be written.

Compression -> (string)

The compression type to apply to the output data.

SchemaChangePolicy -> (structure)

Defines how schema changes are handled during write operations.

EnableUpdateCatalog -> (boolean)

Whether to use the specified update behavior when the crawler finds a changed schema.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

Table -> (string)

Specifies the table in the database that the schema change policy applies to.

Database -> (string)

Specifies the database that the schema change policy applies to.

S3DirectTarget -> (structure)

Specifies a data target that writes to Amazon S3.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

PartitionKeys -> (list)

Specifies native partitioning using a sequence of keys.

(list)

(string)

Path -> (string)

A single Amazon S3 path to write to.

Compression -> (string)

Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"` ).

NumberTargetPartitions -> (string)

Specifies the number of target partitions when writing data directly to Amazon S3.

Format -> (string)

Specifies the data output format for the target.

SchemaChangePolicy -> (structure)

A policy that specifies update behavior for the crawler.

EnableUpdateCatalog -> (boolean)

Whether to use the specified update behavior when the crawler finds a changed schema.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

Table -> (string)

Specifies the table in the database that the schema change policy applies to.

Database -> (string)

Specifies the database that the schema change policy applies to.

S3IcebergDirectTarget -> (structure)

Defines configuration parameters for writing data to Amazon S3 as an Apache Iceberg table.

Name -> (string)

Specifies the unique identifier for the Iceberg target node in your data pipeline.

Inputs -> (list)

Defines the single input source that provides data to this Iceberg target.

(string)

PartitionKeys -> (list)

Specifies the columns used to partition the Iceberg table data in S3.

(list)

(string)

Path -> (string)

Defines the S3 location where the Iceberg table data will be stored.

Format -> (string)

Specifies the file format used for storing Iceberg table data (e.g., Parquet, ORC).

AdditionalOptions -> (map)

Provides additional configuration options for customizing the Iceberg table behavior.

key -> (string)

value -> (string)

SchemaChangePolicy -> (structure)

Defines how schema changes are handled when writing data to the Iceberg table.

EnableUpdateCatalog -> (boolean)

Whether to use the specified update behavior when the crawler finds a changed schema.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

Table -> (string)

Specifies the table in the database that the schema change policy applies to.

Database -> (string)

Specifies the database that the schema change policy applies to.

Compression -> (string)

Specifies the compression codec used for Iceberg table files in S3.

NumberTargetPartitions -> (string)

Sets the number of target partitions for distributing Iceberg table files across S3.

ApplyMapping -> (structure)

Specifies a transform that maps data property keys in the data source to data property keys in the data target. You can rename keys, modify the data types for keys, and choose which keys to drop from the dataset.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

Mapping -> (list)

Specifies the mapping of data property keys in the data source to data property keys in the data target.

(structure)

Specifies the mapping of data property keys.

ToKey -> (string)

After the apply mapping, what the name of the column should be. Can be the same as `FromPath` .

FromPath -> (list)

The table or column to be modified.

(string)

FromType -> (string)

The type of the data to be modified.

ToType -> (string)

The data type that the data is to be modified to.

Dropped -> (boolean)

If true, then the column is removed.

Children -> (list)

Only applicable to nested data structures. If you want to change the parent structure, but also one of its children, you can fill out this data strucutre. It is also `Mapping` , but its `FromPath` will be the parentâs `FromPath` plus the `FromPath` from this structure.

For the children part, suppose you have the structure:

`{ "FromPath": "OuterStructure", "ToKey": "OuterStructure", "ToType": "Struct", "Dropped": false, "Chidlren": [{ "FromPath": "inner", "ToKey": "inner", "ToType": "Double", "Dropped": false, }] }`

You can specify a `Mapping` that looks like:

`{ "FromPath": "OuterStructure", "ToKey": "OuterStructure", "ToType": "Struct", "Dropped": false, "Chidlren": [{ "FromPath": "inner", "ToKey": "inner", "ToType": "Double", "Dropped": false, }] }`

(structure)

Specifies the mapping of data property keys.

ToKey -> (string)

After the apply mapping, what the name of the column should be. Can be the same as `FromPath` .

FromPath -> (list)

The table or column to be modified.

(string)

FromType -> (string)

The type of the data to be modified.

ToType -> (string)

The data type that the data is to be modified to.

Dropped -> (boolean)

If true, then the column is removed.

SelectFields -> (structure)

Specifies a transform that chooses the data property keys that you want to keep.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

Paths -> (list)

A JSON path to a variable in the data structure.

(list)

(string)

DropFields -> (structure)

Specifies a transform that chooses the data property keys that you want to drop.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

Paths -> (list)

A JSON path to a variable in the data structure.

(list)

(string)

RenameField -> (structure)

Specifies a transform that renames a single data property key.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

SourcePath -> (list)

A JSON path to a variable in the data structure for the source data.

(string)

TargetPath -> (list)

A JSON path to a variable in the data structure for the target data.

(string)

Spigot -> (structure)

Specifies a transform that writes samples of the data to an Amazon S3 bucket.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

Path -> (string)

A path in Amazon S3 where the transform will write a subset of records from the dataset to a JSON file in an Amazon S3 bucket.

Topk -> (integer)

Specifies a number of records to write starting from the beginning of the dataset.

Prob -> (double)

The probability (a decimal value with a maximum value of 1) of picking any given record. A value of 1 indicates that each row read from the dataset should be included in the sample output.

Join -> (structure)

Specifies a transform that joins two datasets into one dataset using a comparison phrase on the specified data property keys. You can use inner, outer, left, right, left semi, and left anti joins.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

JoinType -> (string)

Specifies the type of join to be performed on the datasets.

Columns -> (list)

A list of the two columns to be joined.

(structure)

Specifies a column to be joined.

From -> (string)

The column to be joined.

Keys -> (list)

The key of the column to be joined.

(list)

(string)

SplitFields -> (structure)

Specifies a transform that splits data property keys into two `DynamicFrames` . The output is a collection of `DynamicFrames` : one with selected data property keys, and one with the remaining data property keys.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

Paths -> (list)

A JSON path to a variable in the data structure.

(list)

(string)

SelectFromCollection -> (structure)

Specifies a transform that chooses one `DynamicFrame` from a collection of `DynamicFrames` . The output is the selected `DynamicFrame`

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

Index -> (integer)

The index for the DynamicFrame to be selected.

FillMissingValues -> (structure)

Specifies a transform that locates records in the dataset that have missing values and adds a new field with a value determined by imputation. The input data set is used to train the machine learning model that determines what the missing value should be.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

ImputedPath -> (string)

A JSON path to a variable in the data structure for the dataset that is imputed.

FilledPath -> (string)

A JSON path to a variable in the data structure for the dataset that is filled.

Filter -> (structure)

Specifies a transform that splits a dataset into two, based on a filter condition.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

LogicalOperator -> (string)

The operator used to filter rows by comparing the key value to a specified value.

Filters -> (list)

Specifies a filter expression.

(structure)

Specifies a filter expression.

Operation -> (string)

The type of operation to perform in the expression.

Negated -> (boolean)

Whether the expression is to be negated.

Values -> (list)

A list of filter values.

(structure)

Represents a single entry in the list of values for a `FilterExpression` .

Type -> (string)

The type of filter value.

Value -> (list)

The value to be associated.

(string)

CustomCode -> (structure)

Specifies a transform that uses custom code you provide to perform the data transformation. The output is a collection of DynamicFrames.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

Code -> (string)

The custom code that is used to perform the data transformation.

ClassName -> (string)

The name defined for the custom code node class.

OutputSchemas -> (list)

Specifies the data schema for the custom code transform.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

SparkSQL -> (structure)

Specifies a transform where you enter a SQL query using Spark SQL syntax to transform the data. The output is a single `DynamicFrame` .

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names. You can associate a table name with each input node to use in the SQL query. The name you choose must meet the Spark SQL naming restrictions.

(string)

SqlQuery -> (string)

A SQL query that must use Spark SQL syntax and return a single data set.

SqlAliases -> (list)

A list of aliases. An alias allows you to specify what name to use in the SQL for a given input. For example, you have a datasource named âMyDataSourceâ. If you specify `From` as MyDataSource, and `Alias` as SqlName, then in your SQL you can do:

`select * from SqlName`

and that gets data from MyDataSource.

(structure)

Represents a single entry in the list of values for `SqlAliases` .

From -> (string)

A table, or a column in a table.

Alias -> (string)

A temporary name given to a table, or a column in a table.

OutputSchemas -> (list)

Specifies the data schema for the SparkSQL transform.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

DirectKinesisSource -> (structure)

Specifies a direct Amazon Kinesis data source.

Name -> (string)

The name of the data source.

WindowSize -> (integer)

The amount of time to spend processing each micro batch.

DetectSchema -> (boolean)

Whether to automatically determine the schema from the incoming data.

StreamingOptions -> (structure)

Additional options for the Kinesis streaming data source.

EndpointUrl -> (string)

The URL of the Kinesis endpoint.

StreamName -> (string)

The name of the Kinesis data stream.

Classification -> (string)

An optional classification.

Delimiter -> (string)

Specifies the delimiter character.

StartingPosition -> (string)

The starting position in the Kinesis data stream to read data from. The possible values are `"latest"` , `"trim_horizon"` , `"earliest"` , or a timestamp string in UTC format in the pattern `yyyy-mm-ddTHH:MM:SSZ` (where `Z` represents a UTC timezone offset with a +/-. For example: â2023-04-04T08:00:00-04:00â). The default value is `"latest"` .

Note: Using a value that is a timestamp string in UTC format for âstartingPositionâ is supported only for Glue version 4.0 or later.

MaxFetchTimeInMs -> (long)

The maximum time spent for the job executor to read records for the current batch from the Kinesis data stream, specified in milliseconds (ms). Multiple `GetRecords` API calls may be made within this time. The default value is `1000` .

MaxFetchRecordsPerShard -> (long)

The maximum number of records to fetch per shard in the Kinesis data stream per microbatch. Note: The client can exceed this limit if the streaming job has already read extra records from Kinesis (in the same get-records call). If `MaxFetchRecordsPerShard` needs to be strict then it needs to be a multiple of `MaxRecordPerRead` . The default value is `100000` .

MaxRecordPerRead -> (long)

The maximum number of records to fetch from the Kinesis data stream in each getRecords operation. The default value is `10000` .

AddIdleTimeBetweenReads -> (boolean)

Adds a time delay between two consecutive getRecords operations. The default value is `"False"` . This option is only configurable for Glue version 2.0 and above.

IdleTimeBetweenReadsInMs -> (long)

The minimum time delay between two consecutive getRecords operations, specified in ms. The default value is `1000` . This option is only configurable for Glue version 2.0 and above.

DescribeShardInterval -> (long)

The minimum time interval between two ListShards API calls for your script to consider resharding. The default value is `1s` .

NumRetries -> (integer)

The maximum number of retries for Kinesis Data Streams API requests. The default value is `3` .

RetryIntervalMs -> (long)

The cool-off time period (specified in ms) before retrying the Kinesis Data Streams API call. The default value is `1000` .

MaxRetryIntervalMs -> (long)

The maximum cool-off time period (specified in ms) between two retries of a Kinesis Data Streams API call. The default value is `10000` .

AvoidEmptyBatches -> (boolean)

Avoids creating an empty microbatch job by checking for unread data in the Kinesis data stream before the batch is started. The default value is `"False"` .

StreamArn -> (string)

The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role to assume using AWS Security Token Service (AWS STS). This role must have permissions for describe or read record operations for the Kinesis data stream. You must use this parameter when accessing a data stream in a different account. Used in conjunction with `"awsSTSSessionName"` .

RoleSessionName -> (string)

An identifier for the session assuming the role using AWS STS. You must use this parameter when accessing a data stream in a different account. Used in conjunction with `"awsSTSRoleARN"` .

AddRecordTimestamp -> (string)

When this option is set to âtrueâ, the data output will contain an additional column named â__src_timestampâ that indicates the time when the corresponding record received by the stream. The default value is âfalseâ. This option is supported in Glue version 4.0 or later.

EmitConsumerLagMetrics -> (string)

When this option is set to âtrueâ, for each batch, it will emit the metrics for the duration between the oldest record received by the stream and the time it arrives in Glue to CloudWatch. The metricâs name is âglue.driver.streaming.maxConsumerLagInMsâ. The default value is âfalseâ. This option is supported in Glue version 4.0 or later.

StartingTimestamp -> (timestamp)

The timestamp of the record in the Kinesis data stream to start reading data from. The possible values are a timestamp string in UTC format of the pattern `yyyy-mm-ddTHH:MM:SSZ` (where Z represents a UTC timezone offset with a +/-. For example: â2023-04-04T08:00:00+08:00â).

DataPreviewOptions -> (structure)

Additional options for data preview.

PollingTime -> (long)

The polling time in milliseconds.

RecordPollingLimit -> (long)

The limit to the number of records polled.

DirectKafkaSource -> (structure)

Specifies an Apache Kafka data store.

Name -> (string)

The name of the data store.

StreamingOptions -> (structure)

Specifies the streaming options.

BootstrapServers -> (string)

A list of bootstrap server URLs, for example, as `b-1.vpc-test-2.o4q88o.c6.kafka.us-east-1.amazonaws.com:9094` . This option must be specified in the API call or defined in the table metadata in the Data Catalog.

SecurityProtocol -> (string)

The protocol used to communicate with brokers. The possible values are `"SSL"` or `"PLAINTEXT"` .

ConnectionName -> (string)

The name of the connection.

TopicName -> (string)

The topic name as specified in Apache Kafka. You must specify at least one of `"topicName"` , `"assign"` or `"subscribePattern"` .

Assign -> (string)

The specific `TopicPartitions` to consume. You must specify at least one of `"topicName"` , `"assign"` or `"subscribePattern"` .

SubscribePattern -> (string)

A Java regex string that identifies the topic list to subscribe to. You must specify at least one of `"topicName"` , `"assign"` or `"subscribePattern"` .

Classification -> (string)

An optional classification.

Delimiter -> (string)

Specifies the delimiter character.

StartingOffsets -> (string)

The starting position in the Kafka topic to read data from. The possible values are `"earliest"` or `"latest"` . The default value is `"latest"` .

EndingOffsets -> (string)

The end point when a batch query is ended. Possible values are either `"latest"` or a JSON string that specifies an ending offset for each `TopicPartition` .

PollTimeoutMs -> (long)

The timeout in milliseconds to poll data from Kafka in Spark job executors. The default value is `512` .

NumRetries -> (integer)

The number of times to retry before failing to fetch Kafka offsets. The default value is `3` .

RetryIntervalMs -> (long)

The time in milliseconds to wait before retrying to fetch Kafka offsets. The default value is `10` .

MaxOffsetsPerTrigger -> (long)

The rate limit on the maximum number of offsets that are processed per trigger interval. The specified total number of offsets is proportionally split across `topicPartitions` of different volumes. The default value is null, which means that the consumer reads all offsets until the known latest offset.

MinPartitions -> (integer)

The desired minimum number of partitions to read from Kafka. The default value is null, which means that the number of spark partitions is equal to the number of Kafka partitions.

IncludeHeaders -> (boolean)

Whether to include the Kafka headers. When the option is set to âtrueâ, the data output will contain an additional column named âglue_streaming_kafka_headersâ with type `Array[Struct(key: String, value: String)]` . The default value is âfalseâ. This option is available in Glue version 3.0 or later only.

AddRecordTimestamp -> (string)

When this option is set to âtrueâ, the data output will contain an additional column named â__src_timestampâ that indicates the time when the corresponding record received by the topic. The default value is âfalseâ. This option is supported in Glue version 4.0 or later.

EmitConsumerLagMetrics -> (string)

When this option is set to âtrueâ, for each batch, it will emit the metrics for the duration between the oldest record received by the topic and the time it arrives in Glue to CloudWatch. The metricâs name is âglue.driver.streaming.maxConsumerLagInMsâ. The default value is âfalseâ. This option is supported in Glue version 4.0 or later.

StartingTimestamp -> (timestamp)

The timestamp of the record in the Kafka topic to start reading data from. The possible values are a timestamp string in UTC format of the pattern `yyyy-mm-ddTHH:MM:SSZ` (where Z represents a UTC timezone offset with a +/-. For example: â2023-04-04T08:00:00+08:00â).

Only one of `StartingTimestamp` or `StartingOffsets` must be set.

WindowSize -> (integer)

The amount of time to spend processing each micro batch.

DetectSchema -> (boolean)

Whether to automatically determine the schema from the incoming data.

DataPreviewOptions -> (structure)

Specifies options related to data preview for viewing a sample of your data.

PollingTime -> (long)

The polling time in milliseconds.

RecordPollingLimit -> (long)

The limit to the number of records polled.

CatalogKinesisSource -> (structure)

Specifies a Kinesis data source in the Glue Data Catalog.

Name -> (string)

The name of the data source.

WindowSize -> (integer)

The amount of time to spend processing each micro batch.

DetectSchema -> (boolean)

Whether to automatically determine the schema from the incoming data.

Table -> (string)

The name of the table in the database to read from.

Database -> (string)

The name of the database to read from.

StreamingOptions -> (structure)

Additional options for the Kinesis streaming data source.

EndpointUrl -> (string)

The URL of the Kinesis endpoint.

StreamName -> (string)

The name of the Kinesis data stream.

Classification -> (string)

An optional classification.

Delimiter -> (string)

Specifies the delimiter character.

StartingPosition -> (string)

The starting position in the Kinesis data stream to read data from. The possible values are `"latest"` , `"trim_horizon"` , `"earliest"` , or a timestamp string in UTC format in the pattern `yyyy-mm-ddTHH:MM:SSZ` (where `Z` represents a UTC timezone offset with a +/-. For example: â2023-04-04T08:00:00-04:00â). The default value is `"latest"` .

Note: Using a value that is a timestamp string in UTC format for âstartingPositionâ is supported only for Glue version 4.0 or later.

MaxFetchTimeInMs -> (long)

The maximum time spent for the job executor to read records for the current batch from the Kinesis data stream, specified in milliseconds (ms). Multiple `GetRecords` API calls may be made within this time. The default value is `1000` .

MaxFetchRecordsPerShard -> (long)

The maximum number of records to fetch per shard in the Kinesis data stream per microbatch. Note: The client can exceed this limit if the streaming job has already read extra records from Kinesis (in the same get-records call). If `MaxFetchRecordsPerShard` needs to be strict then it needs to be a multiple of `MaxRecordPerRead` . The default value is `100000` .

MaxRecordPerRead -> (long)

The maximum number of records to fetch from the Kinesis data stream in each getRecords operation. The default value is `10000` .

AddIdleTimeBetweenReads -> (boolean)

Adds a time delay between two consecutive getRecords operations. The default value is `"False"` . This option is only configurable for Glue version 2.0 and above.

IdleTimeBetweenReadsInMs -> (long)

The minimum time delay between two consecutive getRecords operations, specified in ms. The default value is `1000` . This option is only configurable for Glue version 2.0 and above.

DescribeShardInterval -> (long)

The minimum time interval between two ListShards API calls for your script to consider resharding. The default value is `1s` .

NumRetries -> (integer)

The maximum number of retries for Kinesis Data Streams API requests. The default value is `3` .

RetryIntervalMs -> (long)

The cool-off time period (specified in ms) before retrying the Kinesis Data Streams API call. The default value is `1000` .

MaxRetryIntervalMs -> (long)

The maximum cool-off time period (specified in ms) between two retries of a Kinesis Data Streams API call. The default value is `10000` .

AvoidEmptyBatches -> (boolean)

Avoids creating an empty microbatch job by checking for unread data in the Kinesis data stream before the batch is started. The default value is `"False"` .

StreamArn -> (string)

The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the role to assume using AWS Security Token Service (AWS STS). This role must have permissions for describe or read record operations for the Kinesis data stream. You must use this parameter when accessing a data stream in a different account. Used in conjunction with `"awsSTSSessionName"` .

RoleSessionName -> (string)

An identifier for the session assuming the role using AWS STS. You must use this parameter when accessing a data stream in a different account. Used in conjunction with `"awsSTSRoleARN"` .

AddRecordTimestamp -> (string)

When this option is set to âtrueâ, the data output will contain an additional column named â__src_timestampâ that indicates the time when the corresponding record received by the stream. The default value is âfalseâ. This option is supported in Glue version 4.0 or later.

EmitConsumerLagMetrics -> (string)

When this option is set to âtrueâ, for each batch, it will emit the metrics for the duration between the oldest record received by the stream and the time it arrives in Glue to CloudWatch. The metricâs name is âglue.driver.streaming.maxConsumerLagInMsâ. The default value is âfalseâ. This option is supported in Glue version 4.0 or later.

StartingTimestamp -> (timestamp)

The timestamp of the record in the Kinesis data stream to start reading data from. The possible values are a timestamp string in UTC format of the pattern `yyyy-mm-ddTHH:MM:SSZ` (where Z represents a UTC timezone offset with a +/-. For example: â2023-04-04T08:00:00+08:00â).

DataPreviewOptions -> (structure)

Additional options for data preview.

PollingTime -> (long)

The polling time in milliseconds.

RecordPollingLimit -> (long)

The limit to the number of records polled.

CatalogKafkaSource -> (structure)

Specifies an Apache Kafka data store in the Data Catalog.

Name -> (string)

The name of the data store.

WindowSize -> (integer)

The amount of time to spend processing each micro batch.

DetectSchema -> (boolean)

Whether to automatically determine the schema from the incoming data.

Table -> (string)

The name of the table in the database to read from.

Database -> (string)

The name of the database to read from.

StreamingOptions -> (structure)

Specifies the streaming options.

BootstrapServers -> (string)

A list of bootstrap server URLs, for example, as `b-1.vpc-test-2.o4q88o.c6.kafka.us-east-1.amazonaws.com:9094` . This option must be specified in the API call or defined in the table metadata in the Data Catalog.

SecurityProtocol -> (string)

The protocol used to communicate with brokers. The possible values are `"SSL"` or `"PLAINTEXT"` .

ConnectionName -> (string)

The name of the connection.

TopicName -> (string)

The topic name as specified in Apache Kafka. You must specify at least one of `"topicName"` , `"assign"` or `"subscribePattern"` .

Assign -> (string)

The specific `TopicPartitions` to consume. You must specify at least one of `"topicName"` , `"assign"` or `"subscribePattern"` .

SubscribePattern -> (string)

A Java regex string that identifies the topic list to subscribe to. You must specify at least one of `"topicName"` , `"assign"` or `"subscribePattern"` .

Classification -> (string)

An optional classification.

Delimiter -> (string)

Specifies the delimiter character.

StartingOffsets -> (string)

The starting position in the Kafka topic to read data from. The possible values are `"earliest"` or `"latest"` . The default value is `"latest"` .

EndingOffsets -> (string)

The end point when a batch query is ended. Possible values are either `"latest"` or a JSON string that specifies an ending offset for each `TopicPartition` .

PollTimeoutMs -> (long)

The timeout in milliseconds to poll data from Kafka in Spark job executors. The default value is `512` .

NumRetries -> (integer)

The number of times to retry before failing to fetch Kafka offsets. The default value is `3` .

RetryIntervalMs -> (long)

The time in milliseconds to wait before retrying to fetch Kafka offsets. The default value is `10` .

MaxOffsetsPerTrigger -> (long)

The rate limit on the maximum number of offsets that are processed per trigger interval. The specified total number of offsets is proportionally split across `topicPartitions` of different volumes. The default value is null, which means that the consumer reads all offsets until the known latest offset.

MinPartitions -> (integer)

The desired minimum number of partitions to read from Kafka. The default value is null, which means that the number of spark partitions is equal to the number of Kafka partitions.

IncludeHeaders -> (boolean)

Whether to include the Kafka headers. When the option is set to âtrueâ, the data output will contain an additional column named âglue_streaming_kafka_headersâ with type `Array[Struct(key: String, value: String)]` . The default value is âfalseâ. This option is available in Glue version 3.0 or later only.

AddRecordTimestamp -> (string)

When this option is set to âtrueâ, the data output will contain an additional column named â__src_timestampâ that indicates the time when the corresponding record received by the topic. The default value is âfalseâ. This option is supported in Glue version 4.0 or later.

EmitConsumerLagMetrics -> (string)

When this option is set to âtrueâ, for each batch, it will emit the metrics for the duration between the oldest record received by the topic and the time it arrives in Glue to CloudWatch. The metricâs name is âglue.driver.streaming.maxConsumerLagInMsâ. The default value is âfalseâ. This option is supported in Glue version 4.0 or later.

StartingTimestamp -> (timestamp)

The timestamp of the record in the Kafka topic to start reading data from. The possible values are a timestamp string in UTC format of the pattern `yyyy-mm-ddTHH:MM:SSZ` (where Z represents a UTC timezone offset with a +/-. For example: â2023-04-04T08:00:00+08:00â).

Only one of `StartingTimestamp` or `StartingOffsets` must be set.

DataPreviewOptions -> (structure)

Specifies options related to data preview for viewing a sample of your data.

PollingTime -> (long)

The polling time in milliseconds.

RecordPollingLimit -> (long)

The limit to the number of records polled.

DropNullFields -> (structure)

Specifies a transform that removes columns from the dataset if all values in the column are ânullâ. By default, Glue Studio will recognize null objects, but some values such as empty strings, strings that are ânullâ, -1 integers or other placeholders such as zeros, are not automatically recognized as nulls.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

NullCheckBoxList -> (structure)

A structure that represents whether certain values are recognized as null values for removal.

IsEmpty -> (boolean)

Specifies that an empty string is considered as a null value.

IsNullString -> (boolean)

Specifies that a value spelling out the word ânullâ is considered as a null value.

IsNegOne -> (boolean)

Specifies that an integer value of -1 is considered as a null value.

NullTextList -> (list)

A structure that specifies a list of NullValueField structures that represent a custom null value such as zero or other value being used as a null placeholder unique to the dataset.

The `DropNullFields` transform removes custom null values only if both the value of the null placeholder and the datatype match the data.

(structure)

Represents a custom null value such as a zeros or other value being used as a null placeholder unique to the dataset.

Value -> (string)

The value of the null placeholder.

Datatype -> (structure)

The datatype of the value.

Id -> (string)

The datatype of the value.

Label -> (string)

A label assigned to the datatype.

Merge -> (structure)

Specifies a transform that merges a `DynamicFrame` with a staging `DynamicFrame` based on the specified primary keys to identify records. Duplicate records (records with the same primary keys) are not de-duplicated.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

Source -> (string)

The source `DynamicFrame` that will be merged with a staging `DynamicFrame` .

PrimaryKeys -> (list)

The list of primary key fields to match records from the source and staging dynamic frames.

(list)

(string)

Union -> (structure)

Specifies a transform that combines the rows from two or more datasets into a single result.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The node ID inputs to the transform.

(string)

UnionType -> (string)

Indicates the type of Union transform.

Specify `ALL` to join all rows from data sources to the resulting DynamicFrame. The resulting union does not remove duplicate rows.

Specify `DISTINCT` to remove duplicate rows in the resulting DynamicFrame.

PIIDetection -> (structure)

Specifies a transform that identifies, removes or masks PII data.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The node ID inputs to the transform.

(string)

PiiType -> (string)

Indicates the type of PIIDetection transform.

EntityTypesToDetect -> (list)

Indicates the types of entities the PIIDetection transform will identify as PII data.

PII type entities include: PERSON_NAME, DATE, USA_SNN, EMAIL, USA_ITIN, USA_PASSPORT_NUMBER, PHONE_NUMBER, BANK_ACCOUNT, IP_ADDRESS, MAC_ADDRESS, USA_CPT_CODE, USA_HCPCS_CODE, USA_NATIONAL_DRUG_CODE, USA_MEDICARE_BENEFICIARY_IDENTIFIER, USA_HEALTH_INSURANCE_CLAIM_NUMBER,CREDIT_CARD,USA_NATIONAL_PROVIDER_IDENTIFIER,USA_DEA_NUMBER,USA_DRIVING_LICENSE

(string)

OutputColumnName -> (string)

Indicates the output column name that will contain any entity type detected in that row.

SampleFraction -> (double)

Indicates the fraction of the data to sample when scanning for PII entities.

ThresholdFraction -> (double)

Indicates the fraction of the data that must be met in order for a column to be identified as PII data.

MaskValue -> (string)

Indicates the value that will replace the detected entity.

Aggregate -> (structure)

Specifies a transform that groups rows by chosen fields and computes the aggregated value by specified function.

Name -> (string)

The name of the transform node.

Inputs -> (list)

Specifies the fields and rows to use as inputs for the aggregate transform.

(string)

Groups -> (list)

Specifies the fields to group by.

(list)

(string)

Aggs -> (list)

Specifies the aggregate functions to be performed on specified fields.

(structure)

Specifies the set of parameters needed to perform aggregation in the aggregate transform.

Column -> (list)

Specifies the column on the data set on which the aggregation function will be applied.

(string)

AggFunc -> (string)

Specifies the aggregation function to apply.

Possible aggregation functions include: avg countDistinct, count, first, last, kurtosis, max, min, skewness, stddev_samp, stddev_pop, sum, sumDistinct, var_samp, var_pop

DropDuplicates -> (structure)

Specifies a transform that removes rows of repeating data from a data set.

Name -> (string)

The name of the transform node.

Inputs -> (list)

The data inputs identified by their node names.

(string)

Columns -> (list)

The name of the columns to be merged or removed if repeating.

(list)

(string)

GovernedCatalogTarget -> (structure)

Specifies a data target that writes to a goverened catalog.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

PartitionKeys -> (list)

Specifies native partitioning using a sequence of keys.

(list)

(string)

Table -> (string)

The name of the table in the database to write to.

Database -> (string)

The name of the database to write to.

SchemaChangePolicy -> (structure)

A policy that specifies update behavior for the governed catalog.

EnableUpdateCatalog -> (boolean)

Whether to use the specified update behavior when the crawler finds a changed schema.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

GovernedCatalogSource -> (structure)

Specifies a data source in a goverened Data Catalog.

Name -> (string)

The name of the data store.

Database -> (string)

The database to read from.

Table -> (string)

The database table to read from.

PartitionPredicate -> (string)

Partitions satisfying this predicate are deleted. Files within the retention period in these partitions are not deleted. Set to `""` â empty by default.

AdditionalOptions -> (structure)

Specifies additional connection options.

BoundedSize -> (long)

Sets the upper limit for the target size of the dataset in bytes that will be processed.

BoundedFiles -> (long)

Sets the upper limit for the target number of files that will be processed.

MicrosoftSQLServerCatalogSource -> (structure)

Specifies a Microsoft SQL server data source in the Glue Data Catalog.

Name -> (string)

The name of the data source.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

MySQLCatalogSource -> (structure)

Specifies a MySQL data source in the Glue Data Catalog.

Name -> (string)

The name of the data source.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

OracleSQLCatalogSource -> (structure)

Specifies an Oracle data source in the Glue Data Catalog.

Name -> (string)

The name of the data source.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

PostgreSQLCatalogSource -> (structure)

Specifies a PostgresSQL data source in the Glue Data Catalog.

Name -> (string)

The name of the data source.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

MicrosoftSQLServerCatalogTarget -> (structure)

Specifies a target that uses Microsoft SQL.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

Database -> (string)

The name of the database to write to.

Table -> (string)

The name of the table in the database to write to.

MySQLCatalogTarget -> (structure)

Specifies a target that uses MySQL.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

Database -> (string)

The name of the database to write to.

Table -> (string)

The name of the table in the database to write to.

OracleSQLCatalogTarget -> (structure)

Specifies a target that uses Oracle SQL.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

Database -> (string)

The name of the database to write to.

Table -> (string)

The name of the table in the database to write to.

PostgreSQLCatalogTarget -> (structure)

Specifies a target that uses Postgres SQL.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

Database -> (string)

The name of the database to write to.

Table -> (string)

The name of the table in the database to write to.

DynamicTransform -> (structure)

Specifies a custom visual transform created by a user.

Name -> (string)

Specifies the name of the dynamic transform.

TransformName -> (string)

Specifies the name of the dynamic transform as it appears in the Glue Studio visual editor.

Inputs -> (list)

Specifies the inputs for the dynamic transform that are required.

(string)

Parameters -> (list)

Specifies the parameters of the dynamic transform.

(structure)

Specifies the parameters in the config file of the dynamic transform.

Name -> (string)

Specifies the name of the parameter in the config file of the dynamic transform.

Type -> (string)

Specifies the parameter type in the config file of the dynamic transform.

ValidationRule -> (string)

Specifies the validation rule in the config file of the dynamic transform.

ValidationMessage -> (string)

Specifies the validation message in the config file of the dynamic transform.

Value -> (list)

Specifies the value of the parameter in the config file of the dynamic transform.

(string)

ListType -> (string)

Specifies the list type of the parameter in the config file of the dynamic transform.

IsOptional -> (boolean)

Specifies whether the parameter is optional or not in the config file of the dynamic transform.

FunctionName -> (string)

Specifies the name of the function of the dynamic transform.

Path -> (string)

Specifies the path of the dynamic transform source and config files.

Version -> (string)

This field is not used and will be deprecated in future release.

OutputSchemas -> (list)

Specifies the data schema for the dynamic transform.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

EvaluateDataQuality -> (structure)

Specifies your data quality evaluation criteria.

Name -> (string)

The name of the data quality evaluation.

Inputs -> (list)

The inputs of your data quality evaluation.

(string)

Ruleset -> (string)

The ruleset for your data quality evaluation.

Output -> (string)

The output of your data quality evaluation.

PublishingOptions -> (structure)

Options to configure how your results are published.

EvaluationContext -> (string)

The context of the evaluation.

ResultsS3Prefix -> (string)

The Amazon S3 prefix prepended to the results.

CloudWatchMetricsEnabled -> (boolean)

Enable metrics for your data quality results.

ResultsPublishingEnabled -> (boolean)

Enable publishing for your data quality results.

StopJobOnFailureOptions -> (structure)

Options to configure how your job will stop if your data quality evaluation fails.

StopJobOnFailureTiming -> (string)

When to stop job if your data quality evaluation fails. Options are Immediate or AfterDataLoad.

S3CatalogHudiSource -> (structure)

Specifies a Hudi data source that is registered in the Glue Data Catalog. The data source must be stored in Amazon S3.

Name -> (string)

The name of the Hudi data source.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

AdditionalHudiOptions -> (map)

Specifies additional connection options.

key -> (string)

value -> (string)

OutputSchemas -> (list)

Specifies the data schema for the Hudi source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

CatalogHudiSource -> (structure)

Specifies a Hudi data source that is registered in the Glue Data Catalog.

Name -> (string)

The name of the Hudi data source.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

AdditionalHudiOptions -> (map)

Specifies additional connection options.

key -> (string)

value -> (string)

OutputSchemas -> (list)

Specifies the data schema for the Hudi source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

S3HudiSource -> (structure)

Specifies a Hudi data source stored in Amazon S3.

Name -> (string)

The name of the Hudi source.

Paths -> (list)

A list of the Amazon S3 paths to read from.

(string)

AdditionalHudiOptions -> (map)

Specifies additional connection options.

key -> (string)

value -> (string)

AdditionalOptions -> (structure)

Specifies additional options for the connector.

BoundedSize -> (long)

Sets the upper limit for the target size of the dataset in bytes that will be processed.

BoundedFiles -> (long)

Sets the upper limit for the target number of files that will be processed.

EnableSamplePath -> (boolean)

Sets option to enable a sample path.

SamplePath -> (string)

If enabled, specifies the sample path.

OutputSchemas -> (list)

Specifies the data schema for the Hudi source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

S3HudiCatalogTarget -> (structure)

Specifies a target that writes to a Hudi data source in the Glue Data Catalog.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

PartitionKeys -> (list)

Specifies native partitioning using a sequence of keys.

(list)

(string)

Table -> (string)

The name of the table in the database to write to.

Database -> (string)

The name of the database to write to.

AdditionalOptions -> (map)

Specifies additional connection options for the connector.

key -> (string)

value -> (string)

SchemaChangePolicy -> (structure)

A policy that specifies update behavior for the crawler.

EnableUpdateCatalog -> (boolean)

Whether to use the specified update behavior when the crawler finds a changed schema.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

S3HudiDirectTarget -> (structure)

Specifies a target that writes to a Hudi data source in Amazon S3.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

Path -> (string)

The Amazon S3 path of your Hudi data source to write to.

Compression -> (string)

Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"` ).

NumberTargetPartitions -> (string)

Specifies the number of target partitions for distributing Hudi dataset files across Amazon S3.

PartitionKeys -> (list)

Specifies native partitioning using a sequence of keys.

(list)

(string)

Format -> (string)

Specifies the data output format for the target.

AdditionalOptions -> (map)

Specifies additional connection options for the connector.

key -> (string)

value -> (string)

SchemaChangePolicy -> (structure)

A policy that specifies update behavior for the crawler.

EnableUpdateCatalog -> (boolean)

Whether to use the specified update behavior when the crawler finds a changed schema.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

Table -> (string)

Specifies the table in the database that the schema change policy applies to.

Database -> (string)

Specifies the database that the schema change policy applies to.

DirectJDBCSource -> (structure)

Specifies the direct JDBC source connection.

Name -> (string)

The name of the JDBC source connection.

Database -> (string)

The database of the JDBC source connection.

Table -> (string)

The table of the JDBC source connection.

ConnectionName -> (string)

The connection name of the JDBC source.

ConnectionType -> (string)

The connection type of the JDBC source.

RedshiftTmpDir -> (string)

The temp directory of the JDBC Redshift source.

S3CatalogDeltaSource -> (structure)

Specifies a Delta Lake data source that is registered in the Glue Data Catalog. The data source must be stored in Amazon S3.

Name -> (string)

The name of the Delta Lake data source.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

AdditionalDeltaOptions -> (map)

Specifies additional connection options.

key -> (string)

value -> (string)

OutputSchemas -> (list)

Specifies the data schema for the Delta Lake source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

CatalogDeltaSource -> (structure)

Specifies a Delta Lake data source that is registered in the Glue Data Catalog.

Name -> (string)

The name of the Delta Lake data source.

Database -> (string)

The name of the database to read from.

Table -> (string)

The name of the table in the database to read from.

AdditionalDeltaOptions -> (map)

Specifies additional connection options.

key -> (string)

value -> (string)

OutputSchemas -> (list)

Specifies the data schema for the Delta Lake source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

S3DeltaSource -> (structure)

Specifies a Delta Lake data source stored in Amazon S3.

Name -> (string)

The name of the Delta Lake source.

Paths -> (list)

A list of the Amazon S3 paths to read from.

(string)

AdditionalDeltaOptions -> (map)

Specifies additional connection options.

key -> (string)

value -> (string)

AdditionalOptions -> (structure)

Specifies additional options for the connector.

BoundedSize -> (long)

Sets the upper limit for the target size of the dataset in bytes that will be processed.

BoundedFiles -> (long)

Sets the upper limit for the target number of files that will be processed.

EnableSamplePath -> (boolean)

Sets option to enable a sample path.

SamplePath -> (string)

If enabled, specifies the sample path.

OutputSchemas -> (list)

Specifies the data schema for the Delta Lake source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

S3DeltaCatalogTarget -> (structure)

Specifies a target that writes to a Delta Lake data source in the Glue Data Catalog.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

PartitionKeys -> (list)

Specifies native partitioning using a sequence of keys.

(list)

(string)

Table -> (string)

The name of the table in the database to write to.

Database -> (string)

The name of the database to write to.

AdditionalOptions -> (map)

Specifies additional connection options for the connector.

key -> (string)

value -> (string)

SchemaChangePolicy -> (structure)

A policy that specifies update behavior for the crawler.

EnableUpdateCatalog -> (boolean)

Whether to use the specified update behavior when the crawler finds a changed schema.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

S3DeltaDirectTarget -> (structure)

Specifies a target that writes to a Delta Lake data source in Amazon S3.

Name -> (string)

The name of the data target.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

PartitionKeys -> (list)

Specifies native partitioning using a sequence of keys.

(list)

(string)

Path -> (string)

The Amazon S3 path of your Delta Lake data source to write to.

Compression -> (string)

Specifies how the data is compressed. This is generally not necessary if the data has a standard file extension. Possible values are `"gzip"` and `"bzip"` ).

NumberTargetPartitions -> (string)

Specifies the number of target partitions for distributing Delta Lake dataset files across Amazon S3.

Format -> (string)

Specifies the data output format for the target.

AdditionalOptions -> (map)

Specifies additional connection options for the connector.

key -> (string)

value -> (string)

SchemaChangePolicy -> (structure)

A policy that specifies update behavior for the crawler.

EnableUpdateCatalog -> (boolean)

Whether to use the specified update behavior when the crawler finds a changed schema.

UpdateBehavior -> (string)

The update behavior when the crawler finds a changed schema.

Table -> (string)

Specifies the table in the database that the schema change policy applies to.

Database -> (string)

Specifies the database that the schema change policy applies to.

AmazonRedshiftSource -> (structure)

Specifies a target that writes to a data source in Amazon Redshift.

Name -> (string)

The name of the Amazon Redshift source.

Data -> (structure)

Specifies the data of the Amazon Reshift source node.

AccessType -> (string)

The access type for the Redshift connection. Can be a direct connection or catalog connections.

SourceType -> (string)

The source type to specify whether a specific table is the source or a custom query.

Connection -> (structure)

The Glue connection to the Redshift cluster.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

Schema -> (structure)

The Redshift schema name when working with a direct connection.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

Table -> (structure)

The Redshift table name when working with a direct connection.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

CatalogDatabase -> (structure)

The name of the Glue Data Catalog database when working with a data catalog.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

CatalogTable -> (structure)

The Glue Data Catalog table name when working with a data catalog.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

CatalogRedshiftSchema -> (string)

The Redshift schema name when working with a data catalog.

CatalogRedshiftTable -> (string)

The database table to read from.

TempDir -> (string)

The Amazon S3 path where temporary data can be staged when copying out of the database.

IamRole -> (structure)

Optional. The role name use when connection to S3. The IAM role ill default to the role on the job when left blank.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

AdvancedOptions -> (list)

Optional values when connecting to the Redshift cluster.

(structure)

Specifies an optional value when connecting to the Redshift cluster.

Key -> (string)

The key for the additional connection option.

Value -> (string)

The value for the additional connection option.

SampleQuery -> (string)

The SQL used to fetch the data from a Redshift sources when the SourceType is âqueryâ.

PreAction -> (string)

The SQL used before a MERGE or APPEND with upsert is run.

PostAction -> (string)

The SQL used before a MERGE or APPEND with upsert is run.

Action -> (string)

Specifies how writing to a Redshift cluser will occur.

TablePrefix -> (string)

Specifies the prefix to a table.

Upsert -> (boolean)

The action used on Redshift sinks when doing an APPEND.

MergeAction -> (string)

The action used when to detemine how a MERGE in a Redshift sink will be handled.

MergeWhenMatched -> (string)

The action used when to detemine how a MERGE in a Redshift sink will be handled when an existing record matches a new record.

MergeWhenNotMatched -> (string)

The action used when to detemine how a MERGE in a Redshift sink will be handled when an existing record doesnât match a new record.

MergeClause -> (string)

The SQL used in a custom merge to deal with matching records.

CrawlerConnection -> (string)

Specifies the name of the connection that is associated with the catalog table used.

TableSchema -> (list)

The array of schema output for a given node.

(structure)

Specifies an option value.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

StagingTable -> (string)

The name of the temporary staging table that is used when doing a MERGE or APPEND with upsert.

SelectedColumns -> (list)

The list of column names used to determine a matching record when doing a MERGE or APPEND with upsert.

(structure)

Specifies an option value.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

AmazonRedshiftTarget -> (structure)

Specifies a target that writes to a data target in Amazon Redshift.

Name -> (string)

The name of the Amazon Redshift target.

Data -> (structure)

Specifies the data of the Amazon Redshift target node.

AccessType -> (string)

The access type for the Redshift connection. Can be a direct connection or catalog connections.

SourceType -> (string)

The source type to specify whether a specific table is the source or a custom query.

Connection -> (structure)

The Glue connection to the Redshift cluster.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

Schema -> (structure)

The Redshift schema name when working with a direct connection.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

Table -> (structure)

The Redshift table name when working with a direct connection.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

CatalogDatabase -> (structure)

The name of the Glue Data Catalog database when working with a data catalog.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

CatalogTable -> (structure)

The Glue Data Catalog table name when working with a data catalog.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

CatalogRedshiftSchema -> (string)

The Redshift schema name when working with a data catalog.

CatalogRedshiftTable -> (string)

The database table to read from.

TempDir -> (string)

The Amazon S3 path where temporary data can be staged when copying out of the database.

IamRole -> (structure)

Optional. The role name use when connection to S3. The IAM role ill default to the role on the job when left blank.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

AdvancedOptions -> (list)

Optional values when connecting to the Redshift cluster.

(structure)

Specifies an optional value when connecting to the Redshift cluster.

Key -> (string)

The key for the additional connection option.

Value -> (string)

The value for the additional connection option.

SampleQuery -> (string)

The SQL used to fetch the data from a Redshift sources when the SourceType is âqueryâ.

PreAction -> (string)

The SQL used before a MERGE or APPEND with upsert is run.

PostAction -> (string)

The SQL used before a MERGE or APPEND with upsert is run.

Action -> (string)

Specifies how writing to a Redshift cluser will occur.

TablePrefix -> (string)

Specifies the prefix to a table.

Upsert -> (boolean)

The action used on Redshift sinks when doing an APPEND.

MergeAction -> (string)

The action used when to detemine how a MERGE in a Redshift sink will be handled.

MergeWhenMatched -> (string)

The action used when to detemine how a MERGE in a Redshift sink will be handled when an existing record matches a new record.

MergeWhenNotMatched -> (string)

The action used when to detemine how a MERGE in a Redshift sink will be handled when an existing record doesnât match a new record.

MergeClause -> (string)

The SQL used in a custom merge to deal with matching records.

CrawlerConnection -> (string)

Specifies the name of the connection that is associated with the catalog table used.

TableSchema -> (list)

The array of schema output for a given node.

(structure)

Specifies an option value.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

StagingTable -> (string)

The name of the temporary staging table that is used when doing a MERGE or APPEND with upsert.

SelectedColumns -> (list)

The list of column names used to determine a matching record when doing a MERGE or APPEND with upsert.

(structure)

Specifies an option value.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

EvaluateDataQualityMultiFrame -> (structure)

Specifies your data quality evaluation criteria. Allows multiple input data and returns a collection of Dynamic Frames.

Name -> (string)

The name of the data quality evaluation.

Inputs -> (list)

The inputs of your data quality evaluation. The first input in this list is the primary data source.

(string)

AdditionalDataSources -> (map)

The aliases of all data sources except primary.

key -> (string)

value -> (string)

Ruleset -> (string)

The ruleset for your data quality evaluation.

PublishingOptions -> (structure)

Options to configure how your results are published.

EvaluationContext -> (string)

The context of the evaluation.

ResultsS3Prefix -> (string)

The Amazon S3 prefix prepended to the results.

CloudWatchMetricsEnabled -> (boolean)

Enable metrics for your data quality results.

ResultsPublishingEnabled -> (boolean)

Enable publishing for your data quality results.

AdditionalOptions -> (map)

Options to configure runtime behavior of the transform.

key -> (string)

value -> (string)

StopJobOnFailureOptions -> (structure)

Options to configure how your job will stop if your data quality evaluation fails.

StopJobOnFailureTiming -> (string)

When to stop job if your data quality evaluation fails. Options are Immediate or AfterDataLoad.

Recipe -> (structure)

Specifies a Glue DataBrew recipe node.

Name -> (string)

The name of the Glue Studio node.

Inputs -> (list)

The nodes that are inputs to the recipe node, identified by id.

(string)

RecipeReference -> (structure)

A reference to the DataBrew recipe used by the node.

RecipeArn -> (string)

The ARN of the DataBrew recipe.

RecipeVersion -> (string)

The RecipeVersion of the DataBrew recipe.

RecipeSteps -> (list)

Transform steps used in the recipe node.

(structure)

A recipe step used in a Glue Studio data preparation recipe node.

Action -> (structure)

The transformation action of the recipe step.

Operation -> (string)

The operation of the recipe action.

Parameters -> (map)

The parameters of the recipe action.

key -> (string)

value -> (string)

ConditionExpressions -> (list)

The condition expressions for the recipe step.

(structure)

Condition expression defined in the Glue Studio data preparation recipe node.

Condition -> (string)

The condition of the condition expression.

Value -> (string)

The value of the condition expression.

TargetColumn -> (string)

The target column of the condition expressions.

SnowflakeSource -> (structure)

Specifies a Snowflake data source.

Name -> (string)

The name of the Snowflake data source.

Data -> (structure)

Configuration for the Snowflake data source.

SourceType -> (string)

Specifies how retrieved data is specified. Valid values: `"table"` , `"query"` .

Connection -> (structure)

Specifies a Glue Data Catalog Connection to a Snowflake endpoint.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

Schema -> (string)

Specifies a Snowflake database schema for your node to use.

Table -> (string)

Specifies a Snowflake table for your node to use.

Database -> (string)

Specifies a Snowflake database for your node to use.

TempDir -> (string)

Not currently used.

IamRole -> (structure)

Not currently used.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

AdditionalOptions -> (map)

Specifies additional options passed to the Snowflake connector. If options are specified elsewhere in this node, this will take precedence.

key -> (string)

value -> (string)

SampleQuery -> (string)

A SQL string used to retrieve data with the `query` sourcetype.

PreAction -> (string)

A SQL string run before the Snowflake connector performs its standard actions.

PostAction -> (string)

A SQL string run after the Snowflake connector performs its standard actions.

Action -> (string)

Specifies what action to take when writing to a table with preexisting data. Valid values: `append` , `merge` , `truncate` , `drop` .

Upsert -> (boolean)

Used when Action is `append` . Specifies the resolution behavior when a row already exists. If true, preexisting rows will be updated. If false, those rows will be inserted.

MergeAction -> (string)

Specifies a merge action. Valid values: `simple` , `custom` . If simple, merge behavior is defined by `MergeWhenMatched` and `MergeWhenNotMatched` . If custom, defined by `MergeClause` .

MergeWhenMatched -> (string)

Specifies how to resolve records that match preexisting data when merging. Valid values: `update` , `delete` .

MergeWhenNotMatched -> (string)

Specifies how to process records that do not match preexisting data when merging. Valid values: `insert` , `none` .

MergeClause -> (string)

A SQL statement that specifies a custom merge behavior.

StagingTable -> (string)

The name of a staging table used when performing `merge` or upsert `append` actions. Data is written to this table, then moved to `table` by a generated postaction.

SelectedColumns -> (list)

Specifies the columns combined to identify a record when detecting matches for merges and upserts. A list of structures with `value` , `label` and `description` keys. Each structure describes a column.

(structure)

Specifies an option value.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

AutoPushdown -> (boolean)

Specifies whether automatic query pushdown is enabled. If pushdown is enabled, then when a query is run on Spark, if part of the query can be âpushed downâ to the Snowflake server, it is pushed down. This improves performance of some queries.

TableSchema -> (list)

Manually defines the target schema for the node. A list of structures with `value` , `label` and `description` keys. Each structure defines a column.

(structure)

Specifies an option value.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

OutputSchemas -> (list)

Specifies user-defined schemas for your output data.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

SnowflakeTarget -> (structure)

Specifies a target that writes to a Snowflake data source.

Name -> (string)

The name of the Snowflake target.

Data -> (structure)

Specifies the data of the Snowflake target node.

SourceType -> (string)

Specifies how retrieved data is specified. Valid values: `"table"` , `"query"` .

Connection -> (structure)

Specifies a Glue Data Catalog Connection to a Snowflake endpoint.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

Schema -> (string)

Specifies a Snowflake database schema for your node to use.

Table -> (string)

Specifies a Snowflake table for your node to use.

Database -> (string)

Specifies a Snowflake database for your node to use.

TempDir -> (string)

Not currently used.

IamRole -> (structure)

Not currently used.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

AdditionalOptions -> (map)

Specifies additional options passed to the Snowflake connector. If options are specified elsewhere in this node, this will take precedence.

key -> (string)

value -> (string)

SampleQuery -> (string)

A SQL string used to retrieve data with the `query` sourcetype.

PreAction -> (string)

A SQL string run before the Snowflake connector performs its standard actions.

PostAction -> (string)

A SQL string run after the Snowflake connector performs its standard actions.

Action -> (string)

Specifies what action to take when writing to a table with preexisting data. Valid values: `append` , `merge` , `truncate` , `drop` .

Upsert -> (boolean)

Used when Action is `append` . Specifies the resolution behavior when a row already exists. If true, preexisting rows will be updated. If false, those rows will be inserted.

MergeAction -> (string)

Specifies a merge action. Valid values: `simple` , `custom` . If simple, merge behavior is defined by `MergeWhenMatched` and `MergeWhenNotMatched` . If custom, defined by `MergeClause` .

MergeWhenMatched -> (string)

Specifies how to resolve records that match preexisting data when merging. Valid values: `update` , `delete` .

MergeWhenNotMatched -> (string)

Specifies how to process records that do not match preexisting data when merging. Valid values: `insert` , `none` .

MergeClause -> (string)

A SQL statement that specifies a custom merge behavior.

StagingTable -> (string)

The name of a staging table used when performing `merge` or upsert `append` actions. Data is written to this table, then moved to `table` by a generated postaction.

SelectedColumns -> (list)

Specifies the columns combined to identify a record when detecting matches for merges and upserts. A list of structures with `value` , `label` and `description` keys. Each structure describes a column.

(structure)

Specifies an option value.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

AutoPushdown -> (boolean)

Specifies whether automatic query pushdown is enabled. If pushdown is enabled, then when a query is run on Spark, if part of the query can be âpushed downâ to the Snowflake server, it is pushed down. This improves performance of some queries.

TableSchema -> (list)

Manually defines the target schema for the node. A list of structures with `value` , `label` and `description` keys. Each structure defines a column.

(structure)

Specifies an option value.

Value -> (string)

Specifies the value of the option.

Label -> (string)

Specifies the label of the option.

Description -> (string)

Specifies the description of the option.

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

ConnectorDataSource -> (structure)

Specifies a source generated with standard connection options.

Name -> (string)

The name of this source node.

ConnectionType -> (string)

The `connectionType` , as provided to the underlying Glue library. This node type supports the following connection types:

- `opensearch`
- `azuresql`
- `azurecosmos`
- `bigquery`
- `saphana`
- `teradata`
- `vertica`

Data -> (map)

A map specifying connection options for the node. You can find standard connection options for the corresponding connection type in the [Connection parameters](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html) section of the Glue documentation.

key -> (string)

value -> (string)

OutputSchemas -> (list)

Specifies the data schema for this source.

(structure)

Specifies a user-defined schema when a schema cannot be determined by Glue.

Columns -> (list)

Specifies the column definitions that make up a Glue schema.

(structure)

Specifies a single column in a Glue schema definition.

Name -> (string)

The name of the column in the Glue Studio schema.

Type -> (string)

The hive type for this column in the Glue Studio schema.

ConnectorDataTarget -> (structure)

Specifies a target generated with standard connection options.

Name -> (string)

The name of this target node.

ConnectionType -> (string)

The `connectionType` , as provided to the underlying Glue library. This node type supports the following connection types:

- `opensearch`
- `azuresql`
- `azurecosmos`
- `bigquery`
- `saphana`
- `teradata`
- `vertica`

Data -> (map)

A map specifying connection options for the node. You can find standard connection options for the corresponding connection type in the [Connection parameters](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-programming-etl-connect.html) section of the Glue documentation.

key -> (string)

value -> (string)

Inputs -> (list)

The nodes that are inputs to the data target.

(string)

ExecutionClass -> (string)

Indicates whether the job is run with a standard or flexible execution class. The standard execution-class is ideal for time-sensitive workloads that require fast job startup and dedicated resources.

The flexible execution class is appropriate for time-insensitive jobs whose start and completion times may vary.

Only jobs with Glue version 3.0 and above and command type `glueetl` will be allowed to set `ExecutionClass` to `FLEX` . The flexible execution class is available for Spark jobs.

SourceControlDetails -> (structure)

The details for a source control configuration for a job, allowing synchronization of job artifacts to or from a remote repository.

Provider -> (string)

The provider for the remote repository.

Repository -> (string)

The name of the remote repository that contains the job artifacts.

Owner -> (string)

The owner of the remote repository that contains the job artifacts.

Branch -> (string)

An optional branch in the remote repository.

Folder -> (string)

An optional folder in the remote repository.

LastCommitId -> (string)

The last commit ID for a commit in the remote repository.

AuthStrategy -> (string)

The type of authentication, which can be an authentication token stored in Amazon Web Services Secrets Manager, or a personal access token.

AuthToken -> (string)

The value of an authorization token.

MaintenanceWindow -> (string)

This field specifies a day of the week and hour for a maintenance window for streaming jobs. Glue periodically performs maintenance activities. During these maintenance windows, Glue will need to restart your streaming jobs.

Glue will restart the job within 3 hours of the specified maintenance window. For instance, if you set up the maintenance window for Monday at 10:00AM GMT, your jobs will be restarted between 10:00AM GMT to 1:00PM GMT.

JSON Syntax:

```
{
  "JobMode": "SCRIPT"|"VISUAL"|"NOTEBOOK",
  "JobRunQueuingEnabled": true|false,
  "Description": "string",
  "LogUri": "string",
  "Role": "string",
  "ExecutionProperty": {
    "MaxConcurrentRuns": integer
  },
  "Command": {
    "Name": "string",
    "ScriptLocation": "string",
    "PythonVersion": "string",
    "Runtime": "string"
  },
  "DefaultArguments": {"string": "string"
    ...},
  "NonOverridableArguments": {"string": "string"
    ...},
  "Connections": {
    "Connections": ["string", ...]
  },
  "MaxRetries": integer,
  "AllocatedCapacity": integer,
  "Timeout": integer,
  "MaxCapacity": double,
  "WorkerType": "Standard"|"G.1X"|"G.2X"|"G.025X"|"G.4X"|"G.8X"|"Z.2X",
  "NumberOfWorkers": integer,
  "SecurityConfiguration": "string",
  "NotificationProperty": {
    "NotifyDelayAfter": integer
  },
  "GlueVersion": "string",
  "CodeGenConfigurationNodes": {"string": {
        "AthenaConnectorSource": {
          "Name": "string",
          "ConnectionName": "string",
          "ConnectorName": "string",
          "ConnectionType": "string",
          "ConnectionTable": "string",
          "SchemaName": "string",
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "JDBCConnectorSource": {
          "Name": "string",
          "ConnectionName": "string",
          "ConnectorName": "string",
          "ConnectionType": "string",
          "AdditionalOptions": {
            "FilterPredicate": "string",
            "PartitionColumn": "string",
            "LowerBound": long,
            "UpperBound": long,
            "NumPartitions": long,
            "JobBookmarkKeys": ["string", ...],
            "JobBookmarkKeysSortOrder": "string",
            "DataTypeMapping": {"ARRAY"|"BIGINT"|"BINARY"|"BIT"|"BLOB"|"BOOLEAN"|"CHAR"|"CLOB"|"DATALINK"|"DATE"|"DECIMAL"|"DISTINCT"|"DOUBLE"|"FLOAT"|"INTEGER"|"JAVA_OBJECT"|"LONGNVARCHAR"|"LONGVARBINARY"|"LONGVARCHAR"|"NCHAR"|"NCLOB"|"NULL"|"NUMERIC"|"NVARCHAR"|"OTHER"|"REAL"|"REF"|"REF_CURSOR"|"ROWID"|"SMALLINT"|"SQLXML"|"STRUCT"|"TIME"|"TIME_WITH_TIMEZONE"|"TIMESTAMP"|"TIMESTAMP_WITH_TIMEZONE"|"TINYINT"|"VARBINARY"|"VARCHAR": "DATE"|"STRING"|"TIMESTAMP"|"INT"|"FLOAT"|"LONG"|"BIGDECIMAL"|"BYTE"|"SHORT"|"DOUBLE"
              ...}
          },
          "ConnectionTable": "string",
          "Query": "string",
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "SparkConnectorSource": {
          "Name": "string",
          "ConnectionName": "string",
          "ConnectorName": "string",
          "ConnectionType": "string",
          "AdditionalOptions": {"string": "string"
            ...},
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "CatalogSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string"
        },
        "RedshiftSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string",
          "RedshiftTmpDir": "string",
          "TmpDirIAMRole": "string"
        },
        "S3CatalogSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string",
          "PartitionPredicate": "string",
          "AdditionalOptions": {
            "BoundedSize": long,
            "BoundedFiles": long
          }
        },
        "S3CsvSource": {
          "Name": "string",
          "Paths": ["string", ...],
          "CompressionType": "gzip"|"bzip2",
          "Exclusions": ["string", ...],
          "GroupSize": "string",
          "GroupFiles": "string",
          "Recurse": true|false,
          "MaxBand": integer,
          "MaxFilesInBand": integer,
          "AdditionalOptions": {
            "BoundedSize": long,
            "BoundedFiles": long,
            "EnableSamplePath": true|false,
            "SamplePath": "string"
          },
          "Separator": "comma"|"ctrla"|"pipe"|"semicolon"|"tab",
          "Escaper": "string",
          "QuoteChar": "quote"|"quillemet"|"single_quote"|"disabled",
          "Multiline": true|false,
          "WithHeader": true|false,
          "WriteHeader": true|false,
          "SkipFirst": true|false,
          "OptimizePerformance": true|false,
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "S3ExcelSource": {
          "Name": "string",
          "Paths": ["string", ...],
          "CompressionType": "snappy"|"lzo"|"gzip"|"brotli"|"lz4"|"uncompressed"|"none",
          "Exclusions": ["string", ...],
          "GroupSize": "string",
          "GroupFiles": "string",
          "Recurse": true|false,
          "MaxBand": integer,
          "MaxFilesInBand": integer,
          "AdditionalOptions": {
            "BoundedSize": long,
            "BoundedFiles": long,
            "EnableSamplePath": true|false,
            "SamplePath": "string"
          },
          "NumberRows": long,
          "SkipFooter": integer,
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "S3JsonSource": {
          "Name": "string",
          "Paths": ["string", ...],
          "CompressionType": "gzip"|"bzip2",
          "Exclusions": ["string", ...],
          "GroupSize": "string",
          "GroupFiles": "string",
          "Recurse": true|false,
          "MaxBand": integer,
          "MaxFilesInBand": integer,
          "AdditionalOptions": {
            "BoundedSize": long,
            "BoundedFiles": long,
            "EnableSamplePath": true|false,
            "SamplePath": "string"
          },
          "JsonPath": "string",
          "Multiline": true|false,
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "S3ParquetSource": {
          "Name": "string",
          "Paths": ["string", ...],
          "CompressionType": "snappy"|"lzo"|"gzip"|"brotli"|"lz4"|"uncompressed"|"none",
          "Exclusions": ["string", ...],
          "GroupSize": "string",
          "GroupFiles": "string",
          "Recurse": true|false,
          "MaxBand": integer,
          "MaxFilesInBand": integer,
          "AdditionalOptions": {
            "BoundedSize": long,
            "BoundedFiles": long,
            "EnableSamplePath": true|false,
            "SamplePath": "string"
          },
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "RelationalCatalogSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string"
        },
        "DynamoDBCatalogSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string"
        },
        "JDBCConnectorTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "ConnectionName": "string",
          "ConnectionTable": "string",
          "ConnectorName": "string",
          "ConnectionType": "string",
          "AdditionalOptions": {"string": "string"
            ...},
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "SparkConnectorTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "ConnectionName": "string",
          "ConnectorName": "string",
          "ConnectionType": "string",
          "AdditionalOptions": {"string": "string"
            ...},
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "CatalogTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Database": "string",
          "Table": "string"
        },
        "RedshiftTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Database": "string",
          "Table": "string",
          "RedshiftTmpDir": "string",
          "TmpDirIAMRole": "string",
          "UpsertRedshiftOptions": {
            "TableLocation": "string",
            "ConnectionName": "string",
            "UpsertKeys": ["string", ...]
          }
        },
        "S3CatalogTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Table": "string",
          "Database": "string",
          "SchemaChangePolicy": {
            "EnableUpdateCatalog": true|false,
            "UpdateBehavior": "UPDATE_IN_DATABASE"|"LOG"
          }
        },
        "S3GlueParquetTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Path": "string",
          "Compression": "snappy"|"lzo"|"gzip"|"brotli"|"lz4"|"uncompressed"|"none",
          "NumberTargetPartitions": "string",
          "SchemaChangePolicy": {
            "EnableUpdateCatalog": true|false,
            "UpdateBehavior": "UPDATE_IN_DATABASE"|"LOG",
            "Table": "string",
            "Database": "string"
          }
        },
        "S3HyperDirectTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Path": "string",
          "Compression": "uncompressed",
          "SchemaChangePolicy": {
            "EnableUpdateCatalog": true|false,
            "UpdateBehavior": "UPDATE_IN_DATABASE"|"LOG",
            "Table": "string",
            "Database": "string"
          }
        },
        "S3DirectTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Path": "string",
          "Compression": "string",
          "NumberTargetPartitions": "string",
          "Format": "json"|"csv"|"avro"|"orc"|"parquet"|"hudi"|"delta"|"iceberg"|"hyper"|"xml",
          "SchemaChangePolicy": {
            "EnableUpdateCatalog": true|false,
            "UpdateBehavior": "UPDATE_IN_DATABASE"|"LOG",
            "Table": "string",
            "Database": "string"
          }
        },
        "S3IcebergDirectTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Path": "string",
          "Format": "json"|"csv"|"avro"|"orc"|"parquet"|"hudi"|"delta"|"iceberg"|"hyper"|"xml",
          "AdditionalOptions": {"string": "string"
            ...},
          "SchemaChangePolicy": {
            "EnableUpdateCatalog": true|false,
            "UpdateBehavior": "UPDATE_IN_DATABASE"|"LOG",
            "Table": "string",
            "Database": "string"
          },
          "Compression": "gzip"|"lzo"|"uncompressed"|"snappy",
          "NumberTargetPartitions": "string"
        },
        "ApplyMapping": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Mapping": [
            {
              "ToKey": "string",
              "FromPath": ["string", ...],
              "FromType": "string",
              "ToType": "string",
              "Dropped": true|false,
              "Children": [
                {
                  "ToKey": "string",
                  "FromPath": ["string", ...],
                  "FromType": "string",
                  "ToType": "string",
                  "Dropped": true|false,
                  "Children":
                }
                ...
              ]
            }
            ...
          ]
        },
        "SelectFields": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Paths": [
            ["string", ...]
            ...
          ]
        },
        "DropFields": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Paths": [
            ["string", ...]
            ...
          ]
        },
        "RenameField": {
          "Name": "string",
          "Inputs": ["string", ...],
          "SourcePath": ["string", ...],
          "TargetPath": ["string", ...]
        },
        "Spigot": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Path": "string",
          "Topk": integer,
          "Prob": double
        },
        "Join": {
          "Name": "string",
          "Inputs": ["string", ...],
          "JoinType": "equijoin"|"left"|"right"|"outer"|"leftsemi"|"leftanti",
          "Columns": [
            {
              "From": "string",
              "Keys": [
                ["string", ...]
                ...
              ]
            }
            ...
          ]
        },
        "SplitFields": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Paths": [
            ["string", ...]
            ...
          ]
        },
        "SelectFromCollection": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Index": integer
        },
        "FillMissingValues": {
          "Name": "string",
          "Inputs": ["string", ...],
          "ImputedPath": "string",
          "FilledPath": "string"
        },
        "Filter": {
          "Name": "string",
          "Inputs": ["string", ...],
          "LogicalOperator": "AND"|"OR",
          "Filters": [
            {
              "Operation": "EQ"|"LT"|"GT"|"LTE"|"GTE"|"REGEX"|"ISNULL",
              "Negated": true|false,
              "Values": [
                {
                  "Type": "COLUMNEXTRACTED"|"CONSTANT",
                  "Value": ["string", ...]
                }
                ...
              ]
            }
            ...
          ]
        },
        "CustomCode": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Code": "string",
          "ClassName": "string",
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "SparkSQL": {
          "Name": "string",
          "Inputs": ["string", ...],
          "SqlQuery": "string",
          "SqlAliases": [
            {
              "From": "string",
              "Alias": "string"
            }
            ...
          ],
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "DirectKinesisSource": {
          "Name": "string",
          "WindowSize": integer,
          "DetectSchema": true|false,
          "StreamingOptions": {
            "EndpointUrl": "string",
            "StreamName": "string",
            "Classification": "string",
            "Delimiter": "string",
            "StartingPosition": "latest"|"trim_horizon"|"earliest"|"timestamp",
            "MaxFetchTimeInMs": long,
            "MaxFetchRecordsPerShard": long,
            "MaxRecordPerRead": long,
            "AddIdleTimeBetweenReads": true|false,
            "IdleTimeBetweenReadsInMs": long,
            "DescribeShardInterval": long,
            "NumRetries": integer,
            "RetryIntervalMs": long,
            "MaxRetryIntervalMs": long,
            "AvoidEmptyBatches": true|false,
            "StreamArn": "string",
            "RoleArn": "string",
            "RoleSessionName": "string",
            "AddRecordTimestamp": "string",
            "EmitConsumerLagMetrics": "string",
            "StartingTimestamp": timestamp
          },
          "DataPreviewOptions": {
            "PollingTime": long,
            "RecordPollingLimit": long
          }
        },
        "DirectKafkaSource": {
          "Name": "string",
          "StreamingOptions": {
            "BootstrapServers": "string",
            "SecurityProtocol": "string",
            "ConnectionName": "string",
            "TopicName": "string",
            "Assign": "string",
            "SubscribePattern": "string",
            "Classification": "string",
            "Delimiter": "string",
            "StartingOffsets": "string",
            "EndingOffsets": "string",
            "PollTimeoutMs": long,
            "NumRetries": integer,
            "RetryIntervalMs": long,
            "MaxOffsetsPerTrigger": long,
            "MinPartitions": integer,
            "IncludeHeaders": true|false,
            "AddRecordTimestamp": "string",
            "EmitConsumerLagMetrics": "string",
            "StartingTimestamp": timestamp
          },
          "WindowSize": integer,
          "DetectSchema": true|false,
          "DataPreviewOptions": {
            "PollingTime": long,
            "RecordPollingLimit": long
          }
        },
        "CatalogKinesisSource": {
          "Name": "string",
          "WindowSize": integer,
          "DetectSchema": true|false,
          "Table": "string",
          "Database": "string",
          "StreamingOptions": {
            "EndpointUrl": "string",
            "StreamName": "string",
            "Classification": "string",
            "Delimiter": "string",
            "StartingPosition": "latest"|"trim_horizon"|"earliest"|"timestamp",
            "MaxFetchTimeInMs": long,
            "MaxFetchRecordsPerShard": long,
            "MaxRecordPerRead": long,
            "AddIdleTimeBetweenReads": true|false,
            "IdleTimeBetweenReadsInMs": long,
            "DescribeShardInterval": long,
            "NumRetries": integer,
            "RetryIntervalMs": long,
            "MaxRetryIntervalMs": long,
            "AvoidEmptyBatches": true|false,
            "StreamArn": "string",
            "RoleArn": "string",
            "RoleSessionName": "string",
            "AddRecordTimestamp": "string",
            "EmitConsumerLagMetrics": "string",
            "StartingTimestamp": timestamp
          },
          "DataPreviewOptions": {
            "PollingTime": long,
            "RecordPollingLimit": long
          }
        },
        "CatalogKafkaSource": {
          "Name": "string",
          "WindowSize": integer,
          "DetectSchema": true|false,
          "Table": "string",
          "Database": "string",
          "StreamingOptions": {
            "BootstrapServers": "string",
            "SecurityProtocol": "string",
            "ConnectionName": "string",
            "TopicName": "string",
            "Assign": "string",
            "SubscribePattern": "string",
            "Classification": "string",
            "Delimiter": "string",
            "StartingOffsets": "string",
            "EndingOffsets": "string",
            "PollTimeoutMs": long,
            "NumRetries": integer,
            "RetryIntervalMs": long,
            "MaxOffsetsPerTrigger": long,
            "MinPartitions": integer,
            "IncludeHeaders": true|false,
            "AddRecordTimestamp": "string",
            "EmitConsumerLagMetrics": "string",
            "StartingTimestamp": timestamp
          },
          "DataPreviewOptions": {
            "PollingTime": long,
            "RecordPollingLimit": long
          }
        },
        "DropNullFields": {
          "Name": "string",
          "Inputs": ["string", ...],
          "NullCheckBoxList": {
            "IsEmpty": true|false,
            "IsNullString": true|false,
            "IsNegOne": true|false
          },
          "NullTextList": [
            {
              "Value": "string",
              "Datatype": {
                "Id": "string",
                "Label": "string"
              }
            }
            ...
          ]
        },
        "Merge": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Source": "string",
          "PrimaryKeys": [
            ["string", ...]
            ...
          ]
        },
        "Union": {
          "Name": "string",
          "Inputs": ["string", ...],
          "UnionType": "ALL"|"DISTINCT"
        },
        "PIIDetection": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PiiType": "RowAudit"|"RowMasking"|"ColumnAudit"|"ColumnMasking",
          "EntityTypesToDetect": ["string", ...],
          "OutputColumnName": "string",
          "SampleFraction": double,
          "ThresholdFraction": double,
          "MaskValue": "string"
        },
        "Aggregate": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Groups": [
            ["string", ...]
            ...
          ],
          "Aggs": [
            {
              "Column": ["string", ...],
              "AggFunc": "avg"|"countDistinct"|"count"|"first"|"last"|"kurtosis"|"max"|"min"|"skewness"|"stddev_samp"|"stddev_pop"|"sum"|"sumDistinct"|"var_samp"|"var_pop"
            }
            ...
          ]
        },
        "DropDuplicates": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Columns": [
            ["string", ...]
            ...
          ]
        },
        "GovernedCatalogTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Table": "string",
          "Database": "string",
          "SchemaChangePolicy": {
            "EnableUpdateCatalog": true|false,
            "UpdateBehavior": "UPDATE_IN_DATABASE"|"LOG"
          }
        },
        "GovernedCatalogSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string",
          "PartitionPredicate": "string",
          "AdditionalOptions": {
            "BoundedSize": long,
            "BoundedFiles": long
          }
        },
        "MicrosoftSQLServerCatalogSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string"
        },
        "MySQLCatalogSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string"
        },
        "OracleSQLCatalogSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string"
        },
        "PostgreSQLCatalogSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string"
        },
        "MicrosoftSQLServerCatalogTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Database": "string",
          "Table": "string"
        },
        "MySQLCatalogTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Database": "string",
          "Table": "string"
        },
        "OracleSQLCatalogTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Database": "string",
          "Table": "string"
        },
        "PostgreSQLCatalogTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Database": "string",
          "Table": "string"
        },
        "DynamicTransform": {
          "Name": "string",
          "TransformName": "string",
          "Inputs": ["string", ...],
          "Parameters": [
            {
              "Name": "string",
              "Type": "str"|"int"|"float"|"complex"|"bool"|"list"|"null",
              "ValidationRule": "string",
              "ValidationMessage": "string",
              "Value": ["string", ...],
              "ListType": "str"|"int"|"float"|"complex"|"bool"|"list"|"null",
              "IsOptional": true|false
            }
            ...
          ],
          "FunctionName": "string",
          "Path": "string",
          "Version": "string",
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "EvaluateDataQuality": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Ruleset": "string",
          "Output": "PrimaryInput"|"EvaluationResults",
          "PublishingOptions": {
            "EvaluationContext": "string",
            "ResultsS3Prefix": "string",
            "CloudWatchMetricsEnabled": true|false,
            "ResultsPublishingEnabled": true|false
          },
          "StopJobOnFailureOptions": {
            "StopJobOnFailureTiming": "Immediate"|"AfterDataLoad"
          }
        },
        "S3CatalogHudiSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string",
          "AdditionalHudiOptions": {"string": "string"
            ...},
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "CatalogHudiSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string",
          "AdditionalHudiOptions": {"string": "string"
            ...},
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "S3HudiSource": {
          "Name": "string",
          "Paths": ["string", ...],
          "AdditionalHudiOptions": {"string": "string"
            ...},
          "AdditionalOptions": {
            "BoundedSize": long,
            "BoundedFiles": long,
            "EnableSamplePath": true|false,
            "SamplePath": "string"
          },
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "S3HudiCatalogTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Table": "string",
          "Database": "string",
          "AdditionalOptions": {"string": "string"
            ...},
          "SchemaChangePolicy": {
            "EnableUpdateCatalog": true|false,
            "UpdateBehavior": "UPDATE_IN_DATABASE"|"LOG"
          }
        },
        "S3HudiDirectTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "Path": "string",
          "Compression": "gzip"|"lzo"|"uncompressed"|"snappy",
          "NumberTargetPartitions": "string",
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Format": "json"|"csv"|"avro"|"orc"|"parquet"|"hudi"|"delta"|"iceberg"|"hyper"|"xml",
          "AdditionalOptions": {"string": "string"
            ...},
          "SchemaChangePolicy": {
            "EnableUpdateCatalog": true|false,
            "UpdateBehavior": "UPDATE_IN_DATABASE"|"LOG",
            "Table": "string",
            "Database": "string"
          }
        },
        "DirectJDBCSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string",
          "ConnectionName": "string",
          "ConnectionType": "sqlserver"|"mysql"|"oracle"|"postgresql"|"redshift",
          "RedshiftTmpDir": "string"
        },
        "S3CatalogDeltaSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string",
          "AdditionalDeltaOptions": {"string": "string"
            ...},
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "CatalogDeltaSource": {
          "Name": "string",
          "Database": "string",
          "Table": "string",
          "AdditionalDeltaOptions": {"string": "string"
            ...},
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "S3DeltaSource": {
          "Name": "string",
          "Paths": ["string", ...],
          "AdditionalDeltaOptions": {"string": "string"
            ...},
          "AdditionalOptions": {
            "BoundedSize": long,
            "BoundedFiles": long,
            "EnableSamplePath": true|false,
            "SamplePath": "string"
          },
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "S3DeltaCatalogTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Table": "string",
          "Database": "string",
          "AdditionalOptions": {"string": "string"
            ...},
          "SchemaChangePolicy": {
            "EnableUpdateCatalog": true|false,
            "UpdateBehavior": "UPDATE_IN_DATABASE"|"LOG"
          }
        },
        "S3DeltaDirectTarget": {
          "Name": "string",
          "Inputs": ["string", ...],
          "PartitionKeys": [
            ["string", ...]
            ...
          ],
          "Path": "string",
          "Compression": "uncompressed"|"snappy",
          "NumberTargetPartitions": "string",
          "Format": "json"|"csv"|"avro"|"orc"|"parquet"|"hudi"|"delta"|"iceberg"|"hyper"|"xml",
          "AdditionalOptions": {"string": "string"
            ...},
          "SchemaChangePolicy": {
            "EnableUpdateCatalog": true|false,
            "UpdateBehavior": "UPDATE_IN_DATABASE"|"LOG",
            "Table": "string",
            "Database": "string"
          }
        },
        "AmazonRedshiftSource": {
          "Name": "string",
          "Data": {
            "AccessType": "string",
            "SourceType": "string",
            "Connection": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "Schema": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "Table": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "CatalogDatabase": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "CatalogTable": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "CatalogRedshiftSchema": "string",
            "CatalogRedshiftTable": "string",
            "TempDir": "string",
            "IamRole": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "AdvancedOptions": [
              {
                "Key": "string",
                "Value": "string"
              }
              ...
            ],
            "SampleQuery": "string",
            "PreAction": "string",
            "PostAction": "string",
            "Action": "string",
            "TablePrefix": "string",
            "Upsert": true|false,
            "MergeAction": "string",
            "MergeWhenMatched": "string",
            "MergeWhenNotMatched": "string",
            "MergeClause": "string",
            "CrawlerConnection": "string",
            "TableSchema": [
              {
                "Value": "string",
                "Label": "string",
                "Description": "string"
              }
              ...
            ],
            "StagingTable": "string",
            "SelectedColumns": [
              {
                "Value": "string",
                "Label": "string",
                "Description": "string"
              }
              ...
            ]
          }
        },
        "AmazonRedshiftTarget": {
          "Name": "string",
          "Data": {
            "AccessType": "string",
            "SourceType": "string",
            "Connection": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "Schema": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "Table": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "CatalogDatabase": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "CatalogTable": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "CatalogRedshiftSchema": "string",
            "CatalogRedshiftTable": "string",
            "TempDir": "string",
            "IamRole": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "AdvancedOptions": [
              {
                "Key": "string",
                "Value": "string"
              }
              ...
            ],
            "SampleQuery": "string",
            "PreAction": "string",
            "PostAction": "string",
            "Action": "string",
            "TablePrefix": "string",
            "Upsert": true|false,
            "MergeAction": "string",
            "MergeWhenMatched": "string",
            "MergeWhenNotMatched": "string",
            "MergeClause": "string",
            "CrawlerConnection": "string",
            "TableSchema": [
              {
                "Value": "string",
                "Label": "string",
                "Description": "string"
              }
              ...
            ],
            "StagingTable": "string",
            "SelectedColumns": [
              {
                "Value": "string",
                "Label": "string",
                "Description": "string"
              }
              ...
            ]
          },
          "Inputs": ["string", ...]
        },
        "EvaluateDataQualityMultiFrame": {
          "Name": "string",
          "Inputs": ["string", ...],
          "AdditionalDataSources": {"string": "string"
            ...},
          "Ruleset": "string",
          "PublishingOptions": {
            "EvaluationContext": "string",
            "ResultsS3Prefix": "string",
            "CloudWatchMetricsEnabled": true|false,
            "ResultsPublishingEnabled": true|false
          },
          "AdditionalOptions": {"performanceTuning.caching"|"observations.scope": "string"
            ...},
          "StopJobOnFailureOptions": {
            "StopJobOnFailureTiming": "Immediate"|"AfterDataLoad"
          }
        },
        "Recipe": {
          "Name": "string",
          "Inputs": ["string", ...],
          "RecipeReference": {
            "RecipeArn": "string",
            "RecipeVersion": "string"
          },
          "RecipeSteps": [
            {
              "Action": {
                "Operation": "string",
                "Parameters": {"string": "string"
                  ...}
              },
              "ConditionExpressions": [
                {
                  "Condition": "string",
                  "Value": "string",
                  "TargetColumn": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "SnowflakeSource": {
          "Name": "string",
          "Data": {
            "SourceType": "string",
            "Connection": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "Schema": "string",
            "Table": "string",
            "Database": "string",
            "TempDir": "string",
            "IamRole": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "AdditionalOptions": {"string": "string"
              ...},
            "SampleQuery": "string",
            "PreAction": "string",
            "PostAction": "string",
            "Action": "string",
            "Upsert": true|false,
            "MergeAction": "string",
            "MergeWhenMatched": "string",
            "MergeWhenNotMatched": "string",
            "MergeClause": "string",
            "StagingTable": "string",
            "SelectedColumns": [
              {
                "Value": "string",
                "Label": "string",
                "Description": "string"
              }
              ...
            ],
            "AutoPushdown": true|false,
            "TableSchema": [
              {
                "Value": "string",
                "Label": "string",
                "Description": "string"
              }
              ...
            ]
          },
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "SnowflakeTarget": {
          "Name": "string",
          "Data": {
            "SourceType": "string",
            "Connection": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "Schema": "string",
            "Table": "string",
            "Database": "string",
            "TempDir": "string",
            "IamRole": {
              "Value": "string",
              "Label": "string",
              "Description": "string"
            },
            "AdditionalOptions": {"string": "string"
              ...},
            "SampleQuery": "string",
            "PreAction": "string",
            "PostAction": "string",
            "Action": "string",
            "Upsert": true|false,
            "MergeAction": "string",
            "MergeWhenMatched": "string",
            "MergeWhenNotMatched": "string",
            "MergeClause": "string",
            "StagingTable": "string",
            "SelectedColumns": [
              {
                "Value": "string",
                "Label": "string",
                "Description": "string"
              }
              ...
            ],
            "AutoPushdown": true|false,
            "TableSchema": [
              {
                "Value": "string",
                "Label": "string",
                "Description": "string"
              }
              ...
            ]
          },
          "Inputs": ["string", ...]
        },
        "ConnectorDataSource": {
          "Name": "string",
          "ConnectionType": "string",
          "Data": {"string": "string"
            ...},
          "OutputSchemas": [
            {
              "Columns": [
                {
                  "Name": "string",
                  "Type": "string"
                }
                ...
              ]
            }
            ...
          ]
        },
        "ConnectorDataTarget": {
          "Name": "string",
          "ConnectionType": "string",
          "Data": {"string": "string"
            ...},
          "Inputs": ["string", ...]
        }
      }
    ...},
  "ExecutionClass": "FLEX"|"STANDARD",
  "SourceControlDetails": {
    "Provider": "GITHUB"|"GITLAB"|"BITBUCKET"|"AWS_CODE_COMMIT",
    "Repository": "string",
    "Owner": "string",
    "Branch": "string",
    "Folder": "string",
    "LastCommitId": "string",
    "AuthStrategy": "PERSONAL_ACCESS_TOKEN"|"AWS_SECRETS_MANAGER",
    "AuthToken": "string"
  },
  "MaintenanceWindow": "string"
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

JobName -> (string)

Returns the name of the updated job definition.