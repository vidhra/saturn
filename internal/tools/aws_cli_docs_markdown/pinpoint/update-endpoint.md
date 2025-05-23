# update-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/update-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# update-endpoint

## Description

Creates a new endpoint for an application or updates the settings and attributes of an existing endpoint for an application. You can also use this operation to define custom attributes for an endpoint. If an update includes one or more values for a custom attribute, Amazon Pinpoint replaces (overwrites) any existing values with the new values.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/UpdateEndpoint)

## Synopsis

```
update-endpoint
--application-id <value>
--endpoint-id <value>
--endpoint-request <value>
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

`--application-id` (string)

The unique identifier for the application. This identifier is displayed as the **Project ID** on the Amazon Pinpoint console.

`--endpoint-id` (string)

The case insensitive unique identifier for the endpoint. The identifier canât contain `$` , `{` or `}` .

`--endpoint-request` (structure)

Specifies the channel type and other settings for an endpoint.

Address -> (string)

The destination address for messages or push notifications that you send to the endpoint. The address varies by channel. For a push-notification channel, use the token provided by the push notification service, such as an Apple Push Notification service (APNs) device token or a Firebase Cloud Messaging (FCM) registration token. For the SMS channel, use a phone number in E.164 format, such as +12065550100. For the email channel, use an email address.

Attributes -> (map)

One or more custom attributes that describe the endpoint by associating a name with an array of values. For example, the value of a custom attribute named Interests might be: [âScienceâ, âMusicâ, âTravelâ]. You can use these attributes as filter criteria when you create segments. Attribute names are case sensitive.

An attribute name can contain up to 50 characters. An attribute value can contain up to 100 characters. When you define the name of a custom attribute, avoid using the following characters: number sign (#), colon (:), question mark (?), backslash (), and slash (/). The Amazon Pinpoint console canât display attribute names that contain these characters. This restriction doesnât apply to attribute values.

key -> (string)

value -> (list)

(string)

ChannelType -> (string)

The channel to use when sending messages or push notifications to the endpoint.

Demographic -> (structure)

The demographic information for the endpoint, such as the time zone and platform.

AppVersion -> (string)

The version of the app thatâs associated with the endpoint.

Locale -> (string)

The locale of the endpoint, in the following format: the ISO 639-1 alpha-2 code, followed by an underscore (_), followed by an ISO 3166-1 alpha-2 value.

Make -> (string)

The manufacturer of the endpoint device, such as apple or samsung.

Model -> (string)

The model name or number of the endpoint device, such as iPhone or SM-G900F.

ModelVersion -> (string)

The model version of the endpoint device.

Platform -> (string)

The platform of the endpoint device, such as ios.

PlatformVersion -> (string)

The platform version of the endpoint device.

Timezone -> (string)

The time zone of the endpoint, specified as a tz database name value, such as America/Los_Angeles.

EffectiveDate -> (string)

The date and time, in ISO 8601 format, when the endpoint is updated.

EndpointStatus -> (string)

Specifies whether to send messages or push notifications to the endpoint. Valid values are: ACTIVE, messages are sent to the endpoint; and, INACTIVE, messages arenât sent to the endpoint.

Amazon Pinpoint automatically sets this value to ACTIVE when you create an endpoint or update an existing endpoint. Amazon Pinpoint automatically sets this value to INACTIVE if you update another endpoint that has the same address specified by the Address property.

Location -> (structure)

The geographic information for the endpoint.

City -> (string)

The name of the city where the endpoint is located.

Country -> (string)

The two-character code, in ISO 3166-1 alpha-2 format, for the country or region where the endpoint is located. For example, US for the United States.

Latitude -> (double)

The latitude coordinate of the endpoint location, rounded to one decimal place.

Longitude -> (double)

The longitude coordinate of the endpoint location, rounded to one decimal place.

PostalCode -> (string)

The postal or ZIP code for the area where the endpoint is located.

Region -> (string)

The name of the region where the endpoint is located. For locations in the United States, this value is the name of a state.

Metrics -> (map)

One or more custom metrics that your app reports to Amazon Pinpoint for the endpoint.

key -> (string)

value -> (double)

OptOut -> (string)

Specifies whether the user whoâs associated with the endpoint has opted out of receiving messages and push notifications from you. Possible values are: ALL, the user has opted out and doesnât want to receive any messages or push notifications; and, NONE, the user hasnât opted out and wants to receive all messages and push notifications.

RequestId -> (string)

The unique identifier for the most recent request to update the endpoint.

User -> (structure)

One or more custom attributes that describe the user whoâs associated with the endpoint.

UserAttributes -> (map)

One or more custom attributes that describe the user by associating a name with an array of values. For example, the value of an attribute named Interests might be: [âScienceâ, âMusicâ, âTravelâ]. You can use these attributes as filter criteria when you create segments. Attribute names are case sensitive.

An attribute name can contain up to 50 characters. An attribute value can contain up to 100 characters. When you define the name of a custom attribute, avoid using the following characters: number sign (#), colon (:), question mark (?), backslash (), and slash (/). The Amazon Pinpoint console canât display attribute names that contain these characters. This restriction doesnât apply to attribute values.

key -> (string)

value -> (list)

(string)

UserId -> (string)

The unique identifier for the user.

Shorthand Syntax:

```
Address=string,Attributes={KeyName1=string,string,KeyName2=string,string},ChannelType=string,Demographic={AppVersion=string,Locale=string,Make=string,Model=string,ModelVersion=string,Platform=string,PlatformVersion=string,Timezone=string},EffectiveDate=string,EndpointStatus=string,Location={City=string,Country=string,Latitude=double,Longitude=double,PostalCode=string,Region=string},Metrics={KeyName1=double,KeyName2=double},OptOut=string,RequestId=string,User={UserAttributes={KeyName1=[string,string],KeyName2=[string,string]},UserId=string}
```

JSON Syntax:

```
{
  "Address": "string",
  "Attributes": {"string": ["string", ...]
    ...},
  "ChannelType": "PUSH"|"GCM"|"APNS"|"APNS_SANDBOX"|"APNS_VOIP"|"APNS_VOIP_SANDBOX"|"ADM"|"SMS"|"VOICE"|"EMAIL"|"BAIDU"|"CUSTOM"|"IN_APP",
  "Demographic": {
    "AppVersion": "string",
    "Locale": "string",
    "Make": "string",
    "Model": "string",
    "ModelVersion": "string",
    "Platform": "string",
    "PlatformVersion": "string",
    "Timezone": "string"
  },
  "EffectiveDate": "string",
  "EndpointStatus": "string",
  "Location": {
    "City": "string",
    "Country": "string",
    "Latitude": double,
    "Longitude": double,
    "PostalCode": "string",
    "Region": "string"
  },
  "Metrics": {"string": double
    ...},
  "OptOut": "string",
  "RequestId": "string",
  "User": {
    "UserAttributes": {"string": ["string", ...]
      ...},
    "UserId": "string"
  }
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

MessageBody -> (structure)

Provides information about an API request or response.

Message -> (string)

The message thatâs returned from the API.

RequestID -> (string)

The unique identifier for the request or response.