# list-instance-type-detailsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/list-instance-type-details.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/list-instance-type-details.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [opensearch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/opensearch/index.html#cli-aws-opensearch) ]

# list-instance-type-details

## Description

Lists all instance types and available features for a given OpenSearch or Elasticsearch version.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/opensearch-2021-01-01/ListInstanceTypeDetails)

## Synopsis

```
list-instance-type-details
--engine-version <value>
[--domain-name <value>]
[--max-results <value>]
[--next-token <value>]
[--retrieve-azs | --no-retrieve-azs]
[--instance-type <value>]
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

`--engine-version` (string)

The version of OpenSearch or Elasticsearch, in the format Elasticsearch_X.Y or OpenSearch_X.Y. Defaults to the latest version of OpenSearch.

`--domain-name` (string)

The name of the domain.

`--max-results` (integer)

An optional parameter that specifies the maximum number of results to return. You can use `nextToken` to get the next page of results.

`--next-token` (string)

If your initial `ListInstanceTypeDetails` operation returns a `nextToken` , you can include the returned `nextToken` in subsequent `ListInstanceTypeDetails` operations, which returns results in the next page.

`--retrieve-azs` | `--no-retrieve-azs` (boolean)

An optional parameter that specifies the Availability Zones for the domain.

`--instance-type` (string)

An optional parameter that lists information for a given instance type.

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

InstanceTypeDetails -> (list)

Lists all supported instance types and features for the given OpenSearch or Elasticsearch version.

(structure)

Lists all instance types and available features for a given OpenSearch or Elasticsearch version.

InstanceType -> (string)

The instance type.

EncryptionEnabled -> (boolean)

Whether encryption at rest and node-to-node encryption are supported for the instance type.

CognitoEnabled -> (boolean)

Whether Amazon Cognito access is supported for the instance type.

AppLogsEnabled -> (boolean)

Whether logging is supported for the instance type.

AdvancedSecurityEnabled -> (boolean)

Whether fine-grained access control is supported for the instance type.

WarmEnabled -> (boolean)

Whether UltraWarm is supported for the instance type.

InstanceRole -> (list)

Whether the instance acts as a data node, a dedicated master node, or an UltraWarm node.

(string)

AvailabilityZones -> (list)

The supported Availability Zones for the instance type.

(string)

NextToken -> (string)

When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Send the request again using the returned token to retrieve the next page.