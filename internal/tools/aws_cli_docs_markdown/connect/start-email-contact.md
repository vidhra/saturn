# start-email-contactÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-email-contact.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-email-contact.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# start-email-contact

## Description

Creates an inbound email contact and initiates a flow to start the email contact for the customer. Response of this API provides the ContactId of the email contact created.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/StartEmailContact)

## Synopsis

```
start-email-contact
--instance-id <value>
--from-email-address <value>
--destination-email-address <value>
[--description <value>]
[--references <value>]
[--name <value>]
--email-message <value>
[--additional-recipients <value>]
[--attachments <value>]
[--contact-flow-id <value>]
[--related-contact-id <value>]
[--attributes <value>]
[--segment-attributes <value>]
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

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--from-email-address` (structure)

The email address of the customer.

EmailAddress -> (string)

The email address with the instance, in [^s@]+@[^s@]+.[^s@]+ format.

DisplayName -> (string)

The display name of email address.

Shorthand Syntax:

```
EmailAddress=string,DisplayName=string
```

JSON Syntax:

```
{
  "EmailAddress": "string",
  "DisplayName": "string"
}
```

`--destination-email-address` (string)

The email address associated with the instance.

`--description` (string)

A description of the email contact.

`--references` (map)

A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Emails can have the following reference types at the time of creation: `URL` | `NUMBER` | `STRING` | `DATE` . `EMAIL` | `EMAIL_MESSAGE` [|](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-email-contact.html#id1)`ATTACHMENT` are not a supported reference type during email creation.

key -> (string)

value -> (structure)

Well-formed data on a contact, used by agents to complete a contact request. You can have up to 4,096 UTF-8 bytes across all references for a contact.

Value -> (string)

A valid value for the reference. For example, for a URL reference, a formatted URL that is displayed to an agent in the Contact Control Panel (CCP).

Type -> (string)

The type of the reference. `DATE` must be of type Epoch timestamp.

Status -> (string)

Status of the attachment reference type.

Arn -> (string)

The Amazon Resource Name (ARN) of the reference

StatusReason -> (string)

Relevant details why the reference was not successfully created.

Shorthand Syntax:

```
KeyName1=Value=string,Type=string,Status=string,Arn=string,StatusReason=string,KeyName2=Value=string,Type=string,Status=string,Arn=string,StatusReason=string
```

JSON Syntax:

```
{"string": {
      "Value": "string",
      "Type": "URL"|"ATTACHMENT"|"CONTACT_ANALYSIS"|"NUMBER"|"STRING"|"DATE"|"EMAIL"|"EMAIL_MESSAGE",
      "Status": "AVAILABLE"|"DELETED"|"APPROVED"|"REJECTED"|"PROCESSING"|"FAILED",
      "Arn": "string",
      "StatusReason": "string"
    }
  ...}
```

`--name` (string)

The name of a email that is shown to an agent in the Contact Control Panel (CCP).

`--email-message` (structure)

The email message body to be sent to the newly created email.

MessageSourceType -> (string)

The message source type, that is, `RAW` .

RawMessage -> (structure)

The raw email body content.

Subject -> (string)

The email subject.

Body -> (string)

The email message body.

ContentType -> (string)

Type of content, that is, `text/plain` or `text/html` .

Headers -> (map)

Headers present in inbound email.

key -> (string)

value -> (string)

Shorthand Syntax:

```
MessageSourceType=string,RawMessage={Subject=string,Body=string,ContentType=string,Headers={KeyName1=string,KeyName2=string}}
```

JSON Syntax:

```
{
  "MessageSourceType": "RAW",
  "RawMessage": {
    "Subject": "string",
    "Body": "string",
    "ContentType": "string",
    "Headers": {"REFERENCES"|"MESSAGE_ID"|"IN_REPLY_TO"|"X_SES_SPAM_VERDICT"|"X_SES_VIRUS_VERDICT": "string"
      ...}
  }
}
```

`--additional-recipients` (structure)

The addtional recipients address of the email.

ToAddresses -> (list)

The additional recipients information present in to list.

(structure)

Contains information about a source or destination email address

EmailAddress -> (string)

The email address with the instance, in [^s@]+@[^s@]+.[^s@]+ format.

DisplayName -> (string)

The display name of email address.

CcAddresses -> (list)

The additional recipients information present in cc list.

(structure)

Contains information about a source or destination email address

EmailAddress -> (string)

The email address with the instance, in [^s@]+@[^s@]+.[^s@]+ format.

DisplayName -> (string)

The display name of email address.

Shorthand Syntax:

```
ToAddresses=[{EmailAddress=string,DisplayName=string},{EmailAddress=string,DisplayName=string}],CcAddresses=[{EmailAddress=string,DisplayName=string},{EmailAddress=string,DisplayName=string}]
```

JSON Syntax:

```
{
  "ToAddresses": [
    {
      "EmailAddress": "string",
      "DisplayName": "string"
    }
    ...
  ],
  "CcAddresses": [
    {
      "EmailAddress": "string",
      "DisplayName": "string"
    }
    ...
  ]
}
```

`--attachments` (list)

List of S3 presigned URLs of email attachments and their file name.

(structure)

Information about the email attachment files.

FileName -> (string)

A case-sensitive name of the attached file being uploaded.

S3Url -> (string)

The pre-signed URLs for the S3 bucket where the email attachment is stored.

Shorthand Syntax:

```
FileName=string,S3Url=string ...
```

JSON Syntax:

```
[
  {
    "FileName": "string",
    "S3Url": "string"
  }
  ...
]
```

`--contact-flow-id` (string)

The identifier of the flow for initiating the emails. To see the ContactFlowId in the Amazon Connect admin website, on the navigation menu go to **Routing** , **Flows** . Choose the flow. On the flow page, under the name of the flow, choose **Show additional flow information** . The ContactFlowId is the last part of the ARN, shown here in bold:

arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/**846ec553-a005-41c0-8341-xxxxxxxxxxxx**

`--related-contact-id` (string)

The contactId that is related to this contact. Linking emails together by using `RelatedContactID` copies over contact attributes from the related email contact to the new email contact. All updates to user-defined attributes in the new email contact are limited to the individual contact ID. There are no limits to the number of contacts that can be linked by using `RelatedContactId` .

`--attributes` (map)

A custom key-value pair using an attribute map. The attributes are standard Amazon Connect attributes, and can be accessed in flows just like any other contact attributes.

There can be up to 32,768 UTF-8 bytes across all key-value pairs per contact. Attribute keys can include only alphanumeric, dash, and underscore characters.

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

`--segment-attributes` (map)

A set of system defined key-value pairs stored on individual contact segments using an attribute map. The attributes are standard Amazon Connect attributes. They can be accessed in flows.

Attribute keys can include only alphanumeric, -, and _.

This field can be used to show channel subtype, such as `connect:Guide` .

### Note

To set contact expiry, a `ValueMap` must be specified containing the integer number of minutes the contact will be active for before expiring, with `SegmentAttributes` like { `"connect:ContactExpiry": {"ValueMap" : { "ExpiryDuration": { "ValueInteger":135}}}}` .

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

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) .

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