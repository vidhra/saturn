# merge-profilesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/merge-profiles.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/merge-profiles.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [customer-profiles](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/customer-profiles/index.html#cli-aws-customer-profiles) ]

# merge-profiles

## Description

Runs an AWS Lambda job that does the following:

- All the profileKeys in the `ProfileToBeMerged` will be moved to the main profile.
- All the objects in the `ProfileToBeMerged` will be moved to the main profile.
- All the `ProfileToBeMerged` will be deleted at the end.
- All the profileKeys in the `ProfileIdsToBeMerged` will be moved to the main profile.
- Standard fields are merged as follows:
- Fields are always âunionâ-ed if there are no conflicts in standard fields or attributeKeys.
- When there are conflicting fields:
- If no `SourceProfileIds` entry is specified, the main Profile value is always taken.
- If a `SourceProfileIds` entry is specified, the specified profileId is always taken, even if it is a NULL value.

You can use MergeProfiles together with [GetMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html) , which returns potentially matching profiles, or use it with the results of another matching system. After profiles have been merged, they cannot be separated (unmerged).

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/customer-profiles-2020-08-15/MergeProfiles)

## Synopsis

```
merge-profiles
--domain-name <value>
--main-profile-id <value>
--profile-ids-to-be-merged <value>
[--field-source-profile-ids <value>]
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

`--main-profile-id` (string)

The identifier of the profile to be taken.

`--profile-ids-to-be-merged` (list)

The identifier of the profile to be merged into MainProfileId.

(string)

Syntax:

```
"string" "string" ...
```

`--field-source-profile-ids` (structure)

The identifiers of the fields in the profile that has the information you want to apply to the merge. For example, say you want to merge EmailAddress from Profile1 into MainProfile. This would be the identifier of the EmailAddress field in Profile1.

AccountNumber -> (string)

A unique identifier for the account number field to be merged.

AdditionalInformation -> (string)

A unique identifier for the additional information field to be merged.

PartyType -> (string)

A unique identifier for the party type field to be merged.

BusinessName -> (string)

A unique identifier for the business name field to be merged.

FirstName -> (string)

A unique identifier for the first name field to be merged.

MiddleName -> (string)

A unique identifier for the middle name field to be merged.

LastName -> (string)

A unique identifier for the last name field to be merged.

BirthDate -> (string)

A unique identifier for the birthdate field to be merged.

Gender -> (string)

A unique identifier for the gender field to be merged.

PhoneNumber -> (string)

A unique identifier for the phone number field to be merged.

MobilePhoneNumber -> (string)

A unique identifier for the mobile phone number field to be merged.

HomePhoneNumber -> (string)

A unique identifier for the home phone number field to be merged.

BusinessPhoneNumber -> (string)

A unique identifier for the business phone number field to be merged.

EmailAddress -> (string)

A unique identifier for the email address field to be merged.

PersonalEmailAddress -> (string)

A unique identifier for the personal email address field to be merged.

BusinessEmailAddress -> (string)

A unique identifier for the party type field to be merged.

Address -> (string)

A unique identifier for the party type field to be merged.

ShippingAddress -> (string)

A unique identifier for the shipping address field to be merged.

MailingAddress -> (string)

A unique identifier for the mailing address field to be merged.

BillingAddress -> (string)

A unique identifier for the billing type field to be merged.

Attributes -> (map)

A unique identifier for the attributes field to be merged.

key -> (string)

value -> (string)

Shorthand Syntax:

```
AccountNumber=string,AdditionalInformation=string,PartyType=string,BusinessName=string,FirstName=string,MiddleName=string,LastName=string,BirthDate=string,Gender=string,PhoneNumber=string,MobilePhoneNumber=string,HomePhoneNumber=string,BusinessPhoneNumber=string,EmailAddress=string,PersonalEmailAddress=string,BusinessEmailAddress=string,Address=string,ShippingAddress=string,MailingAddress=string,BillingAddress=string,Attributes={KeyName1=string,KeyName2=string}
```

JSON Syntax:

```
{
  "AccountNumber": "string",
  "AdditionalInformation": "string",
  "PartyType": "string",
  "BusinessName": "string",
  "FirstName": "string",
  "MiddleName": "string",
  "LastName": "string",
  "BirthDate": "string",
  "Gender": "string",
  "PhoneNumber": "string",
  "MobilePhoneNumber": "string",
  "HomePhoneNumber": "string",
  "BusinessPhoneNumber": "string",
  "EmailAddress": "string",
  "PersonalEmailAddress": "string",
  "BusinessEmailAddress": "string",
  "Address": "string",
  "ShippingAddress": "string",
  "MailingAddress": "string",
  "BillingAddress": "string",
  "Attributes": {"string": "string"
    ...}
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

Message -> (string)

A message that indicates the merge request is complete.