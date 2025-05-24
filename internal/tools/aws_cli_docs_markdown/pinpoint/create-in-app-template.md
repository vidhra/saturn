# create-in-app-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-in-app-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-in-app-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# create-in-app-template

## Description

Creates a new message template for messages using the in-app message channel.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/CreateInAppTemplate)

## Synopsis

```
create-in-app-template
--in-app-template-request <value>
--template-name <value>
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

`--in-app-template-request` (structure)

InApp Template Request.

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

CustomConfig -> (map)

Custom config to be sent to client.

key -> (string)

value -> (string)

Layout -> (string)

The layout of the message.

tags -> (map)

### Note

As of **22-05-2023** tags has been deprecated for update operations. After this date any value in tags is not processed and an error code is not returned. To manage tags we recommend using either [Tags](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html) in the *API Reference for Amazon Pinpoint* , [resourcegroupstaggingapi](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html) commands in the *AWS Command Line Interface Documentation* or [resourcegroupstaggingapi](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroupstaggingapi/package-summary.html) in the *AWS SDK* .

(Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value.

key -> (string)

value -> (string)

TemplateDescription -> (string)

The description of the template.

JSON Syntax:

```
{
  "Content": [
    {
      "BackgroundColor": "string",
      "BodyConfig": {
        "Alignment": "LEFT"|"CENTER"|"RIGHT",
        "Body": "string",
        "TextColor": "string"
      },
      "HeaderConfig": {
        "Alignment": "LEFT"|"CENTER"|"RIGHT",
        "Header": "string",
        "TextColor": "string"
      },
      "ImageUrl": "string",
      "PrimaryBtn": {
        "Android": {
          "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
          "Link": "string"
        },
        "DefaultConfig": {
          "BackgroundColor": "string",
          "BorderRadius": integer,
          "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
          "Link": "string",
          "Text": "string",
          "TextColor": "string"
        },
        "IOS": {
          "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
          "Link": "string"
        },
        "Web": {
          "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
          "Link": "string"
        }
      },
      "SecondaryBtn": {
        "Android": {
          "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
          "Link": "string"
        },
        "DefaultConfig": {
          "BackgroundColor": "string",
          "BorderRadius": integer,
          "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
          "Link": "string",
          "Text": "string",
          "TextColor": "string"
        },
        "IOS": {
          "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
          "Link": "string"
        },
        "Web": {
          "ButtonAction": "LINK"|"DEEP_LINK"|"CLOSE",
          "Link": "string"
        }
      }
    }
    ...
  ],
  "CustomConfig": {"string": "string"
    ...},
  "Layout": "BOTTOM_BANNER"|"TOP_BANNER"|"OVERLAYS"|"MOBILE_FEED"|"MIDDLE_BANNER"|"CAROUSEL",
  "tags": {"string": "string"
    ...},
  "TemplateDescription": "string"
}
```

`--template-name` (string)

The name of the message template. A template name must start with an alphanumeric character and can contain a maximum of 128 characters. The characters can be alphanumeric characters, underscores (_), or hyphens (-). Template names are case sensitive.

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

TemplateCreateMessageBody -> (structure)

Provides information about a request to create a message template.

Arn -> (string)

The Amazon Resource Name (ARN) of the message template that was created.

Message -> (string)

The message thatâs returned from the API for the request to create the message template.

RequestID -> (string)

The unique identifier for the request to create the message template.