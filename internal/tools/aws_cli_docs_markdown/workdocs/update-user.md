# update-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/update-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workdocs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/index.html#cli-aws-workdocs) ]

# update-user

## Description

Updates the specified attributes of the specified user, and grants or revokes administrative privileges to the Amazon WorkDocs site.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/UpdateUser)

## Synopsis

```
update-user
[--authentication-token <value>]
--user-id <value>
[--given-name <value>]
[--surname <value>]
[--type <value>]
[--storage-rule <value>]
[--time-zone-id <value>]
[--locale <value>]
[--grant-poweruser-privileges <value>]
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

`--authentication-token` (string)

Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.

`--user-id` (string)

The ID of the user.

`--given-name` (string)

The given name of the user.

`--surname` (string)

The surname of the user.

`--type` (string)

The type of the user.

Possible values:

- `USER`
- `ADMIN`
- `POWERUSER`
- `MINIMALUSER`
- `WORKSPACESUSER`

`--storage-rule` (structure)

The amount of storage for the user.

StorageAllocatedInBytes -> (long)

The amount of storage allocated, in bytes.

StorageType -> (string)

The type of storage.

Shorthand Syntax:

```
StorageAllocatedInBytes=long,StorageType=string
```

JSON Syntax:

```
{
  "StorageAllocatedInBytes": long,
  "StorageType": "UNLIMITED"|"QUOTA"
}
```

`--time-zone-id` (string)

The time zone ID of the user.

`--locale` (string)

The locale of the user.

Possible values:

- `en`
- `fr`
- `ko`
- `de`
- `es`
- `ja`
- `ru`
- `zh_CN`
- `zh_TW`
- `pt_BR`
- `default`

`--grant-poweruser-privileges` (string)

Boolean value to determine whether the user is granted Power user privileges.

Possible values:

- `TRUE`
- `FALSE`

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

**To update a user**

This example updates the time zone for the specified user.

Command:

```
aws workdocs update-user --user-id "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c" --time-zone-id "America/Los_Angeles"
```

Output:

```
{
  "User": {
      "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c",
      "Username": "exampleUser",
      "EmailAddress": "exampleUser@site.awsapps.com",
      "GivenName": "Example",
      "Surname": "User",
      "OrganizationId": "d-926726012c",
      "RootFolderId": "c5eceb5e1a2d1d460c9d1af8330ae117fc8d39bb1d3ed6acd0992d5ff192d986",
      "RecycleBinFolderId": "6ca20102926ad15f04b1d248d6d6e44f2449944eda5c758f9a1e9df6a6b7fa66",
      "Status": "ACTIVE",
      "Type": "USER",
      "TimeZoneId": "America/Los_Angeles",
      "Storage": {
          "StorageUtilizedInBytes": 0,
          "StorageRule": {
              "StorageAllocatedInBytes": 53687091200,
              "StorageType": "QUOTA"
          }
      }
  }
}
```

## Output

User -> (structure)

The user information.

Id -> (string)

The ID of the user.

Username -> (string)

The login name of the user.

EmailAddress -> (string)

The email address of the user.

GivenName -> (string)

The given name of the user.

Surname -> (string)

The surname of the user.

OrganizationId -> (string)

The ID of the organization.

RootFolderId -> (string)

The ID of the root folder.

RecycleBinFolderId -> (string)

The ID of the recycle bin folder.

Status -> (string)

The status of the user.

Type -> (string)

The type of user.

CreatedTimestamp -> (timestamp)

The time when the user was created.

ModifiedTimestamp -> (timestamp)

The time when the user was modified.

TimeZoneId -> (string)

The time zone ID of the user.

Locale -> (string)

The locale of the user.

Storage -> (structure)

The storage for the user.

StorageUtilizedInBytes -> (long)

The amount of storage used, in bytes.

StorageRule -> (structure)

The storage for a user.

StorageAllocatedInBytes -> (long)

The amount of storage allocated, in bytes.

StorageType -> (string)

The type of storage.