# create-push-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-push-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/create-push-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# create-push-template

## Description

Creates a message template for messages that are sent through a push notification channel.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/CreatePushTemplate)

## Synopsis

```
create-push-template
--push-notification-template-request <value>
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

`--push-notification-template-request` (structure)

Specifies the content and settings for a message template that can be used in messages that are sent through a push notification channel.

ADM -> (structure)

The message template to use for the ADM (Amazon Device Messaging) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).

Action -> (string)

The action to occur if a recipient taps a push notification thatâs based on the message template. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The message body to use in a push notification thatâs based on the message template.

ImageIconUrl -> (string)

The URL of the large icon image to display in the content view of a push notification thatâs based on the message template.

ImageUrl -> (string)

The URL of an image to display in a push notification thatâs based on the message template.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for a push notification thatâs based on the message template. If specified, this value overrides all other content for the message template.

SmallImageIconUrl -> (string)

The URL of the small icon image to display in the status bar and the content view of a push notification thatâs based on the message template.

Sound -> (string)

The sound to play when a recipient receives a push notification thatâs based on the message template. You can use the default stream or specify the file name of a sound resource thatâs bundled in your app. On an Android platform, the sound file must reside in /res/raw/.

Title -> (string)

The title to use in a push notification thatâs based on the message template. This title appears above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps a push notification thatâs based on the message template and the value of the Action property is URL.

APNS -> (structure)

The message template to use for the APNs (Apple Push Notification service) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).

Action -> (string)

The action to occur if a recipient taps a push notification thatâs based on the message template. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS platform.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The message body to use in push notifications that are based on the message template.

MediaUrl -> (string)

The URL of an image or video to display in push notifications that are based on the message template.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for push notifications that are based on the message template. If specified, this value overrides all other content for the message template.

Sound -> (string)

The key for the sound to play when the recipient receives a push notification thatâs based on the message template. The value for this key is the name of a sound file in your appâs main bundle or the Library/Sounds folder in your appâs data container. If the sound file canât be found or you specify default for the value, the system plays the default alert sound.

Title -> (string)

The title to use in push notifications that are based on the message template. This title appears above the notification message on a recipientâs device.

Url -> (string)

The URL to open in the recipientâs default mobile browser, if a recipient taps a push notification thatâs based on the message template and the value of the Action property is URL.

Baidu -> (structure)

The message template to use for the Baidu (Baidu Cloud Push) channel. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).

Action -> (string)

The action to occur if a recipient taps a push notification thatâs based on the message template. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The message body to use in a push notification thatâs based on the message template.

ImageIconUrl -> (string)

The URL of the large icon image to display in the content view of a push notification thatâs based on the message template.

ImageUrl -> (string)

The URL of an image to display in a push notification thatâs based on the message template.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for a push notification thatâs based on the message template. If specified, this value overrides all other content for the message template.

SmallImageIconUrl -> (string)

The URL of the small icon image to display in the status bar and the content view of a push notification thatâs based on the message template.

Sound -> (string)

The sound to play when a recipient receives a push notification thatâs based on the message template. You can use the default stream or specify the file name of a sound resource thatâs bundled in your app. On an Android platform, the sound file must reside in /res/raw/.

Title -> (string)

The title to use in a push notification thatâs based on the message template. This title appears above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps a push notification thatâs based on the message template and the value of the Action property is URL.

Default -> (structure)

The default message template to use for push notification channels.

Action -> (string)

The action to occur if a recipient taps a push notification thatâs based on the message template. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This setting uses the deep-linking features of the iOS and Android platforms.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The message body to use in push notifications that are based on the message template.

Sound -> (string)

The sound to play when a recipient receives a push notification thatâs based on the message template. You can use the default stream or specify the file name of a sound resource thatâs bundled in your app. On an Android platform, the sound file must reside in /res/raw/.

For an iOS platform, this value is the key for the name of a sound file in your appâs main bundle or the Library/Sounds folder in your appâs data container. If the sound file canât be found or you specify default for the value, the system plays the default alert sound.

Title -> (string)

The title to use in push notifications that are based on the message template. This title appears above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps a push notification thatâs based on the message template and the value of the Action property is URL.

DefaultSubstitutions -> (string)

A JSON object that specifies the default values to use for message variables in the message template. This object is a set of key-value pairs. Each key defines a message variable in the template. The corresponding value defines the default value for that variable. When you create a message thatâs based on the template, you can override these defaults with message-specific and address-specific variables and values.

GCM -> (structure)

The message template to use for the GCM channel, which is used to send notifications through the Firebase Cloud Messaging (FCM), formerly Google Cloud Messaging (GCM), service. This message template overrides the default template for push notification channels (DefaultPushNotificationTemplate).

Action -> (string)

The action to occur if a recipient taps a push notification thatâs based on the message template. Valid values are:

- OPEN_APP - Your app opens or it becomes the foreground app if it was sent to the background. This is the default action.
- DEEP_LINK - Your app opens and displays a designated user interface in the app. This action uses the deep-linking features of the Android platform.
- URL - The default mobile browser on the recipientâs device opens and loads the web page at a URL that you specify.

Body -> (string)

The message body to use in a push notification thatâs based on the message template.

ImageIconUrl -> (string)

The URL of the large icon image to display in the content view of a push notification thatâs based on the message template.

ImageUrl -> (string)

The URL of an image to display in a push notification thatâs based on the message template.

RawContent -> (string)

The raw, JSON-formatted string to use as the payload for a push notification thatâs based on the message template. If specified, this value overrides all other content for the message template.

SmallImageIconUrl -> (string)

The URL of the small icon image to display in the status bar and the content view of a push notification thatâs based on the message template.

Sound -> (string)

The sound to play when a recipient receives a push notification thatâs based on the message template. You can use the default stream or specify the file name of a sound resource thatâs bundled in your app. On an Android platform, the sound file must reside in /res/raw/.

Title -> (string)

The title to use in a push notification thatâs based on the message template. This title appears above the notification message on a recipientâs device.

Url -> (string)

The URL to open in a recipientâs default mobile browser, if a recipient taps a push notification thatâs based on the message template and the value of the Action property is URL.

RecommenderId -> (string)

The unique identifier for the recommender model to use for the message template. Amazon Pinpoint uses this value to determine how to retrieve and process data from a recommender model when it sends messages that use the template, if the template contains message variables for recommendation data.

tags -> (map)

### Note

As of **22-05-2023** tags has been deprecated for update operations. After this date any value in tags is not processed and an error code is not returned. To manage tags we recommend using either [Tags](https://docs.aws.amazon.com/pinpoint/latest/apireference/tags-resource-arn.html) in the *API Reference for Amazon Pinpoint* , [resourcegroupstaggingapi](https://docs.aws.amazon.com/cli/latest/reference/resourcegroupstaggingapi/index.html) commands in the *AWS Command Line Interface Documentation* or [resourcegroupstaggingapi](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/resourcegroupstaggingapi/package-summary.html) in the *AWS SDK* .

(Deprecated) A string-to-string map of key-value pairs that defines the tags to associate with the message template. Each tag consists of a required tag key and an associated tag value.

key -> (string)

value -> (string)

TemplateDescription -> (string)

A custom description of the message template.

Shorthand Syntax:

```
ADM={Action=string,Body=string,ImageIconUrl=string,ImageUrl=string,RawContent=string,SmallImageIconUrl=string,Sound=string,Title=string,Url=string},APNS={Action=string,Body=string,MediaUrl=string,RawContent=string,Sound=string,Title=string,Url=string},Baidu={Action=string,Body=string,ImageIconUrl=string,ImageUrl=string,RawContent=string,SmallImageIconUrl=string,Sound=string,Title=string,Url=string},Default={Action=string,Body=string,Sound=string,Title=string,Url=string},DefaultSubstitutions=string,GCM={Action=string,Body=string,ImageIconUrl=string,ImageUrl=string,RawContent=string,SmallImageIconUrl=string,Sound=string,Title=string,Url=string},RecommenderId=string,tags={KeyName1=string,KeyName2=string},TemplateDescription=string
```

JSON Syntax:

```
{
  "ADM": {
    "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
    "Body": "string",
    "ImageIconUrl": "string",
    "ImageUrl": "string",
    "RawContent": "string",
    "SmallImageIconUrl": "string",
    "Sound": "string",
    "Title": "string",
    "Url": "string"
  },
  "APNS": {
    "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
    "Body": "string",
    "MediaUrl": "string",
    "RawContent": "string",
    "Sound": "string",
    "Title": "string",
    "Url": "string"
  },
  "Baidu": {
    "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
    "Body": "string",
    "ImageIconUrl": "string",
    "ImageUrl": "string",
    "RawContent": "string",
    "SmallImageIconUrl": "string",
    "Sound": "string",
    "Title": "string",
    "Url": "string"
  },
  "Default": {
    "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
    "Body": "string",
    "Sound": "string",
    "Title": "string",
    "Url": "string"
  },
  "DefaultSubstitutions": "string",
  "GCM": {
    "Action": "OPEN_APP"|"DEEP_LINK"|"URL",
    "Body": "string",
    "ImageIconUrl": "string",
    "ImageUrl": "string",
    "RawContent": "string",
    "SmallImageIconUrl": "string",
    "Sound": "string",
    "Title": "string",
    "Url": "string"
  },
  "RecommenderId": "string",
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

CreateTemplateMessageBody -> (structure)

Provides information about a request to create a message template.

Arn -> (string)

The Amazon Resource Name (ARN) of the message template that was created.

Message -> (string)

The message thatâs returned from the API for the request to create the message template.

RequestID -> (string)

The unique identifier for the request to create the message template.