# start-job-runÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-serverless/start-job-run.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-serverless/start-job-run.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr-serverless](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-serverless/index.html#cli-aws-emr-serverless) ]

# start-job-run

## Description

Starts a job run.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/emr-serverless-2021-07-13/StartJobRun)

## Synopsis

```
start-job-run
--application-id <value>
[--client-token <value>]
--execution-role-arn <value>
[--job-driver <value>]
[--configuration-overrides <value>]
[--tags <value>]
[--execution-timeout-minutes <value>]
[--name <value>]
[--mode <value>]
[--retry-policy <value>]
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

`--application-id` (string)

The ID of the application on which to run the job.

`--client-token` (string)

The client idempotency token of the job run to start. Its value must be unique for each request.

`--execution-role-arn` (string)

The execution role ARN for the job run.

`--job-driver` (tagged union structure)

The job driver for the job run.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `sparkSubmit`, `hive`.

sparkSubmit -> (structure)

The job driver parameters specified for Spark.

entryPoint -> (string)

The entry point for the Spark submit job run.

entryPointArguments -> (list)

The arguments for the Spark submit job run.

(string)

sparkSubmitParameters -> (string)

The parameters for the Spark submit job run.

hive -> (structure)

The job driver parameters specified for Hive.

query -> (string)

The query for the Hive job run.

initQueryFile -> (string)

The query file for the Hive job run.

parameters -> (string)

The parameters for the Hive job run.

Shorthand Syntax:

```
sparkSubmit={entryPoint=string,entryPointArguments=[string,string],sparkSubmitParameters=string},hive={query=string,initQueryFile=string,parameters=string}
```

JSON Syntax:

```
{
  "sparkSubmit": {
    "entryPoint": "string",
    "entryPointArguments": ["string", ...],
    "sparkSubmitParameters": "string"
  },
  "hive": {
    "query": "string",
    "initQueryFile": "string",
    "parameters": "string"
  }
}
```

`--configuration-overrides` (structure)

The configuration overrides for the job run.

applicationConfiguration -> (list)

The override configurations for the application.

(structure)

A configuration specification to be used when provisioning an application. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.

classification -> (string)

The classification within a configuration.

properties -> (map)

A set of properties specified within a configuration classification.

key -> (string)

value -> (string)

configurations -> (list)

A list of additional configurations to apply within a configuration object.

(structure)

A configuration specification to be used when provisioning an application. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.

classification -> (string)

The classification within a configuration.

properties -> (map)

A set of properties specified within a configuration classification.

key -> (string)

value -> (string)

monitoringConfiguration -> (structure)

The override configurations for monitoring.

s3MonitoringConfiguration -> (structure)

The Amazon S3 configuration for monitoring log publishing.

logUri -> (string)

The Amazon S3 destination URI for log publishing.

encryptionKeyArn -> (string)

The KMS key ARN to encrypt the logs published to the given Amazon S3 destination.

managedPersistenceMonitoringConfiguration -> (structure)

The managed log persistence configuration for a job run.

enabled -> (boolean)

Enables managed logging and defaults to true. If set to false, managed logging will be turned off.

encryptionKeyArn -> (string)

The KMS key ARN to encrypt the logs stored in managed log persistence.

cloudWatchLoggingConfiguration -> (structure)

The Amazon CloudWatch configuration for monitoring logs. You can configure your jobs to send log information to CloudWatch.

enabled -> (boolean)

Enables CloudWatch logging.

logGroupName -> (string)

The name of the log group in Amazon CloudWatch Logs where you want to publish your logs.

logStreamNamePrefix -> (string)

Prefix for the CloudWatch log stream name.

encryptionKeyArn -> (string)

The Key Management Service (KMS) key ARN to encrypt the logs that you store in CloudWatch Logs.

logTypes -> (map)

The types of logs that you want to publish to CloudWatch. If you donât specify any log types, driver STDOUT and STDERR logs will be published to CloudWatch Logs by default. For more information including the supported worker types for Hive and Spark, see [Logging for EMR Serverless with CloudWatch](https://docs.aws.amazon.com/emr/latest/EMR-Serverless-UserGuide/logging.html#jobs-log-storage-cw) .

- **Key Valid Values** : `SPARK_DRIVER` , `SPARK_EXECUTOR` , `HIVE_DRIVER` , `TEZ_TASK`
- **Array Members Valid Values** : `STDOUT` , `STDERR` , `HIVE_LOG` , `TEZ_AM` , `SYSTEM_LOGS`

key -> (string)

Worker type for an analytics framework.

value -> (list)

(string)

Log type for a Spark/Hive job-run.

prometheusMonitoringConfiguration -> (structure)

The monitoring configuration object you can configure to send metrics to Amazon Managed Service for Prometheus for a job run.

remoteWriteUrl -> (string)

The remote write URL in the Amazon Managed Service for Prometheus workspace to send metrics to.

JSON Syntax:

```
{
  "applicationConfiguration": [
    {
      "classification": "string",
      "properties": {"string": "string"
        ...},
      "configurations": [
        {
          "classification": "string",
          "properties": {"string": "string"
            ...},
          "configurations":
        }
        ...
      ]
    }
    ...
  ],
  "monitoringConfiguration": {
    "s3MonitoringConfiguration": {
      "logUri": "string",
      "encryptionKeyArn": "string"
    },
    "managedPersistenceMonitoringConfiguration": {
      "enabled": true|false,
      "encryptionKeyArn": "string"
    },
    "cloudWatchLoggingConfiguration": {
      "enabled": true|false,
      "logGroupName": "string",
      "logStreamNamePrefix": "string",
      "encryptionKeyArn": "string",
      "logTypes": {"string": ["string", ...]
        ...}
    },
    "prometheusMonitoringConfiguration": {
      "remoteWriteUrl": "string"
    }
  }
}
```

`--tags` (map)

The tags assigned to the job run.

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

`--execution-timeout-minutes` (long)

The maximum duration for the job run to run. If the job run runs beyond this duration, it will be automatically cancelled.

`--name` (string)

The optional job run name. This doesnât have to be unique.

`--mode` (string)

The mode of the job run when it starts.

Possible values:

- `BATCH`
- `STREAMING`

`--retry-policy` (structure)

The retry policy when job run starts.

maxAttempts -> (integer)

Maximum number of attempts for the job run. This parameter is only applicable for `BATCH` mode.

maxFailedAttemptsPerHour -> (integer)

Maximum number of failed attempts per hour. This [arameter is only applicable for `STREAMING` mode.

Shorthand Syntax:

```
maxAttempts=integer,maxFailedAttemptsPerHour=integer
```

JSON Syntax:

```
{
  "maxAttempts": integer,
  "maxFailedAttemptsPerHour": integer
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

applicationId -> (string)

This output displays the application ID on which the job run was submitted.

jobRunId -> (string)

The output contains the ID of the started job run.

arn -> (string)

This output displays the ARN of the job run..