# start-outbound-voice-contactÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-outbound-voice-contact.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/start-outbound-voice-contact.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# start-outbound-voice-contact

## Description

Places an outbound call to a contact, and then initiates the flow. It performs the actions in the flow thatâs specified (in `ContactFlowId` ).

Agents do not initiate the outbound API, which means that they do not dial the contact. If the flow places an outbound call to a contact, and then puts the contact in queue, the call is then routed to the agent, like any other inbound case.

There is a 60-second dialing timeout for this operation. If the call is not connected after 60 seconds, it fails.

### Note

UK numbers with a 447 prefix are not allowed by default. Before you can dial these UK mobile numbers, you must submit a service quota increase request. For more information, see [Amazon Connect Service Quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) in the *Amazon Connect Administrator Guide* .

### Note

Campaign calls are not allowed by default. Before you can make a call with `TrafficType` = `CAMPAIGN` , you must submit a service quota increase request to the quota [Amazon Connect campaigns](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#outbound-communications-quotas) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/StartOutboundVoiceContact)

## Synopsis

```
start-outbound-voice-contact
[--name <value>]
[--description <value>]
[--references <value>]
[--related-contact-id <value>]
--destination-phone-number <value>
--contact-flow-id <value>
--instance-id <value>
[--client-token <value>]
[--source-phone-number <value>]
[--queue-id <value>]
[--attributes <value>]
[--answer-machine-detection-config <value>]
[--campaign-id <value>]
[--traffic-type <value>]
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

`--name` (string)

The name of a voice contact that is shown to an agent in the Contact Control Panel (CCP).

`--description` (string)

A description of the voice contact that appears in the agentâs snapshot in the CCP logs. For more information about CCP logs, see [Download and review CCP logs](https://docs.aws.amazon.com/connect/latest/adminguide/download-ccp-logs.html) in the *Amazon Connect Administrator Guide* .

`--references` (map)

A formatted URL that is shown to an agent in the Contact Control Panel (CCP). Contacts can have the following reference types at the time of creation: `URL` | `NUMBER` | `STRING` | `DATE` | `EMAIL` . `ATTACHMENT` is not a supported reference type during voice contact creation.

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

`--related-contact-id` (string)

The `contactId` that is related to this contact. Linking voice, task, or chat by using `RelatedContactID` copies over contact attributes from the related contact to the new contact. All updates to user-defined attributes in the new contact are limited to the individual contact ID. There are no limits to the number of contacts that can be linked by using `RelatedContactId` .

`--destination-phone-number` (string)

The phone number of the customer, in E.164 format.

`--contact-flow-id` (string)

The identifier of the flow for the outbound call. To see the ContactFlowId in the Amazon Connect admin website, on the navigation menu go to **Routing** , **Contact Flows** . Choose the flow. On the flow page, under the name of the flow, choose **Show additional flow information** . The ContactFlowId is the last part of the ARN, shown here in bold:

arn:aws:connect:us-west-2:xxxxxxxxxxxx:instance/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx/contact-flow/**846ec553-a005-41c0-8341-xxxxxxxxxxxx**

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

`--client-token` (string)

A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see [Making retries safe with idempotent APIs](https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/) . The token is valid for 7 days after creation. If a contact is already started, the contact ID is returned.

`--source-phone-number` (string)

The phone number associated with the Amazon Connect instance, in E.164 format. If you do not specify a source phone number, you must specify a queue.

`--queue-id` (string)

The queue for the call. If you specify a queue, the phone displayed for caller ID is the phone number specified in the queue. If you do not specify a queue, the queue defined in the flow is used. If you do not specify a queue, you must specify a source phone number.

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

`--answer-machine-detection-config` (structure)

Configuration of the answering machine detection for this outbound call.

EnableAnswerMachineDetection -> (boolean)

The flag to indicate if answer machine detection analysis needs to be performed for a voice call. If set to `true` , `TrafficType` must be set as `CAMPAIGN` .

AwaitAnswerMachinePrompt -> (boolean)

Wait for the answering machine prompt.

Shorthand Syntax:

```
EnableAnswerMachineDetection=boolean,AwaitAnswerMachinePrompt=boolean
```

JSON Syntax:

```
{
  "EnableAnswerMachineDetection": true|false,
  "AwaitAnswerMachinePrompt": true|false
}
```

`--campaign-id` (string)

The campaign identifier of the outbound communication.

`--traffic-type` (string)

Denotes the class of traffic. Calls with different traffic types are handled differently by Amazon Connect. The default value is `GENERAL` . Use `CAMPAIGN` if `EnableAnswerMachineDetection` is set to `true` . For all other cases, use `GENERAL` .

Possible values:

- `GENERAL`
- `CAMPAIGN`

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