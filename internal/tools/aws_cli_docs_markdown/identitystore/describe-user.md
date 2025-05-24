# describe-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/describe-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/describe-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [identitystore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/index.html#cli-aws-identitystore) ]

# describe-user

## Description

Retrieves the user metadata and attributes from the `UserId` in an identity store.

### Note

If you have administrator access to a member account, you can use this API from the member account. Read about [member accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html) in the *Organizations User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/identitystore-2020-06-15/DescribeUser)

## Synopsis

```
describe-user
--identity-store-id <value>
--user-id <value>
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

`--identity-store-id` (string)

The globally unique identifier for the identity store, such as `d-1234567890` . In this example, `d-` is a fixed prefix, and `1234567890` is a randomly generated string that contains numbers and lower case letters. This value is generated at the time that a new identity store is created.

`--user-id` (string)

The identifier for a user in the identity store.

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

UserName -> (string)

A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store.

UserId -> (string)

The identifier for a user in the identity store.

ExternalIds -> (list)

A list of `ExternalId` objects that contains the identifiers issued to this resource by an external identity provider.

(structure)

The identifier issued to this resource by an external identity provider.

Issuer -> (string)

The issuer for an external identifier.

Id -> (string)

The identifier issued to this resource by an external identity provider.

Name -> (structure)

The name of the user.

Formatted -> (string)

A string containing a formatted version of the name for display.

FamilyName -> (string)

The family name of the user.

GivenName -> (string)

The given name of the user.

MiddleName -> (string)

The middle name of the user.

HonorificPrefix -> (string)

The honorific prefix of the user. For example, âDr.â

HonorificSuffix -> (string)

The honorific suffix of the user. For example, âM.D.â

DisplayName -> (string)

The display name of the user.

NickName -> (string)

An alternative descriptive name for the user.

ProfileUrl -> (string)

A URL link for the userâs profile.

Emails -> (list)

The email address of the user.

(structure)

The email address associated with the user.

Value -> (string)

A string containing an email address. For example, â[johndoe@amazon.com](mailto:johndoe%40amazon.com).â

Type -> (string)

A string representing the type of address. For example, âWork.â

Primary -> (boolean)

A Boolean value representing whether this is the primary email address for the associated resource.

Addresses -> (list)

The physical address of the user.

(structure)

The address associated with the specified user.

StreetAddress -> (string)

The street of the address.

Locality -> (string)

A string of the address locality.

Region -> (string)

The region of the address.

PostalCode -> (string)

The postal code of the address.

Country -> (string)

The country of the address.

Formatted -> (string)

A string containing a formatted version of the address for display.

Type -> (string)

A string representing the type of address. For example, âHome.â

Primary -> (boolean)

A Boolean value representing whether this is the primary address for the associated resource.

PhoneNumbers -> (list)

A list of `PhoneNumber` objects associated with a user.

(structure)

The phone number associated with the user.

Value -> (string)

A string containing a phone number. For example, â8675309â or â+1 (800) 123-4567â.

Type -> (string)

A string representing the type of a phone number. For example, âMobile.â

Primary -> (boolean)

A Boolean value representing whether this is the primary phone number for the associated resource.

UserType -> (string)

A string indicating the type of user.

Title -> (string)

A string containing the title of the user.

PreferredLanguage -> (string)

The preferred language of the user.

Locale -> (string)

A string containing the geographical region or location of the user.

Timezone -> (string)

The time zone for a user.

IdentityStoreId -> (string)

The globally unique identifier for the identity store.