# update-knowledge-baseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/update-knowledge-base.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/update-knowledge-base.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [bedrock-agent](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/bedrock-agent/index.html#cli-aws-bedrock-agent) ]

# update-knowledge-base

## Description

Updates the configuration of a knowledge base with the fields that you specify. Because all fields will be overwritten, you must include the same values for fields that you want to keep the same.

You can change the following fields:

- `name`
- `description`
- `roleArn`

You canât change the `knowledgeBaseConfiguration` or `storageConfiguration` fields, so you must specify the same configurations as when you created the knowledge base. You can send a [GetKnowledgeBase](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent_GetKnowledgeBase.html) request and copy the same configurations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agent-2023-06-05/UpdateKnowledgeBase)

## Synopsis

```
update-knowledge-base
[--description <value>]
--knowledge-base-configuration <value>
--knowledge-base-id <value>
--name <value>
--role-arn <value>
[--storage-configuration <value>]
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

`--description` (string)

Specifies a new description for the knowledge base.

`--knowledge-base-configuration` (structure)

Specifies the configuration for the embeddings model used for the knowledge base. You must use the same configuration as when the knowledge base was created.

kendraKnowledgeBaseConfiguration -> (structure)

Settings for an Amazon Kendra knowledge base.

kendraIndexArn -> (string)

The ARN of the Amazon Kendra index.

sqlKnowledgeBaseConfiguration -> (structure)

Specifies configurations for a knowledge base connected to an SQL database.

redshiftConfiguration -> (structure)

Specifies configurations for a knowledge base connected to an Amazon Redshift database.

queryEngineConfiguration -> (structure)

Specifies configurations for an Amazon Redshift query engine.

provisionedConfiguration -> (structure)

Specifies configurations for a provisioned Amazon Redshift query engine.

authConfiguration -> (structure)

Specifies configurations for authentication to Amazon Redshift.

databaseUser -> (string)

The database username for authentication to an Amazon Redshift provisioned data warehouse.

type -> (string)

The type of authentication to use.

usernamePasswordSecretArn -> (string)

The ARN of an Secrets Manager secret for authentication.

clusterIdentifier -> (string)

The ID of the Amazon Redshift cluster.

serverlessConfiguration -> (structure)

Specifies configurations for a serverless Amazon Redshift query engine.

authConfiguration -> (structure)

Specifies configurations for authentication to an Amazon Redshift provisioned data warehouse.

type -> (string)

The type of authentication to use.

usernamePasswordSecretArn -> (string)

The ARN of an Secrets Manager secret for authentication.

workgroupArn -> (string)

The ARN of the Amazon Redshift workgroup.

type -> (string)

The type of query engine.

queryGenerationConfiguration -> (structure)

Specifies configurations for generating queries.

executionTimeoutSeconds -> (integer)

The time after which query generation will time out.

generationContext -> (structure)

Specifies configurations for context to use during query generation.

curatedQueries -> (list)

An array of objects, each of which defines information about example queries to help the query engine generate appropriate SQL queries.

(structure)

Contains configurations for a query, each of which defines information about example queries to help the query engine generate appropriate SQL queries.

naturalLanguage -> (string)

An example natural language query.

sql -> (string)

The SQL equivalent of the natural language query.

tables -> (list)

An array of objects, each of which defines information about a table in the database.

(structure)

Contains information about a table for the query engine to consider.

columns -> (list)

An array of objects, each of which defines information about a column in the table.

(structure)

Contains information about a column in the current table for the query engine to consider.

description -> (string)

A description of the column that helps the query engine understand the contents of the column.

inclusion -> (string)

Specifies whether to include or exclude the column during query generation. If you specify `EXCLUDE` , the column will be ignored. If you specify `INCLUDE` , all other columns in the table will be ignored.

name -> (string)

The name of the column for which the other fields in this object apply.

description -> (string)

A description of the table that helps the query engine understand the contents of the table.

inclusion -> (string)

Specifies whether to include or exclude the table during query generation. If you specify `EXCLUDE` , the table will be ignored. If you specify `INCLUDE` , all other tables will be ignored.

name -> (string)

The name of the table for which the other fields in this object apply.

storageConfigurations -> (list)

Specifies configurations for Amazon Redshift database storage.

(structure)

Contains configurations for Amazon Redshift data storage. Specify the data storage service to use in the `type` field and include the corresponding field. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide.

awsDataCatalogConfiguration -> (structure)

Specifies configurations for storage in Glue Data Catalog.

tableNames -> (list)

A list of names of the tables to use.

(string)

redshiftConfiguration -> (structure)

Specifies configurations for storage in Amazon Redshift.

databaseName -> (string)

The name of the Amazon Redshift database.

type -> (string)

The data storage service to use.

type -> (string)

The type of SQL database to connect to the knowledge base.

type -> (string)

The type of data that the data source is converted into for the knowledge base.

vectorKnowledgeBaseConfiguration -> (structure)

Contains details about the model thatâs used to convert the data source into vector embeddings.

embeddingModelArn -> (string)

The Amazon Resource Name (ARN) of the model used to create vector embeddings for the knowledge base.

embeddingModelConfiguration -> (structure)

The embeddings model configuration details for the vector model used in Knowledge Base.

bedrockEmbeddingModelConfiguration -> (structure)

The vector configuration details on the Bedrock embeddings model.

dimensions -> (integer)

The dimensions details for the vector configuration used on the Bedrock embeddings model.

embeddingDataType -> (string)

The data type for the vectors when using a model to convert text into vector embeddings. The model must support the specified data type for vector embeddings. Floating-point (float32) is the default data type, and is supported by most models for vector embeddings. See [Supported embeddings models](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html) for information on the available models and their vector data types.

supplementalDataStorageConfiguration -> (structure)

If you include multimodal data from your data source, use this object to specify configurations for the storage location of the images extracted from your documents. These images can be retrieved and returned to the end user. They can also be used in generation when using [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html) .

storageLocations -> (list)

A list of objects specifying storage locations for images extracted from multimodal documents in your data source.

(structure)

Contains information about a storage location for images extracted from multimodal documents in your data source.

s3Location -> (structure)

Contains information about the Amazon S3 location for the extracted images.

uri -> (string)

The locationâs URI. For example, `s3://my-bucket/chunk-processor/` .

type -> (string)

Specifies the storage service used for this location.

JSON Syntax:

```
{
  "kendraKnowledgeBaseConfiguration": {
    "kendraIndexArn": "string"
  },
  "sqlKnowledgeBaseConfiguration": {
    "redshiftConfiguration": {
      "queryEngineConfiguration": {
        "provisionedConfiguration": {
          "authConfiguration": {
            "databaseUser": "string",
            "type": "IAM"|"USERNAME_PASSWORD"|"USERNAME",
            "usernamePasswordSecretArn": "string"
          },
          "clusterIdentifier": "string"
        },
        "serverlessConfiguration": {
          "authConfiguration": {
            "type": "IAM"|"USERNAME_PASSWORD",
            "usernamePasswordSecretArn": "string"
          },
          "workgroupArn": "string"
        },
        "type": "SERVERLESS"|"PROVISIONED"
      },
      "queryGenerationConfiguration": {
        "executionTimeoutSeconds": integer,
        "generationContext": {
          "curatedQueries": [
            {
              "naturalLanguage": "string",
              "sql": "string"
            }
            ...
          ],
          "tables": [
            {
              "columns": [
                {
                  "description": "string",
                  "inclusion": "INCLUDE"|"EXCLUDE",
                  "name": "string"
                }
                ...
              ],
              "description": "string",
              "inclusion": "INCLUDE"|"EXCLUDE",
              "name": "string"
            }
            ...
          ]
        }
      },
      "storageConfigurations": [
        {
          "awsDataCatalogConfiguration": {
            "tableNames": ["string", ...]
          },
          "redshiftConfiguration": {
            "databaseName": "string"
          },
          "type": "REDSHIFT"|"AWS_DATA_CATALOG"
        }
        ...
      ]
    },
    "type": "REDSHIFT"
  },
  "type": "VECTOR"|"KENDRA"|"SQL",
  "vectorKnowledgeBaseConfiguration": {
    "embeddingModelArn": "string",
    "embeddingModelConfiguration": {
      "bedrockEmbeddingModelConfiguration": {
        "dimensions": integer,
        "embeddingDataType": "FLOAT32"|"BINARY"
      }
    },
    "supplementalDataStorageConfiguration": {
      "storageLocations": [
        {
          "s3Location": {
            "uri": "string"
          },
          "type": "S3"
        }
        ...
      ]
    }
  }
}
```

`--knowledge-base-id` (string)

The unique identifier of the knowledge base to update.

`--name` (string)

Specifies a new name for the knowledge base.

`--role-arn` (string)

Specifies a different Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.

`--storage-configuration` (structure)

Specifies the configuration for the vector store used for the knowledge base. You must use the same configuration as when the knowledge base was created.

mongoDbAtlasConfiguration -> (structure)

Contains the storage configuration of the knowledge base in MongoDB Atlas.

collectionName -> (string)

The collection name of the knowledge base in MongoDB Atlas.

credentialsSecretArn -> (string)

The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that contains user credentials for your MongoDB Atlas cluster.

databaseName -> (string)

The database name in your MongoDB Atlas cluster for your knowledge base.

endpoint -> (string)

The endpoint URL of your MongoDB Atlas cluster for your knowledge base.

endpointServiceName -> (string)

The name of the VPC endpoint service in your account that is connected to your MongoDB Atlas cluster.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

vectorField -> (string)

The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.

textIndexName -> (string)

The name of the text search index in the MongoDB collection. This is required for using the hybrid search feature.

vectorIndexName -> (string)

The name of the MongoDB Atlas vector search index.

neptuneAnalyticsConfiguration -> (structure)

Contains details about the Neptune Analytics configuration of the knowledge base in Amazon Neptune. For more information, see [Create a vector index in Amazon Neptune Analytics.](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-neptune.html) .

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

graphArn -> (string)

The Amazon Resource Name (ARN) of the Neptune Analytics vector store.

opensearchManagedClusterConfiguration -> (structure)

Contains details about the storage configuration of the knowledge base in OpenSearch Managed Cluster. For more information, see [Create a vector index in Amazon OpenSearch Service](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-osm.html) .

domainArn -> (string)

The Amazon Resource Name (ARN) of the OpenSearch domain.

domainEndpoint -> (string)

The endpoint URL the OpenSearch domain.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

vectorField -> (string)

The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.

vectorIndexName -> (string)

The name of the vector store.

opensearchServerlessConfiguration -> (structure)

Contains the storage configuration of the knowledge base in Amazon OpenSearch Service.

collectionArn -> (string)

The Amazon Resource Name (ARN) of the OpenSearch Service vector store.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

vectorField -> (string)

The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.

vectorIndexName -> (string)

The name of the vector store.

pineconeConfiguration -> (structure)

Contains the storage configuration of the knowledge base in Pinecone.

connectionString -> (string)

The endpoint URL for your index management page.

credentialsSecretArn -> (string)

The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that is linked to your Pinecone API key.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

namespace -> (string)

The namespace to be used to write new data to your database.

rdsConfiguration -> (structure)

Contains details about the storage configuration of the knowledge base in Amazon RDS. For more information, see [Create a vector index in Amazon RDS](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html) .

credentialsSecretArn -> (string)

The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that is linked to your Amazon RDS database.

databaseName -> (string)

The name of your Amazon RDS database.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

customMetadataField -> (string)

Provide a name for the universal metadata field where Amazon Bedrock will store any custom metadata from your data source.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

primaryKeyField -> (string)

The name of the field in which Amazon Bedrock stores the ID for each entry.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

vectorField -> (string)

The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.

resourceArn -> (string)

The Amazon Resource Name (ARN) of the vector store.

tableName -> (string)

The name of the table in the database.

redisEnterpriseCloudConfiguration -> (structure)

Contains the storage configuration of the knowledge base in Redis Enterprise Cloud.

credentialsSecretArn -> (string)

The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that is linked to your Redis Enterprise Cloud database.

endpoint -> (string)

The endpoint URL of the Redis Enterprise Cloud database.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

vectorField -> (string)

The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.

vectorIndexName -> (string)

The name of the vector index.

type -> (string)

The vector store service in which the knowledge base is stored.

Shorthand Syntax:

```
mongoDbAtlasConfiguration={collectionName=string,credentialsSecretArn=string,databaseName=string,endpoint=string,endpointServiceName=string,fieldMapping={metadataField=string,textField=string,vectorField=string},textIndexName=string,vectorIndexName=string},neptuneAnalyticsConfiguration={fieldMapping={metadataField=string,textField=string},graphArn=string},opensearchManagedClusterConfiguration={domainArn=string,domainEndpoint=string,fieldMapping={metadataField=string,textField=string,vectorField=string},vectorIndexName=string},opensearchServerlessConfiguration={collectionArn=string,fieldMapping={metadataField=string,textField=string,vectorField=string},vectorIndexName=string},pineconeConfiguration={connectionString=string,credentialsSecretArn=string,fieldMapping={metadataField=string,textField=string},namespace=string},rdsConfiguration={credentialsSecretArn=string,databaseName=string,fieldMapping={customMetadataField=string,metadataField=string,primaryKeyField=string,textField=string,vectorField=string},resourceArn=string,tableName=string},redisEnterpriseCloudConfiguration={credentialsSecretArn=string,endpoint=string,fieldMapping={metadataField=string,textField=string,vectorField=string},vectorIndexName=string},type=string
```

JSON Syntax:

```
{
  "mongoDbAtlasConfiguration": {
    "collectionName": "string",
    "credentialsSecretArn": "string",
    "databaseName": "string",
    "endpoint": "string",
    "endpointServiceName": "string",
    "fieldMapping": {
      "metadataField": "string",
      "textField": "string",
      "vectorField": "string"
    },
    "textIndexName": "string",
    "vectorIndexName": "string"
  },
  "neptuneAnalyticsConfiguration": {
    "fieldMapping": {
      "metadataField": "string",
      "textField": "string"
    },
    "graphArn": "string"
  },
  "opensearchManagedClusterConfiguration": {
    "domainArn": "string",
    "domainEndpoint": "string",
    "fieldMapping": {
      "metadataField": "string",
      "textField": "string",
      "vectorField": "string"
    },
    "vectorIndexName": "string"
  },
  "opensearchServerlessConfiguration": {
    "collectionArn": "string",
    "fieldMapping": {
      "metadataField": "string",
      "textField": "string",
      "vectorField": "string"
    },
    "vectorIndexName": "string"
  },
  "pineconeConfiguration": {
    "connectionString": "string",
    "credentialsSecretArn": "string",
    "fieldMapping": {
      "metadataField": "string",
      "textField": "string"
    },
    "namespace": "string"
  },
  "rdsConfiguration": {
    "credentialsSecretArn": "string",
    "databaseName": "string",
    "fieldMapping": {
      "customMetadataField": "string",
      "metadataField": "string",
      "primaryKeyField": "string",
      "textField": "string",
      "vectorField": "string"
    },
    "resourceArn": "string",
    "tableName": "string"
  },
  "redisEnterpriseCloudConfiguration": {
    "credentialsSecretArn": "string",
    "endpoint": "string",
    "fieldMapping": {
      "metadataField": "string",
      "textField": "string",
      "vectorField": "string"
    },
    "vectorIndexName": "string"
  },
  "type": "OPENSEARCH_SERVERLESS"|"PINECONE"|"REDIS_ENTERPRISE_CLOUD"|"RDS"|"MONGO_DB_ATLAS"|"NEPTUNE_ANALYTICS"|"OPENSEARCH_MANAGED_CLUSTER"
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

## Output

knowledgeBase -> (structure)

Contains details about the knowledge base.

createdAt -> (timestamp)

The time the knowledge base was created.

description -> (string)

The description of the knowledge base.

failureReasons -> (list)

A list of reasons that the API operation on the knowledge base failed.

(string)

knowledgeBaseArn -> (string)

The Amazon Resource Name (ARN) of the knowledge base.

knowledgeBaseConfiguration -> (structure)

Contains details about the embeddings configuration of the knowledge base.

kendraKnowledgeBaseConfiguration -> (structure)

Settings for an Amazon Kendra knowledge base.

kendraIndexArn -> (string)

The ARN of the Amazon Kendra index.

sqlKnowledgeBaseConfiguration -> (structure)

Specifies configurations for a knowledge base connected to an SQL database.

redshiftConfiguration -> (structure)

Specifies configurations for a knowledge base connected to an Amazon Redshift database.

queryEngineConfiguration -> (structure)

Specifies configurations for an Amazon Redshift query engine.

provisionedConfiguration -> (structure)

Specifies configurations for a provisioned Amazon Redshift query engine.

authConfiguration -> (structure)

Specifies configurations for authentication to Amazon Redshift.

databaseUser -> (string)

The database username for authentication to an Amazon Redshift provisioned data warehouse.

type -> (string)

The type of authentication to use.

usernamePasswordSecretArn -> (string)

The ARN of an Secrets Manager secret for authentication.

clusterIdentifier -> (string)

The ID of the Amazon Redshift cluster.

serverlessConfiguration -> (structure)

Specifies configurations for a serverless Amazon Redshift query engine.

authConfiguration -> (structure)

Specifies configurations for authentication to an Amazon Redshift provisioned data warehouse.

type -> (string)

The type of authentication to use.

usernamePasswordSecretArn -> (string)

The ARN of an Secrets Manager secret for authentication.

workgroupArn -> (string)

The ARN of the Amazon Redshift workgroup.

type -> (string)

The type of query engine.

queryGenerationConfiguration -> (structure)

Specifies configurations for generating queries.

executionTimeoutSeconds -> (integer)

The time after which query generation will time out.

generationContext -> (structure)

Specifies configurations for context to use during query generation.

curatedQueries -> (list)

An array of objects, each of which defines information about example queries to help the query engine generate appropriate SQL queries.

(structure)

Contains configurations for a query, each of which defines information about example queries to help the query engine generate appropriate SQL queries.

naturalLanguage -> (string)

An example natural language query.

sql -> (string)

The SQL equivalent of the natural language query.

tables -> (list)

An array of objects, each of which defines information about a table in the database.

(structure)

Contains information about a table for the query engine to consider.

columns -> (list)

An array of objects, each of which defines information about a column in the table.

(structure)

Contains information about a column in the current table for the query engine to consider.

description -> (string)

A description of the column that helps the query engine understand the contents of the column.

inclusion -> (string)

Specifies whether to include or exclude the column during query generation. If you specify `EXCLUDE` , the column will be ignored. If you specify `INCLUDE` , all other columns in the table will be ignored.

name -> (string)

The name of the column for which the other fields in this object apply.

description -> (string)

A description of the table that helps the query engine understand the contents of the table.

inclusion -> (string)

Specifies whether to include or exclude the table during query generation. If you specify `EXCLUDE` , the table will be ignored. If you specify `INCLUDE` , all other tables will be ignored.

name -> (string)

The name of the table for which the other fields in this object apply.

storageConfigurations -> (list)

Specifies configurations for Amazon Redshift database storage.

(structure)

Contains configurations for Amazon Redshift data storage. Specify the data storage service to use in the `type` field and include the corresponding field. For more information, see [Build a knowledge base by connecting to a structured data source](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-build-structured.html) in the Amazon Bedrock User Guide.

awsDataCatalogConfiguration -> (structure)

Specifies configurations for storage in Glue Data Catalog.

tableNames -> (list)

A list of names of the tables to use.

(string)

redshiftConfiguration -> (structure)

Specifies configurations for storage in Amazon Redshift.

databaseName -> (string)

The name of the Amazon Redshift database.

type -> (string)

The data storage service to use.

type -> (string)

The type of SQL database to connect to the knowledge base.

type -> (string)

The type of data that the data source is converted into for the knowledge base.

vectorKnowledgeBaseConfiguration -> (structure)

Contains details about the model thatâs used to convert the data source into vector embeddings.

embeddingModelArn -> (string)

The Amazon Resource Name (ARN) of the model used to create vector embeddings for the knowledge base.

embeddingModelConfiguration -> (structure)

The embeddings model configuration details for the vector model used in Knowledge Base.

bedrockEmbeddingModelConfiguration -> (structure)

The vector configuration details on the Bedrock embeddings model.

dimensions -> (integer)

The dimensions details for the vector configuration used on the Bedrock embeddings model.

embeddingDataType -> (string)

The data type for the vectors when using a model to convert text into vector embeddings. The model must support the specified data type for vector embeddings. Floating-point (float32) is the default data type, and is supported by most models for vector embeddings. See [Supported embeddings models](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-supported.html) for information on the available models and their vector data types.

supplementalDataStorageConfiguration -> (structure)

If you include multimodal data from your data source, use this object to specify configurations for the storage location of the images extracted from your documents. These images can be retrieved and returned to the end user. They can also be used in generation when using [RetrieveAndGenerate](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_agent-runtime_RetrieveAndGenerate.html) .

storageLocations -> (list)

A list of objects specifying storage locations for images extracted from multimodal documents in your data source.

(structure)

Contains information about a storage location for images extracted from multimodal documents in your data source.

s3Location -> (structure)

Contains information about the Amazon S3 location for the extracted images.

uri -> (string)

The locationâs URI. For example, `s3://my-bucket/chunk-processor/` .

type -> (string)

Specifies the storage service used for this location.

knowledgeBaseId -> (string)

The unique identifier of the knowledge base.

name -> (string)

The name of the knowledge base.

roleArn -> (string)

The Amazon Resource Name (ARN) of the IAM role with permissions to invoke API operations on the knowledge base.

status -> (string)

The status of the knowledge base. The following statuses are possible:

- CREATING â The knowledge base is being created.
- ACTIVE â The knowledge base is ready to be queried.
- DELETING â The knowledge base is being deleted.
- UPDATING â The knowledge base is being updated.
- FAILED â The knowledge base API operation failed.

storageConfiguration -> (structure)

Contains details about the storage configuration of the knowledge base.

mongoDbAtlasConfiguration -> (structure)

Contains the storage configuration of the knowledge base in MongoDB Atlas.

collectionName -> (string)

The collection name of the knowledge base in MongoDB Atlas.

credentialsSecretArn -> (string)

The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that contains user credentials for your MongoDB Atlas cluster.

databaseName -> (string)

The database name in your MongoDB Atlas cluster for your knowledge base.

endpoint -> (string)

The endpoint URL of your MongoDB Atlas cluster for your knowledge base.

endpointServiceName -> (string)

The name of the VPC endpoint service in your account that is connected to your MongoDB Atlas cluster.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

vectorField -> (string)

The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.

textIndexName -> (string)

The name of the text search index in the MongoDB collection. This is required for using the hybrid search feature.

vectorIndexName -> (string)

The name of the MongoDB Atlas vector search index.

neptuneAnalyticsConfiguration -> (structure)

Contains details about the Neptune Analytics configuration of the knowledge base in Amazon Neptune. For more information, see [Create a vector index in Amazon Neptune Analytics.](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-neptune.html) .

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

graphArn -> (string)

The Amazon Resource Name (ARN) of the Neptune Analytics vector store.

opensearchManagedClusterConfiguration -> (structure)

Contains details about the storage configuration of the knowledge base in OpenSearch Managed Cluster. For more information, see [Create a vector index in Amazon OpenSearch Service](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-osm.html) .

domainArn -> (string)

The Amazon Resource Name (ARN) of the OpenSearch domain.

domainEndpoint -> (string)

The endpoint URL the OpenSearch domain.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

vectorField -> (string)

The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.

vectorIndexName -> (string)

The name of the vector store.

opensearchServerlessConfiguration -> (structure)

Contains the storage configuration of the knowledge base in Amazon OpenSearch Service.

collectionArn -> (string)

The Amazon Resource Name (ARN) of the OpenSearch Service vector store.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

vectorField -> (string)

The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.

vectorIndexName -> (string)

The name of the vector store.

pineconeConfiguration -> (structure)

Contains the storage configuration of the knowledge base in Pinecone.

connectionString -> (string)

The endpoint URL for your index management page.

credentialsSecretArn -> (string)

The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that is linked to your Pinecone API key.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

namespace -> (string)

The namespace to be used to write new data to your database.

rdsConfiguration -> (structure)

Contains details about the storage configuration of the knowledge base in Amazon RDS. For more information, see [Create a vector index in Amazon RDS](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html) .

credentialsSecretArn -> (string)

The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that is linked to your Amazon RDS database.

databaseName -> (string)

The name of your Amazon RDS database.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

customMetadataField -> (string)

Provide a name for the universal metadata field where Amazon Bedrock will store any custom metadata from your data source.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

primaryKeyField -> (string)

The name of the field in which Amazon Bedrock stores the ID for each entry.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

vectorField -> (string)

The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.

resourceArn -> (string)

The Amazon Resource Name (ARN) of the vector store.

tableName -> (string)

The name of the table in the database.

redisEnterpriseCloudConfiguration -> (structure)

Contains the storage configuration of the knowledge base in Redis Enterprise Cloud.

credentialsSecretArn -> (string)

The Amazon Resource Name (ARN) of the secret that you created in Secrets Manager that is linked to your Redis Enterprise Cloud database.

endpoint -> (string)

The endpoint URL of the Redis Enterprise Cloud database.

fieldMapping -> (structure)

Contains the names of the fields to which to map information about the vector store.

metadataField -> (string)

The name of the field in which Amazon Bedrock stores metadata about the vector store.

textField -> (string)

The name of the field in which Amazon Bedrock stores the raw text from your data. The text is split according to the chunking strategy you choose.

vectorField -> (string)

The name of the field in which Amazon Bedrock stores the vector embeddings for your data sources.

vectorIndexName -> (string)

The name of the vector index.

type -> (string)

The vector store service in which the knowledge base is stored.

updatedAt -> (timestamp)

The time the knowledge base was last updated.