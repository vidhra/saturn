# update-environmentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/update-environment.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/update-environment.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mwaa](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mwaa/index.html#cli-aws-mwaa) ]

# update-environment

## Description

Updates an Amazon Managed Workflows for Apache Airflow (MWAA) environment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mwaa-2020-07-01/UpdateEnvironment)

## Synopsis

```
update-environment
--name <value>
[--execution-role-arn <value>]
[--airflow-version <value>]
[--source-bucket-arn <value>]
[--dag-s3-path <value>]
[--plugins-s3-path <value>]
[--plugins-s3-object-version <value>]
[--requirements-s3-path <value>]
[--requirements-s3-object-version <value>]
[--startup-script-s3-path <value>]
[--startup-script-s3-object-version <value>]
[--airflow-configuration-options <value>]
[--environment-class <value>]
[--max-workers <value>]
[--network-configuration <value>]
[--logging-configuration <value>]
[--weekly-maintenance-window-start <value>]
[--webserver-access-mode <value>]
[--min-workers <value>]
[--schedulers <value>]
[--min-webservers <value>]
[--max-webservers <value>]
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

The name of your Amazon MWAA environment. For example, `MyMWAAEnvironment` .

`--execution-role-arn` (string)

The Amazon Resource Name (ARN) of the execution role in IAM that allows MWAA to access Amazon Web Services resources in your environment. For example, `arn:aws:iam::123456789:role/my-execution-role` . For more information, see [Amazon MWAA Execution role](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-create-role.html) .

`--airflow-version` (string)

The Apache Airflow version for your environment. To upgrade your environment, specify a newer version of Apache Airflow supported by Amazon MWAA.

Before you upgrade an environment, make sure your requirements, DAGs, plugins, and other resources used in your workflows are compatible with the new Apache Airflow version. For more information about updating your resources, see [Upgrading an Amazon MWAA environment](https://docs.aws.amazon.com/mwaa/latest/userguide/upgrading-environment.html) .

Valid values: `1.10.12` , `2.0.2` , `2.2.2` , `2.4.3` , `2.5.1` , `2.6.3` , `2.7.2` , `2.8.1` , `2.9.2` , `2.10.1` , and `2.10.3` .

`--source-bucket-arn` (string)

The Amazon Resource Name (ARN) of the Amazon S3 bucket where your DAG code and supporting files are stored. For example, `arn:aws:s3:::my-airflow-bucket-unique-name` . For more information, see [Create an Amazon S3 bucket for Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/mwaa-s3-bucket.html) .

`--dag-s3-path` (string)

The relative path to the DAGs folder on your Amazon S3 bucket. For example, `dags` . For more information, see [Adding or updating DAGs](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-folder.html) .

`--plugins-s3-path` (string)

The relative path to the `plugins.zip` file on your Amazon S3 bucket. For example, `plugins.zip` . If specified, then the plugins.zip version is required. For more information, see [Installing custom plugins](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-dag-import-plugins.html) .

`--plugins-s3-object-version` (string)

The version of the plugins.zip file on your Amazon S3 bucket. You must specify a version each time a `plugins.zip` file is updated. For more information, see [How S3 Versioning works](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) .

`--requirements-s3-path` (string)

The relative path to the `requirements.txt` file on your Amazon S3 bucket. For example, `requirements.txt` . If specified, then a file version is required. For more information, see [Installing Python dependencies](https://docs.aws.amazon.com/mwaa/latest/userguide/working-dags-dependencies.html) .

`--requirements-s3-object-version` (string)

The version of the requirements.txt file on your Amazon S3 bucket. You must specify a version each time a `requirements.txt` file is updated. For more information, see [How S3 Versioning works](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) .

`--startup-script-s3-path` (string)

The relative path to the startup shell script in your Amazon S3 bucket. For example, `s3://mwaa-environment/startup.sh` .

Amazon MWAA runs the script as your environment starts, and before running the Apache Airflow process. You can use this script to install dependencies, modify Apache Airflow configuration options, and set environment variables. For more information, see [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html) .

`--startup-script-s3-object-version` (string)

The version of the startup shell script in your Amazon S3 bucket. You must specify the [version ID](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) that Amazon S3 assigns to the file every time you update the script.

Version IDs are Unicode, UTF-8 encoded, URL-ready, opaque strings that are no more than 1,024 bytes long. The following is an example:

`3sL4kqtJlcpXroDTDmJ+rmSpXd3dIbrHY+MTRCxf3vjVBH40Nr8X8gdRQBpUMLUo`

For more information, see [Using a startup script](https://docs.aws.amazon.com/mwaa/latest/userguide/using-startup-script.html) .

`--airflow-configuration-options` (map)

A list of key-value pairs containing the Apache Airflow configuration options you want to attach to your environment. For more information, see [Apache Airflow configuration options](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-env-variables.html) .

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--environment-class` (string)

The environment class type. Valid values: `mw1.micro` , `mw1.small` , `mw1.medium` , `mw1.large` , `mw1.xlarge` , and `mw1.2xlarge` . For more information, see [Amazon MWAA environment class](https://docs.aws.amazon.com/mwaa/latest/userguide/environment-class.html) .

`--max-workers` (integer)

The maximum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the `MaxWorkers` field. For example, `20` . When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the one worker that is included with your environment, or the number you specify in `MinWorkers` .

`--network-configuration` (structure)

The VPC networking components used to secure and enable network traffic between the Amazon Web Services resources for your environment. For more information, see [About networking on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/networking-about.html) .

SecurityGroupIds -> (list)

A list of security group IDs. A security group must be attached to the same VPC as the subnets. For more information, see [Security in your VPC on Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/vpc-security.html) .

(string)

Shorthand Syntax:

```
SecurityGroupIds=string,string
```

JSON Syntax:

```
{
  "SecurityGroupIds": ["string", ...]
}
```

`--logging-configuration` (structure)

The Apache Airflow log types to send to CloudWatch Logs.

DagProcessingLogs -> (structure)

Publishes Airflow DAG processing logs to CloudWatch Logs.

Enabled -> (boolean)

Indicates whether to enable the Apache Airflow log type (e.g. `DagProcessingLogs` ).

LogLevel -> (string)

Defines the Apache Airflow log level (e.g. `INFO` ) to send to CloudWatch Logs.

SchedulerLogs -> (structure)

Publishes Airflow scheduler logs to CloudWatch Logs.

Enabled -> (boolean)

Indicates whether to enable the Apache Airflow log type (e.g. `DagProcessingLogs` ).

LogLevel -> (string)

Defines the Apache Airflow log level (e.g. `INFO` ) to send to CloudWatch Logs.

WebserverLogs -> (structure)

Publishes Airflow web server logs to CloudWatch Logs.

Enabled -> (boolean)

Indicates whether to enable the Apache Airflow log type (e.g. `DagProcessingLogs` ).

LogLevel -> (string)

Defines the Apache Airflow log level (e.g. `INFO` ) to send to CloudWatch Logs.

WorkerLogs -> (structure)

Publishes Airflow worker logs to CloudWatch Logs.

Enabled -> (boolean)

Indicates whether to enable the Apache Airflow log type (e.g. `DagProcessingLogs` ).

LogLevel -> (string)

Defines the Apache Airflow log level (e.g. `INFO` ) to send to CloudWatch Logs.

TaskLogs -> (structure)

Publishes Airflow task logs to CloudWatch Logs.

Enabled -> (boolean)

Indicates whether to enable the Apache Airflow log type (e.g. `DagProcessingLogs` ).

LogLevel -> (string)

Defines the Apache Airflow log level (e.g. `INFO` ) to send to CloudWatch Logs.

Shorthand Syntax:

```
DagProcessingLogs={Enabled=boolean,LogLevel=string},SchedulerLogs={Enabled=boolean,LogLevel=string},WebserverLogs={Enabled=boolean,LogLevel=string},WorkerLogs={Enabled=boolean,LogLevel=string},TaskLogs={Enabled=boolean,LogLevel=string}
```

JSON Syntax:

```
{
  "DagProcessingLogs": {
    "Enabled": true|false,
    "LogLevel": "CRITICAL"|"ERROR"|"WARNING"|"INFO"|"DEBUG"
  },
  "SchedulerLogs": {
    "Enabled": true|false,
    "LogLevel": "CRITICAL"|"ERROR"|"WARNING"|"INFO"|"DEBUG"
  },
  "WebserverLogs": {
    "Enabled": true|false,
    "LogLevel": "CRITICAL"|"ERROR"|"WARNING"|"INFO"|"DEBUG"
  },
  "WorkerLogs": {
    "Enabled": true|false,
    "LogLevel": "CRITICAL"|"ERROR"|"WARNING"|"INFO"|"DEBUG"
  },
  "TaskLogs": {
    "Enabled": true|false,
    "LogLevel": "CRITICAL"|"ERROR"|"WARNING"|"INFO"|"DEBUG"
  }
}
```

`--weekly-maintenance-window-start` (string)

The day and time of the week in Coordinated Universal Time (UTC) 24-hour standard time to start weekly maintenance updates of your environment in the following format: `DAY:HH:MM` . For example: `TUE:03:30` . You can specify a start time in 30 minute increments only.

`--webserver-access-mode` (string)

The Apache Airflow *Web server* access mode. For more information, see [Apache Airflow access modes](https://docs.aws.amazon.com/mwaa/latest/userguide/configuring-networking.html) .

Possible values:

- `PRIVATE_ONLY`
- `PUBLIC_ONLY`

`--min-workers` (integer)

The minimum number of workers that you want to run in your environment. MWAA scales the number of Apache Airflow workers up to the number you specify in the `MaxWorkers` field. When there are no more tasks running, and no more in the queue, MWAA disposes of the extra workers leaving the worker count you specify in the `MinWorkers` field. For example, `2` .

`--schedulers` (integer)

The number of Apache Airflow schedulers to run in your Amazon MWAA environment.

`--min-webservers` (integer)

The minimum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for `MaxWebservers` when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. As the transaction-per-second rate, and the network load, decrease, Amazon MWAA disposes of the additional web servers, and scales down to the number set in `MinxWebserers` .

Valid values: For environments larger than mw1.micro, accepts values from `2` to `5` . Defaults to `2` for all environment sizes except mw1.micro, which defaults to `1` .

`--max-webservers` (integer)

The maximum number of web servers that you want to run in your environment. Amazon MWAA scales the number of Apache Airflow web servers up to the number you specify for `MaxWebservers` when you interact with your Apache Airflow environment using Apache Airflow REST API, or the Apache Airflow CLI. For example, in scenarios where your workload requires network calls to the Apache Airflow REST API with a high transaction-per-second (TPS) rate, Amazon MWAA will increase the number of web servers up to the number set in `MaxWebserers` . As TPS rates decrease Amazon MWAA disposes of the additional web servers, and scales down to the number set in `MinxWebserers` .

Valid values: For environments larger than mw1.micro, accepts values from `2` to `5` . Defaults to `2` for all environment sizes except mw1.micro, which defaults to `1` .

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

Arn -> (string)

The Amazon Resource Name (ARN) of the Amazon MWAA environment. For example, `arn:aws:airflow:us-east-1:123456789012:environment/MyMWAAEnvironment` .