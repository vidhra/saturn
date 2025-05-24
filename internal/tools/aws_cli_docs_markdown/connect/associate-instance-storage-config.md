# associate-instance-storage-configÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-instance-storage-config.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/associate-instance-storage-config.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# associate-instance-storage-config

## Description

This API is in preview release for Amazon Connect and is subject to change.

Associates a storage resource type for the first time. You can only associate one type of storage configuration in a single call. This means, for example, that you canât define an instance with multiple S3 buckets for storing chat transcripts.

This API does not create a resource that doesnât exist. It only associates it to the instance. Ensure that the resource being specified in the storage configuration, like an S3 bucket, exists when being used for association.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/AssociateInstanceStorageConfig)

## Synopsis

```
associate-instance-storage-config
--instance-id <value>
--resource-type <value>
--storage-config <value>
[--client-token <value>]
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--resource-type` (string)

A valid resource type. To [enable streaming for real-time analysis of contacts](https://docs.aws.amazon.com/connect/latest/adminguide/enable-contact-analysis-segment-streams.html) , use the following types:

- For chat contacts, use `REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS` .
- For voice contacts, use `REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS` .

### Note

`REAL_TIME_CONTACT_ANALYSIS_SEGMENTS` is deprecated, but it is still supported and will apply only to VOICE channel contacts. Use `REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS` for voice contacts moving forward.

If you have previously associated a stream with `REAL_TIME_CONTACT_ANALYSIS_SEGMENTS` , no action is needed to update the stream to `REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS` .

Possible values:

- `CHAT_TRANSCRIPTS`
- `CALL_RECORDINGS`
- `SCHEDULED_REPORTS`
- `MEDIA_STREAMS`
- `CONTACT_TRACE_RECORDS`
- `AGENT_EVENTS`
- `REAL_TIME_CONTACT_ANALYSIS_SEGMENTS`
- `ATTACHMENTS`
- `CONTACT_EVALUATIONS`
- `SCREEN_RECORDINGS`
- `REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS`
- `REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS`
- `EMAIL_MESSAGES`

`--storage-config` (structure)

A valid storage type.

AssociationId -> (string)

The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.

StorageType -> (string)

A valid storage type.

S3Config -> (structure)

The S3 bucket configuration.

BucketName -> (string)

The S3 bucket name.

BucketPrefix -> (string)

The S3 bucket prefix.

EncryptionConfig -> (structure)

The Amazon S3 encryption configuration.

EncryptionType -> (string)

The type of encryption.

KeyId -> (string)

The full ARN of the encryption key.

### Note

Be sure to provide the full ARN of the encryption key, not just the ID.

Amazon Connect supports only KMS keys with the default key spec of ` `SYMMETRIC_DEFAULT` [https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-symmetric](https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-symmetric)-default`__ .

KinesisVideoStreamConfig -> (structure)

The configuration of the Kinesis video stream.

Prefix -> (string)

The prefix of the video stream.

RetentionPeriodHours -> (integer)

The number of hours data is retained in the stream. Kinesis Video Streams retains the data in a data store that is associated with the stream.

The default value is 0, indicating that the stream does not persist data.

EncryptionConfig -> (structure)

The encryption configuration.

EncryptionType -> (string)

The type of encryption.

KeyId -> (string)

The full ARN of the encryption key.

### Note

Be sure to provide the full ARN of the encryption key, not just the ID.

Amazon Connect supports only KMS keys with the default key spec of ` `SYMMETRIC_DEFAULT` [https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-symmetric](https://docs.aws.amazon.com/kms/latest/developerguide/asymmetric-key-specs.html#key-spec-symmetric)-default`__ .

KinesisStreamConfig -> (structure)

The configuration of the Kinesis data stream.

StreamArn -> (string)

The Amazon Resource Name (ARN) of the data stream.

KinesisFirehoseConfig -> (structure)

The configuration of the Kinesis Firehose delivery stream.

FirehoseArn -> (string)

The Amazon Resource Name (ARN) of the delivery stream.

Shorthand Syntax:

```
AssociationId=string,StorageType=string,S3Config={BucketName=string,BucketPrefix=string,EncryptionConfig={EncryptionType=string,KeyId=string}},KinesisVideoStreamConfig={Prefix=string,RetentionPeriodHours=integer,EncryptionConfig={EncryptionType=string,KeyId=string}},KinesisStreamConfig={StreamArn=string},KinesisFirehoseConfig={FirehoseArn=string}
```

JSON Syntax:

```
{
  "AssociationId": "string",
  "StorageType": "S3"|"KINESIS_VIDEO_STREAM"|"KINESIS_STREAM"|"KINESIS_FIREHOSE",
  "S3Config": {
    "BucketName": "string",
    "BucketPrefix": "string",
    "EncryptionConfig": {
      "EncryptionType": "KMS",
      "KeyId": "string"
    }
  },
  "KinesisVideoStreamConfig": {
    "Prefix": "string",
    "RetentionPeriodHours": integer,
    "EncryptionConfig": {
      "EncryptionType": "KMS",
      "KeyId": "string"
    }
  },
  "KinesisStreamConfig": {
    "StreamArn": "string"
  },
  "KinesisFirehoseConfig": {
    "FirehoseArn": "string"
  }
}
```

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) .

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

AssociationId -> (string)

The existing association identifier that uniquely identifies the resource type and storage config for the given instance ID.