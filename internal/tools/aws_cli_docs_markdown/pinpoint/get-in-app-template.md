# get-in-app-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-in-app-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/get-in-app-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# get-in-app-template

## Description

Retrieves the content and settings of a message template for messages sent through the in-app channel.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/GetInAppTemplate)

## Synopsis

```
get-in-app-template
--template-name <value>
[--template-version <value>]
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

`--template-name` (string)

The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.

`--template-version` (string)

The unique identifier for the version of the message template to update, retrieve information about, or delete. To retrieve identifiers and other information for all the versions of a template, use the Template Versionsresource.

If specified, this value must match the identifier for an existing template version. If specified for an update operation, this value must match the identifier for the latest existing version of the template. This restriction helps ensure that race conditions donât occur.

If you donât specify a value for this parameter, Amazon Pinpoint does the following:

- For a get operation, retrieves information about the active version of the template.
- For an update operation, saves the updates to (overwrites) the latest existing version of the template, if the create-new-version parameter isnât used or is set to false.
- For a delete operation, deletes the template, including all versions of the template.

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

InAppTemplateResponse -> (structure)

In-App Template Response.

Arn -> (string)

The resource arn of the template.

Content -> (list)

The content of the message, can include up to 5 modals. Each modal must contain a message, a header, and background color. ImageUrl and buttons are optional.

(structure)

The configuration for the message content.

BackgroundColor -> (string)

The background color for the message.

BodyConfig -> (structure)

The configuration for the message body.

Alignment -> (string)

The alignment of the text. Valid values: LEFT, CENTER, RIGHT.

Body -> (string)

Message Body.

TextColor -> (string)

The text color.

HeaderConfig -> (structure)

The configuration for the message header.

Alignment -> (string)

The alignment of the text. Valid values: LEFT, CENTER, RIGHT.

Header -> (string)

Message Header.

TextColor -> (string)

The text color.

ImageUrl -> (string)

The image url for the background of message.

PrimaryBtn -> (structure)

The first button inside the message.

Android -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

DefaultConfig -> (structure)

Default button content.

BackgroundColor -> (string)

The background color of the button.

BorderRadius -> (integer)

The border radius of the button.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

Text -> (string)

Button text.

TextColor -> (string)

The text color of the button.

IOS -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

Web -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

SecondaryBtn -> (structure)

The second button inside message.

Android -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

DefaultConfig -> (structure)

Default button content.

BackgroundColor -> (string)

The background color of the button.

BorderRadius -> (integer)

The border radius of the button.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

Text -> (string)

Button text.

TextColor -> (string)

The text color of the button.

IOS -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

Web -> (structure)

Default button content.

ButtonAction -> (string)

Action triggered by the button.

Link -> (string)

Button destination.

CreationDate -> (string)

The creation date of the template.

CustomConfig -> (map)

Custom config to be sent to client.

key -> (string)

value -> (string)

LastModifiedDate -> (string)

The last modified date of the template.

Layout -> (string)

The layout of the message.

tags -> (map)

A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value.

key -> (string)

value -> (string)

TemplateDescription -> (string)

The description of the template.

TemplateName -> (string)

The name of the template.

TemplateType -> (string)

The type of the template.

Version -> (string)

The version id of the template.