# create-packageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/create-package.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/create-package.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opensearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html#cli-aws-opensearch) ]

# create-package

## Description

Creates a package for use with Amazon OpenSearch Service domains. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opensearch-2021-01-01/CreatePackage)

## Synopsis

```
create-package
--package-name <value>
--package-type <value>
[--package-description <value>]
--package-source <value>
[--package-configuration <value>]
[--engine-version <value>]
[--package-vending-options <value>]
[--package-encryption-options <value>]
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

`--package-name` (string)

Unique name for the package.

`--package-type` (string)

The type of package.

Possible values:

- `TXT-DICTIONARY`
- `ZIP-PLUGIN`
- `PACKAGE-LICENSE`
- `PACKAGE-CONFIG`

`--package-description` (string)

Description of the package.

`--package-source` (structure)

The Amazon S3 location from which to import the package.

S3BucketName -> (string)

The name of the Amazon S3 bucket containing the package.

S3Key -> (string)

Key (file name) of the package.

Shorthand Syntax:

```
S3BucketName=string,S3Key=string
```

JSON Syntax:

```
{
  "S3BucketName": "string",
  "S3Key": "string"
}
```

`--package-configuration` (structure)

The configuration parameters for the package being created.

LicenseRequirement -> (string)

The license requirements for the package.

LicenseFilepath -> (string)

The relative file path for the license associated with the package.

ConfigurationRequirement -> (string)

The configuration requirements for the package.

RequiresRestartForConfigurationUpdate -> (boolean)

This indicates whether a B/G deployment is required for updating the configuration that the plugin is prerequisite for.

Shorthand Syntax:

```
LicenseRequirement=string,LicenseFilepath=string,ConfigurationRequirement=string,RequiresRestartForConfigurationUpdate=boolean
```

JSON Syntax:

```
{
  "LicenseRequirement": "REQUIRED"|"OPTIONAL"|"NONE",
  "LicenseFilepath": "string",
  "ConfigurationRequirement": "REQUIRED"|"OPTIONAL"|"NONE",
  "RequiresRestartForConfigurationUpdate": true|false
}
```

`--engine-version` (string)

The version of the Amazon OpenSearch Service engine for which is compatible with the package. This can only be specified for package type `ZIP-PLUGIN`

`--package-vending-options` (structure)

The vending options for the package being created. They determine if the package can be vended to other users.

VendingEnabled -> (boolean)

Indicates whether the package vending feature is enabled, allowing the package to be used by other users.

Shorthand Syntax:

```
VendingEnabled=boolean
```

JSON Syntax:

```
{
  "VendingEnabled": true|false
}
```

`--package-encryption-options` (structure)

The encryption parameters for the package being created.

KmsKeyIdentifier -> (string)

KMS key ID for encrypting the package.

EncryptionEnabled -> (boolean)

Whether encryption is enabled for the package.

Shorthand Syntax:

```
KmsKeyIdentifier=string,EncryptionEnabled=boolean
```

JSON Syntax:

```
{
  "KmsKeyIdentifier": "string",
  "EncryptionEnabled": true|false
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

PackageDetails -> (structure)

Basic information about an OpenSearch Service package.

PackageID -> (string)

The unique identifier of the package.

PackageName -> (string)

The user-specified name of the package.

PackageType -> (string)

The type of package.

PackageDescription -> (string)

User-specified description of the package.

PackageStatus -> (string)

The current status of the package. The available options are `AVAILABLE` , `COPYING` , `COPY_FAILED` , `VALIDATNG` , `VALIDATION_FAILED` , `DELETING` , and `DELETE_FAILED` .

CreatedAt -> (timestamp)

The timestamp when the package was created.

LastUpdatedAt -> (timestamp)

Date and time when the package was last updated.

AvailablePackageVersion -> (string)

The package version.

ErrorDetails -> (structure)

Additional information if the package is in an error state. Null otherwise.

ErrorType -> (string)

The type of error that occurred.

ErrorMessage -> (string)

A message describing the error.

EngineVersion -> (string)

Version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.

AvailablePluginProperties -> (structure)

If the package is a `ZIP-PLUGIN` package, additional information about plugin properties.

Name -> (string)

The name of the plugin.

Description -> (string)

The description of the plugin.

Version -> (string)

The version of the plugin.

ClassName -> (string)

The name of the class to load.

UncompressedSizeInBytes -> (long)

The uncompressed size of the plugin.

AvailablePackageConfiguration -> (structure)

This represents the available configuration parameters for the package.

LicenseRequirement -> (string)

The license requirements for the package.

LicenseFilepath -> (string)

The relative file path for the license associated with the package.

ConfigurationRequirement -> (string)

The configuration requirements for the package.

RequiresRestartForConfigurationUpdate -> (boolean)

This indicates whether a B/G deployment is required for updating the configuration that the plugin is prerequisite for.

AllowListedUserList -> (list)

A list of users who are allowed to view and associate the package. This field is only visible to the owner of a package.

(string)

PackageOwner -> (string)

The owner of the package who is allowed to create and update a package and add users to the package scope.

PackageVendingOptions -> (structure)

Package Vending Options for a package.

VendingEnabled -> (boolean)

Indicates whether the package vending feature is enabled, allowing the package to be used by other users.

PackageEncryptionOptions -> (structure)

Encryption options for a package.

KmsKeyIdentifier -> (string)

KMS key ID for encrypting the package.

EncryptionEnabled -> (boolean)

Whether encryption is enabled for the package.