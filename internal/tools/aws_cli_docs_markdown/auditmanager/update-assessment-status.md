# update-assessment-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/update-assessment-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [auditmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html#cli-aws-auditmanager) ]

# update-assessment-status

## Description

Updates the status of an assessment in Audit Manager.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/auditmanager-2017-07-25/UpdateAssessmentStatus)

## Synopsis

```
update-assessment-status
--assessment-id <value>
--status <value>
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

`--assessment-id` (string)

The unique identifier for the assessment.

`--status` (string)

The current status of the assessment.

Possible values:

- `ACTIVE`
- `INACTIVE`

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

assessment -> (structure)

The name of the updated assessment that the `UpdateAssessmentStatus` API returned.

arn -> (string)

The Amazon Resource Name (ARN) of the assessment.

awsAccount -> (structure)

The Amazon Web Services account thatâs associated with the assessment.

id -> (string)

The identifier for the Amazon Web Services account.

emailAddress -> (string)

The email address thatâs associated with the Amazon Web Services account.

name -> (string)

The name of the Amazon Web Services account.

metadata -> (structure)

The metadata for the assessment.

name -> (string)

The name of the assessment.

id -> (string)

The unique identifier for the assessment.

description -> (string)

The description of the assessment.

complianceType -> (string)

The name of the compliance standard thatâs related to the assessment, such as PCI-DSS.

status -> (string)

The overall status of the assessment.

assessmentReportsDestination -> (structure)

The destination that evidence reports are stored in for the assessment.

destinationType -> (string)

The destination type, such as Amazon S3.

destination -> (string)

The destination bucket where Audit Manager stores assessment reports.

scope -> (structure)

The wrapper of Amazon Web Services accounts and services that are in scope for the assessment.

awsAccounts -> (list)

The Amazon Web Services accounts that are included in the scope of the assessment.

(structure)

The wrapper of Amazon Web Services account details, such as account ID or email address.

id -> (string)

The identifier for the Amazon Web Services account.

emailAddress -> (string)

The email address thatâs associated with the Amazon Web Services account.

name -> (string)

The name of the Amazon Web Services account.

awsServices -> (list)

The Amazon Web Services services that are included in the scope of the assessment.

### Warning

This API parameter is no longer supported. If you use this parameter to specify one or more Amazon Web Services, Audit Manager ignores this input. Instead, the value for `awsServices` will show as empty.

(structure)

An Amazon Web Service such as Amazon S3 or CloudTrail.

For an example of how to find an Amazon Web Service name and how to define it in your assessment scope, see the following:

- [Finding an Amazon Web Service name to use in your assessment scope](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetServicesInScope.html#API_GetServicesInScope_Example_2)
- [Defining an Amazon Web Service name in your assessment scope](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetServicesInScope.html#API_GetServicesInScope_Example_3)

serviceName -> (string)

The name of the Amazon Web Service.

roles -> (list)

The roles that are associated with the assessment.

(structure)

The wrapper that contains the Audit Manager role information of the current user. This includes the role type and IAM Amazon Resource Name (ARN).

roleType -> (string)

The type of customer persona.

### Note

In `CreateAssessment` , `roleType` can only be `PROCESS_OWNER` .

In `UpdateSettings` , `roleType` can only be `PROCESS_OWNER` .

In `BatchCreateDelegationByAssessment` , `roleType` can only be `RESOURCE_OWNER` .

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role.

delegations -> (list)

The delegations that are associated with the assessment.

(structure)

The assignment of a control set to a delegate for review.

id -> (string)

The unique identifier for the delegation.

assessmentName -> (string)

The name of the assessment thatâs associated with the delegation.

assessmentId -> (string)

The identifier for the assessment thatâs associated with the delegation.

status -> (string)

The status of the delegation.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role.

roleType -> (string)

The type of customer persona.

### Note

In `CreateAssessment` , `roleType` can only be `PROCESS_OWNER` .

In `UpdateSettings` , `roleType` can only be `PROCESS_OWNER` .

In `BatchCreateDelegationByAssessment` , `roleType` can only be `RESOURCE_OWNER` .

creationTime -> (timestamp)

Specifies when the delegation was created.

lastUpdated -> (timestamp)

Specifies when the delegation was last updated.

controlSetId -> (string)

The identifier for the control set thatâs associated with the delegation.

comment -> (string)

The comment thatâs related to the delegation.

createdBy -> (string)

The user or role that created the delegation.

creationTime -> (timestamp)

Specifies when the assessment was created.

lastUpdated -> (timestamp)

The time of the most recent update.

framework -> (structure)

The framework that the assessment was created from.

id -> (string)

The unique identifier for the framework.

arn -> (string)

The Amazon Resource Name (ARN) of the framework.

metadata -> (structure)

The metadata of a framework, such as the name, ID, or description.

name -> (string)

The name of the framework.

description -> (string)

The description of the framework.

logo -> (string)

The logo thatâs associated with the framework.

complianceType -> (string)

The compliance standard thatâs associated with the framework. For example, this could be PCI DSS or HIPAA.

controlSets -> (list)

The control sets that are associated with the framework.

(structure)

Represents a set of controls in an Audit Manager assessment.

id -> (string)

The identifier of the control set in the assessment. This is the control set name in a plain string format.

description -> (string)

The description for the control set.

status -> (string)

The current status of the control set.

roles -> (list)

The roles that are associated with the control set.

(structure)

The wrapper that contains the Audit Manager role information of the current user. This includes the role type and IAM Amazon Resource Name (ARN).

roleType -> (string)

The type of customer persona.

### Note

In `CreateAssessment` , `roleType` can only be `PROCESS_OWNER` .

In `UpdateSettings` , `roleType` can only be `PROCESS_OWNER` .

In `BatchCreateDelegationByAssessment` , `roleType` can only be `RESOURCE_OWNER` .

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role.

controls -> (list)

The list of controls thatâs contained with the control set.

(structure)

The control entity that represents a standard control or a custom control in an Audit Manager assessment.

id -> (string)

The identifier for the control.

name -> (string)

The name of the control.

description -> (string)

The description of the control.

status -> (string)

The status of the control.

response -> (string)

The response of the control.

comments -> (list)

The list of comments thatâs attached to the control.

(structure)

A comment thatâs posted by a user on a control. This includes the authorâs name, the comment text, and a timestamp.

authorName -> (string)

The name of the user who authored the comment.

commentBody -> (string)

The body text of a control comment.

postedDate -> (timestamp)

The time when the comment was posted.

evidenceSources -> (list)

The list of data sources for the evidence.

(string)

evidenceCount -> (integer)

The amount of evidence thatâs collected for the control.

assessmentReportEvidenceCount -> (integer)

The amount of evidence in the assessment report.

delegations -> (list)

The delegations that are associated with the control set.

(structure)

The assignment of a control set to a delegate for review.

id -> (string)

The unique identifier for the delegation.

assessmentName -> (string)

The name of the assessment thatâs associated with the delegation.

assessmentId -> (string)

The identifier for the assessment thatâs associated with the delegation.

status -> (string)

The status of the delegation.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role.

roleType -> (string)

The type of customer persona.

### Note

In `CreateAssessment` , `roleType` can only be `PROCESS_OWNER` .

In `UpdateSettings` , `roleType` can only be `PROCESS_OWNER` .

In `BatchCreateDelegationByAssessment` , `roleType` can only be `RESOURCE_OWNER` .

creationTime -> (timestamp)

Specifies when the delegation was created.

lastUpdated -> (timestamp)

Specifies when the delegation was last updated.

controlSetId -> (string)

The identifier for the control set thatâs associated with the delegation.

comment -> (string)

The comment thatâs related to the delegation.

createdBy -> (string)

The user or role that created the delegation.

systemEvidenceCount -> (integer)

The total number of evidence objects that are retrieved automatically for the control set.

manualEvidenceCount -> (integer)

The total number of evidence objects that are uploaded manually to the control set.

tags -> (map)

The tags that are associated with the assessment.

key -> (string)

value -> (string)