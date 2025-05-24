# list-compute-quotasÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-compute-quotas.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/list-compute-quotas.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# list-compute-quotas

## Description

List the resource allocation definitions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/ListComputeQuotas)

`list-compute-quotas` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ComputeQuotaSummaries`

## Synopsis

```
list-compute-quotas
[--created-after <value>]
[--created-before <value>]
[--name-contains <value>]
[--status <value>]
[--cluster-arn <value>]
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

Filter for after this creation time. The input for this parameter is a Unix timestamp. To convert a date and time into a Unix timestamp, see [EpochConverter](https://www.epochconverter.com/) .

`--created-before` (timestamp)

Filter for before this creation time. The input for this parameter is a Unix timestamp. To convert a date and time into a Unix timestamp, see [EpochConverter](https://www.epochconverter.com/) .

`--name-contains` (string)

Filter for name containing this string.

`--status` (string)

Filter for status.

Possible values:

- `Creating`
- `CreateFailed`
- `CreateRollbackFailed`
- `Created`
- `Updating`
- `UpdateFailed`
- `UpdateRollbackFailed`
- `Updated`
- `Deleting`
- `DeleteFailed`
- `DeleteRollbackFailed`
- `Deleted`

`--cluster-arn` (string)

Filter for ARN of the cluster.

`--sort-by` (string)

Filter for sorting the list by a given value. For example, sort by name, creation time, or status.

Possible values:

- `Name`
- `CreationTime`
- `Status`
- `ClusterArn`

`--sort-order` (string)

The order of the list. By default, listed in `Descending` order according to by `SortBy` . To change the list order, you can specify `SortOrder` to be `Ascending` .

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

ComputeQuotaSummaries -> (list)

Summaries of the compute allocation definitions.

(structure)

Summary of the compute allocation definition.

ComputeQuotaArn -> (string)

ARN of the compute allocation definition.

ComputeQuotaId -> (string)

ID of the compute allocation definition.

Name -> (string)

Name of the compute allocation definition.

ComputeQuotaVersion -> (integer)

Version of the compute allocation definition.

Status -> (string)

Status of the compute allocation definition.

ClusterArn -> (string)

ARN of the cluster.

ComputeQuotaConfig -> (structure)

Configuration of the compute allocation definition. This includes the resource sharing option, and the setting to preempt low priority tasks.

ComputeQuotaResources -> (list)

Allocate compute resources by instance types.

(structure)

Configuration of the resources used for the compute allocation definition.

InstanceType -> (string)

The instance type of the instance group for the cluster.

Count -> (integer)

The number of instances to add to the instance group of a SageMaker HyperPod cluster.

ResourceSharingConfig -> (structure)

Resource sharing configuration. This defines how an entity can lend and borrow idle compute with other entities within the cluster.

Strategy -> (string)

The strategy of how idle compute is shared within the cluster. The following are the options of strategies.

- `DontLend` : entities do not lend idle compute.
- `Lend` : entities can lend idle compute to entities that can borrow.
- `LendandBorrow` : entities can lend idle compute and borrow idle compute from other entities.

Default is `LendandBorrow` .

BorrowLimit -> (integer)

The limit on how much idle compute can be borrowed.The values can be 1 - 500 percent of idle compute that the team is allowed to borrow.

Default is `50` .

PreemptTeamTasks -> (string)

Allows workloads from within an entity to preempt same-team workloads. When set to `LowerPriority` , the entityâs lower priority tasks are preempted by their own higher priority tasks.

Default is `LowerPriority` .

ComputeQuotaTarget -> (structure)

The target entity to allocate compute resources to.

TeamName -> (string)

Name of the team to allocate compute resources to.

FairShareWeight -> (integer)

Assigned entity fair-share weight. Idle compute will be shared across entities based on these assigned weights. This weight is only used when `FairShare` is enabled.

A weight of 0 is the lowest priority and 100 is the highest. Weight 0 is the default.

ActivationState -> (string)

The state of the compute allocation being described. Use to enable or disable compute allocation.

Default is `Enabled` .

CreationTime -> (timestamp)

Creation time of the compute allocation definition.

LastModifiedTime -> (timestamp)

Last modified time of the compute allocation definition.

NextToken -> (string)

If the previous response was truncated, you will receive this token. Use it in your next request to receive the next set of results.