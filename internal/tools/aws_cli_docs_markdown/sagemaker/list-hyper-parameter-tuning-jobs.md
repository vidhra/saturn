# list-hyper-parameter-tuning-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-hyper-parameter-tuning-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-hyper-parameter-tuning-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# list-hyper-parameter-tuning-jobs

## Description

Gets a list of [HyperParameterTuningJobSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobSummary.html) objects that describe the hyperparameter tuning jobs launched in your account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListHyperParameterTuningJobs)

`list-hyper-parameter-tuning-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `HyperParameterTuningJobSummaries`

## Synopsis

```
list-hyper-parameter-tuning-jobs
[--sort-by <value>]
[--sort-order <value>]
[--name-contains <value>]
[--creation-time-after <value>]
[--creation-time-before <value>]
[--last-modified-time-after <value>]
[--last-modified-time-before <value>]
[--status-equals <value>]
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

`--sort-by` (string)

The field to sort results by. The default is `Name` .

Possible values:

- `Name`
- `Status`
- `CreationTime`

`--sort-order` (string)

The sort order for results. The default is `Ascending` .

Possible values:

- `Ascending`
- `Descending`

`--name-contains` (string)

A string in the tuning job name. This filter returns only tuning jobs whose name contains the specified string.

`--creation-time-after` (timestamp)

A filter that returns only tuning jobs that were created after the specified time.

`--creation-time-before` (timestamp)

A filter that returns only tuning jobs that were created before the specified time.

`--last-modified-time-after` (timestamp)

A filter that returns only tuning jobs that were modified after the specified time.

`--last-modified-time-before` (timestamp)

A filter that returns only tuning jobs that were modified before the specified time.

`--status-equals` (string)

A filter that returns only tuning jobs with the specified status.

Possible values:

- `Completed`
- `InProgress`
- `Failed`
- `Stopped`
- `Stopping`
- `Deleting`
- `DeleteFailed`

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

HyperParameterTuningJobSummaries -> (list)

A list of [HyperParameterTuningJobSummary](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_HyperParameterTuningJobSummary.html) objects that describe the tuning jobs that the `ListHyperParameterTuningJobs` request returned.

(structure)

Provides summary information about a hyperparameter tuning job.

HyperParameterTuningJobName -> (string)

The name of the tuning job.

HyperParameterTuningJobArn -> (string)

The Amazon Resource Name (ARN) of the tuning job.

HyperParameterTuningJobStatus -> (string)

The status of the tuning job.

Strategy -> (string)

Specifies the search strategy hyperparameter tuning uses to choose which hyperparameters to evaluate at each iteration.

CreationTime -> (timestamp)

The date and time that the tuning job was created.

HyperParameterTuningEndTime -> (timestamp)

The date and time that the tuning job ended.

LastModifiedTime -> (timestamp)

The date and time that the tuning job was modified.

TrainingJobStatusCounters -> (structure)

The [TrainingJobStatusCounters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_TrainingJobStatusCounters.html) object that specifies the numbers of training jobs, categorized by status, that this tuning job launched.

Completed -> (integer)

The number of completed training jobs launched by the hyperparameter tuning job.

InProgress -> (integer)

The number of in-progress training jobs launched by a hyperparameter tuning job.

RetryableError -> (integer)

The number of training jobs that failed, but can be retried. A failed training job can be retried only if it failed because an internal service error occurred.

NonRetryableError -> (integer)

The number of training jobs that failed and canât be retried. A failed training job canât be retried if it failed because a client error occurred.

Stopped -> (integer)

The number of training jobs launched by a hyperparameter tuning job that were manually stopped.

ObjectiveStatusCounters -> (structure)

The [ObjectiveStatusCounters](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ObjectiveStatusCounters.html) object that specifies the numbers of training jobs, categorized by objective metric status, that this tuning job launched.

Succeeded -> (integer)

The number of training jobs whose final objective metric was evaluated by the hyperparameter tuning job and used in the hyperparameter tuning process.

Pending -> (integer)

The number of training jobs that are in progress and pending evaluation of their final objective metric.

Failed -> (integer)

The number of training jobs whose final objective metric was not evaluated and used in the hyperparameter tuning process. This typically occurs when the training job failed or did not emit an objective metric.

ResourceLimits -> (structure)

The [ResourceLimits](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ResourceLimits.html) object that specifies the maximum number of training jobs and parallel training jobs allowed for this tuning job.

MaxNumberOfTrainingJobs -> (integer)

The maximum number of training jobs that a hyperparameter tuning job can launch.

MaxParallelTrainingJobs -> (integer)

The maximum number of concurrent training jobs that a hyperparameter tuning job can launch.

MaxRuntimeInSeconds -> (integer)

The maximum time in seconds that a hyperparameter tuning job can run.

NextToken -> (string)

If the result of this `ListHyperParameterTuningJobs` request was truncated, the response includes a `NextToken` . To retrieve the next set of tuning jobs, use the token in the next request.