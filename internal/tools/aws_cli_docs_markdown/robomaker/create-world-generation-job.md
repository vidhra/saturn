# create-world-generation-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-world-generation-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/create-world-generation-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [robomaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/robomaker/index.html#cli-aws-robomaker) ]

# create-world-generation-job

## Description

### Warning

End of support notice: On September 10, 2025, Amazon Web Services will discontinue support for Amazon Web Services RoboMaker. After September 10, 2025, you will no longer be able to access the Amazon Web Services RoboMaker console or Amazon Web Services RoboMaker resources. For more information on transitioning to Batch to help run containerized simulations, visit [https://aws.amazon.com/blogs/hpc/run-simulations-using-multiple-containers-in-a-single-aws-batch-job/](https://aws.amazon.com/blogs/hpc/run-simulations-using-multiple-containers-in-a-single-aws-batch-job/) .

Creates worlds using the specified template.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/robomaker-2018-06-29/CreateWorldGenerationJob)

## Synopsis

```
create-world-generation-job
[--client-request-token <value>]
--template <value>
--world-count <value>
[--tags <value>]
[--world-tags <value>]
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

`--client-request-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

`--template` (string)

The Amazon Resource Name (arn) of the world template describing the worlds you want to create.

`--world-count` (structure)

Information about the world count.

floorplanCount -> (integer)

The number of unique floorplans.

interiorCountPerFloorplan -> (integer)

The number of unique interiors per floorplan.

Shorthand Syntax:

```
floorplanCount=integer,interiorCountPerFloorplan=integer
```

JSON Syntax:

```
{
  "floorplanCount": integer,
  "interiorCountPerFloorplan": integer
}
```

`--tags` (map)

A map that contains tag keys and tag values that are attached to the world generator job.

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

`--world-tags` (map)

A map that contains tag keys and tag values that are attached to the generated worlds.

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

arn -> (string)

The Amazon Resource Name (ARN) of the world generator job.

status -> (string)

The status of the world generator job.

Pending

The world generator job request is pending.

Running

The world generator job is running.

Completed

The world generator job completed.

Failed

The world generator job failed. See `failureCode` for more information.

PartialFailed

Some worlds did not generate.

Canceled

The world generator job was cancelled.

Canceling

The world generator job is being cancelled.

createdAt -> (timestamp)

The time, in milliseconds since the epoch, when the world generator job was created.

failureCode -> (string)

The failure code of the world generator job if it failed:

InternalServiceError

Internal service error.

LimitExceeded

The requested resource exceeds the maximum number allowed, or the number of concurrent stream requests exceeds the maximum number allowed.

ResourceNotFound

The specified resource could not be found.

RequestThrottled

The request was throttled.

InvalidInput

An input parameter in the request is not valid.

clientRequestToken -> (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.

template -> (string)

The Amazon Resource Name (arn) of the world template.

worldCount -> (structure)

Information about the world count.

floorplanCount -> (integer)

The number of unique floorplans.

interiorCountPerFloorplan -> (integer)

The number of unique interiors per floorplan.

tags -> (map)

A map that contains tag keys and tag values that are attached to the world generator job.

key -> (string)

value -> (string)

worldTags -> (map)

A map that contains tag keys and tag values that are attached to the generated worlds.

key -> (string)

value -> (string)