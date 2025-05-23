# create-directoryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-directory.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/create-directory.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ds](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/index.html#cli-aws-ds) ]

# create-directory

## Description

Creates a Simple AD directory. For more information, see [Simple Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_simple_ad.html) in the *Directory Service Admin Guide* .

Before you call `CreateDirectory` , ensure that all of the required permissions have been explicitly granted through a policy. For details about what permissions are required to run the `CreateDirectory` operation, see [Directory Service API Permissions: Actions, Resources, and Conditions Reference](http://docs.aws.amazon.com/directoryservice/latest/admin-guide/UsingWithDS_IAM_ResourcePermissions.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ds-2015-04-16/CreateDirectory)

## Synopsis

```
create-directory
--name <value>
[--short-name <value>]
--password <value>
[--description <value>]
--size <value>
[--vpc-settings <value>]
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

`--name` (string)

The fully qualified name for the directory, such as `corp.example.com` .

`--short-name` (string)

The NetBIOS name of the directory, such as `CORP` .

`--password` (string)

The password for the directory administrator. The directory creation process creates a directory administrator account with the user name `Administrator` and this password.

If you need to change the password for the administrator account, you can use the  ResetUserPassword API call.

The regex pattern for this string is made up of the following conditions:

- Length (?=^.{8,64}$) â Must be between 8 and 64 characters

AND any 3 of the following password complexity rules required by Active Directory:

- Numbers and upper case and lowercase (?=.*d)(?=.*[A-Z])(?=.*[a-z])
- Numbers and special characters and lower case (?=.*d)(?=.*[^A-Za-z0-9s])(?=.*[a-z])
- Special characters and upper case and lower case (?=.*[^A-Za-z0-9s])(?=.*[A-Z])(?=.*[a-z])
- Numbers and upper case and special characters (?=.*d)(?=.*[A-Z])(?=.*[^A-Za-z0-9s])

For additional information about how Active Directory passwords are enforced, see [Password must meet complexity requirements](https://docs.microsoft.com/en-us/windows/security/threat-protection/security-policy-settings/password-must-meet-complexity-requirements) on the Microsoft website.

`--description` (string)

A description for the directory.

`--size` (string)

The size of the directory.

Possible values:

- `Small`
- `Large`

`--vpc-settings` (structure)

A  DirectoryVpcSettings object that contains additional information for the operation.

VpcId -> (string)

The identifier of the VPC in which to create the directory.

SubnetIds -> (list)

The identifiers of the subnets for the directory servers. The two subnets must be in different Availability Zones. Directory Service creates a directory server and a DNS server in each of these subnets.

(string)

Shorthand Syntax:

```
VpcId=string,SubnetIds=string,string
```

JSON Syntax:

```
{
  "VpcId": "string",
  "SubnetIds": ["string", ...]
}
```

`--tags` (list)

The tags to be assigned to the Simple AD directory.

(structure)

Metadata assigned to a directory consisting of a key-value pair.

Key -> (string)

Required name of the tag. The string value can be Unicode characters and cannot be prefixed with âaws:â. The string can contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â, â:â, â@â(Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

Value -> (string)

The optional value of the tag. The string value can be Unicode characters. The string can contain only the set of Unicode letters, digits, white-space, â_â, â.â, â/â, â=â, â+â, â-â, â:â, â@â (Java regex: â^([\p{L}\p{Z}\p{N}_.:/=+\-]*)$â).

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
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

DirectoryId -> (string)

The identifier of the directory that was created.