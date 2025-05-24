# get-data-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/get-data-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/get-data-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-agent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/index.html#cli-aws-bedrock-agent) ]

# get-data-source

## Description

Gets information about a data source.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agent-2023-06-05/GetDataSource)

## Synopsis

```
get-data-source
--data-source-id <value>
--knowledge-base-id <value>
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

`--data-source-id` (string)

The unique identifier of the data source.

`--knowledge-base-id` (string)

The unique identifier of the knowledge base for the data source.

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

dataSource -> (structure)

Contains details about the data source.

createdAt -> (timestamp)

The time at which the data source was created.

dataDeletionPolicy -> (string)

The data deletion policy for the data source.

dataSourceConfiguration -> (structure)

The connection configuration for the data source.

confluenceConfiguration -> (structure)

The configuration information to connect to Confluence as your data source.

### Note

Confluence data source connector is in preview release and is subject to change.

crawlerConfiguration -> (structure)

The configuration of the Confluence content. For example, configuring specific types of Confluence content.

filterConfiguration -> (structure)

The configuration of filtering the Confluence content. For example, configuring regular expression patterns to include or exclude certain content.

patternObjectFilter -> (structure)

The configuration of filtering certain objects or content types of the data source.

filters -> (list)

The configuration of specific filters applied to your data source content. You can filter out or include certain content.

(structure)

The specific filters applied to your data source content. You can filter out or include certain content.

exclusionFilters -> (list)

A list of one or more exclusion regular expression patterns to exclude certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isnât crawled.

(string)

inclusionFilters -> (list)

A list of one or more inclusion regular expression patterns to include certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isnât crawled.

(string)

objectType -> (string)

The supported object type or content type of the data source.

type -> (string)

The type of filtering that you want to apply to certain objects or content of the data source. For example, the `PATTERN` type is regular expression patterns you can apply to filter your content.

sourceConfiguration -> (structure)

The endpoint information to connect to your Confluence data source.

authType -> (string)

The supported authentication type to authenticate and connect to your Confluence instance.

credentialsSecretArn -> (string)

The Amazon Resource Name of an Secrets Manager secret that stores your authentication credentials for your Confluence instance URL. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see [Confluence connection configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/confluence-data-source-connector.html#configuration-confluence-connector) .

hostType -> (string)

The supported host type, whether online/cloud or server/on-premises.

hostUrl -> (string)

The Confluence host URL or instance URL.

s3Configuration -> (structure)

The configuration information to connect to Amazon S3 as your data source.

bucketArn -> (string)

The Amazon Resource Name (ARN) of the S3 bucket that contains your data.

bucketOwnerAccountId -> (string)

The account ID for the owner of the S3 bucket.

inclusionPrefixes -> (list)

A list of S3 prefixes to include certain files or content. For more information, see [Organizing objects using prefixes](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-prefixes.html) .

(string)

salesforceConfiguration -> (structure)

The configuration information to connect to Salesforce as your data source.

### Note

Salesforce data source connector is in preview release and is subject to change.

crawlerConfiguration -> (structure)

The configuration of the Salesforce content. For example, configuring specific types of Salesforce content.

filterConfiguration -> (structure)

The configuration of filtering the Salesforce content. For example, configuring regular expression patterns to include or exclude certain content.

patternObjectFilter -> (structure)

The configuration of filtering certain objects or content types of the data source.

filters -> (list)

The configuration of specific filters applied to your data source content. You can filter out or include certain content.

(structure)

The specific filters applied to your data source content. You can filter out or include certain content.

exclusionFilters -> (list)

A list of one or more exclusion regular expression patterns to exclude certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isnât crawled.

(string)

inclusionFilters -> (list)

A list of one or more inclusion regular expression patterns to include certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isnât crawled.

(string)

objectType -> (string)

The supported object type or content type of the data source.

type -> (string)

The type of filtering that you want to apply to certain objects or content of the data source. For example, the `PATTERN` type is regular expression patterns you can apply to filter your content.

sourceConfiguration -> (structure)

The endpoint information to connect to your Salesforce data source.

authType -> (string)

The supported authentication type to authenticate and connect to your Salesforce instance.

credentialsSecretArn -> (string)

The Amazon Resource Name of an Secrets Manager secret that stores your authentication credentials for your Salesforce instance URL. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see [Salesforce connection configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/salesforce-data-source-connector.html#configuration-salesforce-connector) .

hostUrl -> (string)

The Salesforce host URL or instance URL.

sharePointConfiguration -> (structure)

The configuration information to connect to SharePoint as your data source.

### Note

SharePoint data source connector is in preview release and is subject to change.

crawlerConfiguration -> (structure)

The configuration of the SharePoint content. For example, configuring specific types of SharePoint content.

filterConfiguration -> (structure)

The configuration of filtering the SharePoint content. For example, configuring regular expression patterns to include or exclude certain content.

patternObjectFilter -> (structure)

The configuration of filtering certain objects or content types of the data source.

filters -> (list)

The configuration of specific filters applied to your data source content. You can filter out or include certain content.

(structure)

The specific filters applied to your data source content. You can filter out or include certain content.

exclusionFilters -> (list)

A list of one or more exclusion regular expression patterns to exclude certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isnât crawled.

(string)

inclusionFilters -> (list)

A list of one or more inclusion regular expression patterns to include certain object types that adhere to the pattern. If you specify an inclusion and exclusion filter/pattern and both match a document, the exclusion filter takes precedence and the document isnât crawled.

(string)

objectType -> (string)

The supported object type or content type of the data source.

type -> (string)

The type of filtering that you want to apply to certain objects or content of the data source. For example, the `PATTERN` type is regular expression patterns you can apply to filter your content.

sourceConfiguration -> (structure)

The endpoint information to connect to your SharePoint data source.

authType -> (string)

The supported authentication type to authenticate and connect to your SharePoint site/sites.

credentialsSecretArn -> (string)

The Amazon Resource Name of an Secrets Manager secret that stores your authentication credentials for your SharePoint site/sites. For more information on the key-value pairs that must be included in your secret, depending on your authentication type, see [SharePoint connection configuration](https://docs.aws.amazon.com/bedrock/latest/userguide/sharepoint-data-source-connector.html#configuration-sharepoint-connector) .

domain -> (string)

The domain of your SharePoint instance or site URL/URLs.

hostType -> (string)

The supported host type, whether online/cloud or server/on-premises.

siteUrls -> (list)

A list of one or more SharePoint site URLs.

(string)

tenantId -> (string)

The identifier of your Microsoft 365 tenant.

type -> (string)

The type of data source.

webConfiguration -> (structure)

The configuration of web URLs to crawl for your data source. You should be authorized to crawl the URLs.

### Note

Crawling web URLs as your data source is in preview release and is subject to change.

crawlerConfiguration -> (structure)

The Web Crawler configuration details for the web data source.

crawlerLimits -> (structure)

The configuration of crawl limits for the web URLs.

maxPages -> (integer)

The max number of web pages crawled from your source URLs, up to 25,000 pages. If the web pages exceed this limit, the data source sync will fail and no web pages will be ingested.

rateLimit -> (integer)

The max rate at which pages are crawled, up to 300 per minute per host.

exclusionFilters -> (list)

A list of one or more exclusion regular expression patterns to exclude certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isnât crawled.

(string)

inclusionFilters -> (list)

A list of one or more inclusion regular expression patterns to include certain URLs. If you specify an inclusion and exclusion filter/pattern and both match a URL, the exclusion filter takes precedence and the web content of the URL isnât crawled.

(string)

scope -> (string)

The scope of what is crawled for your URLs.

You can choose to crawl only web pages that belong to the same host or primary domain. For example, only web pages that contain the seed URL â[https://docs.aws.amazon.com/bedrock/latest/userguide/](https://docs.aws.amazon.com/bedrock/latest/userguide/)â and no other domains. You can choose to include sub domains in addition to the host or primary domain. For example, web pages that contain âaws.amazon.comâ can also include sub domain âdocs.aws.amazon.comâ.

userAgent -> (string)

Returns the user agent suffix for your web crawler.

userAgentHeader -> (string)

A string used for identifying the crawler or bot when it accesses a web server. The user agent header value consists of the `bedrockbot` , UUID, and a user agent suffix for your crawler (if one is provided). By default, it is set to `bedrockbot_UUID` . You can optionally append a custom suffix to `bedrockbot_UUID` to allowlist a specific user agent permitted to access your source URLs.

sourceConfiguration -> (structure)

The source configuration details for the web data source.

urlConfiguration -> (structure)

The configuration of the URL/URLs.

seedUrls -> (list)

One or more seed or starting point URLs.

(structure)

The seed or starting point URL. You should be authorized to crawl the URL.

url -> (string)

A seed or starting point URL.

dataSourceId -> (string)

The unique identifier of the data source.

description -> (string)

The description of the data source.

failureReasons -> (list)

The detailed reasons on the failure to delete a data source.

(string)

knowledgeBaseId -> (string)

The unique identifier of the knowledge base to which the data source belongs.

name -> (string)

The name of the data source.

serverSideEncryptionConfiguration -> (structure)

Contains details about the configuration of the server-side encryption.

kmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the KMS key used to encrypt the resource.

status -> (string)

The status of the data source. The following statuses are possible:

- Available â The data source has been created and is ready for ingestion into the knowledge base.
- Deleting â The data source is being deleted.

updatedAt -> (timestamp)

The time at which the data source was last updated.

vectorIngestionConfiguration -> (structure)

Contains details about how to ingest the documents in the data source.

chunkingConfiguration -> (structure)

Details about how to chunk the documents in the data source. A *chunk* refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried.

chunkingStrategy -> (string)

Knowledge base can split your source data into chunks. A *chunk* refers to an excerpt from a data source that is returned when the knowledge base that it belongs to is queried. You have the following options for chunking your data. If you opt for `NONE` , then you may want to pre-process your files by splitting them up such that each file corresponds to a chunk.

- `FIXED_SIZE` â Amazon Bedrock splits your source data into chunks of the approximate size that you set in the `fixedSizeChunkingConfiguration` .
- `HIERARCHICAL` â Split documents into layers of chunks where the first layer contains large chunks, and the second layer contains smaller chunks derived from the first layer.
- `SEMANTIC` â Split documents into chunks based on groups of similar content derived with natural language processing.
- `NONE` â Amazon Bedrock treats each file as one chunk. If you choose this option, you may want to pre-process your documents by splitting them into separate files.

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

Token settings for a layer in a hierarchical chunking configuration.

maxTokens -> (integer)

The maximum number of tokens that a chunk can contain in this layer.

overlapTokens -> (integer)

The number of tokens to repeat across chunks in the same layer.

semanticChunkingConfiguration -> (structure)

Settings for semantic document chunking for a data source. Semantic chunking splits a document into into smaller documents based on groups of similar content derived from the text with natural language processing.

breakpointPercentileThreshold -> (integer)

The dissimilarity threshold for splitting chunks.

bufferSize -> (integer)

The buffer size.

maxTokens -> (integer)

The maximum number of tokens that a chunk can contain.

contextEnrichmentConfiguration -> (structure)

The context enrichment configuration used for ingestion of the data into the vector store.

bedrockFoundationModelConfiguration -> (structure)

The configuration of the Amazon Bedrock foundation model used for context enrichment.

enrichmentStrategyConfiguration -> (structure)

The enrichment stategy used to provide additional context. For example, Neptune GraphRAG uses Amazon Bedrock foundation models to perform chunk entity extraction.

method -> (string)

The method used for the context enrichment strategy.

modelArn -> (string)

The Amazon Resource Name (ARN) of the model used to create vector embeddings for the knowledge base.

type -> (string)

The method used for context enrichment. It must be Amazon Bedrock foundation models.

customTransformationConfiguration -> (structure)

A custom document transformer for parsed data source documents.

intermediateStorage -> (structure)

An S3 bucket path for input and output objects.

s3Location -> (structure)

An S3 bucket path.

uri -> (string)

The locationâs URI. For example, `s3://my-bucket/chunk-processor/` .

transformations -> (list)

A Lambda function that processes documents.

(structure)

A custom processing step for documents moving through a data source ingestion pipeline. To process documents after they have been converted into chunks, set the step to apply to `POST_CHUNKING` .

stepToApply -> (string)

When the service applies the transformation.

transformationFunction -> (structure)

A Lambda function that processes documents.

transformationLambdaConfiguration -> (structure)

The Lambda function.

lambdaArn -> (string)

The functionâs ARN identifier.

parsingConfiguration -> (structure)

Configurations for a parser to use for parsing documents in your data source. If you exclude this field, the default parser will be used.

bedrockDataAutomationConfiguration -> (structure)

If you specify `BEDROCK_DATA_AUTOMATION` as the parsing strategy for ingesting your data source, use this object to modify configurations for using the Amazon Bedrock Data Automation parser.

parsingModality -> (string)

Specifies whether to enable parsing of multimodal data, including both text and/or images.

bedrockFoundationModelConfiguration -> (structure)

If you specify `BEDROCK_FOUNDATION_MODEL` as the parsing strategy for ingesting your data source, use this object to modify configurations for using a foundation model to parse documents.

modelArn -> (string)

The ARN of the foundation model to use for parsing.

parsingModality -> (string)

Specifies whether to enable parsing of multimodal data, including both text and/or images.

parsingPrompt -> (structure)

Instructions for interpreting the contents of a document.

parsingPromptText -> (string)

Instructions for interpreting the contents of a document.

parsingStrategy -> (string)

The parsing strategy for the data source.