# get-workflowÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-workflow.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/get-workflow.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [omics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html#cli-aws-omics) ]

# get-workflow

## Description

Gets information about a workflow.

If a workflow is shared with you, you cannot export the workflow.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/omics-2022-11-28/GetWorkflow)

## Synopsis

```
get-workflow
--id <value>
[--type <value>]
[--export <value>]
[--workflow-owner-id <value>]
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

The workflowâs ID.

`--type` (string)

The workflowâs type.

Possible values:

- `PRIVATE`
- `READY2RUN`

`--export` (list)

The export format for the workflow.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  DEFINITION
```

`--workflow-owner-id` (string)

The ID of the workflow owner.

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

**To view a workflow**

The following `get-workflow` example gets details about a workflow with ID `1234567`.

```
aws omics get-workflow \
    --id 1234567
```

Output:

```
{
    "arn": "arn:aws:omics:us-west-2:123456789012:workflow/1234567",
    "creationTime": "2022-11-30T22:33:16.225368Z",
    "digest": "sha256:c54bxmpl742dcc26f7fa1f10e37550ddd8f251f418277c0a58e895b801ed28cf",
    "engine": "WDL",
    "id": "1234567",
    "main": "workflow-crambam.wdl",
    "name": "cram-converter",
    "parameterTemplate": {
        "ref_dict": {
            "description": "dictionary file for 'ref_fasta'"
        },
        "ref_fasta_index": {
            "description": "Index of the reference genome fasta file"
        },
        "ref_fasta": {
            "description": "Reference genome fasta file"
        },
        "input_cram": {
            "description": "The Cram file to convert to BAM"
        },
        "sample_name": {
            "description": "The name of the input sample, used to name the output BAM"
        }
    },
    "status": "ACTIVE",
    "statusMessage": "workflow-crambam.wdl\n    workflow CramToBamFlow\n        call CramToBamTask\n        call ValidateSamFile\n    task CramToBamTask\n    task ValidateSamFile\n",
    "tags": {},
    "type": "PRIVATE"
}
```

For more information, see [Omics Workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows.html) in the *Amazon Omics Developer Guide*.

## Output

arn -> (string)

The workflowâs ARN.

id -> (string)

The workflowâs ID.

status -> (string)

The workflowâs status.

type -> (string)

The workflowâs type.

name -> (string)

The workflowâs name.

description -> (string)

The workflowâs description.

engine -> (string)

The workflowâs engine.

definition -> (string)

The workflowâs definition.

main -> (string)

The path of the main definition file for the workflow.

digest -> (string)

The workflowâs digest.

parameterTemplate -> (map)

The workflowâs parameter template.

key -> (string)

value -> (structure)

A workflow parameter.

description -> (string)

The parameterâs description.

optional -> (boolean)

Whether the parameter is optional.

storageCapacity -> (integer)

The default static storage capacity (in gibibytes) for runs that use this workflow or workflow version.

creationTime -> (timestamp)

When the workflow was created.

statusMessage -> (string)

The workflowâs status message.

tags -> (map)

The workflowâs tags.

key -> (string)

value -> (string)

metadata -> (map)

Gets metadata for the workflow.

key -> (string)

value -> (string)

accelerators -> (string)

The computational accelerator specified to run the workflow.

storageType -> (string)

The default storage type for runs using this workflow.

uuid -> (string)

The universally unique identifier (UUID) value for this workflow.