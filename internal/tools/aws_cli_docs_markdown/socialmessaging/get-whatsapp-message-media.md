# get-whatsapp-message-mediaÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/socialmessaging/get-whatsapp-message-media.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/socialmessaging/get-whatsapp-message-media.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [socialmessaging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/socialmessaging/index.html#cli-aws-socialmessaging) ]

# get-whatsapp-message-media

## Description

Get a media file from the WhatsApp service. On successful completion the media file is retrieved from Meta and stored in the specified Amazon S3 bucket. Use either `destinationS3File` or `destinationS3PresignedUrl` for the destination. If both are used then an `InvalidParameterException` is returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/socialmessaging-2024-01-01/GetWhatsAppMessageMedia)

## Synopsis

```
get-whatsapp-message-media
--media-id <value>
--origination-phone-number-id <value>
[--metadata-only | --no-metadata-only]
[--destination-s3-presigned-url <value>]
[--destination-s3-file <value>]
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

`--media-id` (string)

The unique identifier for the media file.

`--origination-phone-number-id` (string)

The unique identifier of the originating phone number for the WhatsApp message media. The phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901` . Use [GetLinkedWhatsAppBusinessAccount](https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetLinkedWhatsAppBusinessAccountPhoneNumber.html) to find a phone numberâs id.

`--metadata-only` | `--no-metadata-only` (boolean)

Set to `True` to get only the metadata for the file.

`--destination-s3-presigned-url` (structure)

The presign url of the media file.

url -> (string)

The presign url to the object.

headers -> (map)

A map of headers and their values. You must specify the `Content-Type` header when using `PostWhatsAppMessageMedia` . For a list of common headers, see [Common Request Headers](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonRequestHeaders.html) in the *Amazon S3 API Reference*

key -> (string)

value -> (string)

Shorthand Syntax:

```
url=string,headers={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "url": "string",
  "headers": {"string": "string"
    ...}
}
```

`--destination-s3-file` (structure)

The `bucketName` and `key` of the S3 media file.

bucketName -> (string)

The bucket name.

key -> (string)

The object key of the media file.

Shorthand Syntax:

```
bucketName=string,key=string
```

JSON Syntax:

```
{
  "bucketName": "string",
  "key": "string"
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

mimeType -> (string)

The MIME type of the media.

fileSize -> (long)

The file size of the media, in KB.