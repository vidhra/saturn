# update-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/update-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [chime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/chime/index.html#cli-aws-chime) ]

# update-user

## Description

Updates user details for a specified user ID. Currently, only `LicenseType` updates are supported for this action.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/chime-2018-05-01/UpdateUser)

## Synopsis

```
update-user
--account-id <value>
--user-id <value>
[--license-type <value>]
[--user-type <value>]
[--alexa-for-business-metadata <value>]
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

`--account-id` (string)

The Amazon Chime account ID.

`--user-id` (string)

The user ID.

`--license-type` (string)

The user license type to update. This must be a supported license type for the Amazon Chime account that the user belongs to.

Possible values:

- `Basic`
- `Plus`
- `Pro`
- `ProTrial`

`--user-type` (string)

The user type.

Possible values:

- `PrivateUser`
- `SharedDevice`

`--alexa-for-business-metadata` (structure)

The Alexa for Business metadata.

IsAlexaForBusinessEnabled -> (boolean)

Starts or stops Alexa for Business.

AlexaForBusinessRoomArn -> (string)

The ARN of the room resource.

Shorthand Syntax:

```
IsAlexaForBusinessEnabled=boolean,AlexaForBusinessRoomArn=string
```

JSON Syntax:

```
{
  "IsAlexaForBusinessEnabled": true|false,
  "AlexaForBusinessRoomArn": "string"
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To update user details**

This example updates the specified details for the specified user.

Command:

```
aws chime update-user \
    --account-id a1b2c3d4-5678-90ab-cdef-11111EXAMPLE \
    --user-id a1b2c3d4-5678-90ab-cdef-22222EXAMPLE \
    --license-type "Basic"
```

Output:

```
{
    "User": {
        "UserId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE"
    }
}
```

## Output

User -> (structure)

The updated user details.

UserId -> (string)

The user ID.

AccountId -> (string)

The Amazon Chime account ID.

PrimaryEmail -> (string)

The primary email address of the user.

PrimaryProvisionedNumber -> (string)

The primary phone number associated with the user.

DisplayName -> (string)

The display name of the user.

LicenseType -> (string)

The license type for the user.

UserType -> (string)

The user type.

UserRegistrationStatus -> (string)

The user registration status.

UserInvitationStatus -> (string)

The user invite status.

RegisteredOn -> (timestamp)

Date and time when the user is registered, in ISO 8601 format.

InvitedOn -> (timestamp)

Date and time when the user is invited to the Amazon Chime account, in ISO 8601 format.

AlexaForBusinessMetadata -> (structure)

The Alexa for Business metadata.

IsAlexaForBusinessEnabled -> (boolean)

Starts or stops Alexa for Business.

AlexaForBusinessRoomArn -> (string)

The ARN of the room resource.

PersonalPIN -> (string)

The userâs personal meeting PIN.