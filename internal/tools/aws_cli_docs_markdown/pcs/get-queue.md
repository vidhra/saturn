# get-queueÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/get-queue.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/get-queue.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pcs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/index.html#cli-aws-pcs) ]

# get-queue

## Description

Returns detailed information about a queue. The information includes the compute node groups that the queue uses to schedule jobs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pcs-2023-02-10/GetQueue)

## Synopsis

```
get-queue
--cluster-identifier <value>
--queue-identifier <value>
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

`--cluster-identifier` (string)

The name or ID of the cluster of the queue.

`--queue-identifier` (string)

The name or ID of the queue.

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

queue -> (structure)

A queue resource.

name -> (string)

The name that identifies the queue.

id -> (string)

The generated unique ID of the queue.

arn -> (string)

The unique Amazon Resource Name (ARN) of the queue.

clusterId -> (string)

The ID of the cluster of the queue.

createdAt -> (timestamp)

The date and time the resource was created.

modifiedAt -> (timestamp)

The date and time the resource was modified.

status -> (string)

The provisioning status of the queue.

### Note

The provisioning status doesnât indicate the overall health of the queue.

computeNodeGroupConfigurations -> (list)

The list of compute node group configurations associated with the queue. Queues assign jobs to associated compute node groups.

(structure)

The compute node group configuration for a queue.

computeNodeGroupId -> (string)

The compute node group ID for the compute node group configuration.

errorInfo -> (list)

The list of errors that occurred during queue provisioning.

(structure)

An error that occurred during resource creation.

code -> (string)

The short-form error code.

message -> (string)

The detailed error information.