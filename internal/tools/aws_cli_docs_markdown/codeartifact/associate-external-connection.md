# associate-external-connectionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/associate-external-connection.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/associate-external-connection.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeartifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html#cli-aws-codeartifact) ]

# associate-external-connection

## Description

Adds an existing external connection to a repository. One external connection is allowed per repository.

### Note

A repository can have one or more upstream repositories, or an external connection.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeartifact-2018-09-22/AssociateExternalConnection)

## Synopsis

```
associate-external-connection
--domain <value>
[--domain-owner <value>]
--repository <value>
--external-connection <value>
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

The name of the domain that contains the repository.

`--domain-owner` (string)

The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.

`--repository` (string)

The name of the repository to which the external connection is added.

`--external-connection` (string)

The name of the external connection to add to the repository. The following values are supported:

- `public:npmjs` - for the npm public repository.
- `public:nuget-org` - for the NuGet Gallery.
- `public:pypi` - for the Python Package Index.
- `public:maven-central` - for Maven Central.
- `public:maven-googleandroid` - for the Google Android repository.
- `public:maven-gradleplugins` - for the Gradle plugins repository.
- `public:maven-commonsware` - for the CommonsWare Android repository.
- `public:maven-clojars` - for the Clojars repository.
- `public:ruby-gems-org` - for RubyGems.org.
- `public:crates-io` - for Crates.io.

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

**To add an external connection to a repository**

The following `associate-external-connection` example adds an external connection to npmjs.com to a repository named test-repo.

```
aws codeartifact associate-external-connection \
    --repository test-repo \
    --domain test-domain \
    --external-connection public:npmjs
```

Output:

```
{
    "repository": {
        "name": "test-repo",
        "administratorAccount": "111122223333",
        "domainName": "test-domain",
        "domainOwner": "111122223333",
        "arn": "arn:aws:codeartifact:us-west-2:111122223333:repository/test-domain/test-repo",
        "upstreams": [],
        "externalConnections": [
            {
                "externalConnectionName": "public:npmjs",
                "packageFormat": "npm",
                "status": "AVAILABLE"
            }
        ]
    }
}
```

For more information, see [Add an external connection](https://docs.aws.amazon.com/codeartifact/latest/ug/external-connection.html) in the *AWS CodeArtifact User Guide*.

## Output

repository -> (structure)

Information about the connected repository after processing the request.

name -> (string)

The name of the repository.

administratorAccount -> (string)

The 12-digit account number of the Amazon Web Services account that manages the repository.

domainName -> (string)

The name of the domain that contains the repository.

domainOwner -> (string)

The 12-digit account number of the Amazon Web Services account that owns the domain that contains the repository. It does not include dashes or spaces.

arn -> (string)

The Amazon Resource Name (ARN) of the repository.

description -> (string)

A text description of the repository.

upstreams -> (list)

A list of upstream repositories to associate with the repository. The order of the upstream repositories in the list determines their priority order when CodeArtifact looks for a requested package version. For more information, see [Working with upstream repositories](https://docs.aws.amazon.com/codeartifact/latest/ug/repos-upstream.html) .

(structure)

Information about an upstream repository.

repositoryName -> (string)

The name of an upstream repository.

externalConnections -> (list)

An array of external connections associated with the repository.

(structure)

Contains information about the external connection of a repository.

externalConnectionName -> (string)

The name of the external connection associated with a repository.

packageFormat -> (string)

The package format associated with a repositoryâs external connection. The valid package formats are:

- `npm` : A Node Package Manager (npm) package.
- `pypi` : A Python Package Index (PyPI) package.
- `maven` : A Maven package that contains compiled code in a distributable format, such as a JAR file.
- `nuget` : A NuGet package.
- `generic` : A generic package.
- `ruby` : A Ruby package.
- `swift` : A Swift package.
- `cargo` : A Cargo package.

status -> (string)

The status of the external connection of a repository. There is one valid value, `Available` .

createdTime -> (timestamp)

A timestamp that represents the date and time the repository was created.