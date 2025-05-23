# update-workloadÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/update-workload.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/update-workload.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wellarchitected](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wellarchitected/index.html#cli-aws-wellarchitected) ]

# update-workload

## Description

Update an existing workload.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wellarchitected-2020-03-31/UpdateWorkload)

## Synopsis

```
update-workload
--workload-id <value>
[--workload-name <value>]
[--description <value>]
[--environment <value>]
[--account-ids <value>]
[--aws-regions <value>]
[--non-aws-regions <value>]
[--pillar-priorities <value>]
[--architectural-design <value>]
[--review-owner <value>]
[--is-review-owner-update-acknowledged | --no-is-review-owner-update-acknowledged]
[--industry-type <value>]
[--industry <value>]
[--notes <value>]
[--improvement-status <value>]
[--discovery-config <value>]
[--applications <value>]
[--jira-configuration <value>]
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

`--workload-id` (string)

The ID assigned to the workload. This ID is unique within an Amazon Web Services Region.

`--workload-name` (string)

The name of the workload.

The name must be unique within an account within an Amazon Web Services Region. Spaces and capitalization are ignored when checking for uniqueness.

`--description` (string)

The description for the workload.

`--environment` (string)

The environment for the workload.

Possible values:

- `PRODUCTION`
- `PREPRODUCTION`

`--account-ids` (list)

The list of Amazon Web Services account IDs associated with the workload.

(string)

An Amazon Web Services account ID.

Syntax:

```
"string" "string" ...
```

`--aws-regions` (list)

The list of Amazon Web Services Regions associated with the workload, for example, `us-east-2` , or `ca-central-1` .

(string)

An Amazon Web Services Region, for example, `us-west-2` or `ap-northeast-1` .

Syntax:

```
"string" "string" ...
```

`--non-aws-regions` (list)

The list of non-Amazon Web Services Regions associated with the workload.

(string)

Syntax:

```
"string" "string" ...
```

`--pillar-priorities` (list)

The priorities of the pillars, which are used to order items in the improvement plan. Each pillar is represented by its  PillarReviewSummary$PillarId .

(string)

The ID used to identify a pillar, for example, `security` .

A pillar is identified by its  PillarReviewSummary$PillarId .

Syntax:

```
"string" "string" ...
```

`--architectural-design` (string)

The URL of the architectural design for the workload.

`--review-owner` (string)

The review owner of the workload. The name, email address, or identifier for the primary group or individual that owns the workload review process.

`--is-review-owner-update-acknowledged` | `--no-is-review-owner-update-acknowledged` (boolean)

Flag indicating whether the workload owner has acknowledged that the *Review owner* field is required.

If a **Review owner** is not added to the workload within 60 days of acknowledgement, access to the workload is restricted until an owner is added.

`--industry-type` (string)

The industry type for the workload.

If specified, must be one of the following:

- `Agriculture`
- `Automobile`
- `Defense`
- `Design and Engineering`
- `Digital Advertising`
- `Education`
- `Environmental Protection`
- `Financial Services`
- `Gaming`
- `General Public Services`
- `Healthcare`
- `Hospitality`
- `InfoTech`
- `Justice and Public Safety`
- `Life Sciences`
- `Manufacturing`
- `Media & Entertainment`
- `Mining & Resources`
- `Oil & Gas`
- `Power & Utilities`
- `Professional Services`
- `Real Estate & Construction`
- `Retail & Wholesale`
- `Social Protection`
- `Telecommunications`
- `Travel, Transportation & Logistics`
- `Other`

`--industry` (string)

The industry for the workload.

`--notes` (string)

The notes associated with the workload.

For a review template, these are the notes that will be associated with the workload when the template is applied.

`--improvement-status` (string)

The improvement status for a workload.

Possible values:

- `NOT_APPLICABLE`
- `NOT_STARTED`
- `IN_PROGRESS`
- `COMPLETE`
- `RISK_ACKNOWLEDGED`

`--discovery-config` (structure)

Well-Architected discovery configuration settings to associate to the workload.

TrustedAdvisorIntegrationStatus -> (string)

Discovery integration status in respect to Trusted Advisor for the workload.

WorkloadResourceDefinition -> (list)

The mode to use for identifying resources associated with the workload.

You can specify `WORKLOAD_METADATA` , `APP_REGISTRY` , or both.

(string)

Shorthand Syntax:

```
TrustedAdvisorIntegrationStatus=string,WorkloadResourceDefinition=string,string
```

JSON Syntax:

```
{
  "TrustedAdvisorIntegrationStatus": "ENABLED"|"DISABLED",
  "WorkloadResourceDefinition": ["WORKLOAD_METADATA"|"APP_REGISTRY", ...]
}
```

`--applications` (list)

List of AppRegistry application ARNs to associate to the workload.

(string)

Syntax:

```
"string" "string" ...
```

`--jira-configuration` (structure)

Configuration of the Jira integration.

IssueManagementStatus -> (string)

Workload-level: Jira issue management status.

IssueManagementType -> (string)

Workload-level: Jira issue management type.

JiraProjectKey -> (string)

Workload-level: Jira project key to sync workloads to.

Shorthand Syntax:

```
IssueManagementStatus=string,IssueManagementType=string,JiraProjectKey=string
```

JSON Syntax:

```
{
  "IssueManagementStatus": "ENABLED"|"DISABLED"|"INHERIT",
  "IssueManagementType": "AUTO"|"MANUAL",
  "JiraProjectKey": "string"
}
```

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

Workload -> (structure)

A workload return object.

WorkloadId -> (string)

The ID assigned to the workload. This ID is unique within an Amazon Web Services Region.

WorkloadArn -> (string)

The ARN for the workload.

WorkloadName -> (string)

The name of the workload.

The name must be unique within an account within an Amazon Web Services Region. Spaces and capitalization are ignored when checking for uniqueness.

Description -> (string)

The description for the workload.

Environment -> (string)

The environment for the workload.

UpdatedAt -> (timestamp)

The date and time recorded.

AccountIds -> (list)

The list of Amazon Web Services account IDs associated with the workload.

(string)

An Amazon Web Services account ID.

AwsRegions -> (list)

The list of Amazon Web Services Regions associated with the workload, for example, `us-east-2` , or `ca-central-1` .

(string)

An Amazon Web Services Region, for example, `us-west-2` or `ap-northeast-1` .

NonAwsRegions -> (list)

The list of non-Amazon Web Services Regions associated with the workload.

(string)

ArchitecturalDesign -> (string)

The URL of the architectural design for the workload.

ReviewOwner -> (string)

The review owner of the workload. The name, email address, or identifier for the primary group or individual that owns the workload review process.

ReviewRestrictionDate -> (timestamp)

The date and time recorded.

IsReviewOwnerUpdateAcknowledged -> (boolean)

Flag indicating whether the workload owner has acknowledged that the *Review owner* field is required.

If a **Review owner** is not added to the workload within 60 days of acknowledgement, access to the workload is restricted until an owner is added.

IndustryType -> (string)

The industry type for the workload.

If specified, must be one of the following:

- `Agriculture`
- `Automobile`
- `Defense`
- `Design and Engineering`
- `Digital Advertising`
- `Education`
- `Environmental Protection`
- `Financial Services`
- `Gaming`
- `General Public Services`
- `Healthcare`
- `Hospitality`
- `InfoTech`
- `Justice and Public Safety`
- `Life Sciences`
- `Manufacturing`
- `Media & Entertainment`
- `Mining & Resources`
- `Oil & Gas`
- `Power & Utilities`
- `Professional Services`
- `Real Estate & Construction`
- `Retail & Wholesale`
- `Social Protection`
- `Telecommunications`
- `Travel, Transportation & Logistics`
- `Other`

Industry -> (string)

The industry for the workload.

Notes -> (string)

The notes associated with the workload.

For a review template, these are the notes that will be associated with the workload when the template is applied.

ImprovementStatus -> (string)

The improvement status for a workload.

RiskCounts -> (map)

A map from risk names to the count of how many questions have that rating.

key -> (string)

The risk for a given workload, lens review, pillar, or question.

value -> (integer)

A non-negative integer that denotes how many.

PillarPriorities -> (list)

The priorities of the pillars, which are used to order items in the improvement plan. Each pillar is represented by its  PillarReviewSummary$PillarId .

(string)

The ID used to identify a pillar, for example, `security` .

A pillar is identified by its  PillarReviewSummary$PillarId .

Lenses -> (list)

The list of lenses associated with the workload. Each lens is identified by its  LensSummary$LensAlias .

If a review template that specifies lenses is applied to the workload, those lenses are applied to the workload in addition to these lenses.

(string)

The alias of the lens.

For Amazon Web Services official lenses, this is either the lens alias, such as `serverless` , or the lens ARN, such as `arn:aws:wellarchitected:us-east-1::lens/serverless` . Note that some operations (such as ExportLens and CreateLensShare) are not permitted on Amazon Web Services official lenses.

For custom lenses, this is the lens ARN, such as `arn:aws:wellarchitected:us-west-2:123456789012:lens/0123456789abcdef01234567890abcdef` .

Each lens is identified by its  LensSummary$LensAlias .

Owner -> (string)

An Amazon Web Services account ID.

ShareInvitationId -> (string)

The ID assigned to the share invitation.

Tags -> (map)

The tags associated with the workload.

key -> (string)

value -> (string)

DiscoveryConfig -> (structure)

Discovery configuration associated to the workload.

TrustedAdvisorIntegrationStatus -> (string)

Discovery integration status in respect to Trusted Advisor for the workload.

WorkloadResourceDefinition -> (list)

The mode to use for identifying resources associated with the workload.

You can specify `WORKLOAD_METADATA` , `APP_REGISTRY` , or both.

(string)

Applications -> (list)

List of AppRegistry application ARNs associated to the workload.

(string)

Profiles -> (list)

Profile associated with a workload.

(structure)

The profile associated with a workload.

ProfileArn -> (string)

The profile ARN.

ProfileVersion -> (string)

The profile version.

PrioritizedRiskCounts -> (map)

A map from risk names to the count of how many questions have that rating.

key -> (string)

The risk for a given workload, lens review, pillar, or question.

value -> (integer)

A non-negative integer that denotes how many.

JiraConfiguration -> (structure)

Jira configuration for a specific workload.

IssueManagementStatus -> (string)

Workload-level: Jira issue management status.

IssueManagementType -> (string)

Workload-level: Jira issue management type.

JiraProjectKey -> (string)

Workload-level: Jira project key to sync workloads to.

StatusMessage -> (string)

Workload-level: Status message on configuration of the Jira integration.