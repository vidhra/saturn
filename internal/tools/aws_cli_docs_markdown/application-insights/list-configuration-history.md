# list-configuration-historyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/list-configuration-history.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/list-configuration-history.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [application-insights](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/application-insights/index.html#cli-aws-application-insights) ]

# list-configuration-history

## Description

Lists the INFO, WARN, and ERROR events for periodic configuration updates performed by Application Insights. Examples of events represented are:

- INFO: creating a new alarm or updating an alarm threshold.
- WARN: alarm not created due to insufficient data points used to predict thresholds.
- ERROR: alarm not created due to permission errors or exceeding quotas.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/application-insights-2018-11-25/ListConfigurationHistory)

## Synopsis

```
list-configuration-history
[--resource-group-name <value>]
[--start-time <value>]
[--end-time <value>]
[--event-status <value>]
[--max-results <value>]
[--next-token <value>]
[--account-id <value>]
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

`--resource-group-name` (string)

Resource group to which the application belongs.

`--start-time` (timestamp)

The start time of the event.

`--end-time` (timestamp)

The end time of the event.

`--event-status` (string)

The status of the configuration update event. Possible values include INFO, WARN, and ERROR.

Possible values:

- `INFO`
- `WARN`
- `ERROR`

`--max-results` (integer)

The maximum number of results returned by `ListConfigurationHistory` in paginated output. When this parameter is used, `ListConfigurationHistory` returns only `MaxResults` in a single page along with a `NextToken` response element. The remaining results of the initial request can be seen by sending another `ListConfigurationHistory` request with the returned `NextToken` value. If this parameter is not used, then `ListConfigurationHistory` returns all results.

`--next-token` (string)

The `NextToken` value returned from a previous paginated `ListConfigurationHistory` request where `MaxResults` was used and the results exceeded the value of that parameter. Pagination continues from the end of the previous results that returned the `NextToken` value. This value is `null` when there are no more results to return.

`--account-id` (string)

The Amazon Web Services account ID for the resource group owner.

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

EventList -> (list)

The list of configuration events and their corresponding details.

(structure)

The event information.

ResourceGroupName -> (string)

The name of the resource group of the application to which the configuration event belongs.

AccountId -> (string)

The Amazon Web Services account ID for the owner of the application to which the configuration event belongs.

MonitoredResourceARN -> (string)

The resource monitored by Application Insights.

EventStatus -> (string)

The status of the configuration update event. Possible values include INFO, WARN, and ERROR.

EventResourceType -> (string)

The resource type that Application Insights attempted to configure, for example, CLOUDWATCH_ALARM.

EventTime -> (timestamp)

The timestamp of the event.

EventDetail -> (string)

The details of the event in plain text.

EventResourceName -> (string)

The name of the resource Application Insights attempted to configure.

NextToken -> (string)

The `NextToken` value to include in a future `ListConfigurationHistory` request. When the results of a `ListConfigurationHistory` request exceed `MaxResults` , this value can be used to retrieve the next page of results. This value is `null` when there are no more results to return.