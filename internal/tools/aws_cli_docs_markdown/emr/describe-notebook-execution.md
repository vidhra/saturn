# describe-notebook-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-notebook-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/describe-notebook-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# describe-notebook-execution

## Description

Provides details of a notebook execution.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/DescribeNotebookExecution)

## Synopsis

```
describe-notebook-execution
--notebook-execution-id <value>
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

`--notebook-execution-id` (string)

The unique identifier of the notebook execution.

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

NotebookExecution -> (structure)

Properties of the notebook execution.

NotebookExecutionId -> (string)

The unique identifier of a notebook execution.

EditorId -> (string)

The unique identifier of the Amazon EMR Notebook that is used for the notebook execution.

ExecutionEngine -> (structure)

The execution engine, such as an Amazon EMR cluster, used to run the Amazon EMR notebook and perform the notebook execution.

Id -> (string)

The unique identifier of the execution engine. For an Amazon EMR cluster, this is the cluster ID.

Type -> (string)

The type of execution engine. A value of `EMR` specifies an Amazon EMR cluster.

MasterInstanceSecurityGroupId -> (string)

An optional unique ID of an Amazon EC2 security group to associate with the master instance of the Amazon EMR cluster for this notebook execution. For more information see [Specifying Amazon EC2 Security Groups for Amazon EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security-groups.html) in the *EMR Management Guide* .

ExecutionRoleArn -> (string)

The execution role ARN required for the notebook execution.

NotebookExecutionName -> (string)

A name for the notebook execution.

NotebookParams -> (string)

Input parameters in JSON format passed to the Amazon EMR Notebook at runtime for execution.

Status -> (string)

The status of the notebook execution.

- `START_PENDING` indicates that the cluster has received the execution request but execution has not begun.
- `STARTING` indicates that the execution is starting on the cluster.
- `RUNNING` indicates that the execution is being processed by the cluster.
- `FINISHING` indicates that execution processing is in the final stages.
- `FINISHED` indicates that the execution has completed without error.
- `FAILING` indicates that the execution is failing and will not finish successfully.
- `FAILED` indicates that the execution failed.
- `STOP_PENDING` indicates that the cluster has received a `StopNotebookExecution` request and the stop is pending.
- `STOPPING` indicates that the cluster is in the process of stopping the execution as a result of a `StopNotebookExecution` request.
- `STOPPED` indicates that the execution stopped because of a `StopNotebookExecution` request.

StartTime -> (timestamp)

The timestamp when notebook execution started.

EndTime -> (timestamp)

The timestamp when notebook execution ended.

Arn -> (string)

The Amazon Resource Name (ARN) of the notebook execution.

OutputNotebookURI -> (string)

The location of the notebook executionâs output file in Amazon S3.

LastStateChangeReason -> (string)

The reason for the latest status change of the notebook execution.

NotebookInstanceSecurityGroupId -> (string)

The unique identifier of the Amazon EC2 security group associated with the Amazon EMR Notebook instance. For more information see [Specifying Amazon EC2 Security Groups for Amazon EMR Notebooks](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-managed-notebooks-security-groups.html) in the *Amazon EMR Management Guide* .

Tags -> (list)

A list of tags associated with a notebook execution. Tags are user-defined key-value pairs that consist of a required key string with a maximum of 128 characters and an optional value string with a maximum of 256 characters.

(structure)

A key-value pair containing user-defined metadata that you can associate with an Amazon EMR resource. Tags make it easier to associate clusters in various ways, such as grouping clusters to track your Amazon EMR resource allocation costs. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html) .

Key -> (string)

A user-defined key, which is the minimum required information for a valid tag. For more information, see [Tag](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html) .

Value -> (string)

A user-defined value, which is optional in a tag. For more information, see [Tag Clusters](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-tags.html) .

NotebookS3Location -> (structure)

The Amazon S3 location that stores the notebook execution input.

Bucket -> (string)

The Amazon S3 bucket that stores the notebook execution input.

Key -> (string)

The key to the Amazon S3 location that stores the notebook execution input.

OutputNotebookS3Location -> (structure)

The Amazon S3 location for the notebook execution output.

Bucket -> (string)

The Amazon S3 bucket that stores the notebook execution output.

Key -> (string)

The key to the Amazon S3 location that stores the notebook execution output.

OutputNotebookFormat -> (string)

The output format for the notebook execution.

EnvironmentVariables -> (map)

The environment variables associated with the notebook execution.

key -> (string)

value -> (string)