# update-contactÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-contact.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/update-contact.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# update-contact

## Description

This API is in preview release for Amazon Connect and is subject to change.

Adds or updates user-defined contact information associated with the specified contact. At least one field to be updated must be present in the request.

### Warning

You can add or update user-defined contact information for both ongoing and completed contacts.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/UpdateContact)

## Synopsis

```
update-contact
--instance-id <value>
--contact-id <value>
[--name <value>]
[--description <value>]
[--references <value>]
[--segment-attributes <value>]
[--queue-info <value>]
[--user-info <value>]
[--customer-endpoint <value>]
[--system-endpoint <value>]
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

`--contact-id` (string)

The identifier of the contact. This is the identifier of the contact associated with the first interaction with your contact center.

`--name` (string)

The name of the contact.

`--description` (string)

The description of the contact.

`--references` (map)

Well-formed data on contact, shown to agents on Contact Control Panel (CCP).

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

`--segment-attributes` (map)

A set of system defined key-value pairs stored on individual contact segments (unique contact ID) using an attribute map. The attributes are standard Amazon Connect attributes. They can be accessed in flows.

Attribute keys can include only alphanumeric, -, and _.

This field can be used to show channel subtype, such as `connect:Guide` .

Currently Contact Expiry is the only segment attribute which can be updated by using the UpdateContact API.

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

`--queue-info` (structure)

Information about the queue associated with a contact. This parameter can only be updated for external audio contacts. It is used when you integrate third-party systems with Contact Lens for analytics. For more information, see [Amazon Connect Contact Lens integration](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html) in the *Amazon Connect Administrator Guide* .

Id -> (string)

The identifier of the queue.

Shorthand Syntax:

```
Id=string
```

JSON Syntax:

```
{
  "Id": "string"
}
```

`--user-info` (structure)

Information about the agent associated with a contact. This parameter can only be updated for external audio contacts. It is used when you integrate third-party systems with Contact Lens for analytics. For more information, see [Amazon Connect Contact Lens integration](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html) in the *Amazon Connect Administrator Guide* .

UserId -> (string)

The user identifier for the contact.

Shorthand Syntax:

```
UserId=string
```

JSON Syntax:

```
{
  "UserId": "string"
}
```

`--customer-endpoint` (structure)

The endpoint of the customer for which the contact was initiated. For external audio contacts, this is usually the end customerâs phone number. This value can only be updated for external audio contacts. For more information, see [Amazon Connect Contact Lens integration](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html) in the *Amazon Connect Administrator Guide* .

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

`--system-endpoint` (structure)

External system endpoint for the contact was initiated. For external audio contacts, this is the phone number of the external system such as the contact center. This value can only be updated for external audio contacts. For more information, see [Amazon Connect Contact Lens integration](https://docs.aws.amazon.com/connect/latest/adminguide/contact-lens-integration.html) in the *Amazon Connect Administrator Guide* .

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