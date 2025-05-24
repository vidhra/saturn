# list-package-version-dependenciesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-package-version-dependencies.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-package-version-dependencies.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeartifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html#cli-aws-codeartifact) ]

# list-package-version-dependencies

## Description

Returns the direct dependencies for a package version. The dependencies are returned as [PackageDependency](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html) objects. CodeArtifact extracts the dependencies for a package version from the metadata file for the package format (for example, the `package.json` file for npm packages and the `pom.xml` file for Maven). Any package version dependencies that are not listed in the configuration file are not returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeartifact-2018-09-22/ListPackageVersionDependencies)

## Synopsis

```
list-package-version-dependencies
--domain <value>
[--domain-owner <value>]
--repository <value>
--format <value>
[--namespace <value>]
--package <value>
--package-version <value>
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

`--domain` (string)

The name of the domain that contains the repository that contains the requested package version dependencies.

`--domain-owner` (string)

The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.

`--repository` (string)

The name of the repository that contains the requested package version.

`--format` (string)

The format of the package with the requested dependencies.

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

The namespace of the package version with the requested dependencies. The package component that specifies its namespace depends on its type. For example:

### Note

The namespace is required when listing dependencies from package versions of the following formats:

- Maven

- The namespace of a Maven package version is its `groupId` .
- The namespace of an npm package version is its `scope` .
- Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace.

`--package` (string)

The name of the package versionsâ package.

`--package-version` (string)

A string that contains the package version (for example, `3.5.2` ).

`--next-token` (string)

The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

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

**To view a package versionâs dependencies**

The following `list-package-version-dependencies` example retrieves the dependencies for version 4.0.0 of an npm package named test-package.

```
aws codeartifact list-package-version-dependencies \
    --domain test-domain \
    --repo test-repo \
    --format npm \
    --package test-package \
    --package-version 4.0.0
```

Output:

```
{
    "format": "npm",
    "package": "test-package",
    "version": "4.0.0",
    "versionRevision": "Ciqe5/9yicvkJT13b5/LdLpCyE6fqA7poa9qp+FilPs=",
    "dependencies": [
        {
            "namespace": "testns",
            "package": "testdep1",
            "dependencyType": "regular",
            "versionRequirement": "1.8.5"
        },
        {
            "namespace": "testns",
            "package": "testdep2",
            "dependencyType": "regular",
            "versionRequirement": "1.8.5"
        }
    ]
}
```

For more information, see [View and update package version details and dependencies](https://docs.aws.amazon.com/codeartifact/latest/ug/describe-package-version.html) in the *AWS CodeArtifact User Guide*.

## Output

format -> (string)

A format that specifies the type of the package that contains the returned dependencies.

namespace -> (string)

The namespace of the package version that contains the returned dependencies. The package component that specifies its namespace depends on its type. For example:

### Note

The namespace is required when listing dependencies from package versions of the following formats:

- Maven

- The namespace of a Maven package version is its `groupId` .
- The namespace of an npm package version is its `scope` .
- Python and NuGet package versions do not contain a corresponding component, package versions of those formats do not have a namespace.

package -> (string)

The name of the package that contains the returned package versions dependencies.

version -> (string)

The version of the package that is specified in the request.

versionRevision -> (string)

The current revision associated with the package version.

nextToken -> (string)

The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.

dependencies -> (list)

The returned list of [PackageDependency](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageDependency.html) objects.

(structure)

Details about a package dependency.

namespace -> (string)

The namespace of the package that this package depends on. The package component that specifies its namespace depends on its type. For example:

- The namespace of a Maven package version is its `groupId` .
- The namespace of an npm or Swift package version is its `scope` .
- The namespace of a generic package is its `namespace` .
- Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.

package -> (string)

The name of the package that this package depends on.

dependencyType -> (string)

The type of a package dependency. The possible values depend on the package type.

- npm: `regular` , `dev` , `peer` , `optional`
- maven: `optional` , `parent` , `compile` , `runtime` , `test` , `system` , `provided` .

### Note

Note that `parent` is not a regular Maven dependency type; instead this is extracted from the `<parent>` element if one is defined in the package versionâs POM file.

- nuget: The `dependencyType` field is never set for NuGet packages.
- pypi: `Requires-Dist`

versionRequirement -> (string)

The required version, or version range, of the package that this package depends on. The version format is specific to the package type. For example, the following are possible valid required versions: `1.2.3` , `^2.3.4` , or `4.x` .