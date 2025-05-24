# get-identity-resolution-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-identity-resolution-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/get-identity-resolution-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [customer-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/index.html#cli-aws-customer-profiles) ]

# get-identity-resolution-job

## Description

Returns information about an Identity Resolution Job in a specific domain.

Identity Resolution Jobs are set up using the Amazon Connect admin console. For more information, see [Use Identity Resolution to consolidate similar profiles](https://docs.aws.amazon.com/connect/latest/adminguide/use-identity-resolution.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/customer-profiles-2020-08-15/GetIdentityResolutionJob)

## Synopsis

```
get-identity-resolution-job
--domain-name <value>
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

`--domain-name` (string)

The unique name of the domain.

`--job-id` (string)

The unique identifier of the Identity Resolution Job.

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

DomainName -> (string)

The unique name of the domain.

JobId -> (string)

The unique identifier of the Identity Resolution Job.

Status -> (string)

The status of the Identity Resolution Job.

- `PENDING` : The Identity Resolution Job is scheduled but has not started yet. If you turn off the Identity Resolution feature in your domain, jobs in the `PENDING` state are deleted.
- `PREPROCESSING` : The Identity Resolution Job is loading your data.
- `FIND_MATCHING` : The Identity Resolution Job is using the machine learning model to identify profiles that belong to the same matching group.
- `MERGING` : The Identity Resolution Job is merging duplicate profiles.
- `COMPLETED` : The Identity Resolution Job completed successfully.
- `PARTIAL_SUCCESS` : Thereâs a system error and not all of the data is merged. The Identity Resolution Job writes a message indicating the source of the problem.
- `FAILED` : The Identity Resolution Job did not merge any data. It writes a message indicating the source of the problem.

Message -> (string)

The error messages that are generated when the Identity Resolution Job runs.

JobStartTime -> (timestamp)

The timestamp of when the Identity Resolution Job was started or will be started.

JobEndTime -> (timestamp)

The timestamp of when the Identity Resolution Job was completed.

LastUpdatedAt -> (timestamp)

The timestamp of when the Identity Resolution Job was most recently edited.

JobExpirationTime -> (timestamp)

The timestamp of when the Identity Resolution Job will expire.

AutoMerging -> (structure)

Configuration settings for how to perform the auto-merging of profiles.

Enabled -> (boolean)

The flag that enables the auto-merging of duplicate profiles.

Consolidation -> (structure)

A list of matching attributes that represent matching criteria. If two profiles meet at least one of the requirements in the matching attributes list, they will be merged.

MatchingAttributesList -> (list)

A list of matching criteria.

(list)

(string)

ConflictResolution -> (structure)

How the auto-merging process should resolve conflicts between different profiles. For example, if Profile A and Profile B have the same `FirstName` and `LastName` (and that is the matching criteria), which `EmailAddress` should be used?

ConflictResolvingModel -> (string)

How the auto-merging process should resolve conflicts between different profiles.

- `RECENCY` : Uses the data that was most recently updated.
- `SOURCE` : Uses the data from a specific source. For example, if a company has been aquired or two departments have merged, data from the specified source is used. If two duplicate profiles are from the same source, then `RECENCY` is used again.

SourceName -> (string)

The `ObjectType` name that is used to resolve profile merging conflicts when choosing `SOURCE` as the `ConflictResolvingModel` .

MinAllowedConfidenceScoreForMerging -> (double)

A number between 0 and 1 that represents the minimum confidence score required for profiles within a matching group to be merged during the auto-merge process. A higher score means higher similarity required to merge profiles.

ExportingLocation -> (structure)

The S3 location where the Identity Resolution Job writes result files.

S3Exporting -> (structure)

Information about the S3 location where Identity Resolution Jobs write result files.

S3BucketName -> (string)

The name of the S3 bucket name where Identity Resolution Jobs write result files.

S3KeyName -> (string)

The S3 key name of the location where Identity Resolution Jobs write result files.

JobStats -> (structure)

Statistics about the Identity Resolution Job.

NumberOfProfilesReviewed -> (long)

The number of profiles reviewed.

NumberOfMatchesFound -> (long)

The number of matches found.

NumberOfMergesDone -> (long)

The number of merges completed.