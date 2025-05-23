# create-run-cacheÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-run-cache.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/create-run-cache.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [omics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html#cli-aws-omics) ]

# create-run-cache

## Description

You can create a run cache to save the task outputs from completed tasks in a run for a private workflow. Subsequent runs use the task outputs from the cache, rather than computing the task outputs again. You specify an Amazon S3 location where Amazon Web Services HealthOmics saves the cached data. This data must be immediately accessible (not in an archived state).

For more information, see [Creating a run cache](https://docs.aws.amazon.com/omics/latest/dev/workflow-cache-create.html) in the Amazon Web Services HealthOmics User Guide.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/omics-2022-11-28/CreateRunCache)

## Synopsis

```
create-run-cache
[--cache-behavior <value>]
--cache-s3-location <value>
[--description <value>]
[--name <value>]
[--request-id <value>]
[--tags <value>]
[--cache-bucket-owner-id <value>]
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

`--cache-behavior` (string)

Default cache behavior for runs that use this cache. Supported values are:

`CACHE_ON_FAILURE` : Caches task outputs from completed tasks for runs that fail. This setting is useful if youâre debugging a workflow that fails after several tasks completed successfully. The subsequent run uses the cache outputs for previously-completed tasks if the task definition, inputs, and container in ECR are identical to the prior run.

`CACHE_ALWAYS` : Caches task outputs from completed tasks for all runs. This setting is useful in development mode, but do not use it in a production setting.

If you donât specify a value, the default behavior is CACHE_ON_FAILURE. When you start a run that uses this cache, you can override the default cache behavior.

For more information, see [Run cache behavior](https://docs.aws.amazon.com/omics/latest/dev/how-run-cache.html#run-cache-behavior) in the Amazon Web Services HealthOmics User Guide.

Possible values:

- `CACHE_ON_FAILURE`
- `CACHE_ALWAYS`

`--cache-s3-location` (string)

Specify the S3 location for storing the cached task outputs. This data must be immediately accessible (not in an archived state).

`--description` (string)

Enter a description of the run cache.

`--name` (string)

Enter a user-friendly name for the run cache.

`--request-id` (string)

A unique request token, to ensure idempotency. If you donât specify a token, Amazon Web Services HealthOmics automatically generates a universally unique identifier (UUID) for the request.

`--tags` (map)

Specify one or more tags to associate with this run cache.

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

`--cache-bucket-owner-id` (string)

The Amazon Web Services account ID of the expected owner of the S3 bucket for the run cache. If not provided, your account ID is set as the owner of the bucket.

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

Unique resource identifier for the run cache.

id -> (string)

Identifier for the run cache.

status -> (string)

Run cache status.

tags -> (map)

The tags associated with this run cache.

key -> (string)

value -> (string)