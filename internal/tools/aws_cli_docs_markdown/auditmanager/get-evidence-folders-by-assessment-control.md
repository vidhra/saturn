# get-evidence-folders-by-assessment-controlÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-evidence-folders-by-assessment-control.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-evidence-folders-by-assessment-control.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [auditmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html#cli-aws-auditmanager) ]

# get-evidence-folders-by-assessment-control

## Description

Gets a list of evidence folders that are associated with a specified control in an Audit Manager assessment.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/auditmanager-2017-07-25/GetEvidenceFoldersByAssessmentControl)

## Synopsis

```
get-evidence-folders-by-assessment-control
--assessment-id <value>
--control-set-id <value>
--control-id <value>
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

`--assessment-id` (string)

The identifier for the assessment.

`--control-set-id` (string)

The identifier for the control set.

`--control-id` (string)

The identifier for the control.

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

evidenceFolders -> (list)

The list of evidence folders that the `GetEvidenceFoldersByAssessmentControl` API returned.

(structure)

The folder where Audit Manager stores evidence for an assessment.

name -> (string)

The name of the evidence folder.

date -> (timestamp)

The date when the first evidence was added to the evidence folder.

assessmentId -> (string)

The identifier for the assessment.

controlSetId -> (string)

The identifier for the control set.

controlId -> (string)

The unique identifier for the control.

id -> (string)

The identifier for the folder that the evidence is stored in.

dataSource -> (string)

The Amazon Web Service that the evidence was collected from.

author -> (string)

The name of the user who created the evidence folder.

totalEvidence -> (integer)

The total amount of evidence in the evidence folder.

assessmentReportSelectionCount -> (integer)

The total count of evidence thatâs included in the assessment report.

controlName -> (string)

The name of the control.

evidenceResourcesIncludedCount -> (integer)

The amount of evidence thatâs included in the evidence folder.

evidenceByTypeConfigurationDataCount -> (integer)

The number of evidence that falls under the configuration data category. This evidence is collected from configuration snapshots of other Amazon Web Services such as Amazon EC2, Amazon S3, or IAM.

evidenceByTypeManualCount -> (integer)

The number of evidence that falls under the manual category. This evidence is imported manually.

evidenceByTypeComplianceCheckCount -> (integer)

The number of evidence that falls under the compliance check category. This evidence is collected from Config or Security Hub.

evidenceByTypeComplianceCheckIssuesCount -> (integer)

The total number of issues that were reported directly from Security Hub, Config, or both.

evidenceByTypeUserActivityCount -> (integer)

The number of evidence that falls under the user activity category. This evidence is collected from CloudTrail logs.

evidenceAwsServiceSourceCount -> (integer)

The total number of Amazon Web Services resources that were assessed to generate the evidence.

nextToken -> (string)

The pagination token thatâs used to fetch the next set of results.