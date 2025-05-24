# get-environmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/get-environment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/get-environment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mwaa](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/index.html#cli-aws-mwaa) ]

# get-environment

## Description

Describes an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mwaa-2020-07-01/GetEnvironment)

## Synopsis

```
get-environment
--name <value>
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

`--name` (string)

The name of the Amazon MWAA environment. For example, `MyMWAAEnvironment` .

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

Environment -> (structure)

An object containing all available details about the environment.

Name -> (string)

The name of the Amazon MWAA environment. For example, `MyMWAAEnvironment` .

Status -> (string)

The status of the Amazon MWAA environment.

Valid values:

- `CREATING` - Indicates the request to create the environment is in progress.
- `CREATING_SNAPSHOT` - Indicates the request to update environment details, or upgrade the environment version, is in progress and Amazon MWAA is creating a storage volume snapshot of the Amazon RDS database cluster associated with the environment. A database snapshot is a backup created at a specific point in time. Amazon MWAA uses snapshots to recover environment metadata if the process to update or upgrade an environment fails.
- `CREATE_FAILED` - Indicates the request to create the environment failed, and the environment could not be created.
- `AVAILABLE` - Indicates the request was successful and the environment is ready to use.
- `PENDING` - Indicates the request was successful, but the process to create the environment is paused until you create the required VPC endpoints in your VPC. After you create the VPC endpoints, the process resumes.
- `UPDATING` - Indicates the request to update the environment is in progress.
- `ROLLING_BACK` - Indicates the request to update environment details, or upgrade the environment version, failed and Amazon MWAA is restoring the environment using the latest storage volume snapshot.
- `DELETING` - Indicates the request to delete the environment is in progress.
- `DELETED` - Indicates the request to delete the environment is complete, and the environment has been deleted.
- `UNAVAILABLE` - Indicates the request failed, but the environment did not return to its previous state and is not stable.
- `UPDATE_FAILED` - Indicates the request to update the environment failed, and the environment was restored to its previous state successfully and is ready to use.
- `MAINTENANCE` - Indicates that the environment is undergoing maintenance. Depending on the type of work Amazon MWAA is performing, your environment might become unavailable during this process. After all operations are done, your environment will return to its status prior to mainteneace operations.

We recommend reviewing our troubleshooting guide for a list of common errors and their solutions. For more information, see [Amazon MWAA troubleshooting](https://docs.aws.amazon.com/mwaa/latest/userguide/troubleshooting.html) .

Arn -> (string)

The Amazon Resource Name (ARN) of the Amazon MWAA environment.

CreatedAt -> (timestamp)

The day and time the environment was created.

WebserverUrl -> (string)

The Apache Airflow *web server* host name for the Amazon MWAA environment. For more information, see [Accessing the Apache Airflow UI](https://docs.aws.amazon.com/mwaa/latest/userguide/access-airflow-ui.html) .

ExecutionRoleArn -> (string)

The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access Amazon Web Services resources in your environment. For example, `arn:aws:iam::123456789:role/my-execution-role` . For more information, see [Amazon MWAA Execution role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html) .

ServiceRoleArn -> (string)

The Amazon Resource Name (ARN) for the service-linked role of the environment. For more information, see [Amazon MWAA Service-linked role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-slr.html) .

KmsKey -> (string)

The KMS encryption key used to encrypt the data in your environment.

AirflowVersion -> (string)

The Apache Airflow version on your environment.

Valid values: `1.10.12` , `2.0.2` , `2.2.2` , `2.4.3` , `2.5.1` , `2.6.3` , `2.7.2` , `2.8.1` , `2.9.2` , `2.10.1` , and `2.10.3` .

SourceBucketArn -> (string)

The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, `arn:aws:s3:::my-airflow-bucket-unique-name` . For more information, see [Create an Amazon S3 bucket for Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html) .

DagS3Path -> (string)

The relative path to the DAGs folder in your Amazon S3 bucket. For example, `s3://mwaa-environment/dags` . For more information, see [Adding or updating DAGs](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html) .

PluginsS3Path -> (string)

The relative path to the file in your Amazon S3 bucket. For example, `s3://mwaa-environment/plugins.zip` . For more information, see [Installing custom plugins](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html) .

PluginsS3ObjectVersion -> (string)

The version of the `plugins.zip` file in your Amazon S3 bucket. You must specify the [version ID](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) that Amazon S3 assigns to the file.

Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example:

`3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`

For more information, see [Installing custom plugins](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html) .

RequirementsS3Path -> (string)

The relative path to the `requirements.txt` file in your Amazon S3 bucket. For example, `s3://mwaa-environment/requirements.txt` . For more information, see [Installing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html) .

RequirementsS3ObjectVersion -> (string)

The version of the `requirements.txt` file on your Amazon S3 bucket. You must specify the [version ID](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) that Amazon S3 assigns to the file.

Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example:

`3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`

For more information, see [Installing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html) .

StartupScriptS3Path -> (string)

The relative path to the startup shell script in your Amazon S3 bucket. For example, `s3://mwaa-environment/startup.sh` .

Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, see [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html) .

StartupScriptS3ObjectVersion -> (string)

The version of the startup shell script in your Amazon S3 bucket. You must specify the [version ID](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) that Amazon S3 assigns to the file.

Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example:

`3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`

For more information, see [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html) .

AirflowConfigurationOptions -> (map)

A list of key-value pairs containing the Apache Airflow configuration options attached to your environment. For more information, see [Apache Airflow configuration options](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html) .

key -> (string)

value -> (string)

EnvironmentClass -> (string)

The environment class type. Valid values: `mw1.micro` , `mw1.small` , `mw1.medium` , `mw1.large` , `mw1.xlarge` , and `mw1.2xlarge` . For more information, see [Amazon MWAA environment class](https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html) .

MaxWorkers -> (integer)

The maximum number of workers that run in your environment. For example, `20` .

NetworkConfiguration -> (structure)

Describes the VPC networking components used to secure and enable network traffic between the Amazon Web Services resources for your environment. For more information, see [About networking on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html) .

SubnetIds -> (list)

A list of subnet IDs. For more information, see [About networking on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html) .

(string)

SecurityGroupIds -> (list)

A list of security group IDs. For more information, see [Security in your VPC on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html) .

(string)

LoggingConfiguration -> (structure)

The Apache Airflow logs published to CloudWatch Logs.

DagProcessingLogs -> (structure)

The Airflow DAG processing logs published to CloudWatch Logs and the log level.

Enabled -> (boolean)

Indicates whether the Apache Airflow log type (e.g. `DagProcessingLogs` ) is enabled.

LogLevel -> (string)

The Apache Airflow log level for the log type (e.g. `DagProcessingLogs` ).

CloudWatchLogGroupArn -> (string)

The Amazon Resource Name (ARN) for the CloudWatch Logs group where the Apache Airflow log type (e.g. `DagProcessingLogs` ) is published. For example, `arn:aws:logs:us-east-1:123456789012:log-group:airflow-MyMWAAEnvironment-MwaaEnvironment-DAGProcessing:*` .

SchedulerLogs -> (structure)

The Airflow scheduler logs published to CloudWatch Logs and the log level.

Enabled -> (boolean)

Indicates whether the Apache Airflow log type (e.g. `DagProcessingLogs` ) is enabled.

LogLevel -> (string)

The Apache Airflow log level for the log type (e.g. `DagProcessingLogs` ).

CloudWatchLogGroupArn -> (string)

The Amazon Resource Name (ARN) for the CloudWatch Logs group where the Apache Airflow log type (e.g. `DagProcessingLogs` ) is published. For example, `arn:aws:logs:us-east-1:123456789012:log-group:airflow-MyMWAAEnvironment-MwaaEnvironment-DAGProcessing:*` .

WebserverLogs -> (structure)

The Airflow web server logs published to CloudWatch Logs and the log level.

Enabled -> (boolean)

Indicates whether the Apache Airflow log type (e.g. `DagProcessingLogs` ) is enabled.

LogLevel -> (string)

The Apache Airflow log level for the log type (e.g. `DagProcessingLogs` ).

CloudWatchLogGroupArn -> (string)

The Amazon Resource Name (ARN) for the CloudWatch Logs group where the Apache Airflow log type (e.g. `DagProcessingLogs` ) is published. For example, `arn:aws:logs:us-east-1:123456789012:log-group:airflow-MyMWAAEnvironment-MwaaEnvironment-DAGProcessing:*` .

WorkerLogs -> (structure)

The Airflow worker logs published to CloudWatch Logs and the log level.

Enabled -> (boolean)

Indicates whether the Apache Airflow log type (e.g. `DagProcessingLogs` ) is enabled.

LogLevel -> (string)

The Apache Airflow log level for the log type (e.g. `DagProcessingLogs` ).

CloudWatchLogGroupArn -> (string)

The Amazon Resource Name (ARN) for the CloudWatch Logs group where the Apache Airflow log type (e.g. `DagProcessingLogs` ) is published. For example, `arn:aws:logs:us-east-1:123456789012:log-group:airflow-MyMWAAEnvironment-MwaaEnvironment-DAGProcessing:*` .

TaskLogs -> (structure)

The Airflow task logs published to CloudWatch Logs and the log level.

Enabled -> (boolean)

Indicates whether the Apache Airflow log type (e.g. `DagProcessingLogs` ) is enabled.

LogLevel -> (string)

The Apache Airflow log level for the log type (e.g. `DagProcessingLogs` ).

CloudWatchLogGroupArn -> (string)

The Amazon Resource Name (ARN) for the CloudWatch Logs group where the Apache Airflow log type (e.g. `DagProcessingLogs` ) is published. For example, `arn:aws:logs:us-east-1:123456789012:log-group:airflow-MyMWAAEnvironment-MwaaEnvironment-DAGProcessing:*` .

LastUpdate -> (structure)

The status of the last update on the environment.

Status -> (string)

The status of the last update on the environment.

CreatedAt -> (timestamp)

The day and time of the last update on the environment.

Error -> (structure)

The error that was encountered during the last update of the environment.

ErrorCode -> (string)

The error code that corresponds to the error with the last update.

ErrorMessage -> (string)

The error message that corresponds to the error code.

Source -> (string)

The source of the last update to the environment. Includes internal processes by Amazon MWAA, such as an environment maintenance update.

WeeklyMaintenanceWindowStart -> (string)

The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time that weekly maintenance updates are scheduled. For example: `TUE:03:30` .

Tags -> (map)

The key-value tag pairs associated to your environment. For example, `"Environment": "Staging"` . For more information, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) .

key -> (string)

value -> (string)

WebserverAccessMode -> (string)

The Apache Airflow *web server* access mode. For more information, see [Apache Airflow access modes](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html) .

MinWorkers -> (integer)

The minimum number of workers that run in your environment. For example, `2` .

Schedulers -> (integer)

The number of Apache Airflow schedulers that run in your Amazon MWAA environment.

WebserverVpcEndpointService -> (string)

The VPC endpoint for the environmentâs web server.

DatabaseVpcEndpointService -> (string)

The VPC endpoint for the environmentâs Amazon RDS database.

CeleryExecutorQueue -> (string)

The queue ARN for the environmentâs [Celery Executor](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/executor/celery.html) . Amazon MWAA uses a Celery Executor to distribute tasks across multiple workers. When you create an environment in a shared VPC, you must provide access to the Celery Executor queue from your VPC.

EndpointManagement -> (string)

Defines whether the VPC endpoints configured for the environment are created, and managed, by the customer or by Amazon MWAA. If set to `SERVICE` , Amazon MWAA will create and manage the required VPC endpoints in your VPC. If set to `CUSTOMER` , you must create, and manage, the VPC endpoints in your VPC.

MinWebservers -> (integer)

The minimum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for `MaxWebservers` when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. As the transaction-per-second rate, and the network load, decrease, Amazon MWAA disposes of the additional web servers, and scales down to the number set in `MinxWebserers` .

Valid values: For environments larger than mw1.micro, accepts values from `2` to `5` . Defaults to `2` for all environment sizes except mw1.micro, which defaults to `1` .

MaxWebservers -> (integer)

The maximum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for `MaxWebservers` when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. For example, in scenarios where your workload requires network calls to the Apache Airflow REST API with a high transaction-per-second (TPS) rate, Amazon MWAA will increase the number of web servers up to the number set in `MaxWebserers` . As TPS rates decrease Amazon MWAA disposes of the additional web servers, and scales down to the number set in `MinxWebserers` .

Valid values: For environments larger than mw1.micro, accepts values from `2` to `5` . Defaults to `2` for all environment sizes except mw1.micro, which defaults to `1` .