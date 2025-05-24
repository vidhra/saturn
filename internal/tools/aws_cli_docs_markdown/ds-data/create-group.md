# create-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/create-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/create-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ds-data](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds-data/index.html#cli-aws-ds-data) ]

# create-group

## Description

Creates a new group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/directory-service-data-2023-05-31/CreateGroup)

## Synopsis

```
create-group
[--client-token <value>]
--directory-id <value>
[--group-scope <value>]
[--group-type <value>]
[--other-attributes <value>]
--sam-account-name <value>
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

`--client-token` (string)

A unique and case-sensitive identifier that you provide to make sure the idempotency of the request, so multiple identical calls have the same effect as one single call.

A client token is valid for 8 hours after the first request that uses it completes. After 8 hours, any request with the same client token is treated as a new request. If the request succeeds, any future uses of that token will be idempotent for another 8 hours.

If you submit a request with the same client token but change one of the other parameters within the 8-hour idempotency window, Directory Service Data returns an `ConflictException` .

### Note

This parameter is optional when using the CLI or SDK.

`--directory-id` (string)

The identifier (ID) of the directory thatâs associated with the group.

`--group-scope` (string)

The scope of the AD group. For details, see [Active Directory security group scope](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#group-scope) .

Possible values:

- `DomainLocal`
- `Global`
- `Universal`
- `BuiltinLocal`

`--group-type` (string)

The AD group type. For details, see [Active Directory security group type](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/manage/understand-security-groups#how-active-directory-security-groups-work) .

Possible values:

- `Distribution`
- `Security`

`--other-attributes` (map)

An expression that defines one or more attributes with the data type and value of each attribute.

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

Shorthand Syntax:

```
KeyName1=BOOL=boolean,N=long,S=string,SS=string,string,KeyName2=BOOL=boolean,N=long,S=string,SS=string,string
```

JSON Syntax:

```
{"string": {
      "BOOL": true|false,
      "N": long,
      "S": "string",
      "SS": ["string", ...]
    }
  ...}
```

`--sam-account-name` (string)

The name of the group.

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

**To list the available widgets**

The following `create-group` example creates a group in a specified directory.

```
aws ds-data create-group \
    --directory-id d-1234567890 \
    --sam-account-name "sales"
```

Output:

```
{
    "DirectoryId": "d-1234567890",
    "SAMAccountName": "sales",
    "SID": "S-1-2-34-5567891234-5678912345-67891234567-8912"
}
```

For more information, see [Creating an AWS Managed Microsoft AD group](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_create_group.html) in the *AWS Directory Service Administration Guide*.

## Output

DirectoryId -> (string)

The identifier (ID) of the directory thatâs associated with the group.

SAMAccountName -> (string)

The name of the group.

SID -> (string)

The unique security identifier (SID) of the group.