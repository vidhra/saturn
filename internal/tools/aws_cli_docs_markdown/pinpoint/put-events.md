# put-eventsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/put-events.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/put-events.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pinpoint](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pinpoint/index.html#cli-aws-pinpoint) ]

# put-events

## Description

Creates a new event to record for endpoints, or creates or updates endpoint data that existing events are associated with.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pinpoint-2016-12-01/PutEvents)

## Synopsis

```
put-events
--application-id <value>
--events-request <value>
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

`--events-request` (structure)

Specifies a batch of events to process.

BatchItem -> (map)

The batch of events to process. For each item in a batch, the endpoint ID acts as a key that has an EventsBatch object as its value.

key -> (string)

value -> (structure)

Specifies a batch of endpoints and events to process.

Endpoint -> (structure)

A set of properties and attributes that are associated with the endpoint.

Address -> (string)

The unique identifier for the recipient, such as a device token, email address, or mobile phone number.

Attributes -> (map)

One or more custom attributes that describe the endpoint by associating a name with an array of values. You can use these attributes as filter criteria when you create segments.

key -> (string)

value -> (list)

(string)

ChannelType -> (string)

The channel thatâs used when sending messages or push notifications to the endpoint.

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

The date and time, in ISO 8601 format, when the endpoint was last updated.

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

A unique identifier thatâs generated each time the endpoint is updated.

User -> (structure)

One or more custom user attributes that your app reports to Amazon Pinpoint for the user whoâs associated with the endpoint.

UserAttributes -> (map)

One or more custom attributes that describe the user by associating a name with an array of values. For example, the value of an attribute named Interests might be: [âScienceâ, âMusicâ, âTravelâ]. You can use these attributes as filter criteria when you create segments. Attribute names are case sensitive.

An attribute name can contain up to 50 characters. An attribute value can contain up to 100 characters. When you define the name of a custom attribute, avoid using the following characters: number sign (#), colon (:), question mark (?), backslash (), and slash (/). The Amazon Pinpoint console canât display attribute names that contain these characters. This restriction doesnât apply to attribute values.

key -> (string)

value -> (list)

(string)

UserId -> (string)

The unique identifier for the user.

Events -> (map)

A set of properties that are associated with the event.

key -> (string)

value -> (structure)

Specifies information about an event that reports data to Amazon Pinpoint.

AppPackageName -> (string)

The package name of the app thatâs recording the event.

AppTitle -> (string)

The title of the app thatâs recording the event.

AppVersionCode -> (string)

The version number of the app thatâs recording the event.

Attributes -> (map)

One or more custom attributes that are associated with the event.

key -> (string)

value -> (string)

ClientSdkVersion -> (string)

The version of the SDK thatâs running on the client device.

EventType -> (string)

The name of the event.

Metrics -> (map)

One or more custom metrics that are associated with the event.

key -> (string)

value -> (double)

SdkName -> (string)

The name of the SDK thatâs being used to record the event.

Session -> (structure)

Information about the session in which the event occurred.

Duration -> (integer)

The duration of the session, in milliseconds.

Id -> (string)

The unique identifier for the session.

StartTimestamp -> (string)

The date and time when the session began.

StopTimestamp -> (string)

The date and time when the session ended.

Timestamp -> (string)

The date and time, in ISO 8601 format, when the event occurred.

JSON Syntax:

```
{
  "BatchItem": {"string": {
        "Endpoint": {
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
        },
        "Events": {"string": {
              "AppPackageName": "string",
              "AppTitle": "string",
              "AppVersionCode": "string",
              "Attributes": {"string": "string"
                ...},
              "ClientSdkVersion": "string",
              "EventType": "string",
              "Metrics": {"string": double
                ...},
              "SdkName": "string",
              "Session": {
                "Duration": integer,
                "Id": "string",
                "StartTimestamp": "string",
                "StopTimestamp": "string"
              },
              "Timestamp": "string"
            }
          ...}
      }
    ...}
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

EventsResponse -> (structure)

Provides information about endpoints and the events that theyâre associated with.

Results -> (map)

A map that contains a multipart response for each endpoint. For each item in this object, the endpoint ID is the key and the item response is the value. If no item response exists, the value can also be one of the following: 202, the request was processed successfully; or 400, the payload wasnât valid or required fields were missing.

key -> (string)

value -> (structure)

Provides information about the results of a request to create or update an endpoint thatâs associated with an event.

EndpointItemResponse -> (structure)

The response that was received after the endpoint data was accepted.

Message -> (string)

The custom message thatâs returned in the response as a result of processing the endpoint data.

StatusCode -> (integer)

The status code thatâs returned in the response as a result of processing the endpoint data.

EventsItemResponse -> (map)

A multipart response object that contains a key and a value for each event in the request. In each object, the event ID is the key and an EventItemResponse object is the value.

key -> (string)

value -> (structure)

Provides the status code and message that result from processing an event.

Message -> (string)

A custom message thatâs returned in the response as a result of processing the event.

StatusCode -> (integer)

The status code thatâs returned in the response as a result of processing the event. Possible values are: 202, for events that were accepted; and, 400, for events that werenât valid.