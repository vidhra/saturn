# get-runÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-run.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-run.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [omics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html#cli-aws-omics) ]

# get-run

## Description

Gets information about a workflow run.

If a workflow is shared with you, you cannot export information about the run.

Amazon Web Services HealthOmics stores a fixed number of runs that are available to the console and API. If GetRun doesnât return the requested run, you can find run logs for all runs in the CloudWatch logs. For more information about viewing the run logs, see [CloudWatch logs](https://docs.aws.amazon.com/omics/latest/dev/cloudwatch-logs.html) in the *in the Amazon Web Services HealthOmics User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/omics-2022-11-28/GetRun)

`get-run` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
get-run
--id <value>
[--export <value>]
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

`--id` (string)

The runâs ID.

`--export` (list)

The runâs export format.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  DEFINITION
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

**To view a workflow run**

The following `get-run` example gets details about a workflow run.

```
aws omics get-run \
    --id 1234567
```

Output:

```
{
    "arn": "arn:aws:omics:us-west-2:123456789012:run/1234567",
    "creationTime": "2022-11-30T22:58:22.615865Z",
    "digest": "sha256:c54bxmpl742dcc26f7fa1f10e37550ddd8f251f418277c0a58e895b801ed28cf",
    "id": "1234567",
    "name": "cram-to-bam",
    "outputUri": "s3://omics-artifacts-01d6xmpl4e72dd32/workflow-output/",
    "parameters": {
        "ref_dict": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.dict",
        "ref_fasta_index": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta.fai",
        "ref_fasta": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta",
        "sample_name": "NA12878",
        "input_cram": "s3://omics-artifacts-01d6xmpl4e72dd32/NA12878.cram"
    },
    "resourceDigests": {
        "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta.fai": "etag:f76371b113734a56cde236bc0372de0a",
        "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.dict": "etag:3884c62eb0e53fa92459ed9bff133ae6",
        "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta": "etag:e307d81c605fb91b7720a08f00276842-388",
        "s3://omics-artifacts-01d6xmpl4e72dd32/NA12878.cram": "etag:a9f52976381286c6143b5cc681671ec6"
    },
    "roleArn": "arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ",
    "startedBy": "arn:aws:iam::123456789012:user/laptop-2020",
    "status": "STARTING",
    "tags": {},
    "workflowId": "1234567",
    "workflowType": "PRIVATE"
}
```

For more information, see [Omics Workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows.html) in the *Amazon Omics Developer Guide*.

## Output

arn -> (string)

The runâs ARN.

id -> (string)

The runâs ID.

cacheId -> (string)

The run cache associated with the run.

cacheBehavior -> (string)

The run cache behavior for the run.

engineVersion -> (string)

The actual Nextflow engine version that Amazon Web Services HealthOmics used for the run. The other workflow definition languages donât provide a value for this field.

status -> (string)

The runâs status.

workflowId -> (string)

The runâs workflow ID.

workflowType -> (string)

The runâs workflow type.

runId -> (string)

The runâs ID.

roleArn -> (string)

The runâs service role ARN.

name -> (string)

The runâs name.

runGroupId -> (string)

The runâs group ID.

priority -> (integer)

The runâs priority.

definition -> (string)

The runâs definition.

digest -> (string)

The runâs digest.

parameters -> (document)

The runâs parameters.

storageCapacity -> (integer)

The runâs storage capacity in gibibytes. For dynamic storage, after the run has completed, this value is the maximum amount of storage used during the run.

outputUri -> (string)

The runâs output URI.

logLevel -> (string)

The runâs log level.

resourceDigests -> (map)

The runâs resource digests.

key -> (string)

value -> (string)

startedBy -> (string)

Who started the run.

creationTime -> (timestamp)

When the run was created.

startTime -> (timestamp)

When the run started.

stopTime -> (timestamp)

The runâs stop time.

statusMessage -> (string)

The runâs status message.

tags -> (map)

The runâs tags.

key -> (string)

value -> (string)

accelerators -> (string)

The computational accelerator used to run the workflow.

retentionMode -> (string)

The runâs retention mode.

failureReason -> (string)

The reason a run has failed.

logLocation -> (structure)

The location of the run log.

engineLogStream -> (string)

The log stream ARN for the engine log.

runLogStream -> (string)

The log stream ARN for the run log.

uuid -> (string)

The universally unique identifier for a run.

runOutputUri -> (string)

The destination for workflow outputs.

storageType -> (string)

The runâs storage type.

workflowOwnerId -> (string)

The ID of the workflow owner.

workflowVersionName -> (string)

The workflow version name.

workflowUuid -> (string)

The universally unique identifier (UUID) value for the workflow.