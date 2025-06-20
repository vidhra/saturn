# search-usersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/search-users.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/search-users.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ds-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/index.html#cli-aws-ds-data) ]

# search-users

## Description

Searches the specified directory for a user. You can find users that match the `SearchString` parameter with the value of their attributes included in the `SearchString` parameter.

This operation supports pagination with the use of the `NextToken` request and response parameters. If more results are available, the `SearchUsers.NextToken` member contains a token that you pass in the next call to `SearchUsers` . This retrieves the next set of items.

You can also specify a maximum number of return results with the `MaxResults` parameter.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/directory-service-data-2023-05-31/SearchUsers)

`search-users` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Users`

## Synopsis

```
search-users
--directory-id <value>
[--realm <value>]
--search-attributes <value>
--search-string <value>
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

`--directory-id` (string)

The identifier (ID) of the directory thatâs associated with the user.

`--realm` (string)

The domain name thatâs associated with the user.

### Note

This parameter is optional, so you can return users outside of your Managed Microsoft AD domain. When no value is defined, only your Managed Microsoft AD users are returned.

This value is case insensitive.

`--search-attributes` (list)

One or more data attributes that are used to search for a user. For a list of supported attributes, see [Directory Service Data Attributes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html) .

(string)

Syntax:

```
"string" "string" ...
```

`--search-string` (string)

The attribute value that you want to search for.

### Note

Wildcard `(*)` searches arenât supported. For a list of supported attributes, see [Directory Service Data Attributes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html) .

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To search for a user in a directory**

The following `search-users` example searches for the specified user in the specified directory.

```
aws ds-data search-users \
    --directory-id d-1234567890 \
    --search-attributes 'SamAccountName' \
    --Search-string 'john.doe'
```

Output:

```
{
    "Users": [
        {
            "Enabled": true,
            "SAMAccountName": "john.doe",
            "SID": "S-1-2-34-5678901234-5678901234-5678910123-4567"
        }
    ],
    "DirectoryId": "d-1234567890",
    "Realm": "corp.example.com"
}
```

For more information, see [Viewing and updating an AWS Managed Microsoft AD user](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_update_user.html) in the *AWS Directory Service Administration Guide*.

## Output

DirectoryId -> (string)

The identifier (ID) of the directory where the address block is added.

NextToken -> (string)

An encoded paging token for paginated calls that can be passed back to retrieve the next page.

Realm -> (string)

The domain thatâs associated with the user.

Users -> (list)

The user information that the request returns.

(structure)

A user object that contains identifying information and attributes for a specified user.

DistinguishedName -> (string)

The [distinguished name](https://learn.microsoft.com/en-us/windows/win32/ad/object-names-and-identities#distinguished-name) of the object.

EmailAddress -> (string)

The email address of the user.

Enabled -> (boolean)

Indicates whether the user account is active.

GivenName -> (string)

The first name of the user.

OtherAttributes -> (map)

An expression that includes one or more attributes, data types, and values of a user.

key -> (string)

value -> (tagged union structure)

The data type for an attribute. Each attribute value is described as a name-value pair. The name is the AD schema name, and the value is the data itself. For a list of supported attributes, see [Directory Service Data Attributes](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ad_data_attributes.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `BOOL`, `N`, `S`, `SS`.

BOOL -> (boolean)

Indicates that the attribute type value is a boolean. For example:

`"BOOL": true`

N -> (long)

Indicates that the attribute type value is a number. For example:

`"N": "16"`

S -> (string)

Indicates that the attribute type value is a string. For example:

`"S": "S Group"`

SS -> (list)

Indicates that the attribute type value is a string set. For example:

`"SS": ["sample_service_class/host.sample.com:1234/sample_service_name_1", "sample_service_class/host.sample.com:1234/sample_service_name_2"]`

(string)

SAMAccountName -> (string)

The name of the user.

SID -> (string)

The unique security identifier (SID) of the user.

Surname -> (string)

The last name of the user.

UserPrincipalName -> (string)

The UPN that is an internet-style login name for a user and based on the internet standard [RFC 822](https://datatracker.ietf.org/doc/html/rfc822) . The UPN is shorter than the distinguished name and easier to remember.