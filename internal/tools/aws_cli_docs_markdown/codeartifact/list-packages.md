# list-packagesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-packages.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/list-packages.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeartifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html#cli-aws-codeartifact) ]

# list-packages

## Description

Returns a list of [PackageSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html) objects for packages in a repository that match the request parameters.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeartifact-2018-09-22/ListPackages)

`list-packages` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `packages`

## Synopsis

```
list-packages
--domain <value>
[--domain-owner <value>]
--repository <value>
[--format <value>]
[--namespace <value>]
[--package-prefix <value>]
[--publish <value>]
[--upstream <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

The name of the domain that contains the repository that contains the requested packages.

`--domain-owner` (string)

The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.

`--repository` (string)

The name of the repository that contains the requested packages.

`--format` (string)

The format used to filter requested packages. Only packages from the provided format will be returned.

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

The namespace prefix used to filter requested packages. Only packages with a namespace that starts with the provided string value are returned. Note that although this option is called `--namespace` and not `--namespace-prefix` , it has prefix-matching behavior.

Each package format uses namespace as follows:

- The namespace of a Maven package version is its `groupId` .
- The namespace of an npm or Swift package version is its `scope` .
- The namespace of a generic package is its `namespace` .
- Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.

`--package-prefix` (string)

A prefix used to filter requested packages. Only packages with names that start with `packagePrefix` are returned.

`--publish` (string)

The value of the `Publish` package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see [PackageOriginRestrictions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html) .

Possible values:

- `ALLOW`
- `BLOCK`

`--upstream` (string)

The value of the `Upstream` package origin control restriction used to filter requested packages. Only packages with the provided restriction are returned. For more information, see [PackageOriginRestrictions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html) .

Possible values:

- `ALLOW`
- `BLOCK`

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

**To list packages in a repository**

The following `list-packages` example list packages in a repository named `test-repo` in a domain named `test-domain`.

```
aws codeartifact list-packages \
    --domain test-domain \
    --repository test-repo
```

Output:

```
{
    "packages": [
        {
            "format": "npm",
            "package": "lodash"
        }
        {
            "format": "python",
            "package": "test-package"
        }
    ]
}
```

For more information, see [List package names](https://docs.aws.amazon.com/codeartifact/latest/ug/list-packages.html) in the *AWS CodeArtifact User Guide*.

## Output

packages -> (list)

The list of returned [PackageSummary](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageSummary.html) objects.

(structure)

Details about a package, including its format, namespace, and name.

format -> (string)

The format of the package.

namespace -> (string)

The namespace of the package. The package component that specifies its namespace depends on its type. For example:

- The namespace of a Maven package version is its `groupId` .
- The namespace of an npm or Swift package version is its `scope` .
- The namespace of a generic package is its `namespace` .
- Python, NuGet, Ruby, and Cargo package versions do not contain a corresponding component, package versions of those formats do not have a namespace.

package -> (string)

The name of the package.

originConfiguration -> (structure)

A [PackageOriginConfiguration](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginConfiguration.html) object that contains a [PackageOriginRestrictions](https://docs.aws.amazon.com/codeartifact/latest/APIReference/API_PackageOriginRestrictions.html) object that contains information about the upstream and publish package origin restrictions.

restrictions -> (structure)

A `PackageOriginRestrictions` object that contains information about the upstream and publish package origin configuration for the package.

publish -> (string)

The package origin configuration that determines if new versions of the package can be published directly to the repository.

upstream -> (string)

The package origin configuration that determines if new versions of the package can be added to the repository from an external connection or upstream source.

nextToken -> (string)

If there are additional results, this is the token for the next set of results.