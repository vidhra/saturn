# batch-import-evidence-to-assessment-controlÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/batch-import-evidence-to-assessment-control.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/batch-import-evidence-to-assessment-control.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [auditmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html#cli-aws-auditmanager) ]

# batch-import-evidence-to-assessment-control

## Description

Adds one or more pieces of evidence to a control in an Audit Manager assessment.

You can import manual evidence from any S3 bucket by specifying the S3 URI of the object. You can also upload a file from your browser, or enter plain text in response to a risk assessment question.

The following restrictions apply to this action:

- `manualEvidence` can be only one of the following: `evidenceFileName` , `s3ResourcePath` , or `textResponse`
- Maximum size of an individual evidence file: 100 MB
- Number of daily manual evidence uploads per control: 100
- Supported file formats: See [Supported file types for manual evidence](https://docs.aws.amazon.com/audit-manager/latest/userguide/upload-evidence.html#supported-manual-evidence-files) in the *Audit Manager User Guide*

For more information about Audit Manager service restrictions, see [Quotas and restrictions for Audit Manager](https://docs.aws.amazon.com/audit-manager/latest/userguide/service-quotas.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/auditmanager-2017-07-25/BatchImportEvidenceToAssessmentControl)

## Synopsis

```
batch-import-evidence-to-assessment-control
--assessment-id <value>
--control-set-id <value>
--control-id <value>
--manual-evidence <value>
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

`--manual-evidence` (list)

The list of manual evidence objects.

(structure)

Evidence thatâs manually added to a control in Audit Manager. `manualEvidence` can be one of the following: `evidenceFileName` , `s3ResourcePath` , or `textResponse` .

s3ResourcePath -> (string)

The S3 URL of the object thatâs imported as manual evidence.

textResponse -> (string)

The plain text response thatâs entered and saved as manual evidence.

evidenceFileName -> (string)

The name of the file thatâs uploaded as manual evidence. This name is populated using the `evidenceFileName` value from the ` `GetEvidenceFileUploadUrl` [https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFileUploadUrl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFileUploadUrl).html`__ API response.

Shorthand Syntax:

```
s3ResourcePath=string,textResponse=string,evidenceFileName=string ...
```

JSON Syntax:

```
[
  {
    "s3ResourcePath": "string",
    "textResponse": "string",
    "evidenceFileName": "string"
  }
  ...
]
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

errors -> (list)

A list of errors that the `BatchImportEvidenceToAssessmentControl` API returned.

(structure)

An error entity for the `BatchImportEvidenceToAssessmentControl` API. This is used to provide more meaningful errors than a simple string message.

manualEvidence -> (structure)

Manual evidence that canât be collected automatically by Audit Manager.

s3ResourcePath -> (string)

The S3 URL of the object thatâs imported as manual evidence.

textResponse -> (string)

The plain text response thatâs entered and saved as manual evidence.

evidenceFileName -> (string)

The name of the file thatâs uploaded as manual evidence. This name is populated using the `evidenceFileName` value from the ` `GetEvidenceFileUploadUrl` [https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFileUploadUrl](https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_GetEvidenceFileUploadUrl).html`__ API response.

errorCode -> (string)

The error code that the `BatchImportEvidenceToAssessmentControl` API returned.

errorMessage -> (string)

The error message that the `BatchImportEvidenceToAssessmentControl` API returned.