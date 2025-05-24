# update-queueÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/update-queue.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/update-queue.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deadline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/index.html#cli-aws-deadline) ]

# update-queue

## Description

Updates a queue.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-12/UpdateQueue)

## Synopsis

```
update-queue
[--client-token <value>]
--farm-id <value>
--queue-id <value>
[--display-name <value>]
[--description <value>]
[--default-budget-action <value>]
[--job-attachment-settings <value>]
[--role-arn <value>]
[--job-run-as-user <value>]
[--required-file-system-location-names-to-add <value>]
[--required-file-system-location-names-to-remove <value>]
[--allowed-storage-profile-ids-to-add <value>]
[--allowed-storage-profile-ids-to-remove <value>]
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

The idempotency token to update in the queue.

`--farm-id` (string)

The farm ID to update in the queue.

`--queue-id` (string)

The queue ID to update.

`--display-name` (string)

The display name of the queue to update.

### Warning

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.

`--description` (string)

The description of the queue to update.

### Warning

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.

`--default-budget-action` (string)

The default action to take for a queue update if a budget isnât configured.

Possible values:

- `NONE`
- `STOP_SCHEDULING_AND_COMPLETE_TASKS`
- `STOP_SCHEDULING_AND_CANCEL_TASKS`

`--job-attachment-settings` (structure)

The job attachment settings to update for the queue.

s3BucketName -> (string)

The Amazon S3 bucket name.

rootPrefix -> (string)

The root prefix.

Shorthand Syntax:

```
s3BucketName=string,rootPrefix=string
```

JSON Syntax:

```
{
  "s3BucketName": "string",
  "rootPrefix": "string"
}
```

`--role-arn` (string)

The IAM role ARN thatâs used to run jobs from this queue.

`--job-run-as-user` (structure)

Update the jobs in the queue to run as a specified POSIX user.

posix -> (structure)

The user and group that the jobs in the queue run as.

user -> (string)

The name of the POSIX user.

group -> (string)

The name of the POSIX userâs group.

windows -> (structure)

Identifies a Microsoft Windows user.

user -> (string)

The user.

passwordArn -> (string)

The password ARN for the Windows user.

runAs -> (string)

Specifies whether the job should run using the queueâs system user or if the job should run using the worker agent system user.

Shorthand Syntax:

```
posix={user=string,group=string},windows={user=string,passwordArn=string},runAs=string
```

JSON Syntax:

```
{
  "posix": {
    "user": "string",
    "group": "string"
  },
  "windows": {
    "user": "string",
    "passwordArn": "string"
  },
  "runAs": "QUEUE_CONFIGURED_USER"|"WORKER_AGENT_USER"
}
```

`--required-file-system-location-names-to-add` (list)

The required file system location names to add to the queue.

(string)

Syntax:

```
"string" "string" ...
```

`--required-file-system-location-names-to-remove` (list)

The required file system location names to remove from the queue.

(string)

Syntax:

```
"string" "string" ...
```

`--allowed-storage-profile-ids-to-add` (list)

The storage profile IDs to add.

(string)

Syntax:

```
"string" "string" ...
```

`--allowed-storage-profile-ids-to-remove` (list)

The storage profile ID to remove.

(string)

Syntax:

```
"string" "string" ...
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

None