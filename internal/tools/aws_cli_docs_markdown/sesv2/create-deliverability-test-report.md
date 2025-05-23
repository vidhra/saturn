# create-deliverability-test-reportÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-deliverability-test-report.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/create-deliverability-test-report.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sesv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sesv2/index.html#cli-aws-sesv2) ]

# create-deliverability-test-report

## Description

Create a new predictive inbox placement test. Predictive inbox placement tests can help you predict how your messages will be handled by various email providers around the world. When you perform a predictive inbox placement test, you provide a sample message that contains the content that you plan to send to your customers. Amazon SES then sends that message to special email addresses spread across several major email providers. After about 24 hours, the test is complete, and you can use the `GetDeliverabilityTestReport` operation to view the results of the test.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sesv2-2019-09-27/CreateDeliverabilityTestReport)

## Synopsis

```
create-deliverability-test-report
[--report-name <value>]
--from-email-address <value>
--content <value>
[--tags <value>]
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

`--report-name` (string)

A unique name that helps you to identify the predictive inbox placement test when you retrieve the results.

`--from-email-address` (string)

The email address that the predictive inbox placement test email was sent from.

`--content` (structure)

The HTML body of the message that you sent when you performed the predictive inbox placement test.

Simple -> (structure)

The simple email message. The message consists of a subject, message body and attachments list.

Subject -> (structure)

The subject line of the email. The subject line can only contain 7-bit ASCII characters. However, you can specify non-ASCII characters in the subject line by using encoded-word syntax, as described in [RFC 2047](https://tools.ietf.org/html/rfc2047) .

Data -> (string)

The content of the message itself.

Charset -> (string)

The character set for the content. Because of the constraints of the SMTP protocol, Amazon SES uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify `UTF-8` , `ISO-8859-1` , or `Shift_JIS` .

Body -> (structure)

The body of the message. You can specify an HTML version of the message, a text-only version of the message, or both.

Text -> (structure)

An object that represents the version of the message that is displayed in email clients that donât support HTML, or clients where the recipient has disabled HTML rendering.

Data -> (string)

The content of the message itself.

Charset -> (string)

The character set for the content. Because of the constraints of the SMTP protocol, Amazon SES uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify `UTF-8` , `ISO-8859-1` , or `Shift_JIS` .

Html -> (structure)

An object that represents the version of the message that is displayed in email clients that support HTML. HTML messages can include formatted text, hyperlinks, images, and more.

Data -> (string)

The content of the message itself.

Charset -> (string)

The character set for the content. Because of the constraints of the SMTP protocol, Amazon SES uses 7-bit ASCII by default. If the text includes characters outside of the ASCII range, you have to specify a character set. For example, you could specify `UTF-8` , `ISO-8859-1` , or `Shift_JIS` .

Headers -> (list)

The list of message headers that will be added to the email message.

(structure)

Contains the name and value of a message header that you add to an email.

Name -> (string)

The name of the message header. The message header name has to meet the following criteria:

- Can contain any printable ASCII character (33 - 126) except for colon (:).
- Can contain no more than 126 characters.

Value -> (string)

The value of the message header. The message header value has to meet the following criteria:

- Can contain any printable ASCII character.
- Can contain no more than 870 characters.

Attachments -> (list)

The List of attachments to include in your email. All recipients will receive the same attachments.

(structure)

Contains metadata and attachment raw content.

RawContent -> (blob)

The raw data of the attachment. It needs to be base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an Amazon Web Services SDK, the SDK takes care of the base 64-encoding for you.

ContentDisposition -> (string)

A standard descriptor indicating how the attachment should be rendered in the email. Supported values: `ATTACHMENT` or `INLINE` .

FileName -> (string)

The file name for the attachment as it will appear in the email. Amazon SES restricts certain file extensions. To ensure attachments are accepted, check the [Unsupported attachment types](https://docs.aws.amazon.com/ses/latest/dg/mime-types.html) in the Amazon SES Developer Guide.

ContentDescription -> (string)

A brief description of the attachment content.

ContentId -> (string)

Unique identifier for the attachment, used for referencing attachments with INLINE disposition in HTML content.

ContentTransferEncoding -> (string)

Specifies how the attachment is encoded. Supported values: `BASE64` , `QUOTED_PRINTABLE` , `SEVEN_BIT` .

ContentType -> (string)

The MIME type of the attachment.

### Note

Example: `application/pdf` , `image/jpeg`

Raw -> (structure)

The raw email message. The message has to meet the following criteria:

- The message has to contain a header and a body, separated by one blank line.
- All of the required header fields must be present in the message.
- Each part of a multipart MIME message must be formatted properly.
- If you include attachments, they must be in a file format that the Amazon SES API v2 supports.
- The raw data of the message needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an Amazon Web Services SDK, the SDK takes care of the base 64-encoding for you.
- If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipientsâ email clients render the message properly.
- The length of any single line of text in the message canât exceed 1,000 characters. This restriction is defined in [RFC 5321](https://tools.ietf.org/html/rfc5321) .

Data -> (blob)

The raw email message. The message has to meet the following criteria:

- The message has to contain a header and a body, separated by one blank line.
- All of the required header fields must be present in the message.
- Each part of a multipart MIME message must be formatted properly.
- Attachments must be in a file format that the Amazon SES supports.
- The raw data of the message needs to base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an Amazon Web Services SDK, the SDK takes care of the base 64-encoding for you.
- If any of the MIME parts in your message contain content that is outside of the 7-bit ASCII character range, you should encode that content to ensure that recipientsâ email clients render the message properly.
- The length of any single line of text in the message canât exceed 1,000 characters. This restriction is defined in [RFC 5321](https://tools.ietf.org/html/rfc5321) .

Template -> (structure)

The template to use for the email message.

TemplateName -> (string)

The name of the template. You will refer to this name when you send email using the `SendTemplatedEmail` or `SendBulkTemplatedEmail` operations.

TemplateArn -> (string)

The Amazon Resource Name (ARN) of the template.

TemplateContent -> (structure)

The content of the template.

### Note

Amazon SES supports only simple substitions when you send email using the `SendEmail` or `SendBulkEmail` operations and you provide the full template content in the request.

Subject -> (string)

The subject line of the email.

Text -> (string)

The email body that will be visible to recipients whose email clients do not display HTML.

Html -> (string)

The HTML body of the email.

TemplateData -> (string)

An object that defines the values to use for message variables in the template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the value to use for that variable.

Headers -> (list)

The list of message headers that will be added to the email message.

(structure)

Contains the name and value of a message header that you add to an email.

Name -> (string)

The name of the message header. The message header name has to meet the following criteria:

- Can contain any printable ASCII character (33 - 126) except for colon (:).
- Can contain no more than 126 characters.

Value -> (string)

The value of the message header. The message header value has to meet the following criteria:

- Can contain any printable ASCII character.
- Can contain no more than 870 characters.

Attachments -> (list)

The List of attachments to include in your email. All recipients will receive the same attachments.

(structure)

Contains metadata and attachment raw content.

RawContent -> (blob)

The raw data of the attachment. It needs to be base64-encoded if you are accessing Amazon SES directly through the HTTPS interface. If you are accessing Amazon SES using an Amazon Web Services SDK, the SDK takes care of the base 64-encoding for you.

ContentDisposition -> (string)

A standard descriptor indicating how the attachment should be rendered in the email. Supported values: `ATTACHMENT` or `INLINE` .

FileName -> (string)

The file name for the attachment as it will appear in the email. Amazon SES restricts certain file extensions. To ensure attachments are accepted, check the [Unsupported attachment types](https://docs.aws.amazon.com/ses/latest/dg/mime-types.html) in the Amazon SES Developer Guide.

ContentDescription -> (string)

A brief description of the attachment content.

ContentId -> (string)

Unique identifier for the attachment, used for referencing attachments with INLINE disposition in HTML content.

ContentTransferEncoding -> (string)

Specifies how the attachment is encoded. Supported values: `BASE64` , `QUOTED_PRINTABLE` , `SEVEN_BIT` .

ContentType -> (string)

The MIME type of the attachment.

### Note

Example: `application/pdf` , `image/jpeg`

JSON Syntax:

```
{
  "Simple": {
    "Subject": {
      "Data": "string",
      "Charset": "string"
    },
    "Body": {
      "Text": {
        "Data": "string",
        "Charset": "string"
      },
      "Html": {
        "Data": "string",
        "Charset": "string"
      }
    },
    "Headers": [
      {
        "Name": "string",
        "Value": "string"
      }
      ...
    ],
    "Attachments": [
      {
        "RawContent": blob,
        "ContentDisposition": "ATTACHMENT"|"INLINE",
        "FileName": "string",
        "ContentDescription": "string",
        "ContentId": "string",
        "ContentTransferEncoding": "BASE64"|"QUOTED_PRINTABLE"|"SEVEN_BIT",
        "ContentType": "string"
      }
      ...
    ]
  },
  "Raw": {
    "Data": blob
  },
  "Template": {
    "TemplateName": "string",
    "TemplateArn": "string",
    "TemplateContent": {
      "Subject": "string",
      "Text": "string",
      "Html": "string"
    },
    "TemplateData": "string",
    "Headers": [
      {
        "Name": "string",
        "Value": "string"
      }
      ...
    ],
    "Attachments": [
      {
        "RawContent": blob,
        "ContentDisposition": "ATTACHMENT"|"INLINE",
        "FileName": "string",
        "ContentDescription": "string",
        "ContentId": "string",
        "ContentTransferEncoding": "BASE64"|"QUOTED_PRINTABLE"|"SEVEN_BIT",
        "ContentType": "string"
      }
      ...
    ]
  }
}
```

`--tags` (list)

An array of objects that define the tags (keys and values) that you want to associate with the predictive inbox placement test.

(structure)

An object that defines the tags that are associated with a resource. A *tag* is a label that you optionally define and associate with a resource. Tags can help you categorize and manage resources in different ways, such as by purpose, owner, environment, or other criteria. A resource can have as many as 50 tags.

Each tag consists of a required *tag key* and an associated *tag value* , both of which you define. A tag key is a general label that acts as a category for a more specific tag value. A tag value acts as a descriptor within a tag key. A tag key can contain as many as 128 characters. A tag value can contain as many as 256 characters. The characters can be Unicode letters, digits, white space, or one of the following symbols: _ . : / = + -. The following additional restrictions apply to tags:

- Tag keys and values are case sensitive.
- For each associated resource, each tag key must be unique and it can have only one value.
- The `aws:` prefix is reserved for use by Amazon Web Services; you canât use it in any tag keys or values that you define. In addition, you canât edit or remove tag keys or values that use this prefix. Tags that use this prefix donât count against the limit of 50 tags per resource.
- You can associate tags with public or shared resources, but the tags are available only for your Amazon Web Services account, not any other accounts that share the resource. In addition, the tags are available only for resources that are located in the specified Amazon Web Services Region for your Amazon Web Services account.

Key -> (string)

One part of a key-value pair that defines a tag. The maximum length of a tag key is 128 characters. The minimum length is 1 character.

Value -> (string)

The optional part of a key-value pair that defines a tag. The maximum length of a tag value is 256 characters. The minimum length is 0 characters. If you donât want a resource to have a specific tag value, donât specify a value for this parameter. If you donât specify a value, Amazon SES sets the value to an empty string.

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

ReportId -> (string)

A unique string that identifies the predictive inbox placement test.

DeliverabilityTestStatus -> (string)

The status of the predictive inbox placement test. If the status is `IN_PROGRESS` , then the predictive inbox placement test is currently running. Predictive inbox placement tests are usually complete within 24 hours of creating the test. If the status is `COMPLETE` , then the test is finished, and you can use the `GetDeliverabilityTestReport` to view the results of the test.