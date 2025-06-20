# delete-package-versionsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-package-versions.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/delete-package-versions.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeartifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html#cli-aws-codeartifact) ]

# delete-package-versions

## Description

Deletes one or more versions of a package. A deleted package version cannot be restored in your repository. If you want to remove a package version from your repository and be able to restore it later, set its status to `Archived` . Archived packages cannot be downloaded from a repository and donât show up with list package APIs (for example, [ListPackageVersions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_ListPackageVersions.html) ), but you can restore them using [UpdatePackageVersionsStatus](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_UpdatePackageVersionsStatus.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeartifact-2018-09-22/DeletePackageVersions)

## Synopsis

```
delete-package-versions
--domain <value>
[--domain-owner <value>]
--repository <value>
--format <value>
[--namespace <value>]
--package <value>
--versions <value>
[--expected-status <value>]
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

The name of the domain that contains the package to delete.

`--domain-owner` (string)

The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.

`--repository` (string)

The name of the repository that contains the package versions to delete.

`--format` (string)

The format of the package versions to delete.

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

The namespace of the package versions to be deleted. The package component that specifies its namespace depends on its type. For example:

### Note

The namespace is required when deleting package versions of the following formats:

- Maven
- Swift
- generic

- The namespace of a Maven package version is its `groupId` .
- The namespace of an npm or Swift package version is its `scope` .
- The namespace of a generic package is its `namespace` .
- Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.

`--package` (string)

The name of the package with the versions to delete.

`--versions` (list)

An array of strings that specify the versions of the package to delete.

(string)

Syntax:

```
"string" "string" ...
```

`--expected-status` (string)

The expected status of the package version to delete.

Possible values:

- `Published`
- `Unfinished`
- `Unlisted`
- `Archived`
- `Disposed`
- `Deleted`

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

**To delete package versions**

The following `delete-package-versions` example deletes version 4.0.0 of a package named test-package.

```
aws codeartifact delete-package-versions \
    --domain test-domain \
    --repo test-repo \
    --format npm \
    --package test-package \
    --versions 4.0.0
```

Output:

```
{
    "successfulVersions": {
        "4.0.0": {
            "revision": "Ciqe5/9yicvkJT13b5/LdLpCyE6fqA7poa9qp+FilPs=",
            "status": "Deleted"
        }
    },
    "failedVersions": {}
}
```

For more information, see [Delete a package version](https://docs.aws.amazon.com/codeartifact/latest/ug/delete-package.html) in the *AWS CodeArtifact User Guide*.

## Output

successfulVersions -> (map)

A list of the package versions that were successfully deleted. The status of every successful version will be `Deleted` .

key -> (string)

value -> (structure)

Contains the revision and status of a package version.

revision -> (string)

The revision of a package version.

status -> (string)

The status of a package version.

failedVersions -> (map)

A `PackageVersionError` object that contains a map of errors codes for the deleted package that failed. The possible error codes are:

- `ALREADY_EXISTS`
- `MISMATCHED_REVISION`
- `MISMATCHED_STATUS`
- `NOT_ALLOWED`
- `NOT_FOUND`
- `SKIPPED`

key -> (string)

value -> (structure)

l An error associated with package.

errorCode -> (string)

The error code associated with the error. Valid error codes are:

- `ALREADY_EXISTS`
- `MISMATCHED_REVISION`
- `MISMATCHED_STATUS`
- `NOT_ALLOWED`
- `NOT_FOUND`
- `SKIPPED`

errorMessage -> (string)

The error message associated with the error.