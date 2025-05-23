# get-documentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-document.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-document.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# get-document

## Description

Gets the contents of the specified Amazon Web Services Systems Manager document (SSM document).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetDocument)

## Synopsis

```
get-document
--name <value>
[--version-name <value>]
[--document-version <value>]
[--document-format <value>]
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

`--name` (string)

The name of the SSM document.

`--version-name` (string)

An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document and canât be changed.

`--document-version` (string)

The document version for which you want information.

`--document-format` (string)

Returns the document in the specified format. The document format can be either JSON or YAML. JSON is the default format.

Possible values:

- `YAML`
- `JSON`
- `TEXT`

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To get document content**

The following `get-document` example displays the content of a Systems Manager document.

```
aws ssm get-document \
    --name "AWS-RunShellScript"
```

Output:

```
{
    "Name": "AWS-RunShellScript",
    "DocumentVersion": "1",
    "Status": "Active",
    "Content": "{\n    \"schemaVersion\":\"1.2\",\n    \"description\":\"Run a shell script or specify the commands to run.\",\n    \"parameters\":{\n        \"commands\":{\n            \"type\":\"StringList\",\n            \"description\":\"(Required) Specify a shell script or a command to run.\",\n            \"minItems\":1,\n            \"displayType\":\"textarea\"\n        },\n        \"workingDirectory\":{\n            \"type\":\"String\",\n            \"default\":\"\",\n            \"description\":\"(Optional) The path to the working directory on your instance.\",\n            \"maxChars\":4096\n        },\n        \"executionTimeout\":{\n            \"type\":\"String\",\n            \"default\":\"3600\",\n            \"description\":\"(Optional) The time in seconds for a command to complete before it is considered to have failed. Default is 3600 (1 hour). Maximum is 172800 (48 hours).\",\n            \"allowedPattern\":\"([1-9][0-9]{0,4})|(1[0-6][0-9]{4})|(17[0-1][0-9]{3})|(172[0-7][0-9]{2})|(172800)\"\n        }\n    },\n    \"runtimeConfig\":{\n        \"aws:runShellScript\":{\n            \"properties\":[\n                {\n                    \"id\":\"0.aws:runShellScript\",\n                    \"runCommand\":\"{{ commands }}\",\n                    \"workingDirectory\":\"{{ workingDirectory }}\",\n                    \"timeoutSeconds\":\"{{ executionTimeout }}\"\n                }\n            ]\n        }\n    }\n}\n",
    "DocumentType": "Command",
    "DocumentFormat": "JSON"
}
```

For more information, see [AWS Systems Manager Documents](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-ssm-docs.html) in the *AWS Systems Manager User Guide*.

## Output

Name -> (string)

The name of the SSM document.

CreatedDate -> (timestamp)

The date the SSM document was created.

DisplayName -> (string)

The friendly name of the SSM document. This value can differ for each version of the document. If you want to update this value, see  UpdateDocument .

VersionName -> (string)

The version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and canât be changed.

DocumentVersion -> (string)

The document version.

Status -> (string)

The status of the SSM document, such as `Creating` , `Active` , `Updating` , `Failed` , and `Deleting` .

StatusInformation -> (string)

A message returned by Amazon Web Services Systems Manager that explains the `Status` value. For example, a `Failed` status might be explained by the `StatusInformation` message, âThe specified S3 bucket doesnât exist. Verify that the URL of the S3 bucket is correct.â

Content -> (string)

The contents of the SSM document.

DocumentType -> (string)

The document type.

DocumentFormat -> (string)

The document format, either JSON or YAML.

Requires -> (list)

A list of SSM documents required by a document. For example, an `ApplicationConfiguration` document requires an `ApplicationConfigurationSchema` document.

(structure)

An SSM document required by the current document.

Name -> (string)

The name of the required SSM document. The name can be an Amazon Resource Name (ARN).

Version -> (string)

The document version required by the current document.

RequireType -> (string)

The document type of the required SSM document.

VersionName -> (string)

An optional field specifying the version of the artifact associated with the document. For example, 12.6. This value is unique across all versions of a document, and canât be changed.

AttachmentsContent -> (list)

A description of the document attachments, including names, locations, sizes, and so on.

(structure)

A structure that includes attributes that describe a document attachment.

Name -> (string)

The name of an attachment.

Size -> (long)

The size of an attachment in bytes.

Hash -> (string)

The cryptographic hash value of the document content.

HashType -> (string)

The hash algorithm used to calculate the hash value.

Url -> (string)

The URL location of the attachment content.

ReviewStatus -> (string)

The current review status of a new custom Systems Manager document (SSM document) created by a member of your organization, or of the latest version of an existing SSM document.

Only one version of an SSM document can be in the APPROVED state at a time. When a new version is approved, the status of the previous version changes to REJECTED.

Only one version of an SSM document can be in review, or PENDING, at a time.