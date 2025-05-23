# get-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/get-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [dataexchange](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/dataexchange/index.html#cli-aws-dataexchange) ]

# get-job

## Description

This operation returns information about a job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/dataexchange-2017-07-25/GetJob)

## Synopsis

```
get-job
--job-id <value>
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

`--job-id` (string)

The unique identifier for a job.

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

Arn -> (string)

The ARN for the job.

CreatedAt -> (timestamp)

The date and time that the job was created, in ISO 8601 format.

Details -> (structure)

Details about the job.

ExportAssetToSignedUrl -> (structure)

Details for the export to signed URL response.

AssetId -> (string)

The unique identifier for the asset associated with this export job.

DataSetId -> (string)

The unique identifier for the data set associated with this export job.

RevisionId -> (string)

The unique identifier for the revision associated with this export response.

SignedUrl -> (string)

The signed URL for the export request.

SignedUrlExpiresAt -> (timestamp)

The date and time that the signed URL expires, in ISO 8601 format.

ExportAssetsToS3 -> (structure)

Details for the export to Amazon S3 response.

AssetDestinations -> (list)

The destination in Amazon S3 where the asset is exported.

(structure)

The destination for the asset.

AssetId -> (string)

The unique identifier for the asset.

Bucket -> (string)

The Amazon S3 bucket that is the destination for the asset.

Key -> (string)

The name of the object in Amazon S3 for the asset.

DataSetId -> (string)

The unique identifier for the data set associated with this export job.

Encryption -> (structure)

Encryption configuration of the export job.

KmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the AWS KMS key you want to use to encrypt the Amazon S3 objects. This parameter is required if you choose aws:kms as an encryption type.

Type -> (string)

The type of server side encryption used for encrypting the objects in Amazon S3.

RevisionId -> (string)

The unique identifier for the revision associated with this export response.

ExportRevisionsToS3 -> (structure)

Details for the export revisions to Amazon S3 response.

DataSetId -> (string)

The unique identifier for the data set associated with this export job.

Encryption -> (structure)

Encryption configuration of the export job.

KmsKeyArn -> (string)

The Amazon Resource Name (ARN) of the AWS KMS key you want to use to encrypt the Amazon S3 objects. This parameter is required if you choose aws:kms as an encryption type.

Type -> (string)

The type of server side encryption used for encrypting the objects in Amazon S3.

RevisionDestinations -> (list)

The destination in Amazon S3 where the revision is exported.

(structure)

The destination where the assets in the revision will be exported.

Bucket -> (string)

The Amazon S3 bucket that is the destination for the assets in the revision.

KeyPattern -> (string)

A string representing the pattern for generated names of the individual assets in the revision. For more information about key patterns, see [Key patterns when exporting revisions](https://docs.aws.amazon.com/data-exchange/latest/userguide/jobs.html#revision-export-keypatterns) .

RevisionId -> (string)

The unique identifier for the revision.

EventActionArn -> (string)

The Amazon Resource Name (ARN) of the event action.

ImportAssetFromSignedUrl -> (structure)

Details for the import from signed URL response.

AssetName -> (string)

The name for the asset associated with this import job.

DataSetId -> (string)

The unique identifier for the data set associated with this import job.

Md5Hash -> (string)

The Base64-encoded Md5 hash for the asset, used to ensure the integrity of the file at that location.

RevisionId -> (string)

The unique identifier for the revision associated with this import response.

SignedUrl -> (string)

The signed URL.

SignedUrlExpiresAt -> (timestamp)

The time and date at which the signed URL expires, in ISO 8601 format.

ImportAssetsFromS3 -> (structure)

Details for the import from Amazon S3 response.

AssetSources -> (list)

Is a list of Amazon S3 bucket and object key pairs.

(structure)

The source of the assets.

Bucket -> (string)

The Amazon S3 bucket thatâs part of the source of the asset.

Key -> (string)

The name of the object in Amazon S3 for the asset.

DataSetId -> (string)

The unique identifier for the data set associated with this import job.

RevisionId -> (string)

The unique identifier for the revision associated with this import response.

ImportAssetsFromRedshiftDataShares -> (structure)

Details from an import from Amazon Redshift datashare response.

AssetSources -> (list)

A list of Amazon Redshift datashare asset sources.

(structure)

The source of the Amazon Redshift datashare asset.

DataShareArn -> (string)

The Amazon Resource Name (ARN) of the datashare asset.

DataSetId -> (string)

The unique identifier for the data set associated with this import job.

RevisionId -> (string)

The unique identifier for the revision associated with this import job.

ImportAssetFromApiGatewayApi -> (structure)

The response details.

ApiDescription -> (string)

The API description.

ApiId -> (string)

The API ID.

ApiKey -> (string)

The API key.

ApiName -> (string)

The API name.

ApiSpecificationMd5Hash -> (string)

The Base64-encoded Md5 hash for the API asset, used to ensure the integrity of the API at that location.

ApiSpecificationUploadUrl -> (string)

The upload URL of the API specification.

ApiSpecificationUploadUrlExpiresAt -> (timestamp)

The date and time that the upload URL expires, in ISO 8601 format.

DataSetId -> (string)

The data set ID.

ProtocolType -> (string)

The protocol type.

RevisionId -> (string)

The revision ID.

Stage -> (string)

The API stage.

CreateS3DataAccessFromS3Bucket -> (structure)

Response details from the CreateS3DataAccessFromS3Bucket job.

AssetSource -> (structure)

Details about the asset source from an Amazon S3 bucket.

Bucket -> (string)

The Amazon S3 bucket used for hosting shared data in the Amazon S3 data access.

KeyPrefixes -> (list)

Organizes Amazon S3 asset key prefixes stored in an Amazon S3 bucket.

(string)

Keys -> (list)

The keys used to create the Amazon S3 data access.

(string)

KmsKeysToGrant -> (list)

List of AWS KMS CMKs (Key Management System Customer Managed Keys) and ARNs used to encrypt S3 objects being shared in this S3 Data Access asset.

(structure)

The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the shared S3 objects.

KmsKeyArn -> (string)

The AWS KMS CMK (Key Management System Customer Managed Key) used to encrypt S3 objects in the shared S3 Bucket. AWS Data exchange will create a KMS grant for each subscriber to allow them to access and decrypt their entitled data that is encrypted using this KMS key specified.

DataSetId -> (string)

The unique identifier for this data set.

RevisionId -> (string)

The unique identifier for the revision.

ImportAssetsFromLakeFormationTagPolicy -> (structure)

Response details from the ImportAssetsFromLakeFormationTagPolicy job.

CatalogId -> (string)

The identifier for the AWS Glue Data Catalog.

Database -> (structure)

A structure for the database object.

Expression -> (list)

A list of LF-tag conditions that apply to database resources.

(structure)

A structure that allows an LF-admin to grant permissions on certain conditions.

TagKey -> (string)

The key name for the LF-tag.

TagValues -> (list)

A list of LF-tag values.

(string)

Permissions -> (list)

The permissions granted to subscribers on database resources.

(string)

Table -> (structure)

A structure for the table object.

Expression -> (list)

A list of LF-tag conditions that apply to table resources.

(structure)

A structure that allows an LF-admin to grant permissions on certain conditions.

TagKey -> (string)

The key name for the LF-tag.

TagValues -> (list)

A list of LF-tag values.

(string)

Permissions -> (list)

The permissions granted to subscribers on table resources.

(string)

RoleArn -> (string)

The IAM roleâs ARN that allows AWS Data Exchange to assume the role and grant and revoke permissions to AWS Lake Formation data permissions.

DataSetId -> (string)

The unique identifier for the data set associated with this import job.

RevisionId -> (string)

The unique identifier for the revision associated with this import job.

Errors -> (list)

The errors associated with jobs.

(structure)

An error that occurred with the job request.

Code -> (string)

The code for the job error.

Details -> (structure)

The details about the job error.

ImportAssetFromSignedUrlJobErrorDetails -> (structure)

Information about the job error.

AssetName -> (string)

Details about the job error.

ImportAssetsFromS3JobErrorDetails -> (list)

Details about the job error.

(structure)

The source of the assets.

Bucket -> (string)

The Amazon S3 bucket thatâs part of the source of the asset.

Key -> (string)

The name of the object in Amazon S3 for the asset.

LimitName -> (string)

The name of the limit that was reached.

LimitValue -> (double)

The value of the exceeded limit.

Message -> (string)

The message related to the job error.

ResourceId -> (string)

The unique identifier for the resource related to the error.

ResourceType -> (string)

The type of resource related to the error.

Id -> (string)

The unique identifier for the job.

State -> (string)

The state of the job.

Type -> (string)

The job type.

UpdatedAt -> (timestamp)

The date and time that the job was last updated, in ISO 8601 format.