# start-runÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/start-run.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/start-run.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [omics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html#cli-aws-omics) ]

# start-run

## Description

Starts a new run or duplicates an existing run.

For a new run, specify a unique `requestId` , the `workflowId` , and a role ARN. If youâre using static run storage (the default), specify the required `storageCapacity` .

You duplicate a run by specifing a unique `requestId` , the `runID` of the run to duplicate, and a role ARN.

For more information about the optional parameters in the StartRun request, see [Starting a run](https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html) in the *Amazon Web Services HealthOmics User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/omics-2022-11-28/StartRun)

`start-run` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
start-run
[--workflow-id <value>]
[--workflow-type <value>]
[--run-id <value>]
--role-arn <value>
[--name <value>]
[--cache-id <value>]
[--cache-behavior <value>]
[--run-group-id <value>]
[--priority <value>]
[--parameters <value>]
[--storage-capacity <value>]
[--output-uri <value>]
[--log-level <value>]
[--tags <value>]
[--request-id <value>]
[--retention-mode <value>]
[--storage-type <value>]
[--workflow-owner-id <value>]
[--workflow-version-name <value>]
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

`--workflow-id` (string)

The runâs workflow ID.

`--workflow-type` (string)

The runâs workflow type.

Possible values:

- `PRIVATE`
- `READY2RUN`

`--run-id` (string)

The ID of a run to duplicate.

`--role-arn` (string)

A service role for the run.

`--name` (string)

A name for the run.

`--cache-id` (string)

Identifier of the cache associated with this run. If you donât specify a cache ID, no task outputs are cached for this run.

`--cache-behavior` (string)

The cache behavior for the run. You specify this value if you want to override the default behavior for the cache. You had set the default value when you created the cache. For more information, see [Run cache behavior](https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior) in the Amazon Web Services HealthOmics User Guide.

Possible values:

- `CACHE_ON_FAILURE`
- `CACHE_ALWAYS`

`--run-group-id` (string)

The runâs group ID.

`--priority` (integer)

A priority for the run.

`--parameters` (document)

Parameters for the run.

JSON Syntax:

```
{...}
```

`--storage-capacity` (integer)

The static storage capacity (in gibibytes) for this run. This field is not required if the storage type is dynamic (the system ignores any value that you enter).

`--output-uri` (string)

An output URI for the run.

`--log-level` (string)

A log level for the run.

Possible values:

- `OFF`
- `FATAL`
- `ERROR`
- `ALL`

`--tags` (map)

Tags for the run.

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

`--request-id` (string)

To ensure that requests donât run multiple times, specify a unique ID for each request.

`--retention-mode` (string)

The retention mode for the run. The default value is RETAIN.

Amazon Web Services HealthOmics stores a fixed number of runs that are available to the console and API. In the default mode (RETAIN), you need to remove runs manually when the number of run exceeds the maximum. If you set the retention mode to `REMOVE` , Amazon Web Services HealthOmics automatically removes runs (that have mode set to REMOVE) when the number of run exceeds the maximum. All run logs are available in CloudWatch logs, if you need information about a run that is no longer available to the API.

For more information about retention mode, see [Specifying run retention mode](https://docs.aws.amazon.com/omics/latest/dev/starting-a-run.html) in the *Amazon Web Services HealthOmics User Guide* .

Possible values:

- `RETAIN`
- `REMOVE`

`--storage-type` (string)

The storage type for the run. By default, the run uses STATIC storage type, which allocates a fixed amount of storage. If you set the storage type to DYNAMIC, Amazon Web Services HealthOmics dynamically scales the storage up or down, based on file system utilization. For more information about static and dynamic storage, see [Running workflows](https://docs.aws.amazon.com/omics/latest/dev/Using-workflows.html) in the *Amazon Web Services HealthOmics User Guide* .

Possible values:

- `STATIC`
- `DYNAMIC`

`--workflow-owner-id` (string)

The ID of the workflow owner.

`--workflow-version-name` (string)

The name of the workflow version.

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

**To run a workflow**

The following `start-run` example runs a workflow with ID `1234567`.

```
aws omics start-run \
    --workflow-id 1234567 \
    --role-arn arn:aws:iam::123456789012:role/omics-service-role-serviceRole-W8O1XMPL7QZ \
    --name 'cram-to-bam' \
    --output-uri s3://omics-artifacts-01d6xmpl4e72dd32/workflow-output/ \
    --run-group-id 1234567 \
    --priority 1 \
    --storage-capacity 10 \
    --log-level ALL \
    --parameters file://workflow-inputs.json
```

workflow-inputs.json is a JSON document with the following content.

```
{
    "sample_name": "NA12878",
    "input_cram": "s3://omics-artifacts-01d6xmpl4e72dd32/NA12878.cram",
    "ref_dict": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.dict",
    "ref_fasta": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta",
    "ref_fasta_index": "omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.fasta.fai"
}
```

Output:

```
{
    "arn": "arn:aws:omics:us-west-2:123456789012:run/1234567",
    "id": "1234567",
    "status": "PENDING",
    "tags": {}
}
```

For more information, see [Omics Workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows.html) in the *Amazon Omics Developer Guide*.

**To load source files from Amazon Omics**

You can also load source files from Amazon Omics storage, by using service-specific URIs. The following example workflow-inputs.json file uses Amazon Omics URIs for read set and reference genome sources.

```
{
    "sample_name": "NA12878",
    "input_cram": "omics://123456789012.storage.us-west-2.amazonaws.com/1234567890/readSet/1234567890/source1",
    "ref_dict": "s3://omics-artifacts-01d6xmpl4e72dd32/Homo_sapiens_assembly38.dict",
    "ref_fasta": "omics://123456789012.storage.us-west-2.amazonaws.com/1234567890/reference/1234567890",
    "ref_fasta_index": "omics://123456789012.storage.us-west-2.amazonaws.com/1234567890/reference/1234567890/index"
}
```

For more information, see [Omics Workflows](https://docs.aws.amazon.com/omics/latest/dev/workflows.html) in the *Amazon Omics Developer Guide*.

## Output

arn -> (string)

Unique resource identifier for the run.

id -> (string)

The runâs ID.

status -> (string)

The runâs status.

tags -> (map)

The runâs tags.

key -> (string)

value -> (string)

uuid -> (string)

The universally unique identifier for a run.

runOutputUri -> (string)

The destination for workflow outputs.