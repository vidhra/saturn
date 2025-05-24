# list-assessmentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-assessments.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [auditmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html#cli-aws-auditmanager) ]

# list-assessments

## Description

Returns a list of current and past assessments from Audit Manager.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/auditmanager-2017-07-25/ListAssessments)

## Synopsis

```
list-assessments
[--status <value>]
[--next-token <value>]
[--max-results <value>]
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

`--status` (string)

The current status of the assessment.

Possible values:

- `ACTIVE`
- `INACTIVE`

`--next-token` (string)

The pagination token thatâs used to fetch the next set of results.

`--max-results` (integer)

Represents the maximum number of results on a page or for an API request call.

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

assessmentMetadata -> (list)

The metadata that the `ListAssessments` API returns for each assessment.

(structure)

A metadata object thatâs associated with an assessment in Audit Manager.

name -> (string)

The name of the assessment.

id -> (string)

The unique identifier for the assessment.

complianceType -> (string)

The name of the compliance standard thatâs related to the assessment, such as PCI-DSS.

status -> (string)

The current status of the assessment.

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

nextToken -> (string)

The pagination token thatâs used to fetch the next set of results.