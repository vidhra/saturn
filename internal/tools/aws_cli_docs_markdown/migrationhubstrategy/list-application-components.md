# list-application-componentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/list-application-components.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/list-application-components.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [migrationhubstrategy](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/migrationhubstrategy/index.html#cli-aws-migrationhubstrategy) ]

# list-application-components

## Description

Retrieves a list of all the application components (processes).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/migrationhubstrategy-2020-02-19/ListApplicationComponents)

`list-application-components` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `applicationComponentInfos`

## Synopsis

```
list-application-components
[--application-component-criteria <value>]
[--filter-value <value>]
[--group-id-filter <value>]
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

`--application-component-criteria` (string)

Criteria for filtering the list of application components.

Possible values:

- `NOT_DEFINED`
- `APP_NAME`
- `SERVER_ID`
- `APP_TYPE`
- `STRATEGY`
- `DESTINATION`
- `ANALYSIS_STATUS`
- `ERROR_CATEGORY`

`--filter-value` (string)

Specify the value based on the application component criteria type. For example, if `applicationComponentCriteria` is set to `SERVER_ID` and `filterValue` is set to `server1` , then  ListApplicationComponents returns all the application components running on server1.

`--group-id-filter` (list)

The group ID specified in to filter on.

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

applicationComponentInfos -> (list)

The list of application components with detailed information about each component.

(structure)

Contains detailed information about an application component.

analysisStatus -> (string)

The status of analysis, if the application component has source code or an associated database.

antipatternReportS3Object -> (structure)

The S3 bucket name and the Amazon S3 key name for the anti-pattern report.

s3Bucket -> (string)

The S3 bucket name.

s3key -> (string)

The Amazon S3 key name.

antipatternReportStatus -> (string)

The status of the anti-pattern report generation.

antipatternReportStatusMessage -> (string)

The status message for the anti-pattern.

appType -> (string)

The type of application component.

appUnitError -> (structure)

The error in the analysis of the source code or database.

appUnitErrorCategory -> (string)

The category of the error.

associatedServerId -> (string)

The ID of the server that the application component is running on.

databaseConfigDetail -> (structure)

Configuration details for the database associated with the application component.

secretName -> (string)

AWS Secrets Manager key that holds the credentials that you use to connect to a database.

id -> (string)

The ID of the application component.

inclusionStatus -> (string)

Indicates whether the application component has been included for server recommendation or not.

lastAnalyzedTimestamp -> (timestamp)

The timestamp of when the application component was assessed.

listAntipatternSeveritySummary -> (list)

A list of anti-pattern severity summaries.

(structure)

Contains the summary of anti-patterns and their severity.

count -> (integer)

Contains the count of anti-patterns.

severity -> (string)

Contains the severity of anti-patterns.

moreServerAssociationExists -> (boolean)

Set to true if the application component is running on multiple servers.

name -> (string)

The name of application component.

osDriver -> (string)

OS driver.

osVersion -> (string)

OS version.

recommendationSet -> (structure)

The top recommendation set for the application component.

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

resourceSubType -> (string)

The application component subtype.

resultList -> (list)

A list of the analysis results.

(structure)

The error in server analysis.

analysisStatus -> (tagged union structure)

The error in server analysis.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `runtimeAnalysisStatus`, `srcCodeOrDbAnalysisStatus`.

runtimeAnalysisStatus -> (string)

The status of the analysis.

srcCodeOrDbAnalysisStatus -> (string)

The status of the source code or database analysis.

analysisType -> (string)

The error in server analysis.

antipatternReportResultList -> (list)

The error in server analysis.

(structure)

The anti-pattern report result.

analyzerName -> (tagged union structure)

The analyzer name.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `binaryAnalyzerName`, `runTimeAnalyzerName`, `sourceCodeAnalyzerName`.

binaryAnalyzerName -> (string)

The binary analyzer names.

runTimeAnalyzerName -> (string)

The assessment analyzer names.

sourceCodeAnalyzerName -> (string)

The source code analyzer names.

antiPatternReportS3Object -> (structure)

Contains the S3 bucket name and the Amazon S3 key name.

s3Bucket -> (string)

The S3 bucket name.

s3key -> (string)

The Amazon S3 key name.

antipatternReportStatus -> (string)

The status of the anti-pattern report generation.

antipatternReportStatusMessage -> (string)

The status message for the anti-pattern.

statusMessage -> (string)

The error in server analysis.

runtimeStatus -> (string)

The status of the application unit.

runtimeStatusMessage -> (string)

The status message for the application unit.

sourceCodeRepositories -> (list)

Details about the source code repository associated with the application component.

(structure)

Object containing source code information that is linked to an application component.

branch -> (string)

The branch of the source code.

projectName -> (string)

The name of the project.

repository -> (string)

The repository name for the source code.

versionControlType -> (string)

The type of repository to use for the source code.

statusMessage -> (string)

A detailed description of the analysis status and any failure message.

nextToken -> (string)

The token you use to retrieve the next set of results, or null if there are no more results.