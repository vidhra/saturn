# update-message-templateÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/update-message-template.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/update-message-template.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qconnect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qconnect/index.html#cli-aws-qconnect) ]

# update-message-template

## Description

Updates the Amazon Q in Connect message template. Partial update is supported. If any field is not supplied, it will remain unchanged for the message template that is referenced by the `$LATEST` qualifier. Any modification will only apply to the message template that is referenced by the `$LATEST` qualifier. The fields for all available versions will remain unchanged.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qconnect-2020-10-19/UpdateMessageTemplate)

## Synopsis

```
update-message-template
--knowledge-base-id <value>
--message-template-id <value>
[--content <value>]
[--language <value>]
[--default-attributes <value>]
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

`--knowledge-base-id` (string)

The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.

`--message-template-id` (string)

The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.

`--content` (tagged union structure)

The content of the message template.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `email`, `sms`.

email -> (structure)

The content of the message template that applies to the email channel subtype.

subject -> (string)

The subject line, or title, to use in email messages.

body -> (structure)

The body to use in email messages.

plainText -> (tagged union structure)

The message body, in plain text format, to use in email messages that are based on the message template. We recommend using plain text format for email clients that donât render HTML content and clients that are connected to high-latency networks, such as mobile devices.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `content`.

content -> (string)

The content of the message template.

html -> (tagged union structure)

The message body, in HTML format, to use in email messages that are based on the message template. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `content`.

content -> (string)

The content of the message template.

headers -> (list)

The email headers to include in email messages.

(structure)

The email header to include in email messages.

name -> (string)

The name of the email header.

value -> (string)

The value of the email header.

sms -> (structure)

The content of the message template that applies to the SMS channel subtype.

body -> (structure)

The body to use in SMS messages.

plainText -> (tagged union structure)

The message body to use in SMS messages.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `content`.

content -> (string)

The content of the message template.

JSON Syntax:

```
{
  "email": {
    "subject": "string",
    "body": {
      "plainText": {
        "content": "string"
      },
      "html": {
        "content": "string"
      }
    },
    "headers": [
      {
        "name": "string",
        "value": "string"
      }
      ...
    ]
  },
  "sms": {
    "body": {
      "plainText": {
        "content": "string"
      }
    }
  }
}
```

`--language` (string)

The language code value for the language in which the quick response is written. The supported language codes include `de_DE` , `en_US` , `es_ES` , `fr_FR` , `id_ID` , `it_IT` , `ja_JP` , `ko_KR` , `pt_BR` , `zh_CN` , `zh_TW`

`--default-attributes` (structure)

An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.

systemAttributes -> (structure)

The system attributes that are used with the message template.

name -> (string)

The name of the task.

customerEndpoint -> (structure)

The CustomerEndpoint attribute.

address -> (string)

The customerâs phone number if used with `customerEndpoint` , or the number the customer dialed to call your contact center if used with `systemEndpoint` .

systemEndpoint -> (structure)

The SystemEndpoint attribute.

address -> (string)

The customerâs phone number if used with `customerEndpoint` , or the number the customer dialed to call your contact center if used with `systemEndpoint` .

agentAttributes -> (structure)

The agent attributes that are used with the message template.

firstName -> (string)

The agentâs first name as entered in their Amazon Connect user account.

lastName -> (string)

The agentâs last name as entered in their Amazon Connect user account.

customerProfileAttributes -> (structure)

The customer profile attributes that are used with the message template.

profileId -> (string)

The unique identifier of a customer profile.

profileARN -> (string)

The ARN of a customer profile.

firstName -> (string)

The customerâs first name.

middleName -> (string)

The customerâs middle name.

lastName -> (string)

The customerâs last name.

accountNumber -> (string)

A unique account number that you have given to the customer.

emailAddress -> (string)

The customerâs email address, which has not been specified as a personal or business address.

phoneNumber -> (string)

The customerâs phone number, which has not been specified as a mobile, home, or business number.

additionalInformation -> (string)

Any additional information relevant to the customerâs profile.

partyType -> (string)

The customerâs party type.

businessName -> (string)

The name of the customerâs business.

birthDate -> (string)

The customerâs birth date.

gender -> (string)

The customerâs gender.

mobilePhoneNumber -> (string)

The customerâs mobile phone number.

homePhoneNumber -> (string)

The customerâs mobile phone number.

businessPhoneNumber -> (string)

The customerâs business phone number.

businessEmailAddress -> (string)

The customerâs business email address.

address1 -> (string)

The first line of a customer address.

address2 -> (string)

The second line of a customer address.

address3 -> (string)

The third line of a customer address.

address4 -> (string)

The fourth line of a customer address.

city -> (string)

The city in which a customer lives.

county -> (string)

The county in which a customer lives.

country -> (string)

The country in which a customer lives.

postalCode -> (string)

The postal code of a customer address.

province -> (string)

The province in which a customer lives.

state -> (string)

The state in which a customer lives.

shippingAddress1 -> (string)

The first line of a customerâs shipping address.

shippingAddress2 -> (string)

The second line of a customerâs shipping address.

shippingAddress3 -> (string)

The third line of a customerâs shipping address.

shippingAddress4 -> (string)

The fourth line of a customerâs shipping address.

shippingCity -> (string)

The city of a customerâs shipping address.

shippingCounty -> (string)

The county of a customerâs shipping address.

shippingCountry -> (string)

The country of a customerâs shipping address.

shippingPostalCode -> (string)

The postal code of a customerâs shipping address.

shippingProvince -> (string)

The province of a customerâs shipping address.

shippingState -> (string)

The state of a customerâs shipping address.

mailingAddress1 -> (string)

The first line of a customerâs mailing address.

mailingAddress2 -> (string)

The second line of a customerâs mailing address.

mailingAddress3 -> (string)

The third line of a customerâs mailing address.

mailingAddress4 -> (string)

The fourth line of a customerâs mailing address.

mailingCity -> (string)

The city of a customerâs mailing address.

mailingCounty -> (string)

The county of a customerâs mailing address.

mailingCountry -> (string)

The country of a customerâs mailing address.

mailingPostalCode -> (string)

The postal code of a customerâs mailing address.

mailingProvince -> (string)

The province of a customerâs mailing address.

mailingState -> (string)

The state of a customerâs mailing address.

billingAddress1 -> (string)

The first line of a customerâs billing address.

billingAddress2 -> (string)

The second line of a customerâs billing address.

billingAddress3 -> (string)

The third line of a customerâs billing address.

billingAddress4 -> (string)

The fourth line of a customerâs billing address.

billingCity -> (string)

The city of a customerâs billing address.

billingCounty -> (string)

The county of a customerâs billing address.

billingCountry -> (string)

The country of a customerâs billing address.

billingPostalCode -> (string)

The postal code of a customerâs billing address.

billingProvince -> (string)

The province of a customerâs billing address.

billingState -> (string)

The state of a customerâs billing address.

custom -> (map)

The custom attributes in customer profile attributes.

key -> (string)

value -> (string)

customAttributes -> (map)

The custom attributes that are used with the message template.

key -> (string)

value -> (string)

Shorthand Syntax:

```
systemAttributes={name=string,customerEndpoint={address=string},systemEndpoint={address=string}},agentAttributes={firstName=string,lastName=string},customerProfileAttributes={profileId=string,profileARN=string,firstName=string,middleName=string,lastName=string,accountNumber=string,emailAddress=string,phoneNumber=string,additionalInformation=string,partyType=string,businessName=string,birthDate=string,gender=string,mobilePhoneNumber=string,homePhoneNumber=string,businessPhoneNumber=string,businessEmailAddress=string,address1=string,address2=string,address3=string,address4=string,city=string,county=string,country=string,postalCode=string,province=string,state=string,shippingAddress1=string,shippingAddress2=string,shippingAddress3=string,shippingAddress4=string,shippingCity=string,shippingCounty=string,shippingCountry=string,shippingPostalCode=string,shippingProvince=string,shippingState=string,mailingAddress1=string,mailingAddress2=string,mailingAddress3=string,mailingAddress4=string,mailingCity=string,mailingCounty=string,mailingCountry=string,mailingPostalCode=string,mailingProvince=string,mailingState=string,billingAddress1=string,billingAddress2=string,billingAddress3=string,billingAddress4=string,billingCity=string,billingCounty=string,billingCountry=string,billingPostalCode=string,billingProvince=string,billingState=string,custom={KeyName1=string,KeyName2=string}},customAttributes={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "systemAttributes": {
    "name": "string",
    "customerEndpoint": {
      "address": "string"
    },
    "systemEndpoint": {
      "address": "string"
    }
  },
  "agentAttributes": {
    "firstName": "string",
    "lastName": "string"
  },
  "customerProfileAttributes": {
    "profileId": "string",
    "profileARN": "string",
    "firstName": "string",
    "middleName": "string",
    "lastName": "string",
    "accountNumber": "string",
    "emailAddress": "string",
    "phoneNumber": "string",
    "additionalInformation": "string",
    "partyType": "string",
    "businessName": "string",
    "birthDate": "string",
    "gender": "string",
    "mobilePhoneNumber": "string",
    "homePhoneNumber": "string",
    "businessPhoneNumber": "string",
    "businessEmailAddress": "string",
    "address1": "string",
    "address2": "string",
    "address3": "string",
    "address4": "string",
    "city": "string",
    "county": "string",
    "country": "string",
    "postalCode": "string",
    "province": "string",
    "state": "string",
    "shippingAddress1": "string",
    "shippingAddress2": "string",
    "shippingAddress3": "string",
    "shippingAddress4": "string",
    "shippingCity": "string",
    "shippingCounty": "string",
    "shippingCountry": "string",
    "shippingPostalCode": "string",
    "shippingProvince": "string",
    "shippingState": "string",
    "mailingAddress1": "string",
    "mailingAddress2": "string",
    "mailingAddress3": "string",
    "mailingAddress4": "string",
    "mailingCity": "string",
    "mailingCounty": "string",
    "mailingCountry": "string",
    "mailingPostalCode": "string",
    "mailingProvince": "string",
    "mailingState": "string",
    "billingAddress1": "string",
    "billingAddress2": "string",
    "billingAddress3": "string",
    "billingAddress4": "string",
    "billingCity": "string",
    "billingCounty": "string",
    "billingCountry": "string",
    "billingPostalCode": "string",
    "billingProvince": "string",
    "billingState": "string",
    "custom": {"string": "string"
      ...}
  },
  "customAttributes": {"string": "string"
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

messageTemplate -> (structure)

The message template.

messageTemplateArn -> (string)

The Amazon Resource Name (ARN) of the message template.

messageTemplateId -> (string)

The identifier of the message template.

knowledgeBaseArn -> (string)

The Amazon Resource Name (ARN) of the knowledge base.

knowledgeBaseId -> (string)

The identifier of the knowledge base.

name -> (string)

The name of the message template.

channelSubtype -> (string)

The channel subtype this message template applies to.

createdTime -> (timestamp)

The timestamp when the message template was created.

lastModifiedTime -> (timestamp)

The timestamp when the message template data was last modified.

lastModifiedBy -> (string)

The Amazon Resource Name (ARN) of the user who last updated the message template data.

content -> (tagged union structure)

The content of the message template.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `email`, `sms`.

email -> (structure)

The content of the message template that applies to the email channel subtype.

subject -> (string)

The subject line, or title, to use in email messages.

body -> (structure)

The body to use in email messages.

plainText -> (tagged union structure)

The message body, in plain text format, to use in email messages that are based on the message template. We recommend using plain text format for email clients that donât render HTML content and clients that are connected to high-latency networks, such as mobile devices.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `content`.

content -> (string)

The content of the message template.

html -> (tagged union structure)

The message body, in HTML format, to use in email messages that are based on the message template. We recommend using HTML format for email clients that render HTML content. You can include links, formatted text, and more in an HTML message.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `content`.

content -> (string)

The content of the message template.

headers -> (list)

The email headers to include in email messages.

(structure)

The email header to include in email messages.

name -> (string)

The name of the email header.

value -> (string)

The value of the email header.

sms -> (structure)

The content of the message template that applies to the SMS channel subtype.

body -> (structure)

The body to use in SMS messages.

plainText -> (tagged union structure)

The message body to use in SMS messages.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `content`.

content -> (string)

The content of the message template.

description -> (string)

The description of the message template.

language -> (string)

The language code value for the language in which the quick response is written. The supported language codes include `de_DE` , `en_US` , `es_ES` , `fr_FR` , `id_ID` , `it_IT` , `ja_JP` , `ko_KR` , `pt_BR` , `zh_CN` , `zh_TW`

groupingConfiguration -> (structure)

The configuration information of the grouping of Amazon Q in Connect users.

criteria -> (string)

The criteria used for grouping Amazon Q in Connect users.

The following is the list of supported criteria values.

- `RoutingProfileArn` : Grouping the users by their [Amazon Connect routing profile ARN](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html) . User should have [SearchRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchRoutingProfiles.html) and [DescribeRoutingProfile](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeRoutingProfile.html) permissions when setting criteria to this value.

values -> (list)

The list of values that define different groups of Amazon Q in Connect users.

- When setting `criteria` to `RoutingProfileArn` , you need to provide a list of ARNs of [Amazon Connect routing profiles](https://docs.aws.amazon.com/connect/latest/APIReference/API_RoutingProfile.html) as values of this parameter.

(string)

defaultAttributes -> (structure)

An object that specifies the default values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template. The corresponding value defines the default value for that variable.

systemAttributes -> (structure)

The system attributes that are used with the message template.

name -> (string)

The name of the task.

customerEndpoint -> (structure)

The CustomerEndpoint attribute.

address -> (string)

The customerâs phone number if used with `customerEndpoint` , or the number the customer dialed to call your contact center if used with `systemEndpoint` .

systemEndpoint -> (structure)

The SystemEndpoint attribute.

address -> (string)

The customerâs phone number if used with `customerEndpoint` , or the number the customer dialed to call your contact center if used with `systemEndpoint` .

agentAttributes -> (structure)

The agent attributes that are used with the message template.

firstName -> (string)

The agentâs first name as entered in their Amazon Connect user account.

lastName -> (string)

The agentâs last name as entered in their Amazon Connect user account.

customerProfileAttributes -> (structure)

The customer profile attributes that are used with the message template.

profileId -> (string)

The unique identifier of a customer profile.

profileARN -> (string)

The ARN of a customer profile.

firstName -> (string)

The customerâs first name.

middleName -> (string)

The customerâs middle name.

lastName -> (string)

The customerâs last name.

accountNumber -> (string)

A unique account number that you have given to the customer.

emailAddress -> (string)

The customerâs email address, which has not been specified as a personal or business address.

phoneNumber -> (string)

The customerâs phone number, which has not been specified as a mobile, home, or business number.

additionalInformation -> (string)

Any additional information relevant to the customerâs profile.

partyType -> (string)

The customerâs party type.

businessName -> (string)

The name of the customerâs business.

birthDate -> (string)

The customerâs birth date.

gender -> (string)

The customerâs gender.

mobilePhoneNumber -> (string)

The customerâs mobile phone number.

homePhoneNumber -> (string)

The customerâs mobile phone number.

businessPhoneNumber -> (string)

The customerâs business phone number.

businessEmailAddress -> (string)

The customerâs business email address.

address1 -> (string)

The first line of a customer address.

address2 -> (string)

The second line of a customer address.

address3 -> (string)

The third line of a customer address.

address4 -> (string)

The fourth line of a customer address.

city -> (string)

The city in which a customer lives.

county -> (string)

The county in which a customer lives.

country -> (string)

The country in which a customer lives.

postalCode -> (string)

The postal code of a customer address.

province -> (string)

The province in which a customer lives.

state -> (string)

The state in which a customer lives.

shippingAddress1 -> (string)

The first line of a customerâs shipping address.

shippingAddress2 -> (string)

The second line of a customerâs shipping address.

shippingAddress3 -> (string)

The third line of a customerâs shipping address.

shippingAddress4 -> (string)

The fourth line of a customerâs shipping address.

shippingCity -> (string)

The city of a customerâs shipping address.

shippingCounty -> (string)

The county of a customerâs shipping address.

shippingCountry -> (string)

The country of a customerâs shipping address.

shippingPostalCode -> (string)

The postal code of a customerâs shipping address.

shippingProvince -> (string)

The province of a customerâs shipping address.

shippingState -> (string)

The state of a customerâs shipping address.

mailingAddress1 -> (string)

The first line of a customerâs mailing address.

mailingAddress2 -> (string)

The second line of a customerâs mailing address.

mailingAddress3 -> (string)

The third line of a customerâs mailing address.

mailingAddress4 -> (string)

The fourth line of a customerâs mailing address.

mailingCity -> (string)

The city of a customerâs mailing address.

mailingCounty -> (string)

The county of a customerâs mailing address.

mailingCountry -> (string)

The country of a customerâs mailing address.

mailingPostalCode -> (string)

The postal code of a customerâs mailing address.

mailingProvince -> (string)

The province of a customerâs mailing address.

mailingState -> (string)

The state of a customerâs mailing address.

billingAddress1 -> (string)

The first line of a customerâs billing address.

billingAddress2 -> (string)

The second line of a customerâs billing address.

billingAddress3 -> (string)

The third line of a customerâs billing address.

billingAddress4 -> (string)

The fourth line of a customerâs billing address.

billingCity -> (string)

The city of a customerâs billing address.

billingCounty -> (string)

The county of a customerâs billing address.

billingCountry -> (string)

The country of a customerâs billing address.

billingPostalCode -> (string)

The postal code of a customerâs billing address.

billingProvince -> (string)

The province of a customerâs billing address.

billingState -> (string)

The state of a customerâs billing address.

custom -> (map)

The custom attributes in customer profile attributes.

key -> (string)

value -> (string)

customAttributes -> (map)

The custom attributes that are used with the message template.

key -> (string)

value -> (string)

attributeTypes -> (list)

The types of attributes that the message template contains.

(string)

messageTemplateContentSha256 -> (string)

The checksum value of the message template content that is referenced by the `$LATEST` qualifier. It can be returned in `MessageTemplateData` or `ExtendedMessageTemplateData` . Itâs calculated by content, language, `defaultAttributes` and `Attachments` of the message template.

tags -> (map)

The tags used to organize, track, or control access for this resource.

key -> (string)

value -> (string)