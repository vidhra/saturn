# list-job-templatesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/list-job-templates.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/list-job-templates.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr-containers](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr-containers/index.html#cli-aws-emr-containers) ]

# list-job-templates

## Description

Lists job templates based on a set of parameters. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/emr-containers-2020-10-01/ListJobTemplates)

`list-job-templates` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `templates`

## Synopsis

```
list-job-templates
[--created-after <value>]
[--created-before <value>]
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

`--created-after` (timestamp)

The date and time after which the job templates were created.

`--created-before` (timestamp)

The date and time before which the job templates were created.

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

templates -> (list)

This output lists information about the specified job templates.

(structure)

This entity describes a job template. Job template stores values of StartJobRun API request in a template and can be used to start a job run. Job template allows two use cases: avoid repeating recurring StartJobRun API request values, enforcing certain values in StartJobRun API request.

name -> (string)

The name of the job template.

id -> (string)

The ID of the job template.

arn -> (string)

The ARN of the job template.

createdAt -> (timestamp)

The date and time when the job template was created.

createdBy -> (string)

The user who created the job template.

tags -> (map)

The tags assigned to the job template.

key -> (string)

value -> (string)

jobTemplateData -> (structure)

The job template data which holds values of StartJobRun API request.

executionRoleArn -> (string)

The execution role ARN of the job run.

releaseLabel -> (string)

The release version of Amazon EMR.

configurationOverrides -> (structure)

The configuration settings that are used to override defaults configuration.

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

jobDriver -> (structure)

Specify the driver that the job runs on. Exactly one of the two available job drivers is required, either sparkSqlJobDriver or sparkSubmitJobDriver.

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

parameterConfiguration -> (map)

The configuration of parameters existing in the job template.

key -> (string)

value -> (structure)

The configuration of a job template parameter.

type -> (string)

The type of the job template parameter. Allowed values are: âSTRINGâ, âNUMBERâ.

defaultValue -> (string)

The default value for the job template parameter.

jobTags -> (map)

The tags assigned to jobs started using the job template.

key -> (string)

value -> (string)

kmsKeyArn -> (string)

The KMS key ARN used to encrypt the job template.

decryptionError -> (string)

The error message in case the decryption of job template fails.

nextToken -> (string)

This output displays the token for the next set of job templates.