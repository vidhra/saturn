# put-package-origin-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-package-origin-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/put-package-origin-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeartifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html#cli-aws-codeartifact) ]

# put-package-origin-configuration

## Description

Sets the package origin configuration for a package.

The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package origin controls and configuration, see [Editing package origin controls](https://docs.aws.amazon.com/codeartifact/latest/ug/package-origin-controls.html) in the *CodeArtifact User Guide* .

`PutPackageOriginConfiguration` can be called on a package that doesnât yet exist in the repository. When called on a package that does not exist, a package is created in the repository with no versions and the requested restrictions are set on the package. This can be used to preemptively block ingesting or retaining any versions from external connections or upstream repositories, or to block publishing any versions of the package into the repository before connecting any package managers or publishers to the repository.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeartifact-2018-09-22/PutPackageOriginConfiguration)

## Synopsis

```
put-package-origin-configuration
--domain <value>
[--domain-owner <value>]
--repository <value>
--format <value>
[--namespace <value>]
--package <value>
--restrictions <value>
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

The name of the domain that contains the repository that contains the package.

`--domain-owner` (string)

The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.

`--repository` (string)

The name of the repository that contains the package.

`--format` (string)

A format that specifies the type of the package to be updated.

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

The namespace of the package to be updated. The package component that specifies its namespace depends on its type. For example:

- The namespace of a Maven package version is its `groupId` .
- The namespace of an npm or Swift package version is its `scope` .
- The namespace of a generic package is its `namespace` .
- Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.

`--package` (string)

The name of the package to be updated.

`--restrictions` (structure)

A [PackageOriginRestrictions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html) object that contains information about the `upstream` and `publish` package origin restrictions. The `upstream` restriction determines if new package versions can be ingested or retained from external connections or upstream repositories. The `publish` restriction determines if new package versions can be published directly to the repository.

You must include both the desired `upstream` and `publish` restrictions.

publish -> (string)

The package origin configuration that determines if new versions of the package can be published directly to the repository.

upstream -> (string)

The package origin configuration that determines if new versions of the package can be added to the repository from an external connection or upstream source.

Shorthand Syntax:

```
publish=string,upstream=string
```

JSON Syntax:

```
{
  "publish": "ALLOW"|"BLOCK",
  "upstream": "ALLOW"|"BLOCK"
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

originConfiguration -> (structure)

A [PackageOriginConfiguration](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginConfiguration.html) object that describes the origin configuration set for the package. It contains a [PackageOriginRestrictions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html) object that describes how new versions of the package can be introduced to the repository.

restrictions -> (structure)

A `PackageOriginRestrictions` object that contains information about the upstream and publish package origin configuration for the package.

publish -> (string)

The package origin configuration that determines if new versions of the package can be published directly to the repository.

upstream -> (string)

The package origin configuration that determines if new versions of the package can be added to the repository from an external connection or upstream source.