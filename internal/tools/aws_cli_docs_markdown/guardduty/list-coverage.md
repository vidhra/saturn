# list-coverageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-coverage.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/list-coverage.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [guardduty](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/guardduty/index.html#cli-aws-guardduty) ]

# list-coverage

## Description

Lists coverage details for your GuardDuty account. If youâre a GuardDuty administrator, you can retrieve all resources associated with the active member accounts in your organization.

Make sure the accounts have Runtime Monitoring enabled and GuardDuty agent running on their resources.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/guardduty-2017-11-28/ListCoverage)

`list-coverage` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Resources`

## Synopsis

```
list-coverage
--detector-id <value>
[--filter-criteria <value>]
[--sort-criteria <value>]
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

`--detector-id` (string)

The unique ID of the detector whose coverage details you want to retrieve.

To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

`--filter-criteria` (structure)

Represents the criteria used to filter the coverage details.

FilterCriterion -> (list)

Represents a condition that when matched will be added to the response of the operation.

(structure)

Represents a condition that when matched will be added to the response of the operation.

CriterionKey -> (string)

An enum value representing possible filter fields.

### Note

Replace the enum value `CLUSTER_NAME` with `EKS_CLUSTER_NAME` . `CLUSTER_NAME` has been deprecated.

FilterCondition -> (structure)

Contains information about the condition.

Equals -> (list)

Represents an equal condition that is applied to a single field while retrieving the coverage details.

(string)

NotEquals -> (list)

Represents a not equal condition that is applied to a single field while retrieving the coverage details.

(string)

JSON Syntax:

```
{
  "FilterCriterion": [
    {
      "CriterionKey": "ACCOUNT_ID"|"CLUSTER_NAME"|"RESOURCE_TYPE"|"COVERAGE_STATUS"|"ADDON_VERSION"|"MANAGEMENT_TYPE"|"EKS_CLUSTER_NAME"|"ECS_CLUSTER_NAME"|"AGENT_VERSION"|"INSTANCE_ID"|"CLUSTER_ARN",
      "FilterCondition": {
        "Equals": ["string", ...],
        "NotEquals": ["string", ...]
      }
    }
    ...
  ]
}
```

`--sort-criteria` (structure)

Represents the criteria used to sort the coverage details.

AttributeName -> (string)

Represents the field name used to sort the coverage details.

### Note

Replace the enum value `CLUSTER_NAME` with `EKS_CLUSTER_NAME` . `CLUSTER_NAME` has been deprecated.

OrderBy -> (string)

The order in which the sorted findings are to be displayed.

Shorthand Syntax:

```
AttributeName=string,OrderBy=string
```

JSON Syntax:

```
{
  "AttributeName": "ACCOUNT_ID"|"CLUSTER_NAME"|"COVERAGE_STATUS"|"ISSUE"|"ADDON_VERSION"|"UPDATED_AT"|"EKS_CLUSTER_NAME"|"ECS_CLUSTER_NAME"|"INSTANCE_ID",
  "OrderBy": "ASC"|"DESC"
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

Resources -> (list)

A list of resources and their attributes providing cluster details.

(structure)

Information about the resource of the GuardDuty account.

ResourceId -> (string)

The unique ID of the resource.

DetectorId -> (string)

The unique ID of the GuardDuty detector associated with the resource.

AccountId -> (string)

The unique ID of the Amazon Web Services account.

ResourceDetails -> (structure)

Information about the resource for which the coverage statistics are retrieved.

EksClusterDetails -> (structure)

EKS cluster details involved in the coverage statistics.

ClusterName -> (string)

Name of the EKS cluster.

CoveredNodes -> (long)

Represents the nodes within the EKS cluster that have a `HEALTHY` coverage status.

CompatibleNodes -> (long)

Represents all the nodes within the EKS cluster in your account.

AddonDetails -> (structure)

Information about the installed EKS add-on.

AddonVersion -> (string)

Version of the installed EKS add-on.

AddonStatus -> (string)

Status of the installed EKS add-on.

ManagementType -> (string)

Indicates how the Amazon EKS add-on GuardDuty agent is managed for this EKS cluster.

`AUTO_MANAGED` indicates GuardDuty deploys and manages updates for this resource.

`MANUAL` indicates that you are responsible to deploy, update, and manage the Amazon EKS add-on GuardDuty agent for this resource.

ResourceType -> (string)

The type of Amazon Web Services resource.

EcsClusterDetails -> (structure)

Information about the Amazon ECS cluster that is assessed for runtime coverage.

ClusterName -> (string)

The name of the Amazon ECS cluster.

FargateDetails -> (structure)

Information about the Fargate details associated with the Amazon ECS cluster.

Issues -> (list)

Runtime coverage issues identified for the resource running on Amazon Web Services Fargate.

(string)

ManagementType -> (string)

Indicates how the GuardDuty security agent is managed for this resource.

- `AUTO_MANAGED` indicates that GuardDuty deploys and manages updates for this resource.
- `DISABLED` indicates that the deployment of the GuardDuty security agent is disabled for this resource.

### Note

The `MANUAL` status doesnât apply to the Amazon Web Services Fargate (Amazon ECS only) woprkloads.

ContainerInstanceDetails -> (structure)

Information about the Amazon ECS container running on Amazon EC2 instance.

CoveredContainerInstances -> (long)

Represents the nodes in the Amazon ECS cluster that has a `HEALTHY` coverage status.

CompatibleContainerInstances -> (long)

Represents total number of nodes in the Amazon ECS cluster.

Ec2InstanceDetails -> (structure)

Information about the Amazon EC2 instance assessed for runtime coverage.

InstanceId -> (string)

The Amazon EC2 instance ID.

InstanceType -> (string)

The instance type of the Amazon EC2 instance.

ClusterArn -> (string)

The cluster ARN of the Amazon ECS cluster running on the Amazon EC2 instance.

AgentDetails -> (structure)

Information about the installed security agent.

Version -> (string)

Version of the installed GuardDuty security agent.

ManagementType -> (string)

Indicates how the GuardDuty security agent is managed for this resource.

- `AUTO_MANAGED` indicates that GuardDuty deploys and manages updates for this resource.
- `MANUAL` indicates that you are responsible to deploy, update, and manage the GuardDuty security agent updates for this resource.

### Note

The `DISABLED` status doesnât apply to Amazon EC2 instances and Amazon EKS clusters.

CoverageStatus -> (string)

Represents the status of the EKS cluster coverage.

Issue -> (string)

Represents the reason why a coverage status was `UNHEALTHY` for the EKS cluster.

UpdatedAt -> (timestamp)

The timestamp at which the coverage details for the resource were last updated. This is in UTC format.

NextToken -> (string)

The pagination parameter to be used on the next list operation to retrieve more items.