# get-retrieverÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/get-retriever.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/get-retriever.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [qbusiness](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/qbusiness/index.html#cli-aws-qbusiness) ]

# get-retriever

## Description

Gets information about an existing retriever used by an Amazon Q Business application.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/qbusiness-2023-11-27/GetRetriever)

## Synopsis

```
get-retriever
--application-id <value>
--retriever-id <value>
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

`--application-id` (string)

The identifier of the Amazon Q Business application using the retriever.

`--retriever-id` (string)

The identifier of the retriever.

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

applicationId -> (string)

The identifier of the Amazon Q Business application using the retriever.

retrieverId -> (string)

The identifier of the retriever.

retrieverArn -> (string)

The Amazon Resource Name (ARN) of the IAM role associated with the retriever.

type -> (string)

The type of the retriever.

status -> (string)

The status of the retriever.

displayName -> (string)

The name of the retriever.

configuration -> (tagged union structure)

Provides information on how the retriever used for your Amazon Q Business application is configured.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `nativeIndexConfiguration`, `kendraIndexConfiguration`.

nativeIndexConfiguration -> (structure)

Provides information on how a Amazon Q Business index used as a retriever for your Amazon Q Business application is configured.

indexId -> (string)

The identifier for the Amazon Q Business index.

boostingOverride -> (map)

Overrides the default boosts applied by Amazon Q Business to supported document attribute data types.

key -> (string)

value -> (tagged union structure)

Provides information on boosting supported Amazon Q Business document attribute types. When an end user chat query matches document attributes that have been boosted, Amazon Q Business prioritizes generating responses from content that matches the boosted document attributes.

### Note

For `STRING` and `STRING_LIST` type document attributes to be used for boosting on the console and the API, they must be enabled for search using the [DocumentAttributeConfiguration](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_DocumentAttributeConfiguration.html) object of the [UpdateIndex](https://docs.aws.amazon.com/amazonq/latest/api-reference/API_UpdateIndex.html) API. If you havenât enabled searching on these attributes, you canât boost attributes of these data types on either the console or the API.

For more information on how boosting document attributes work in Amazon Q Business, see [Boosting using document attributes](https://docs.aws.amazon.com/amazonq/latest/business-use-dg/metadata-boosting.html) .

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `numberConfiguration`, `stringConfiguration`, `dateConfiguration`, `stringListConfiguration`.

numberConfiguration -> (structure)

Provides information on boosting `NUMBER` type document attributes.

boostingLevel -> (string)

Specifies the duration, in seconds, of a boost applies to a `NUMBER` type document attribute.

boostingType -> (string)

Specifies how much a document attribute is boosted.

stringConfiguration -> (structure)

Provides information on boosting `STRING` type document attributes.

boostingLevel -> (string)

Specifies how much a document attribute is boosted.

attributeValueBoosting -> (map)

Specifies specific values of a `STRING` type document attribute being boosted.

key -> (string)

value -> (string)

dateConfiguration -> (structure)

Provides information on boosting `DATE` type document attributes.

boostingLevel -> (string)

Specifies how much a document attribute is boosted.

boostingDurationInSeconds -> (long)

Specifies the duration, in seconds, of a boost applies to a `DATE` type document attribute.

stringListConfiguration -> (structure)

Provides information on boosting `STRING_LIST` type document attributes.

boostingLevel -> (string)

Specifies how much a document attribute is boosted.

kendraIndexConfiguration -> (structure)

Provides information on how the Amazon Kendra index used as a retriever for your Amazon Q Business application is configured.

indexId -> (string)

The identifier of the Amazon Kendra index.

roleArn -> (string)

The Amazon Resource Name (ARN) of the role with the permission to access the retriever and required resources.

createdAt -> (timestamp)

The Unix timestamp when the retriever was created.

updatedAt -> (timestamp)

The Unix timestamp when the retriever was last updated.