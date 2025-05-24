# create-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [connect](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/index.html#cli-aws-connect) ]

# create-user

## Description

Creates a user account for the specified Amazon Connect instance.

### Warning

Certain [UserIdentityInfo](https://docs.aws.amazon.com/connect/latest/APIReference/API_UserIdentityInfo.html) parameters are required in some situations. For example, `Email` is required if you are using SAML for identity management. `FirstName` and `LastName` are required if you are using Amazon Connect or SAML for identity management.

For information about how to create users using the Amazon Connect admin website, see [Add Users](https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html) in the *Amazon Connect Administrator Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/connect-2017-08-08/CreateUser)

## Synopsis

```
create-user
--username <value>
[--password <value>]
[--identity-info <value>]
--phone-config <value>
[--directory-user-id <value>]
--security-profile-ids <value>
--routing-profile-id <value>
[--hierarchy-group-id <value>]
--instance-id <value>
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

`--username` (string)

The user name for the account. For instances not using SAML for identity management, the user name can include up to 20 characters. If you are using SAML for identity management, the user name can include up to 64 characters from [[a-zA-Z0-9_](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/connect/create-user.html#id1)-.@]+.

Username can include @ only if used in an email format. For example:

- Correct: testuser
- Correct: [testuser@example.com](mailto:testuser%40example.com)
- Incorrect: [testuser@example](mailto:testuser%40example)

`--password` (string)

The password for the user account. A password is required if you are using Amazon Connect for identity management. Otherwise, it is an error to include a password.

`--identity-info` (structure)

The information about the identity of the user.

FirstName -> (string)

The first name. This is required if you are using Amazon Connect or SAML for identity management. Inputs must be in Unicode Normalization Form C (NFC). Text containing characters in a non-NFC form (for example, decomposed characters or combining marks) are not accepted.

LastName -> (string)

The last name. This is required if you are using Amazon Connect or SAML for identity management. Inputs must be in Unicode Normalization Form C (NFC). Text containing characters in a non-NFC form (for example, decomposed characters or combining marks) are not accepted.

Email -> (string)

The email address. If you are using SAML for identity management and include this parameter, an error is returned.

SecondaryEmail -> (string)

The userâs secondary email address. If you provide a secondary email, the user receives email notifications - other than password reset notifications - to this email address instead of to their primary email address.

Pattern: `(?=^.{0,265}$)[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,63}`

Mobile -> (string)

The userâs mobile number.

Shorthand Syntax:

```
FirstName=string,LastName=string,Email=string,SecondaryEmail=string,Mobile=string
```

JSON Syntax:

```
{
  "FirstName": "string",
  "LastName": "string",
  "Email": "string",
  "SecondaryEmail": "string",
  "Mobile": "string"
}
```

`--phone-config` (structure)

The phone settings for the user.

PhoneType -> (string)

The phone type.

AutoAccept -> (boolean)

The Auto accept setting.

AfterContactWorkTimeLimit -> (integer)

The After Call Work (ACW) timeout setting, in seconds. This parameter has a minimum value of 0 and a maximum value of 2,000,000 seconds (24 days). Enter 0 if you donât want to allocate a specific amount of ACW time. It essentially means an indefinite amount of time. When the conversation ends, ACW starts; the agent must choose Close contact to end ACW.

### Note

When returned by a `SearchUsers` call, `AfterContactWorkTimeLimit` is returned in milliseconds.

DeskPhoneNumber -> (string)

The phone number for the userâs desk phone.

Shorthand Syntax:

```
PhoneType=string,AutoAccept=boolean,AfterContactWorkTimeLimit=integer,DeskPhoneNumber=string
```

JSON Syntax:

```
{
  "PhoneType": "SOFT_PHONE"|"DESK_PHONE",
  "AutoAccept": true|false,
  "AfterContactWorkTimeLimit": integer,
  "DeskPhoneNumber": "string"
}
```

`--directory-user-id` (string)

The identifier of the user account in the directory used for identity management. If Amazon Connect cannot access the directory, you can specify this identifier to authenticate users. If you include the identifier, we assume that Amazon Connect cannot access the directory. Otherwise, the identity information is used to authenticate users from your directory.

This parameter is required if you are using an existing directory for identity management in Amazon Connect when Amazon Connect cannot access your directory to authenticate users. If you are using SAML for identity management and include this parameter, an error is returned.

`--security-profile-ids` (list)

The identifier of the security profile for the user.

(string)

Syntax:

```
"string" "string" ...
```

`--routing-profile-id` (string)

The identifier of the routing profile for the user.

`--hierarchy-group-id` (string)

The identifier of the hierarchy group for the user.

`--instance-id` (string)

The identifier of the Amazon Connect instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a user**

The following `create-user` example adds a user with the specified attributes to the specified Amazon Connect instance.

```
aws connect create-user \
    --username Mary \
    --password Pass@Word1 \
    --identity-info FirstName=Mary,LastName=Major \
    --phone-config PhoneType=DESK_PHONE,AutoAccept=true,AfterContactWorkTimeLimit=60,DeskPhoneNumber=+15555551212 \
    --security-profile-id 12345678-1111-2222-aaaa-a1b2c3d4f5g7 \
    --routing-profile-id 87654321-9999-3434-abcd-x1y2z3a1b2c3 \
    --instance-id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111
```

Output:

```
{
    "UserId": "87654321-2222-1234-1234-111234567891",
    "UserArn": "arn:aws:connect:us-west-2:123456789012:instance/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111/agent/87654321-2222-1234-1234-111234567891"
}
```

For more information, see [Add Users](https://docs.aws.amazon.com/connect/latest/adminguide/user-management.html) in the *Amazon Connect Administrator Guide*.

## Output

UserId -> (string)

The identifier of the user account.

UserArn -> (string)

The Amazon Resource Name (ARN) of the user account.