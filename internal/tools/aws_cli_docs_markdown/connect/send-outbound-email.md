# send-outbound-emailÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/send-outbound-email.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/send-outbound-email.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# send-outbound-email

## Description

Send outbound email for outbound campaigns. For more information about outbound campaigns, see [Set up Amazon Connect outbound campaigns](https://docs.aws.amazon.com/connect/latest/adminguide/enable-outbound-campaigns.html) .

### Note

Only the Amazon Connect outbound campaigns service principal is allowed to assume a role in your account and call this API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/SendOutboundEmail)

## Synopsis

```
send-outbound-email
--instance-id <value>
--from-email-address <value>
--destination-email-address <value>
[--additional-recipients <value>]
--email-message <value>
--traffic-type <value>
[--source-campaign <value>]
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

The email address to be used for sending email.

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

`--destination-email-address` (structure)

The email address to send the email to.

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

`--additional-recipients` (structure)

The additional recipients address of the email in CC.

CcEmailAddresses -> (list)

The additional CC email address recipients information.

(structure)

Contains information about a source or destination email address

EmailAddress -> (string)

The email address with the instance, in [^s@]+@[^s@]+.[^s@]+ format.

DisplayName -> (string)

The display name of email address.

Shorthand Syntax:

```
CcEmailAddresses=[{EmailAddress=string,DisplayName=string},{EmailAddress=string,DisplayName=string}]
```

JSON Syntax:

```
{
  "CcEmailAddresses": [
    {
      "EmailAddress": "string",
      "DisplayName": "string"
    }
    ...
  ]
}
```

`--email-message` (structure)

The email message body to be sent to the newly created email.

MessageSourceType -> (string)

The message source type, that is, `RAW` or `TEMPLATE` .

TemplatedMessageConfig -> (structure)

Information about template message configuration.

KnowledgeBaseId -> (string)

The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.

MessageTemplateId -> (string)

The identifier of the message template Id.

TemplateAttributes -> (structure)

Information about template attributes, that is, CustomAttributes or CustomerProfileAttributes.

CustomAttributes -> (map)

An object that specifies the custom attributes values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template.

key -> (string)

value -> (string)

CustomerProfileAttributes -> (string)

An object that specifies the customer profile attributes values to use for variables in the message template. This object contains different categories of key-value pairs. Each key defines a variable or placeholder in the message template.

RawMessage -> (structure)

The raw email body content.

Subject -> (string)

The email subject.

Body -> (string)

The email message body.

ContentType -> (string)

Type of content, that is, `text/plain` or `text/html` .

Shorthand Syntax:

```
MessageSourceType=string,TemplatedMessageConfig={KnowledgeBaseId=string,MessageTemplateId=string,TemplateAttributes={CustomAttributes={KeyName1=string,KeyName2=string},CustomerProfileAttributes=string}},RawMessage={Subject=string,Body=string,ContentType=string}
```

JSON Syntax:

```
{
  "MessageSourceType": "TEMPLATE"|"RAW",
  "TemplatedMessageConfig": {
    "KnowledgeBaseId": "string",
    "MessageTemplateId": "string",
    "TemplateAttributes": {
      "CustomAttributes": {"string": "string"
        ...},
      "CustomerProfileAttributes": "string"
    }
  },
  "RawMessage": {
    "Subject": "string",
    "Body": "string",
    "ContentType": "string"
  }
}
```

`--traffic-type` (string)

Denotes the class of traffic.

### Note

Only the CAMPAIGN traffic type is supported.

Possible values:

- `GENERAL`
- `CAMPAIGN`

`--source-campaign` (structure)

A Campaign object need for Campaign traffic type.

CampaignId -> (string)

A unique identifier for a campaign.

OutboundRequestId -> (string)

A unique identifier for a each request part of same campaign.

Shorthand Syntax:

```
CampaignId=string,OutboundRequestId=string
```

JSON Syntax:

```
{
  "CampaignId": "string",
  "OutboundRequestId": "string"
}
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

None