# update-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/update-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/update-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deadline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/index.html#cli-aws-deadline) ]

# update-job

## Description

Updates a job.

When you change the status of the job to `ARCHIVED` , the job canât be scheduled or archived.

### Warning

An archived jobs and its steps and tasks are deleted after 120 days. The job canât be recovered.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-12/UpdateJob)

## Synopsis

```
update-job
[--client-token <value>]
[--target-task-run-status <value>]
[--priority <value>]
[--max-failed-tasks-count <value>]
[--max-retries-per-task <value>]
[--lifecycle-status <value>]
[--max-worker-count <value>]
--farm-id <value>
--queue-id <value>
--job-id <value>
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

`--target-task-run-status` (string)

The task status to update the jobâs tasks to.

Possible values:

- `READY`
- `FAILED`
- `SUCCEEDED`
- `CANCELED`
- `SUSPENDED`
- `PENDING`

`--priority` (integer)

The job priority to update.

`--max-failed-tasks-count` (integer)

The number of task failures before the job stops running and is marked as `FAILED` .

`--max-retries-per-task` (integer)

The maximum number of retries for a job.

`--lifecycle-status` (string)

The status of a job in its lifecycle. When you change the status of the job to `ARCHIVED` , the job canât be scheduled or archived.

### Warning

An archived jobs and its steps and tasks are deleted after 120 days. The job canât be recovered.

Possible values:

- `ARCHIVED`

`--max-worker-count` (integer)

The maximum number of worker hosts that can concurrently process a job. When the `maxWorkerCount` is reached, no more workers will be assigned to process the job, even if the fleets assigned to the jobâs queue has available workers.

You canât set the `maxWorkerCount` to 0. If you set it to -1, there is no maximum number of workers.

If you donât specify the `maxWorkerCount` , the default is -1.

The maximum number of workers that can process tasks in the job.

`--farm-id` (string)

The farm ID of the job to update.

`--queue-id` (string)

The queue ID of the job to update.

`--job-id` (string)

The job ID to update.

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