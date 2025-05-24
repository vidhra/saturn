# get-limitÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/get-limit.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/get-limit.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deadline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/index.html#cli-aws-deadline) ]

# get-limit

## Description

Gets information about a specific limit.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-12/GetLimit)

## Synopsis

```
get-limit
--farm-id <value>
--limit-id <value>
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

`--farm-id` (string)

The unique identifier of the farm that contains the limit.

`--limit-id` (string)

The unique identifier of the limit to return.

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

displayName -> (string)

The display name of the limit.

### Warning

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.

amountRequirementName -> (string)

The value that you specify as the `name` in the `amounts` field of the `hostRequirements` in a step of a job template to declare the limit requirement.

maxCount -> (integer)

The maximum number of resources constrained by this limit. When all of the resources are in use, steps that require the limit wonât be scheduled until the resource is available.

The `maxValue` must not be 0. If the value is -1, there is no restriction on the number of resources that can be acquired for this limit.

createdAt -> (timestamp)

The Unix timestamp of the date and time that the limit was created.

createdBy -> (string)

The user identifier of the person that created the limit.

updatedAt -> (timestamp)

The Unix timestamp of the date and time that the limit was last updated.

updatedBy -> (string)

The user identifier of the person that last updated the limit.

farmId -> (string)

The unique identifier of the farm that contains the limit.

limitId -> (string)

The unique identifier of the limit.

currentCount -> (integer)

The number of resources from the limit that are being used by jobs. The result is delayed and may not be the count at the time that you called the operation.

description -> (string)

The description of the limit that helps identify what the limit is used for.

### Warning

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.