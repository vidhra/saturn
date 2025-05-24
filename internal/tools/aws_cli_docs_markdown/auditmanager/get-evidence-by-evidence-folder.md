# get-evidence-by-evidence-folderÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-evidence-by-evidence-folder.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/get-evidence-by-evidence-folder.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [auditmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html#cli-aws-auditmanager) ]

# get-evidence-by-evidence-folder

## Description

Gets all evidence from a specified evidence folder in Audit Manager.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/auditmanager-2017-07-25/GetEvidenceByEvidenceFolder)

## Synopsis

```
get-evidence-by-evidence-folder
--assessment-id <value>
--control-set-id <value>
--evidence-folder-id <value>
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

`--evidence-folder-id` (string)

The unique identifier for the folder that the evidence is stored in.

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

evidence -> (list)

The list of evidence that the `GetEvidenceByEvidenceFolder` API returned.

(structure)

A record that contains the information needed to demonstrate compliance with the requirements specified by a control. Examples of evidence include change activity invoked by a user, or a system configuration snapshot.

dataSource -> (string)

The data source where the evidence was collected from.

evidenceAwsAccountId -> (string)

The identifier for the Amazon Web Services account.

time -> (timestamp)

The timestamp that represents when the evidence was collected.

eventSource -> (string)

The Amazon Web Service that the evidence is collected from.

eventName -> (string)

The name of the evidence event.

evidenceByType -> (string)

The type of automated evidence.

resourcesIncluded -> (list)

The list of resources that are assessed to generate the evidence.

(structure)

A system asset thatâs evaluated in an Audit Manager assessment.

arn -> (string)

The Amazon Resource Name (ARN) for the resource.

value -> (string)

The value of the resource.

complianceCheck -> (string)

The evaluation status for a resource that was assessed when collecting compliance check evidence.

- Audit Manager classes the resource as non-compliant if Security Hub reports a *Fail* result, or if Config reports a *Non-compliant* result.
- Audit Manager classes the resource as compliant if Security Hub reports a *Pass* result, or if Config reports a *Compliant* result.
- If a compliance check isnât available or applicable, then no compliance evaluation can be made for that resource. This is the case if a resource assessment uses Config or Security Hub as the underlying data source type, but those services arenât enabled. This is also the case if the resource assessment uses an underlying data source type that doesnât support compliance checks (such as manual evidence, Amazon Web Services API calls, or CloudTrail).

attributes -> (map)

The names and values that are used by the evidence event. This includes an attribute name (such as `allowUsersToChangePassword` ) and value (such as `true` or `false` ).

key -> (string)

value -> (string)

iamId -> (string)

The unique identifier for the user or role thatâs associated with the evidence.

complianceCheck -> (string)

The evaluation status for automated evidence that falls under the compliance check category.

- Audit Manager classes evidence as non-compliant if Security Hub reports a *Fail* result, or if Config reports a *Non-compliant* result.
- Audit Manager classes evidence as compliant if Security Hub reports a *Pass* result, or if Config reports a *Compliant* result.
- If a compliance check isnât available or applicable, then no compliance evaluation can be made for that evidence. This is the case if the evidence uses Config or Security Hub as the underlying data source type, but those services arenât enabled. This is also the case if the evidence uses an underlying data source type that doesnât support compliance checks (such as manual evidence, Amazon Web Services API calls, or CloudTrail).

awsOrganization -> (string)

The Amazon Web Services account that the evidence is collected from, and its organization path.

awsAccountId -> (string)

The identifier for the Amazon Web Services account.

evidenceFolderId -> (string)

The identifier for the folder that the evidence is stored in.

id -> (string)

The identifier for the evidence.

assessmentReportSelection -> (string)

Specifies whether the evidence is included in the assessment report.

nextToken -> (string)

The pagination token thatâs used to fetch the next set of results.