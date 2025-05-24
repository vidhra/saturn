# batch-get-recordÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/batch-get-record.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/batch-get-record.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker-featurestore-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/index.html#cli-aws-sagemaker-featurestore-runtime) ]

# batch-get-record

## Description

Retrieves a batch of `Records` from a `FeatureGroup` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-featurestore-runtime-2020-07-01/BatchGetRecord)

## Synopsis

```
batch-get-record
--identifiers <value>
[--expiration-time-response <value>]
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

`--identifiers` (list)

A list containing the name or Amazon Resource Name (ARN) of the `FeatureGroup` , the list of names of `Feature` s to be retrieved, and the corresponding `RecordIdentifier` values as strings.

(structure)

The identifier that identifies the batch of Records you are retrieving in a batch.

FeatureGroupName -> (string)

The name or Amazon Resource Name (ARN) of the `FeatureGroup` containing the records you are retrieving in a batch.

RecordIdentifiersValueAsString -> (list)

The value for a list of record identifiers in string format.

(string)

FeatureNames -> (list)

List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.

(string)

Shorthand Syntax:

```
FeatureGroupName=string,RecordIdentifiersValueAsString=string,string,FeatureNames=string,string ...
```

JSON Syntax:

```
[
  {
    "FeatureGroupName": "string",
    "RecordIdentifiersValueAsString": ["string", ...],
    "FeatureNames": ["string", ...]
  }
  ...
]
```

`--expiration-time-response` (string)

Parameter to request `ExpiresAt` in response. If `Enabled` , `BatchGetRecord` will return the value of `ExpiresAt` , if it is not null. If `Disabled` and null, `BatchGetRecord` will return null.

Possible values:

- `Enabled`
- `Disabled`

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

Records -> (list)

A list of Records you requested to be retrieved in batch.

(structure)

The output of records that have been retrieved in a batch.

FeatureGroupName -> (string)

The `FeatureGroupName` containing Records you retrieved in a batch.

RecordIdentifierValueAsString -> (string)

The value of the record identifier in string format.

Record -> (list)

The `Record` retrieved.

(structure)

The value associated with a feature.

FeatureName -> (string)

The name of a feature that a feature value corresponds to.

ValueAsString -> (string)

The value in string format associated with a feature. Used when your `CollectionType` is `None` . Note that features types can be `String` , `Integral` , or `Fractional` . This value represents all three types as a string.

ValueAsStringList -> (list)

The list of values in string format associated with a feature. Used when your `CollectionType` is a `List` , `Set` , or `Vector` . Note that features types can be `String` , `Integral` , or `Fractional` . These values represents all three types as a string.

(string)

ExpiresAt -> (string)

The `ExpiresAt` ISO string of the requested record.

Errors -> (list)

A list of errors that have occurred when retrieving a batch of Records.

(structure)

The error that has occurred when attempting to retrieve a batch of Records.

FeatureGroupName -> (string)

The name of the feature group that the record belongs to.

RecordIdentifierValueAsString -> (string)

The value for the `RecordIdentifier` in string format of a Record from a `FeatureGroup` that is causing an error when attempting to be retrieved.

ErrorCode -> (string)

The error code of an error that has occurred when attempting to retrieve a batch of Records. For more information on errors, see [Errors](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_GetRecord.html#API_feature_store_GetRecord_Errors) .

ErrorMessage -> (string)

The error message of an error that has occurred when attempting to retrieve a record in the batch.

UnprocessedIdentifiers -> (list)

A unprocessed list of `FeatureGroup` names, with their corresponding `RecordIdentifier` value, and Feature name.

(structure)

The identifier that identifies the batch of Records you are retrieving in a batch.

FeatureGroupName -> (string)

The name or Amazon Resource Name (ARN) of the `FeatureGroup` containing the records you are retrieving in a batch.

RecordIdentifiersValueAsString -> (list)

The value for a list of record identifiers in string format.

(string)

FeatureNames -> (list)

List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.

(string)