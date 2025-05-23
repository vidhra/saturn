# start-pipeline-executionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/start-pipeline-execution.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/start-pipeline-execution.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codepipeline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codepipeline/index.html#cli-aws-codepipeline) ]

# start-pipeline-execution

## Description

Starts the specified pipeline. Specifically, it begins processing the latest commit to the source location specified as part of the pipeline.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codepipeline-2015-07-09/StartPipelineExecution)

## Synopsis

```
start-pipeline-execution
--name <value>
[--variables <value>]
[--client-request-token <value>]
[--source-revisions <value>]
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

The name of the pipeline to start.

`--variables` (list)

A list that overrides pipeline variables for a pipeline execution thatâs being started. Variable names must match `[A-Za-z0-9@\-_]+` , and the values can be anything except an empty string.

(structure)

A pipeline-level variable used for a pipeline execution.

name -> (string)

The name of a pipeline-level variable.

value -> (string)

The value of a pipeline-level variable.

Shorthand Syntax:

```
name=string,value=string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "value": "string"
  }
  ...
]
```

`--client-request-token` (string)

The system-generated unique ID used to identify a unique execution request.

`--source-revisions` (list)

A list that allows you to specify, or override, the source revision for a pipeline execution thatâs being started. A source revision is the version with all the changes to your application code, or source artifact, for the pipeline execution.

(structure)

A list that allows you to specify, or override, the source revision for a pipeline execution thatâs being started. A source revision is the version with all the changes to your application code, or source artifact, for the pipeline execution.

### Note

For the `S3_OBJECT_VERSION_ID` and `S3_OBJECT_KEY` types of source revisions, either of the types can be used independently, or they can be used together to override the source with a specific ObjectKey and VersionID.

actionName -> (string)

The name of the action where the override will be applied.

revisionType -> (string)

The type of source revision, based on the source provider. For example, the revision type for the CodeCommit action provider is the commit ID.

revisionValue -> (string)

The source revision, or version of your source artifact, with the changes that you want to run in the pipeline execution.

Shorthand Syntax:

```
actionName=string,revisionType=string,revisionValue=string ...
```

JSON Syntax:

```
[
  {
    "actionName": "string",
    "revisionType": "COMMIT_ID"|"IMAGE_DIGEST"|"S3_OBJECT_VERSION_ID"|"S3_OBJECT_KEY",
    "revisionValue": "string"
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To run the latest revision through a pipeline**

This example runs the latest revision present in the source stage of a pipeline through the pipeline named âMyFirstPipelineâ.

Command:

```
aws codepipeline start-pipeline-execution --name MyFirstPipeline
```

Output:

```
{
  "pipelineExecutionId": "3137f7cb-7cf7-EXAMPLE"
}
```

## Output

pipelineExecutionId -> (string)

The unique system-generated ID of the pipeline execution that was started.