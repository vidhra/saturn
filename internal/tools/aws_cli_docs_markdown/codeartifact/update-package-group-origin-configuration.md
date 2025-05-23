# update-package-group-origin-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/update-package-group-origin-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/update-package-group-origin-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [codeartifact](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codeartifact/index.html#cli-aws-codeartifact) ]

# update-package-group-origin-configuration

## Description

Updates the package origin configuration for a package group.

The package origin configuration determines how new versions of a package can be added to a repository. You can allow or block direct publishing of new package versions, or ingestion and retaining of new package versions from an external connection or upstream source. For more information about package group origin controls and configuration, see [Package group origin controls](https://docs.aws.amazon.com/codeartifact/latest/ug/package-group-origin-controls.html) in the *CodeArtifact User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/codeartifact-2018-09-22/UpdatePackageGroupOriginConfiguration)

## Synopsis

```
update-package-group-origin-configuration
--domain <value>
[--domain-owner <value>]
--package-group <value>
[--restrictions <value>]
[--add-allowed-repositories <value>]
[--remove-allowed-repositories <value>]
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

The name of the domain which contains the package group for which to update the origin configuration.

`--domain-owner` (string)

The 12-digit account number of the Amazon Web Services account that owns the domain. It does not include dashes or spaces.

`--package-group` (string)

The pattern of the package group for which to update the origin configuration.

`--restrictions` (map)

The origin configuration settings that determine how package versions can enter repositories.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string

Where valid key names are:
  EXTERNAL_UPSTREAM
  INTERNAL_UPSTREAM
  PUBLISH
```

JSON Syntax:

```
{"EXTERNAL_UPSTREAM"|"INTERNAL_UPSTREAM"|"PUBLISH": "ALLOW"|"ALLOW_SPECIFIC_REPOSITORIES"|"BLOCK"|"INHERIT"
  ...}
```

`--add-allowed-repositories` (list)

The repository name and restrictions to add to the allowed repository list of the specified package group.

(structure)

Details about an allowed repository for a package group, including its name and origin configuration.

repositoryName -> (string)

The name of the allowed repository.

originRestrictionType -> (string)

The origin configuration restriction type of the allowed repository.

Shorthand Syntax:

```
repositoryName=string,originRestrictionType=string ...
```

JSON Syntax:

```
[
  {
    "repositoryName": "string",
    "originRestrictionType": "EXTERNAL_UPSTREAM"|"INTERNAL_UPSTREAM"|"PUBLISH"
  }
  ...
]
```

`--remove-allowed-repositories` (list)

The repository name and restrictions to remove from the allowed repository list of the specified package group.

(structure)

Details about an allowed repository for a package group, including its name and origin configuration.

repositoryName -> (string)

The name of the allowed repository.

originRestrictionType -> (string)

The origin configuration restriction type of the allowed repository.

Shorthand Syntax:

```
repositoryName=string,originRestrictionType=string ...
```

JSON Syntax:

```
[
  {
    "repositoryName": "string",
    "originRestrictionType": "EXTERNAL_UPSTREAM"|"INTERNAL_UPSTREAM"|"PUBLISH"
  }
  ...
]
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

packageGroup -> (structure)

The package group and information about it after processing the request.

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

allowedRepositoryUpdates -> (map)

Information about the updated allowed repositories after processing the request.

key -> (string)

value -> (map)

key -> (string)

value -> (list)

(string)