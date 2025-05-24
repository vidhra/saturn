# describe-fraudster-registration-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/voice-id/describe-fraudster-registration-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/voice-id/describe-fraudster-registration-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [voice-id](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/voice-id/index.html#cli-aws-voice-id) ]

# describe-fraudster-registration-job

## Description

Describes the specified fraudster registration job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/voice-id-2021-09-27/DescribeFraudsterRegistrationJob)

## Synopsis

```
describe-fraudster-registration-job
--domain-id <value>
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

`--domain-id` (string)

The identifier of the domain that contains the fraudster registration job.

`--job-id` (string)

The identifier of the fraudster registration job you are describing.

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

Job -> (structure)

Contains details about the specified fraudster registration job.

CreatedAt -> (timestamp)

A timestamp of when the fraudster registration job was created.

DataAccessRoleArn -> (string)

The IAM role Amazon Resource Name (ARN) that grants Voice ID permissions to access customerâs buckets to read the input manifest file and write the job output file.

DomainId -> (string)

The identifier of the domain that contains the fraudster registration job.

EndedAt -> (timestamp)

A timestamp of when the fraudster registration job ended.

FailureDetails -> (structure)

Contains details that are populated when an entire batch job fails. In cases of individual registration job failures, the batch job as a whole doesnât fail; it is completed with a `JobStatus` of `COMPLETED_WITH_ERRORS` . You can use the job output file to identify the individual registration requests that failed.

Message -> (string)

A description of the error that caused the batch job failure.

StatusCode -> (integer)

An HTTP status code representing the nature of the error.

InputDataConfig -> (structure)

The input data config containing an S3 URI for the input manifest file that contains the list of fraudster registration job requests.

S3Uri -> (string)

The S3 location for the input manifest file that contains the list of individual enrollment or registration job requests.

JobId -> (string)

The service-generated identifier for the fraudster registration job.

JobName -> (string)

The client-provided name for the fraudster registration job.

JobProgress -> (structure)

Shows the completed percentage of registration requests listed in the input file.

PercentComplete -> (integer)

Shows the completed percentage of enrollment or registration requests listed in the input file.

JobStatus -> (string)

The current status of the fraudster registration job.

OutputDataConfig -> (structure)

The output data config containing the S3 location where you want Voice ID to write your job output file; you must also include a KMS key ID in order to encrypt the file.

KmsKeyId -> (string)

The identifier of the KMS key you want Voice ID to use to encrypt the output file of a speaker enrollment job/fraudster registration job.

S3Uri -> (string)

The S3 path of the folder where Voice ID writes the job output file. It has a `*.out` extension. For example, if the input file name is `input-file.json` and the output folder path is `s3://output-bucket/output-folder` , the full output file path is `s3://output-bucket/output-folder/job-Id/input-file.json.out` .

RegistrationConfig -> (structure)

The registration config containing details such as the action to take when a duplicate fraudster is detected, and the similarity threshold to use for detecting a duplicate fraudster.

DuplicateRegistrationAction -> (string)

The action to take when a fraudster is identified as a duplicate. The default action is `SKIP` , which skips registering the duplicate fraudster. Setting the value to `REGISTER_AS_NEW` always registers a new fraudster into the specified domain.

FraudsterSimilarityThreshold -> (integer)

The minimum similarity score between the new and old fraudsters in order to consider the new fraudster a duplicate.

WatchlistIds -> (list)

The identifiers of watchlists that a fraudster is registered to. If a watchlist isnât provided, the fraudsters are registered to the default watchlist.

(string)