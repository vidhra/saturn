# create-faqÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-faq.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/create-faq.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [kendra](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kendra/index.html#cli-aws-kendra) ]

# create-faq

## Description

Creates a set of frequently ask questions (FAQs) using a specified FAQ file stored in an Amazon S3 bucket.

Adding FAQs to an index is an asynchronous operation.

For an example of adding an FAQ to an index using Python and Java SDKs, see [Using your FAQ file](https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html#using-faq-file) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/kendra-2019-02-03/CreateFaq)

## Synopsis

```
create-faq
--index-id <value>
--name <value>
[--description <value>]
--s3-path <value>
--role-arn <value>
[--tags <value>]
[--file-format <value>]
[--client-token <value>]
[--language-code <value>]
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

`--index-id` (string)

The identifier of the index for the FAQ.

`--name` (string)

A name for the FAQ.

`--description` (string)

A description for the FAQ.

`--s3-path` (structure)

The path to the FAQ file in S3.

Bucket -> (string)

The name of the S3 bucket that contains the file.

Key -> (string)

The name of the file.

Shorthand Syntax:

```
Bucket=string,Key=string
```

JSON Syntax:

```
{
  "Bucket": "string",
  "Key": "string"
}
```

`--role-arn` (string)

The Amazon Resource Name (ARN) of an IAM role with permission to access the S3 bucket that contains the FAQ file. For more information, see [IAM access roles for Amazon Kendra](https://docs.aws.amazon.com/kendra/latest/dg/iam-roles.html) .

`--tags` (list)

A list of key-value pairs that identify the FAQ. You can use the tags to identify and organize your resources and to control access to resources.

(structure)

A key-value pair that identifies or categorizes an index, FAQ, data source, or other resource. TA tag key and value can consist of Unicode letters, digits, white space, and any of the following symbols: _ . : / = + - @.

Key -> (string)

The key for the tag. Keys are not case sensitive and must be unique for the index, FAQ, data source, or other resource.

Value -> (string)

The value associated with the tag. The value may be an empty string but it canât be null.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--file-format` (string)

The format of the FAQ input file. You can choose between a basic CSV format, a CSV format that includes customs attributes in a header, and a JSON format that includes custom attributes.

The default format is CSV.

The format must match the format of the file stored in the S3 bucket identified in the `S3Path` parameter.

For more information, see [Adding questions and answers](https://docs.aws.amazon.com/kendra/latest/dg/in-creating-faq.html) .

Possible values:

- `CSV`
- `CSV_WITH_HEADER`
- `JSON`

`--client-token` (string)

A token that you provide to identify the request to create a FAQ. Multiple calls to the `CreateFaqRequest` API with the same client token will create only one FAQ.

`--language-code` (string)

The code for a language. This allows you to support a language for the FAQ document. English is supported by default. For more information on supported languages, including their codes, see [Adding documents in languages other than English](https://docs.aws.amazon.com/kendra/latest/dg/in-adding-languages.html) .

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

Id -> (string)

The identifier of the FAQ.