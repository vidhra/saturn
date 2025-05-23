# describe-flow-execution-recordsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-flow-execution-records.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/describe-flow-execution-records.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [appflow](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/appflow/index.html#cli-aws-appflow) ]

# describe-flow-execution-records

## Description

Fetches the execution history of the flow.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/appflow-2020-08-23/DescribeFlowExecutionRecords)

## Synopsis

```
describe-flow-execution-records
--flow-name <value>
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

`--flow-name` (string)

The specified name of the flow. Spaces are not allowed. Use underscores (_) or hyphens (-) only.

`--max-results` (integer)

Specifies the maximum number of items that should be returned in the result set. The default for `maxResults` is 20 (for all paginated API operations).

`--next-token` (string)

The pagination token for the next page of data.

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

flowExecutions -> (list)

Returns a list of all instances when this flow was run.

(structure)

Specifies information about the past flow run instances for a given flow.

executionId -> (string)

Specifies the identifier of the given flow run.

executionStatus -> (string)

Specifies the flow run status and whether it is in progress, has completed successfully, or has failed.

executionResult -> (structure)

Describes the result of the given flow run.

errorInfo -> (structure)

Provides any error message information related to the flow run.

putFailuresCount -> (long)

Specifies the failure count for the attempted flow.

executionMessage -> (string)

Specifies the error message that appears if a flow fails.

bytesProcessed -> (long)

The total number of bytes processed by the flow run.

bytesWritten -> (long)

The total number of bytes written as a result of the flow run.

recordsProcessed -> (long)

The number of records processed in the flow run.

numParallelProcesses -> (long)

The number of processes that Amazon AppFlow ran at the same time when it retrieved your data.

maxPageSize -> (long)

The maximum number of records that Amazon AppFlow receives in each page of the response from your SAP application.

startedAt -> (timestamp)

Specifies the start time of the flow run.

lastUpdatedAt -> (timestamp)

Specifies the time of the most recent update.

dataPullStartTime -> (timestamp)

The timestamp that determines the first new or updated record to be transferred in the flow run.

dataPullEndTime -> (timestamp)

The timestamp that indicates the last new or updated record to be transferred in the flow run.

metadataCatalogDetails -> (list)

Describes the metadata catalog, metadata table, and data partitions that Amazon AppFlow used for the associated flow run.

(structure)

Describes the metadata catalog, metadata table, and data partitions that Amazon AppFlow used for the associated flow run.

catalogType -> (string)

The type of metadata catalog that Amazon AppFlow used for the associated flow run. This parameter returns the following value:

GLUE

The metadata catalog is provided by the Glue Data Catalog. Glue includes the Glue Data Catalog as a component.

tableName -> (string)

The name of the table that stores the metadata for the associated flow run. The table stores metadata that represents the data that the flow transferred. Amazon AppFlow stores the table in the metadata catalog.

tableRegistrationOutput -> (structure)

Describes the status of the attempt from Amazon AppFlow to register the metadata table with the metadata catalog. Amazon AppFlow creates or updates this table for the associated flow run.

message -> (string)

Explains the status of the registration attempt from Amazon AppFlow. If the attempt fails, the message explains why.

result -> (string)

Indicates the number of resources that Amazon AppFlow created or updated. Possible resources include metadata tables and data partitions.

status -> (string)

Indicates the status of the registration attempt from Amazon AppFlow.

partitionRegistrationOutput -> (structure)

Describes the status of the attempt from Amazon AppFlow to register the data partitions with the metadata catalog. The data partitions organize the flow output into a hierarchical path, such as a folder path in an S3 bucket. Amazon AppFlow creates the partitions (if they donât already exist) based on your flow configuration.

message -> (string)

Explains the status of the registration attempt from Amazon AppFlow. If the attempt fails, the message explains why.

result -> (string)

Indicates the number of resources that Amazon AppFlow created or updated. Possible resources include metadata tables and data partitions.

status -> (string)

Indicates the status of the registration attempt from Amazon AppFlow.

nextToken -> (string)

The pagination token for the next page of data.