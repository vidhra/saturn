# start-batch-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/m2/start-batch-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/m2/start-batch-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [m2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/m2/index.html#cli-aws-m2) ]

# start-batch-job

## Description

Starts a batch job and returns the unique identifier of this execution of the batch job. The associated application must be running in order to start the batch job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/m2-2021-04-28/StartBatchJob)

## Synopsis

```
start-batch-job
--application-id <value>
[--auth-secrets-manager-arn <value>]
--batch-job-identifier <value>
[--job-params <value>]
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

The unique identifier of the application associated with this batch job.

`--auth-secrets-manager-arn` (string)

The Amazon Web Services Secrets Manager containing userâs credentials for authentication and authorization for Start Batch Job execution operation.

`--batch-job-identifier` (tagged union structure)

The unique identifier of the batch job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fileBatchJobIdentifier`, `restartBatchJobIdentifier`, `s3BatchJobIdentifier`, `scriptBatchJobIdentifier`.

fileBatchJobIdentifier -> (structure)

Specifies a file associated with a specific batch job.

fileName -> (string)

The file name for the batch job identifier.

folderPath -> (string)

The relative path to the file name for the batch job identifier.

restartBatchJobIdentifier -> (structure)

Specifies the required information for restart, including `executionId` and `JobStepRestartMarker` .

executionId -> (string)

The `executionId` from the `StartBatchJob` response when the job ran for the first time.

jobStepRestartMarker -> (structure)

The step/procedure step information for a restart batch job operation.

fromProcStep -> (string)

The procedure step name that a batch job was restarted from.

fromStep -> (string)

The step name that a batch job was restarted from.

skip -> (boolean)

The step-level checkpoint timestamp (creation or last modification) for an Amazon Web Services Blu Age application batch job.

stepCheckpoint -> (integer)

Skip selected step and issue a restart from immediate successor step for an Amazon Web Services Blu Age application batch job.

toProcStep -> (string)

The procedure step name that a batch job was restarted to.

toStep -> (string)

The step name that a batch job was restarted to.

s3BatchJobIdentifier -> (structure)

Specifies an Amazon S3 location that identifies the batch jobs that you want to run. Use this identifier to run ad hoc batch jobs.

bucket -> (string)

The Amazon S3 bucket that contains the batch job definitions.

identifier -> (tagged union structure)

Identifies the batch job definition. This identifier can also point to any batch job definition that already exists in the application or to one of the batch job definitions within the directory that is specified in `keyPrefix` .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `fileName`, `scriptName`.

fileName -> (string)

The name of the file that contains the batch job definition.

scriptName -> (string)

The name of the script that contains the batch job definition.

keyPrefix -> (string)

The key prefix that specifies the path to the folder in the S3 bucket that has the batch job definitions.

scriptBatchJobIdentifier -> (structure)

A batch job identifier in which the batch job to run is identified by the script name.

scriptName -> (string)

The name of the script containing the batch job definition.

Shorthand Syntax:

```
fileBatchJobIdentifier={fileName=string,folderPath=string},restartBatchJobIdentifier={executionId=string,jobStepRestartMarker={fromProcStep=string,fromStep=string,skip=boolean,stepCheckpoint=integer,toProcStep=string,toStep=string}},s3BatchJobIdentifier={bucket=string,identifier={fileName=string,scriptName=string},keyPrefix=string},scriptBatchJobIdentifier={scriptName=string}
```

JSON Syntax:

```
{
  "fileBatchJobIdentifier": {
    "fileName": "string",
    "folderPath": "string"
  },
  "restartBatchJobIdentifier": {
    "executionId": "string",
    "jobStepRestartMarker": {
      "fromProcStep": "string",
      "fromStep": "string",
      "skip": true|false,
      "stepCheckpoint": integer,
      "toProcStep": "string",
      "toStep": "string"
    }
  },
  "s3BatchJobIdentifier": {
    "bucket": "string",
    "identifier": {
      "fileName": "string",
      "scriptName": "string"
    },
    "keyPrefix": "string"
  },
  "scriptBatchJobIdentifier": {
    "scriptName": "string"
  }
}
```

`--job-params` (map)

The collection of batch job parameters. For details about limits for keys and values, see [Coding variables in JCL](https://www.ibm.com/docs/en/workload-automation/9.3.0?topic=zos-coding-variables-in-jcl) .

key -> (string)

See [https://www.ibm.com/docs/en/workload-automation/9.3.0?topic=zos-coding-variables-in-jcl](https://www.ibm.com/docs/en/workload-automation/9.3.0?topic=zos-coding-variables-in-jcl) to get details about limits for both keys and values: 8 for keys (variable names), 44 for values (variable values) In addition, keys will be only alphabetic characters and digits, without any space or special characters (dash, underscore, etc â¦)

For BluAge Engine: There is no limit in length of keys and values. Additional validation may be applied in code, per engine. Parameter key: the first character must be alphabetic. Can be of up to 32 alphanumeric characters.

value -> (string)

Parameter value can be of up to 1024 alphanumeric characters.

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

executionId -> (string)

The unique identifier of this execution of the batch job.