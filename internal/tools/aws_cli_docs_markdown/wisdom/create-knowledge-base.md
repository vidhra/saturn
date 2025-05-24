# create-knowledge-baseÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wisdom/create-knowledge-base.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wisdom/create-knowledge-base.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wisdom](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wisdom/index.html#cli-aws-wisdom) ]

# create-knowledge-base

## Description

Creates a knowledge base.

### Note

When using this API, you cannot reuse [Amazon AppIntegrations](https://docs.aws.amazon.com/appintegrations/latest/APIReference/Welcome.html) DataIntegrations with external knowledge bases such as Salesforce and ServiceNow. If you do, youâll get an `InvalidRequestException` error.

For example, youâre programmatically managing your external knowledge base, and you want to add or remove one of the fields that is being ingested from Salesforce. Do the following:

- Call [DeleteKnowledgeBase](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_DeleteKnowledgeBase.html) .
- Call [DeleteDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_DeleteDataIntegration.html) .
- Call [CreateDataIntegration](https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_CreateDataIntegration.html) to recreate the DataIntegration or a create different one.
- Call CreateKnowledgeBase.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wisdom-2020-10-19/CreateKnowledgeBase)

## Synopsis

```
create-knowledge-base
[--client-token <value>]
[--description <value>]
--knowledge-base-type <value>
--name <value>
[--rendering-configuration <value>]
[--server-side-encryption-configuration <value>]
[--source-configuration <value>]
[--tags <value>]
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

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) .

`--description` (string)

The description.

`--knowledge-base-type` (string)

The type of knowledge base. Only CUSTOM knowledge bases allow you to upload your own content. EXTERNAL knowledge bases support integrations with third-party systems whose content is synchronized automatically.

Possible values:

- `EXTERNAL`
- `CUSTOM`
- `QUICK_RESPONSES`

`--name` (string)

The name of the knowledge base.

`--rendering-configuration` (structure)

Information about how to render the content.

templateUri -> (string)

A URI template containing exactly one variable in `${variableName}` format. This can only be set for `EXTERNAL` knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following:

- Salesforce: `Id` , `ArticleNumber` , `VersionNumber` , `Title` , `PublishStatus` , or `IsDeleted`
- ServiceNow: `number` , `short_description` , `sys_mod_count` , `workflow_state` , or `active`
- Zendesk: `id` , `title` , `updated_at` , or `draft`

The variable is replaced with the actual value for a piece of content when calling [GetContent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetContent.html) .

Shorthand Syntax:

```
templateUri=string
```

JSON Syntax:

```
{
  "templateUri": "string"
}
```

`--server-side-encryption-configuration` (structure)

The configuration information for the customer managed key used for encryption.

This KMS key must have a policy that allows `kms:CreateGrant` , `kms:DescribeKey` , and `kms:Decrypt/kms:GenerateDataKey` permissions to the IAM identity using the key to invoke Wisdom.

For more information about setting up a customer managed key for Wisdom, see [Enable Amazon Connect Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html) .

kmsKeyId -> (string)

The customer managed key used for encryption. For more information about setting up a customer managed key for Wisdom, see [Enable Amazon Connect Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html) . For information about valid ID values, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) .

Shorthand Syntax:

```
kmsKeyId=string
```

JSON Syntax:

```
{
  "kmsKeyId": "string"
}
```

`--source-configuration` (tagged union structure)

The source of the knowledge base content. Only set this argument for EXTERNAL knowledge bases.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `appIntegrations`.

appIntegrations -> (structure)

Configuration information for Amazon AppIntegrations to automatically ingest content.

appIntegrationArn -> (string)

The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content.

- For [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm) , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least `Id` , `ArticleNumber` , `VersionNumber` , `Title` , `PublishStatus` , and `IsDeleted` as source fields.
- For [ServiceNow](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api) , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least `number` , `short_description` , `sys_mod_count` , `workflow_state` , and `active` as source fields.
- For [Zendesk](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/) , your AppIntegrations DataIntegration must have an ObjectConfiguration if `objectFields` is not provided, including at least `id` , `title` , `updated_at` , and `draft` as source fields.
- For [SharePoint](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index) , your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among `docx` , `pdf` , `html` , `htm` , and `txt` .
- For [Amazon S3](https://aws.amazon.com/s3/) , the ObjectConfiguration and FileConfiguration of your AppIntegrations DataIntegration must be null. The `SourceURI` of your DataIntegration must use the following format: `s3://your_s3_bucket_name` .

### Warning

The bucket policy of the corresponding S3 bucket must allow the Amazon Web Services principal `app-integrations.amazonaws.com` to perform `s3:ListBucket` , `s3:GetObject` , and `s3:GetBucketLocation` against the bucket.

objectFields -> (list)

The fields from the source that are made available to your agents in Wisdom. Optional if ObjectConfiguration is included in the provided DataIntegration.

- For [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm) , you must include at least `Id` , `ArticleNumber` , `VersionNumber` , `Title` , `PublishStatus` , and `IsDeleted` .
- For [ServiceNow](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api) , you must include at least `number` , `short_description` , `sys_mod_count` , `workflow_state` , and `active` .
- For [Zendesk](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/) , you must include at least `id` , `title` , `updated_at` , and `draft` .

Make sure to include additional fields. These fields are indexed and used to source recommendations.

(string)

Shorthand Syntax:

```
appIntegrations={appIntegrationArn=string,objectFields=[string,string]}
```

JSON Syntax:

```
{
  "appIntegrations": {
    "appIntegrationArn": "string",
    "objectFields": ["string", ...]
  }
}
```

`--tags` (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

The knowledge base.

description -> (string)

The description.

knowledgeBaseArn -> (string)

The Amazon Resource Name (ARN) of the knowledge base.

knowledgeBaseId -> (string)

The identifier of the knowledge base. This should not be a QUICK_RESPONSES type knowledge base if youâre storing Wisdom Content resource to it.

knowledgeBaseType -> (string)

The type of knowledge base.

lastContentModificationTime -> (timestamp)

An epoch timestamp indicating the most recent content modification inside the knowledge base. If no content exists in a knowledge base, this value is unset.

name -> (string)

The name of the knowledge base.

renderingConfiguration -> (structure)

Information about how to render the content.

templateUri -> (string)

A URI template containing exactly one variable in `${variableName}` format. This can only be set for `EXTERNAL` knowledge bases. For Salesforce, ServiceNow, and Zendesk, the variable must be one of the following:

- Salesforce: `Id` , `ArticleNumber` , `VersionNumber` , `Title` , `PublishStatus` , or `IsDeleted`
- ServiceNow: `number` , `short_description` , `sys_mod_count` , `workflow_state` , or `active`
- Zendesk: `id` , `title` , `updated_at` , or `draft`

The variable is replaced with the actual value for a piece of content when calling [GetContent](https://docs.aws.amazon.com/wisdom/latest/APIReference/API_GetContent.html) .

serverSideEncryptionConfiguration -> (structure)

The configuration information for the customer managed key used for encryption.

This KMS key must have a policy that allows `kms:CreateGrant` , `kms:DescribeKey` , and `kms:Decrypt/kms:GenerateDataKey` permissions to the IAM identity using the key to invoke Wisdom.

For more information about setting up a customer managed key for Wisdom, see [Enable Amazon Connect Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html) .

kmsKeyId -> (string)

The customer managed key used for encryption. For more information about setting up a customer managed key for Wisdom, see [Enable Amazon Connect Wisdom for your instance](https://docs.aws.amazon.com/connect/latest/adminguide/enable-wisdom.html) . For information about valid ID values, see [Key identifiers (KeyId)](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) .

sourceConfiguration -> (tagged union structure)

Source configuration information about the knowledge base.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `appIntegrations`.

appIntegrations -> (structure)

Configuration information for Amazon AppIntegrations to automatically ingest content.

appIntegrationArn -> (string)

The Amazon Resource Name (ARN) of the AppIntegrations DataIntegration to use for ingesting content.

- For [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm) , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least `Id` , `ArticleNumber` , `VersionNumber` , `Title` , `PublishStatus` , and `IsDeleted` as source fields.
- For [ServiceNow](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api) , your AppIntegrations DataIntegration must have an ObjectConfiguration if objectFields is not provided, including at least `number` , `short_description` , `sys_mod_count` , `workflow_state` , and `active` as source fields.
- For [Zendesk](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/) , your AppIntegrations DataIntegration must have an ObjectConfiguration if `objectFields` is not provided, including at least `id` , `title` , `updated_at` , and `draft` as source fields.
- For [SharePoint](https://learn.microsoft.com/en-us/sharepoint/dev/sp-add-ins/sharepoint-net-server-csom-jsom-and-rest-api-index) , your AppIntegrations DataIntegration must have a FileConfiguration, including only file extensions that are among `docx` , `pdf` , `html` , `htm` , and `txt` .
- For [Amazon S3](https://aws.amazon.com/s3/) , the ObjectConfiguration and FileConfiguration of your AppIntegrations DataIntegration must be null. The `SourceURI` of your DataIntegration must use the following format: `s3://your_s3_bucket_name` .

### Warning

The bucket policy of the corresponding S3 bucket must allow the Amazon Web Services principal `app-integrations.amazonaws.com` to perform `s3:ListBucket` , `s3:GetObject` , and `s3:GetBucketLocation` against the bucket.

objectFields -> (list)

The fields from the source that are made available to your agents in Wisdom. Optional if ObjectConfiguration is included in the provided DataIntegration.

- For [Salesforce](https://developer.salesforce.com/docs/atlas.en-us.knowledge_dev.meta/knowledge_dev/sforce_api_objects_knowledge__kav.htm) , you must include at least `Id` , `ArticleNumber` , `VersionNumber` , `Title` , `PublishStatus` , and `IsDeleted` .
- For [ServiceNow](https://developer.servicenow.com/dev.do#!/reference/api/rome/rest/knowledge-management-api) , you must include at least `number` , `short_description` , `sys_mod_count` , `workflow_state` , and `active` .
- For [Zendesk](https://developer.zendesk.com/api-reference/help_center/help-center-api/articles/) , you must include at least `id` , `title` , `updated_at` , and `draft` .

Make sure to include additional fields. These fields are indexed and used to source recommendations.

(string)

status -> (string)

The status of the knowledge base.

tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)