# get-ota-updateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-ota-update.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/get-ota-update.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iot](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html#cli-aws-iot) ]

# get-ota-update

## Description

Gets an OTA update.

Requires permission to access the [GetOTAUpdate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iot-2015-05-28/GetOTAUpdate)

## Synopsis

```
get-ota-update
--ota-update-id <value>
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

`--ota-update-id` (string)

The OTA update ID.

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

**To retrieve information about an OTA Update**

The following `get-ota-update` example displays details about the specified OTA Update.

```
aws iot get-ota-update \
    --ota-update-id ota12345
```

Output:

```
{
    "otaUpdateInfo": {
        "otaUpdateId": "ota12345",
        "otaUpdateArn": "arn:aws:iot:us-west-2:123456789012:otaupdate/itsaupdate",
        "creationDate": 1557863215.995,
        "lastModifiedDate": 1557863215.995,
        "description": "A critical update needed right away.",
        "targets": [
           "device1",
           "device2",
           "device3",
           "device4"
        ],
        "targetSelection": "SNAPSHOT",
        "protocols": ["HTTP"],
        "awsJobExecutionsRolloutConfig": {
           "maximumPerMinute": 10
        },
        "otaUpdateFiles": [
            {
                "fileName": "firmware.bin",
                "fileLocation": {
                    "stream": {
                        "streamId": "004",
                        "fileId":123
                    }
                },
                "codeSigning": {
                    "awsSignerJobId": "48c67f3c-63bb-4f92-a98a-4ee0fbc2bef6"
                }
            }
        ],
        "roleArn": "arn:aws:iam:123456789012:role/service-role/my_ota_role"
        "otaUpdateStatus": "CREATE_COMPLETE",
        "awsIotJobId": "job54321",
        "awsIotJobArn": "arn:aws:iot:us-west-2:123456789012:job/job54321",
        "errorInfo": {
        }
    }
}
```

For more information, see [GetOTAUpdate](https://docs.aws.amazon.com/iot/latest/apireference/API_GetOTAUpdate.html) in the *AWS IoT API Reference*.

## Output

otaUpdateInfo -> (structure)

The OTA update info.

otaUpdateId -> (string)

The OTA update ID.

otaUpdateArn -> (string)

The OTA update ARN.

creationDate -> (timestamp)

The date when the OTA update was created.

lastModifiedDate -> (timestamp)

The date when the OTA update was last updated.

description -> (string)

A description of the OTA update.

targets -> (list)

The targets of the OTA update.

(string)

protocols -> (list)

The protocol used to transfer the OTA update image. Valid values are [HTTP], [MQTT], [HTTP, MQTT]. When both HTTP and MQTT are specified, the target device can choose the protocol.

(string)

awsJobExecutionsRolloutConfig -> (structure)

Configuration for the rollout of OTA updates.

maximumPerMinute -> (integer)

The maximum number of OTA update job executions started per minute.

exponentialRate -> (structure)

The rate of increase for a job rollout. This parameter allows you to define an exponential rate increase for a job rollout.

baseRatePerMinute -> (integer)

The minimum number of things that will be notified of a pending job, per minute, at the start of the job rollout. This is the initial rate of the rollout.

incrementFactor -> (double)

The rate of increase for a job rollout. The number of things notified is multiplied by this factor.

rateIncreaseCriteria -> (structure)

The criteria to initiate the increase in rate of rollout for a job.

Amazon Web Services IoT Core supports up to one digit after the decimal (for example, 1.5, but not 1.55).

numberOfNotifiedThings -> (integer)

When this number of things have been notified, it will initiate an increase in the rollout rate.

numberOfSucceededThings -> (integer)

When this number of things have succeeded in their job execution, it will initiate an increase in the rollout rate.

awsJobPresignedUrlConfig -> (structure)

Configuration information for pre-signed URLs. Valid when `protocols` contains HTTP.

expiresInSec -> (long)

How long (in seconds) pre-signed URLs are valid. Valid values are 60 - 3600, the default value is 1800 seconds. Pre-signed URLs are generated when a request for the job document is received.

targetSelection -> (string)

Specifies whether the OTA update will continue to run (CONTINUOUS), or will be complete after all those things specified as targets have completed the OTA update (SNAPSHOT). If continuous, the OTA update may also be run on a thing when a change is detected in a target. For example, an OTA update will run on a thing when the thing is added to a target group, even after the OTA update was completed by all things originally in the group.

otaUpdateFiles -> (list)

A list of files associated with the OTA update.

(structure)

Describes a file to be associated with an OTA update.

fileName -> (string)

The name of the file.

fileType -> (integer)

An integer value you can include in the job document to allow your devices to identify the type of file received from the cloud.

fileVersion -> (string)

The file version.

fileLocation -> (structure)

The location of the updated firmware.

stream -> (structure)

The stream that contains the OTA update.

streamId -> (string)

The stream ID.

fileId -> (integer)

The ID of a file associated with a stream.

s3Location -> (structure)

The location of the updated firmware in S3.

bucket -> (string)

The S3 bucket.

key -> (string)

The S3 key.

version -> (string)

The S3 bucket version.

codeSigning -> (structure)

The code signing method of the file.

awsSignerJobId -> (string)

The ID of the `AWSSignerJob` which was created to sign the file.

startSigningJobParameter -> (structure)

Describes the code-signing job.

signingProfileParameter -> (structure)

Describes the code-signing profile.

certificateArn -> (string)

Certificate ARN.

platform -> (string)

The hardware platform of your device.

certificatePathOnDevice -> (string)

The location of the code-signing certificate on your device.

signingProfileName -> (string)

The code-signing profile name.

destination -> (structure)

The location to write the code-signed file.

s3Destination -> (structure)

Describes the location in S3 of the updated firmware.

bucket -> (string)

The S3 bucket that contains the updated firmware.

prefix -> (string)

The S3 prefix.

customCodeSigning -> (structure)

A custom method for code signing a file.

signature -> (structure)

The signature for the file.

inlineDocument -> (blob)

A base64 encoded binary representation of the code signing signature.

certificateChain -> (structure)

The certificate chain.

certificateName -> (string)

The name of the certificate.

inlineDocument -> (string)

A base64 encoded binary representation of the code signing certificate chain.

hashAlgorithm -> (string)

The hash algorithm used to code sign the file. You can use a string as the algorithm name if the target over-the-air (OTA) update devices are able to verify the signature that was generated using the same signature algorithm. For example, FreeRTOS uses `SHA256` or `SHA1` , so you can pass either of them based on which was used for generating the signature.

signatureAlgorithm -> (string)

The signature algorithm used to code sign the file. You can use a string as the algorithm name if the target over-the-air (OTA) update devices are able to verify the signature that was generated using the same signature algorithm. For example, FreeRTOS uses `ECDSA` or `RSA` , so you can pass either of them based on which was used for generating the signature.

attributes -> (map)

A list of name-attribute pairs. They wonât be sent to devices as a part of the Job document.

key -> (string)

value -> (string)

otaUpdateStatus -> (string)

The status of the OTA update.

awsIotJobId -> (string)

The IoT job ID associated with the OTA update.

awsIotJobArn -> (string)

The IoT job ARN associated with the OTA update.

errorInfo -> (structure)

Error information associated with the OTA update.

code -> (string)

The error code.

message -> (string)

The error message.

additionalParameters -> (map)

A collection of name/value pairs

key -> (string)

value -> (string)