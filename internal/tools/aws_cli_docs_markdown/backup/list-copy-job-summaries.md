# list-copy-job-summariesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-copy-job-summaries.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/list-copy-job-summaries.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [backup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/backup/index.html#cli-aws-backup) ]

# list-copy-job-summaries

## Description

This request obtains a list of copy jobs created or running within the the most recent 30 days. You can include parameters AccountID, State, ResourceType, MessageCategory, AggregationPeriod, MaxResults, or NextToken to filter results.

This request returns a summary that contains Region, Account, State, RestourceType, MessageCategory, StartTime, EndTime, and Count of included jobs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/backup-2018-11-15/ListCopyJobSummaries)

## Synopsis

```
list-copy-job-summaries
[--account-id <value>]
[--state <value>]
[--resource-type <value>]
[--message-category <value>]
[--aggregation-period <value>]
[--max-results <value>]
[--next-token <value>]
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

`--account-id` (string)

Returns the job count for the specified account.

If the request is sent from a member account or an account not part of Amazon Web Services Organizations, jobs within requestorâs account will be returned.

Root, admin, and delegated administrator accounts can use the value ANY to return job counts from every account in the organization.

`AGGREGATE_ALL` aggregates job counts from all accounts within the authenticated organization, then returns the sum.

`--state` (string)

This parameter returns the job count for jobs with the specified state.

The the value ANY returns count of all states.

`AGGREGATE_ALL` aggregates job counts for all states and returns the sum.

Possible values:

- `CREATED`
- `RUNNING`
- `ABORTING`
- `ABORTED`
- `COMPLETING`
- `COMPLETED`
- `FAILING`
- `FAILED`
- `PARTIAL`
- `AGGREGATE_ALL`
- `ANY`

`--resource-type` (string)

Returns the job count for the specified resource type. Use request `GetSupportedResourceTypes` to obtain strings for supported resource types.

The the value ANY returns count of all resource types.

`AGGREGATE_ALL` aggregates job counts for all resource types and returns the sum.

The type of Amazon Web Services resource to be backed up; for example, an Amazon Elastic Block Store (Amazon EBS) volume or an Amazon Relational Database Service (Amazon RDS) database.

`--message-category` (string)

This parameter returns the job count for the specified message category.

Example accepted strings include `AccessDenied` , `Success` , and `InvalidParameters` . See [Monitoring](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html) for a list of accepted MessageCategory strings.

The the value ANY returns count of all message categories.

`AGGREGATE_ALL` aggregates job counts for all message categories and returns the sum.

`--aggregation-period` (string)

The period for the returned results.

- `ONE_DAY` - The daily job count for the prior 14 days.
- `SEVEN_DAYS` - The aggregated job count for the prior 7 days.
- `FOURTEEN_DAYS` - The aggregated job count for prior 14 days.

Possible values:

- `ONE_DAY`
- `SEVEN_DAYS`
- `FOURTEEN_DAYS`

`--max-results` (integer)

This parameter sets the maximum number of items to be returned.

The value is an integer. Range of accepted values is from 1 to 500.

`--next-token` (string)

The next item following a partial list of returned resources. For example, if a request is made to return `MaxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.

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

CopyJobSummaries -> (list)

This return shows a summary that contains Region, Account, State, ResourceType, MessageCategory, StartTime, EndTime, and Count of included jobs.

(structure)

This is a summary of copy jobs created or running within the most recent 30 days.

The returned summary may contain the following: Region, Account, State, RestourceType, MessageCategory, StartTime, EndTime, and Count of included jobs.

Region -> (string)

The Amazon Web Services Regions within the job summary.

AccountId -> (string)

The account ID that owns the jobs within the summary.

State -> (string)

This value is job count for jobs with the specified state.

ResourceType -> (string)

This value is the job count for the specified resource type. The request `GetSupportedResourceTypes` returns strings for supported resource types

MessageCategory -> (string)

This parameter is the job count for the specified message category.

Example strings include `AccessDenied` , `Success` , and `InvalidParameters` . See [Monitoring](https://docs.aws.amazon.com/aws-backup/latest/devguide/monitoring.html) for a list of MessageCategory strings.

The the value ANY returns count of all message categories.

`AGGREGATE_ALL` aggregates job counts for all message categories and returns the sum.

Count -> (integer)

The value as a number of jobs in a job summary.

StartTime -> (timestamp)

The value of time in number format of a job start time.

This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

EndTime -> (timestamp)

The value of time in number format of a job end time.

This value is the time in Unix format, Coordinated Universal Time (UTC), and accurate to milliseconds. For example, the value 1516925490.087 represents Friday, January 26, 2018 12:11:30.087 AM.

AggregationPeriod -> (string)

The period for the returned results.

- `ONE_DAY` - The daily job count for the prior 14 days.
- `SEVEN_DAYS` - The aggregated job count for the prior 7 days.
- `FOURTEEN_DAYS` - The aggregated job count for prior 14 days.

NextToken -> (string)

The next item following a partial list of returned resources. For example, if a request is made to return `MaxResults` number of resources, `NextToken` allows you to return more items in your list starting at the location pointed to by the next token.