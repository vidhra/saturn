# batch-get-profileÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/batch-get-profile.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/batch-get-profile.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [customer-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/index.html#cli-aws-customer-profiles) ]

# batch-get-profile

## Description

Get a batch of profiles.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/customer-profiles-2020-08-15/BatchGetProfile)

## Synopsis

```
batch-get-profile
--domain-name <value>
--profile-ids <value>
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

`--domain-name` (string)

The unique name of the domain.

`--profile-ids` (list)

List of unique identifiers for customer profiles to retrieve.

(string)

Syntax:

```
"string" "string" ...
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

Errors -> (list)

For information about the errors that are common to all actions, see [Common Errors](https://docs.aws.amazon.com/connect/latest/APIReference/CommonErrors.html) .

(structure)

Error object describing why a specific profile failed.

Code -> (string)

Status code for why a specific profile failed.

Message -> (string)

Message describing why a specific profile failed.

ProfileId -> (string)

The profile id that failed.

Profiles -> (list)

Array of Profile Objects.

(structure)

The standard profile of a customer.

ProfileId -> (string)

The unique identifier of a customer profile.

AccountNumber -> (string)

An account number that you have given to the customer.

AdditionalInformation -> (string)

Any additional information relevant to the customerâs profile.

PartyType -> (string)

The type of profile used to describe the customer.

BusinessName -> (string)

The name of the customerâs business.

FirstName -> (string)

The customerâs first name.

MiddleName -> (string)

The customerâs middle name.

LastName -> (string)

The customerâs last name.

BirthDate -> (string)

The customerâs birth date.

Gender -> (string)

The gender with which the customer identifies.

PhoneNumber -> (string)

The customerâs phone number, which has not been specified as a mobile, home, or business number.

MobilePhoneNumber -> (string)

The customerâs mobile phone number.

HomePhoneNumber -> (string)

The customerâs home phone number.

BusinessPhoneNumber -> (string)

The customerâs home phone number.

EmailAddress -> (string)

The customerâs email address, which has not been specified as a personal or business address.

PersonalEmailAddress -> (string)

The customerâs personal email address.

BusinessEmailAddress -> (string)

The customerâs business email address.

Address -> (structure)

A generic address associated with the customer that is not mailing, shipping, or billing.

Address1 -> (string)

The first line of a customer address.

Address2 -> (string)

The second line of a customer address.

Address3 -> (string)

The third line of a customer address.

Address4 -> (string)

The fourth line of a customer address.

City -> (string)

The city in which a customer lives.

County -> (string)

The county in which a customer lives.

State -> (string)

The state in which a customer lives.

Province -> (string)

The province in which a customer lives.

Country -> (string)

The country in which a customer lives.

PostalCode -> (string)

The postal code of a customer address.

ShippingAddress -> (structure)

The customerâs shipping address.

Address1 -> (string)

The first line of a customer address.

Address2 -> (string)

The second line of a customer address.

Address3 -> (string)

The third line of a customer address.

Address4 -> (string)

The fourth line of a customer address.

City -> (string)

The city in which a customer lives.

County -> (string)

The county in which a customer lives.

State -> (string)

The state in which a customer lives.

Province -> (string)

The province in which a customer lives.

Country -> (string)

The country in which a customer lives.

PostalCode -> (string)

The postal code of a customer address.

MailingAddress -> (structure)

The customerâs mailing address.

Address1 -> (string)

The first line of a customer address.

Address2 -> (string)

The second line of a customer address.

Address3 -> (string)

The third line of a customer address.

Address4 -> (string)

The fourth line of a customer address.

City -> (string)

The city in which a customer lives.

County -> (string)

The county in which a customer lives.

State -> (string)

The state in which a customer lives.

Province -> (string)

The province in which a customer lives.

Country -> (string)

The country in which a customer lives.

PostalCode -> (string)

The postal code of a customer address.

BillingAddress -> (structure)

The customerâs billing address.

Address1 -> (string)

The first line of a customer address.

Address2 -> (string)

The second line of a customer address.

Address3 -> (string)

The third line of a customer address.

Address4 -> (string)

The fourth line of a customer address.

City -> (string)

The city in which a customer lives.

County -> (string)

The county in which a customer lives.

State -> (string)

The state in which a customer lives.

Province -> (string)

The province in which a customer lives.

Country -> (string)

The country in which a customer lives.

PostalCode -> (string)

The postal code of a customer address.

Attributes -> (map)

A key value pair of attributes of a customer profile.

key -> (string)

value -> (string)

FoundByItems -> (list)

A list of items used to find a profile returned in a [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) response. An item is a key-value(s) pair that matches an attribute in the profile.

If the optional `AdditionalSearchKeys` parameter was included in the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) request, the `FoundByItems` list should be interpreted based on the `LogicalOperator` used in the request:

- `AND` - The profile included in the response matched all of the search keys specified in the request. The `FoundByItems` will include all of the key-value(s) pairs that were specified in the request (as this is a requirement of `AND` search logic).
- `OR` - The profile included in the response matched at least one of the search keys specified in the request. The `FoundByItems` will include each of the key-value(s) pairs that the profile was found by.

The `OR` relationship is the default behavior if the `LogicalOperator` parameter is not included in the [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) request.

(structure)

A data type pair that consists of a `KeyName` and `Values` list that were used to find a profile returned in response to a [SearchProfiles](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SearchProfiles.html) request.

KeyName -> (string)

A searchable identifier of a customer profile.

Values -> (list)

A list of key values.

(string)

PartyTypeString -> (string)

An alternative to PartyType which accepts any string as input.

GenderString -> (string)

An alternative to Gender which accepts any string as input.