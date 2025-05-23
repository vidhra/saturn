# describe-applicationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-applications.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/describe-applications.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [workspaces](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/workspaces/index.html#cli-aws-workspaces) ]

# describe-applications

## Description

Describes the specified applications by filtering based on their compute types, license availability, operating systems, and owners.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/workspaces-2015-04-08/DescribeApplications)

## Synopsis

```
describe-applications
[--application-ids <value>]
[--compute-type-names <value>]
[--license-type <value>]
[--operating-system-names <value>]
[--owner <value>]
[--max-results <value>]
[--next-token <value>]
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

`--application-ids` (list)

The identifiers of one or more applications.

(string)

Syntax:

```
"string" "string" ...
```

`--compute-type-names` (list)

The compute types supported by the applications.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  VALUE
  STANDARD
  PERFORMANCE
  POWER
  GRAPHICS
  POWERPRO
  GENERALPURPOSE_4XLARGE
  GENERALPURPOSE_8XLARGE
  GRAPHICSPRO
  GRAPHICS_G4DN
  GRAPHICSPRO_G4DN
```

`--license-type` (string)

The license availability for the applications.

Possible values:

- `LICENSED`
- `UNLICENSED`

`--operating-system-names` (list)

The operating systems supported by the applications.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  AMAZON_LINUX_2
  UBUNTU_18_04
  UBUNTU_20_04
  UBUNTU_22_04
  UNKNOWN
  WINDOWS_10
  WINDOWS_11
  WINDOWS_7
  WINDOWS_SERVER_2016
  WINDOWS_SERVER_2019
  WINDOWS_SERVER_2022
  RHEL_8
  ROCKY_8
```

`--owner` (string)

The owner of the applications.

`--max-results` (integer)

The maximum number of applications to return.

`--next-token` (string)

If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.

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

Applications -> (list)

List of information about the specified applications.

(structure)

Describes the WorkSpace application.

ApplicationId -> (string)

The identifier of the application.

Created -> (timestamp)

The time the application is created.

Description -> (string)

The description of the WorkSpace application.

LicenseType -> (string)

The license availability for the applications.

Name -> (string)

The name of the WorkSpace application.

Owner -> (string)

The owner of the WorkSpace application.

State -> (string)

The status of WorkSpace application.

SupportedComputeTypeNames -> (list)

The supported compute types of the WorkSpace application.

(string)

SupportedOperatingSystemNames -> (list)

The supported operating systems of the WorkSpace application.

(string)

NextToken -> (string)

If you received a `NextToken` from a previous call that was paginated, provide this token to receive the next set of results.