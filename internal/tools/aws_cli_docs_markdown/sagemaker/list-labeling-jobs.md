# list-labeling-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-labeling-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-labeling-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# list-labeling-jobs

## Description

Gets a list of labeling jobs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListLabelingJobs)

`list-labeling-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `LabelingJobSummaryList`

## Synopsis

```
list-labeling-jobs
[--creation-time-after <value>]
[--creation-time-before <value>]
[--last-modified-time-after <value>]
[--last-modified-time-before <value>]
[--name-contains <value>]
[--sort-by <value>]
[--sort-order <value>]
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

`--creation-time-after` (timestamp)

A filter that returns only labeling jobs created after the specified time (timestamp).

`--creation-time-before` (timestamp)

A filter that returns only labeling jobs created before the specified time (timestamp).

`--last-modified-time-after` (timestamp)

A filter that returns only labeling jobs modified after the specified time (timestamp).

`--last-modified-time-before` (timestamp)

A filter that returns only labeling jobs modified before the specified time (timestamp).

`--name-contains` (string)

A string in the labeling job name. This filter returns only labeling jobs whose name contains the specified string.

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

`--status-equals` (string)

A filter that retrieves only labeling jobs with a specific status.

Possible values:

- `Initializing`
- `InProgress`
- `Completed`
- `Failed`
- `Stopping`
- `Stopped`

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

LabelingJobSummaryList -> (list)

An array of `LabelingJobSummary` objects, each describing a labeling job.

(structure)

Provides summary information about a labeling job.

LabelingJobName -> (string)

The name of the labeling job.

LabelingJobArn -> (string)

The Amazon Resource Name (ARN) assigned to the labeling job when it was created.

CreationTime -> (timestamp)

The date and time that the job was created (timestamp).

LastModifiedTime -> (timestamp)

The date and time that the job was last modified (timestamp).

LabelingJobStatus -> (string)

The current status of the labeling job.

LabelCounters -> (structure)

Counts showing the progress of the labeling job.

TotalLabeled -> (integer)

The total number of objects labeled.

HumanLabeled -> (integer)

The total number of objects labeled by a human worker.

MachineLabeled -> (integer)

The total number of objects labeled by automated data labeling.

FailedNonRetryableError -> (integer)

The total number of objects that could not be labeled due to an error.

Unlabeled -> (integer)

The total number of objects not yet labeled.

WorkteamArn -> (string)

The Amazon Resource Name (ARN) of the work team assigned to the job.

PreHumanTaskLambdaArn -> (string)

The Amazon Resource Name (ARN) of a Lambda function. The function is run before each data object is sent to a worker.

AnnotationConsolidationLambdaArn -> (string)

The Amazon Resource Name (ARN) of the Lambda function used to consolidate the annotations from individual workers into a label for a data object. For more information, see [Annotation Consolidation](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-annotation-consolidation.html) .

FailureReason -> (string)

If the `LabelingJobStatus` field is `Failed` , this field contains a description of the error.

LabelingJobOutput -> (structure)

The location of the output produced by the labeling job.

OutputDatasetS3Uri -> (string)

The Amazon S3 bucket location of the manifest file for labeled data.

FinalActiveLearningModelArn -> (string)

The Amazon Resource Name (ARN) for the most recent SageMaker model trained as part of automated data labeling.

InputConfig -> (structure)

Input configuration for the labeling job.

DataSource -> (structure)

The location of the input data.

S3DataSource -> (structure)

The Amazon S3 location of the input data objects.

ManifestS3Uri -> (string)

The Amazon S3 location of the manifest file that describes the input data objects.

The input manifest file referenced in `ManifestS3Uri` must contain one of the following keys: `source-ref` or `source` . The value of the keys are interpreted as follows:

- `source-ref` : The source of the object is the Amazon S3 object specified in the value. Use this value when the object is a binary object, such as an image.
- `source` : The source of the object is the value. Use this value when the object is a text value.

If you are a new user of Ground Truth, it is recommended you review [Use an Input Manifest File](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-input-data-input-manifest.html) in the Amazon SageMaker Developer Guide to learn how to create an input manifest file.

SnsDataSource -> (structure)

An Amazon SNS data source used for streaming labeling jobs. To learn more, see [Send Data to a Streaming Labeling Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-labeling-job.html#sms-streaming-how-it-works-send-data) .

SnsTopicArn -> (string)

The Amazon SNS input topic Amazon Resource Name (ARN). Specify the ARN of the input topic you will use to send new data objects to a streaming labeling job.

DataAttributes -> (structure)

Attributes of the data specified by the customer.

ContentClassifiers -> (list)

Declares that your content is free of personally identifiable information or adult content. SageMaker may restrict the Amazon Mechanical Turk workers that can view your task based on this information.

(string)

NextToken -> (string)

If the response is truncated, SageMaker returns this token. To retrieve the next set of labeling jobs, use it in the subsequent request.