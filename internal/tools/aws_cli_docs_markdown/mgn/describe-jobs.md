# describe-jobsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/describe-jobs.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/describe-jobs.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [mgn](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/mgn/index.html#cli-aws-mgn) ]

# describe-jobs

## Description

Returns a list of Jobs. Use the JobsID and fromDate and toData filters to limit which jobs are returned. The response is sorted by creationDataTime - latest date first. Jobs are normally created by the StartTest, StartCutover, and TerminateTargetInstances APIs. Jobs are also created by DiagnosticLaunch and TerminateDiagnosticInstances, which are APIs available only to *Support* and only used in response to relevant support tickets.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/mgn-2020-02-26/DescribeJobs)

`describe-jobs` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `items`

## Synopsis

```
describe-jobs
[--account-id <value>]
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

`--account-id` (string)

Request to describe job log items by Account ID.

`--filters` (structure)

Request to describe Job log filters.

fromDate -> (string)

Request to describe Job log filters by date.

jobIDs -> (list)

Request to describe Job log filters by job ID.

(string)

toDate -> (string)

Request to describe job log items by last date.

Shorthand Syntax:

```
fromDate=string,jobIDs=string,string,toDate=string
```

JSON Syntax:

```
{
  "fromDate": "string",
  "jobIDs": ["string", ...],
  "toDate": "string"
}
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

items -> (list)

Request to describe Job log items.

(structure)

Job.

arn -> (string)

the ARN of the specific Job.

creationDateTime -> (string)

Job creation time.

endDateTime -> (string)

Job end time.

initiatedBy -> (string)

Job initiated by field.

jobID -> (string)

Job ID.

participatingServers -> (list)

Servers participating in a specific Job.

(structure)

Server participating in Job.

launchStatus -> (string)

Participating server launch status.

launchedEc2InstanceID -> (string)

Participating serverâs launched ec2 instance ID.

postLaunchActionsStatus -> (structure)

Participating serverâs Post Launch Actions Status.

postLaunchActionsLaunchStatusList -> (list)

List of Post Launch Action status.

(structure)

Launch Status of the Job Post Launch Actions.

executionID -> (string)

AWS Systems Manager Documentâs execution ID of the of the Job Post Launch Actions.

executionStatus -> (string)

AWS Systems Manager Documentâs execution status.

failureReason -> (string)

AWS Systems Manager Documentâs failure reason.

ssmDocument -> (structure)

AWS Systems Managerâs Document of the of the Job Post Launch Actions.

actionName -> (string)

User-friendly name for the AWS Systems Manager Document.

externalParameters -> (map)

AWS Systems Manager Document external parameters.

key -> (string)

value -> (tagged union structure)

AWS Systems Manager Document external parameter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `dynamicPath`.

dynamicPath -> (string)

AWS Systems Manager Document external parameters dynamic path.

mustSucceedForCutover -> (boolean)

If true, Cutover will not be enabled if the document has failed.

parameters -> (map)

AWS Systems Manager Document parameters.

key -> (string)

value -> (list)

(structure)

AWS Systems Manager Parameter Store parameter.

parameterName -> (string)

AWS Systems Manager Parameter Store parameter name.

parameterType -> (string)

AWS Systems Manager Parameter Store parameter type.

ssmDocumentName -> (string)

AWS Systems Manager Document name or full ARN.

timeoutSeconds -> (integer)

AWS Systems Manager Document timeout seconds.

ssmDocumentType -> (string)

AWS Systems Manager Document type.

ssmAgentDiscoveryDatetime -> (string)

Time where the AWS Systems Manager was detected as running on the Test or Cutover instance.

sourceServerID -> (string)

Participating server Source Server ID.

status -> (string)

Job status.

tags -> (map)

Tags associated with specific Job.

key -> (string)

value -> (string)

type -> (string)

Job type.

nextToken -> (string)

Request to describe Job response by next token.