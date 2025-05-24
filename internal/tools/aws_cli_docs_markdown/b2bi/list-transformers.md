# list-transformersÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/list-transformers.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/list-transformers.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [b2bi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/index.html#cli-aws-b2bi) ]

# list-transformers

## Description

Lists the available transformers. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/b2bi-2022-06-23/ListTransformers)

`list-transformers` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `transformers`

## Synopsis

```
list-transformers
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

## Output

transformers -> (list)

Returns an array of one or more transformer objects.

For each transformer, a `TransformerSummary` object is returned. The `TransformerSummary` contains all the details for a specific transformer.

(structure)

Contains the details for a transformer object. A transformer can take an EDI file as input and transform it into a JSON-or XML-formatted document. Alternatively, a transformer can take a JSON-or XML-formatted document as input and transform it into an EDI file.

transformerId -> (string)

Returns the system-assigned unique identifier for the transformer.

name -> (string)

Returns the descriptive name for the transformer.

status -> (string)

Returns the state of the newly created transformer. The transformer can be either `active` or `inactive` . For the transformer to be used in a capability, its status must `active` .

createdAt -> (timestamp)

Returns a timestamp indicating when the transformer was created. For example, `2023-07-20T19:58:44.624Z` .

modifiedAt -> (timestamp)

Returns a timestamp representing the date and time for the most recent change for the transformer object.

fileFormat -> (string)

Returns that the currently supported file formats for EDI transformations are `JSON` and `XML` .

mappingTemplate -> (string)

Returns the mapping template for the transformer. This template is used to map the parsed EDI file using JSONata or XSLT.

ediType -> (tagged union structure)

Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12Details`.

x12Details -> (structure)

Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

transactionSet -> (string)

Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.

version -> (string)

Returns the version to use for the specified X12 transaction set.

sampleDocument -> (string)

Returns a sample EDI document that is used by a transformer as a guide for processing the EDI data.

inputConversion -> (structure)

Returns a structure that contains the format options for the transformation.

fromFormat -> (string)

The format for the transformer input: currently on `X12` is supported.

formatOptions -> (tagged union structure)

A structure that contains the formatting options for an inbound transformer.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12`.

x12 -> (structure)

A structure that contains the X12 transaction set and version. The X12 structure is used when the system transforms an EDI (electronic data interchange) file.

### Note

If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.

transactionSet -> (string)

Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.

version -> (string)

Returns the version to use for the specified X12 transaction set.

mapping -> (structure)

Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).

templateLanguage -> (string)

The transformation language for the template, either XSLT or JSONATA.

template -> (string)

A string that represents the mapping template, in the transformation language specified in `templateLanguage` .

outputConversion -> (structure)

Returns the `OutputConversion` object, which contains the format options for the outbound transformation.

toFormat -> (string)

The format for the output from an outbound transformer: only X12 is currently supported.

formatOptions -> (tagged union structure)

A structure that contains the X12 transaction set and version for the transformer output.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12`.

x12 -> (structure)

A structure that contains the X12 transaction set and version. The X12 structure is used when the system transforms an EDI (electronic data interchange) file.

### Note

If an EDI input file contains more than one transaction, each transaction must have the same transaction set and version, for example 214/4010. If not, the transformer cannot parse the file.

transactionSet -> (string)

Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.

version -> (string)

Returns the version to use for the specified X12 transaction set.

sampleDocuments -> (structure)

Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.

bucketName -> (string)

Contains the Amazon S3 bucket that is used to hold your sample documents.

keys -> (list)

Contains an array of the Amazon S3 keys used to identify the location for your sample documents.

(structure)

An array of the Amazon S3 keys used to identify the location for your sample documents.

input -> (string)

An array of keys for your input sample documents.

output -> (string)

An array of keys for your output sample documents.

nextToken -> (string)

When additional results are obtained from the command, a `NextToken` parameter is returned in the output. You can then pass the `NextToken` parameter in a subsequent command to continue listing additional resources.