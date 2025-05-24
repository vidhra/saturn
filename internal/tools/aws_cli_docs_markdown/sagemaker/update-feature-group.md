# update-feature-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-feature-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-feature-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# update-feature-group

## Description

Updates the feature group by either adding features or updating the online store configuration. Use one of the following request parameters at a time while using the `UpdateFeatureGroup` API.

You can add features for your feature group using the `FeatureAdditions` request parameter. Features cannot be removed from a feature group.

You can update the online store configuration by using the `OnlineStoreConfig` request parameter. If a `TtlDuration` is specified, the default `TtlDuration` applies for all records added to the feature group *after the feature group is updated* . If a record level `TtlDuration` exists from using the `PutRecord` API, the record level `TtlDuration` applies to that record instead of the default `TtlDuration` . To remove the default `TtlDuration` from an existing feature group, use the `UpdateFeatureGroup` API and set the `TtlDuration` `Unit` and `Value` to `null` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateFeatureGroup)

## Synopsis

```
update-feature-group
--feature-group-name <value>
[--feature-additions <value>]
[--online-store-config <value>]
[--throughput-config <value>]
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

The name or Amazon Resource Name (ARN) of the feature group that youâre updating.

`--feature-additions` (list)

Updates the feature group. Updating a feature group is an asynchronous operation. When you get an HTTP 200 response, youâve made a valid request. It takes some time after youâve made a valid request for Feature Store to update the feature group.

(structure)

A list of features. You must include `FeatureName` and `FeatureType` . Valid feature `FeatureType` s are `Integral` , `Fractional` and `String` .

FeatureName -> (string)

The name of a feature. The type must be a string. `FeatureName` cannot be any of the following: `is_deleted` , `write_time` , `api_invocation_time` .

The name:

- Must start with an alphanumeric character.
- Can only include alphanumeric characters, underscores, and hyphens. Spaces are not allowed.

FeatureType -> (string)

The value type of a feature. Valid values are Integral, Fractional, or String.

CollectionType -> (string)

A grouping of elements where each element within the collection must have the same feature type (`String` , `Integral` , or `Fractional` ).

- `List` : An ordered collection of elements.
- `Set` : An unordered collection of unique elements.
- `Vector` : A specialized list that represents a fixed-size array of elements. The vector dimension is determined by you. Must have elements with fractional feature types.

CollectionConfig -> (tagged union structure)

Configuration for your collection.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `VectorConfig`.

VectorConfig -> (structure)

Configuration for your vector collection type.

- `Dimension` : The number of elements in your vector.

Dimension -> (integer)

The number of elements in your vector.

Shorthand Syntax:

```
FeatureName=string,FeatureType=string,CollectionType=string,CollectionConfig={VectorConfig={Dimension=integer}} ...
```

JSON Syntax:

```
[
  {
    "FeatureName": "string",
    "FeatureType": "Integral"|"Fractional"|"String",
    "CollectionType": "List"|"Set"|"Vector",
    "CollectionConfig": {
      "VectorConfig": {
        "Dimension": integer
      }
    }
  }
  ...
]
```

`--online-store-config` (structure)

Updates the feature group online store configuration.

TtlDuration -> (structure)

Time to live duration, where the record is hard deleted after the expiration time is reached; `ExpiresAt` = `EventTime` + `TtlDuration` . For information on HardDelete, see the [DeleteRecord](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_feature_store_DeleteRecord.html) API in the Amazon SageMaker API Reference guide.

Unit -> (string)

`TtlDuration` time unit.

Value -> (integer)

`TtlDuration` time value.

Shorthand Syntax:

```
TtlDuration={Unit=string,Value=integer}
```

JSON Syntax:

```
{
  "TtlDuration": {
    "Unit": "Seconds"|"Minutes"|"Hours"|"Days"|"Weeks",
    "Value": integer
  }
}
```

`--throughput-config` (structure)

The new throughput configuration for the feature group. You can switch between on-demand and provisioned modes or update the read / write capacity of provisioned feature groups. You can switch a feature group to on-demand only once in a 24 hour period.

ThroughputMode -> (string)

Target throughput mode of the feature group. Throughput update is an asynchronous operation, and the outcome should be monitored by polling `LastUpdateStatus` field in `DescribeFeatureGroup` response. You cannot update a feature groupâs throughput while another update is in progress.

ProvisionedReadCapacityUnits -> (integer)

For provisioned feature groups with online store enabled, this indicates the read throughput you are billed for and can consume without throttling.

ProvisionedWriteCapacityUnits -> (integer)

For provisioned feature groups, this indicates the write throughput you are billed for and can consume without throttling.

Shorthand Syntax:

```
ThroughputMode=string,ProvisionedReadCapacityUnits=integer,ProvisionedWriteCapacityUnits=integer
```

JSON Syntax:

```
{
  "ThroughputMode": "OnDemand"|"Provisioned",
  "ProvisionedReadCapacityUnits": integer,
  "ProvisionedWriteCapacityUnits": integer
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

FeatureGroupArn -> (string)

The Amazon Resource Number (ARN) of the feature group that youâre updating.