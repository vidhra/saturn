# list-serversÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/list-servers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/list-servers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [migrationhubstrategy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/index.html#cli-aws-migrationhubstrategy) ]

# list-servers

## Description

Returns a list of all the servers.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/migrationhubstrategy-2020-02-19/ListServers)

`list-servers` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `serverInfos`

## Synopsis

```
list-servers
[--filter-value <value>]
[--group-id-filter <value>]
[--server-criteria <value>]
[--sort <value>]
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

`--filter-value` (string)

Specifies the filter value, which is based on the type of server criteria. For example, if `serverCriteria` is `OS_NAME` , and the `filterValue` is equal to `WindowsServer` , then `ListServers` returns all of the servers matching the OS name `WindowsServer` .

`--group-id-filter` (list)

Specifies the group ID to filter on.

(structure)

The object containing information about distinct imports or groups for Strategy Recommendations.

name -> (string)

The key of the specific import group.

value -> (string)

The value of the specific import group.

Shorthand Syntax:

```
name=string,value=string ...
```

JSON Syntax:

```
[
  {
    "name": "ExternalId"|"ExternalSourceType",
    "value": "string"
  }
  ...
]
```

`--server-criteria` (string)

Criteria for filtering servers.

Possible values:

- `NOT_DEFINED`
- `OS_NAME`
- `STRATEGY`
- `DESTINATION`
- `SERVER_ID`
- `ANALYSIS_STATUS`
- `ERROR_CATEGORY`

`--sort` (string)

Specifies whether to sort by ascending (`ASC` ) or descending (`DESC` ) order.

Possible values:

- `ASC`
- `DESC`

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

The token you use to retrieve the next set of results, or null if there are no more results.

serverInfos -> (list)

The list of servers with detailed information about each server.

(structure)

Detailed information about a server.

antipatternReportS3Object -> (structure)

The S3 bucket name and Amazon S3 key name for anti-pattern report.

s3Bucket -> (string)

The S3 bucket name.

s3key -> (string)

The Amazon S3 key name.

antipatternReportStatus -> (string)

The status of the anti-pattern report generation.

antipatternReportStatusMessage -> (string)

A message about the status of the anti-pattern report generation.

applicationComponentStrategySummary -> (list)

A list of strategy summaries.

(structure)

Object containing the summary of the strategy recommendations.

count -> (integer)

The count of recommendations per strategy.

strategy -> (string)

The name of recommended strategy.

dataCollectionStatus -> (string)

The status of assessment for the server.

id -> (string)

The server ID.

lastAnalyzedTimestamp -> (timestamp)

The timestamp of when the server was assessed.

listAntipatternSeveritySummary -> (list)

A list of anti-pattern severity summaries.

(structure)

Contains the summary of anti-patterns and their severity.

count -> (integer)

Contains the count of anti-patterns.

severity -> (string)

Contains the severity of anti-patterns.

name -> (string)

The name of the server.

recommendationSet -> (structure)

A set of recommendations.

strategy -> (string)

The recommended strategy.

targetDestination -> (string)

The recommended target destination.

transformationTool -> (structure)

The target destination for the recommendation set.

description -> (string)

Description of the tool.

name -> (string)

Name of the tool.

tranformationToolInstallationLink -> (string)

URL for installing the tool.

serverError -> (structure)

The error in server analysis.

serverErrorCategory -> (string)

The error category of server analysis.

serverType -> (string)

The type of server.

statusMessage -> (string)

A message about the status of data collection, which contains detailed descriptions of any error messages.

systemInfo -> (structure)

System information about the server.

cpuArchitecture -> (string)

CPU architecture type for the server.

fileSystemType -> (string)

File system type for the server.

networkInfoList -> (list)

Networking information related to a server.

(structure)

Information about the serverâs network for which the assessment was run.

interfaceName -> (string)

Information about the name of the interface of the server for which the assessment was run.

ipAddress -> (string)

Information about the IP address of the server for which the assessment was run.

macAddress -> (string)

Information about the MAC address of the server for which the assessment was run.

netMask -> (string)

Information about the subnet mask of the server for which the assessment was run.

osInfo -> (structure)

Operating system corresponding to a server.

type -> (string)

Information about the type of operating system.

version -> (string)

Information about the version of operating system.