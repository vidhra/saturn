# create-queueÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-queue.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-queue.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# create-queue

## Description

Creates a new queue for the specified Amazon Connect instance.

### Warning

- If the phone number is claimed to a traffic distribution group that was created in the same Region as the Amazon Connect instance where you are calling this API, then you can use a full phone number ARN or a UUID for `OutboundCallerIdNumberId` . However, if the phone number is claimed to a traffic distribution group that is in one Region, and you are calling this API from an instance in another Amazon Web Services Region that is associated with the traffic distribution group, you must provide a full phone number ARN. If a UUID is provided in this scenario, you will receive a `ResourceNotFoundException` .
- Only use the phone number ARN format that doesnât contain `instance` in the path, for example, `arn:aws:connect:us-east-1:1234567890:phone-number/uuid` . This is the same ARN format that is returned when you call the [ListPhoneNumbersV2](https://docs.aws.amazon.com/connect/latest/APIReference/API_ListPhoneNumbersV2.html) API.
- If you plan to use IAM policies to allow/deny access to this API for phone number resources claimed to a traffic distribution group, see [Allow or Deny queue API actions for phone numbers in a replica Region](https://docs.aws.amazon.com/connect/latest/adminguide/security_iam_resource-level-policy-examples.html#allow-deny-queue-actions-replica-region) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/CreateQueue)

## Synopsis

```
create-queue
--instance-id <value>
--name <value>
[--description <value>]
[--outbound-caller-config <value>]
[--outbound-email-config <value>]
--hours-of-operation-id <value>
[--max-contacts <value>]
[--quick-connect-ids <value>]
[--tags <value>]
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

`--name` (string)

The name of the queue.

`--description` (string)

The description of the queue.

`--outbound-caller-config` (structure)

The outbound caller ID name, number, and outbound whisper flow.

OutboundCallerIdName -> (string)

The caller ID name.

OutboundCallerIdNumberId -> (string)

The caller ID number.

OutboundFlowId -> (string)

The outbound whisper flow to be used during an outbound call.

Shorthand Syntax:

```
OutboundCallerIdName=string,OutboundCallerIdNumberId=string,OutboundFlowId=string
```

JSON Syntax:

```
{
  "OutboundCallerIdName": "string",
  "OutboundCallerIdNumberId": "string",
  "OutboundFlowId": "string"
}
```

`--outbound-email-config` (structure)

The outbound email address ID for a specified queue.

OutboundEmailAddressId -> (string)

The identifier of the email address.

Shorthand Syntax:

```
OutboundEmailAddressId=string
```

JSON Syntax:

```
{
  "OutboundEmailAddressId": "string"
}
```

`--hours-of-operation-id` (string)

The identifier for the hours of operation.

`--max-contacts` (integer)

The maximum number of contacts that can be in the queue before it is considered full.

`--quick-connect-ids` (list)

The quick connects available to agents who are working the queue.

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (map)

The tags used to organize, track, or control access for this resource. For example, { âTagsâ: {âkey1â:âvalue1â, âkey2â:âvalue2â} }.

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

QueueArn -> (string)

The Amazon Resource Name (ARN) of the queue.

QueueId -> (string)

The identifier for the queue.