# list-model-invocation-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/list-model-invocation-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/list-model-invocation-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock/index.html#cli-aws-bedrock) ]

# list-model-invocation-jobs

## Description

Lists all batch inference jobs in the account. For more information, see [View details about a batch inference job](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-view.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-2023-04-20/ListModelInvocationJobs)

`list-model-invocation-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `invocationJobSummaries`

## Synopsis

```
list-model-invocation-jobs
[--submit-time-after <value>]
[--submit-time-before <value>]
[--status-equals <value>]
[--name-contains <value>]
[--sort-by <value>]
[--sort-order <value>]
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

`--submit-time-after` (timestamp)

Specify a time to filter for batch inference jobs that were submitted after the time you specify.

`--submit-time-before` (timestamp)

Specify a time to filter for batch inference jobs that were submitted before the time you specify.

`--status-equals` (string)

Specify a status to filter for batch inference jobs whose statuses match the string you specify.

The following statuses are possible:

- Submitted â This job has been submitted to a queue for validation.
- Validating â This job is being validated for the requirements described in [Format and upload your batch inference data](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html) . The criteria include the following:
- Your IAM service role has access to the Amazon S3 buckets containing your files.
- Your files are .jsonl files and each individual record is a JSON object in the correct format. Note that validation doesnât check if the `modelInput` value matches the request body for the model.
- Your files fulfill the requirements for file size and number of records. For more information, see [Quotas for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) .
- Scheduled â This job has been validated and is now in a queue. The job will automatically start when it reaches its turn.
- Expired â This job timed out because it was scheduled but didnât begin before the set timeout duration. Submit a new job request.
- InProgress â This job has begun. You can start viewing the results in the output S3 location.
- Completed â This job has successfully completed. View the output files in the output S3 location.
- PartiallyCompleted â This job has partially completed. Not all of your records could be processed in time. View the output files in the output S3 location.
- Failed â This job has failed. Check the failure message for any further details. For further assistance, reach out to the [Amazon Web ServicesSupport Center](https://console.aws.amazon.com/support/home/) .
- Stopped â This job was stopped by a user.
- Stopping â This job is being stopped by a user.

Possible values:

- `Submitted`
- `InProgress`
- `Completed`
- `Failed`
- `Stopping`
- `Stopped`
- `PartiallyCompleted`
- `Expired`
- `Validating`
- `Scheduled`

`--name-contains` (string)

Specify a string to filter for batch inference jobs whose names contain the string.

`--sort-by` (string)

An attribute by which to sort the results.

Possible values:

- `CreationTime`

`--sort-order` (string)

Specifies whether to sort the results by ascending or descending order.

Possible values:

- `Ascending`
- `Descending`

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

nextToken -> (string)

If there are more results than can fit in the response, a `nextToken` is returned. Use the `nextToken` in a request to return the next batch of results.

invocationJobSummaries -> (list)

A list of items, each of which contains a summary about a batch inference job.

(structure)

A summary of a batch inference job.

jobArn -> (string)

The Amazon Resource Name (ARN) of the batch inference job.

jobName -> (string)

The name of the batch inference job.

modelId -> (string)

The unique identifier of the foundation model used for model inference.

clientRequestToken -> (string)

A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If this token matches a previous request, Amazon Bedrock ignores the request, but does not return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .

roleArn -> (string)

The Amazon Resource Name (ARN) of the service role with permissions to carry out and manage batch inference. You can use the console to create a default service role or follow the steps at [Create a service role for batch inference](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-iam-sr.html) .

status -> (string)

The status of the batch inference job.

The following statuses are possible:

- Submitted â This job has been submitted to a queue for validation.
- Validating â This job is being validated for the requirements described in [Format and upload your batch inference data](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-inference-data.html) . The criteria include the following:
- Your IAM service role has access to the Amazon S3 buckets containing your files.
- Your files are .jsonl files and each individual record is a JSON object in the correct format. Note that validation doesnât check if the `modelInput` value matches the request body for the model.
- Your files fulfill the requirements for file size and number of records. For more information, see [Quotas for Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/quotas.html) .
- Scheduled â This job has been validated and is now in a queue. The job will automatically start when it reaches its turn.
- Expired â This job timed out because it was scheduled but didnât begin before the set timeout duration. Submit a new job request.
- InProgress â This job has begun. You can start viewing the results in the output S3 location.
- Completed â This job has successfully completed. View the output files in the output S3 location.
- PartiallyCompleted â This job has partially completed. Not all of your records could be processed in time. View the output files in the output S3 location.
- Failed â This job has failed. Check the failure message for any further details. For further assistance, reach out to the [Amazon Web ServicesSupport Center](https://console.aws.amazon.com/support/home/) .
- Stopped â This job was stopped by a user.
- Stopping â This job is being stopped by a user.

message -> (string)

If the batch inference job failed, this field contains a message describing why the job failed.

submitTime -> (timestamp)

The time at which the batch inference job was submitted.

lastModifiedTime -> (timestamp)

The time at which the batch inference job was last modified.

endTime -> (timestamp)

The time at which the batch inference job ended.

inputDataConfig -> (tagged union structure)

Details about the location of the input to the batch inference job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3InputDataConfig`.

s3InputDataConfig -> (structure)

Contains the configuration of the S3 location of the input data.

s3InputFormat -> (string)

The format of the input data.

s3Uri -> (string)

The S3 location of the input data.

s3BucketOwner -> (string)

The ID of the Amazon Web Services account that owns the S3 bucket containing the input data.

outputDataConfig -> (tagged union structure)

Details about the location of the output of the batch inference job.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `s3OutputDataConfig`.

s3OutputDataConfig -> (structure)

Contains the configuration of the S3 location of the output data.

s3Uri -> (string)

The S3 location of the output data.

s3EncryptionKeyId -> (string)

The unique identifier of the key that encrypts the S3 location of the output data.

s3BucketOwner -> (string)

The ID of the Amazon Web Services account that owns the S3 bucket containing the output data.

vpcConfig -> (structure)

The configuration of the Virtual Private Cloud (VPC) for the data in the batch inference job. For more information, see [Protect batch inference jobs using a VPC](https://docs.aws.amazon.com/bedrock/latest/userguide/batch-vpc) .

subnetIds -> (list)

An array of IDs for each subnet in the VPC to use.

(string)

securityGroupIds -> (list)

An array of IDs for each security group in the VPC to use.

(string)

timeoutDurationInHours -> (integer)

The number of hours after which the batch inference job was set to time out.

jobExpirationTime -> (timestamp)

The time at which the batch inference job times or timed out.