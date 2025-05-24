# start-job-runÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/start-job-run.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/start-job-run.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr-containers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/index.html#cli-aws-emr-containers) ]

# start-job-run

## Description

Starts a job run. A job run is a unit of work, such as a Spark jar, PySpark script, or SparkSQL query, that you submit to Amazon EMR on EKS.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/emr-containers-2020-10-01/StartJobRun)

## Synopsis

```
start-job-run
[--name <value>]
--virtual-cluster-id <value>
[--client-token <value>]
[--execution-role-arn <value>]
[--release-label <value>]
[--job-driver <value>]
[--configuration-overrides <value>]
[--tags <value>]
[--job-template-id <value>]
[--job-template-parameters <value>]
[--retry-policy-configuration <value>]
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

The name of the job run.

`--virtual-cluster-id` (string)

The virtual cluster ID for which the job run request is submitted.

`--client-token` (string)

The client idempotency token of the job run request.

`--execution-role-arn` (string)

The execution role ARN for the job run.

`--release-label` (string)

The Amazon EMR release version to use for the job run.

`--job-driver` (structure)

The job driver for the job run.

sparkSubmitJobDriver -> (structure)

The job driver parameters specified for spark submit.

entryPoint -> (string)

The entry point of job application.

entryPointArguments -> (list)

The arguments for job application.

(string)

sparkSubmitParameters -> (string)

The Spark submit parameters that are used for job runs.

sparkSqlJobDriver -> (structure)

The job driver for job type.

entryPoint -> (string)

The SQL file to be executed.

sparkSqlParameters -> (string)

The Spark parameters to be included in the Spark SQL command.

Shorthand Syntax:

```
sparkSubmitJobDriver={entryPoint=string,entryPointArguments=[string,string],sparkSubmitParameters=string},sparkSqlJobDriver={entryPoint=string,sparkSqlParameters=string}
```

JSON Syntax:

```
{
  "sparkSubmitJobDriver": {
    "entryPoint": "string",
    "entryPointArguments": ["string", ...],
    "sparkSubmitParameters": "string"
  },
  "sparkSqlJobDriver": {
    "entryPoint": "string",
    "sparkSqlParameters": "string"
  }
}
```

`--configuration-overrides` (structure)

The configuration overrides for the job run.

applicationConfiguration -> (list)

The configurations for the application running by the job run.

(structure)

A configuration specification to be used when provisioning virtual clusters, which can include configurations for applications and software bundled with Amazon EMR on EKS. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.

classification -> (string)

The classification within a configuration.

properties -> (map)

A set of properties specified within a configuration classification.

key -> (string)

value -> (string)

configurations -> (list)

A list of additional configurations to apply within a configuration object.

(structure)

A configuration specification to be used when provisioning virtual clusters, which can include configurations for applications and software bundled with Amazon EMR on EKS. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file.

classification -> (string)

The classification within a configuration.

properties -> (map)

A set of properties specified within a configuration classification.

key -> (string)

value -> (string)

monitoringConfiguration -> (structure)

The configurations for monitoring.

managedLogs -> (structure)

The entity that controls configuration for managed logs.

allowAWSToRetainLogs -> (string)

Determines whether Amazon Web Services can retain logs.

encryptionKeyArn -> (string)

The Amazon resource name (ARN) of the encryption key for logs.

persistentAppUI -> (string)

Monitoring configurations for the persistent application UI.

cloudWatchMonitoringConfiguration -> (structure)

Monitoring configurations for CloudWatch.

logGroupName -> (string)

The name of the log group for log publishing.

logStreamNamePrefix -> (string)

The specified name prefix for log streams.

s3MonitoringConfiguration -> (structure)

Amazon S3 configuration for monitoring log publishing.

logUri -> (string)

Amazon S3 destination URI for log publishing.

containerLogRotationConfiguration -> (structure)

Enable or disable container log rotation.

rotationSize -> (string)

The file size at which to rotate logs. Minimum of 2KB, Maximum of 2GB.

maxFilesToKeep -> (integer)

The number of files to keep in container after rotation.

Shorthand Syntax:

```
applicationConfiguration=[{classification=string,properties={KeyName1=string,KeyName2=string},( ... recursive ... )},{classification=string,properties={KeyName1=string,KeyName2=string},( ... recursive ... )}],monitoringConfiguration={managedLogs={allowAWSToRetainLogs=string,encryptionKeyArn=string},persistentAppUI=string,cloudWatchMonitoringConfiguration={logGroupName=string,logStreamNamePrefix=string},s3MonitoringConfiguration={logUri=string},containerLogRotationConfiguration={rotationSize=string,maxFilesToKeep=integer}}
```

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
    "managedLogs": {
      "allowAWSToRetainLogs": "ENABLED"|"DISABLED",
      "encryptionKeyArn": "string"
    },
    "persistentAppUI": "ENABLED"|"DISABLED",
    "cloudWatchMonitoringConfiguration": {
      "logGroupName": "string",
      "logStreamNamePrefix": "string"
    },
    "s3MonitoringConfiguration": {
      "logUri": "string"
    },
    "containerLogRotationConfiguration": {
      "rotationSize": "string",
      "maxFilesToKeep": integer
    }
  }
}
```

`--tags` (map)

The tags assigned to job runs.

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

`--job-template-id` (string)

The job template ID to be used to start the job run.

`--job-template-parameters` (map)

The values of job template parameters to start a job run.

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

`--retry-policy-configuration` (structure)

The retry policy configuration for the job run.

maxAttempts -> (integer)

The maximum number of attempts on the jobâs driver.

Shorthand Syntax:

```
maxAttempts=integer
```

JSON Syntax:

```
{
  "maxAttempts": integer
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

id -> (string)

This output displays the started job run ID.

name -> (string)

This output displays the name of the started job run.

arn -> (string)

This output lists the ARN of job run.

virtualClusterId -> (string)

This output displays the virtual cluster ID for which the job run was submitted.