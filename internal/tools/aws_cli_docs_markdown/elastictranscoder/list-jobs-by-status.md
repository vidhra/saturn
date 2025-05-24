# list-jobs-by-statusÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/list-jobs-by-status.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/list-jobs-by-status.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elastictranscoder](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elastictranscoder/index.html#cli-aws-elastictranscoder) ]

# list-jobs-by-status

## Description

The ListJobsByStatus operation gets a list of jobs that have a specified status. The response body contains one element for each job that satisfies the search criteria.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elastictranscoder-2012-09-25/ListJobsByStatus)

`list-jobs-by-status` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Jobs`

## Synopsis

```
list-jobs-by-status
--status <value>
[--ascending <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--status` (string)

To get information about all of the jobs associated with the current AWS account that have a given status, specify the following status: `Submitted` , `Progressing` , `Complete` , `Canceled` , or `Error` .

`--ascending` (string)

To list jobs in chronological order by the date and time that they were submitted, enter `true` . To list jobs in reverse chronological order, enter `false` .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To retrieve a list of ElasticTranscoder jobs with a status of Complete**

This example retrieves a list of ElasticTranscoder jobs with a status of Complete.

Command:

```
aws elastictranscoder list-jobs-by-status --status Complete
```

Output:

```
{
   "Jobs": []
}
```

## Output

Jobs -> (list)

An array of `Job` objects that have the specified status.

(structure)

A section of the response body that provides information about the job that is created.

Id -> (string)

The identifier that Elastic Transcoder assigned to the job. You use this value to get settings for the job or to delete the job.

Arn -> (string)

The Amazon Resource Name (ARN) for the job.

PipelineId -> (string)

The `Id` of the pipeline that you want Elastic Transcoder to use for transcoding. The pipeline determines several settings, including the Amazon S3 bucket from which Elastic Transcoder gets the files to transcode and the bucket into which Elastic Transcoder puts the transcoded files.

Input -> (structure)

A section of the request or response body that provides information about the file that is being transcoded.

Key -> (string)

The name of the file to transcode. Elsewhere in the body of the JSON block is the the ID of the pipeline to use for processing the job. The `InputBucket` object in that pipeline tells Elastic Transcoder which Amazon S3 bucket to get the file from.

If the file name includes a prefix, such as `cooking/lasagna.mpg` , include the prefix in the key. If the file isnât in the specified bucket, Elastic Transcoder returns an error.

FrameRate -> (string)

The frame rate of the input file. If you want Elastic Transcoder to automatically detect the frame rate of the input file, specify `auto` . If you want to specify the frame rate for the input file, enter one of the following values:

`10` , `15` , `23.97` , `24` , `25` , `29.97` , `30` , `60`

If you specify a value other than `auto` , Elastic Transcoder disables automatic detection of the frame rate.

Resolution -> (string)

This value must be `auto` , which causes Elastic Transcoder to automatically detect the resolution of the input file.

AspectRatio -> (string)

The aspect ratio of the input file. If you want Elastic Transcoder to automatically detect the aspect ratio of the input file, specify `auto` . If you want to specify the aspect ratio for the output file, enter one of the following values:

`1:1` , `4:3` , `3:2` , `16:9`

If you specify a value other than `auto` , Elastic Transcoder disables automatic detection of the aspect ratio.

Interlaced -> (string)

Whether the input file is interlaced. If you want Elastic Transcoder to automatically detect whether the input file is interlaced, specify `auto` . If you want to specify whether the input file is interlaced, enter one of the following values:

`true` , `false`

If you specify a value other than `auto` , Elastic Transcoder disables automatic detection of interlacing.

Container -> (string)

The container type for the input file. If you want Elastic Transcoder to automatically detect the container type of the input file, specify `auto` . If you want to specify the container type for the input file, enter one of the following values:

`3gp` , `aac` , `asf` , `avi` , `divx` , `flv` , `m4a` , `mkv` , `mov` , `mp3` , `mp4` , `mpeg` , `mpeg-ps` , `mpeg-ts` , `mxf` , `ogg` , `vob` , `wav` , `webm`

Encryption -> (structure)

The encryption settings, if any, that are used for decrypting your input files. If your input file is encrypted, you must specify the mode that Elastic Transcoder uses to decrypt your file.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

TimeSpan -> (structure)

Settings for clipping an input. Each input can have different clip settings.

StartTime -> (string)

The place in the input file where you want a clip to start. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you donât specify a value, Elastic Transcoder starts at the beginning of the input file.

Duration -> (string)

The duration of the clip. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you donât specify a value, Elastic Transcoder creates an output file from StartTime to the end of the file.

If you specify a value longer than the duration of the input file, Elastic Transcoder transcodes the file and returns a warning message.

InputCaptions -> (structure)

You can configure Elastic Transcoder to transcode captions, or subtitles, from one format to another. All captions must be in UTF-8. Elastic Transcoder supports two types of captions:

- **Embedded:** Embedded captions are included in the same file as the audio and video. Elastic Transcoder supports only one embedded caption per language, to a maximum of 300 embedded captions per file. Valid input values include: `CEA-608 (EIA-608` , first non-empty channel only), `CEA-708 (EIA-708` , first non-empty channel only), and `mov-text`   Valid outputs include: `mov-text`   Elastic Transcoder supports a maximum of one embedded format per output.
- **Sidecar:** Sidecar captions are kept in a separate metadata file from the audio and video data. Sidecar captions require a player that is capable of understanding the relationship between the video file and the sidecar file. Elastic Transcoder supports only one sidecar caption per language, to a maximum of 20 sidecar captions per file. Valid input values include: `dfxp` (first div element only), `ebu-tt` , `scc` , `smpt` , `srt` , `ttml` (first div element only), and `webvtt`   Valid outputs include: `dfxp` (first div element only), `scc` , `srt` , and `webvtt` .

If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.

Elastic Transcoder does not support OCR (Optical Character Recognition), does not accept pictures as a valid input for captions, and is not available for audio-only transcoding. Elastic Transcoder does not preserve text formatting (for example, italics) during the transcoding process.

To remove captions or leave the captions empty, set `Captions` to null. To pass through existing captions unchanged, set the `MergePolicy` to `MergeRetain` , and pass in a null `CaptionSources` array.

For more information on embedded files, see the Subtitles Wikipedia page.

For more information on sidecar files, see the Extensible Metadata Platform and Sidecar file Wikipedia pages.

MergePolicy -> (string)

A policy that determines how Elastic Transcoder handles the existence of multiple captions.

- **MergeOverride:** Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the sidecar captions and ignores the embedded captions for that language.
- **MergeRetain:** Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the embedded captions and ignores the sidecar captions for that language. If `CaptionSources` is empty, Elastic Transcoder omits all sidecar captions from the output files.
- **Override:** Elastic Transcoder transcodes only the sidecar captions that you specify in `CaptionSources` .

`MergePolicy` cannot be null.

CaptionSources -> (list)

Source files for the input sidecar captions used during the transcoding process. To omit all sidecar captions, leave `CaptionSources` blank.

(structure)

A source file for the input sidecar captions used during the transcoding process.

Key -> (string)

The name of the sidecar caption file that you want Elastic Transcoder to include in the output file.

Language -> (string)

A string that specifies the language of the caption. If you specified multiple inputs with captions, the caption language must match in order to be included in the output. Specify this as one of:

- 2-character ISO 639-1 code
- 3-character ISO 639-2 code

For more information on ISO language codes and language names, see the List of ISO 639-1 codes.

TimeOffset -> (string)

For clip generation or captions that do not start at the same time as the associated video file, the `TimeOffset` tells Elastic Transcoder how much of the video to encode before including captions.

Specify the TimeOffset in the form [+-]SS.sss or [+-]HH:mm:SS.ss.

Label -> (string)

The label of the caption shown in the player when choosing a language. We recommend that you put the caption language name here, in the language of the captions.

Encryption -> (structure)

The encryption settings, if any, that Elastic Transcoder needs to decyrpt your caption sources, or that you want Elastic Transcoder to apply to your caption sources.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

DetectedProperties -> (structure)

The detected properties of the input file.

Width -> (integer)

The detected width of the input file, in pixels.

Height -> (integer)

The detected height of the input file, in pixels.

FrameRate -> (string)

The detected frame rate of the input file, in frames per second.

FileSize -> (long)

The detected file size of the input file, in bytes.

DurationMillis -> (long)

The detected duration of the input file, in milliseconds.

Inputs -> (list)

Information about the files that youâre transcoding. If you specified multiple files for this job, Elastic Transcoder stitches the files together to make one output.

(structure)

Information about the file that youâre transcoding.

Key -> (string)

The name of the file to transcode. Elsewhere in the body of the JSON block is the the ID of the pipeline to use for processing the job. The `InputBucket` object in that pipeline tells Elastic Transcoder which Amazon S3 bucket to get the file from.

If the file name includes a prefix, such as `cooking/lasagna.mpg` , include the prefix in the key. If the file isnât in the specified bucket, Elastic Transcoder returns an error.

FrameRate -> (string)

The frame rate of the input file. If you want Elastic Transcoder to automatically detect the frame rate of the input file, specify `auto` . If you want to specify the frame rate for the input file, enter one of the following values:

`10` , `15` , `23.97` , `24` , `25` , `29.97` , `30` , `60`

If you specify a value other than `auto` , Elastic Transcoder disables automatic detection of the frame rate.

Resolution -> (string)

This value must be `auto` , which causes Elastic Transcoder to automatically detect the resolution of the input file.

AspectRatio -> (string)

The aspect ratio of the input file. If you want Elastic Transcoder to automatically detect the aspect ratio of the input file, specify `auto` . If you want to specify the aspect ratio for the output file, enter one of the following values:

`1:1` , `4:3` , `3:2` , `16:9`

If you specify a value other than `auto` , Elastic Transcoder disables automatic detection of the aspect ratio.

Interlaced -> (string)

Whether the input file is interlaced. If you want Elastic Transcoder to automatically detect whether the input file is interlaced, specify `auto` . If you want to specify whether the input file is interlaced, enter one of the following values:

`true` , `false`

If you specify a value other than `auto` , Elastic Transcoder disables automatic detection of interlacing.

Container -> (string)

The container type for the input file. If you want Elastic Transcoder to automatically detect the container type of the input file, specify `auto` . If you want to specify the container type for the input file, enter one of the following values:

`3gp` , `aac` , `asf` , `avi` , `divx` , `flv` , `m4a` , `mkv` , `mov` , `mp3` , `mp4` , `mpeg` , `mpeg-ps` , `mpeg-ts` , `mxf` , `ogg` , `vob` , `wav` , `webm`

Encryption -> (structure)

The encryption settings, if any, that are used for decrypting your input files. If your input file is encrypted, you must specify the mode that Elastic Transcoder uses to decrypt your file.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

TimeSpan -> (structure)

Settings for clipping an input. Each input can have different clip settings.

StartTime -> (string)

The place in the input file where you want a clip to start. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you donât specify a value, Elastic Transcoder starts at the beginning of the input file.

Duration -> (string)

The duration of the clip. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you donât specify a value, Elastic Transcoder creates an output file from StartTime to the end of the file.

If you specify a value longer than the duration of the input file, Elastic Transcoder transcodes the file and returns a warning message.

InputCaptions -> (structure)

You can configure Elastic Transcoder to transcode captions, or subtitles, from one format to another. All captions must be in UTF-8. Elastic Transcoder supports two types of captions:

- **Embedded:** Embedded captions are included in the same file as the audio and video. Elastic Transcoder supports only one embedded caption per language, to a maximum of 300 embedded captions per file. Valid input values include: `CEA-608 (EIA-608` , first non-empty channel only), `CEA-708 (EIA-708` , first non-empty channel only), and `mov-text`   Valid outputs include: `mov-text`   Elastic Transcoder supports a maximum of one embedded format per output.
- **Sidecar:** Sidecar captions are kept in a separate metadata file from the audio and video data. Sidecar captions require a player that is capable of understanding the relationship between the video file and the sidecar file. Elastic Transcoder supports only one sidecar caption per language, to a maximum of 20 sidecar captions per file. Valid input values include: `dfxp` (first div element only), `ebu-tt` , `scc` , `smpt` , `srt` , `ttml` (first div element only), and `webvtt`   Valid outputs include: `dfxp` (first div element only), `scc` , `srt` , and `webvtt` .

If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.

Elastic Transcoder does not support OCR (Optical Character Recognition), does not accept pictures as a valid input for captions, and is not available for audio-only transcoding. Elastic Transcoder does not preserve text formatting (for example, italics) during the transcoding process.

To remove captions or leave the captions empty, set `Captions` to null. To pass through existing captions unchanged, set the `MergePolicy` to `MergeRetain` , and pass in a null `CaptionSources` array.

For more information on embedded files, see the Subtitles Wikipedia page.

For more information on sidecar files, see the Extensible Metadata Platform and Sidecar file Wikipedia pages.

MergePolicy -> (string)

A policy that determines how Elastic Transcoder handles the existence of multiple captions.

- **MergeOverride:** Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the sidecar captions and ignores the embedded captions for that language.
- **MergeRetain:** Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the embedded captions and ignores the sidecar captions for that language. If `CaptionSources` is empty, Elastic Transcoder omits all sidecar captions from the output files.
- **Override:** Elastic Transcoder transcodes only the sidecar captions that you specify in `CaptionSources` .

`MergePolicy` cannot be null.

CaptionSources -> (list)

Source files for the input sidecar captions used during the transcoding process. To omit all sidecar captions, leave `CaptionSources` blank.

(structure)

A source file for the input sidecar captions used during the transcoding process.

Key -> (string)

The name of the sidecar caption file that you want Elastic Transcoder to include in the output file.

Language -> (string)

A string that specifies the language of the caption. If you specified multiple inputs with captions, the caption language must match in order to be included in the output. Specify this as one of:

- 2-character ISO 639-1 code
- 3-character ISO 639-2 code

For more information on ISO language codes and language names, see the List of ISO 639-1 codes.

TimeOffset -> (string)

For clip generation or captions that do not start at the same time as the associated video file, the `TimeOffset` tells Elastic Transcoder how much of the video to encode before including captions.

Specify the TimeOffset in the form [+-]SS.sss or [+-]HH:mm:SS.ss.

Label -> (string)

The label of the caption shown in the player when choosing a language. We recommend that you put the caption language name here, in the language of the captions.

Encryption -> (structure)

The encryption settings, if any, that Elastic Transcoder needs to decyrpt your caption sources, or that you want Elastic Transcoder to apply to your caption sources.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

DetectedProperties -> (structure)

The detected properties of the input file.

Width -> (integer)

The detected width of the input file, in pixels.

Height -> (integer)

The detected height of the input file, in pixels.

FrameRate -> (string)

The detected frame rate of the input file, in frames per second.

FileSize -> (long)

The detected file size of the input file, in bytes.

DurationMillis -> (long)

The detected duration of the input file, in milliseconds.

Output -> (structure)

If you specified one output for a job, information about that output. If you specified multiple outputs for a job, the Output object lists information about the first output. This duplicates the information that is listed for the first output in the Outputs object.

### Warning

Outputs recommended instead.

A section of the request or response body that provides information about the transcoded (target) file.

Id -> (string)

A sequential counter, starting with 1, that identifies an output among the outputs from the current job. In the Output syntax, this value is always 1.

Key -> (string)

The name to assign to the transcoded file. Elastic Transcoder saves the file in the Amazon S3 bucket specified by the `OutputBucket` object in the pipeline that is specified by the pipeline ID.

ThumbnailPattern -> (string)

Whether you want Elastic Transcoder to create thumbnails for your videos and, if so, how you want Elastic Transcoder to name the files.

If you donât want Elastic Transcoder to create thumbnails, specify ââ.

If you do want Elastic Transcoder to create thumbnails, specify the information that you want to include in the file name for each thumbnail. You can specify the following values in any sequence:

- **``{count}`` (Required)** : If you want to create thumbnails, you must include `{count}` in the `ThumbnailPattern` object. Wherever you specify `{count}` , Elastic Transcoder adds a five-digit sequence number (beginning with **00001** ) to thumbnail file names. The number indicates where a given thumbnail appears in the sequence of thumbnails for a transcoded file.

### Warning

If you specify a literal value and/or `{resolution}` but you omit `{count}` , Elastic Transcoder returns a validation error and does not create the job.

- **Literal values (Optional)** : You can specify literal values anywhere in the `ThumbnailPattern` object. For example, you can include them as a file name prefix or as a delimiter between `{resolution}` and `{count}` .
- **``{resolution}`` (Optional)** : If you want Elastic Transcoder to include the resolution in the file name, include `{resolution}` in the `ThumbnailPattern` object.

When creating thumbnails, Elastic Transcoder automatically saves the files in the format (.jpg or .png) that appears in the preset that you specified in the `PresetID` value of `CreateJobOutput` . Elastic Transcoder also appends the applicable file name extension.

ThumbnailEncryption -> (structure)

The encryption settings, if any, that you want Elastic Transcoder to apply to your thumbnail.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

Rotate -> (string)

The number of degrees clockwise by which you want Elastic Transcoder to rotate the output relative to the input. Enter one of the following values:

`auto` , `0` , `90` , `180` , `270`

The value `auto` generally works only if the file that youâre transcoding contains rotation metadata.

PresetId -> (string)

The value of the `Id` object for the preset that you want to use for this job. The preset determines the audio, video, and thumbnail settings that Elastic Transcoder uses for transcoding. To use a preset that you created, specify the preset ID that Elastic Transcoder returned in the response when you created the preset. You can also use the Elastic Transcoder system presets, which you can get with `ListPresets` .

SegmentDuration -> (string)

### Warning

(Outputs in Fragmented MP4 or MPEG-TS format only.

If you specify a preset in `PresetId` for which the value of `Container` is `fmp4` (Fragmented MP4) or `ts` (MPEG-TS), `SegmentDuration` is the target maximum duration of each segment in seconds. For `HLSv3` format playlists, each media segment is stored in a separate `.ts` file. For `HLSv4` , `MPEG-DASH` , and `Smooth` playlists, all media segments for an output are stored in a single file. Each segment is approximately the length of the `SegmentDuration` , though individual segments might be shorter or longer.

The range of valid values is 1 to 60 seconds. If the duration of the video is not evenly divisible by `SegmentDuration` , the duration of the last segment is the remainder of total length/SegmentDuration.

Elastic Transcoder creates an output-specific playlist for each output `HLS` output that you specify in OutputKeys. To add an output to the master playlist for this job, include it in the `OutputKeys` of the associated playlist.

Status -> (string)

The status of one output in a job. If you specified only one output for the job, `Outputs:Status` is always the same as `Job:Status` . If you specified more than one output:

- `Job:Status` and `Outputs:Status` for all of the outputs is Submitted until Elastic Transcoder starts to process the first output.
- When Elastic Transcoder starts to process the first output, `Outputs:Status` for that output and `Job:Status` both change to Progressing. For each output, the value of `Outputs:Status` remains Submitted until Elastic Transcoder starts to process the output.
- Job:Status remains Progressing until all of the outputs reach a terminal status, either Complete or Error.
- When all of the outputs reach a terminal status, `Job:Status` changes to Complete only if `Outputs:Status` for all of the outputs is `Complete` . If `Outputs:Status` for one or more outputs is `Error` , the terminal status for `Job:Status` is also `Error` .

The value of `Status` is one of the following: `Submitted` , `Progressing` , `Complete` , `Canceled` , or `Error` .

StatusDetail -> (string)

Information that further explains `Status` .

Duration -> (long)

Duration of the output file, in seconds.

Width -> (integer)

Specifies the width of the output file in pixels.

Height -> (integer)

Height of the output file, in pixels.

FrameRate -> (string)

Frame rate of the output file, in frames per second.

FileSize -> (long)

File size of the output file, in bytes.

DurationMillis -> (long)

Duration of the output file, in milliseconds.

Watermarks -> (list)

Information about the watermarks that you want Elastic Transcoder to add to the video during transcoding. You can specify up to four watermarks for each output. Settings for each watermark must be defined in the preset that you specify in `Preset` for the current output.

Watermarks are added to the output video in the sequence in which you list them in the job outputâthe first watermark in the list is added to the output video first, the second watermark in the list is added next, and so on. As a result, if the settings in a preset cause Elastic Transcoder to place all watermarks in the same location, the second watermark that you add covers the first one, the third one covers the second, and the fourth one covers the third.

(structure)

Watermarks can be in .png or .jpg format. If you want to display a watermark that is not rectangular, use the .png format, which supports transparency.

PresetWatermarkId -> (string)

The ID of the watermark settings that Elastic Transcoder uses to add watermarks to the video during transcoding. The settings are in the preset specified by Preset for the current output. In that preset, the value of Watermarks Id tells Elastic Transcoder which settings to use.

InputKey -> (string)

The name of the .png or .jpg file that you want to use for the watermark. To determine which Amazon S3 bucket contains the specified file, Elastic Transcoder checks the pipeline specified by `Pipeline` ; the `Input Bucket` object in that pipeline identifies the bucket.

If the file name includes a prefix, for example, **logos/128x64.png** , include the prefix in the key. If the file isnât in the specified bucket, Elastic Transcoder returns an error.

Encryption -> (structure)

The encryption settings, if any, that you want Elastic Transcoder to apply to your watermarks.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

AlbumArt -> (structure)

The album art to be associated with the output file, if any.

MergePolicy -> (string)

A policy that determines how Elastic Transcoder handles the existence of multiple album artwork files.

- `Replace:` The specified album art replaces any existing album art.
- `Prepend:` The specified album art is placed in front of any existing album art.
- `Append:` The specified album art is placed after any existing album art.
- `Fallback:` If the original input file contains artwork, Elastic Transcoder uses that artwork for the output. If the original input does not contain artwork, Elastic Transcoder uses the specified album art file.

Artwork -> (list)

The file to be used as album art. There can be multiple artworks associated with an audio file, to a maximum of 20. Valid formats are `.jpg` and `.png`

(structure)

The file to be used as album art. There can be multiple artworks associated with an audio file, to a maximum of 20.

To remove artwork or leave the artwork empty, you can either set `Artwork` to null, or set the `Merge Policy` to âReplaceâ and use an empty `Artwork` array.

To pass through existing artwork unchanged, set the `Merge Policy` to âPrependâ, âAppendâ, or âFallbackâ, and use an empty `Artwork` array.

InputKey -> (string)

The name of the file to be used as album art. To determine which Amazon S3 bucket contains the specified file, Elastic Transcoder checks the pipeline specified by `PipelineId` ; the `InputBucket` object in that pipeline identifies the bucket.

If the file name includes a prefix, for example, `cooking/pie.jpg` , include the prefix in the key. If the file isnât in the specified bucket, Elastic Transcoder returns an error.

MaxWidth -> (string)

The maximum width of the output album art in pixels. If you specify `auto` , Elastic Transcoder uses 600 as the default value. If you specify a numeric value, enter an even integer between 32 and 4096, inclusive.

MaxHeight -> (string)

The maximum height of the output album art in pixels. If you specify `auto` , Elastic Transcoder uses 600 as the default value. If you specify a numeric value, enter an even integer between 32 and 3072, inclusive.

SizingPolicy -> (string)

Specify one of the following values to control scaling of the output album art:

- `Fit:` Elastic Transcoder scales the output art so it matches the value that you specified in either `MaxWidth` or `MaxHeight` without exceeding the other value.
- `Fill:` Elastic Transcoder scales the output art so it matches the value that you specified in either `MaxWidth` or `MaxHeight` and matches or exceeds the other value. Elastic Transcoder centers the output art and then crops it in the dimension (if any) that exceeds the maximum value.
- `Stretch:` Elastic Transcoder stretches the output art to match the values that you specified for `MaxWidth` and `MaxHeight` . If the relative proportions of the input art and the output art are different, the output art will be distorted.
- `Keep:` Elastic Transcoder does not scale the output art. If either dimension of the input art exceeds the values that you specified for `MaxWidth` and `MaxHeight` , Elastic Transcoder crops the output art.
- `ShrinkToFit:` Elastic Transcoder scales the output art down so that its dimensions match the values that you specified for at least one of `MaxWidth` and `MaxHeight` without exceeding either value. If you specify this option, Elastic Transcoder does not scale the art up.
- `ShrinkToFill` Elastic Transcoder scales the output art down so that its dimensions match the values that you specified for at least one of `MaxWidth` and `MaxHeight` without dropping below either value. If you specify this option, Elastic Transcoder does not scale the art up.

PaddingPolicy -> (string)

When you set `PaddingPolicy` to `Pad` , Elastic Transcoder may add white bars to the top and bottom and/or left and right sides of the output album art to make the total size of the output art match the values that you specified for `MaxWidth` and `MaxHeight` .

AlbumArtFormat -> (string)

The format of album art, if any. Valid formats are `.jpg` and `.png` .

Encryption -> (structure)

The encryption settings, if any, that you want Elastic Transcoder to apply to your artwork.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

Composition -> (list)

You can create an output file that contains an excerpt from the input file. This excerpt, called a clip, can come from the beginning, middle, or end of the file. The Composition object contains settings for the clips that make up an output file. For the current release, you can only specify settings for a single clip per output file. The Composition object cannot be null.

(structure)

Settings for one clip in a composition. All jobs in a playlist must have the same clip settings.

TimeSpan -> (structure)

Settings that determine when a clip begins and how long it lasts.

StartTime -> (string)

The place in the input file where you want a clip to start. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you donât specify a value, Elastic Transcoder starts at the beginning of the input file.

Duration -> (string)

The duration of the clip. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you donât specify a value, Elastic Transcoder creates an output file from StartTime to the end of the file.

If you specify a value longer than the duration of the input file, Elastic Transcoder transcodes the file and returns a warning message.

Captions -> (structure)

You can configure Elastic Transcoder to transcode captions, or subtitles, from one format to another. All captions must be in UTF-8. Elastic Transcoder supports two types of captions:

- **Embedded:** Embedded captions are included in the same file as the audio and video. Elastic Transcoder supports only one embedded caption per language, to a maximum of 300 embedded captions per file. Valid input values include: `CEA-608 (EIA-608` , first non-empty channel only), `CEA-708 (EIA-708` , first non-empty channel only), and `mov-text`   Valid outputs include: `mov-text`   Elastic Transcoder supports a maximum of one embedded format per output.
- **Sidecar:** Sidecar captions are kept in a separate metadata file from the audio and video data. Sidecar captions require a player that is capable of understanding the relationship between the video file and the sidecar file. Elastic Transcoder supports only one sidecar caption per language, to a maximum of 20 sidecar captions per file. Valid input values include: `dfxp` (first div element only), `ebu-tt` , `scc` , `smpt` , `srt` , `ttml` (first div element only), and `webvtt`   Valid outputs include: `dfxp` (first div element only), `scc` , `srt` , and `webvtt` .

If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.

Elastic Transcoder does not support OCR (Optical Character Recognition), does not accept pictures as a valid input for captions, and is not available for audio-only transcoding. Elastic Transcoder does not preserve text formatting (for example, italics) during the transcoding process.

To remove captions or leave the captions empty, set `Captions` to null. To pass through existing captions unchanged, set the `MergePolicy` to `MergeRetain` , and pass in a null `CaptionSources` array.

For more information on embedded files, see the Subtitles Wikipedia page.

For more information on sidecar files, see the Extensible Metadata Platform and Sidecar file Wikipedia pages.

MergePolicy -> (string)

A policy that determines how Elastic Transcoder handles the existence of multiple captions.

- **MergeOverride:** Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the sidecar captions and ignores the embedded captions for that language.
- **MergeRetain:** Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the embedded captions and ignores the sidecar captions for that language. If `CaptionSources` is empty, Elastic Transcoder omits all sidecar captions from the output files.
- **Override:** Elastic Transcoder transcodes only the sidecar captions that you specify in `CaptionSources` .

`MergePolicy` cannot be null.

CaptionSources -> (list)

Source files for the input sidecar captions used during the transcoding process. To omit all sidecar captions, leave `CaptionSources` blank.

(structure)

A source file for the input sidecar captions used during the transcoding process.

Key -> (string)

The name of the sidecar caption file that you want Elastic Transcoder to include in the output file.

Language -> (string)

A string that specifies the language of the caption. If you specified multiple inputs with captions, the caption language must match in order to be included in the output. Specify this as one of:

- 2-character ISO 639-1 code
- 3-character ISO 639-2 code

For more information on ISO language codes and language names, see the List of ISO 639-1 codes.

TimeOffset -> (string)

For clip generation or captions that do not start at the same time as the associated video file, the `TimeOffset` tells Elastic Transcoder how much of the video to encode before including captions.

Specify the TimeOffset in the form [+-]SS.sss or [+-]HH:mm:SS.ss.

Label -> (string)

The label of the caption shown in the player when choosing a language. We recommend that you put the caption language name here, in the language of the captions.

Encryption -> (structure)

The encryption settings, if any, that Elastic Transcoder needs to decyrpt your caption sources, or that you want Elastic Transcoder to apply to your caption sources.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

CaptionFormats -> (list)

The array of file formats for the output captions. If you leave this value blank, Elastic Transcoder returns an error.

(structure)

The file format of the output captions. If you leave this value blank, Elastic Transcoder returns an error.

Format -> (string)

The format you specify determines whether Elastic Transcoder generates an embedded or sidecar caption for this output.

- **Valid Embedded Caption Formats:**
- **for FLAC** : None
- **For MP3** : None
- **For MP4** : mov-text
- **For MPEG-TS** : None
- **For ogg** : None
- **For webm** : None
- **Valid Sidecar Caption Formats:** Elastic Transcoder supports dfxp (first div element only), scc, srt, and webvtt. If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.
- **For FMP4** : dfxp
- **Non-FMP4 outputs** : All sidecar types

`fmp4` captions have an extension of `.ismt`

Pattern -> (string)

The prefix for caption filenames, in the form *description* -`{language}` , where:

- *description* is a description of the video.
- `{language}` is a literal value that Elastic Transcoder replaces with the two- or three-letter code for the language of the caption in the output file names.

If you donât include `{language}` in the file name pattern, Elastic Transcoder automatically appends â`{language}` â to the value that you specify for the description. In addition, Elastic Transcoder automatically appends the count to the end of the segment files.

For example, suppose youâre transcoding into srt format. When you enter âSydney-{language}-sunriseâ, and the language of the captions is English (en), the name of the first caption file is be Sydney-en-sunrise00000.srt.

Encryption -> (structure)

The encryption settings, if any, that you want Elastic Transcoder to apply to your caption formats.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

Encryption -> (structure)

The encryption settings, if any, that you want Elastic Transcoder to apply to your output files. If you choose to use encryption, you must specify a mode to use. If you choose not to use encryption, Elastic Transcoder writes an unencrypted file to your Amazon S3 bucket.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

AppliedColorSpaceConversion -> (string)

If Elastic Transcoder used a preset with a `ColorSpaceConversionMode` to transcode the output file, the `AppliedColorSpaceConversion` parameter shows the conversion used. If no `ColorSpaceConversionMode` was defined in the preset, this parameter is not be included in the job response.

Outputs -> (list)

Information about the output files. We recommend that you use the `Outputs` syntax for all jobs, even when you want Elastic Transcoder to transcode a file into only one format. Do not use both the `Outputs` and `Output` syntaxes in the same request. You can create a maximum of 30 outputs per job.

If you specify more than one output for a job, Elastic Transcoder creates the files for each output in the order in which you specify them in the job.

(structure)

### Warning

Outputs recommended instead.

If you specified one output for a job, information about that output. If you specified multiple outputs for a job, the `Output` object lists information about the first output. This duplicates the information that is listed for the first output in the `Outputs` object.

Id -> (string)

A sequential counter, starting with 1, that identifies an output among the outputs from the current job. In the Output syntax, this value is always 1.

Key -> (string)

The name to assign to the transcoded file. Elastic Transcoder saves the file in the Amazon S3 bucket specified by the `OutputBucket` object in the pipeline that is specified by the pipeline ID.

ThumbnailPattern -> (string)

Whether you want Elastic Transcoder to create thumbnails for your videos and, if so, how you want Elastic Transcoder to name the files.

If you donât want Elastic Transcoder to create thumbnails, specify ââ.

If you do want Elastic Transcoder to create thumbnails, specify the information that you want to include in the file name for each thumbnail. You can specify the following values in any sequence:

- **``{count}`` (Required)** : If you want to create thumbnails, you must include `{count}` in the `ThumbnailPattern` object. Wherever you specify `{count}` , Elastic Transcoder adds a five-digit sequence number (beginning with **00001** ) to thumbnail file names. The number indicates where a given thumbnail appears in the sequence of thumbnails for a transcoded file.

### Warning

If you specify a literal value and/or `{resolution}` but you omit `{count}` , Elastic Transcoder returns a validation error and does not create the job.

- **Literal values (Optional)** : You can specify literal values anywhere in the `ThumbnailPattern` object. For example, you can include them as a file name prefix or as a delimiter between `{resolution}` and `{count}` .
- **``{resolution}`` (Optional)** : If you want Elastic Transcoder to include the resolution in the file name, include `{resolution}` in the `ThumbnailPattern` object.

When creating thumbnails, Elastic Transcoder automatically saves the files in the format (.jpg or .png) that appears in the preset that you specified in the `PresetID` value of `CreateJobOutput` . Elastic Transcoder also appends the applicable file name extension.

ThumbnailEncryption -> (structure)

The encryption settings, if any, that you want Elastic Transcoder to apply to your thumbnail.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

Rotate -> (string)

The number of degrees clockwise by which you want Elastic Transcoder to rotate the output relative to the input. Enter one of the following values:

`auto` , `0` , `90` , `180` , `270`

The value `auto` generally works only if the file that youâre transcoding contains rotation metadata.

PresetId -> (string)

The value of the `Id` object for the preset that you want to use for this job. The preset determines the audio, video, and thumbnail settings that Elastic Transcoder uses for transcoding. To use a preset that you created, specify the preset ID that Elastic Transcoder returned in the response when you created the preset. You can also use the Elastic Transcoder system presets, which you can get with `ListPresets` .

SegmentDuration -> (string)

### Warning

(Outputs in Fragmented MP4 or MPEG-TS format only.

If you specify a preset in `PresetId` for which the value of `Container` is `fmp4` (Fragmented MP4) or `ts` (MPEG-TS), `SegmentDuration` is the target maximum duration of each segment in seconds. For `HLSv3` format playlists, each media segment is stored in a separate `.ts` file. For `HLSv4` , `MPEG-DASH` , and `Smooth` playlists, all media segments for an output are stored in a single file. Each segment is approximately the length of the `SegmentDuration` , though individual segments might be shorter or longer.

The range of valid values is 1 to 60 seconds. If the duration of the video is not evenly divisible by `SegmentDuration` , the duration of the last segment is the remainder of total length/SegmentDuration.

Elastic Transcoder creates an output-specific playlist for each output `HLS` output that you specify in OutputKeys. To add an output to the master playlist for this job, include it in the `OutputKeys` of the associated playlist.

Status -> (string)

The status of one output in a job. If you specified only one output for the job, `Outputs:Status` is always the same as `Job:Status` . If you specified more than one output:

- `Job:Status` and `Outputs:Status` for all of the outputs is Submitted until Elastic Transcoder starts to process the first output.
- When Elastic Transcoder starts to process the first output, `Outputs:Status` for that output and `Job:Status` both change to Progressing. For each output, the value of `Outputs:Status` remains Submitted until Elastic Transcoder starts to process the output.
- Job:Status remains Progressing until all of the outputs reach a terminal status, either Complete or Error.
- When all of the outputs reach a terminal status, `Job:Status` changes to Complete only if `Outputs:Status` for all of the outputs is `Complete` . If `Outputs:Status` for one or more outputs is `Error` , the terminal status for `Job:Status` is also `Error` .

The value of `Status` is one of the following: `Submitted` , `Progressing` , `Complete` , `Canceled` , or `Error` .

StatusDetail -> (string)

Information that further explains `Status` .

Duration -> (long)

Duration of the output file, in seconds.

Width -> (integer)

Specifies the width of the output file in pixels.

Height -> (integer)

Height of the output file, in pixels.

FrameRate -> (string)

Frame rate of the output file, in frames per second.

FileSize -> (long)

File size of the output file, in bytes.

DurationMillis -> (long)

Duration of the output file, in milliseconds.

Watermarks -> (list)

Information about the watermarks that you want Elastic Transcoder to add to the video during transcoding. You can specify up to four watermarks for each output. Settings for each watermark must be defined in the preset that you specify in `Preset` for the current output.

Watermarks are added to the output video in the sequence in which you list them in the job outputâthe first watermark in the list is added to the output video first, the second watermark in the list is added next, and so on. As a result, if the settings in a preset cause Elastic Transcoder to place all watermarks in the same location, the second watermark that you add covers the first one, the third one covers the second, and the fourth one covers the third.

(structure)

Watermarks can be in .png or .jpg format. If you want to display a watermark that is not rectangular, use the .png format, which supports transparency.

PresetWatermarkId -> (string)

The ID of the watermark settings that Elastic Transcoder uses to add watermarks to the video during transcoding. The settings are in the preset specified by Preset for the current output. In that preset, the value of Watermarks Id tells Elastic Transcoder which settings to use.

InputKey -> (string)

The name of the .png or .jpg file that you want to use for the watermark. To determine which Amazon S3 bucket contains the specified file, Elastic Transcoder checks the pipeline specified by `Pipeline` ; the `Input Bucket` object in that pipeline identifies the bucket.

If the file name includes a prefix, for example, **logos/128x64.png** , include the prefix in the key. If the file isnât in the specified bucket, Elastic Transcoder returns an error.

Encryption -> (structure)

The encryption settings, if any, that you want Elastic Transcoder to apply to your watermarks.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

AlbumArt -> (structure)

The album art to be associated with the output file, if any.

MergePolicy -> (string)

A policy that determines how Elastic Transcoder handles the existence of multiple album artwork files.

- `Replace:` The specified album art replaces any existing album art.
- `Prepend:` The specified album art is placed in front of any existing album art.
- `Append:` The specified album art is placed after any existing album art.
- `Fallback:` If the original input file contains artwork, Elastic Transcoder uses that artwork for the output. If the original input does not contain artwork, Elastic Transcoder uses the specified album art file.

Artwork -> (list)

The file to be used as album art. There can be multiple artworks associated with an audio file, to a maximum of 20. Valid formats are `.jpg` and `.png`

(structure)

The file to be used as album art. There can be multiple artworks associated with an audio file, to a maximum of 20.

To remove artwork or leave the artwork empty, you can either set `Artwork` to null, or set the `Merge Policy` to âReplaceâ and use an empty `Artwork` array.

To pass through existing artwork unchanged, set the `Merge Policy` to âPrependâ, âAppendâ, or âFallbackâ, and use an empty `Artwork` array.

InputKey -> (string)

The name of the file to be used as album art. To determine which Amazon S3 bucket contains the specified file, Elastic Transcoder checks the pipeline specified by `PipelineId` ; the `InputBucket` object in that pipeline identifies the bucket.

If the file name includes a prefix, for example, `cooking/pie.jpg` , include the prefix in the key. If the file isnât in the specified bucket, Elastic Transcoder returns an error.

MaxWidth -> (string)

The maximum width of the output album art in pixels. If you specify `auto` , Elastic Transcoder uses 600 as the default value. If you specify a numeric value, enter an even integer between 32 and 4096, inclusive.

MaxHeight -> (string)

The maximum height of the output album art in pixels. If you specify `auto` , Elastic Transcoder uses 600 as the default value. If you specify a numeric value, enter an even integer between 32 and 3072, inclusive.

SizingPolicy -> (string)

Specify one of the following values to control scaling of the output album art:

- `Fit:` Elastic Transcoder scales the output art so it matches the value that you specified in either `MaxWidth` or `MaxHeight` without exceeding the other value.
- `Fill:` Elastic Transcoder scales the output art so it matches the value that you specified in either `MaxWidth` or `MaxHeight` and matches or exceeds the other value. Elastic Transcoder centers the output art and then crops it in the dimension (if any) that exceeds the maximum value.
- `Stretch:` Elastic Transcoder stretches the output art to match the values that you specified for `MaxWidth` and `MaxHeight` . If the relative proportions of the input art and the output art are different, the output art will be distorted.
- `Keep:` Elastic Transcoder does not scale the output art. If either dimension of the input art exceeds the values that you specified for `MaxWidth` and `MaxHeight` , Elastic Transcoder crops the output art.
- `ShrinkToFit:` Elastic Transcoder scales the output art down so that its dimensions match the values that you specified for at least one of `MaxWidth` and `MaxHeight` without exceeding either value. If you specify this option, Elastic Transcoder does not scale the art up.
- `ShrinkToFill` Elastic Transcoder scales the output art down so that its dimensions match the values that you specified for at least one of `MaxWidth` and `MaxHeight` without dropping below either value. If you specify this option, Elastic Transcoder does not scale the art up.

PaddingPolicy -> (string)

When you set `PaddingPolicy` to `Pad` , Elastic Transcoder may add white bars to the top and bottom and/or left and right sides of the output album art to make the total size of the output art match the values that you specified for `MaxWidth` and `MaxHeight` .

AlbumArtFormat -> (string)

The format of album art, if any. Valid formats are `.jpg` and `.png` .

Encryption -> (structure)

The encryption settings, if any, that you want Elastic Transcoder to apply to your artwork.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

Composition -> (list)

You can create an output file that contains an excerpt from the input file. This excerpt, called a clip, can come from the beginning, middle, or end of the file. The Composition object contains settings for the clips that make up an output file. For the current release, you can only specify settings for a single clip per output file. The Composition object cannot be null.

(structure)

Settings for one clip in a composition. All jobs in a playlist must have the same clip settings.

TimeSpan -> (structure)

Settings that determine when a clip begins and how long it lasts.

StartTime -> (string)

The place in the input file where you want a clip to start. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you donât specify a value, Elastic Transcoder starts at the beginning of the input file.

Duration -> (string)

The duration of the clip. The format can be either HH:mm:ss.SSS (maximum value: 23:59:59.999; SSS is thousandths of a second) or sssss.SSS (maximum value: 86399.999). If you donât specify a value, Elastic Transcoder creates an output file from StartTime to the end of the file.

If you specify a value longer than the duration of the input file, Elastic Transcoder transcodes the file and returns a warning message.

Captions -> (structure)

You can configure Elastic Transcoder to transcode captions, or subtitles, from one format to another. All captions must be in UTF-8. Elastic Transcoder supports two types of captions:

- **Embedded:** Embedded captions are included in the same file as the audio and video. Elastic Transcoder supports only one embedded caption per language, to a maximum of 300 embedded captions per file. Valid input values include: `CEA-608 (EIA-608` , first non-empty channel only), `CEA-708 (EIA-708` , first non-empty channel only), and `mov-text`   Valid outputs include: `mov-text`   Elastic Transcoder supports a maximum of one embedded format per output.
- **Sidecar:** Sidecar captions are kept in a separate metadata file from the audio and video data. Sidecar captions require a player that is capable of understanding the relationship between the video file and the sidecar file. Elastic Transcoder supports only one sidecar caption per language, to a maximum of 20 sidecar captions per file. Valid input values include: `dfxp` (first div element only), `ebu-tt` , `scc` , `smpt` , `srt` , `ttml` (first div element only), and `webvtt`   Valid outputs include: `dfxp` (first div element only), `scc` , `srt` , and `webvtt` .

If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.

Elastic Transcoder does not support OCR (Optical Character Recognition), does not accept pictures as a valid input for captions, and is not available for audio-only transcoding. Elastic Transcoder does not preserve text formatting (for example, italics) during the transcoding process.

To remove captions or leave the captions empty, set `Captions` to null. To pass through existing captions unchanged, set the `MergePolicy` to `MergeRetain` , and pass in a null `CaptionSources` array.

For more information on embedded files, see the Subtitles Wikipedia page.

For more information on sidecar files, see the Extensible Metadata Platform and Sidecar file Wikipedia pages.

MergePolicy -> (string)

A policy that determines how Elastic Transcoder handles the existence of multiple captions.

- **MergeOverride:** Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the sidecar captions and ignores the embedded captions for that language.
- **MergeRetain:** Elastic Transcoder transcodes both embedded and sidecar captions into outputs. If captions for a language are embedded in the input file and also appear in a sidecar file, Elastic Transcoder uses the embedded captions and ignores the sidecar captions for that language. If `CaptionSources` is empty, Elastic Transcoder omits all sidecar captions from the output files.
- **Override:** Elastic Transcoder transcodes only the sidecar captions that you specify in `CaptionSources` .

`MergePolicy` cannot be null.

CaptionSources -> (list)

Source files for the input sidecar captions used during the transcoding process. To omit all sidecar captions, leave `CaptionSources` blank.

(structure)

A source file for the input sidecar captions used during the transcoding process.

Key -> (string)

The name of the sidecar caption file that you want Elastic Transcoder to include in the output file.

Language -> (string)

A string that specifies the language of the caption. If you specified multiple inputs with captions, the caption language must match in order to be included in the output. Specify this as one of:

- 2-character ISO 639-1 code
- 3-character ISO 639-2 code

For more information on ISO language codes and language names, see the List of ISO 639-1 codes.

TimeOffset -> (string)

For clip generation or captions that do not start at the same time as the associated video file, the `TimeOffset` tells Elastic Transcoder how much of the video to encode before including captions.

Specify the TimeOffset in the form [+-]SS.sss or [+-]HH:mm:SS.ss.

Label -> (string)

The label of the caption shown in the player when choosing a language. We recommend that you put the caption language name here, in the language of the captions.

Encryption -> (structure)

The encryption settings, if any, that Elastic Transcoder needs to decyrpt your caption sources, or that you want Elastic Transcoder to apply to your caption sources.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

CaptionFormats -> (list)

The array of file formats for the output captions. If you leave this value blank, Elastic Transcoder returns an error.

(structure)

The file format of the output captions. If you leave this value blank, Elastic Transcoder returns an error.

Format -> (string)

The format you specify determines whether Elastic Transcoder generates an embedded or sidecar caption for this output.

- **Valid Embedded Caption Formats:**
- **for FLAC** : None
- **For MP3** : None
- **For MP4** : mov-text
- **For MPEG-TS** : None
- **For ogg** : None
- **For webm** : None
- **Valid Sidecar Caption Formats:** Elastic Transcoder supports dfxp (first div element only), scc, srt, and webvtt. If you want ttml or smpte-tt compatible captions, specify dfxp as your output format.
- **For FMP4** : dfxp
- **Non-FMP4 outputs** : All sidecar types

`fmp4` captions have an extension of `.ismt`

Pattern -> (string)

The prefix for caption filenames, in the form *description* -`{language}` , where:

- *description* is a description of the video.
- `{language}` is a literal value that Elastic Transcoder replaces with the two- or three-letter code for the language of the caption in the output file names.

If you donât include `{language}` in the file name pattern, Elastic Transcoder automatically appends â`{language}` â to the value that you specify for the description. In addition, Elastic Transcoder automatically appends the count to the end of the segment files.

For example, suppose youâre transcoding into srt format. When you enter âSydney-{language}-sunriseâ, and the language of the captions is English (en), the name of the first caption file is be Sydney-en-sunrise00000.srt.

Encryption -> (structure)

The encryption settings, if any, that you want Elastic Transcoder to apply to your caption formats.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

Encryption -> (structure)

The encryption settings, if any, that you want Elastic Transcoder to apply to your output files. If you choose to use encryption, you must specify a mode to use. If you choose not to use encryption, Elastic Transcoder writes an unencrypted file to your Amazon S3 bucket.

Mode -> (string)

The specific server-side encryption mode that you want Elastic Transcoder to use when decrypting your input files or encrypting your output files. Elastic Transcoder supports the following options:

- **s3:** Amazon S3 creates and manages the keys used for encrypting your files.
- **s3-aws-kms:** Amazon S3 calls the Amazon Key Management Service, which creates and manages the keys that are used for encrypting your files. If you specify `s3-aws-kms` and you donât want to use the default key, you must add the AWS-KMS key that you want to use to your pipeline.
- **aes-cbc-pkcs7:** A padded cipher-block mode of operation originally used for HLS files.
- **aes-ctr:** AES Counter Mode.
- **aes-gcm:** AES Galois Counter Mode, a mode of operation that is an authenticated encryption format, meaning that a file, key, or initialization vector that has been tampered with fails the decryption process.

For all three AES options, you must provide the following settings, which must be base64-encoded:

- **Key**
- **Key MD5**
- **Initialization Vector**

### Warning

For the AES modes, your private encryption keys and your unencrypted data are never stored by AWS; therefore, it is important that you safely manage your encryption keys. If you lose them, you wonât be able to unencrypt your data.

Key -> (string)

The data encryption key that you want Elastic Transcoder to use to encrypt your output file, or that was used to encrypt your input file. The key must be base64-encoded and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using the Amazon Key Management Service.

KeyMd5 -> (string)

The MD5 digest of the key that you used to encrypt your input file, or that you want Elastic Transcoder to use to encrypt your output file. Elastic Transcoder uses the key digest as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you used to encrypt your input files or that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes long before being base64-encoded.

AppliedColorSpaceConversion -> (string)

If Elastic Transcoder used a preset with a `ColorSpaceConversionMode` to transcode the output file, the `AppliedColorSpaceConversion` parameter shows the conversion used. If no `ColorSpaceConversionMode` was defined in the preset, this parameter is not be included in the job response.

OutputKeyPrefix -> (string)

The value, if any, that you want Elastic Transcoder to prepend to the names of all files that this job creates, including output files, thumbnails, and playlists. We recommend that you add a / or some other delimiter to the end of the `OutputKeyPrefix` .

Playlists -> (list)

### Warning

Outputs in Fragmented MP4 or MPEG-TS format only.

If you specify a preset in `PresetId` for which the value of `Container` is fmp4 (Fragmented MP4) or ts (MPEG-TS), `Playlists` contains information about the master playlists that you want Elastic Transcoder to create.

The maximum number of master playlists in a job is 30.

(structure)

Use Only for Fragmented MP4 or MPEG-TS Outputs. If you specify a preset for which the value of Container is `fmp4` (Fragmented MP4) or `ts` (MPEG-TS), Playlists contains information about the master playlists that you want Elastic Transcoder to create. We recommend that you create only one master playlist per output format. The maximum number of master playlists in a job is 30.

Name -> (string)

The name that you want Elastic Transcoder to assign to the master playlist, for example, nyc-vacation.m3u8. If the name includes a `/` character, the section of the name before the last `/` must be identical for all `Name` objects. If you create more than one master playlist, the values of all `Name` objects must be unique.

### Note

Elastic Transcoder automatically appends the relevant file extension to the file name (`.m3u8` for `HLSv3` and `HLSv4` playlists, and `.ism` and `.ismc` for `Smooth` playlists). If you include a file extension in `Name` , the file name will have two extensions.

Format -> (string)

The format of the output playlist. Valid formats include `HLSv3` , `HLSv4` , and `Smooth` .

OutputKeys -> (list)

For each output in this job that you want to include in a master playlist, the value of the Outputs:Key object.

- If your output is not `HLS` or does not have a segment duration set, the name of the output file is a concatenation of `OutputKeyPrefix` and `Outputs:Key` : OutputKeyPrefix``Outputs:Key``
- If your output is `HLSv3` and has a segment duration set, or is not included in a playlist, Elastic Transcoder creates an output playlist file with a file extension of `.m3u8` , and a series of `.ts` files that include a five-digit sequential counter beginning with 00000: OutputKeyPrefix``Outputs:Key`` .m3u8 OutputKeyPrefix``Outputs:Key`` 00000.ts
- If your output is `HLSv4` , has a segment duration set, and is included in an `HLSv4` playlist, Elastic Transcoder creates an output playlist file with a file extension of `_v4.m3u8` . If the output is video, Elastic Transcoder also creates an output file with an extension of `_iframe.m3u8` : OutputKeyPrefix``Outputs:Key`` _v4.m3u8 OutputKeyPrefix``Outputs:Key`` _iframe.m3u8 OutputKeyPrefix``Outputs:Key`` .ts

Elastic Transcoder automatically appends the relevant file extension to the file name. If you include a file extension in Output Key, the file name will have two extensions.

If you include more than one output in a playlist, any segment duration settings, clip settings, or caption settings must be the same for all outputs in the playlist. For `Smooth` playlists, the `Audio:Profile` , `Video:Profile` , and `Video:FrameRate` to `Video:KeyframesMaxDist` ratio must be the same for all outputs.

(string)

HlsContentProtection -> (structure)

The HLS content protection settings, if any, that you want Elastic Transcoder to apply to the output files associated with this playlist.

Method -> (string)

The content protection method for your output. The only valid value is: `aes-128` .

This value is written into the method attribute of the `EXT-X-KEY` metadata tag in the output playlist.

Key -> (string)

If you want Elastic Transcoder to generate a key for you, leave this field blank.

If you choose to supply your own key, you must encrypt the key by using AWS KMS. The key must be base64-encoded, and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

KeyMd5 -> (string)

If Elastic Transcoder is generating your key for you, you must leave this field blank.

The MD5 digest of the key that you want Elastic Transcoder to use to encrypt your output file, and that you want Elastic Transcoder to use as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes before being base64- encoded.

InitializationVector -> (string)

If Elastic Transcoder is generating your key for you, you must leave this field blank.

The series of random bits created by a random bit generator, unique for every encryption operation, that you want Elastic Transcoder to use to encrypt your output files. The initialization vector must be base64-encoded, and it must be exactly 16 bytes before being base64-encoded.

LicenseAcquisitionUrl -> (string)

The location of the license key required to decrypt your HLS playlist. The URL must be an absolute path, and is referenced in the URI attribute of the EXT-X-KEY metadata tag in the playlist file.

KeyStoragePolicy -> (string)

Specify whether you want Elastic Transcoder to write your HLS license key to an Amazon S3 bucket. If you choose `WithVariantPlaylists` , `LicenseAcquisitionUrl` must be left blank and Elastic Transcoder writes your data key into the same bucket as the associated playlist.

PlayReadyDrm -> (structure)

The DRM settings, if any, that you want Elastic Transcoder to apply to the output files associated with this playlist.

Format -> (string)

The type of DRM, if any, that you want Elastic Transcoder to apply to the output files associated with this playlist.

Key -> (string)

The DRM key for your file, provided by your DRM license provider. The key must be base64-encoded, and it must be one of the following bit lengths before being base64-encoded:

`128` , `192` , or `256` .

The key must also be encrypted by using AWS KMS.

KeyMd5 -> (string)

The MD5 digest of the key used for DRM on your file, and that you want Elastic Transcoder to use as a checksum to make sure your key was not corrupted in transit. The key MD5 must be base64-encoded, and it must be exactly 16 bytes before being base64-encoded.

KeyId -> (string)

The ID for your DRM key, so that your DRM license provider knows which key to provide.

The key ID must be provided in big endian, and Elastic Transcoder converts it to little endian before inserting it into the PlayReady DRM headers. If you are unsure whether your license server provides your key ID in big or little endian, check with your DRM provider.

InitializationVector -> (string)

The series of random bits created by a random bit generator, unique for every encryption operation, that you want Elastic Transcoder to use to encrypt your files. The initialization vector must be base64-encoded, and it must be exactly 8 bytes long before being base64-encoded. If no initialization vector is provided, Elastic Transcoder generates one for you.

LicenseAcquisitionUrl -> (string)

The location of the license key required to play DRM content. The URL must be an absolute path, and is referenced by the PlayReady header. The PlayReady header is referenced in the protection header of the client manifest for Smooth Streaming outputs, and in the EXT-X-DXDRM and EXT-XDXDRMINFO metadata tags for HLS playlist outputs. An example URL looks like this: `https://www.example.com/exampleKey/`

Status -> (string)

The status of the job with which the playlist is associated.

StatusDetail -> (string)

Information that further explains the status.

Status -> (string)

The status of the job: `Submitted` , `Progressing` , `Complete` , `Canceled` , or `Error` .

UserMetadata -> (map)

User-defined metadata that you want to associate with an Elastic Transcoder job. You specify metadata in `key/value` pairs, and you can add up to 10 `key/value` pairs per job. Elastic Transcoder does not guarantee that `key/value` pairs are returned in the same order in which you specify them.

Metadata `keys` and `values` must use characters from the following list:

- `0-9`
- `A-Z` and `a-z`
- `Space`
- The following symbols: `_.:/=+-%@`

key -> (string)

value -> (string)

Timing -> (structure)

Details about the timing of a job.

SubmitTimeMillis -> (long)

The time the job was submitted to Elastic Transcoder, in epoch milliseconds.

StartTimeMillis -> (long)

The time the job began transcoding, in epoch milliseconds.

FinishTimeMillis -> (long)

The time the job finished transcoding, in epoch milliseconds.

NextPageToken -> (string)

A value that you use to access the second and subsequent pages of results, if any. When the jobs in the specified pipeline fit on one page or when youâve reached the last page of results, the value of `NextPageToken` is `null` .