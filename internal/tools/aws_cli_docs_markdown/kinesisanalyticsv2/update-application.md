# update-applicationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/update-application.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/update-application.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kinesisanalyticsv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesisanalyticsv2/index.html#cli-aws-kinesisanalyticsv2) ]

# update-application

## Description

Updates an existing Managed Service for Apache Flink application. Using this operation, you can update application code, input configuration, and output configuration.

Managed Service for Apache Flink updates the `ApplicationVersionId` each time you update your application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kinesisanalyticsv2-2018-05-23/UpdateApplication)

## Synopsis

```
update-application
--application-name <value>
[--current-application-version-id <value>]
[--application-configuration-update <value>]
[--service-execution-role-update <value>]
[--run-configuration-update <value>]
[--cloud-watch-logging-option-updates <value>]
[--conditional-token <value>]
[--runtime-environment-update <value>]
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

`--application-name` (string)

The name of the application to update.

`--current-application-version-id` (long)

The current application version ID. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken` .You can retrieve the application version ID using  DescribeApplication . For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId` .

`--application-configuration-update` (structure)

Describes application configuration updates.

SqlApplicationConfigurationUpdate -> (structure)

Describes updates to a SQL-based Kinesis Data Analytics applicationâs configuration.

InputUpdates -> (list)

The array of  InputUpdate objects describing the new input streams used by the application.

(structure)

For a SQL-based Kinesis Data Analytics application, describes updates to a specific input configuration (identified by the `InputId` of an application).

InputId -> (string)

The input ID of the application input to be updated.

NamePrefixUpdate -> (string)

The name prefix for in-application streams that Kinesis Data Analytics creates for the specific streaming source.

InputProcessingConfigurationUpdate -> (structure)

Describes updates to an  InputProcessingConfiguration .

InputLambdaProcessorUpdate -> (structure)

Provides update information for an  InputLambdaProcessor .

ResourceARNUpdate -> (string)

The Amazon Resource Name (ARN) of the new Amazon Lambda function that is used to preprocess the records in the stream.

### Note

To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: Amazon Lambda](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)

KinesisStreamsInputUpdate -> (structure)

If a Kinesis data stream is the streaming source to be updated, provides an updated stream Amazon Resource Name (ARN).

ResourceARNUpdate -> (string)

The Amazon Resource Name (ARN) of the input Kinesis data stream to read.

KinesisFirehoseInputUpdate -> (structure)

If a Kinesis Data Firehose delivery stream is the streaming source to be updated, provides an updated stream ARN.

ResourceARNUpdate -> (string)

The Amazon Resource Name (ARN) of the input delivery stream to read.

InputSchemaUpdate -> (structure)

Describes the data format on the streaming source, and how record elements on the streaming source map to columns of the in-application stream that is created.

RecordFormatUpdate -> (structure)

Specifies the format of the records on the streaming source.

RecordFormatType -> (string)

The type of record format.

MappingParameters -> (structure)

When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters -> (structure)

Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath -> (string)

The path to the top-level parent that contains the records.

CSVMappingParameters -> (structure)

Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter -> (string)

The row delimiter. For example, in a CSV format, *ânâ* is the typical row delimiter.

RecordColumnDelimiter -> (string)

The column delimiter. For example, in a CSV format, a comma (â,â) is the typical column delimiter.

RecordEncodingUpdate -> (string)

Specifies the encoding of the records in the streaming source; for example, UTF-8.

RecordColumnUpdates -> (list)

A list of `RecordColumn` objects. Each object describes the mapping of the streaming source element to the corresponding column in the in-application stream.

(structure)

For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

Name -> (string)

The name of the column that is created in the in-application input stream or reference table.

Mapping -> (string)

A reference to the data element in the streaming input or the reference data source.

SqlType -> (string)

The type of column created in the in-application input stream or reference table.

InputParallelismUpdate -> (structure)

Describes the parallelism updates (the number of in-application streams Kinesis Data Analytics creates for the specific streaming source).

CountUpdate -> (integer)

The number of in-application streams to create for the specified streaming source.

OutputUpdates -> (list)

The array of  OutputUpdate objects describing the new destination streams used by the application.

(structure)

For a SQL-based Kinesis Data Analytics application, describes updates to the output configuration identified by the `OutputId` .

OutputId -> (string)

Identifies the specific output configuration that you want to update.

NameUpdate -> (string)

If you want to specify a different in-application stream for this output configuration, use this field to specify the new in-application stream name.

KinesisStreamsOutputUpdate -> (structure)

Describes a Kinesis data stream as the destination for the output.

ResourceARNUpdate -> (string)

The Amazon Resource Name (ARN) of the Kinesis data stream where you want to write the output.

KinesisFirehoseOutputUpdate -> (structure)

Describes a Kinesis Data Firehose delivery stream as the destination for the output.

ResourceARNUpdate -> (string)

The Amazon Resource Name (ARN) of the delivery stream to write to.

LambdaOutputUpdate -> (structure)

Describes an Amazon Lambda function as the destination for the output.

ResourceARNUpdate -> (string)

The Amazon Resource Name (ARN) of the destination Amazon Lambda function.

### Note

To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: Amazon Lambda](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)

DestinationSchemaUpdate -> (structure)

Describes the data format when records are written to the destination.

RecordFormatType -> (string)

Specifies the format of the records on the output stream.

ReferenceDataSourceUpdates -> (list)

The array of  ReferenceDataSourceUpdate objects describing the new reference data sources used by the application.

(structure)

When you update a reference data source configuration for a SQL-based Kinesis Data Analytics application, this object provides all the updated values (such as the source bucket name and object key name), the in-application table name that is created, and updated mapping information that maps the data in the Amazon S3 object to the in-application reference table that is created.

ReferenceId -> (string)

The ID of the reference data source that is being updated. You can use the  DescribeApplication operation to get this value.

TableNameUpdate -> (string)

The in-application table name that is created by this update.

S3ReferenceDataSourceUpdate -> (structure)

Describes the S3 bucket name, object key name, and IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf and populate the in-application reference table.

BucketARNUpdate -> (string)

The Amazon Resource Name (ARN) of the S3 bucket.

FileKeyUpdate -> (string)

The object key name.

ReferenceSchemaUpdate -> (structure)

Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

RecordFormat -> (structure)

Specifies the format of the records on the streaming source.

RecordFormatType -> (string)

The type of record format.

MappingParameters -> (structure)

When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters -> (structure)

Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath -> (string)

The path to the top-level parent that contains the records.

CSVMappingParameters -> (structure)

Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter -> (string)

The row delimiter. For example, in a CSV format, *ânâ* is the typical row delimiter.

RecordColumnDelimiter -> (string)

The column delimiter. For example, in a CSV format, a comma (â,â) is the typical column delimiter.

RecordEncoding -> (string)

Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns -> (list)

A list of `RecordColumn` objects.

(structure)

For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

Name -> (string)

The name of the column that is created in the in-application input stream or reference table.

Mapping -> (string)

A reference to the data element in the streaming input or the reference data source.

SqlType -> (string)

The type of column created in the in-application input stream or reference table.

ApplicationCodeConfigurationUpdate -> (structure)

Describes updates to an applicationâs code configuration.

CodeContentTypeUpdate -> (string)

Describes updates to the code content type.

CodeContentUpdate -> (structure)

Describes updates to the code content of an application.

TextContentUpdate -> (string)

Describes an update to the text code for an application.

ZipFileContentUpdate -> (blob)

Describes an update to the zipped code for an application.

S3ContentLocationUpdate -> (structure)

Describes an update to the location of code for an application.

BucketARNUpdate -> (string)

The new Amazon Resource Name (ARN) for the S3 bucket containing the application code.

FileKeyUpdate -> (string)

The new file key for the object containing the application code.

ObjectVersionUpdate -> (string)

The new version of the object containing the application code.

FlinkApplicationConfigurationUpdate -> (structure)

Describes updates to a Managed Service for Apache Flink applicationâs configuration.

CheckpointConfigurationUpdate -> (structure)

Describes updates to an applicationâs checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.

ConfigurationTypeUpdate -> (string)

Describes updates to whether the application uses the default checkpointing behavior of Managed Service for Apache Flink. You must set this property to `CUSTOM` in order to set the `CheckpointingEnabled` , `CheckpointInterval` , or `MinPauseBetweenCheckpoints` parameters.

### Note

If this value is set to `DEFAULT` , the application will use the following values, even if they are set to other values using APIs or application code:

- **CheckpointingEnabled:** true
- **CheckpointInterval:** 60000
- **MinPauseBetweenCheckpoints:** 5000

CheckpointingEnabledUpdate -> (boolean)

Describes updates to whether checkpointing is enabled for an application.

### Note

If `CheckpointConfiguration.ConfigurationType` is `DEFAULT` , the application will use a `CheckpointingEnabled` value of `true` , even if this value is set to another value using this API or in application code.

CheckpointIntervalUpdate -> (long)

Describes updates to the interval in milliseconds between checkpoint operations.

### Note

If `CheckpointConfiguration.ConfigurationType` is `DEFAULT` , the application will use a `CheckpointInterval` value of 60000, even if this value is set to another value using this API or in application code.

MinPauseBetweenCheckpointsUpdate -> (long)

Describes updates to the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.

### Note

If `CheckpointConfiguration.ConfigurationType` is `DEFAULT` , the application will use a `MinPauseBetweenCheckpoints` value of 5000, even if this value is set using this API or in application code.

MonitoringConfigurationUpdate -> (structure)

Describes updates to the configuration parameters for Amazon CloudWatch logging for an application.

ConfigurationTypeUpdate -> (string)

Describes updates to whether to use the default CloudWatch logging configuration for an application. You must set this property to `CUSTOM` in order to set the `LogLevel` or `MetricsLevel` parameters.

MetricsLevelUpdate -> (string)

Describes updates to the granularity of the CloudWatch Logs for an application. The `Parallelism` level is not recommended for applications with a Parallelism over 64 due to excessive costs.

LogLevelUpdate -> (string)

Describes updates to the verbosity of the CloudWatch Logs for an application.

ParallelismConfigurationUpdate -> (structure)

Describes updates to the parameters for how an application executes multiple tasks simultaneously.

ConfigurationTypeUpdate -> (string)

Describes updates to whether the application uses the default parallelism for the Managed Service for Apache Flink service, or if a custom parallelism is used. You must set this property to `CUSTOM` in order to change your applicationâs `AutoScalingEnabled` , `Parallelism` , or `ParallelismPerKPU` properties.

ParallelismUpdate -> (integer)

Describes updates to the initial number of parallel tasks an application can perform. If `AutoScalingEnabled` is set to True, then Managed Service for Apache Flink can increase the `CurrentParallelism` value in response to application load. The service can increase `CurrentParallelism` up to the maximum parallelism, which is `ParalellismPerKPU` times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service will reduce `CurrentParallelism` down to the `Parallelism` setting.

ParallelismPerKPUUpdate -> (integer)

Describes updates to the number of parallel tasks an application can perform per Kinesis Processing Unit (KPU) used by the application.

AutoScalingEnabledUpdate -> (boolean)

Describes updates to whether the Managed Service for Apache Flink service can increase the parallelism of a Managed Service for Apache Flink application in response to increased throughput.

EnvironmentPropertyUpdates -> (structure)

Describes updates to the environment properties for a Managed Service for Apache Flink application.

PropertyGroups -> (list)

Describes updates to the execution property groups.

(structure)

Property key-value pairs passed into an application.

PropertyGroupId -> (string)

Describes the key of an application execution property key-value pair.

PropertyMap -> (map)

Describes the value of an application execution property key-value pair.

key -> (string)

value -> (string)

ApplicationSnapshotConfigurationUpdate -> (structure)

Describes whether snapshots are enabled for a Managed Service for Apache Flink application.

SnapshotsEnabledUpdate -> (boolean)

Describes updates to whether snapshots are enabled for an application.

ApplicationSystemRollbackConfigurationUpdate -> (structure)

Describes system rollback configuration for a Managed Service for Apache Flink application

RollbackEnabledUpdate -> (boolean)

Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application

VpcConfigurationUpdates -> (list)

Updates to the array of descriptions of VPC configurations available to the application.

(structure)

Describes updates to the VPC configuration used by the application.

VpcConfigurationId -> (string)

Describes an update to the ID of the VPC configuration.

SubnetIdUpdates -> (list)

Describes updates to the array of [Subnet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html) IDs used by the VPC configuration.

(string)

SecurityGroupIdUpdates -> (list)

Describes updates to the array of [SecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html) IDs used by the VPC configuration.

(string)

ZeppelinApplicationConfigurationUpdate -> (structure)

Updates to the configuration of a Managed Service for Apache Flink Studio notebook.

MonitoringConfigurationUpdate -> (structure)

Updates to the monitoring configuration of a Managed Service for Apache Flink Studio notebook.

LogLevelUpdate -> (string)

Updates to the logging level for Apache Zeppelin within a Managed Service for Apache Flink Studio notebook.

CatalogConfigurationUpdate -> (structure)

Updates to the configuration of the Amazon Glue Data Catalog that is associated with the Managed Service for Apache Flink Studio notebook.

GlueDataCatalogConfigurationUpdate -> (structure)

Updates to the configuration parameters for the default Amazon Glue database. You use this database for SQL queries that you write in a Managed Service for Apache Flink Studio notebook.

DatabaseARNUpdate -> (string)

The updated Amazon Resource Name (ARN) of the database.

DeployAsApplicationConfigurationUpdate -> (structure)

Updates to the configuration information required to deploy an Amazon Data Analytics Studio notebook as an application with durable state.

S3ContentLocationUpdate -> (structure)

Updates to the location that holds the data required to specify an Amazon Data Analytics application.

BucketARNUpdate -> (string)

The updated Amazon Resource Name (ARN) of the S3 bucket.

BasePathUpdate -> (string)

The updated S3 bucket path.

CustomArtifactsConfigurationUpdate -> (list)

Updates to the customer artifacts. Custom artifacts are dependency JAR files and user-defined functions (UDF).

(structure)

Specifies dependency JARs, as well as JAR files that contain user-defined functions (UDF).

ArtifactType -> (string)

`UDF` stands for user-defined functions. This type of artifact must be in an S3 bucket. A `DEPENDENCY_JAR` can be in either Maven or an S3 bucket.

S3ContentLocation -> (structure)

For a Managed Service for Apache Flink application provides a description of an Amazon S3 object, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data.

BucketARN -> (string)

The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

FileKey -> (string)

The file key for the object containing the application code.

ObjectVersion -> (string)

The version of the object containing the application code.

MavenReference -> (structure)

The parameters required to fully specify a Maven reference.

GroupId -> (string)

The group ID of the Maven reference.

ArtifactId -> (string)

The artifact ID of the Maven reference.

Version -> (string)

The version of the Maven reference.

JSON Syntax:

```
{
  "SqlApplicationConfigurationUpdate": {
    "InputUpdates": [
      {
        "InputId": "string",
        "NamePrefixUpdate": "string",
        "InputProcessingConfigurationUpdate": {
          "InputLambdaProcessorUpdate": {
            "ResourceARNUpdate": "string"
          }
        },
        "KinesisStreamsInputUpdate": {
          "ResourceARNUpdate": "string"
        },
        "KinesisFirehoseInputUpdate": {
          "ResourceARNUpdate": "string"
        },
        "InputSchemaUpdate": {
          "RecordFormatUpdate": {
            "RecordFormatType": "JSON"|"CSV",
            "MappingParameters": {
              "JSONMappingParameters": {
                "RecordRowPath": "string"
              },
              "CSVMappingParameters": {
                "RecordRowDelimiter": "string",
                "RecordColumnDelimiter": "string"
              }
            }
          },
          "RecordEncodingUpdate": "string",
          "RecordColumnUpdates": [
            {
              "Name": "string",
              "Mapping": "string",
              "SqlType": "string"
            }
            ...
          ]
        },
        "InputParallelismUpdate": {
          "CountUpdate": integer
        }
      }
      ...
    ],
    "OutputUpdates": [
      {
        "OutputId": "string",
        "NameUpdate": "string",
        "KinesisStreamsOutputUpdate": {
          "ResourceARNUpdate": "string"
        },
        "KinesisFirehoseOutputUpdate": {
          "ResourceARNUpdate": "string"
        },
        "LambdaOutputUpdate": {
          "ResourceARNUpdate": "string"
        },
        "DestinationSchemaUpdate": {
          "RecordFormatType": "JSON"|"CSV"
        }
      }
      ...
    ],
    "ReferenceDataSourceUpdates": [
      {
        "ReferenceId": "string",
        "TableNameUpdate": "string",
        "S3ReferenceDataSourceUpdate": {
          "BucketARNUpdate": "string",
          "FileKeyUpdate": "string"
        },
        "ReferenceSchemaUpdate": {
          "RecordFormat": {
            "RecordFormatType": "JSON"|"CSV",
            "MappingParameters": {
              "JSONMappingParameters": {
                "RecordRowPath": "string"
              },
              "CSVMappingParameters": {
                "RecordRowDelimiter": "string",
                "RecordColumnDelimiter": "string"
              }
            }
          },
          "RecordEncoding": "string",
          "RecordColumns": [
            {
              "Name": "string",
              "Mapping": "string",
              "SqlType": "string"
            }
            ...
          ]
        }
      }
      ...
    ]
  },
  "ApplicationCodeConfigurationUpdate": {
    "CodeContentTypeUpdate": "PLAINTEXT"|"ZIPFILE",
    "CodeContentUpdate": {
      "TextContentUpdate": "string",
      "ZipFileContentUpdate": blob,
      "S3ContentLocationUpdate": {
        "BucketARNUpdate": "string",
        "FileKeyUpdate": "string",
        "ObjectVersionUpdate": "string"
      }
    }
  },
  "FlinkApplicationConfigurationUpdate": {
    "CheckpointConfigurationUpdate": {
      "ConfigurationTypeUpdate": "DEFAULT"|"CUSTOM",
      "CheckpointingEnabledUpdate": true|false,
      "CheckpointIntervalUpdate": long,
      "MinPauseBetweenCheckpointsUpdate": long
    },
    "MonitoringConfigurationUpdate": {
      "ConfigurationTypeUpdate": "DEFAULT"|"CUSTOM",
      "MetricsLevelUpdate": "APPLICATION"|"TASK"|"OPERATOR"|"PARALLELISM",
      "LogLevelUpdate": "INFO"|"WARN"|"ERROR"|"DEBUG"
    },
    "ParallelismConfigurationUpdate": {
      "ConfigurationTypeUpdate": "DEFAULT"|"CUSTOM",
      "ParallelismUpdate": integer,
      "ParallelismPerKPUUpdate": integer,
      "AutoScalingEnabledUpdate": true|false
    }
  },
  "EnvironmentPropertyUpdates": {
    "PropertyGroups": [
      {
        "PropertyGroupId": "string",
        "PropertyMap": {"string": "string"
          ...}
      }
      ...
    ]
  },
  "ApplicationSnapshotConfigurationUpdate": {
    "SnapshotsEnabledUpdate": true|false
  },
  "ApplicationSystemRollbackConfigurationUpdate": {
    "RollbackEnabledUpdate": true|false
  },
  "VpcConfigurationUpdates": [
    {
      "VpcConfigurationId": "string",
      "SubnetIdUpdates": ["string", ...],
      "SecurityGroupIdUpdates": ["string", ...]
    }
    ...
  ],
  "ZeppelinApplicationConfigurationUpdate": {
    "MonitoringConfigurationUpdate": {
      "LogLevelUpdate": "INFO"|"WARN"|"ERROR"|"DEBUG"
    },
    "CatalogConfigurationUpdate": {
      "GlueDataCatalogConfigurationUpdate": {
        "DatabaseARNUpdate": "string"
      }
    },
    "DeployAsApplicationConfigurationUpdate": {
      "S3ContentLocationUpdate": {
        "BucketARNUpdate": "string",
        "BasePathUpdate": "string"
      }
    },
    "CustomArtifactsConfigurationUpdate": [
      {
        "ArtifactType": "UDF"|"DEPENDENCY_JAR",
        "S3ContentLocation": {
          "BucketARN": "string",
          "FileKey": "string",
          "ObjectVersion": "string"
        },
        "MavenReference": {
          "GroupId": "string",
          "ArtifactId": "string",
          "Version": "string"
        }
      }
      ...
    ]
  }
}
```

`--service-execution-role-update` (string)

Describes updates to the service execution role.

`--run-configuration-update` (structure)

Describes updates to the applicationâs starting parameters.

FlinkRunConfiguration -> (structure)

Describes the starting parameters for a Managed Service for Apache Flink application.

AllowNonRestoredState -> (boolean)

When restoring from a snapshot, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program. This will happen if the program is updated between snapshots to remove stateful parameters, and state data in the snapshot no longer corresponds to valid application data. For more information, see [Allowing Non-Restored State](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/ops/state/savepoints/#allowing-non-restored-state) in the [Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.19/) .

### Note

This value defaults to `false` . If you update your application without specifying this parameter, `AllowNonRestoredState` will be set to `false` , even if it was previously set to `true` .

ApplicationRestoreConfiguration -> (structure)

Describes updates to the restore behavior of a restarting application.

ApplicationRestoreType -> (string)

Specifies how the application should be restored.

SnapshotName -> (string)

The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if `RESTORE_FROM_CUSTOM_SNAPSHOT` is specified for the `ApplicationRestoreType` .

Shorthand Syntax:

```
FlinkRunConfiguration={AllowNonRestoredState=boolean},ApplicationRestoreConfiguration={ApplicationRestoreType=string,SnapshotName=string}
```

JSON Syntax:

```
{
  "FlinkRunConfiguration": {
    "AllowNonRestoredState": true|false
  },
  "ApplicationRestoreConfiguration": {
    "ApplicationRestoreType": "SKIP_RESTORE_FROM_SNAPSHOT"|"RESTORE_FROM_LATEST_SNAPSHOT"|"RESTORE_FROM_CUSTOM_SNAPSHOT",
    "SnapshotName": "string"
  }
}
```

`--cloud-watch-logging-option-updates` (list)

Describes application Amazon CloudWatch logging option updates. You can only update existing CloudWatch logging options with this action. To add a new CloudWatch logging option, use  AddApplicationCloudWatchLoggingOption .

(structure)

Describes the Amazon CloudWatch logging option updates.

CloudWatchLoggingOptionId -> (string)

The ID of the CloudWatch logging option to update

LogStreamARNUpdate -> (string)

The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

Shorthand Syntax:

```
CloudWatchLoggingOptionId=string,LogStreamARNUpdate=string ...
```

JSON Syntax:

```
[
  {
    "CloudWatchLoggingOptionId": "string",
    "LogStreamARNUpdate": "string"
  }
  ...
]
```

`--conditional-token` (string)

A value you use to implement strong concurrency for application updates. You must provide the `CurrentApplicationVersionId` or the `ConditionalToken` . You get the applicationâs current `ConditionalToken` using  DescribeApplication . For better concurrency support, use the `ConditionalToken` parameter instead of `CurrentApplicationVersionId` .

`--runtime-environment-update` (string)

Updates the Managed Service for Apache Flink runtime environment used to run your code. To avoid issues you must:

- Ensure your new jar and dependencies are compatible with the new runtime selected.
- Ensure your new codeâs state is compatible with the snapshot from which your application will start

Possible values:

- `SQL-1_0`
- `FLINK-1_6`
- `FLINK-1_8`
- `ZEPPELIN-FLINK-1_0`
- `FLINK-1_11`
- `FLINK-1_13`
- `ZEPPELIN-FLINK-2_0`
- `FLINK-1_15`
- `ZEPPELIN-FLINK-3_0`
- `FLINK-1_18`
- `FLINK-1_19`
- `FLINK-1_20`

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

ApplicationDetail -> (structure)

Describes application updates.

ApplicationARN -> (string)

The ARN of the application.

ApplicationDescription -> (string)

The description of the application.

ApplicationName -> (string)

The name of the application.

RuntimeEnvironment -> (string)

The runtime environment for the application.

ServiceExecutionRole -> (string)

Specifies the IAM role that the application uses to access external resources.

ApplicationStatus -> (string)

The status of the application.

ApplicationVersionId -> (long)

Provides the current application version. Managed Service for Apache Flink updates the `ApplicationVersionId` each time you update the application.

CreateTimestamp -> (timestamp)

The current timestamp when the application was created.

LastUpdateTimestamp -> (timestamp)

The current timestamp when the application was last updated.

ApplicationConfigurationDescription -> (structure)

Describes details about the application code and starting parameters for a Managed Service for Apache Flink application.

SqlApplicationConfigurationDescription -> (structure)

The details about inputs, outputs, and reference data sources for a SQL-based Kinesis Data Analytics application.

InputDescriptions -> (list)

The array of  InputDescription objects describing the input streams used by the application.

(structure)

Describes the application input configuration for a SQL-based Kinesis Data Analytics application.

InputId -> (string)

The input ID that is associated with the application input. This is the ID that Kinesis Data Analytics assigns to each input configuration that you add to your application.

NamePrefix -> (string)

The in-application name prefix.

InAppStreamNames -> (list)

Returns the in-application stream names that are mapped to the stream source.

(string)

InputProcessingConfigurationDescription -> (structure)

The description of the preprocessor that executes on records in this input before the applicationâs code is run.

InputLambdaProcessorDescription -> (structure)

Provides configuration information about the associated  InputLambdaProcessorDescription

ResourceARN -> (string)

The ARN of the Amazon Lambda function that is used to preprocess the records in the stream.

### Note

To specify an earlier version of the Lambda function than the latest, include the Lambda function version in the Lambda function ARN. For more information about Lambda ARNs, see [Example ARNs: Amazon Lambda](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html#arn-syntax-lambda)

RoleARN -> (string)

The ARN of the IAM role that is used to access the Amazon Lambda function.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

KinesisStreamsInputDescription -> (structure)

If a Kinesis data stream is configured as a streaming source, provides the Kinesis data streamâs Amazon Resource Name (ARN).

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN -> (string)

The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

KinesisFirehoseInputDescription -> (structure)

If a Kinesis Data Firehose delivery stream is configured as a streaming source, provides the delivery streamâs ARN.

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the delivery stream.

RoleARN -> (string)

The ARN of the IAM role that Kinesis Data Analytics assumes to access the stream.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

InputSchema -> (structure)

Describes the format of the data in the streaming source, and how each data element maps to corresponding columns in the in-application stream that is being created.

RecordFormat -> (structure)

Specifies the format of the records on the streaming source.

RecordFormatType -> (string)

The type of record format.

MappingParameters -> (structure)

When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters -> (structure)

Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath -> (string)

The path to the top-level parent that contains the records.

CSVMappingParameters -> (structure)

Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter -> (string)

The row delimiter. For example, in a CSV format, *ânâ* is the typical row delimiter.

RecordColumnDelimiter -> (string)

The column delimiter. For example, in a CSV format, a comma (â,â) is the typical column delimiter.

RecordEncoding -> (string)

Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns -> (list)

A list of `RecordColumn` objects.

(structure)

For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

Name -> (string)

The name of the column that is created in the in-application input stream or reference table.

Mapping -> (string)

A reference to the data element in the streaming input or the reference data source.

SqlType -> (string)

The type of column created in the in-application input stream or reference table.

InputParallelism -> (structure)

Describes the configured parallelism (number of in-application streams mapped to the streaming source).

Count -> (integer)

The number of in-application streams to create.

InputStartingPositionConfiguration -> (structure)

The point at which the application is configured to read from the input stream.

InputStartingPosition -> (string)

The starting position on the stream.

- `NOW` - Start reading just after the most recent record in the stream, and start at the request timestamp that the customer issued.
- `TRIM_HORIZON` - Start reading at the last untrimmed record in the stream, which is the oldest record available in the stream. This option is not available for an Amazon Kinesis Data Firehose delivery stream.
- `LAST_STOPPED_POINT` - Resume reading from where the application last stopped reading.

OutputDescriptions -> (list)

The array of  OutputDescription objects describing the destination streams used by the application.

(structure)

For a SQL-based Kinesis Data Analytics application, describes the application output configuration, which includes the in-application stream name and the destination where the stream data is written. The destination can be a Kinesis data stream or a Kinesis Data Firehose delivery stream.

OutputId -> (string)

A unique identifier for the output configuration.

Name -> (string)

The name of the in-application stream that is configured as output.

KinesisStreamsOutputDescription -> (structure)

Describes the Kinesis data stream that is configured as the destination where output is written.

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the Kinesis data stream.

RoleARN -> (string)

The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

KinesisFirehoseOutputDescription -> (structure)

Describes the Kinesis Data Firehose delivery stream that is configured as the destination where output is written.

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the delivery stream.

RoleARN -> (string)

The ARN of the IAM role that Kinesis Data Analytics can assume to access the stream.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

LambdaOutputDescription -> (structure)

Describes the Lambda function that is configured as the destination where output is written.

ResourceARN -> (string)

The Amazon Resource Name (ARN) of the destination Lambda function.

RoleARN -> (string)

The ARN of the IAM role that Kinesis Data Analytics can assume to write to the destination function.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

DestinationSchema -> (structure)

The data format used for writing data to the destination.

RecordFormatType -> (string)

Specifies the format of the records on the output stream.

ReferenceDataSourceDescriptions -> (list)

The array of  ReferenceDataSourceDescription objects describing the reference data sources used by the application.

(structure)

For a SQL-based Kinesis Data Analytics application, describes the reference data source configured for an application.

ReferenceId -> (string)

The ID of the reference data source. This is the ID that Kinesis Data Analytics assigns when you add the reference data source to your application using the  CreateApplication or  UpdateApplication operation.

TableName -> (string)

The in-application table name created by the specific reference data source configuration.

S3ReferenceDataSourceDescription -> (structure)

Provides the Amazon S3 bucket name, the object key name that contains the reference data.

BucketARN -> (string)

The Amazon Resource Name (ARN) of the S3 bucket.

FileKey -> (string)

Amazon S3 object key name.

ReferenceRoleARN -> (string)

The ARN of the IAM role that Kinesis Data Analytics can assume to read the Amazon S3 object on your behalf to populate the in-application reference table.

### Note

Provided for backward compatibility. Applications that are created with the current API version have an application-level service execution role rather than a resource-level role.

ReferenceSchema -> (structure)

Describes the format of the data in the streaming source, and how each data element maps to corresponding columns created in the in-application stream.

RecordFormat -> (structure)

Specifies the format of the records on the streaming source.

RecordFormatType -> (string)

The type of record format.

MappingParameters -> (structure)

When you configure application input at the time of creating or updating an application, provides additional mapping information specific to the record format (such as JSON, CSV, or record fields delimited by some delimiter) on the streaming source.

JSONMappingParameters -> (structure)

Provides additional mapping information when JSON is the record format on the streaming source.

RecordRowPath -> (string)

The path to the top-level parent that contains the records.

CSVMappingParameters -> (structure)

Provides additional mapping information when the record format uses delimiters (for example, CSV).

RecordRowDelimiter -> (string)

The row delimiter. For example, in a CSV format, *ânâ* is the typical row delimiter.

RecordColumnDelimiter -> (string)

The column delimiter. For example, in a CSV format, a comma (â,â) is the typical column delimiter.

RecordEncoding -> (string)

Specifies the encoding of the records in the streaming source. For example, UTF-8.

RecordColumns -> (list)

A list of `RecordColumn` objects.

(structure)

For a SQL-based Kinesis Data Analytics application, describes the mapping of each data element in the streaming source to the corresponding column in the in-application stream.

Also used to describe the format of the reference data source.

Name -> (string)

The name of the column that is created in the in-application input stream or reference table.

Mapping -> (string)

A reference to the data element in the streaming input or the reference data source.

SqlType -> (string)

The type of column created in the in-application input stream or reference table.

ApplicationCodeConfigurationDescription -> (structure)

The details about the application code for a Managed Service for Apache Flink application.

CodeContentType -> (string)

Specifies whether the code content is in text or zip format.

CodeContentDescription -> (structure)

Describes details about the location and format of the application code.

TextContent -> (string)

The text-format code

CodeMD5 -> (string)

The checksum that can be used to validate zip-format code.

CodeSize -> (long)

The size in bytes of the application code. Can be used to validate zip-format code.

S3ApplicationCodeLocationDescription -> (structure)

The S3 bucket Amazon Resource Name (ARN), file key, and object version of the application code stored in Amazon S3.

BucketARN -> (string)

The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

FileKey -> (string)

The file key for the object containing the application code.

ObjectVersion -> (string)

The version of the object containing the application code.

RunConfigurationDescription -> (structure)

The details about the starting properties for a Managed Service for Apache Flink application.

ApplicationRestoreConfigurationDescription -> (structure)

Describes the restore behavior of a restarting application.

ApplicationRestoreType -> (string)

Specifies how the application should be restored.

SnapshotName -> (string)

The identifier of an existing snapshot of application state to use to restart an application. The application uses this value if `RESTORE_FROM_CUSTOM_SNAPSHOT` is specified for the `ApplicationRestoreType` .

FlinkRunConfigurationDescription -> (structure)

Describes the starting parameters for a Managed Service for Apache Flink application.

AllowNonRestoredState -> (boolean)

When restoring from a snapshot, specifies whether the runtime is allowed to skip a state that cannot be mapped to the new program. This will happen if the program is updated between snapshots to remove stateful parameters, and state data in the snapshot no longer corresponds to valid application data. For more information, see [Allowing Non-Restored State](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/ops/state/savepoints/#allowing-non-restored-state) in the [Apache Flink documentation](https://nightlies.apache.org/flink/flink-docs-release-1.19/) .

### Note

This value defaults to `false` . If you update your application without specifying this parameter, `AllowNonRestoredState` will be set to `false` , even if it was previously set to `true` .

FlinkApplicationConfigurationDescription -> (structure)

The details about a Managed Service for Apache Flink application.

CheckpointConfigurationDescription -> (structure)

Describes an applicationâs checkpointing configuration. Checkpointing is the process of persisting application state for fault tolerance.

ConfigurationType -> (string)

Describes whether the application uses the default checkpointing behavior in Managed Service for Apache Flink.

### Note

If this value is set to `DEFAULT` , the application will use the following values, even if they are set to other values using APIs or application code:

- **CheckpointingEnabled:** true
- **CheckpointInterval:** 60000
- **MinPauseBetweenCheckpoints:** 5000

CheckpointingEnabled -> (boolean)

Describes whether checkpointing is enabled for a Managed Service for Apache Flink application.

### Note

If `CheckpointConfiguration.ConfigurationType` is `DEFAULT` , the application will use a `CheckpointingEnabled` value of `true` , even if this value is set to another value using this API or in application code.

CheckpointInterval -> (long)

Describes the interval in milliseconds between checkpoint operations.

### Note

If `CheckpointConfiguration.ConfigurationType` is `DEFAULT` , the application will use a `CheckpointInterval` value of 60000, even if this value is set to another value using this API or in application code.

MinPauseBetweenCheckpoints -> (long)

Describes the minimum time in milliseconds after a checkpoint operation completes that a new checkpoint operation can start.

### Note

If `CheckpointConfiguration.ConfigurationType` is `DEFAULT` , the application will use a `MinPauseBetweenCheckpoints` value of 5000, even if this value is set using this API or in application code.

MonitoringConfigurationDescription -> (structure)

Describes configuration parameters for Amazon CloudWatch logging for an application.

ConfigurationType -> (string)

Describes whether to use the default CloudWatch logging configuration for an application.

MetricsLevel -> (string)

Describes the granularity of the CloudWatch Logs for an application.

LogLevel -> (string)

Describes the verbosity of the CloudWatch Logs for an application.

ParallelismConfigurationDescription -> (structure)

Describes parameters for how an application executes multiple tasks simultaneously.

ConfigurationType -> (string)

Describes whether the application uses the default parallelism for the Managed Service for Apache Flink service.

Parallelism -> (integer)

Describes the initial number of parallel tasks that a Managed Service for Apache Flink application can perform. If `AutoScalingEnabled` is set to True, then Managed Service for Apache Flink can increase the `CurrentParallelism` value in response to application load. The service can increase `CurrentParallelism` up to the maximum parallelism, which is `ParalellismPerKPU` times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the `CurrentParallelism` value down to the `Parallelism` setting.

ParallelismPerKPU -> (integer)

Describes the number of parallel tasks that a Managed Service for Apache Flink application can perform per Kinesis Processing Unit (KPU) used by the application.

CurrentParallelism -> (integer)

Describes the current number of parallel tasks that a Managed Service for Apache Flink application can perform. If `AutoScalingEnabled` is set to True, Managed Service for Apache Flink can increase this value in response to application load. The service can increase this value up to the maximum parallelism, which is `ParalellismPerKPU` times the maximum KPUs for the application. The maximum KPUs for an application is 32 by default, and can be increased by requesting a limit increase. If application load is reduced, the service can reduce the `CurrentParallelism` value down to the `Parallelism` setting.

AutoScalingEnabled -> (boolean)

Describes whether the Managed Service for Apache Flink service can increase the parallelism of the application in response to increased throughput.

JobPlanDescription -> (string)

The job plan for an application. For more information about the job plan, see [Jobs and Scheduling](https://nightlies.apache.org/flink/flink-docs-release-1.19/internals/job_scheduling.html) in the [Apache Flink Documentation](https://nightlies.apache.org/flink/flink-docs-release-1.19/) . To retrieve the job plan for the application, use the  DescribeApplicationRequest$IncludeAdditionalDetails parameter of the  DescribeApplication operation.

EnvironmentPropertyDescriptions -> (structure)

Describes execution properties for a Managed Service for Apache Flink application.

PropertyGroupDescriptions -> (list)

Describes the execution property groups.

(structure)

Property key-value pairs passed into an application.

PropertyGroupId -> (string)

Describes the key of an application execution property key-value pair.

PropertyMap -> (map)

Describes the value of an application execution property key-value pair.

key -> (string)

value -> (string)

ApplicationSnapshotConfigurationDescription -> (structure)

Describes whether snapshots are enabled for a Managed Service for Apache Flink application.

SnapshotsEnabled -> (boolean)

Describes whether snapshots are enabled for a Managed Service for Apache Flink application.

ApplicationSystemRollbackConfigurationDescription -> (structure)

Describes system rollback configuration for a Managed Service for Apache Flink application

RollbackEnabled -> (boolean)

Describes whether system rollbacks are enabled for a Managed Service for Apache Flink application

VpcConfigurationDescriptions -> (list)

The array of descriptions of VPC configurations available to the application.

(structure)

Describes the parameters of a VPC used by the application.

VpcConfigurationId -> (string)

The ID of the VPC configuration.

VpcId -> (string)

The ID of the associated VPC.

SubnetIds -> (list)

The array of [Subnet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Subnet.html) IDs used by the VPC configuration.

(string)

SecurityGroupIds -> (list)

The array of [SecurityGroup](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SecurityGroup.html) IDs used by the VPC configuration.

(string)

ZeppelinApplicationConfigurationDescription -> (structure)

The configuration parameters for a Managed Service for Apache Flink Studio notebook.

MonitoringConfigurationDescription -> (structure)

The monitoring configuration of a Managed Service for Apache Flink Studio notebook.

LogLevel -> (string)

Describes the verbosity of the CloudWatch Logs for an application.

CatalogConfigurationDescription -> (structure)

The Amazon Glue Data Catalog that is associated with the Managed Service for Apache Flink Studio notebook.

GlueDataCatalogConfigurationDescription -> (structure)

The configuration parameters for the default Amazon Glue database. You use this database for SQL queries that you write in a Managed Service for Apache Flink Studio notebook.

DatabaseARN -> (string)

The Amazon Resource Name (ARN) of the database.

DeployAsApplicationConfigurationDescription -> (structure)

The parameters required to deploy a Managed Service for Apache Flink Studio notebook as an application with durable state.

S3ContentLocationDescription -> (structure)

The location that holds the data required to specify an Amazon Data Analytics application.

BucketARN -> (string)

The Amazon Resource Name (ARN) of the S3 bucket.

BasePath -> (string)

The base path for the S3 bucket.

CustomArtifactsConfigurationDescription -> (list)

Custom artifacts are dependency JARs and user-defined functions (UDF).

(structure)

Specifies a dependency JAR or a JAR of user-defined functions.

ArtifactType -> (string)

`UDF` stands for user-defined functions. This type of artifact must be in an S3 bucket. A `DEPENDENCY_JAR` can be in either Maven or an S3 bucket.

S3ContentLocationDescription -> (structure)

For a Managed Service for Apache Flink application provides a description of an Amazon S3 object, including the Amazon Resource Name (ARN) of the S3 bucket, the name of the Amazon S3 object that contains the data, and the version number of the Amazon S3 object that contains the data.

BucketARN -> (string)

The Amazon Resource Name (ARN) for the S3 bucket containing the application code.

FileKey -> (string)

The file key for the object containing the application code.

ObjectVersion -> (string)

The version of the object containing the application code.

MavenReferenceDescription -> (structure)

The parameters that are required to specify a Maven dependency.

GroupId -> (string)

The group ID of the Maven reference.

ArtifactId -> (string)

The artifact ID of the Maven reference.

Version -> (string)

The version of the Maven reference.

CloudWatchLoggingOptionDescriptions -> (list)

Describes the application Amazon CloudWatch logging options.

(structure)

Describes the Amazon CloudWatch logging option.

CloudWatchLoggingOptionId -> (string)

The ID of the CloudWatch logging option description.

LogStreamARN -> (string)

The Amazon Resource Name (ARN) of the CloudWatch log to receive application messages.

RoleARN -> (string)

The IAM ARN of the role to use to send application messages.

### Note

Provided for backward compatibility. Applications created with the current API version have an application-level service execution role rather than a resource-level role.

ApplicationMaintenanceConfigurationDescription -> (structure)

The details of the maintenance configuration for the application.

ApplicationMaintenanceWindowStartTime -> (string)

The start time for the maintenance window.

ApplicationMaintenanceWindowEndTime -> (string)

The end time for the maintenance window.

ApplicationVersionUpdatedFrom -> (long)

The previous application version before the latest application update.  RollbackApplication reverts the application to this version.

ApplicationVersionRolledBackFrom -> (long)

If you reverted the application using  RollbackApplication , the application version when `RollbackApplication` was called.

ApplicationVersionCreateTimestamp -> (timestamp)

The current timestamp when the application version was created.

ConditionalToken -> (string)

A value you use to implement strong concurrency for application updates.

ApplicationVersionRolledBackTo -> (long)

The version to which you want to roll back the application.

ApplicationMode -> (string)

To create a Managed Service for Apache Flink Studio notebook, you must set the mode to `INTERACTIVE` . However, for a Managed Service for Apache Flink application, the mode is optional.

OperationId -> (string)

Operation ID for tracking UpdateApplication request