# get-provider-serviceÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/get-provider-service.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/get-provider-service.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [entityresolution](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/entityresolution/index.html#cli-aws-entityresolution) ]

# get-provider-service

## Description

Returns the `ProviderService` of a given name.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/entityresolution-2018-05-10/GetProviderService)

`get-provider-service` uses document type values. Document types follow the JSON data model where valid values are: strings, numbers, booleans, null, arrays, and objects. For command input, options and nested parameters that are labeled with the type `document` must be provided as JSON. Shorthand syntax does not support document types.

## Synopsis

```
get-provider-service
--provider-name <value>
--provider-service-name <value>
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

`--provider-name` (string)

The name of the provider. This name is typically the company name.

`--provider-service-name` (string)

The ARN (Amazon Resource Name) of the product that the provider service provides.

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

providerName -> (string)

The name of the provider. This name is typically the company name.

providerServiceName -> (string)

The name of the product that the provider service provides.

providerServiceDisplayName -> (string)

The display name of the provider service.

providerServiceType -> (string)

The type of provider service.

providerServiceArn -> (string)

The ARN (Amazon Resource Name) that Entity Resolution generated for the provider service.

providerConfigurationDefinition -> (document)

The definition of the provider configuration.

providerIdNameSpaceConfiguration -> (structure)

The provider configuration required for different ID namespace types.

description -> (string)

The description of the ID namespace.

providerTargetConfigurationDefinition -> (document)

Configurations required for the target ID namespace.

providerSourceConfigurationDefinition -> (document)

Configurations required for the source ID namespace.

providerJobConfiguration -> (document)

Provider service job configurations.

providerEndpointConfiguration -> (tagged union structure)

The required configuration fields to use with the provider service.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `marketplaceConfiguration`.

marketplaceConfiguration -> (structure)

The identifiers of the provider service, from Data Exchange.

dataSetId -> (string)

The dataset ID on Data Exchange.

revisionId -> (string)

The revision ID on Data Exchange.

assetId -> (string)

The asset ID on Data Exchange.

listingId -> (string)

The listing ID on Data Exchange.

anonymizedOutput -> (boolean)

Specifies whether output data from the provider is anonymized. A value of `TRUE` means the output will be anonymized and you canât relate the data that comes back from the provider to the identifying input. A value of `FALSE` means the output wonât be anonymized and you can relate the data that comes back from the provider to your source data.

providerEntityOutputDefinition -> (document)

The definition of the provider entity output.

providerIntermediateDataAccessConfiguration -> (structure)

The Amazon Web Services accounts and the S3 permissions that are required by some providers to create an S3 bucket for intermediate data storage.

awsAccountIds -> (list)

The Amazon Web Services account that provider can use to read or write data into the customerâs intermediate S3 bucket.

(string)

requiredBucketActions -> (list)

The S3 bucket actions that the provider requires permission for.

(string)

providerComponentSchema -> (structure)

Input schema for the provider service.

schemas -> (list)

Input schema for the provider service.

(list)

(string)

providerSchemaAttributes -> (list)

The provider schema attributes.

(structure)

The provider schema attribute.

fieldName -> (string)

The field name.

type -> (string)

The type of the provider schema attribute.

LiveRamp supports: `NAME` | `NAME_FIRST` | `NAME_MIDDLE` | `NAME_LAST` | `ADDRESS` | `ADDRESS_STREET1` | `ADDRESS_STREET2` | `ADDRESS_STREET3` | `ADDRESS_CITY` | `ADDRESS_STATE` | `ADDRESS_COUNTRY` | `ADDRESS_POSTALCODE` | `PHONE` | `PHONE_NUMBER` | `EMAIL_ADDRESS` | `UNIQUE_ID` | `PROVIDER_ID`

TransUnion supports: `NAME` | `NAME_FIRST` | `NAME_LAST` | `ADDRESS` | `ADDRESS_CITY` | `ADDRESS_STATE` | `ADDRESS_COUNTRY` | `ADDRESS_POSTALCODE` | `PHONE_NUMBER` | `EMAIL_ADDRESS` | `UNIQUE_ID` | `DATE` | `IPV4` | `IPV6` | `MAID`

Unified ID 2.0 supports: `PHONE_NUMBER` | `EMAIL_ADDRESS` | `UNIQUE_ID`

subType -> (string)

The sub type of the provider schema attribute.

hashing -> (boolean)

The hashing attribute of the provider schema.