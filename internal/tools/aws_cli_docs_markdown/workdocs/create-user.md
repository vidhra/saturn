# create-userÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-user.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/create-user.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workdocs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workdocs/index.html#cli-aws-workdocs) ]

# create-user

## Description

Creates a user in a Simple AD or Microsoft AD directory. The status of a newly created user is âACTIVEâ. New users can access Amazon WorkDocs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workdocs-2016-05-01/CreateUser)

## Synopsis

```
create-user
[--organization-id <value>]
--username <value>
[--email-address <value>]
--given-name <value>
--surname <value>
--password <value>
[--time-zone-id <value>]
[--storage-rule <value>]
[--authentication-token <value>]
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

`--organization-id` (string)

The ID of the organization.

`--username` (string)

The login name of the user.

`--email-address` (string)

The email address of the user.

`--given-name` (string)

The given name of the user.

`--surname` (string)

The surname of the user.

`--password` (string)

The password of the user.

`--time-zone-id` (string)

The time zone ID of the user.

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

`--authentication-token` (string)

Amazon WorkDocs authentication token. Not required when using Amazon Web Services administrator credentials to access the API.

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

**To create a new user**

This example creates a new user in a Simple AD or Microsoft AD directory.

Command:

```
aws workdocs create-user --organization-id d-926726012c --username exampleUser2 --email-address exampleUser2@site.awsapps.com --given-name example2Name --surname example2Surname --password examplePa$$w0rd
```

Output:

```
{
  "User": {
      "Id": "S-1-1-11-1111111111-2222222222-3333333333-3333&d-926726012c",
      "Username": "exampleUser2",
      "EmailAddress": "exampleUser2@site.awsapps.com",
      "GivenName": "example2Name",
      "Surname": "example2Surname",
      "OrganizationId": "d-926726012c",
      "RootFolderId": "35b886cb17198cbd547655e58b025dff0cf34aaed638be52009567e23dc67390",
      "RecycleBinFolderId": "9858c3e9ed4c2460dde9aadb4c69fde998070dd46e5e985bd08ec6169ea249ff",
      "Status": "ACTIVE",
      "Type": "MINIMALUSER",
      "CreatedTimestamp": 1535478836.584,
      "ModifiedTimestamp": 1535478836.584,
      "Storage": {
          "StorageUtilizedInBytes": 0,
          "StorageRule": {
              "StorageAllocatedInBytes": 0,
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