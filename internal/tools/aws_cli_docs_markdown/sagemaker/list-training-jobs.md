# list-training-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-training-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-training-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# list-training-jobs

## Description

Lists training jobs.

### Note

When `StatusEquals` and `MaxResults` are set at the same time, the `MaxResults` number of training jobs are first retrieved ignoring the `StatusEquals` parameter and then they are filtered by the `StatusEquals` parameter, which is returned as a response.

For example, if `ListTrainingJobs` is invoked with the following parameters:

`{ ... MaxResults: 100, StatusEquals: InProgress ... }`

First, 100 trainings jobs with any status, including those other than `InProgress` , are selected (sorted according to the creation time, from the most current to the oldest). Next, those with a status of `InProgress` are returned.

You can quickly test the API using the following Amazon Web Services CLI code.

`aws sagemaker list-training-jobs --max-results 100 --status-equals InProgress`

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListTrainingJobs)

`list-training-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `TrainingJobSummaries`

## Synopsis

```
list-training-jobs
[--creation-time-after <value>]
[--creation-time-before <value>]
[--last-modified-time-after <value>]
[--last-modified-time-before <value>]
[--name-contains <value>]
[--status-equals <value>]
[--sort-by <value>]
[--sort-order <value>]
[--warm-pool-status-equals <value>]
[--training-plan-arn-equals <value>]
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

`--creation-time-after` (timestamp)

A filter that returns only training jobs created after the specified time (timestamp).

`--creation-time-before` (timestamp)

A filter that returns only training jobs created before the specified time (timestamp).

`--last-modified-time-after` (timestamp)

A filter that returns only training jobs modified after the specified time (timestamp).

`--last-modified-time-before` (timestamp)

A filter that returns only training jobs modified before the specified time (timestamp).

`--name-contains` (string)

A string in the training job name. This filter returns only training jobs whose name contains the specified string.

`--status-equals` (string)

A filter that retrieves only training jobs with a specific status.

Possible values:

- `InProgress`
- `Completed`
- `Failed`
- `Stopping`
- `Stopped`

`--sort-by` (string)

The field to sort results by. The default is `CreationTime` .

Possible values:

- `Name`
- `CreationTime`
- `Status`

`--sort-order` (string)

The sort order for results. The default is `Ascending` .

Possible values:

- `Ascending`
- `Descending`

`--warm-pool-status-equals` (string)

A filter that retrieves only training jobs with a specific warm pool status.

Possible values:

- `Available`
- `Terminated`
- `Reused`
- `InUse`

`--training-plan-arn-equals` (string)

The Amazon Resource Name (ARN); of the training plan to filter training jobs by. For more information about reserving GPU capacity for your SageMaker training jobs using Amazon SageMaker Training Plan, see `` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `` .

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

TrainingJobSummaries -> (list)

An array of `TrainingJobSummary` objects, each listing a training job.

(structure)

Provides summary information about a training job.

TrainingJobName -> (string)

The name of the training job that you want a summary for.

TrainingJobArn -> (string)

The Amazon Resource Name (ARN) of the training job.

CreationTime -> (timestamp)

A timestamp that shows when the training job was created.

TrainingEndTime -> (timestamp)

A timestamp that shows when the training job ended. This field is set only if the training job has one of the terminal statuses (`Completed` , `Failed` , or `Stopped` ).

LastModifiedTime -> (timestamp)

Timestamp when the training job was last modified.

TrainingJobStatus -> (string)

The status of the training job.

SecondaryStatus -> (string)

The secondary status of the training job.

WarmPoolStatus -> (structure)

The status of the warm pool associated with the training job.

Status -> (string)

The status of the warm pool.

- `InUse` : The warm pool is in use for the training job.
- `Available` : The warm pool is available to reuse for a matching training job.
- `Reused` : The warm pool moved to a matching training job for reuse.
- `Terminated` : The warm pool is no longer available. Warm pools are unavailable if they are terminated by a user, terminated for a patch update, or terminated for exceeding the specified `KeepAlivePeriodInSeconds` .

ResourceRetainedBillableTimeInSeconds -> (integer)

The billable time in seconds used by the warm pool. Billable time refers to the absolute wall-clock time.

Multiply `ResourceRetainedBillableTimeInSeconds` by the number of instances (`InstanceCount` ) in your training cluster to get the total compute time SageMaker bills you if you run warm pool training. The formula is as follows: `ResourceRetainedBillableTimeInSeconds * InstanceCount` .

ReusedByJob -> (string)

The name of the matching training job that reused the warm pool.

TrainingPlanArn -> (string)

The Amazon Resource Name (ARN); of the training plan associated with this training job.

For more information about how to reserve GPU capacity for your SageMaker HyperPod clusters using Amazon SageMaker Training Plan, see `` [CreateTrainingPlan](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateTrainingPlan.html) `` .

NextToken -> (string)

If the response is truncated, SageMaker returns this token. To retrieve the next set of training jobs, use it in the subsequent request.