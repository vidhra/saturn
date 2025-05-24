# publish-package-versionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/publish-package-version.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/publish-package-version.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeartifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html#cli-aws-codeartifact) ]

# publish-package-version

## Description

Creates a new package version containing one or more assets (or files).

The `unfinished` flag can be used to keep the package version in the `Unfinished` state until all of its assets have been uploaded (see [Package version status](https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status) in the *CodeArtifact user guide* ). To set the package versionâs status to `Published` , omit the `unfinished` flag when uploading the final asset, or set the status using [UpdatePackageVersionStatus](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html) . Once a package versionâs status is set to `Published` , it cannot change back to `Unfinished` .

### Note

Only generic packages can be published using this API. For more information, see [Using generic packages](https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html) in the *CodeArtifact User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeartifact-2018-09-22/PublishPackageVersion)

## Synopsis

```
publish-package-version
--domain <value>
[--domain-owner <value>]
--repository <value>
--format <value>
[--namespace <value>]
--package <value>
--package-version <value>
--asset-content <value>
--asset-name <value>
--asset-sha256 <value>
[--unfinished | --no-unfinished]
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

The name of the domain that contains the repository that contains the package version to publish.

`--domain-owner` (string)

The 12-digit account number of the AWS account that owns the domain. It does not include dashes or spaces.

`--repository` (string)

The name of the repository that the package version will be published to.

`--format` (string)

A format that specifies the type of the package version with the requested asset file.

The only supported value is `generic` .

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

The namespace of the package version to publish.

`--package` (string)

The name of the package version to publish.

`--package-version` (string)

The package version to publish (for example, `3.5.2` ).

`--asset-content` (streaming blob)

The content of the asset to publish.

### Note

This argument is of type: streaming blob. Its value must be the path to a file (e.g. `path/to/file`) and must **not** be prefixed with `file://` or `fileb://`

`--asset-name` (string)

The name of the asset to publish. Asset names can include Unicode letters and numbers, and the following special characters: `~ ! @ ^ & ( ) - ` _ + [ ] { } ; , . ``

`--asset-sha256` (string)

The SHA256 hash of the `assetContent` to publish. This value must be calculated by the caller and provided with the request (see [Publishing a generic package](https://docs.aws.amazon.com/codeartifact/latest/ug/using-generic.html#publishing-generic-packages) in the *CodeArtifact User Guide* ).

This value is used as an integrity check to verify that the `assetContent` has not changed after it was originally sent.

`--unfinished` | `--no-unfinished` (boolean)

Specifies whether the package version should remain in the `unfinished` state. If omitted, the package version status will be set to `Published` (see [Package version status](https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status) in the *CodeArtifact User Guide* ).

Valid values: `unfinished`

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

format -> (string)

The format of the package version.

namespace -> (string)

The namespace of the package version.

package -> (string)

The name of the package.

version -> (string)

The version of the package.

versionRevision -> (string)

The revision of the package version.

status -> (string)

A string that contains the status of the package version. For more information, see [Package version status](https://docs.aws.amazon.com/codeartifact/latest/ug/packages-overview.html#package-version-status.html#package-version-status) in the *CodeArtifact User Guide* .

asset -> (structure)

An [AssetSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_AssetSummary.html) for the published asset.

name -> (string)

The name of the asset.

size -> (long)

The size of the asset.

hashes -> (map)

The hashes of the asset.

key -> (string)

value -> (string)