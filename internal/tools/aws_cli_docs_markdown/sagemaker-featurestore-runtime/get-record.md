# get-recordÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/get-record.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/get-record.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker-featurestore-runtime](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker-featurestore-runtime/index.html#cli-aws-sagemaker-featurestore-runtime) ]

# get-record

## Description

Use for `OnlineStore` serving from a `FeatureStore` . Only the latest records stored in the `OnlineStore` can be retrieved. If no Record with `RecordIdentifierValue` is found, then an empty result is returned.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-featurestore-runtime-2020-07-01/GetRecord)

## Synopsis

```
get-record
--feature-group-name <value>
--record-identifier-value-as-string <value>
[--feature-names <value>]
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

`--feature-group-name` (string)

The name or Amazon Resource Name (ARN) of the feature group from which you want to retrieve a record.

`--record-identifier-value-as-string` (string)

The value that corresponds to `RecordIdentifier` type and uniquely identifies the record in the `FeatureGroup` .

`--feature-names` (list)

List of names of Features to be retrieved. If not specified, the latest value for all the Features are returned.

(string)

Syntax:

```
"string" "string" ...
```

`--expiration-time-response` (string)

Parameter to request `ExpiresAt` in response. If `Enabled` , `GetRecord` will return the value of `ExpiresAt` , if it is not null. If `Disabled` and null, `GetRecord` will return null.

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

Record -> (list)

The record you requested. A list of `FeatureValues` .

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