# search-resourcesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/search-resources.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/search-resources.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workdocs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/index.html#cli-aws-workdocs) ]

# search-resources

## Description

Searches metadata and the content of folders, documents, document versions, and comments.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/SearchResources)

`search-resources` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Items`

## Synopsis

```
search-resources
[--authentication-token <value>]
[--query-text <value>]
[--query-scopes <value>]
[--organization-id <value>]
[--additional-response-fields <value>]
[--filters <value>]
[--order-by <value>]
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

`--query-text` (string)

The String to search for. Searches across different text fields based on request parameters. Use double quotes around the query string for exact phrase matches.

`--query-scopes` (list)

Filter based on the text field type. A Folder has only a name and no content. A Comment has only content and no name. A Document or Document Version has a name and content

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  NAME
  CONTENT
```

`--organization-id` (string)

Filters based on the resource owner OrgId. This is a mandatory parameter when using Admin SigV4 credentials.

`--additional-response-fields` (list)

A list of attributes to include in the response. Used to request fields that are not normally returned in a standard response.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  WEBURL
```

`--filters` (structure)

Filters results based on entity metadata.

TextLocales -> (list)

Filters by the locale of the content or comment.

(string)

ContentCategories -> (list)

Filters by content category.

(string)

ResourceTypes -> (list)

Filters based on entity type.

(string)

Labels -> (list)

Filter by labels using exact match.

(string)

Principals -> (list)

Filter based on UserIds or GroupIds.

(structure)

Filter based on UserIds or GroupIds.

Id -> (string)

UserIds or GroupIds.

Roles -> (list)

The Role of a User or Group.

(string)

AncestorIds -> (list)

Filter based on resourceâs path.

(string)

SearchCollectionTypes -> (list)

Filter based on file groupings.

(string)

SizeRange -> (structure)

Filter based on size (in bytes).

StartValue -> (long)

The size start range (in bytes).

EndValue -> (long)

The size end range (in bytes).

CreatedRange -> (structure)

Filter based on resourceâs creation timestamp.

StartValue -> (timestamp)

Timestamp range start value (in epochs)

EndValue -> (timestamp)

Timestamp range end value (in epochs).

ModifiedRange -> (structure)

Filter based on resourceâs modified timestamp.

StartValue -> (timestamp)

Timestamp range start value (in epochs)

EndValue -> (timestamp)

Timestamp range end value (in epochs).

JSON Syntax:

```
{
  "TextLocales": ["AR"|"BG"|"BN"|"DA"|"DE"|"CS"|"EL"|"EN"|"ES"|"FA"|"FI"|"FR"|"HI"|"HU"|"ID"|"IT"|"JA"|"KO"|"LT"|"LV"|"NL"|"NO"|"PT"|"RO"|"RU"|"SV"|"SW"|"TH"|"TR"|"ZH"|"DEFAULT", ...],
  "ContentCategories": ["IMAGE"|"DOCUMENT"|"PDF"|"SPREADSHEET"|"PRESENTATION"|"AUDIO"|"VIDEO"|"SOURCE_CODE"|"OTHER", ...],
  "ResourceTypes": ["FOLDER"|"DOCUMENT"|"COMMENT"|"DOCUMENT_VERSION", ...],
  "Labels": ["string", ...],
  "Principals": [
    {
      "Id": "string",
      "Roles": ["VIEWER"|"CONTRIBUTOR"|"OWNER"|"COOWNER", ...]
    }
    ...
  ],
  "AncestorIds": ["string", ...],
  "SearchCollectionTypes": ["OWNED"|"SHARED_WITH_ME", ...],
  "SizeRange": {
    "StartValue": long,
    "EndValue": long
  },
  "CreatedRange": {
    "StartValue": timestamp,
    "EndValue": timestamp
  },
  "ModifiedRange": {
    "StartValue": timestamp,
    "EndValue": timestamp
  }
}
```

`--order-by` (list)

Order by results in one or more categories.

(structure)

The result of the sort operation.

Field -> (string)

Sort search results based on this field name.

Order -> (string)

Sort direction.

Shorthand Syntax:

```
Field=string,Order=string ...
```

JSON Syntax:

```
[
  {
    "Field": "RELEVANCE"|"NAME"|"SIZE"|"CREATED_TIMESTAMP"|"MODIFIED_TIMESTAMP",
    "Order": "ASC"|"DESC"
  }
  ...
]
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

Items -> (list)

List of Documents, Folders, Comments, and Document Versions matching the query.

(structure)

List of Documents, Folders, Comments, and Document Versions matching the query.

ResourceType -> (string)

The type of item being returned.

WebUrl -> (string)

The webUrl of the item being returned.

DocumentMetadata -> (structure)

The document that matches the query.

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

FolderMetadata -> (structure)

The folder that matches the query.

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

CommentMetadata -> (structure)

The comment that matches the query.

CommentId -> (string)

The ID of the comment.

Contributor -> (structure)

The user who made the comment.

Id -> (string)

The ID of the user.

Username -> (string)

The login name of the user.

EmailAddress -> (string)

The email address of the user.

GivenName -> (string)

The given name of the user.

Surname -> (string)

The surname of the user.

OrganizationId -> (string)

The ID of the organization.

RootFolderId -> (string)

The ID of the root folder.

RecycleBinFolderId -> (string)

The ID of the recycle bin folder.

Status -> (string)

The status of the user.

Type -> (string)

The type of user.

CreatedTimestamp -> (timestamp)

The time when the user was created.

ModifiedTimestamp -> (timestamp)

The time when the user was modified.

TimeZoneId -> (string)

The time zone ID of the user.

Locale -> (string)

The locale of the user.

Storage -> (structure)

The storage for the user.

StorageUtilizedInBytes -> (long)

The amount of storage used, in bytes.

StorageRule -> (structure)

The storage for a user.

StorageAllocatedInBytes -> (long)

The amount of storage allocated, in bytes.

StorageType -> (string)

The type of storage.

CreatedTimestamp -> (timestamp)

The timestamp that the comment was created.

CommentStatus -> (string)

The status of the comment.

RecipientId -> (string)

The ID of the user being replied to.

ContributorId -> (string)

The ID of the user who made the comment.

DocumentVersionMetadata -> (structure)

The document version that matches the metadata.

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

Marker -> (string)

The marker to use when requesting the next set of results. If there are no additional results, the string is empty.