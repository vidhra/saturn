# list-revision-assetsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-revision-assets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/list-revision-assets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dataexchange](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/index.html#cli-aws-dataexchange) ]

# list-revision-assets

## Description

This operation lists a revisionâs assets sorted alphabetically in descending order.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dataexchange-2017-07-25/ListRevisionAssets)

`list-revision-assets` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Assets`

## Synopsis

```
list-revision-assets
--data-set-id <value>
--revision-id <value>
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

`--data-set-id` (string)

The unique identifier for a data set.

`--revision-id` (string)

The unique identifier for a revision.

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

Assets -> (list)

The asset objects listed by the request.

(structure)

An asset in AWS Data Exchange is a piece of data (Amazon S3 object) or a means of fulfilling data (Amazon Redshift datashare or Amazon API Gateway API, AWS Lake Formation data permission, or Amazon S3 data access). The asset can be a structured data file, an image file, or some other data file that can be stored as an Amazon S3 object, an Amazon API Gateway API, or an Amazon Redshift datashare, an AWS Lake Formation data permission, or an Amazon S3 data access. When you create an import job for your files, API Gateway APIs, Amazon Redshift datashares, AWS Lake Formation data permission, or Amazon S3 data access, you create an asset in AWS Data Exchange.

Arn -> (string)

The ARN for the asset.

AssetDetails -> (structure)

Details about the asset.

S3SnapshotAsset -> (structure)

The Amazon S3 object that is the asset.

Size -> (double)

The size of the Amazon S3 object that is the object.

RedshiftDataShareAsset -> (structure)

The Amazon Redshift datashare that is the asset.

Arn -> (string)

The Amazon Resource Name (ARN) of the datashare asset.

ApiGatewayApiAsset -> (structure)

Information about the API Gateway API asset.

ApiDescription -> (string)

The API description of the API asset.

ApiEndpoint -> (string)

The API endpoint of the API asset.

ApiId -> (string)

The unique identifier of the API asset.

ApiKey -> (string)

The API key of the API asset.

ApiName -> (string)

The API name of the API asset.

ApiSpecificationDownloadUrl -> (string)

The download URL of the API specification of the API asset.

ApiSpecificationDownloadUrlExpiresAt -> (timestamp)

The date and time that the upload URL expires, in ISO 8601 format.

ProtocolType -> (string)

The protocol type of the API asset.

Stage -> (string)

The stage of the API asset.

S3DataAccessAsset -> (structure)

The Amazon S3 data access that is the asset.

Bucket -> (string)

The Amazon S3 bucket hosting data to be shared in the S3 data access.

KeyPrefixes -> (list)

The Amazon S3 bucket used for hosting shared data in the Amazon S3 data access.

(string)

Keys -> (list)

S3 keys made available using this asset.

(string)

S3AccessPointAlias -> (string)

The automatically-generated bucket-style alias for your Amazon S3 Access Point. Customers can access their entitled data using the S3 Access Point alias.

S3AccessPointArn -> (string)

The ARN for your Amazon S3 Access Point. Customers can also access their entitled data using the S3 Access Point ARN.

KmsKeysToGrant -> (list)

List of AWS KMS CMKs (Key Management System Customer Managed Keys) and ARNs used to encrypt S3 objects being shared in this S3 Data Access asset. Providers must include all AWS KMS keys used to encrypt these shared S3 objects.

(structure)

The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the shared S3 objects.

KmsKeyArn -> (string)

The AWS KMS CMK (Key Management System Customer Managed Key) used to encrypt S3 objects in the shared S3 Bucket. AWS Data exchange will create a KMS grant for each subscriber to allow them to access and decrypt their entitled data that is encrypted using this KMS key specified.

LakeFormationDataPermissionAsset -> (structure)

The AWS Lake Formation data permission that is the asset.

LakeFormationDataPermissionDetails -> (structure)

Details about the AWS Lake Formation data permission.

LFTagPolicy -> (structure)

Details about the LF-tag policy.

CatalogId -> (string)

The identifier for the AWS Glue Data Catalog.

ResourceType -> (string)

The resource type for which the LF-tag policy applies.

ResourceDetails -> (structure)

Details for the Lake Formation Resources included in the LF-tag policy.

Database -> (structure)

Details about the database resource included in the AWS Lake Formation data permission.

Expression -> (list)

A list of LF-tag conditions that apply to database resources.

(structure)

A structure that allows an LF-admin to grant permissions on certain conditions.

TagKey -> (string)

The key name for the LF-tag.

TagValues -> (list)

A list of LF-tag values.

(string)

Table -> (structure)

Details about the table resource included in the AWS Lake Formation data permission.

Expression -> (list)

A list of LF-tag conditions that apply to table resources.

(structure)

A structure that allows an LF-admin to grant permissions on certain conditions.

TagKey -> (string)

The key name for the LF-tag.

TagValues -> (list)

A list of LF-tag values.

(string)

LakeFormationDataPermissionType -> (string)

The data permission type.

Permissions -> (list)

The permissions granted to the subscribers on the resource.

(string)

RoleArn -> (string)

The IAM roleâs ARN that allows AWS Data Exchange to assume the role and grant and revoke permissions to AWS Lake Formation data permissions.

AssetType -> (string)

The type of asset that is added to a data set.

CreatedAt -> (timestamp)

The date and time that the asset was created, in ISO 8601 format.

DataSetId -> (string)

The unique identifier for the data set associated with this asset.

Id -> (string)

The unique identifier for the asset.

Name -> (string)

The name of the asset. When importing from Amazon S3, the Amazon S3 object key is used as the asset name. When exporting to Amazon S3, the asset name is used as default target Amazon S3 object key. When importing from Amazon API Gateway API, the API name is used as the asset name. When importing from Amazon Redshift, the datashare name is used as the asset name. When importing from AWS Lake Formation, the static values of âDatabase(s) included in LF-tag policyâ or âTable(s) included in LF-tag policyâ are used as the asset name.

RevisionId -> (string)

The unique identifier for the revision associated with this asset.

SourceId -> (string)

The asset ID of the owned asset corresponding to the entitled asset being viewed. This parameter is returned when an asset owner is viewing the entitled copy of its owned asset.

UpdatedAt -> (timestamp)

The date and time that the asset was last updated, in ISO 8601 format.

NextToken -> (string)

The token value retrieved from a previous call to access the next page of results.