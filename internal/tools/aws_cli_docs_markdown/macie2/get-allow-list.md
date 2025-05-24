# get-allow-listÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-allow-list.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/get-allow-list.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [macie2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/macie2/index.html#cli-aws-macie2) ]

# get-allow-list

## Description

Retrieves the settings and status of an allow list.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/macie2-2020-01-01/GetAllowList)

## Synopsis

```
get-allow-list
--id <value>
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

The unique identifier for the Amazon Macie resource that the request applies to.

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

arn -> (string)

The Amazon Resource Name (ARN) of the allow list.

createdAt -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when the allow list was created in Amazon Macie.

criteria -> (structure)

The criteria that specify the text or text pattern to ignore. The criteria can be the location and name of an S3 object that lists specific text to ignore (s3WordsList), or a regular expression (regex) that defines a text pattern to ignore.

regex -> (string)

The regular expression (*regex* ) that defines the text pattern to ignore. The expression can contain as many as 512 characters.

s3WordsList -> (structure)

The location and name of the S3 object that lists specific text to ignore.

bucketName -> (string)

The full name of the S3 bucket that contains the object.

objectKey -> (string)

The full name (key) of the object.

description -> (string)

The custom description of the allow list.

id -> (string)

The unique identifier for the allow list.

name -> (string)

The custom name of the allow list.

status -> (structure)

The current status of the allow list, which indicates whether Amazon Macie can access and use the listâs criteria.

code -> (string)

The current status of the allow list. If the listâs criteria specify a regular expression (regex), this value is typically OK. Amazon Macie can compile the expression.

If the listâs criteria specify an S3 object, possible values are:

- OK - Macie can retrieve and parse the contents of the object.
- S3_OBJECT_ACCESS_DENIED - Macie isnât allowed to access the object or the object is encrypted with a customer managed KMS key that Macie isnât allowed to use. Check the bucket policy and other permissions settings for the bucket and the object. If the object is encrypted, also ensure that itâs encrypted with a key that Macie is allowed to use.
- S3_OBJECT_EMPTY - Macie can retrieve the object but the object doesnât contain any content. Ensure that the object contains the correct entries. Also ensure that the listâs criteria specify the correct bucket and object names.
- S3_OBJECT_NOT_FOUND - The object doesnât exist in Amazon S3. Ensure that the listâs criteria specify the correct bucket and object names.
- S3_OBJECT_OVERSIZE - Macie can retrieve the object. However, the object contains too many entries or its storage size exceeds the quota for an allow list. Try breaking the list into multiple files and ensure that each file doesnât exceed any quotas. Then configure list settings in Macie for each file.
- S3_THROTTLED - Amazon S3 throttled the request to retrieve the object. Wait a few minutes and then try again.
- S3_USER_ACCESS_DENIED - Amazon S3 denied the request to retrieve the object. If the specified object exists, youâre not allowed to access it or itâs encrypted with an KMS key that youâre not allowed to use. Work with your Amazon Web Services administrator to ensure that the listâs criteria specify the correct bucket and object names, and you have read access to the bucket and the object. If the object is encrypted, also ensure that itâs encrypted with a key that youâre allowed to use.
- UNKNOWN_ERROR - A transient or internal error occurred when Macie attempted to retrieve or parse the object. Wait a few minutes and then try again. A list can also have this status if itâs encrypted with a key that Amazon S3 and Macie canât access or use.

description -> (string)

A brief description of the status of the allow list. Amazon Macie uses this value to provide additional information about an error that occurred when Macie tried to access and use the listâs criteria.

tags -> (map)

A map of key-value pairs that specifies which tags (keys and values) are associated with the allow list.

key -> (string)

value -> (string)

updatedAt -> (timestamp)

The date and time, in UTC and extended ISO 8601 format, when the allow listâs settings were most recently changed in Amazon Macie.