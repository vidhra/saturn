# list-usersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/list-users.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/list-users.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [identitystore](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/identitystore/index.html#cli-aws-identitystore) ]

# list-users

## Description

Lists all users in the identity store. Returns a paginated list of complete `User` objects. Filtering for a `User` by the `UserName` attribute is deprecated. Instead, use the `GetUserId` API action.

### Note

If you have administrator access to a member account, you can use this API from the member account. Read about [member accounts](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_accounts_access.html) in the *Organizations User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/identitystore-2020-06-15/ListUsers)

`list-users` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Users`

## Synopsis

```
list-users
--identity-store-id <value>
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--filters` (list)

A list of `Filter` objects, which is used in the `ListUsers` and `ListGroups` requests.

(structure)

A query filter used by `ListUsers` and `ListGroups` . This filter object provides the attribute name and attribute value to search users or groups.

AttributePath -> (string)

The attribute path that is used to specify which attribute name to search. Length limit is 255 characters. For example, `UserName` is a valid attribute path for the `ListUsers` API, and `DisplayName` is a valid attribute path for the `ListGroups` API.

AttributeValue -> (string)

Represents the data for an attribute. Each attribute value is described as a name-value pair.

Shorthand Syntax:

```
AttributePath=string,AttributeValue=string ...
```

JSON Syntax:

```
[
  {
    "AttributePath": "string",
    "AttributeValue": "string"
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

Users -> (list)

A list of `User` objects in the identity store.

(structure)

A user object that contains the metadata and attributes for a specified user.

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

An object containing the name of the user.

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

A string containing the name of the user that is formatted for display when the user is referenced. For example, âJohn Doe.â

NickName -> (string)

A string containing an alternate name for the user.

ProfileUrl -> (string)

A string containing a URL that might be associated with the user.

Emails -> (list)

A list of `Email` objects containing email addresses associated with the user.

(structure)

The email address associated with the user.

Value -> (string)

A string containing an email address. For example, â[johndoe@amazon.com](mailto:johndoe%40amazon.com).â

Type -> (string)

A string representing the type of address. For example, âWork.â

Primary -> (boolean)

A Boolean value representing whether this is the primary email address for the associated resource.

Addresses -> (list)

A list of `Address` objects containing addresses associated with the user.

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

A list of `PhoneNumber` objects containing phone numbers associated with the user.

(structure)

The phone number associated with the user.

Value -> (string)

A string containing a phone number. For example, â8675309â or â+1 (800) 123-4567â.

Type -> (string)

A string representing the type of a phone number. For example, âMobile.â

Primary -> (boolean)

A Boolean value representing whether this is the primary phone number for the associated resource.

UserType -> (string)

A string indicating the type of user. Possible values are left unspecified. The value can vary based on your specific use case.

Title -> (string)

A string containing the title of the user. Possible values are left unspecified. The value can vary based on your specific use case.

PreferredLanguage -> (string)

A string containing the preferred language of the user. For example, âAmerican Englishâ or âen-us.â

Locale -> (string)

A string containing the geographical region or location of the user.

Timezone -> (string)

A string containing the time zone of the user.

IdentityStoreId -> (string)

The globally unique identifier for the identity store.

NextToken -> (string)

The pagination token used for the `ListUsers` and `ListGroups` API operations. This value is generated by the identity store service. It is returned in the API response if the total results are more than the size of one page. This token is also returned when it is used in the API request to search for the next page.