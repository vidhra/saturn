# describe-package-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-package-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/describe-package-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeartifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html#cli-aws-codeartifact) ]

# describe-package-version

## Description

Returns a [PackageVersionDescription](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html) object that contains information about the requested package version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeartifact-2018-09-22/DescribePackageVersion)

## Synopsis

```
describe-package-version
--domain <value>
[--domain-owner <value>]
--repository <value>
--format <value>
[--namespace <value>]
--package <value>
--package-version <value>
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

The name of the domain that contains the repository that contains the package version.

`--domain-owner` (string)

The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.

`--repository` (string)

The name of the repository that contains the package version.

`--format` (string)

A format that specifies the type of the requested package version.

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

The namespace of the requested package version. The package component that specifies its namespace depends on its type. For example:

### Note

The namespace is required when requesting package versions of the following formats:

- Maven
- Swift
- generic

- The namespace of a Maven package version is its `groupId` .
- The namespace of an npm or Swift package version is its `scope` .
- The namespace of a generic package is its `namespace` .
- Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.

`--package` (string)

The name of the requested package version.

`--package-version` (string)

A string that contains the package version (for example, `3.5.2` ).

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

packageVersion -> (structure)

A [PackageVersionDescription](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionDescription.html) object that contains information about the requested package version.

format -> (string)

The format of the package version.

namespace -> (string)

The namespace of the package version. The package component that specifies its namespace depends on its type. For example:

- The namespace of a Maven package version is its `groupId` .
- The namespace of an npm or Swift package version is its `scope` .
- The namespace of a generic package is its `namespace` .
- Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.

packageName -> (string)

The name of the requested package.

displayName -> (string)

The name of the package that is displayed. The `displayName` varies depending on the package versionâs format. For example, if an npm package is named `ui` , is in the namespace `vue` , and has the format `npm` , then the `displayName` is `@vue/ui` .

version -> (string)

The version of the package.

summary -> (string)

A summary of the package version. The summary is extracted from the package. The information in and detail level of the summary depends on the package versionâs format.

homePage -> (string)

The homepage associated with the package.

sourceCodeRepository -> (string)

The repository for the source code in the package version, or the source code used to build it.

publishedTime -> (timestamp)

A timestamp that contains the date and time the package version was published.

licenses -> (list)

Information about licenses associated with the package version.

(structure)

Details of the license data.

name -> (string)

Name of the license.

url -> (string)

The URL for license data.

revision -> (string)

The revision of the package version.

status -> (string)

A string that contains the status of the package version.

origin -> (structure)

A [PackageVersionOrigin](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageVersionOrigin.html) object that contains information about how the package version was added to the repository.

domainEntryPoint -> (structure)

A [DomainEntryPoint](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_DomainEntryPoint.html) object that contains information about from which repository or external connection the package version was added to the domain.

repositoryName -> (string)

The name of the repository that a package was originally published to.

externalConnectionName -> (string)

The name of the external connection that a package was ingested from.

originType -> (string)

Describes how the package version was originally added to the domain. An `INTERNAL` origin type means the package version was published directly to a repository in the domain. An `EXTERNAL` origin type means the package version was ingested from an external connection.