# list-jobs-by-consumable-resourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs-by-consumable-resource.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/list-jobs-by-consumable-resource.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [batch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/batch/index.html#cli-aws-batch) ]

# list-jobs-by-consumable-resource

## Description

Returns a list of Batch jobs that require a specific consumable resource.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/batch-2016-08-10/ListJobsByConsumableResource)

`list-jobs-by-consumable-resource` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `jobs`

## Synopsis

```
list-jobs-by-consumable-resource
--consumable-resource <value>
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--consumable-resource` (string)

The name or ARN of the consumable resource.

`--filters` (list)

The filters to apply to the job list query. If used, only those jobs requiring the specified consumable resource (`consumableResource` ) and that match the value of the filters are listed. The filter names and values can be:

- name: `JOB_STATUS`   values: `SUBMITTED | PENDING | RUNNABLE | STARTING | RUNNING | SUCCEEDED | FAILED`
- name: `JOB_NAME`   The values are case-insensitive matches for the job name. If a filter value ends with an asterisk (*), it matches any job name that begins with the string before the â*â.

(structure)

A filter name and value pair thatâs used to return a more specific list of results from a `ListJobs` or `ListJobsByConsumableResource` API operation.

name -> (string)

The name of the filter. Filter names are case sensitive.

values -> (list)

The filter values.

(string)

Shorthand Syntax:

```
name=string,values=string,string ...
```

JSON Syntax:

```
[
  {
    "name": "string",
    "values": ["string", ...]
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

jobs -> (list)

The list of jobs that require the specified consumable resources.

(structure)

Current information about a consumable resource required by a job.

jobArn -> (string)

The Amazon Resource Name (ARN) of the job.

jobQueueArn -> (string)

The Amazon Resource Name (ARN) of the job queue.

jobName -> (string)

The name of the job.

jobDefinitionArn -> (string)

The Amazon Resource Name (ARN) of the job definition.

shareIdentifier -> (string)

The fair-share scheduling policy identifier for the job.

jobStatus -> (string)

The status of the job. Can be one of:

- `SUBMITTED`
- `PENDING`
- `RUNNABLE`
- `STARTING`
- `RUNNING`
- `SUCCEEDED`
- `FAILED`

quantity -> (long)

The total amount of the consumable resource that is available.

statusReason -> (string)

A short, human-readable string to provide more details for the current status of the job.

startedAt -> (long)

The Unix timestamp for when the job was started. More specifically, itâs when the job transitioned from the `STARTING` state to the `RUNNING` state.

createdAt -> (long)

The Unix timestamp (in milliseconds) for when the consumable resource was created.

consumableResourceProperties -> (structure)

Contains a list of consumable resources required by the job.

consumableResourceList -> (list)

The list of consumable resources required by a job.

(structure)

Information about a consumable resource required to run a job.

consumableResource -> (string)

The name or ARN of the consumable resource.

quantity -> (long)

The quantity of the consumable resource that is needed.

nextToken -> (string)

The `nextToken` value to include in a future `ListJobsByConsumableResource` request. When the results of a `ListJobsByConsumableResource` request exceed `maxResults` , this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.