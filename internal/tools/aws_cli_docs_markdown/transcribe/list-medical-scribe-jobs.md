# list-medical-scribe-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-medical-scribe-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/list-medical-scribe-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [transcribe](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/transcribe/index.html#cli-aws-transcribe) ]

# list-medical-scribe-jobs

## Description

Provides a list of Medical Scribe jobs that match the specified criteria. If no criteria are specified, all Medical Scribe jobs are returned.

To get detailed information about a specific Medical Scribe job, use the operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/transcribe-2017-10-26/ListMedicalScribeJobs)

## Synopsis

```
list-medical-scribe-jobs
[--status <value>]
[--job-name-contains <value>]
[--next-token <value>]
[--max-results <value>]
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

`--status` (string)

Returns only Medical Scribe jobs with the specified status. Jobs are ordered by creation date, with the newest job first. If you do not include `Status` , all Medical Scribe jobs are returned.

Possible values:

- `QUEUED`
- `IN_PROGRESS`
- `FAILED`
- `COMPLETED`

`--job-name-contains` (string)

Returns only the Medical Scribe jobs that contain the specified string. The search is not case sensitive.

`--next-token` (string)

If your `ListMedicalScribeJobs` request returns more results than can be displayed, `NextToken` is displayed in the response with an associated string. To get the next page of results, copy this string and repeat your request, including `NextToken` with the value of the copied string. Repeat as needed to view all your results.

`--max-results` (integer)

The maximum number of Medical Scribe jobs to return in each page of results. If there are fewer results than the value that you specify, only the actual results are returned. If you do not specify a value, a default of 5 is used.

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

Status -> (string)

Lists all Medical Scribe jobs that have the status specified in your request. Jobs are ordered by creation date, with the newest job first.

NextToken -> (string)

If `NextToken` is present in your response, it indicates that not all results are displayed. To view the next set of results, copy the string associated with the `NextToken` parameter in your results output, then run your request again including `NextToken` with the value of the copied string. Repeat as needed to view all your results.

MedicalScribeJobSummaries -> (list)

Provides a summary of information about each result.

(structure)

Provides detailed information about a specific Medical Scribe job.

MedicalScribeJobName -> (string)

The name of the Medical Scribe job. Job names are case sensitive and must be unique within an Amazon Web Services account.

CreationTime -> (timestamp)

The date and time the specified Medical Scribe job request was made.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.

StartTime -> (timestamp)

The date and time your Medical Scribe job began processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.789000-07:00` represents a Medical Scribe job that started processing at 12:32 PM UTC-7 on May 4, 2022.

CompletionTime -> (timestamp)

The date and time the specified Medical Scribe job finished processing.

Timestamps are in the format `YYYY-MM-DD'T'HH:MM:SS.SSSSSS-UTC` . For example, `2022-05-04T12:32:58.761000-07:00` represents a Medical Scribe job that finished processing at 12:32 PM UTC-7 on May 4, 2022.

LanguageCode -> (string)

The language code used to create your Medical Scribe job. US English (`en-US` ) is the only supported language for Medical Scribe jobs.

MedicalScribeJobStatus -> (string)

Provides the status of the specified Medical Scribe job.

If the status is `COMPLETED` , the job is finished and you can find the results at the location specified in `MedicalScribeOutput` If the status is `FAILED` , `FailureReason` provides details on why your Medical Scribe job failed.

FailureReason -> (string)

If `MedicalScribeJobStatus` is `FAILED` , `FailureReason` contains information about why the transcription job failed. See also: [Common Errors](https://docs.aws.amazon.com/transcribe/latest/APIReference/CommonErrors.html) .