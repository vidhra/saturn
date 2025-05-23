# get-capabilityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/get-capability.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/get-capability.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [b2bi](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/b2bi/index.html#cli-aws-b2bi) ]

# get-capability

## Description

Retrieves the details for the specified capability. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/b2bi-2022-06-23/GetCapability)

## Synopsis

```
get-capability
--capability-id <value>
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

`--capability-id` (string)

Specifies a system-assigned unique identifier for the capability.

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

capabilityId -> (string)

Returns a system-assigned unique identifier for the capability.

capabilityArn -> (string)

Returns an Amazon Resource Name (ARN) for a specific Amazon Web Services resource, such as a capability, partnership, profile, or transformer.

name -> (string)

Returns the name of the capability, used to identify it.

type -> (string)

Returns the type of the capability. Currently, only `edi` is supported.

configuration -> (tagged union structure)

Returns a structure that contains the details for a capability.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `edi`.

edi -> (structure)

An EDI (electronic data interchange) configuration object.

capabilityDirection -> (string)

Specifies whether this is capability is for inbound or outbound transformations.

type -> (tagged union structure)

Returns the type of the capability. Currently, only `edi` is supported.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `x12Details`.

x12Details -> (structure)

Returns the details for the EDI standard that is being used for the transformer. Currently, only X12 is supported. X12 is a set of standards and corresponding messages that define specific business documents.

transactionSet -> (string)

Returns an enumerated type where each value identifies an X12 transaction set. Transaction sets are maintained by the X12 Accredited Standards Committee.

version -> (string)

Returns the version to use for the specified X12 transaction set.

inputLocation -> (structure)

Contains the Amazon S3 bucket and prefix for the location of the input file, which is contained in an `S3Location` object.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

key -> (string)

Specifies the Amazon S3 key for the file location.

outputLocation -> (structure)

Contains the Amazon S3 bucket and prefix for the location of the output file, which is contained in an `S3Location` object.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

key -> (string)

Specifies the Amazon S3 key for the file location.

transformerId -> (string)

Returns the system-assigned unique identifier for the transformer.

instructionsDocuments -> (list)

Returns one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the documentâs location.

(structure)

Specifies the details for the Amazon S3 file location that is being used with Amazon Web Services B2B Data Interchange. File locations in Amazon S3 are identified using a combination of the bucket and key.

bucketName -> (string)

Specifies the name of the Amazon S3 bucket.

key -> (string)

Specifies the Amazon S3 key for the file location.

createdAt -> (timestamp)

Returns a timestamp for creation date and time of the capability.

modifiedAt -> (timestamp)

Returns a timestamp for last time the capability was modified.