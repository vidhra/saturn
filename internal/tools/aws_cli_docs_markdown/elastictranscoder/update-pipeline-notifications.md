# update-pipeline-notificationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/update-pipeline-notifications.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/update-pipeline-notifications.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elastictranscoder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/index.html#cli-aws-elastictranscoder) ]

# update-pipeline-notifications

## Description

With the UpdatePipelineNotifications operation, you can update Amazon Simple Notification Service (Amazon SNS) notifications for a pipeline.

When you update notifications for a pipeline, Elastic Transcoder returns the values that you specified in the request.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elastictranscoder-2012-09-25/UpdatePipelineNotifications)

## Synopsis

```
update-pipeline-notifications
--id <value>
--notifications <value>
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

The identifier of the pipeline for which you want to change notification settings.

`--notifications` (structure)

The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status.

### Warning

To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.

- **Progressing** : The topic ARN for the Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process jobs that are added to this pipeline. This is the ARN that Amazon SNS returned when you created the topic.
- **Complete** : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing a job. This is the ARN that Amazon SNS returned when you created the topic.
- **Warning** : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition. This is the ARN that Amazon SNS returned when you created the topic.
- **Error** : The topic ARN for the Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition. This is the ARN that Amazon SNS returned when you created the topic.

Progressing -> (string)

The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process the job.

Completed -> (string)

The Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing the job.

Warning -> (string)

The Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition.

Error -> (string)

The Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition.

Shorthand Syntax:

```
Progressing=string,Completed=string,Warning=string,Error=string
```

JSON Syntax:

```
{
  "Progressing": "string",
  "Completed": "string",
  "Warning": "string",
  "Error": "string"
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

**To update the notifications of an ElasticTranscoder pipeline**

This example updates the notifications of the specified ElasticTranscoder pipeline.

Command:

```
aws elastictranscoder update-pipeline-notifications --id 1111111111111-abcde1 --notifications Progressing=arn:aws:sns:us-west-2:0123456789012:my-topic,Completed=arn:aws:sns:us-west-2:0123456789012:my-topic,Warning=arn:aws:sns:us-west-2:0123456789012:my-topic,Error=arn:aws:sns:us-east-1:111222333444:ETS_Errors
```

Output:

```
{
   "Pipeline": {
       "Status": "Active",
       "ContentConfig": {
           "Bucket": "ets-example",
           "StorageClass": "Standard",
           "Permissions": [
               {
                   "Access": [
                       "FullControl"
                   ],
                   "Grantee": "marketing-promos@example.com",
                   "GranteeType": "Email"
               }
           ]
       },
       "Name": "Default",
       "ThumbnailConfig": {
           "Bucket": "ets-example",
           "StorageClass": "ReducedRedundancy",
           "Permissions": [
               {
                   "Access": [
                       "FullControl"
                   ],
                   "Grantee": "marketing-promos@example.com",
                   "GranteeType": "Email"
               }
           ]
       },
       "Notifications": {
           "Completed": "arn:aws:sns:us-west-2:0123456789012:my-topic",
           "Warning": "arn:aws:sns:us-west-2:0123456789012:my-topic",
           "Progressing": "arn:aws:sns:us-west-2:0123456789012:my-topic",
           "Error": "arn:aws:sns:us-east-1:111222333444:ETS_Errors"
       },
       "Role": "arn:aws:iam::123456789012:role/Elastic_Transcoder_Default_Role",
       "InputBucket": "ets-example",
       "Id": "1111111111111-abcde1",
       "Arn": "arn:aws:elastictranscoder:us-west-2:123456789012:pipeline/1111111111111-abcde1"
   }
}
```

## Output

Pipeline -> (structure)

A section of the response body that provides information about the pipeline associated with this notification.

Id -> (string)

The identifier for the pipeline. You use this value to identify the pipeline in which you want to perform a variety of operations, such as creating a job or a preset.

Arn -> (string)

The Amazon Resource Name (ARN) for the pipeline.

Name -> (string)

The name of the pipeline. We recommend that the name be unique within the AWS account, but uniqueness is not enforced.

Constraints: Maximum 40 characters

Status -> (string)

The current status of the pipeline:

- `Active` : The pipeline is processing jobs.
- `Paused` : The pipeline is not currently processing jobs.

InputBucket -> (string)

The Amazon S3 bucket from which Elastic Transcoder gets media files for transcoding and the graphics files, if any, that you want to use for watermarks.

OutputBucket -> (string)

The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files, thumbnails, and playlists. Either you specify this value, or you specify both `ContentConfig` and `ThumbnailConfig` .

Role -> (string)

The IAM Amazon Resource Name (ARN) for the role that Elastic Transcoder uses to transcode jobs for this pipeline.

AwsKmsKeyArn -> (string)

The AWS Key Management Service (AWS KMS) key that you want to use with this pipeline.

If you use either `s3` or `s3-aws-kms` as your `Encryption:Mode` , you donât need to provide a key with your job because a default key, known as an AWS-KMS key, is created for you automatically. You need to provide an AWS-KMS key only if you want to use a non-default AWS-KMS key, or if you are using an `Encryption:Mode` of `aes-cbc-pkcs7` , `aes-ctr` , or `aes-gcm` .

Notifications -> (structure)

The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify to report job status.

### Warning

To receive notifications, you must also subscribe to the new topic in the Amazon SNS console.

- **Progressing** (optional): The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process the job.
- **Complete** (optional): The Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing the job.
- **Warning** (optional): The Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition.
- **Error** (optional): The Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition.

Progressing -> (string)

The Amazon Simple Notification Service (Amazon SNS) topic that you want to notify when Elastic Transcoder has started to process the job.

Completed -> (string)

The Amazon SNS topic that you want to notify when Elastic Transcoder has finished processing the job.

Warning -> (string)

The Amazon SNS topic that you want to notify when Elastic Transcoder encounters a warning condition.

Error -> (string)

The Amazon SNS topic that you want to notify when Elastic Transcoder encounters an error condition.

ContentConfig -> (structure)

Information about the Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists. Either you specify both `ContentConfig` and `ThumbnailConfig` , or you specify `OutputBucket` .

- **Bucket** : The Amazon S3 bucket in which you want Elastic Transcoder to save transcoded files and playlists.
- **Permissions** : A list of the users and/or predefined Amazon S3 groups you want to have access to transcoded files and playlists, and the type of access that you want them to have.
- GranteeType: The type of value that appears in the `Grantee` object:
- `Canonical` : Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.
- `Email` : The registered email address of an AWS account.
- `Group` : One of the following predefined Amazon S3 groups: `AllUsers` , `AuthenticatedUsers` , or `LogDelivery` .
- `Grantee` : The AWS user or group that you want to have access to transcoded files and playlists.
- `Access` : The permission that you want to give to the AWS user that is listed in `Grantee` . Valid values include:
- `READ` : The grantee can read the objects and metadata for objects that Elastic Transcoder adds to the Amazon S3 bucket.
- `READ_ACP` : The grantee can read the object ACL for objects that Elastic Transcoder adds to the Amazon S3 bucket.
- `WRITE_ACP` : The grantee can write the ACL for the objects that Elastic Transcoder adds to the Amazon S3 bucket.
- `FULL_CONTROL` : The grantee has `READ` , `READ_ACP` , and `WRITE_ACP` permissions for the objects that Elastic Transcoder adds to the Amazon S3 bucket.
- **StorageClass** : The Amazon S3 storage class, Standard or ReducedRedundancy, that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.

Bucket -> (string)

The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files. Specify this value when all of the following are true:

- You want to save transcoded files, thumbnails (if any), and playlists (if any) together in one bucket.
- You do not want to specify the users or groups who have access to the transcoded files, thumbnails, and playlists.
- You do not want to specify the permissions that Elastic Transcoder grants to the files.
- You want to associate the transcoded files and thumbnails with the Amazon S3 Standard storage class.

If you want to save transcoded files and playlists in one bucket and thumbnails in another bucket, specify which users can access the transcoded files or the permissions the users have, or change the Amazon S3 storage class, omit OutputBucket and specify values for `ContentConfig` and `ThumbnailConfig` instead.

StorageClass -> (string)

The Amazon S3 storage class, `Standard` or `ReducedRedundancy` , that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.

Permissions -> (list)

Optional. The `Permissions` object specifies which users and/or predefined Amazon S3 groups you want to have access to transcoded files and playlists, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.

If you include `Permissions` , Elastic Transcoder grants only the permissions that you specify. It does not grant full permissions to the owner of the role specified by `Role` . If you want that user to have full control, you must explicitly grant full control to the user.

If you omit `Permissions` , Elastic Transcoder grants full control over the transcoded files and playlists to the owner of the role specified by `Role` , and grants no other permissions to any other user or group.

(structure)

The `Permission` structure.

GranteeType -> (string)

The type of value that appears in the Grantee object:

- `Canonical` : Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.

### Warning

A canonical user ID is not the same as an AWS account number.

- `Email` : The registered email address of an AWS account.
- `Group` : One of the following predefined Amazon S3 groups: `AllUsers` , `AuthenticatedUsers` , or `LogDelivery` .

Grantee -> (string)

The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group.

Access -> (list)

The permission that you want to give to the AWS user that is listed in Grantee. Valid values include:

- `READ` : The grantee can read the thumbnails and metadata for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
- `READ_ACP` : The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
- `WRITE_ACP` : The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
- `FULL_CONTROL` : The grantee has READ, READ_ACP, and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.

(string)

ThumbnailConfig -> (structure)

Information about the Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files. Either you specify both `ContentConfig` and `ThumbnailConfig` , or you specify `OutputBucket` .

- `Bucket` : The Amazon S3 bucket in which you want Elastic Transcoder to save thumbnail files.
- `Permissions` : A list of the users and/or predefined Amazon S3 groups you want to have access to thumbnail files, and the type of access that you want them to have.

- GranteeType: The type of value that appears in the Grantee object:

- `Canonical` : Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.

### Warning

A canonical user ID is not the same as an AWS account number.

- `Email` : The registered email address of an AWS account.
- `Group` : One of the following predefined Amazon S3 groups: `AllUsers` , `AuthenticatedUsers` , or `LogDelivery` .
- `Grantee` : The AWS user or group that you want to have access to thumbnail files.
- Access: The permission that you want to give to the AWS user that is listed in Grantee. Valid values include:

- `READ` : The grantee can read the thumbnails and metadata for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
- `READ_ACP` : The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
- `WRITE_ACP` : The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
- `FULL_CONTROL` : The grantee has READ, READ_ACP, and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
- `StorageClass` : The Amazon S3 storage class, `Standard` or `ReducedRedundancy` , that you want Elastic Transcoder to assign to the thumbnails that it stores in your Amazon S3 bucket.

Bucket -> (string)

The Amazon S3 bucket in which you want Elastic Transcoder to save the transcoded files. Specify this value when all of the following are true:

- You want to save transcoded files, thumbnails (if any), and playlists (if any) together in one bucket.
- You do not want to specify the users or groups who have access to the transcoded files, thumbnails, and playlists.
- You do not want to specify the permissions that Elastic Transcoder grants to the files.
- You want to associate the transcoded files and thumbnails with the Amazon S3 Standard storage class.

If you want to save transcoded files and playlists in one bucket and thumbnails in another bucket, specify which users can access the transcoded files or the permissions the users have, or change the Amazon S3 storage class, omit OutputBucket and specify values for `ContentConfig` and `ThumbnailConfig` instead.

StorageClass -> (string)

The Amazon S3 storage class, `Standard` or `ReducedRedundancy` , that you want Elastic Transcoder to assign to the video files and playlists that it stores in your Amazon S3 bucket.

Permissions -> (list)

Optional. The `Permissions` object specifies which users and/or predefined Amazon S3 groups you want to have access to transcoded files and playlists, and the type of access you want them to have. You can grant permissions to a maximum of 30 users and/or predefined Amazon S3 groups.

If you include `Permissions` , Elastic Transcoder grants only the permissions that you specify. It does not grant full permissions to the owner of the role specified by `Role` . If you want that user to have full control, you must explicitly grant full control to the user.

If you omit `Permissions` , Elastic Transcoder grants full control over the transcoded files and playlists to the owner of the role specified by `Role` , and grants no other permissions to any other user or group.

(structure)

The `Permission` structure.

GranteeType -> (string)

The type of value that appears in the Grantee object:

- `Canonical` : Either the canonical user ID for an AWS account or an origin access identity for an Amazon CloudFront distribution.

### Warning

A canonical user ID is not the same as an AWS account number.

- `Email` : The registered email address of an AWS account.
- `Group` : One of the following predefined Amazon S3 groups: `AllUsers` , `AuthenticatedUsers` , or `LogDelivery` .

Grantee -> (string)

The AWS user or group that you want to have access to transcoded files and playlists. To identify the user or group, you can specify the canonical user ID for an AWS account, an origin access identity for a CloudFront distribution, the registered email address of an AWS account, or a predefined Amazon S3 group.

Access -> (list)

The permission that you want to give to the AWS user that is listed in Grantee. Valid values include:

- `READ` : The grantee can read the thumbnails and metadata for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
- `READ_ACP` : The grantee can read the object ACL for thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
- `WRITE_ACP` : The grantee can write the ACL for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.
- `FULL_CONTROL` : The grantee has READ, READ_ACP, and WRITE_ACP permissions for the thumbnails that Elastic Transcoder adds to the Amazon S3 bucket.

(string)