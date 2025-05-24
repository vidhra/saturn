# list-mlflow-tracking-serversÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-mlflow-tracking-servers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-mlflow-tracking-servers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# list-mlflow-tracking-servers

## Description

Lists all MLflow Tracking Servers.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListMlflowTrackingServers)

`list-mlflow-tracking-servers` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `TrackingServerSummaries`

## Synopsis

```
list-mlflow-tracking-servers
[--created-after <value>]
[--created-before <value>]
[--tracking-server-status <value>]
[--mlflow-version <value>]
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

`--created-after` (timestamp)

Use the `CreatedAfter` filter to only list tracking servers created after a specific date and time. Listed tracking servers are shown with a date and time such as `"2024-03-16T01:46:56+00:00"` . The `CreatedAfter` parameter takes in a Unix timestamp. To convert a date and time into a Unix timestamp, see [EpochConverter](https://www.epochconverter.com/) .

`--created-before` (timestamp)

Use the `CreatedBefore` filter to only list tracking servers created before a specific date and time. Listed tracking servers are shown with a date and time such as `"2024-03-16T01:46:56+00:00"` . The `CreatedBefore` parameter takes in a Unix timestamp. To convert a date and time into a Unix timestamp, see [EpochConverter](https://www.epochconverter.com/) .

`--tracking-server-status` (string)

Filter for tracking servers with a specified creation status.

Possible values:

- `Creating`
- `Created`
- `CreateFailed`
- `Updating`
- `Updated`
- `UpdateFailed`
- `Deleting`
- `DeleteFailed`
- `Stopping`
- `Stopped`
- `StopFailed`
- `Starting`
- `Started`
- `StartFailed`
- `MaintenanceInProgress`
- `MaintenanceComplete`
- `MaintenanceFailed`

`--mlflow-version` (string)

Filter for tracking servers using the specified MLflow version.

`--sort-by` (string)

Filter for trackings servers sorting by name, creation time, or creation status.

Possible values:

- `Name`
- `CreationTime`
- `Status`

`--sort-order` (string)

Change the order of the listed tracking servers. By default, tracking servers are listed in `Descending` order by creation time. To change the list order, you can specify `SortOrder` to be `Ascending` .

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

TrackingServerSummaries -> (list)

A list of tracking servers according to chosen filters.

(structure)

The summary of the tracking server to list.

TrackingServerArn -> (string)

The ARN of a listed tracking server.

TrackingServerName -> (string)

The name of a listed tracking server.

CreationTime -> (timestamp)

The creation time of a listed tracking server.

LastModifiedTime -> (timestamp)

The last modified time of a listed tracking server.

TrackingServerStatus -> (string)

The creation status of a listed tracking server.

IsActive -> (string)

The activity status of a listed tracking server.

MlflowVersion -> (string)

The MLflow version used for a listed tracking server.

NextToken -> (string)

If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.