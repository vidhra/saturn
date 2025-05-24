# list-knowledge-basesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/list-knowledge-bases.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/list-knowledge-bases.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/index.html#cli-aws-qconnect) ]

# list-knowledge-bases

## Description

Lists the knowledge bases.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qconnect-2020-10-19/ListKnowledgeBases)

`list-knowledge-bases` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `knowledgeBaseSummaries`

## Synopsis

```
list-knowledge-bases
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

knowledgeBaseSummaries -> (list)

Information about the knowledge bases.

(structure)

Summary information about the knowledge base.

knowledgeBaseId -> (string)

The identifier of the knowledge base.

knowledgeBaseArn -> (string)

The Amazon Resource Name (ARN) of the knowledge base.

name -> (string)

The name of the knowledge base.

knowledgeBaseType -> (string)

The type of knowledge base.

status -> (string)

The status of the knowledge base summary.

sourceConfiguration -> (tagged union structure)

Configuration information about the external data source.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `appIntegrations`, `managedSourceConfiguration`.

appIntegrations -> (structure)

Configuration information for Amazon AppIntegrations to automatically ingest content.

appIntegrationArn -> (string)

The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content.

- For [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm) , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least `Id` , `ArticleNumber` , `VersionNumber` , `Title` , `PublishStatus` , and `IsDeleted` as source fields.
- For [ServiceNow](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api) , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least `number` , `short_description` , `sys_mod_count` , `workflow_state` , and `active` as source fields.
- For [Zendesk](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/) , your AppIntegrations DataIntegration must have an ObjectConfiguration if `objectFields` is not provided, including at least `id` , `title` , `updated_at` , and `draft` as source fields.
- For [SharePoint](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index) , your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among `docx` , `pdf` , `html` , `htm` , and `txt` .
- For [Amazon S3](http://aws.amazon.com/s3/) , the ObjectConfiguration and FileConfiguration of your AppIntegrations DataIntegration must be null. The `SourceURI` of your DataIntegration must use the following format: `s3://your_s3_bucket_name` .

### Warning

The bucket policy of the corresponding S3 bucket must allow the Amazon Web Services principal `app-integrations.amazonaws.com` to perform `s3:ListBucket` , `s3:GetObject` , and `s3:GetBucketLocation` against the bucket.

objectFields -> (list)

The fields from the source that are made available to your agents in Amazon Q in Connect. Optional if ObjectConfiguration is included in the provided DataIntegration.

- For [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm) , you must include at least `Id` , `ArticleNumber` , `VersionNumber` , `Title` , `PublishStatus` , and `IsDeleted` .
- For [ServiceNow](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api) , you must include at least `number` , `short_description` , `sys_mod_count` , `workflow_state` , and `active` .
- For [Zendesk](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/) , you must include at least `id` , `title` , `updated_at` , and `draft` .

Make sure to include additional fields. These fields are indexed and used to source recommendations.

(string)

managedSourceConfiguration -> (tagged union structure)

Source configuration for managed resources.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `webCrawlerConfiguration`.

webCrawlerConfiguration -> (structure)

Configuration data for web crawler data source.

urlConfiguration -> (structure)

The configuration of the URL/URLs for the web content that you want to crawl. You should be authorized to crawl the URLs.

seedUrls -> (list)

List of URLs for crawling.

(structure)

A URL for crawling.

url -> (string)

URL for crawling

crawlerLimits -> (structure)

The configuration of crawl limits for the web URLs.

rateLimit -> (integer)

Rate of web URLs retrieved per minute.

inclusionFilters -> (list)

A list of one or more inclusion regular expression patterns to include certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isnât crawled.

(string)

exclusionFilters -> (list)

A list of one or more exclusion regular expression patterns to exclude certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isnât crawled.

(string)

scope -> (string)

The scope of what is crawled for your URLs. You can choose to crawl only web pages that belong to the same host or primary domain. For example, only web pages that contain the seed URL `https://docs.aws.amazon.com/bedrock/latest/userguide/` and no other domains. You can choose to include sub domains in addition to the host or primary domain. For example, web pages that contain `aws.amazon.com` can also include sub domain `docs.aws.amazon.com` .

vectorIngestionConfiguration -> (structure)

Contains details about how to ingest the documents in a data source.

chunkingConfiguration -> (structure)

Details about how to chunk the documents in the data source. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.

chunkingStrategy -> (string)

Knowledge base can split your source data into chunks. A chunk refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried. You have the following options for chunking your data. If you opt for `NONE` , then you may want to pre-process your files by splitting them up such that each file corresponds to a chunk.

fixedSizeChunkingConfiguration -> (structure)

Configurations for when you choose fixed-size chunking. If you set the `chunkingStrategy` as `NONE` , exclude this field.

maxTokens -> (integer)

The maximum number of tokens to include in a chunk.

overlapPercentage -> (integer)

The percentage of overlap between adjacent chunks of a data source.

hierarchicalChunkingConfiguration -> (structure)

Settings for hierarchical document chunking for a data source. Hierarchical chunking splits documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.

levelConfigurations -> (list)

Token settings for each layer.

(structure)

Token settings for each layer.

maxTokens -> (integer)

The maximum number of tokens that a chunk can contain in this layer.

overlapTokens -> (integer)

The number of tokens to repeat across chunks in the same layer.

semanticChunkingConfiguration -> (structure)

Settings for semantic document chunking for a data source. Semantic chunking splits a document into smaller documents based on groups of similar content derived from the text with natural language processing.

maxTokens -> (integer)

The maximum number of tokens that a chunk can contain.

bufferSize -> (integer)

The buffer size.

breakpointPercentileThreshold -> (integer)

The dissimilarity threshold for splitting chunks.

parsingConfiguration -> (structure)

A custom parser for data source documents.

parsingStrategy -> (string)

The parsing strategy for the data source.

bedrockFoundationModelConfiguration -> (structure)

Settings for a foundation model used to parse documents for a data source.

modelArn -> (string)

The ARN of the foundation model.

parsingPrompt -> (structure)

Instructions for interpreting the contents of a document.

parsingPromptText -> (string)

Instructions for interpreting the contents of a document.

renderingConfiguration -> (structure)

Information about how to render the content.

templateUri -> (string)

A URI template containing exactly one variable in `${variableName}` format. This can only be set for `EXTERNAL` knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following:

- Salesforce: `Id` , `ArticleNumber` , `VersionNumber` , `Title` , `PublishStatus` , or `IsDeleted`
- ServiceNow: `number` , `short_description` , `sys_mod_count` , `workflow_state` , or `active`
- Zendesk: `id` , `title` , `updated_at` , or `draft`

The variable is replaced with the actual value for a piece of content when calling [GetContent](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_GetContent.html) .

serverSideEncryptionConfiguration -> (structure)

The configuration information for the customer managed key used for encryption.

This KMS key must have a policy that allows `kms:CreateGrant` , `kms:DescribeKey` , `kms:Decrypt` , and `kms:GenerateDataKey*` permissions to the IAM identity using the key to invoke Amazon Q in Connect.

For more information about setting up a customer managed key for Amazon Q in Connect, see [Enable Amazon Q in Connect for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html) .

kmsKeyId -> (string)

The customer managed key used for encryption. For more information about setting up a customer managed key for Amazon Q in Connect, see [Enable Amazon Q in Connect for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-q.html) . For information about valid ID values, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) .

description -> (string)

The description of the knowledge base.

tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

nextToken -> (string)

If there are additional results, this is the token for the next set of results.