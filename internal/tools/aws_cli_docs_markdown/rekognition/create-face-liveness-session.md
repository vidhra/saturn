# create-face-liveness-sessionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-face-liveness-session.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/create-face-liveness-session.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [rekognition](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/rekognition/index.html#cli-aws-rekognition) ]

# create-face-liveness-session

## Description

This API operation initiates a Face Liveness session. It returns a `SessionId` , which you can use to start streaming Face Liveness video and get the results for a Face Liveness session.

You can use the `OutputConfig` option in the Settings parameter to provide an Amazon S3 bucket location. The Amazon S3 bucket stores reference images and audit images. If no Amazon S3 bucket is defined, raw bytes are sent instead.

You can use `AuditImagesLimit` to limit the number of audit images returned when `GetFaceLivenessSessionResults` is called. This number is between 0 and 4. By default, it is set to 0. The limit is best effort and based on the duration of the selfie-video.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/rekognition-2016-06-27/CreateFaceLivenessSession)

## Synopsis

```
create-face-liveness-session
[--kms-key-id <value>]
[--settings <value>]
[--client-request-token <value>]
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

`--kms-key-id` (string)

The identifier for your AWS Key Management Service key (AWS KMS key). Used to encrypt audit images and reference images.

`--settings` (structure)

A session settings object. It contains settings for the operation to be performed. For Face Liveness, it accepts `OutputConfig` and `AuditImagesLimit` .

OutputConfig -> (structure)

Can specify the location of an Amazon S3 bucket, where reference and audit images will be stored. Note that the Amazon S3 bucket must be located in the callerâs AWS account and in the same region as the Face Liveness end-point. Additionally, the Amazon S3 object keys are auto-generated by the Face Liveness system. Requires that the caller has the `s3:PutObject` permission on the Amazon S3 bucket.

S3Bucket -> (string)

The path to an AWS Amazon S3 bucket used to store Face Liveness session results.

S3KeyPrefix -> (string)

The prefix prepended to the output files for the Face Liveness session results.

AuditImagesLimit -> (integer)

Number of audit images to be returned back. Takes an integer between 0-4. Any integer less than 0 will return 0, any integer above 4 will return 4 images in the response. By default, it is set to 0. The limit is best effort and is based on the actual duration of the selfie-video.

Shorthand Syntax:

```
OutputConfig={S3Bucket=string,S3KeyPrefix=string},AuditImagesLimit=integer
```

JSON Syntax:

```
{
  "OutputConfig": {
    "S3Bucket": "string",
    "S3KeyPrefix": "string"
  },
  "AuditImagesLimit": integer
}
```

`--client-request-token` (string)

Idempotent token is used to recognize the Face Liveness request. If the same token is used with multiple `CreateFaceLivenessSession` requests, the same session is returned. This token is employed to avoid unintentionally creating the same session multiple times.

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

SessionId -> (string)

A unique 128-bit UUID identifying a Face Liveness session. A new sessionID must be used for every Face Liveness check. If a given sessionID is used for subsequent Face Liveness checks, the checks will fail. Additionally, a SessionId expires 3 minutes after itâs sent, making all Liveness data associated with the session (e.g., sessionID, reference image, audit images, etc.) unavailable.