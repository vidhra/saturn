# create-contactÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/create-contact.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/create-contact.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm-contacts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm-contacts/index.html#cli-aws-ssm-contacts) ]

# create-contact

## Description

Contacts are either the contacts that Incident Manager engages during an incident or the escalation plans that Incident Manager uses to engage contacts in phases during an incident.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-contacts-2021-05-03/CreateContact)

## Synopsis

```
create-contact
--alias <value>
[--display-name <value>]
--type <value>
--plan <value>
[--tags <value>]
[--idempotency-token <value>]
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

`--alias` (string)

The short name to quickly identify a contact or escalation plan. The contact alias must be unique and identifiable.

`--display-name` (string)

The full name of the contact or escalation plan.

`--type` (string)

To create an escalation plan use `ESCALATION` . To create a contact use `PERSONAL` .

Possible values:

- `PERSONAL`
- `ESCALATION`
- `ONCALL_SCHEDULE`

`--plan` (structure)

A list of stages. A contact has an engagement plan with stages that contact specified contact channels. An escalation plan uses stages that contact specified contacts.

Stages -> (list)

A list of stages that the escalation plan or engagement plan uses to engage contacts and contact methods.

(structure)

A set amount of time that an escalation plan or engagement plan engages the specified contacts or contact methods.

DurationInMinutes -> (integer)

The time to wait until beginning the next stage. The duration can only be set to 0 if a target is specified.

Targets -> (list)

The contacts or contact methods that the escalation plan or engagement plan is engaging.

(structure)

The contact or contact channel thatâs being engaged.

ChannelTargetInfo -> (structure)

Information about the contact channel Incident Manager is engaging.

ContactChannelId -> (string)

The Amazon Resource Name (ARN) of the contact channel.

RetryIntervalInMinutes -> (integer)

The number of minutes to wait to retry sending engagement in the case the engagement initially fails.

ContactTargetInfo -> (structure)

Information about the contact that Incident Manager is engaging.

ContactId -> (string)

The Amazon Resource Name (ARN) of the contact.

IsEssential -> (boolean)

A Boolean value determining if the contactâs acknowledgement stops the progress of stages in the plan.

RotationIds -> (list)

The Amazon Resource Names (ARNs) of the on-call rotations associated with the plan.

(string)

JSON Syntax:

```
{
  "Stages": [
    {
      "DurationInMinutes": integer,
      "Targets": [
        {
          "ChannelTargetInfo": {
            "ContactChannelId": "string",
            "RetryIntervalInMinutes": integer
          },
          "ContactTargetInfo": {
            "ContactId": "string",
            "IsEssential": true|false
          }
        }
        ...
      ]
    }
    ...
  ],
  "RotationIds": ["string", ...]
}
```

`--tags` (list)

Adds a tag to the target. You can only tag resources created in the first Region of your replication set.

(structure)

A container of a key-value name pair.

Key -> (string)

Name of the object key.

Value -> (string)

Value of the tag.

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

`--idempotency-token` (string)

A token ensuring that the operation is called only once with the specified details.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a contact**

The following `create-contact` example creates a contact in your environment with a blank plan. The plan can be updated after creating contact channels. Use the create-contact-channel command with the output ARN of this command. After you have created contact channels for this contact use update-contact to update the plan.

```
aws ssm-contacts create-contact \
    --alias "akuam" \
    --display-name "Akua Mansa" \
    --type PERSONAL \
    --plan '{"Stages": []}'
```

Output:

```
{
    "ContactArn": "arn:aws:ssm-contacts:us-east-2:111122223333:contact/akuam"
}
```

For more information, see [Contacts](https://docs.aws.amazon.com/incident-manager/latest/userguide/contacts.html) in the *Incident Manager User Guide*.

## Output

ContactArn -> (string)

The Amazon Resource Name (ARN) of the created contact or escalation plan.