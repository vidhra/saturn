# get-associated-package-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-associated-package-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/get-associated-package-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeartifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html#cli-aws-codeartifact) ]

# get-associated-package-group

## Description

Returns the most closely associated package group to the specified package. This API does not require that the package exist in any repository in the domain. As such, `GetAssociatedPackageGroup` can be used to see which package groupâs origin configuration applies to a package before that package is in a repository. This can be helpful to check if public packages are blocked without ingesting them.

For information package group association and matching, see [Package group definition syntax and matching behavior](https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-definition-syntax-matching-behavior.html) in the *CodeArtifact User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeartifact-2018-09-22/GetAssociatedPackageGroup)

## Synopsis

```
get-associated-package-group
--domain <value>
[--domain-owner <value>]
--format <value>
[--namespace <value>]
--package <value>
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

`--domain` (string)

The name of the domain that contains the package from which to get the associated package group.

`--domain-owner` (string)

The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.

`--format` (string)

The format of the package from which to get the associated package group.

Possible values:

- `npm`
- `pypi`
- `maven`
- `nuget`
- `generic`
- `ruby`
- `swift`
- `cargo`

`--namespace` (string)

The namespace of the package from which to get the associated package group. The package component that specifies its namespace depends on its type. For example:

### Note

The namespace is required when getting associated package groups from packages of the following formats:

- Maven
- Swift
- generic

- The namespace of a Maven package version is its `groupId` .
- The namespace of an npm or Swift package version is its `scope` .
- The namespace of a generic package is its `namespace` .
- Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.

`--package` (string)

The package from which to get the associated package group.

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

packageGroup -> (structure)

The package group that is associated with the requested package.

arn -> (string)

The ARN of the package group.

pattern -> (string)

The pattern of the package group. The pattern determines which packages are associated with the package group.

domainName -> (string)

The name of the domain that contains the package group.

domainOwner -> (string)

The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.

createdTime -> (timestamp)

A timestamp that represents the date and time the package group was created.

contactInfo -> (string)

The contact information of the package group.

description -> (string)

The description of the package group.

originConfiguration -> (structure)

The package group origin configuration that determines how package versions can enter repositories.

restrictions -> (map)

The origin configuration settings that determine how package versions can enter repositories.

key -> (string)

value -> (structure)

Contains information about the configured restrictions of the origin controls of a package group.

mode -> (string)

The package group origin restriction setting. If the value of `mode` is `ALLOW` , `ALLOW_SPECIFIC_REPOSITORIES` , or `BLOCK` , then the value of `effectiveMode` is the same. Otherwise, when the value is `INHERIT` , then the value of `effectiveMode` is the value of `mode` of the first parent group which does not have a value of `INHERIT` .

effectiveMode -> (string)

The effective package group origin restriction setting. If the value of `mode` is `ALLOW` , `ALLOW_SPECIFIC_REPOSITORIES` , or `BLOCK` , then the value of `effectiveMode` is the same. Otherwise, when the value of `mode` is `INHERIT` , then the value of `effectiveMode` is the value of `mode` of the first parent group which does not have a value of `INHERIT` .

inheritedFrom -> (structure)

The parent package group that the package group origin restrictions are inherited from.

arn -> (string)

The ARN of the package group.

pattern -> (string)

The pattern of the package group. The pattern determines which packages are associated with the package group, and is also the identifier of the package group.

repositoriesCount -> (long)

The number of repositories in the allowed repository list.

parent -> (structure)

The direct parent package group of the package group.

arn -> (string)

The ARN of the package group.

pattern -> (string)

The pattern of the package group. The pattern determines which packages are associated with the package group, and is also the identifier of the package group.

associationType -> (string)

Describes the strength of the association between the package and package group. A strong match is also known as an exact match, and a weak match is known as a relative match.