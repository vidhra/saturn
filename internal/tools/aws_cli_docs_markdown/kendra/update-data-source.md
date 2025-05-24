# update-data-sourceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# update-data-source

## Description

Updates an Amazon Kendra data source connector.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/UpdateDataSource)

`update-data-source` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
update-data-source
--id <value>
[--name <value>]
--index-id <value>
[--configuration <value>]
[--vpc-configuration <value>]
[--description <value>]
[--schedule <value>]
[--role-arn <value>]
[--language-code <value>]
[--custom-document-enrichment-configuration <value>]
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

`--id` (string)

The identifier of the data source connector you want to update.

`--name` (string)

A new name for the data source connector.

`--index-id` (string)

The identifier of the index used with the data source connector.

`--configuration` (structure)

Configuration information you want to update for the data source connector.

S3Configuration -> (structure)

Provides the configuration information to connect to an Amazon S3 bucket as your data source.

### Note

Amazon Kendra now supports an upgraded Amazon S3 connector.

You must now use the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) object instead of the `S3DataSourceConfiguration` object to configure your connector.

Connectors configured using the older console and API architecture will continue to function as configured. However, you wonât be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.

We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.

BucketName -> (string)

The name of the bucket that contains the documents.

InclusionPrefixes -> (list)

A list of S3 prefixes for the documents that should be included in the index.

(string)

InclusionPatterns -> (list)

A list of glob patterns (patterns that can expand a wildcard pattern into a list of path names that match the given pattern) for certain file names and file types to include in your index. If a document matches both an inclusion and exclusion prefix or pattern, the exclusion prefix takes precendence and the document is not indexed. Examples of glob patterns include:

- */myapp/config/** âAll files inside config directory.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html#id1)*/*.png* âAll .png files in all directories.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html#id3)*/*.{png, ico, md}* âAll .png, .ico or .md files in all directories.
- */myapp/src/**/*.ts* âAll .ts files inside src directory (and all its subdirectories).
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html#id5)*/!(*.module).ts* âAll .ts files but not .module.ts
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html#id7).png , *.jpg* âAll PNG and JPEG image files in a directory (files with the extensions .png and .jpg).
- **internal** âAll files in a directory that contain âinternalâ in the file name, such as âinternalâ, âinternal_onlyâ, âcompany_internalâ.
- ***/*internal** âAll internal-related files in a directory and its subdirectories.

For more examples, see [Use of Exclude and Include Filters](https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters) in the Amazon Web Services CLI Command Reference.

(string)

ExclusionPatterns -> (list)

A list of glob patterns (patterns that can expand a wildcard pattern into a list of path names that match the given pattern) for certain file names and file types to exclude from your index. If a document matches both an inclusion and exclusion prefix or pattern, the exclusion prefix takes precendence and the document is not indexed. Examples of glob patterns include:

- */myapp/config/** âAll files inside config directory.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html#id9)*/*.png* âAll .png files in all directories.
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html#id11)*/*.{png, ico, md}* âAll .png, .ico or .md files in all directories.
- */myapp/src/**/*.ts* âAll .ts files inside src directory (and all its subdirectories).
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html#id13)*/!(*.module).ts* âAll .ts files but not .module.ts
- [**](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/update-data-source.html#id15).png , *.jpg* âAll PNG and JPEG image files in a directory (files with the extensions .png and .jpg).
- **internal** âAll files in a directory that contain âinternalâ in the file name, such as âinternalâ, âinternal_onlyâ, âcompany_internalâ.
- ***/*internal** âAll internal-related files in a directory and its subdirectories.

For more examples, see [Use of Exclude and Include Filters](https://docs.aws.amazon.com/cli/latest/reference/s3/#use-of-exclude-and-include-filters) in the Amazon Web Services CLI Command Reference.

(string)

DocumentsMetadataConfiguration -> (structure)

Document metadata files that contain information such as the document access control information, source URI, document author, and custom attributes. Each metadata file contains metadata about a single document.

S3Prefix -> (string)

A prefix used to filter metadata configuration files in the Amazon Web Services S3 bucket. The S3 bucket might contain multiple metadata files. Use `S3Prefix` to include only the desired metadata files.

AccessControlListConfiguration -> (structure)

Provides the path to the S3 bucket that contains the user context filtering files for the data source. For the format of the file, see [Access control for S3 data sources](https://docs.aws.amazon.com/kendra/latest/dg/s3-acl.html) .

KeyPath -> (string)

Path to the Amazon S3 bucket that contains the ACL files.

SharePointConfiguration -> (structure)

Provides the configuration information to connect to Microsoft SharePoint as your data source.

SharePointVersion -> (string)

The version of Microsoft SharePoint that you use.

Urls -> (list)

The Microsoft SharePoint site URLs for the documents you want to index.

(string)

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the user name and password required to connect to the SharePoint instance. For more information, see [Microsoft SharePoint](https://docs.aws.amazon.com/kendra/latest/dg/data-source-sharepoint.html) .

CrawlAttachments -> (boolean)

`TRUE` to index document attachments.

UseChangeLog -> (boolean)

`TRUE` to use the SharePoint change log to determine which documents require updating in the index. Depending on the change logâs size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in SharePoint.

InclusionPatterns -> (list)

A list of regular expression patterns to include certain documents in your SharePoint. Documents that match the patterns are included in the index. Documents that donât match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isnât included in the index.

The regex applies to the display URL of the SharePoint document.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain documents in your SharePoint. Documents that match the patterns are excluded from the index. Documents that donât match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isnât included in the index.

The regex applies to the display URL of the SharePoint document.

(string)

VpcConfiguration -> (structure)

Configuration information for an Amazon Virtual Private Cloud to connect to your Microsoft SharePoint. For more information, see [Configuring a VPC](https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html) .

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

FieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map SharePoint data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to SharePoint fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The SharePoint data source field names must exist in your SharePoint custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

DocumentTitleFieldName -> (string)

The Microsoft SharePoint attribute field that contains the title of the document.

DisableLocalGroups -> (boolean)

`TRUE` to disable local groups information.

SslCertificateS3Path -> (structure)

The path to the SSL certificate stored in an Amazon S3 bucket. You use this to connect to SharePoint Server if you require a secure SSL connection.

You can generate a self-signed X509 certificate on any computer using OpenSSL. For an example of using OpenSSL to create an X509 certificate, see [Create and sign an X509 certificate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html) .

Bucket -> (string)

The name of the S3 bucket that contains the file.

Key -> (string)

The name of the file.

AuthenticationType -> (string)

Whether you want to connect to SharePoint Online using basic authentication of user name and password, or OAuth authentication of user name, password, client ID, and client secret, or AD App-only authentication of client secret.

ProxyConfiguration -> (structure)

Configuration information to connect to your Microsoft SharePoint site URLs via instance via a web proxy. You can use this option for SharePoint Server.

You must provide the website host name and port number. For example, the host name of *https://a.example.com/page1.html* is âa.example.comâ and the port is 443, the standard port for HTTPS.

Web proxy credentials are optional and you can use them to connect to a web proxy server that requires basic authentication of user name and password. To store web proxy credentials, you use a secret in Secrets Manager.

It is recommended that you follow best security practices when configuring your web proxy. This includes setting up throttling, setting up logging and monitoring, and applying security patches on a regular basis. If you use your web proxy with multiple data sources, sync jobs that occur at the same time could strain the load on your proxy. It is recommended you prepare your proxy beforehand for any security and load requirements.

Host -> (string)

The name of the website host you want to connect to via a web proxy server.

For example, the host name of [https://a.example.com/page1.html](https://a.example.com/page1.html) is âa.example.comâ.

Port -> (integer)

The port number of the website host you want to connect to via a web proxy server.

For example, the port for [https://a.example.com/page1.html](https://a.example.com/page1.html) is 443, the standard port for HTTPS.

Credentials -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret. You create a secret to store your credentials in [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

The credentials are optional. You use a secret if web proxy credentials are required to connect to a website host. Amazon Kendra currently support basic authentication to connect to a web proxy server. The secret stores your credentials.

DatabaseConfiguration -> (structure)

Provides the configuration information to connect to a database as your data source.

DatabaseEngineType -> (string)

The type of database engine that runs the database.

ConnectionConfiguration -> (structure)

Configuration information thatâs required to connect to a database.

DatabaseHost -> (string)

The name of the host for the database. Can be either a string (host.subdomain.domain.tld) or an IPv4 or IPv6 address.

DatabasePort -> (integer)

The port that the database uses for connections.

DatabaseName -> (string)

The name of the database containing the document data.

TableName -> (string)

The name of the table that contains the document data.

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret that stores the credentials. The credentials should be a user-password pair. For more information, see [Using a Database Data Source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-database.html) . For more information about Secrets Manager, see [What Is Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) in the *Secrets Manager* user guide.

VpcConfiguration -> (structure)

Provides the configuration information to connect to an Amazon VPC.

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

ColumnConfiguration -> (structure)

Information about where the index should get the document information from the database.

DocumentIdColumnName -> (string)

The column that provides the documentâs identifier.

DocumentDataColumnName -> (string)

The column that contains the contents of the document.

DocumentTitleColumnName -> (string)

The column that contains the title of the document.

FieldMappings -> (list)

An array of objects that map database column names to the corresponding fields in an index. You must first create the fields in the index using the `UpdateIndex` API.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

ChangeDetectingColumns -> (list)

One to five columns that indicate when a document in the database has changed.

(string)

AclConfiguration -> (structure)

Information about the database column that provides information for user context filtering.

AllowedGroupsColumnName -> (string)

A list of groups, separated by semi-colons, that filters a query response based on user context. The document is only returned to users that are in one of the groups specified in the `UserContext` field of the `Query` API.

SqlConfiguration -> (structure)

Provides information about how Amazon Kendra uses quote marks around SQL identifiers when querying a database data source.

QueryIdentifiersEnclosingOption -> (string)

Determines whether Amazon Kendra encloses SQL identifiers for tables and column names in double quotes (â) when making a database query.

By default, Amazon Kendra passes SQL identifiers the way that they are entered into the data source configuration. It does not change the case of identifiers or enclose them in quotes.

PostgreSQL internally converts uppercase characters to lower case characters in identifiers unless they are quoted. Choosing this option encloses identifiers in quotes so that PostgreSQL does not convert the characterâs case.

For MySQL databases, you must enable the `ansi_quotes` option when you set this field to `DOUBLE_QUOTES` .

SalesforceConfiguration -> (structure)

Provides the configuration information to connect to Salesforce as your data source.

ServerUrl -> (string)

The instance URL for the Salesforce site that you want to index.

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Managersecret that contains the key/value pairs required to connect to your Salesforce instance. The secret must contain a JSON structure with the following keys:

- authenticationUrl - The OAUTH endpoint that Amazon Kendra connects to get an OAUTH token.
- consumerKey - The application public key generated when you created your Salesforce application.
- consumerSecret - The application private key generated when you created your Salesforce application.
- password - The password associated with the user logging in to the Salesforce instance.
- securityToken - The token associated with the user logging in to the Salesforce instance.
- username - The user name of the user logging in to the Salesforce instance.

StandardObjectConfigurations -> (list)

Configuration of the Salesforce standard objects that Amazon Kendra indexes.

(structure)

Provides the configuration information for indexing a single standard object.

Name -> (string)

The name of the standard object.

DocumentDataFieldName -> (string)

The name of the field in the standard object table that contains the document contents.

DocumentTitleFieldName -> (string)

The name of the field in the standard object table that contains the document title.

FieldMappings -> (list)

Maps attributes or field names of the standard object to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Salesforce fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Salesforce data source field names must exist in your Salesforce custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

KnowledgeArticleConfiguration -> (structure)

Configuration information for the knowledge article types that Amazon Kendra indexes. Amazon Kendra indexes standard knowledge articles and the standard fields of knowledge articles, or the custom fields of custom knowledge articles, but not both.

IncludedStates -> (list)

Specifies the document states that should be included when Amazon Kendra indexes knowledge articles. You must specify at least one state.

(string)

StandardKnowledgeArticleTypeConfiguration -> (structure)

Configuration information for standard Salesforce knowledge articles.

DocumentDataFieldName -> (string)

The name of the field that contains the document data to index.

DocumentTitleFieldName -> (string)

The name of the field that contains the document title.

FieldMappings -> (list)

Maps attributes or field names of the knowledge article to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Salesforce fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Salesforce data source field names must exist in your Salesforce custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

CustomKnowledgeArticleTypeConfigurations -> (list)

Configuration information for custom Salesforce knowledge articles.

(structure)

Provides the configuration information for indexing Salesforce custom articles.

Name -> (string)

The name of the configuration.

DocumentDataFieldName -> (string)

The name of the field in the custom knowledge article that contains the document data to index.

DocumentTitleFieldName -> (string)

The name of the field in the custom knowledge article that contains the document title.

FieldMappings -> (list)

Maps attributes or field names of the custom knowledge article to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Salesforce fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Salesforce data source field names must exist in your Salesforce custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

ChatterFeedConfiguration -> (structure)

Configuration information for Salesforce chatter feeds.

DocumentDataFieldName -> (string)

The name of the column in the Salesforce FeedItem table that contains the content to index. Typically this is the `Body` column.

DocumentTitleFieldName -> (string)

The name of the column in the Salesforce FeedItem table that contains the title of the document. This is typically the `Title` column.

FieldMappings -> (list)

Maps fields from a Salesforce chatter feed into Amazon Kendra index fields.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

IncludeFilterTypes -> (list)

Filters the documents in the feed based on status of the user. When you specify `ACTIVE_USERS` only documents from users who have an active account are indexed. When you specify `STANDARD_USER` only documents for Salesforce standard users are documented. You can specify both.

(string)

CrawlAttachments -> (boolean)

Indicates whether Amazon Kendra should index attachments to Salesforce objects.

StandardObjectAttachmentConfiguration -> (structure)

Configuration information for processing attachments to Salesforce standard objects.

DocumentTitleFieldName -> (string)

The name of the field used for the document title.

FieldMappings -> (list)

One or more objects that map fields in attachments to Amazon Kendra index fields.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

IncludeAttachmentFilePatterns -> (list)

A list of regular expression patterns to include certain documents in your Salesforce. Documents that match the patterns are included in the index. Documents that donât match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isnât included in the index.

The pattern is applied to the name of the attached file.

(string)

ExcludeAttachmentFilePatterns -> (list)

A list of regular expression patterns to exclude certain documents in your Salesforce. Documents that match the patterns are excluded from the index. Documents that donât match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isnât included in the index.

The pattern is applied to the name of the attached file.

(string)

OneDriveConfiguration -> (structure)

Provides the configuration information to connect to Microsoft OneDrive as your data source.

TenantDomain -> (string)

The Azure Active Directory domain of the organization.

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Managersecret that contains the user name and password to connect to OneDrive. The user name should be the application ID for the OneDrive application, and the password is the application key for the OneDrive application.

OneDriveUsers -> (structure)

A list of user accounts whose documents should be indexed.

OneDriveUserList -> (list)

A list of users whose documents should be indexed. Specify the user names in email format, for example, `username@tenantdomain` . If you need to index the documents of more than 10 users, use the `OneDriveUserS3Path` field to specify the location of a file containing a list of users.

(string)

OneDriveUserS3Path -> (structure)

The S3 bucket location of a file containing a list of users whose documents should be indexed.

Bucket -> (string)

The name of the S3 bucket that contains the file.

Key -> (string)

The name of the file.

InclusionPatterns -> (list)

A list of regular expression patterns to include certain documents in your OneDrive. Documents that match the patterns are included in the index. Documents that donât match the patterns are excluded from the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isnât included in the index.

The pattern is applied to the file name.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain documents in your OneDrive. Documents that match the patterns are excluded from the index. Documents that donât match the patterns are included in the index. If a document matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the document isnât included in the index.

The pattern is applied to the file name.

(string)

FieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map OneDrive data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to OneDrive fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The OneDrive data source field names must exist in your OneDrive custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

DisableLocalGroups -> (boolean)

`TRUE` to disable local groups information.

ServiceNowConfiguration -> (structure)

Provides the configuration information to connect to ServiceNow as your data source.

HostUrl -> (string)

The ServiceNow instance that the data source connects to. The host endpoint should look like the following: *{instance}.service-now.com.*

SecretArn -> (string)

The Amazon Resource Name (ARN) of the Secrets Manager secret that contains the user name and password required to connect to the ServiceNow instance. You can also provide OAuth authentication credentials of user name, password, client ID, and client secret. For more information, see [Using a ServiceNow data source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-servicenow.html) .

ServiceNowBuildVersion -> (string)

The identifier of the release that the ServiceNow host is running. If the host is not running the `LONDON` release, use `OTHERS` .

KnowledgeArticleConfiguration -> (structure)

Configuration information for crawling knowledge articles in the ServiceNow site.

CrawlAttachments -> (boolean)

`TRUE` to index attachments to knowledge articles.

IncludeAttachmentFilePatterns -> (list)

A list of regular expression patterns applied to include knowledge article attachments. Attachments that match the patterns are included in the index. Items that donât match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isnât included in the index.

(string)

ExcludeAttachmentFilePatterns -> (list)

A list of regular expression patterns applied to exclude certain knowledge article attachments. Attachments that match the patterns are excluded from the index. Items that donât match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isnât included in the index.

(string)

DocumentDataFieldName -> (string)

The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.

DocumentTitleFieldName -> (string)

The name of the ServiceNow field that is mapped to the index document title field.

FieldMappings -> (list)

Maps attributes or field names of knoweldge articles to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to ServiceNow fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The ServiceNow data source field names must exist in your ServiceNow custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

FilterQuery -> (string)

A query that selects the knowledge articles to index. The query can return articles from multiple knowledge bases, and the knowledge bases can be public or private.

The query string must be one generated by the ServiceNow console. For more information, see [Specifying documents to index with a query](https://docs.aws.amazon.com/kendra/latest/dg/servicenow-query.html) .

ServiceCatalogConfiguration -> (structure)

Configuration information for crawling service catalogs in the ServiceNow site.

CrawlAttachments -> (boolean)

`TRUE` to index attachments to service catalog items.

IncludeAttachmentFilePatterns -> (list)

A list of regular expression patterns to include certain attachments of catalogs in your ServiceNow. Item that match the patterns are included in the index. Items that donât match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isnât included in the index.

The regex is applied to the file name of the attachment.

(string)

ExcludeAttachmentFilePatterns -> (list)

A list of regular expression patterns to exclude certain attachments of catalogs in your ServiceNow. Item that match the patterns are excluded from the index. Items that donât match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isnât included in the index.

The regex is applied to the file name of the attachment.

(string)

DocumentDataFieldName -> (string)

The name of the ServiceNow field that is mapped to the index document contents field in the Amazon Kendra index.

DocumentTitleFieldName -> (string)

The name of the ServiceNow field that is mapped to the index document title field.

FieldMappings -> (list)

Maps attributes or field names of catalogs to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to ServiceNow fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The ServiceNow data source field names must exist in your ServiceNow custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

AuthenticationType -> (string)

The type of authentication used to connect to the ServiceNow instance. If you choose `HTTP_BASIC` , Amazon Kendra is authenticated using the user name and password provided in the Secrets Manager secret in the `SecretArn` field. If you choose `OAUTH2` , Amazon Kendra is authenticated using the credentials of client ID, client secret, user name and password.

When you use `OAUTH2` authentication, you must generate a token and a client secret using the ServiceNow console. For more information, see [Using a ServiceNow data source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-servicenow.html) .

ConfluenceConfiguration -> (structure)

Provides the configuration information to connect to Confluence as your data source.

ServerUrl -> (string)

The URL of your Confluence instance. Use the full URL of the server. For example, *https://server.example.com:port/* . You can also use an IP address, for example, *https://192.168.1.113/* .

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the user name and password required to connect to the Confluence instance. If you use Confluence Cloud, you use a generated API token as the password.

You can also provide authentication credentials in the form of a personal access token. For more information, see [Using a Confluence data source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-confluence.html) .

Version -> (string)

The version or the type of Confluence installation to connect to.

SpaceConfiguration -> (structure)

Configuration information for indexing Confluence spaces.

CrawlPersonalSpaces -> (boolean)

`TRUE` to index personal spaces. You can add restrictions to items in personal spaces. If personal spaces are indexed, queries without user context information may return restricted items from a personal space in their results. For more information, see [Filtering on user context](https://docs.aws.amazon.com/kendra/latest/dg/user-context-filter.html) .

CrawlArchivedSpaces -> (boolean)

`TRUE` to index archived spaces.

IncludeSpaces -> (list)

A list of space keys for Confluence spaces. If you include a key, the blogs, documents, and attachments in the space are indexed. Spaces that arenât in the list arenât indexed. A space in the list must exist. Otherwise, Amazon Kendra logs an error when the data source is synchronized. If a space is in both the `IncludeSpaces` and the `ExcludeSpaces` list, the space is excluded.

(string)

ExcludeSpaces -> (list)

A list of space keys of Confluence spaces. If you include a key, the blogs, documents, and attachments in the space are not indexed. If a space is in both the `ExcludeSpaces` and the `IncludeSpaces` list, the space is excluded.

(string)

SpaceFieldMappings -> (list)

Maps attributes or field names of Confluence spaces to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Confluence data source field names must exist in your Confluence custom metadata.

If you specify the `SpaceFieldMappings` parameter, you must specify at least one field mapping.

(structure)

Maps attributes or field names of Confluence spaces to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Confluence data source field names must exist in your Confluence custom metadata.

DataSourceFieldName -> (string)

The name of the field in the data source.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the Confluence data source field. The index field type must match the Confluence field type.

PageConfiguration -> (structure)

Configuration information for indexing Confluence pages.

PageFieldMappings -> (list)

Maps attributes or field names of Confluence pages to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Confluence data source field names must exist in your Confluence custom metadata.

If you specify the `PageFieldMappings` parameter, you must specify at least one field mapping.

(structure)

Maps attributes or field names of Confluence pages to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Confluence data source field names must exist in your Confluence custom metadata.

DataSourceFieldName -> (string)

The name of the field in the data source.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the Confluence data source field. The index field type must match the Confluence field type.

BlogConfiguration -> (structure)

Configuration information for indexing Confluence blogs.

BlogFieldMappings -> (list)

Maps attributes or field names of Confluence blogs to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Confluence data source field names must exist in your Confluence custom metadata.

If you specify the `BlogFieldMappings` parameter, you must specify at least one field mapping.

(structure)

Maps attributes or field names of Confluence blog to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Confluence data source field names must exist in your Confluence custom metadata.

DataSourceFieldName -> (string)

The name of the field in the data source.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the Confluence data source field. The index field type must match the Confluence field type.

AttachmentConfiguration -> (structure)

Configuration information for indexing attachments to Confluence blogs and pages.

CrawlAttachments -> (boolean)

`TRUE` to index attachments of pages and blogs in Confluence.

AttachmentFieldMappings -> (list)

Maps attributes or field names of Confluence attachments to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Confluence data source field names must exist in your Confluence custom metadata.

If you specify the `AttachentFieldMappings` parameter, you must specify at least one field mapping.

(structure)

Maps attributes or field names of Confluence attachments to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Confluence fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Confuence data source field names must exist in your Confluence custom metadata.

DataSourceFieldName -> (string)

The name of the field in the data source.

You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the Confluence data source field. The index field type must match the Confluence field type.

VpcConfiguration -> (structure)

Configuration information for an Amazon Virtual Private Cloud to connect to your Confluence. For more information, see [Configuring a VPC](https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html) .

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

InclusionPatterns -> (list)

A list of regular expression patterns to include certain blog posts, pages, spaces, or attachments in your Confluence. Content that matches the patterns are included in the index. Content that doesnât match the patterns is excluded from the index. If content matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the content isnât included in the index.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain blog posts, pages, spaces, or attachments in your Confluence. Content that matches the patterns are excluded from the index. Content that doesnât match the patterns is included in the index. If content matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the content isnât included in the index.

(string)

ProxyConfiguration -> (structure)

Configuration information to connect to your Confluence URL instance via a web proxy. You can use this option for Confluence Server.

You must provide the website host name and port number. For example, the host name of *https://a.example.com/page1.html* is âa.example.comâ and the port is 443, the standard port for HTTPS.

Web proxy credentials are optional and you can use them to connect to a web proxy server that requires basic authentication of user name and password. To store web proxy credentials, you use a secret in Secrets Manager.

It is recommended that you follow best security practices when configuring your web proxy. This includes setting up throttling, setting up logging and monitoring, and applying security patches on a regular basis. If you use your web proxy with multiple data sources, sync jobs that occur at the same time could strain the load on your proxy. It is recommended you prepare your proxy beforehand for any security and load requirements.

Host -> (string)

The name of the website host you want to connect to via a web proxy server.

For example, the host name of [https://a.example.com/page1.html](https://a.example.com/page1.html) is âa.example.comâ.

Port -> (integer)

The port number of the website host you want to connect to via a web proxy server.

For example, the port for [https://a.example.com/page1.html](https://a.example.com/page1.html) is 443, the standard port for HTTPS.

Credentials -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret. You create a secret to store your credentials in [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

The credentials are optional. You use a secret if web proxy credentials are required to connect to a website host. Amazon Kendra currently support basic authentication to connect to a web proxy server. The secret stores your credentials.

AuthenticationType -> (string)

Whether you want to connect to Confluence using basic authentication of user name and password, or a personal access token. You can use a personal access token for Confluence Server.

GoogleDriveConfiguration -> (structure)

Provides the configuration information to connect to Google Drive as your data source.

SecretArn -> (string)

The Amazon Resource Name (ARN) of a Secrets Managersecret that contains the credentials required to connect to Google Drive. For more information, see [Using a Google Workspace Drive data source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-google-drive.html) .

InclusionPatterns -> (list)

A list of regular expression patterns to include certain items in your Google Drive, including shared drives and usersâ My Drives. Items that match the patterns are included in the index. Items that donât match the patterns are excluded from the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isnât included in the index.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain items in your Google Drive, including shared drives and usersâ My Drives. Items that match the patterns are excluded from the index. Items that donât match the patterns are included in the index. If an item matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the item isnât included in the index.

(string)

FieldMappings -> (list)

Maps Google Drive data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Google Drive fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Google Drive data source field names must exist in your Google Drive custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

ExcludeMimeTypes -> (list)

A list of MIME types to exclude from the index. All documents matching the specified MIME type are excluded.

For a list of MIME types, see [Using a Google Workspace Drive data source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-google-drive.html) .

(string)

ExcludeUserAccounts -> (list)

A list of email addresses of the users. Documents owned by these users are excluded from the index. Documents shared with excluded users are indexed unless they are excluded in another way.

(string)

ExcludeSharedDrives -> (list)

A list of identifiers or shared drives to exclude from the index. All files and folders stored on the shared drive are excluded.

(string)

WebCrawlerConfiguration -> (structure)

Provides the configuration information required for Amazon Kendra Web Crawler.

Urls -> (structure)

Specifies the seed or starting point URLs of the websites or the sitemap URLs of the websites you want to crawl.

You can include website subdomains. You can list up to 100 seed URLs and up to three sitemap URLs.

You can only crawl websites that use the secure communication protocol, Hypertext Transfer Protocol Secure (HTTPS). If you receive an error when crawling a website, it could be that the website is blocked from crawling.

*When selecting websites to index, you must adhere to the `Amazon Acceptable Use Policy <https://aws.amazon.com/aup/>`__ and all other Amazon terms. Remember that you must only use Amazon Kendra Web Crawler to index your own web pages, or web pages that you have authorization to index.*

SeedUrlConfiguration -> (structure)

Configuration of the seed or starting point URLs of the websites you want to crawl.

You can choose to crawl only the website host names, or the website host names with subdomains, or the website host names with subdomains and other domains that the web pages link to.

You can list up to 100 seed URLs.

SeedUrls -> (list)

The list of seed or starting point URLs of the websites you want to crawl.

The list can include a maximum of 100 seed URLs.

(string)

WebCrawlerMode -> (string)

You can choose one of the following modes:

- `HOST_ONLY` âcrawl only the website host names. For example, if the seed URL is âabc.example.comâ, then only URLs with host name âabc.example.comâ are crawled.
- `SUBDOMAINS` âcrawl the website host names with subdomains. For example, if the seed URL is âabc.example.comâ, then âa.abc.example.comâ and âb.abc.example.comâ are also crawled.
- `EVERYTHING` âcrawl the website host names with subdomains and other domains that the web pages link to.

The default mode is set to `HOST_ONLY` .

SiteMapsConfiguration -> (structure)

Configuration of the sitemap URLs of the websites you want to crawl.

Only URLs belonging to the same website host names are crawled. You can list up to three sitemap URLs.

SiteMaps -> (list)

The list of sitemap URLs of the websites you want to crawl.

The list can include a maximum of three sitemap URLs.

(string)

CrawlDepth -> (integer)

The âdepthâ or number of levels from the seed level to crawl. For example, the seed URL page is depth 1 and any hyperlinks on this page that are also crawled are depth 2.

MaxLinksPerPage -> (integer)

The maximum number of URLs on a web page to include when crawling a website. This number is per web page.

As a websiteâs web pages are crawled, any URLs the web pages link to are also crawled. URLs on a web page are crawled in order of appearance.

The default maximum links per page is 100.

MaxContentSizePerPageInMegaBytes -> (float)

The maximum size (in MB) of a web page or attachment to crawl.

Files larger than this size (in MB) are skipped/not crawled.

The default maximum size of a web page or attachment is set to 50 MB.

MaxUrlsPerMinuteCrawlRate -> (integer)

The maximum number of URLs crawled per website host per minute.

A minimum of one URL is required.

The default maximum number of URLs crawled per website host per minute is 300.

UrlInclusionPatterns -> (list)

A list of regular expression patterns to include certain URLs to crawl. URLs that match the patterns are included in the index. URLs that donât match the patterns are excluded from the index. If a URL matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the URL file isnât included in the index.

(string)

UrlExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain URLs to crawl. URLs that match the patterns are excluded from the index. URLs that donât match the patterns are included in the index. If a URL matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the URL file isnât included in the index.

(string)

ProxyConfiguration -> (structure)

Configuration information required to connect to your internal websites via a web proxy.

You must provide the website host name and port number. For example, the host name of [https://a.example.com/page1.html](https://a.example.com/page1.html) is âa.example.comâ and the port is 443, the standard port for HTTPS.

Web proxy credentials are optional and you can use them to connect to a web proxy server that requires basic authentication. To store web proxy credentials, you use a secret in [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) .

Host -> (string)

The name of the website host you want to connect to via a web proxy server.

For example, the host name of [https://a.example.com/page1.html](https://a.example.com/page1.html) is âa.example.comâ.

Port -> (integer)

The port number of the website host you want to connect to via a web proxy server.

For example, the port for [https://a.example.com/page1.html](https://a.example.com/page1.html) is 443, the standard port for HTTPS.

Credentials -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret. You create a secret to store your credentials in [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

The credentials are optional. You use a secret if web proxy credentials are required to connect to a website host. Amazon Kendra currently support basic authentication to connect to a web proxy server. The secret stores your credentials.

AuthenticationConfiguration -> (structure)

Configuration information required to connect to websites using authentication.

You can connect to websites using basic authentication of user name and password. You use a secret in [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) to store your authentication credentials.

You must provide the website host name and port number. For example, the host name of [https://a.example.com/page1.html](https://a.example.com/page1.html) is âa.example.comâ and the port is 443, the standard port for HTTPS.

BasicAuthentication -> (list)

The list of configuration information thatâs required to connect to and crawl a website host using basic authentication credentials.

The list includes the name and port number of the website host.

(structure)

Provides the configuration information to connect to websites that require basic user authentication.

Host -> (string)

The name of the website host you want to connect to using authentication credentials.

For example, the host name of [https://a.example.com/page1.html](https://a.example.com/page1.html) is âa.example.comâ.

Port -> (integer)

The port number of the website host you want to connect to using authentication credentials.

For example, the port for [https://a.example.com/page1.html](https://a.example.com/page1.html) is 443, the standard port for HTTPS.

Credentials -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret. You create a secret to store your credentials in [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html)

You use a secret if basic authentication credentials are required to connect to a website. The secret stores your credentials of user name and password.

WorkDocsConfiguration -> (structure)

Provides the configuration information to connect to Amazon WorkDocs as your data source.

OrganizationId -> (string)

The identifier of the directory corresponding to your Amazon WorkDocs site repository.

You can find the organization ID in the [Directory Service](https://console.aws.amazon.com/directoryservicev2/) by going to **Active Directory** , then **Directories** . Your Amazon WorkDocs site directory has an ID, which is the organization ID. You can also set up a new Amazon WorkDocs directory in the Directory Service console and enable a Amazon WorkDocs site for the directory in the Amazon WorkDocs console.

CrawlComments -> (boolean)

`TRUE` to include comments on documents in your index. Including comments in your index means each comment is a document that can be searched on.

The default is set to `FALSE` .

UseChangeLog -> (boolean)

`TRUE` to use the Amazon WorkDocs change log to determine which documents require updating in the index. Depending on the change logâs size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in Amazon WorkDocs.

InclusionPatterns -> (list)

A list of regular expression patterns to include certain files in your Amazon WorkDocs site repository. Files that match the patterns are included in the index. Files that donât match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain files in your Amazon WorkDocs site repository. Files that match the patterns are excluded from the index. Files that donât match the patterns are included in the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

FieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map Amazon WorkDocs data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Amazon WorkDocs fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Amazon WorkDocs data source field names must exist in your Amazon WorkDocs custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

FsxConfiguration -> (structure)

Provides the configuration information to connect to Amazon FSx as your data source.

### Note

Amazon Kendra now supports an upgraded Amazon FSx Windows connector.

You must now use the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) object instead of the `FsxConfiguration` object to configure your connector.

Connectors configured using the older console and API architecture will continue to function as configured. However, you wonât be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.

We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.

FileSystemId -> (string)

The identifier of the Amazon FSx file system.

You can find your file system ID on the file system dashboard in the Amazon FSx console. For information on how to create a file system in Amazon FSx console, using Windows File Server as an example, see [Amazon FSx Getting started guide](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/getting-started-step1.html) .

FileSystemType -> (string)

The Amazon FSx file system type. Windows is currently the only supported type.

VpcConfiguration -> (structure)

Configuration information for an Amazon Virtual Private Cloud to connect to your Amazon FSx. Your Amazon FSx instance must reside inside your VPC.

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs required to connect to your Amazon FSx file system. Windows is currently the only supported type. The secret must contain a JSON structure with the following keys:

- usernameâThe Active Directory user name, along with the Domain Name System (DNS) domain name. For example, *user@corp.example.com* . The Active Directory user account must have read and mounting access to the Amazon FSx file system for Windows.
- passwordâThe password of the Active Directory user account with read and mounting access to the Amazon FSx Windows file system.

InclusionPatterns -> (list)

A list of regular expression patterns to include certain files in your Amazon FSx file system. Files that match the patterns are included in the index. Files that donât match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain files in your Amazon FSx file system. Files that match the patterns are excluded from the index. Files that donât match the patterns are included in the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

FieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map Amazon FSx data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Amazon FSx fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Amazon FSx data source field names must exist in your Amazon FSx custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

SlackConfiguration -> (structure)

Provides the configuration information to connect to Slack as your data source.

### Note

Amazon Kendra now supports an upgraded Slack connector.

You must now use the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) object instead of the `SlackConfiguration` object to configure your connector.

Connectors configured using the older console and API architecture will continue to function as configured. However, you wonât be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.

We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.

TeamId -> (string)

The identifier of the team in the Slack workspace. For example, *T0123456789* .

You can find your team ID in the URL of the main page of your Slack workspace. When you log in to Slack via a browser, you are directed to the URL of the main page. For example, *https://app.slack.com/client/**T0123456789** /â¦* .

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs required to connect to your Slack workspace team. The secret must contain a JSON structure with the following keys:

- slackTokenâThe user or bot token created in Slack. For more information on creating a token in Slack, see [Authentication for a Slack data source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-slack.html#slack-authentication) .

VpcConfiguration -> (structure)

Configuration information for an Amazon Virtual Private Cloud to connect to your Slack. For more information, see [Configuring a VPC](https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html) .

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

SlackEntityList -> (list)

Specify whether to index public channels, private channels, group messages, and direct messages. You can specify one or more of these options.

(string)

UseChangeLog -> (boolean)

`TRUE` to use the Slack change log to determine which documents require updating in the index. Depending on the Slack change logâs size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in Slack.

CrawlBotMessage -> (boolean)

`TRUE` to index bot messages from your Slack workspace team.

ExcludeArchived -> (boolean)

`TRUE` to exclude archived messages to index from your Slack workspace team.

SinceCrawlDate -> (string)

The date to start crawling your data from your Slack workspace team. The date must follow this format: `yyyy-mm-dd` .

LookBackPeriod -> (integer)

The number of hours for change log to look back from when you last synchronized your data. You can look back up to 7 days or 168 hours.

Change log updates your index only if new content was added since you last synced your data. Updated or deleted content from before you last synced does not get updated in your index. To capture updated or deleted content before you last synced, set the `LookBackPeriod` to the number of hours you want change log to look back.

PrivateChannelFilter -> (list)

The list of private channel names from your Slack workspace team. You use this if you want to index specific private channels, not all private channels. You can also use regular expression patterns to filter private channels.

(string)

PublicChannelFilter -> (list)

The list of public channel names to index from your Slack workspace team. You use this if you want to index specific public channels, not all public channels. You can also use regular expression patterns to filter public channels.

(string)

InclusionPatterns -> (list)

A list of regular expression patterns to include certain attached files in your Slack workspace team. Files that match the patterns are included in the index. Files that donât match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain attached files in your Slack workspace team. Files that match the patterns are excluded from the index. Files that donât match the patterns are included in the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

FieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map Slack data source attributes or field names to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Slack fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Slack data source field names must exist in your Slack custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

BoxConfiguration -> (structure)

Provides the configuration information to connect to Box as your data source.

EnterpriseId -> (string)

The identifier of the Box Enterprise platform. You can find the enterprise ID in the Box Developer Console settings or when you create an app in Box and download your authentication credentials. For example, *801234567* .

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs required to connect to your Box platform. The secret must contain a JSON structure with the following keys:

- clientIDâThe identifier of the client OAuth 2.0 authentication application created in Box.
- clientSecretâA set of characters known only to the OAuth 2.0 authentication application created in Box.
- publicKeyIdâThe identifier of the public key contained within an identity certificate.
- privateKeyâA set of characters that make up an encryption key.
- passphraseâA set of characters that act like a password.

You create an application in Box to generate the keys or credentials required for the secret. For more information, see [Using a Box data source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-box.html) .

UseChangeLog -> (boolean)

`TRUE` to use the Slack change log to determine which documents require updating in the index. Depending on the data source change logâs size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents.

CrawlComments -> (boolean)

`TRUE` to index comments.

CrawlTasks -> (boolean)

`TRUE` to index the contents of tasks.

CrawlWebLinks -> (boolean)

`TRUE` to index web links.

FileFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Box files to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Box fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Box field names must exist in your Box custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

TaskFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Box tasks to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Box fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Box field names must exist in your Box custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

CommentFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Box comments to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Box fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Box field names must exist in your Box custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

WebLinkFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Box web links to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Box fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Box field names must exist in your Box custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

InclusionPatterns -> (list)

A list of regular expression patterns to include certain files and folders in your Box platform. Files and folders that match the patterns are included in the index. Files and folders that donât match the patterns are excluded from the index. If a file or folder matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file or folder isnât included in the index.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain files and folders from your Box platform. Files and folders that match the patterns are excluded from the index.Files and folders that donât match the patterns are included in the index. If a file or folder matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file or folder isnât included in the index.

(string)

VpcConfiguration -> (structure)

Configuration information for an Amazon VPC to connect to your Box. For more information, see [Configuring a VPC](https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html) .

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

QuipConfiguration -> (structure)

Provides the configuration information to connect to Quip as your data source.

Domain -> (string)

The Quip site domain. For example, *https://quip-company.quipdomain.com/browse* . The domain in this example is âquipdomainâ.

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs that are required to connect to your Quip. The secret must contain a JSON structure with the following keys:

- accessTokenâThe token created in Quip. For more information, see [Using a Quip data source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-slack.html) .

CrawlFileComments -> (boolean)

`TRUE` to index file comments.

CrawlChatRooms -> (boolean)

`TRUE` to index the contents of chat rooms.

CrawlAttachments -> (boolean)

`TRUE` to index attachments.

FolderIds -> (list)

The identifiers of the Quip folders you want to index. You can find the folder ID in your browser URL when you access your folder in Quip. For example, *https://quip-company.quipdomain.com/zlLuOVNSarTL/folder-name* . The folder ID in this example is âzlLuOVNSarTLâ.

(string)

ThreadFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Quip threads to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Quip fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Quip field names must exist in your Quip custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

MessageFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Quip messages to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Quip fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Quip field names must exist in your Quip custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

AttachmentFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Quip attachments to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Quip fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Quip field names must exist in your Quip custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

InclusionPatterns -> (list)

A list of regular expression patterns to include certain files in your Quip file system. Files that match the patterns are included in the index. Files that donât match the patterns are excluded from the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence, and the file isnât included in the index.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain files in your Quip file system. Files that match the patterns are excluded from the index. Files that donât match the patterns are included in the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence, and the file isnât included in the index.

(string)

VpcConfiguration -> (structure)

Configuration information for an Amazon Virtual Private Cloud (VPC) to connect to your Quip. For more information, see [Configuring a VPC](https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html) .

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

JiraConfiguration -> (structure)

Provides the configuration information to connect to Jira as your data source.

JiraAccountUrl -> (string)

The URL of the Jira account. For example, *company.atlassian.net* .

SecretArn -> (string)

The Amazon Resource Name (ARN) of a secret in Secrets Manager contains the key-value pairs required to connect to your Jira data source. The secret must contain a JSON structure with the following keys:

- jiraIdâThe Jira user name or email.
- jiraCredentialsâThe Jira API token. For more information, see [Using a Jira data source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-jira.html) .

UseChangeLog -> (boolean)

`TRUE` to use the Jira change log to determine which documents require updating in the index. Depending on the change logâs size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in Jira.

Project -> (list)

Specify which projects to crawl in your Jira data source. You can specify one or more Jira project IDs.

(string)

IssueType -> (list)

Specify which issue types to crawl in your Jira data source. You can specify one or more of these options to crawl.

(string)

Status -> (list)

Specify which statuses to crawl in your Jira data source. You can specify one or more of these options to crawl.

(string)

IssueSubEntityFilter -> (list)

Specify whether to crawl comments, attachments, and work logs. You can specify one or more of these options.

(string)

AttachmentFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Jira attachments to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Jira fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Jira data source field names must exist in your Jira custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

CommentFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Jira comments to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Jira fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Jira data source field names must exist in your Jira custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

IssueFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Jira issues to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Jira fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Jira data source field names must exist in your Jira custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

ProjectFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Jira projects to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Jira fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Jira data source field names must exist in your Jira custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

WorkLogFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Jira work logs to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Jira fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Jira data source field names must exist in your Jira custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

InclusionPatterns -> (list)

A list of regular expression patterns to include certain file paths, file names, and file types in your Jira data source. Files that match the patterns are included in the index. Files that donât match the patterns are excluded from the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain file paths, file names, and file types in your Jira data source. Files that match the patterns are excluded from the index. Files that donât match the patterns are included in the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

VpcConfiguration -> (structure)

Configuration information for an Amazon Virtual Private Cloud to connect to your Jira. For more information, see [Configuring a VPC](https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html) .

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

GitHubConfiguration -> (structure)

Provides the configuration information to connect to GitHub as your data source.

### Note

Amazon Kendra now supports an upgraded GitHub connector.

You must now use the [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) object instead of the `GitHubConfiguration` object to configure your connector.

Connectors configured using the older console and API architecture will continue to function as configured. However, you wonât be able to edit or update them. If you want to edit or update your connector configuration, you must create a new connector.

We recommended migrating your connector workflow to the upgraded version. Support for connectors configured using the older architecture is scheduled to end by June 2024.

SaaSConfiguration -> (structure)

Configuration information to connect to GitHub Enterprise Cloud (SaaS).

OrganizationName -> (string)

The name of the organization of the GitHub Enterprise Cloud (SaaS) account you want to connect to. You can find your organization name by logging into GitHub desktop and selecting **Your organizations** under your profile picture dropdown.

HostUrl -> (string)

The GitHub host URL or API endpoint URL. For example, *https://api.github.com* .

OnPremiseConfiguration -> (structure)

Configuration information to connect to GitHub Enterprise Server (on premises).

HostUrl -> (string)

The GitHub host URL or API endpoint URL. For example, *https://on-prem-host-url/api/v3/*

OrganizationName -> (string)

The name of the organization of the GitHub Enterprise Server (on-premises) account you want to connect to. You can find your organization name by logging into GitHub desktop and selecting **Your organizations** under your profile picture dropdown.

SslCertificateS3Path -> (structure)

The path to the SSL certificate stored in an Amazon S3 bucket. You use this to connect to GitHub if you require a secure SSL connection.

You can simply generate a self-signed X509 certificate on any computer using OpenSSL. For an example of using OpenSSL to create an X509 certificate, see [Create and sign an X509 certificate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html) .

Bucket -> (string)

The name of the S3 bucket that contains the file.

Key -> (string)

The name of the file.

Type -> (string)

The type of GitHub service you want to connect toâGitHub Enterprise Cloud (SaaS) or GitHub Enterprise Server (on premises).

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs required to connect to your GitHub. The secret must contain a JSON structure with the following keys:

- personalTokenâThe access token created in GitHub. For more information on creating a token in GitHub, see [Using a GitHub data source](https://docs.aws.amazon.com/kendra/latest/dg/data-source-github.html) .

UseChangeLog -> (boolean)

`TRUE` to use the GitHub change log to determine which documents require updating in the index. Depending on the GitHub change logâs size, it may take longer for Amazon Kendra to use the change log than to scan all of your documents in GitHub.

GitHubDocumentCrawlProperties -> (structure)

Configuration information to include certain types of GitHub content. You can configure to index repository files only, or also include issues and pull requests, comments, and comment attachments.

CrawlRepositoryDocuments -> (boolean)

`TRUE` to index all files with a repository.

CrawlIssue -> (boolean)

`TRUE` to index all issues within a repository.

CrawlIssueComment -> (boolean)

`TRUE` to index all comments on issues.

CrawlIssueCommentAttachment -> (boolean)

`TRUE` to include all comment attachments for issues.

CrawlPullRequest -> (boolean)

`TRUE` to index all pull requests within a repository.

CrawlPullRequestComment -> (boolean)

`TRUE` to index all comments on pull requests.

CrawlPullRequestCommentAttachment -> (boolean)

`TRUE` to include all comment attachments for pull requests.

RepositoryFilter -> (list)

A list of names of the specific repositories you want to index.

(string)

InclusionFolderNamePatterns -> (list)

A list of regular expression patterns to include certain folder names in your GitHub repository or repositories. Folder names that match the patterns are included in the index. Folder names that donât match the patterns are excluded from the index. If a folder matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the folder isnât included in the index.

(string)

InclusionFileTypePatterns -> (list)

A list of regular expression patterns to include certain file types in your GitHub repository or repositories. File types that match the patterns are included in the index. File types that donât match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

InclusionFileNamePatterns -> (list)

A list of regular expression patterns to include certain file names in your GitHub repository or repositories. File names that match the patterns are included in the index. File names that donât match the patterns are excluded from the index. If a file matches both an inclusion and exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

ExclusionFolderNamePatterns -> (list)

A list of regular expression patterns to exclude certain folder names in your GitHub repository or repositories. Folder names that match the patterns are excluded from the index. Folder names that donât match the patterns are included in the index. If a folder matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence and the folder isnât included in the index.

(string)

ExclusionFileTypePatterns -> (list)

A list of regular expression patterns to exclude certain file types in your GitHub repository or repositories. File types that match the patterns are excluded from the index. File types that donât match the patterns are included in the index. If a file matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

ExclusionFileNamePatterns -> (list)

A list of regular expression patterns to exclude certain file names in your GitHub repository or repositories. File names that match the patterns are excluded from the index. File names that donât match the patterns are included in the index. If a file matches both an exclusion and inclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

VpcConfiguration -> (structure)

Configuration information of an Amazon Virtual Private Cloud to connect to your GitHub. For more information, see [Configuring a VPC](https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html) .

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

GitHubRepositoryConfigurationFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map GitHub repository attributes or field names to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to GitHub fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The GitHub data source field names must exist in your GitHub custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

GitHubCommitConfigurationFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of GitHub commits to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to GitHub fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The GitHub data source field names must exist in your GitHub custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

GitHubIssueDocumentConfigurationFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of GitHub issues to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to GitHub fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The GitHub data source field names must exist in your GitHub custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

GitHubIssueCommentConfigurationFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of GitHub issue comments to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to GitHub fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The GitHub data source field names must exist in your GitHub custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

GitHubIssueAttachmentConfigurationFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of GitHub issue attachments to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to GitHub fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The GitHub data source field names must exist in your GitHub custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

GitHubPullRequestCommentConfigurationFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of GitHub pull request comments to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to GitHub fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The GitHub data source field names must exist in your GitHub custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

GitHubPullRequestDocumentConfigurationFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of GitHub pull requests to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to GitHub fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The GitHub data source field names must exist in your GitHub custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

GitHubPullRequestDocumentAttachmentConfigurationFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of GitHub pull request attachments to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to GitHub fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The GitHub data source field names must exist in your GitHub custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

AlfrescoConfiguration -> (structure)

Provides the configuration information to connect to Alfresco as your data source.

### Note

Support for `AlfrescoConfiguration` ended May 2023. We recommend migrating to or using the Alfresco data source template schema / [TemplateConfiguration](https://docs.aws.amazon.com/kendra/latest/APIReference/API_TemplateConfiguration.html) API.

SiteUrl -> (string)

The URL of the Alfresco site. For example, *https://hostname:8080* .

SiteId -> (string)

The identifier of the Alfresco site. For example, *my-site* .

SecretArn -> (string)

The Amazon Resource Name (ARN) of an Secrets Manager secret that contains the key-value pairs required to connect to your Alfresco data source. The secret must contain a JSON structure with the following keys:

- usernameâThe user name of the Alfresco account.
- passwordâThe password of the Alfresco account.

SslCertificateS3Path -> (structure)

The path to the SSL certificate stored in an Amazon S3 bucket. You use this to connect to Alfresco if you require a secure SSL connection.

You can simply generate a self-signed X509 certificate on any computer using OpenSSL. For an example of using OpenSSL to create an X509 certificate, see [Create and sign an X509 certificate](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/configuring-https-ssl.html) .

Bucket -> (string)

The name of the S3 bucket that contains the file.

Key -> (string)

The name of the file.

CrawlSystemFolders -> (boolean)

`TRUE` to index shared files.

CrawlComments -> (boolean)

`TRUE` to index comments of blogs and other content.

EntityFilter -> (list)

Specify whether to index document libraries, wikis, or blogs. You can specify one or more of these options.

(string)

DocumentLibraryFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Alfresco document libraries to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Alfresco fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Alfresco data source field names must exist in your Alfresco custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

BlogFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Alfresco blogs to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Alfresco fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Alfresco data source field names must exist in your Alfresco custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

WikiFieldMappings -> (list)

A list of `DataSourceToIndexFieldMapping` objects that map attributes or field names of Alfresco wikis to Amazon Kendra index field names. To create custom fields, use the `UpdateIndex` API before you map to Alfresco fields. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) . The Alfresco data source field names must exist in your Alfresco custom metadata.

(structure)

Maps attributes or field names of the documents synced from the data source to Amazon Kendra index field names. You can set up field mappings for each data source when calling [CreateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_CreateDataSource.html) or [UpdateDataSource](https://docs.aws.amazon.com/kendra/latest/APIReference/API_UpdateDataSource.html) API. To create custom fields, use the `UpdateIndex` API to first create an index field and then map to the data source field. For more information, see [Mapping data source fields](https://docs.aws.amazon.com/kendra/latest/dg/field-mapping.html) .

DataSourceFieldName -> (string)

The name of the field in the data source. You must first create the index field using the `UpdateIndex` API.

DateFieldFormat -> (string)

The format for date fields in the data source. If the field specified in `DataSourceFieldName` is a date field, you must specify the date format. If the field is not a date field, an exception is thrown.

IndexFieldName -> (string)

The name of the index field to map to the data source field. The index field type must match the data source field type.

InclusionPatterns -> (list)

A list of regular expression patterns to include certain files in your Alfresco data source. Files that match the patterns are included in the index. Files that donât match the patterns are excluded from the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

ExclusionPatterns -> (list)

A list of regular expression patterns to exclude certain files in your Alfresco data source. Files that match the patterns are excluded from the index. Files that donât match the patterns are included in the index. If a file matches both an inclusion pattern and an exclusion pattern, the exclusion pattern takes precedence and the file isnât included in the index.

(string)

VpcConfiguration -> (structure)

Configuration information for an Amazon Virtual Private Cloud to connect to your Alfresco. For more information, see [Configuring a VPC](https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html) .

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

TemplateConfiguration -> (structure)

Provides a template for the configuration information to connect to your data source.

Template -> (document)

The template schema used for the data source, where templates schemas are supported.

See [Data source template schemas](https://docs.aws.amazon.com/kendra/latest/dg/ds-schemas.html) .

JSON Syntax:

```
{
  "S3Configuration": {
    "BucketName": "string",
    "InclusionPrefixes": ["string", ...],
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "DocumentsMetadataConfiguration": {
      "S3Prefix": "string"
    },
    "AccessControlListConfiguration": {
      "KeyPath": "string"
    }
  },
  "SharePointConfiguration": {
    "SharePointVersion": "SHAREPOINT_2013"|"SHAREPOINT_2016"|"SHAREPOINT_ONLINE"|"SHAREPOINT_2019",
    "Urls": ["string", ...],
    "SecretArn": "string",
    "CrawlAttachments": true|false,
    "UseChangeLog": true|false,
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "VpcConfiguration": {
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...]
    },
    "FieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "DocumentTitleFieldName": "string",
    "DisableLocalGroups": true|false,
    "SslCertificateS3Path": {
      "Bucket": "string",
      "Key": "string"
    },
    "AuthenticationType": "HTTP_BASIC"|"OAUTH2",
    "ProxyConfiguration": {
      "Host": "string",
      "Port": integer,
      "Credentials": "string"
    }
  },
  "DatabaseConfiguration": {
    "DatabaseEngineType": "RDS_AURORA_MYSQL"|"RDS_AURORA_POSTGRESQL"|"RDS_MYSQL"|"RDS_POSTGRESQL",
    "ConnectionConfiguration": {
      "DatabaseHost": "string",
      "DatabasePort": integer,
      "DatabaseName": "string",
      "TableName": "string",
      "SecretArn": "string"
    },
    "VpcConfiguration": {
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...]
    },
    "ColumnConfiguration": {
      "DocumentIdColumnName": "string",
      "DocumentDataColumnName": "string",
      "DocumentTitleColumnName": "string",
      "FieldMappings": [
        {
          "DataSourceFieldName": "string",
          "DateFieldFormat": "string",
          "IndexFieldName": "string"
        }
        ...
      ],
      "ChangeDetectingColumns": ["string", ...]
    },
    "AclConfiguration": {
      "AllowedGroupsColumnName": "string"
    },
    "SqlConfiguration": {
      "QueryIdentifiersEnclosingOption": "DOUBLE_QUOTES"|"NONE"
    }
  },
  "SalesforceConfiguration": {
    "ServerUrl": "string",
    "SecretArn": "string",
    "StandardObjectConfigurations": [
      {
        "Name": "ACCOUNT"|"CAMPAIGN"|"CASE"|"CONTACT"|"CONTRACT"|"DOCUMENT"|"GROUP"|"IDEA"|"LEAD"|"OPPORTUNITY"|"PARTNER"|"PRICEBOOK"|"PRODUCT"|"PROFILE"|"SOLUTION"|"TASK"|"USER",
        "DocumentDataFieldName": "string",
        "DocumentTitleFieldName": "string",
        "FieldMappings": [
          {
            "DataSourceFieldName": "string",
            "DateFieldFormat": "string",
            "IndexFieldName": "string"
          }
          ...
        ]
      }
      ...
    ],
    "KnowledgeArticleConfiguration": {
      "IncludedStates": ["DRAFT"|"PUBLISHED"|"ARCHIVED", ...],
      "StandardKnowledgeArticleTypeConfiguration": {
        "DocumentDataFieldName": "string",
        "DocumentTitleFieldName": "string",
        "FieldMappings": [
          {
            "DataSourceFieldName": "string",
            "DateFieldFormat": "string",
            "IndexFieldName": "string"
          }
          ...
        ]
      },
      "CustomKnowledgeArticleTypeConfigurations": [
        {
          "Name": "string",
          "DocumentDataFieldName": "string",
          "DocumentTitleFieldName": "string",
          "FieldMappings": [
            {
              "DataSourceFieldName": "string",
              "DateFieldFormat": "string",
              "IndexFieldName": "string"
            }
            ...
          ]
        }
        ...
      ]
    },
    "ChatterFeedConfiguration": {
      "DocumentDataFieldName": "string",
      "DocumentTitleFieldName": "string",
      "FieldMappings": [
        {
          "DataSourceFieldName": "string",
          "DateFieldFormat": "string",
          "IndexFieldName": "string"
        }
        ...
      ],
      "IncludeFilterTypes": ["ACTIVE_USER"|"STANDARD_USER", ...]
    },
    "CrawlAttachments": true|false,
    "StandardObjectAttachmentConfiguration": {
      "DocumentTitleFieldName": "string",
      "FieldMappings": [
        {
          "DataSourceFieldName": "string",
          "DateFieldFormat": "string",
          "IndexFieldName": "string"
        }
        ...
      ]
    },
    "IncludeAttachmentFilePatterns": ["string", ...],
    "ExcludeAttachmentFilePatterns": ["string", ...]
  },
  "OneDriveConfiguration": {
    "TenantDomain": "string",
    "SecretArn": "string",
    "OneDriveUsers": {
      "OneDriveUserList": ["string", ...],
      "OneDriveUserS3Path": {
        "Bucket": "string",
        "Key": "string"
      }
    },
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "FieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "DisableLocalGroups": true|false
  },
  "ServiceNowConfiguration": {
    "HostUrl": "string",
    "SecretArn": "string",
    "ServiceNowBuildVersion": "LONDON"|"OTHERS",
    "KnowledgeArticleConfiguration": {
      "CrawlAttachments": true|false,
      "IncludeAttachmentFilePatterns": ["string", ...],
      "ExcludeAttachmentFilePatterns": ["string", ...],
      "DocumentDataFieldName": "string",
      "DocumentTitleFieldName": "string",
      "FieldMappings": [
        {
          "DataSourceFieldName": "string",
          "DateFieldFormat": "string",
          "IndexFieldName": "string"
        }
        ...
      ],
      "FilterQuery": "string"
    },
    "ServiceCatalogConfiguration": {
      "CrawlAttachments": true|false,
      "IncludeAttachmentFilePatterns": ["string", ...],
      "ExcludeAttachmentFilePatterns": ["string", ...],
      "DocumentDataFieldName": "string",
      "DocumentTitleFieldName": "string",
      "FieldMappings": [
        {
          "DataSourceFieldName": "string",
          "DateFieldFormat": "string",
          "IndexFieldName": "string"
        }
        ...
      ]
    },
    "AuthenticationType": "HTTP_BASIC"|"OAUTH2"
  },
  "ConfluenceConfiguration": {
    "ServerUrl": "string",
    "SecretArn": "string",
    "Version": "CLOUD"|"SERVER",
    "SpaceConfiguration": {
      "CrawlPersonalSpaces": true|false,
      "CrawlArchivedSpaces": true|false,
      "IncludeSpaces": ["string", ...],
      "ExcludeSpaces": ["string", ...],
      "SpaceFieldMappings": [
        {
          "DataSourceFieldName": "DISPLAY_URL"|"ITEM_TYPE"|"SPACE_KEY"|"URL",
          "DateFieldFormat": "string",
          "IndexFieldName": "string"
        }
        ...
      ]
    },
    "PageConfiguration": {
      "PageFieldMappings": [
        {
          "DataSourceFieldName": "AUTHOR"|"CONTENT_STATUS"|"CREATED_DATE"|"DISPLAY_URL"|"ITEM_TYPE"|"LABELS"|"MODIFIED_DATE"|"PARENT_ID"|"SPACE_KEY"|"SPACE_NAME"|"URL"|"VERSION",
          "DateFieldFormat": "string",
          "IndexFieldName": "string"
        }
        ...
      ]
    },
    "BlogConfiguration": {
      "BlogFieldMappings": [
        {
          "DataSourceFieldName": "AUTHOR"|"DISPLAY_URL"|"ITEM_TYPE"|"LABELS"|"PUBLISH_DATE"|"SPACE_KEY"|"SPACE_NAME"|"URL"|"VERSION",
          "DateFieldFormat": "string",
          "IndexFieldName": "string"
        }
        ...
      ]
    },
    "AttachmentConfiguration": {
      "CrawlAttachments": true|false,
      "AttachmentFieldMappings": [
        {
          "DataSourceFieldName": "AUTHOR"|"CONTENT_TYPE"|"CREATED_DATE"|"DISPLAY_URL"|"FILE_SIZE"|"ITEM_TYPE"|"PARENT_ID"|"SPACE_KEY"|"SPACE_NAME"|"URL"|"VERSION",
          "DateFieldFormat": "string",
          "IndexFieldName": "string"
        }
        ...
      ]
    },
    "VpcConfiguration": {
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...]
    },
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "ProxyConfiguration": {
      "Host": "string",
      "Port": integer,
      "Credentials": "string"
    },
    "AuthenticationType": "HTTP_BASIC"|"PAT"
  },
  "GoogleDriveConfiguration": {
    "SecretArn": "string",
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "FieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "ExcludeMimeTypes": ["string", ...],
    "ExcludeUserAccounts": ["string", ...],
    "ExcludeSharedDrives": ["string", ...]
  },
  "WebCrawlerConfiguration": {
    "Urls": {
      "SeedUrlConfiguration": {
        "SeedUrls": ["string", ...],
        "WebCrawlerMode": "HOST_ONLY"|"SUBDOMAINS"|"EVERYTHING"
      },
      "SiteMapsConfiguration": {
        "SiteMaps": ["string", ...]
      }
    },
    "CrawlDepth": integer,
    "MaxLinksPerPage": integer,
    "MaxContentSizePerPageInMegaBytes": float,
    "MaxUrlsPerMinuteCrawlRate": integer,
    "UrlInclusionPatterns": ["string", ...],
    "UrlExclusionPatterns": ["string", ...],
    "ProxyConfiguration": {
      "Host": "string",
      "Port": integer,
      "Credentials": "string"
    },
    "AuthenticationConfiguration": {
      "BasicAuthentication": [
        {
          "Host": "string",
          "Port": integer,
          "Credentials": "string"
        }
        ...
      ]
    }
  },
  "WorkDocsConfiguration": {
    "OrganizationId": "string",
    "CrawlComments": true|false,
    "UseChangeLog": true|false,
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "FieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ]
  },
  "FsxConfiguration": {
    "FileSystemId": "string",
    "FileSystemType": "WINDOWS",
    "VpcConfiguration": {
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...]
    },
    "SecretArn": "string",
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "FieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ]
  },
  "SlackConfiguration": {
    "TeamId": "string",
    "SecretArn": "string",
    "VpcConfiguration": {
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...]
    },
    "SlackEntityList": ["PUBLIC_CHANNEL"|"PRIVATE_CHANNEL"|"GROUP_MESSAGE"|"DIRECT_MESSAGE", ...],
    "UseChangeLog": true|false,
    "CrawlBotMessage": true|false,
    "ExcludeArchived": true|false,
    "SinceCrawlDate": "string",
    "LookBackPeriod": integer,
    "PrivateChannelFilter": ["string", ...],
    "PublicChannelFilter": ["string", ...],
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "FieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ]
  },
  "BoxConfiguration": {
    "EnterpriseId": "string",
    "SecretArn": "string",
    "UseChangeLog": true|false,
    "CrawlComments": true|false,
    "CrawlTasks": true|false,
    "CrawlWebLinks": true|false,
    "FileFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "TaskFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "CommentFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "WebLinkFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "VpcConfiguration": {
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...]
    }
  },
  "QuipConfiguration": {
    "Domain": "string",
    "SecretArn": "string",
    "CrawlFileComments": true|false,
    "CrawlChatRooms": true|false,
    "CrawlAttachments": true|false,
    "FolderIds": ["string", ...],
    "ThreadFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "MessageFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "AttachmentFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "VpcConfiguration": {
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...]
    }
  },
  "JiraConfiguration": {
    "JiraAccountUrl": "string",
    "SecretArn": "string",
    "UseChangeLog": true|false,
    "Project": ["string", ...],
    "IssueType": ["string", ...],
    "Status": ["string", ...],
    "IssueSubEntityFilter": ["COMMENTS"|"ATTACHMENTS"|"WORKLOGS", ...],
    "AttachmentFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "CommentFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "IssueFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "ProjectFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "WorkLogFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "VpcConfiguration": {
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...]
    }
  },
  "GitHubConfiguration": {
    "SaaSConfiguration": {
      "OrganizationName": "string",
      "HostUrl": "string"
    },
    "OnPremiseConfiguration": {
      "HostUrl": "string",
      "OrganizationName": "string",
      "SslCertificateS3Path": {
        "Bucket": "string",
        "Key": "string"
      }
    },
    "Type": "SAAS"|"ON_PREMISE",
    "SecretArn": "string",
    "UseChangeLog": true|false,
    "GitHubDocumentCrawlProperties": {
      "CrawlRepositoryDocuments": true|false,
      "CrawlIssue": true|false,
      "CrawlIssueComment": true|false,
      "CrawlIssueCommentAttachment": true|false,
      "CrawlPullRequest": true|false,
      "CrawlPullRequestComment": true|false,
      "CrawlPullRequestCommentAttachment": true|false
    },
    "RepositoryFilter": ["string", ...],
    "InclusionFolderNamePatterns": ["string", ...],
    "InclusionFileTypePatterns": ["string", ...],
    "InclusionFileNamePatterns": ["string", ...],
    "ExclusionFolderNamePatterns": ["string", ...],
    "ExclusionFileTypePatterns": ["string", ...],
    "ExclusionFileNamePatterns": ["string", ...],
    "VpcConfiguration": {
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...]
    },
    "GitHubRepositoryConfigurationFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "GitHubCommitConfigurationFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "GitHubIssueDocumentConfigurationFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "GitHubIssueCommentConfigurationFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "GitHubIssueAttachmentConfigurationFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "GitHubPullRequestCommentConfigurationFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "GitHubPullRequestDocumentConfigurationFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "GitHubPullRequestDocumentAttachmentConfigurationFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ]
  },
  "AlfrescoConfiguration": {
    "SiteUrl": "string",
    "SiteId": "string",
    "SecretArn": "string",
    "SslCertificateS3Path": {
      "Bucket": "string",
      "Key": "string"
    },
    "CrawlSystemFolders": true|false,
    "CrawlComments": true|false,
    "EntityFilter": ["wiki"|"blog"|"documentLibrary", ...],
    "DocumentLibraryFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "BlogFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "WikiFieldMappings": [
      {
        "DataSourceFieldName": "string",
        "DateFieldFormat": "string",
        "IndexFieldName": "string"
      }
      ...
    ],
    "InclusionPatterns": ["string", ...],
    "ExclusionPatterns": ["string", ...],
    "VpcConfiguration": {
      "SubnetIds": ["string", ...],
      "SecurityGroupIds": ["string", ...]
    }
  },
  "TemplateConfiguration": {
    "Template": {...}
  }
}
```

`--vpc-configuration` (structure)

Configuration information for an Amazon Virtual Private Cloud to connect to your data source. For more information, see [Configuring a VPC](https://docs.aws.amazon.com/kendra/latest/dg/vpc-configuration.html) .

SubnetIds -> (list)

A list of identifiers for subnets within your Amazon VPC. The subnets should be able to connect to each other in the VPC, and they should have outgoing access to the Internet through a NAT device.

(string)

SecurityGroupIds -> (list)

A list of identifiers of security groups within your Amazon VPC. The security groups should enable Amazon Kendra to connect to the data source.

(string)

Shorthand Syntax:

```
SubnetIds=string,string,SecurityGroupIds=string,string
```

JSON Syntax:

```
{
  "SubnetIds": ["string", ...],
  "SecurityGroupIds": ["string", ...]
}
```

`--description` (string)

A new description for the data source connector.

`--schedule` (string)

The sync schedule you want to update for the data source connector.

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role with permission to access the data source and required resources. For more information, see [IAM roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

`--language-code` (string)

The code for a language you want to update for the data source connector. This allows you to support a language for all documents when updating the data source. English is supported by default. For more information on supported languages, including their codes, see [Adding documents in languages other than English](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html) .

`--custom-document-enrichment-configuration` (structure)

Configuration information you want to update for altering document metadata and content during the document ingestion process.

For more information on how to create, modify and delete document metadata, or make other content alterations when you ingest documents into Amazon Kendra, see [Customizing document metadata during the ingestion process](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html) .

InlineConfigurations -> (list)

Configuration information to alter document attributes or metadata fields and content when ingesting documents into Amazon Kendra.

(structure)

Provides the configuration information for applying basic logic to alter document metadata and content when ingesting documents into Amazon Kendra. To apply advanced logic, to go beyond what you can do with basic logic, see [HookConfiguration](https://docs.aws.amazon.com/kendra/latest/dg/API_HookConfiguration.html) .

For more information, see [Customizing document metadata during the ingestion process](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html) .

Condition -> (structure)

Configuration of the condition used for the target document attribute or metadata field when ingesting documents into Amazon Kendra.

ConditionDocumentAttributeKey -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Kendra currently does not support `_document_body` as an attribute key used for the condition.

Operator -> (string)

The condition operator.

For example, you can use âContainsâ to partially match a string.

ConditionOnValue -> (structure)

The value used by the operator.

For example, you can specify the value âfinancialâ for strings in the âSource_URIâ field that partially match or contain this value.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

Target -> (structure)

Configuration of the target document attribute or metadata field when ingesting documents into Amazon Kendra. You can also include a value.

TargetDocumentAttributeKey -> (string)

The identifier of the target document attribute or metadata field.

For example, âDepartmentâ could be an identifier for the target attribute or metadata field that includes the department names associated with the documents.

TargetDocumentAttributeValueDeletion -> (boolean)

`TRUE` to delete the existing target value for your specified target attribute key. You cannot create a target value and set this to `TRUE` . To create a target value (`TargetDocumentAttributeValue` ), set this to `FALSE` .

TargetDocumentAttributeValue -> (structure)

The target value you want to create for the target attribute.

For example, âFinanceâ could be the target value for the target attribute key âDepartmentâ.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

DocumentContentDeletion -> (boolean)

`TRUE` to delete content if the condition used for the target attribute is met.

PreExtractionHookConfiguration -> (structure)

Configuration information for invoking a Lambda function in Lambda on the original or raw documents before extracting their metadata and text. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see [Advanced data manipulation](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation) .

InvocationCondition -> (structure)

The condition used for when a Lambda function should be invoked.

For example, you can specify a condition that if there are empty date-time values, then Amazon Kendra should invoke a function that inserts the current date-time.

ConditionDocumentAttributeKey -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Kendra currently does not support `_document_body` as an attribute key used for the condition.

Operator -> (string)

The condition operator.

For example, you can use âContainsâ to partially match a string.

ConditionOnValue -> (structure)

The value used by the operator.

For example, you can specify the value âfinancialâ for strings in the âSource_URIâ field that partially match or contain this value.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

LambdaArn -> (string)

The Amazon Resource Name (ARN) of an IAM role with permission to run a Lambda function during ingestion. For more information, see [an IAM roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

S3Bucket -> (string)

Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see [Data contracts for Lambda functions](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#cde-data-contracts-lambda) .

PostExtractionHookConfiguration -> (structure)

Configuration information for invoking a Lambda function in Lambda on the structured documents with their metadata and text extracted. You can use a Lambda function to apply advanced logic for creating, modifying, or deleting document metadata and content. For more information, see [Advanced data manipulation](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#advanced-data-manipulation) .

InvocationCondition -> (structure)

The condition used for when a Lambda function should be invoked.

For example, you can specify a condition that if there are empty date-time values, then Amazon Kendra should invoke a function that inserts the current date-time.

ConditionDocumentAttributeKey -> (string)

The identifier of the document attribute used for the condition.

For example, âSource_URIâ could be an identifier for the attribute or metadata field that contains source URIs associated with the documents.

Amazon Kendra currently does not support `_document_body` as an attribute key used for the condition.

Operator -> (string)

The condition operator.

For example, you can use âContainsâ to partially match a string.

ConditionOnValue -> (structure)

The value used by the operator.

For example, you can specify the value âfinancialâ for strings in the âSource_URIâ field that partially match or contain this value.

StringValue -> (string)

A string, such as âdepartmentâ.

StringListValue -> (list)

A list of strings. The default maximum length or number of strings is 10.

(string)

LongValue -> (long)

A long integer value.

DateValue -> (timestamp)

A date expressed as an ISO 8601 string.

It is important for the time zone to be included in the ISO 8601 date-time format. For example, 2012-03-25T12:30:10+01:00 is the ISO 8601 date-time format for March 25th 2012 at 12:30PM (plus 10 seconds) in Central European Time.

LambdaArn -> (string)

The Amazon Resource Name (ARN) of an IAM role with permission to run a Lambda function during ingestion. For more information, see [an IAM roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

S3Bucket -> (string)

Stores the original, raw documents or the structured, parsed documents before and after altering them. For more information, see [Data contracts for Lambda functions](https://docs.aws.amazon.com/kendra/latest/dg/custom-document-enrichment.html#cde-data-contracts-lambda) .

RoleArn -> (string)

The Amazon Resource Name (ARN) of an IAM role with permission to run `PreExtractionHookConfiguration` and `PostExtractionHookConfiguration` for altering document metadata and content during the document ingestion process. For more information, see [an IAM roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

JSON Syntax:

```
{
  "InlineConfigurations": [
    {
      "Condition": {
        "ConditionDocumentAttributeKey": "string",
        "Operator": "GreaterThan"|"GreaterThanOrEquals"|"LessThan"|"LessThanOrEquals"|"Equals"|"NotEquals"|"Contains"|"NotContains"|"Exists"|"NotExists"|"BeginsWith",
        "ConditionOnValue": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      },
      "Target": {
        "TargetDocumentAttributeKey": "string",
        "TargetDocumentAttributeValueDeletion": true|false,
        "TargetDocumentAttributeValue": {
          "StringValue": "string",
          "StringListValue": ["string", ...],
          "LongValue": long,
          "DateValue": timestamp
        }
      },
      "DocumentContentDeletion": true|false
    }
    ...
  ],
  "PreExtractionHookConfiguration": {
    "InvocationCondition": {
      "ConditionDocumentAttributeKey": "string",
      "Operator": "GreaterThan"|"GreaterThanOrEquals"|"LessThan"|"LessThanOrEquals"|"Equals"|"NotEquals"|"Contains"|"NotContains"|"Exists"|"NotExists"|"BeginsWith",
      "ConditionOnValue": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    },
    "LambdaArn": "string",
    "S3Bucket": "string"
  },
  "PostExtractionHookConfiguration": {
    "InvocationCondition": {
      "ConditionDocumentAttributeKey": "string",
      "Operator": "GreaterThan"|"GreaterThanOrEquals"|"LessThan"|"LessThanOrEquals"|"Equals"|"NotEquals"|"Contains"|"NotContains"|"Exists"|"NotExists"|"BeginsWith",
      "ConditionOnValue": {
        "StringValue": "string",
        "StringListValue": ["string", ...],
        "LongValue": long,
        "DateValue": timestamp
      }
    },
    "LambdaArn": "string",
    "S3Bucket": "string"
  },
  "RoleArn": "string"
}
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update an Amazon Kendra data source connector**

The following `update-data-source` updates the configuration of an Amazon Kendra data source connector. If the action is successful, the service either sends back no output, the HTTP status code 200, or the AWS CLI return code 0. You can use `describe-data-source` to view the configuration and status of a data source connector.

```
aws kendra update-data-source \
    --id exampledatasource1 \
    --index-id exampleindex1 \
    --name "new name for example data source 1" \
    --description "new description for example data source 1" \
    --role-arn arn:aws:iam::my-account-id:role/KendraNewRoleForExampleDataSource \
    --configuration '{"TemplateConfiguration": {"Template": file://s3schemanewconfig.json}}' \
    --custom-document-enrichment-configuration '{"PostExtractionHookConfiguration": {"LambdaArn": "arn:aws:iam::my-account-id:function/my-function-ocr-docs", "S3Bucket": "s3://amzn-s3-demo-bucket/scanned-image-text-example-docs"}, "RoleArn": "arn:aws:iam:my-account-id:role/KendraNewRoleForCDE"}' \
    --language-code "es" \
    --schedule "0 0 18 ? * MON,WED,FRI *" \
    --vpc-configuration '{"SecurityGroupIds": ["sg-1234567890abcdef0"], "SubnetIds": ["subnet-1c234","subnet-2b134"]}'
```

This command produces no output.

For more information, see [Getting started with an Amazon Kendra index and data source connector](https://docs.aws.amazon.com/kendra/latest/dg/getting-started.html) in the *Amazon Kendra Developer Guide*.

## Output

None