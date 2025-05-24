# list-profiling-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/list-profiling-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/list-profiling-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeguruprofiler](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeguruprofiler/index.html#cli-aws-codeguruprofiler) ]

# list-profiling-groups

## Description

Returns a list of profiling groups. The profiling groups are returned as ` `ProfilingGroupDescription` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription).html`__ objects.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeguruprofiler-2019-07-18/ListProfilingGroups)

## Synopsis

```
list-profiling-groups
[--include-description | --no-include-description]
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

`--include-description` | `--no-include-description` (boolean)

A `Boolean` value indicating whether to include a description. If `true` , then a list of ` `ProfilingGroupDescription` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription).html`__ objects that contain detailed information about profiling groups is returned. If `false` , then a list of profiling group names is returned.

`--max-results` (integer)

The maximum number of profiling groups results returned by `ListProfilingGroups` in paginated output. When this parameter is used, `ListProfilingGroups` only returns `maxResults` results in a single page along with a `nextToken` response element. The remaining results of the initial request can be seen by sending another `ListProfilingGroups` request with the returned `nextToken` value.

`--next-token` (string)

The `nextToken` value returned from a previous paginated `ListProfilingGroups` request where `maxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `nextToken` value.

### Note

This token should be treated as an opaque identifier that is only used to retrieve the next items in a list and not for other programmatic purposes.

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

nextToken -> (string)

The `nextToken` value to include in a future `ListProfilingGroups` request. When the results of a `ListProfilingGroups` request exceed `maxResults` , this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.

profilingGroupNames -> (list)

A returned list of profiling group names. A list of the names is returned only if `includeDescription` is `false` , otherwise a list of ` `ProfilingGroupDescription` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription).html`__ objects is returned.

(string)

profilingGroups -> (list)

A returned list ` `ProfilingGroupDescription` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription).html`__ objects. A list of ` `ProfilingGroupDescription` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingGroupDescription).html`__ objects is returned only if `includeDescription` is `true` , otherwise a list of profiling group names is returned.

(structure)

Contains information about a profiling group.

agentOrchestrationConfig -> (structure)

An ` `AgentOrchestrationConfig` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentOrchestrationConfig](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AgentOrchestrationConfig).html`__ object that indicates if the profiling group is enabled for profiled or not.

profilingEnabled -> (boolean)

A `Boolean` that specifies whether the profiling agent collects profiling data or not. Set to `true` to enable profiling.

arn -> (string)

The Amazon Resource Name (ARN) identifying the profiling group resource.

computePlatform -> (string)

The compute platform of the profiling group. If it is set to `AWSLambda` , then the profiled application runs on AWS Lambda. If it is set to `Default` , then the profiled application runs on a compute platform that is not AWS Lambda, such an Amazon EC2 instance, an on-premises server, or a different platform. The default is `Default` .

createdAt -> (timestamp)

The time when the profiling group was created. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

name -> (string)

The name of the profiling group.

profilingStatus -> (structure)

A ` `ProfilingStatus` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingStatus](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_ProfilingStatus).html`__ object that includes information about the last time a profile agent pinged back, the last time a profile was received, and the aggregation period and start time for the most recent aggregated profile.

latestAgentOrchestratedAt -> (timestamp)

The date and time when the profiling agent most recently pinged back. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

latestAgentProfileReportedAt -> (timestamp)

The date and time when the most recent profile was received. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

latestAggregatedProfile -> (structure)

An ` `AggregatedProfileTime` [https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime](https://docs.aws.amazon.com/codeguru/latest/profiler-api/API_AggregatedProfileTime).html`__ object that contains the aggregation period and start time for an aggregated profile.

period -> (string)

The aggregation period. This indicates the period during which an aggregation profile collects posted agent profiles for a profiling group. Use one of three valid durations that are specified using the ISO 8601 format.

- `P1D` â 1 day
- `PT1H` â 1 hour
- `PT5M` â 5 minutes

start -> (timestamp)

The time that aggregation of posted agent profiles for a profiling group starts. The aggregation profile contains profiles posted by the agent starting at this time for an aggregation period specified by the `period` property of the `AggregatedProfileTime` object.

Specify `start` using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.

tags -> (map)

A list of the tags that belong to this profiling group.

key -> (string)

value -> (string)

updatedAt -> (timestamp)

The date and time when the profiling group was last updated. Specify using the ISO 8601 format. For example, 2020-06-01T13:15:02.001Z represents 1 millisecond past June 1, 2020 1:15:02 PM UTC.