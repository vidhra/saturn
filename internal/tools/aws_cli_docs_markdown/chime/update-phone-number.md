# update-phone-numberÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-phone-number.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-phone-number.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/index.html#cli-aws-chime) ]

# update-phone-number

## Description

Updates phone number details, such as product type or calling name, for the specified phone number ID. You can update one phone number detail at a time. For example, you can update either the product type or the calling name in one action.

For toll-free numbers, you cannot use the Amazon Chime Business Calling product type. For numbers outside the U.S., you must use the Amazon Chime SIP Media Application Dial-In product type.

Updates to outbound calling names can take 72 hours to complete. Pending updates to outbound calling names must be complete before you can request another update.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdatePhoneNumber)

## Synopsis

```
update-phone-number
--phone-number-id <value>
[--product-type <value>]
[--calling-name <value>]
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

`--phone-number-id` (string)

The phone number ID.

`--product-type` (string)

The product type.

Possible values:

- `BusinessCalling`
- `VoiceConnector`
- `SipMediaApplicationDialIn`

`--calling-name` (string)

The outbound calling name associated with the phone number.

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

**Example 1: To update the product type for a phone number**

The following `update-phone-number` example updates the specified phone numberâs product type.

```
aws chime update-phone-number \
    --phone-number-id "+12065550100" \
    --product-type "BusinessCalling"
```

Output:

```
{
    "PhoneNumber": {
        "PhoneNumberId": "%2B12065550100",
        "E164PhoneNumber": "+12065550100",
        "Type": "Local",
        "ProductType": "BusinessCalling",
        "Status": "Unassigned",
        "Capabilities": {
            "InboundCall": true,
            "OutboundCall": true,
            "InboundSMS": true,
            "OutboundSMS": true,
            "InboundMMS": true,
            "OutboundMMS": true
        },
        "Associations": [],
        "CallingName": "phonenumber1",
        "CreatedTimestamp": "2019-08-09T21:35:21.445Z",
        "UpdatedTimestamp": "2019-08-12T21:44:07.591Z"
    }
}
```

**Example 2: To update the outbound calling name for a phone number**

The following `update-phone-number` example updates the outbound calling name for the specified phone number.

**aws chime update-phone-number**:
âphone-number-id â+12065550100â âcalling-name âphonenumber2â

Output:

```
{
    "PhoneNumber": {
        "PhoneNumberId": "%2B12065550100",
        "E164PhoneNumber": "+12065550100",
        "Type": "Local",
        "ProductType": "BusinessCalling",
        "Status": "Unassigned",
        "Capabilities": {
            "InboundCall": true,
            "OutboundCall": true,
            "InboundSMS": true,
            "OutboundSMS": true,
            "InboundMMS": true,
            "OutboundMMS": true
        },
        "Associations": [],
        "CallingName": "phonenumber2",
        "CreatedTimestamp": "2019-08-09T21:35:21.445Z",
        "UpdatedTimestamp": "2019-08-12T21:44:07.591Z"
    }
}
```

For more information, see [Working with Phone Numbers](https://docs.aws.amazon.com/chime/latest/ag/phone-numbers.html) in the *Amazon Chime Administration Guide*.

## Output

PhoneNumber -> (structure)

The updated phone number details.

PhoneNumberId -> (string)

The phone number ID.

E164PhoneNumber -> (string)

The phone number, in E.164 format.

Country -> (string)

The phone number country. Format: ISO 3166-1 alpha-2.

Type -> (string)

The phone number type.

ProductType -> (string)

The phone number product type.

Status -> (string)

The phone number status.

Capabilities -> (structure)

The phone number capabilities.

InboundCall -> (boolean)

Allows or denies inbound calling for the specified phone number.

OutboundCall -> (boolean)

Allows or denies outbound calling for the specified phone number.

InboundSMS -> (boolean)

Allows or denies inbound SMS messaging for the specified phone number.

OutboundSMS -> (boolean)

Allows or denies outbound SMS messaging for the specified phone number.

InboundMMS -> (boolean)

Allows or denies inbound MMS messaging for the specified phone number.

OutboundMMS -> (boolean)

Allows or denies outbound MMS messaging for the specified phone number.

Associations -> (list)

The phone number associations.

(structure)

The phone number associations, such as Amazon Chime account ID, Amazon Chime user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

Value -> (string)

Contains the ID for the entity specified in Name.

Name -> (string)

Defines the association with an Amazon Chime account ID, user ID, Amazon Chime Voice Connector ID, or Amazon Chime Voice Connector group ID.

AssociatedTimestamp -> (timestamp)

The timestamp of the phone number association, in ISO 8601 format.

CallingName -> (string)

The outbound calling name associated with the phone number.

CallingNameStatus -> (string)

The outbound calling name status.

CreatedTimestamp -> (timestamp)

The phone number creation timestamp, in ISO 8601 format.

UpdatedTimestamp -> (timestamp)

The updated phone number timestamp, in ISO 8601 format.

DeletionTimestamp -> (timestamp)

The deleted phone number timestamp, in ISO 8601 format.