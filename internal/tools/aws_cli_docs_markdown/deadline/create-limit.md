# create-limitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/create-limit.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/create-limit.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deadline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/index.html#cli-aws-deadline) ]

# create-limit

## Description

Creates a limit that manages the distribution of shared resources, such as floating licenses. A limit can throttle work assignments, help manage workloads, and track current usage. Before you use a limit, you must associate the limit with one or more queues.

You must add the `amountRequirementName` to a step in a job template to declare the limit requirement.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-12/CreateLimit)

## Synopsis

```
create-limit
[--client-token <value>]
--display-name <value>
--amount-requirement-name <value>
--max-count <value>
--farm-id <value>
[--description <value>]
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

`--client-token` (string)

The unique token which the server uses to recognize retries of the same request.

`--display-name` (string)

The display name of the limit.

### Warning

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.

`--amount-requirement-name` (string)

The value that you specify as the `name` in the `amounts` field of the `hostRequirements` in a step of a job template to declare the limit requirement.

`--max-count` (integer)

The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit wonât be scheduled until the resource is available.

The `maxCount` must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.

`--farm-id` (string)

The farm ID of the farm that contains the limit.

`--description` (string)

A description of the limit. A description helps you identify the purpose of the limit.

### Warning

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.

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

limitId -> (string)

A unique identifier for the limit. Use this identifier in other operations, such as `CreateQueueLimitAssociation` and `DeleteLimit` .