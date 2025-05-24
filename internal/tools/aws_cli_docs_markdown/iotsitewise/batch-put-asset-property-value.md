# batch-put-asset-property-valueÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/batch-put-asset-property-value.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/batch-put-asset-property-value.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotsitewise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/index.html#cli-aws-iotsitewise) ]

# batch-put-asset-property-value

## Description

Sends a list of asset property values to IoT SiteWise. Each value is a timestamp-quality-value (TQV) data point. For more information, see [Ingesting data using the API](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api.html) in the *IoT SiteWise User Guide* .

To identify an asset property, you must specify one of the following:

- The `assetId` and `propertyId` of an asset property.
- A `propertyAlias` , which is a data stream alias (for example, `/company/windfarm/3/turbine/7/temperature` ). To define an asset propertyâs alias, see [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html) .

### Warning

With respect to Unix epoch time, IoT SiteWise accepts only TQVs that have a timestamp of no more than 7 days in the past and no more than 10 minutes in the future. IoT SiteWise rejects timestamps outside of the inclusive range of [-7 days, +10 minutes] and returns a `TimestampOutOfRangeException` error.

For each asset property, IoT SiteWise overwrites TQVs with duplicate timestamps unless the newer TQV has a different quality. For example, if you store a TQV `{T1, GOOD, V1}` , then storing `{T1, GOOD, V2}` replaces the existing TQV.

IoT SiteWise authorizes access to each `BatchPutAssetPropertyValue` entry individually. For more information, see [BatchPutAssetPropertyValue authorization](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/security_iam_service-with-iam.html#security_iam_service-with-iam-id-based-policies-batchputassetpropertyvalue-action) in the *IoT SiteWise User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotsitewise-2019-12-02/BatchPutAssetPropertyValue)

## Synopsis

```
batch-put-asset-property-value
[--enable-partial-entry-processing | --no-enable-partial-entry-processing]
--entries <value>
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

`--enable-partial-entry-processing` | `--no-enable-partial-entry-processing` (boolean)

This setting enables partial ingestion at entry-level. If set to `true` , we ingest all TQVs not resulting in an error. If set to `false` , an invalid TQV fails ingestion of the entire entry that contains it.

`--entries` (list)

The list of asset property value entries for the batch put request. You can specify up to 10 entries per request.

(structure)

Contains a list of value updates for an asset property in the list of asset entries consumed by the [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html) API operation.

entryId -> (string)

The user specified ID for the entry. You can use this ID to identify which entries failed.

assetId -> (string)

The ID of the asset to update.

propertyId -> (string)

The ID of the asset property for this entry.

propertyAlias -> (string)

The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature` ). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the *IoT SiteWise User Guide* .

propertyValues -> (list)

The list of property values to upload. You can specify up to 10 `propertyValues` array elements.

(structure)

Contains asset property value information.

value -> (structure)

The value of the asset property (see `Variant` ).

stringValue -> (string)

Asset property data of type string (sequence of characters). The allowed pattern: â^$|[^u0000-u001Fu007F]+â. The max length is 1024.

integerValue -> (integer)

Asset property data of type integer (whole number).

doubleValue -> (double)

Asset property data of type double (floating point number). The min value is -10^10. The max value is 10^10. Double.NaN is allowed.

booleanValue -> (boolean)

Asset property data of type Boolean (true or false).

nullValue -> (structure)

The type of null asset property data with BAD and UNCERTAIN qualities.

valueType -> (string)

The type of null asset property data.

timestamp -> (structure)

The timestamp of the asset property value.

timeInSeconds -> (long)

The timestamp date, in seconds, in the Unix epoch format. Fractional nanosecond data is provided by `offsetInNanos` .

offsetInNanos -> (integer)

The nanosecond offset from `timeInSeconds` .

quality -> (string)

The quality of the asset property value.

JSON Syntax:

```
[
  {
    "entryId": "string",
    "assetId": "string",
    "propertyId": "string",
    "propertyAlias": "string",
    "propertyValues": [
      {
        "value": {
          "stringValue": "string",
          "integerValue": integer,
          "doubleValue": double,
          "booleanValue": true|false,
          "nullValue": {
            "valueType": "D"|"B"|"S"|"I"|"U"
          }
        },
        "timestamp": {
          "timeInSeconds": long,
          "offsetInNanos": integer
        },
        "quality": "GOOD"|"BAD"|"UNCERTAIN"
      }
      ...
    ]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To send data to asset properties**

The following `batch-put-asset-property-value` example sends power and temperature data to the asset properties identified by property aliases.

```
aws iotsitewise batch-put-asset-property-value \
    --cli-input-json file://batch-put-asset-property-value.json
```

Contents of `batch-put-asset-property-value.json`:

```
{
    "entries": [
        {
            "entryId": "1575691200-company-windfarm-3-turbine-7-power",
            "propertyAlias": "company-windfarm-3-turbine-7-power",
            "propertyValues": [
                {
                    "value": {
                        "doubleValue": 4.92
                    },
                    "timestamp": {
                        "timeInSeconds": 1575691200
                    },
                    "quality": "GOOD"
                }
            ]
        },
        {
            "entryId": "1575691200-company-windfarm-3-turbine-7-temperature",
            "propertyAlias": "company-windfarm-3-turbine-7-temperature",
            "propertyValues": [
                {
                    "value": {
                        "integerValue": 38
                    },
                    "timestamp": {
                        "timeInSeconds": 1575691200
                    }
                }
            ]
        }
    ]
}
```

Output:

```
{
    "errorEntries": []
}
```

For more information, see [Ingesting data using the AWS IoT SiteWise API](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/ingest-api.html) in the *AWS IoT SiteWise User Guide*.

## Output

errorEntries -> (list)

A list of the errors (if any) associated with the batch put request. Each error entry contains the `entryId` of the entry that failed.

(structure)

Contains error information for asset property value entries that are associated with the [BatchPutAssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyValue.html) API.

entryId -> (string)

The ID of the failed entry.

errors -> (list)

The list of update property value errors.

(structure)

Contains error information from updating a batch of asset property values.

errorCode -> (string)

The error code.

errorMessage -> (string)

The associated error message.

timestamps -> (list)

A list of timestamps for each error, if any.

(structure)

Contains a timestamp with optional nanosecond granularity.

timeInSeconds -> (long)

The timestamp date, in seconds, in the Unix epoch format. Fractional nanosecond data is provided by `offsetInNanos` .

offsetInNanos -> (integer)

The nanosecond offset from `timeInSeconds` .