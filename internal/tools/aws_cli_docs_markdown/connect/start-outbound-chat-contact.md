# start-outbound-chat-contactÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-outbound-chat-contact.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-outbound-chat-contact.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# start-outbound-chat-contact

## Description

Initiates a new outbound SMS contact to a customer. Response of this API provides the `ContactId` of the outbound SMS contact created.

**SourceEndpoint** only supports Endpoints with `CONNECT_PHONENUMBER_ARN` as Type and **DestinationEndpoint** only supports Endpoints with `TELEPHONE_NUMBER` as Type. **ContactFlowId** initiates the flow to manage the new SMS contact created.

This API can be used to initiate outbound SMS contacts for an agent, or it can also deflect an ongoing contact to an outbound SMS contact by using the [StartOutboundChatContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_StartOutboundChatContact.html) Flow Action.

For more information about using SMS in Amazon Connect, see the following topics in the *Amazon Connect Administrator Guide* :

- [Set up SMS messaging](https://docs.aws.amazon.com/connect/latest/adminguide/setup-sms-messaging.html)
- [Request an SMS-enabled phone number through AWS End User Messaging SMS](https://docs.aws.amazon.com/connect/latest/adminguide/sms-number.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/StartOutboundChatContact)

## Synopsis

```
start-outbound-chat-contact
--source-endpoint <value>
--destination-endpoint <value>
--instance-id <value>
--segment-attributes <value>
[--attributes <value>]
--contact-flow-id <value>
[--chat-duration-in-minutes <value>]
[--participant-details <value>]
[--initial-system-message <value>]
[--related-contact-id <value>]
[--supported-messaging-content-types <value>]
[--client-token <value>]
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

`--source-endpoint` (structure)

Information about the endpoint.

Type -> (string)

Type of the endpoint.

Address -> (string)

Address of the endpoint.

Shorthand Syntax:

```
Type=string,Address=string
```

JSON Syntax:

```
{
  "Type": "TELEPHONE_NUMBER"|"VOIP"|"CONTACT_FLOW"|"CONNECT_PHONENUMBER_ARN"|"EMAIL_ADDRESS",
  "Address": "string"
}
```

`--destination-endpoint` (structure)

Information about the endpoint.

Type -> (string)

Type of the endpoint.

Address -> (string)

Address of the endpoint.

Shorthand Syntax:

```
Type=string,Address=string
```

JSON Syntax:

```
{
  "Type": "TELEPHONE_NUMBER"|"VOIP"|"CONTACT_FLOW"|"CONNECT_PHONENUMBER_ARN"|"EMAIL_ADDRESS",
  "Address": "string"
}
```

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can find the instance ID in the Amazon Resource Name (ARN) of the instance.

`--segment-attributes` (map)

A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Amazon Connect attributes. They can be accessed in flows.

- Attribute keys can include only alphanumeric, `-` , and `_` .
- This field can be used to show channel subtype, such as `connect:Guide` and `connect:SMS` .

key -> (string)

value -> (structure)

A value for a segment attribute. This is structured as a map where the key is `valueString` and the value is a string.

ValueString -> (string)

The value of a segment attribute.

ValueMap -> (map)

The value of a segment attribute.

key -> (string)

value -> (structure)

A value for a segment attribute. This is structured as a map where the key is `valueString` and the value is a string.

ValueString -> (string)

The value of a segment attribute.

ValueMap -> (map)

The value of a segment attribute.

key -> (string)

( â¦ recursive â¦ )

ValueInteger -> (integer)

The value of a segment attribute.

ValueInteger -> (integer)

The value of a segment attribute.

Shorthand Syntax:

```
KeyName1=ValueString=string,ValueMap={KeyName1={ValueString=string,( ... recursive ... ),ValueInteger=integer},KeyName2={ValueString=string,( ... recursive ... ),ValueInteger=integer}},ValueInteger=integer,KeyName2=ValueString=string,ValueMap={KeyName1={ValueString=string,( ... recursive ... ),ValueInteger=integer},KeyName2={ValueString=string,( ... recursive ... ),ValueInteger=integer}},ValueInteger=integer
```

JSON Syntax:

```
{"string": {
      "ValueString": "string",
      "ValueMap": {"string": {
            "ValueString": "string",
            "ValueMap": {"string": { ... recursive ... }
              ...},
            "ValueInteger": integer
          }
        ...},
      "ValueInteger": integer
    }
  ...}
```

`--attributes` (map)

A custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in flows just like any other contact attributes.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--contact-flow-id` (string)

The identifier of the flow for the call. To see the ContactFlowId in the Amazon Connect console user interface, on the navigation menu go to **Routing, Contact Flows** . Choose the flow. On the flow page, under the name of the flow, choose **Show additional flow information** . The ContactFlowId is the last part of the ARN, shown here in bold:

- arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/**123ec456-a007-89c0-1234-xxxxxxxxxxxx**

`--chat-duration-in-minutes` (integer)

The total duration of the newly started chat session. If not specified, the chat session duration defaults to 25 hour. The minimum configurable time is 60 minutes. The maximum configurable time is 10,080 minutes (7 days).

`--participant-details` (structure)

The customerâs details.

DisplayName -> (string)

Display name of the participant.

Shorthand Syntax:

```
DisplayName=string
```

JSON Syntax:

```
{
  "DisplayName": "string"
}
```

`--initial-system-message` (structure)

A chat message.

ContentType -> (string)

The type of the content. Supported types are `text/plain` , `text/markdown` , `application/json` , and `application/vnd.amazonaws.connect.message.interactive.response` .

Content -> (string)

The content of the chat message.

- For `text/plain` and `text/markdown` , the Length Constraints are Minimum of 1, Maximum of 1024.
- For `application/json` , the Length Constraints are Minimum of 1, Maximum of 12000.
- For `application/vnd.amazonaws.connect.message.interactive.response` , the Length Constraints are Minimum of 1, Maximum of 12288.

Shorthand Syntax:

```
ContentType=string,Content=string
```

JSON Syntax:

```
{
  "ContentType": "string",
  "Content": "string"
}
```

`--related-contact-id` (string)

The unique identifier for an Amazon Connect contact. This identifier is related to the contact starting.

`--supported-messaging-content-types` (list)

The supported chat message content types. Supported types are:

- `text/plain`
- `text/markdown`
- `application/json, application/vnd.amazonaws.connect.message.interactive`
- `application/vnd.amazonaws.connect.message.interactive.response`

Content types must always contain `text/plain` . You can then put any other supported type in the list. For example, all the following lists are valid because they contain `text/plain` :

- `[text/plain, text/markdown, application/json]`
- `[text/markdown, text/plain]`
- `[text/plain, application/json, application/vnd.amazonaws.connect.message.interactive.response]`

(string)

Syntax:

```
"string" "string" ...
```

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) . The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned.

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

ContactId -> (string)

The identifier of this contact within the Amazon Connect instance.