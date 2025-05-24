# describe-folder-contentsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-folder-contents.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/describe-folder-contents.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workdocs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/index.html#cli-aws-workdocs) ]

# describe-folder-contents

## Description

Describes the contents of the specified folder, including its documents and subfolders.

By default, Amazon WorkDocs returns the first 100 active document and folder metadata items. If there are more results, the response includes a marker that you can use to request the next set of results. You can also request initialized documents.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/DescribeFolderContents)

`describe-folder-contents` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Folders`, `Documents`

## Synopsis

```
describe-folder-contents
[--authentication-token <value>]
--folder-id <value>
[--sort <value>]
[--order <value>]
[--type <value>]
[--include <value>]
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

`--authentication-token` (string)

Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.

`--folder-id` (string)

The ID of the folder.

`--sort` (string)

The sorting criteria.

Possible values:

- `DATE`
- `NAME`

`--order` (string)

The order for the contents of the folder.

Possible values:

- `ASCENDING`
- `DESCENDING`

`--type` (string)

The type of items.

Possible values:

- `ALL`
- `DOCUMENT`
- `FOLDER`

`--include` (string)

The contents to include. Specify âINITIALIZEDâ to include initialized documents.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To describe the contents of a folder**

This example describes all the active contents of the specified folder, including its documents and subfolders, sorted by date in ascending order.

Command:

```
aws workdocs describe-folder-contents --folder-id 1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678 --sort DATE --order ASCENDING --type ALL
```

Output:

```
{
  "Folders": [
      {
          "Id": "50893c0af679524d1a0e0651130ed6d073e1a05f95bd12c42dcde5d35634ed08",
          "Name": "testing",
          "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c",
          "ParentFolderId": "1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678",
          "CreatedTimestamp": 1534450467.622,
          "ModifiedTimestamp": 1534451113.504,
          "ResourceState": "ACTIVE",
          "Signature": "1a23456b78901c23d4ef56gh7EXAMPLE",
          "Size": 23019,
          "LatestVersionSize": 11537
      }
  ],
  "Documents": [
      {
          "Id": "d90d93c1fe44bad0c8471e973ebaab339090401a95e777cffa58e977d2983b65",
          "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c",
          "ParentFolderId": "1ece93e5fe75315c7407c4967918b4fd9da87ddb2a588e67b7fdaf4a98fde678",
          "CreatedTimestamp": 1529005196.082,
          "ModifiedTimestamp": 1534452483.01,
          "LatestVersionMetadata": {
              "Id": "1534452029587-15e129dfc187505c407588df255be83de2920d733859f1d2762411d22a83e3ef",
              "Name": "exampleDoc.docx",
              "ContentType": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
              "Size": 13922,
              "Signature": "1a23456b78901c23d4ef56gh7EXAMPLE",
              "Status": "ACTIVE",
              "CreatedTimestamp": 1534452029.587,
              "ModifiedTimestamp": 1534452029.587,
              "CreatorId": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c"
          },
          "ResourceState": "ACTIVE"
      }
  ]
}
```

## Output

Folders -> (list)

The subfolders in the specified folder.

(structure)

Describes a folder.

Id -> (string)

The ID of the folder.

Name -> (string)

The name of the folder.

CreatorId -> (string)

The ID of the creator.

ParentFolderId -> (string)

The ID of the parent folder.

CreatedTimestamp -> (timestamp)

The time when the folder was created.

ModifiedTimestamp -> (timestamp)

The time when the folder was updated.

ResourceState -> (string)

The resource state of the folder.

Signature -> (string)

The unique identifier created from the subfolders and documents of the folder.

Labels -> (list)

List of labels on the folder.

(string)

Size -> (long)

The size of the folder metadata.

LatestVersionSize -> (long)

The size of the latest version of the folder metadata.

Documents -> (list)

The documents in the specified folder.

(structure)

Describes the document.

Id -> (string)

The ID of the document.

CreatorId -> (string)

The ID of the creator.

ParentFolderId -> (string)

The ID of the parent folder.

CreatedTimestamp -> (timestamp)

The time when the document was created.

ModifiedTimestamp -> (timestamp)

The time when the document was updated.

LatestVersionMetadata -> (structure)

The latest version of the document.

Id -> (string)

The ID of the version.

Name -> (string)

The name of the version.

ContentType -> (string)

The content type of the document.

Size -> (long)

The size of the document, in bytes.

Signature -> (string)

The signature of the document.

Status -> (string)

The status of the document.

CreatedTimestamp -> (timestamp)

The timestamp when the document was first uploaded.

ModifiedTimestamp -> (timestamp)

The timestamp when the document was last uploaded.

ContentCreatedTimestamp -> (timestamp)

The timestamp when the content of the document was originally created.

ContentModifiedTimestamp -> (timestamp)

The timestamp when the content of the document was modified.

CreatorId -> (string)

The ID of the creator.

Thumbnail -> (map)

The thumbnail of the document.

key -> (string)

value -> (string)

Source -> (map)

The source of the document.

key -> (string)

value -> (string)

ResourceState -> (string)

The resource state.

Labels -> (list)

List of labels on the document.

(string)

Marker -> (string)

The marker to use when requesting the next set of results. If there are no additional results, the string is empty.