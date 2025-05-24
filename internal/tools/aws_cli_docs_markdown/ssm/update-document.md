# update-documentÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/update-document.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# update-document

## Description

Updates one or more values for an SSM document.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/UpdateDocument)

## Synopsis

```
update-document
--content <value>
[--attachments <value>]
--name <value>
[--display-name <value>]
[--version-name <value>]
[--document-version <value>]
[--document-format <value>]
[--target-type <value>]
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

`--content` (string)

A valid JSON or YAML string.

`--attachments` (list)

A list of key-value pairs that describe attachments to a version of a document.

(structure)

Identifying information about a document attachment, including the file name and a key-value pair that identifies the location of an attachment to a document.

Key -> (string)

The key of a key-value pair that identifies the location of an attachment to a document.

Values -> (list)

The value of a key-value pair that identifies the location of an attachment to a document. The format for **Value** depends on the type of key you specify.

- For the key *SourceUrl* , the value is an S3 bucket location. For example:  `"Values": [ "s3://amzn-s3-demo-bucket/my-prefix" ]`
- For the key *S3FileUrl* , the value is a file in an S3 bucket. For example:  `"Values": [ "s3://amzn-s3-demo-bucket/my-prefix/my-file.py" ]`
- For the key *AttachmentReference* , the value is constructed from the name of another SSM document in your account, a version number of that document, and a file attached to that document version that you want to reuse. For example:  `"Values": [ "MyOtherDocument/3/my-other-file.py" ]`   However, if the SSM document is shared with you from another account, the full SSM document ARN must be specified instead of the document name only. For example:  `"Values": [ "arn:aws:ssm:us-east-2:111122223333:document/OtherAccountDocument/3/their-file.py" ]`

(string)

Name -> (string)

The name of the document attachment file.

Shorthand Syntax:

```
Key=string,Values=string,string,Name=string ...
```

JSON Syntax:

```
[
  {
    "Key": "SourceUrl"|"S3FileUrl"|"AttachmentReference",
    "Values": ["string", ...],
    "Name": "string"
  }
  ...
]
```

`--name` (string)

The name of the SSM document that you want to update.

`--display-name` (string)

The friendly name of the SSM document that you want to update. This value can differ for each version of the document. If you donât specify a value for this parameter in your request, the existing value is applied to the new document version.

`--version-name` (string)

An optional field specifying the version of the artifact you are updating with the document. For example, 12.6. This value is unique across all versions of a document, and canât be changed.

`--document-version` (string)

The version of the document that you want to update. Currently, Systems Manager supports updating only the latest version of the document. You can specify the version number of the latest version or use the `$LATEST` variable.

### Note

If you change a document version for a State Manager association, Systems Manager immediately runs the association unless you previously specifed the `apply-only-at-cron-interval` parameter.

`--document-format` (string)

Specify the document format for the new document version. Systems Manager supports JSON and YAML documents. JSON is the default format.

Possible values:

- `YAML`
- `JSON`
- `TEXT`

`--target-type` (string)

Specify a new target type for the document.

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

**To create a new version of a document**

The following `update-document` example creates a new version of a document when run on a Windows computer. The document specified by `--document` must be in JSON format. Note that `file://` must be referenced followed by the path of the content file. Because of the `$` at the beginning of the `--document-version` parameter, On Windows you must surround the value with double quotes. On Linux, MacOS, or at a PowerShell prompt, you must surround the value with single quotes.

**Windows version**:

```
aws ssm update-document \
    --name "RunShellScript" \
    --content "file://RunShellScript.json" \
    --document-version "$LATEST"
```

**Linux/Mac version**:

```
aws ssm update-document \
    --name "RunShellScript" \
    --content "file://RunShellScript.json" \
    --document-version '$LATEST'
```

Output:

```
{
  "DocumentDescription": {
      "Status": "Updating",
      "Hash": "f775e5df4904c6fa46686c4722fae9de1950dace25cd9608ff8d622046b68d9b",
      "Name": "RunShellScript",
      "Parameters": [
          {
              "Type": "StringList",
              "Name": "commands",
              "Description": "(Required) Specify a shell script or a command to run."
          }
      ],
      "DocumentType": "Command",
      "PlatformTypes": [
          "Linux"
      ],
      "DocumentVersion": "2",
      "HashType": "Sha256",
      "CreatedDate": 1487899655.152,
      "Owner": "809632081692",
      "SchemaVersion": "2.0",
      "DefaultVersion": "1",
      "LatestVersion": "2",
      "Description": "Run an updated script"
  }
}
```

## Output

DocumentDescription -> (structure)

A description of the document that was updated.

Sha1 -> (string)

The SHA1 hash of the document, which you can use for verification.

Hash -> (string)

The Sha256 or Sha1 hash created by the system when the document was created.

### Note

Sha1 hashes have been deprecated.

HashType -> (string)

The hash type of the document. Valid values include `Sha256` or `Sha1` .

### Note

Sha1 hashes have been deprecated.

Name -> (string)

The name of the SSM document.

DisplayName -> (string)

The friendly name of the SSM document. This value can differ for each version of the document. If you want to update this value, see  UpdateDocument .

VersionName -> (string)

The version of the artifact associated with the document.

Owner -> (string)

The Amazon Web Services user that created the document.

CreatedDate -> (timestamp)

The date when the document was created.

Status -> (string)

The status of the SSM document.

StatusInformation -> (string)

A message returned by Amazon Web Services Systems Manager that explains the `Status` value. For example, a `Failed` status might be explained by the `StatusInformation` message, âThe specified S3 bucket doesnât exist. Verify that the URL of the S3 bucket is correct.â

DocumentVersion -> (string)

The document version.

Description -> (string)

A description of the document.

Parameters -> (list)

A description of the parameters for a document.

(structure)

Parameters specified in a Systems Manager document that run on the server when the command is run.

Name -> (string)

The name of the parameter.

Type -> (string)

The type of parameter. The type can be either String or StringList.

Description -> (string)

A description of what the parameter does, how to use it, the default value, and whether or not the parameter is optional.

DefaultValue -> (string)

If specified, the default values for the parameters. Parameters without a default value are required. Parameters with a default value are optional.

PlatformTypes -> (list)

The list of operating system (OS) platforms compatible with this SSM document.

(string)

DocumentType -> (string)

The type of document.

SchemaVersion -> (string)

The schema version.

LatestVersion -> (string)

The latest version of the document.

DefaultVersion -> (string)

The default version.

DocumentFormat -> (string)

The document format, either JSON or YAML.

TargetType -> (string)

The target type which defines the kinds of resources the document can run on. For example, `/AWS::EC2::Instance` . For a list of valid resource types, see [Amazon Web Services resource and property types reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html) in the *CloudFormation User Guide* .

Tags -> (list)

The tags, or metadata, that have been applied to the document.

(structure)

Metadata that you assign to your Amazon Web Services resources. Tags enable you to categorize your resources in different ways, for example, by purpose, owner, or environment. In Amazon Web Services Systems Manager, you can apply tags to Systems Manager documents (SSM documents), managed nodes, maintenance windows, parameters, patch baselines, OpsItems, and OpsMetadata.

Key -> (string)

The name of the tag.

Value -> (string)

The value of the tag.

AttachmentsInformation -> (list)

Details about the document attachments, including names, locations, sizes, and so on.

(structure)

An attribute of an attachment, such as the attachment name.

Name -> (string)

The name of the attachment.

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

Author -> (string)

The user in your organization who created the document.

ReviewInformation -> (list)

Details about the review of a document.

(structure)

Information about the result of a document review request.

ReviewedTime -> (timestamp)

The time that the reviewer took action on the document review request.

Status -> (string)

The current status of the document review request.

Reviewer -> (string)

The reviewer assigned to take action on the document review request.

ApprovedVersion -> (string)

The version of the document currently approved for use in the organization.

PendingReviewVersion -> (string)

The version of the document that is currently under review.

ReviewStatus -> (string)

The current status of the review.

Category -> (list)

The classification of a document to help you identify and categorize its use.

(string)

CategoryEnum -> (list)

The value that identifies a documentâs category.

(string)