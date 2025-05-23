# list-domains-for-packageÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/list-domains-for-package.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/list-domains-for-package.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opensearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html#cli-aws-opensearch) ]

# list-domains-for-package

## Description

Lists all Amazon OpenSearch Service domains associated with a given package. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opensearch-2021-01-01/ListDomainsForPackage)

## Synopsis

```
list-domains-for-package
--package-id <value>
[--max-results <value>]
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

`--package-id` (string)

The unique identifier of the package for which to list associated domains.

`--max-results` (integer)

An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.

`--next-token` (string)

If your initial `ListDomainsForPackage` operation returns a `nextToken` , you can include the returned `nextToken` in subsequent `ListDomainsForPackage` operations, which returns results in the next page.

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

DomainPackageDetailsList -> (list)

Information about all domains associated with a package.

(structure)

Information about a package that is associated with a domain. For more information, see [Custom packages for Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/custom-packages.html) .

PackageID -> (string)

Internal ID of the package.

PackageName -> (string)

User-specified name of the package.

PackageType -> (string)

The type of package.

LastUpdated -> (timestamp)

Timestamp of the most recent update to the package association status.

DomainName -> (string)

Name of the domain that the package is associated with.

DomainPackageStatus -> (string)

State of the association.

PackageVersion -> (string)

The current version of the package.

PrerequisitePackageIDList -> (list)

A list of package IDs that must be associated with the domain before or with the package can be associated.

(string)

ReferencePath -> (string)

The relative path of the package on the OpenSearch Service cluster nodes. This is `synonym_path` when the package is for synonym files.

ErrorDetails -> (structure)

Additional information if the package is in an error state. Null otherwise.

ErrorType -> (string)

The type of error that occurred.

ErrorMessage -> (string)

A message describing the error.

AssociationConfiguration -> (structure)

The configuration for associating a package with an Amazon OpenSearch Service domain.

KeyStoreAccessOption -> (structure)

The configuration parameters to enable accessing the key store required by the package.

KeyAccessRoleArn -> (string)

Role ARN to access the KeyStore Key

KeyStoreAccessEnabled -> (boolean)

This indicates whether Key Store access is enabled

NextToken -> (string)

When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.