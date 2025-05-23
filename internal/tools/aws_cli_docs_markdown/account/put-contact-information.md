# put-contact-informationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/account/put-contact-information.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/account/put-contact-information.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [account](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/account/index.html#cli-aws-account) ]

# put-contact-information

## Description

Updates the primary contact information of an Amazon Web Services account.

For complete details about how to use the primary contact operations, see [Update the primary and alternate contact information](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-update-contact.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/account-2021-02-01/PutContactInformation)

## Synopsis

```
put-contact-information
[--account-id <value>]
--contact-information <value>
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

Specifies the 12-digit account ID number of the Amazon Web Services account that you want to access or modify with this operation. If you donât specify this parameter, it defaults to the Amazon Web Services account of the identity used to call the operation. To use this parameter, the caller must be an identity in the [organizationâs management account](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#account) or a delegated administrator account. The specified account ID must be a member account in the same organization. The organization must have [all features enabled](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_org_support-all-features.html) , and the organization must have [trusted access](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_integrate_services.html) enabled for the Account Management service, and optionally a [delegated admin](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#delegated-admin) account assigned.

### Note

The management account canât specify its own `AccountId` . It must call the operation in standalone context by not including the `AccountId` parameter.

To call this operation on an account that is not a member of an organization, donât specify this parameter. Instead, call the operation using an identity belonging to the account whose contacts you wish to retrieve or modify.

`--contact-information` (structure)

Contains the details of the primary contact information associated with an Amazon Web Services account.

AddressLine1 -> (string)

The first line of the primary contact address.

AddressLine2 -> (string)

The second line of the primary contact address, if any.

AddressLine3 -> (string)

The third line of the primary contact address, if any.

City -> (string)

The city of the primary contact address.

CompanyName -> (string)

The name of the company associated with the primary contact information, if any.

CountryCode -> (string)

The ISO-3166 two-letter country code for the primary contact address.

DistrictOrCounty -> (string)

The district or county of the primary contact address, if any.

FullName -> (string)

The full name of the primary contact address.

PhoneNumber -> (string)

The phone number of the primary contact information. The number will be validated and, in some countries, checked for activation.

PostalCode -> (string)

The postal code of the primary contact address.

StateOrRegion -> (string)

The state or region of the primary contact address. If the mailing address is within the United States (US), the value in this field can be either a two character state code (for example, `NJ` ) or the full state name (for example, `New Jersey` ). This field is required in the following countries: `US` , `CA` , `GB` , `DE` , `JP` , `IN` , and `BR` .

WebsiteUrl -> (string)

The URL of the website associated with the primary contact information, if any.

Shorthand Syntax:

```
AddressLine1=string,AddressLine2=string,AddressLine3=string,City=string,CompanyName=string,CountryCode=string,DistrictOrCounty=string,FullName=string,PhoneNumber=string,PostalCode=string,StateOrRegion=string,WebsiteUrl=string
```

JSON Syntax:

```
{
  "AddressLine1": "string",
  "AddressLine2": "string",
  "AddressLine3": "string",
  "City": "string",
  "CompanyName": "string",
  "CountryCode": "string",
  "DistrictOrCounty": "string",
  "FullName": "string",
  "PhoneNumber": "string",
  "PostalCode": "string",
  "StateOrRegion": "string",
  "WebsiteUrl": "string"
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