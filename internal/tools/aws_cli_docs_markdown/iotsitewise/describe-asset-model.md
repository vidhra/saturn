# describe-asset-modelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-model.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-model.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotsitewise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/index.html#cli-aws-iotsitewise) ]

# describe-asset-model

## Description

Retrieves information about an asset model.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotsitewise-2019-12-02/DescribeAssetModel)

## Synopsis

```
describe-asset-model
--asset-model-id <value>
[--exclude-properties | --no-exclude-properties]
[--asset-model-version <value>]
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

`--asset-model-id` (string)

The ID of the asset model. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the *IoT SiteWise User Guide* .

`--exclude-properties` | `--no-exclude-properties` (boolean)

Whether or not to exclude asset model properties from the response.

`--asset-model-version` (string)

The version alias that specifies the latest or active version of the asset model. The details are returned in the response. The default value is `LATEST` . See [Asset model versions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html) in the *IoT SiteWise User Guide* .

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

**To describe an asset model**

The following `describe-asset-model` example describes a wind farm asset model.

```
aws iotsitewise describe-asset-model \
    --asset-model-id a1b2c3d4-5678-90ab-cdef-22222EXAMPLE
```

Output:

```
{
    "assetModelId": "a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
    "assetModelArn": "arn:aws:iotsitewise:us-west-2:123456789012:asset-model/a1b2c3d4-5678-90ab-cdef-22222EXAMPLE",
    "assetModelName": "Wind Farm Model",
    "assetModelDescription": "Represents a wind farm that comprises many wind turbines",
    "assetModelProperties": [
        {
            "id": "a1b2c3d4-5678-90ab-cdef-99999EXAMPLE",
            "name": "Total Generated Power",
            "dataType": "DOUBLE",
            "unit": "kW",
            "type": {
                "metric": {
                    "expression": "sum(power)",
                    "variables": [
                        {
                            "name": "power",
                            "value": {
                                "propertyId": "a1b2c3d4-5678-90ab-cdef-66666EXAMPLE",
                                "hierarchyId": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE"
                            }
                        }
                    ],
                    "window": {
                        "tumbling": {
                            "interval": "1h"
                        }
                    }
                }
            }
        },
        {
            "id": "a1b2c3d4-5678-90ab-cdef-88888EXAMPLE",
            "name": "Region",
            "dataType": "STRING",
            "type": {
                "attribute": {
                    "defaultValue": " "
                }
            }
        }
    ],
    "assetModelHierarchies": [
        {
            "id": "a1b2c3d4-5678-90ab-cdef-77777EXAMPLE",
            "name": "Wind Turbines",
            "childAssetModelId": "a1b2c3d4-5678-90ab-cdef-11111EXAMPLE"
        }
    ],
    "assetModelCreationDate": 1575671284.0,
    "assetModelLastUpdateDate": 1575671988.0,
    "assetModelStatus": {
        "state": "ACTIVE"
    }
}
```

For more information, see [Describing a specific asset model](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/discover-asset-resources.html#describe-asset-model) in the *AWS IoT SiteWise User Guide*.

## Output

assetModelId -> (string)

The ID of the asset model, in UUID format.

assetModelExternalId -> (string)

The external ID of the asset model, if any.

assetModelArn -> (string)

The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the asset model, which has the following format.

`arn:${Partition}:iotsitewise:${Region}:${Account}:asset-model/${AssetModelId}`

assetModelName -> (string)

The name of the asset model.

assetModelType -> (string)

The type of asset model.

- **ASSET_MODEL** â (default) An asset model that you can use to create assets. Canât be included as a component in another asset model.
- **COMPONENT_MODEL** â A reusable component that you can include in the composite models of other asset models. You canât create assets directly from this type of asset model.

assetModelDescription -> (string)

The asset modelâs description.

assetModelProperties -> (list)

The list of asset properties for the asset model.

This object doesnât include properties that you define in composite models. You can find composite model properties in the `assetModelCompositeModels` object.

(structure)

Contains information about an asset model property.

id -> (string)

The ID of the asset model property.

- If you are callling [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) to create a *new* property: You can specify its ID here, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
- If you are calling UpdateAssetModel to modify an *existing* property: This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the *IoT SiteWise User Guide* .

externalId -> (string)

The external ID (if any) provided in the [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html) or [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) operation. You can assign an external ID by specifying this value as part of a call to [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) . However, you canât change the external ID if one is already assigned. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

name -> (string)

The name of the asset model property.

dataType -> (string)

The data type of the asset model property.

If you specify `STRUCT` , you must also specify `dataTypeSpec` to identify the type of the structure for this property.

dataTypeSpec -> (string)

The data type of the structure for this property. This parameter exists on properties that have the `STRUCT` data type.

unit -> (string)

The unit of the asset model property, such as `Newtons` or `RPM` .

type -> (structure)

The property type (see `PropertyType` ).

attribute -> (structure)

Specifies an asset attribute property. An attribute generally contains static information, such as the serial number of an [IIoT](https://en.wikipedia.org/wiki/Internet_of_things#Industrial_applications) wind turbine.

defaultValue -> (string)

The default value of the asset model property attribute. All assets that you create from the asset model contain this attribute value. You can update an attributeâs value after you create an asset. For more information, see [Updating attribute values](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-attribute-values.html) in the *IoT SiteWise User Guide* .

measurement -> (structure)

Specifies an asset measurement property. A measurement represents a deviceâs raw sensor data stream, such as timestamped temperature values or timestamped power values.

processingConfig -> (structure)

The processing configuration for the given measurement property. You can configure measurements to be kept at the edge or forwarded to the Amazon Web Services Cloud. By default, measurements are forwarded to the cloud.

forwardingConfig -> (structure)

The forwarding configuration for the given measurement property.

state -> (string)

The forwarding state for the given property.

transform -> (structure)

Specifies an asset transform property. A transform contains a mathematical expression that maps a propertyâs data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.

expression -> (string)

The mathematical expression that defines the transformation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.

For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the *IoT SiteWise User Guide* .

variables -> (list)

The list of variables used in the expression.

(structure)

Contains expression variable information.

name -> (string)

The friendly name of the variable to be used in the expression.

value -> (structure)

The variable that identifies an asset property from which to use values.

propertyId -> (string)

The ID of the property to use as the variable. You can use the property `name` if itâs from the same asset model. If the property has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

hierarchyId -> (string)

The ID of the hierarchy to query for the property ID. You can use the hierarchyâs name instead of the hierarchyâs ID. If the hierarchy has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same `propertyId` . For example, you might have separately grouped assets that come from the same asset model. For more information, see [Asset hierarchies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html) in the *IoT SiteWise User Guide* .

propertyPath -> (list)

The path of the property.

(structure)

Represents one level between a property and the root of the asset model.

id -> (string)

The ID of the path segment.

name -> (string)

The name of the path segment.

processingConfig -> (structure)

The processing configuration for the given transform property. You can configure transforms to be kept at the edge or forwarded to the Amazon Web Services Cloud. You can also configure transforms to be computed at the edge or in the cloud.

computeLocation -> (string)

The compute location for the given transform property.

forwardingConfig -> (structure)

The forwarding configuration for a given property.

state -> (string)

The forwarding state for the given property.

metric -> (structure)

Specifies an asset metric property. A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.

expression -> (string)

The mathematical expression that defines the metric aggregation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.

For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the *IoT SiteWise User Guide* .

variables -> (list)

The list of variables used in the expression.

(structure)

Contains expression variable information.

name -> (string)

The friendly name of the variable to be used in the expression.

value -> (structure)

The variable that identifies an asset property from which to use values.

propertyId -> (string)

The ID of the property to use as the variable. You can use the property `name` if itâs from the same asset model. If the property has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

hierarchyId -> (string)

The ID of the hierarchy to query for the property ID. You can use the hierarchyâs name instead of the hierarchyâs ID. If the hierarchy has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same `propertyId` . For example, you might have separately grouped assets that come from the same asset model. For more information, see [Asset hierarchies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html) in the *IoT SiteWise User Guide* .

propertyPath -> (list)

The path of the property.

(structure)

Represents one level between a property and the root of the asset model.

id -> (string)

The ID of the path segment.

name -> (string)

The name of the path segment.

window -> (structure)

The window (time interval) over which IoT SiteWise computes the metricâs aggregation expression. IoT SiteWise computes one data point per `window` .

tumbling -> (structure)

The tumbling time interval window.

interval -> (string)

The time interval for the tumbling window. The interval time must be between 1 minute and 1 week.

IoT SiteWise computes the `1w` interval the end of Sunday at midnight each week (UTC), the `1d` interval at the end of each day at midnight (UTC), the `1h` interval at the end of each hour, and so on.

When IoT SiteWise aggregates data points for metric computations, the start of each interval is exclusive and the end of each interval is inclusive. IoT SiteWise places the computed data point at the end of the interval.

offset -> (string)

The offset for the tumbling window. The `offset` parameter accepts the following:

- The offset time. For example, if you specify `18h` for `offset` and `1d` for `interval` , IoT SiteWise aggregates data in one of the following ways:
- If you create the metric before or at 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) on the day when you create the metric.
- If you create the metric after 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) the next day.
- The ISO 8601 format. For example, if you specify `PT18H` for `offset` and `1d` for `interval` , IoT SiteWise aggregates data in one of the following ways:
- If you create the metric before or at 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) on the day when you create the metric.
- If you create the metric after 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) the next day.
- The 24-hour clock. For example, if you specify `00:03:00` for `offset` , `5m` for `interval` , and you create the metric at 2 PM (UTC), you get the first aggregation result at 2:03 PM (UTC). You get the second aggregation result at 2:08 PM (UTC).
- The offset time zone. For example, if you specify `2021-07-23T18:00-08` for `offset` and `1d` for `interval` , IoT SiteWise aggregates data in one of the following ways:
- If you create the metric before or at 6 PM (PST), you get the first aggregation result at 6 PM (PST) on the day when you create the metric.
- If you create the metric after 6 PM (PST), you get the first aggregation result at 6 PM (PST) the next day.

processingConfig -> (structure)

The processing configuration for the given metric property. You can configure metrics to be computed at the edge or in the Amazon Web Services Cloud. By default, metrics are forwarded to the cloud.

computeLocation -> (string)

The compute location for the given metric property.

path -> (list)

The structured path to the property from the root of the asset model.

(structure)

Represents one level between a property and the root of the asset model.

id -> (string)

The ID of the path segment.

name -> (string)

The name of the path segment.

assetModelHierarchies -> (list)

A list of asset model hierarchies that each contain a `childAssetModelId` and a `hierarchyId` (named `id` ). A hierarchy specifies allowed parent/child asset relationships for an asset model.

(structure)

Describes an asset hierarchy that contains a hierarchyâs name, ID, and child asset model ID that specifies the type of asset that can be in this hierarchy.

id -> (string)

The ID of the asset model hierarchy. This ID is a `hierarchyId` .

- If you are callling [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) to create a *new* hierarchy: You can specify its ID here, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
- If you are calling UpdateAssetModel to modify an *existing* hierarchy: This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the *IoT SiteWise User Guide* .

externalId -> (string)

The external ID (if any) provided in the [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html) or [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) operation. You can assign an external ID by specifying this value as part of a call to [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) . However, you canât change the external ID if one is already assigned. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

name -> (string)

The name of the asset model hierarchy that you specify by using the [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html) or [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) API operation.

childAssetModelId -> (string)

The ID of the asset model, in UUID format. All assets in this hierarchy must be instances of the `childAssetModelId` asset model. IoT SiteWise will always return the actual asset model ID for this value. However, when you are specifying this value as part of a call to [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) , you may provide either the asset model ID or else `externalId:` followed by the asset modelâs external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

assetModelCompositeModels -> (list)

The list of built-in composite models for the asset model, such as those with those of type `AWS/ALARMS` .

(structure)

Contains information about a composite model in an asset model. This object contains the asset property definitions that you define in the composite model.

name -> (string)

The name of the composite model.

description -> (string)

The description of the composite model.

type -> (string)

The type of the composite model. For alarm composite models, this type is `AWS/ALARM` .

properties -> (list)

The asset property definitions for this composite model.

(structure)

Contains information about an asset model property.

id -> (string)

The ID of the asset model property.

- If you are callling [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) to create a *new* property: You can specify its ID here, if desired. IoT SiteWise automatically generates a unique ID for you, so this parameter is never required. However, if you prefer to supply your own ID instead, you can specify it here in UUID format. If you specify your own ID, it must be globally unique.
- If you are calling UpdateAssetModel to modify an *existing* property: This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the *IoT SiteWise User Guide* .

externalId -> (string)

The external ID (if any) provided in the [CreateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_CreateAssetModel.html) or [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) operation. You can assign an external ID by specifying this value as part of a call to [UpdateAssetModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetModel.html) . However, you canât change the external ID if one is already assigned. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

name -> (string)

The name of the asset model property.

dataType -> (string)

The data type of the asset model property.

If you specify `STRUCT` , you must also specify `dataTypeSpec` to identify the type of the structure for this property.

dataTypeSpec -> (string)

The data type of the structure for this property. This parameter exists on properties that have the `STRUCT` data type.

unit -> (string)

The unit of the asset model property, such as `Newtons` or `RPM` .

type -> (structure)

The property type (see `PropertyType` ).

attribute -> (structure)

Specifies an asset attribute property. An attribute generally contains static information, such as the serial number of an [IIoT](https://en.wikipedia.org/wiki/Internet_of_things#Industrial_applications) wind turbine.

defaultValue -> (string)

The default value of the asset model property attribute. All assets that you create from the asset model contain this attribute value. You can update an attributeâs value after you create an asset. For more information, see [Updating attribute values](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/update-attribute-values.html) in the *IoT SiteWise User Guide* .

measurement -> (structure)

Specifies an asset measurement property. A measurement represents a deviceâs raw sensor data stream, such as timestamped temperature values or timestamped power values.

processingConfig -> (structure)

The processing configuration for the given measurement property. You can configure measurements to be kept at the edge or forwarded to the Amazon Web Services Cloud. By default, measurements are forwarded to the cloud.

forwardingConfig -> (structure)

The forwarding configuration for the given measurement property.

state -> (string)

The forwarding state for the given property.

transform -> (structure)

Specifies an asset transform property. A transform contains a mathematical expression that maps a propertyâs data points from one form to another, such as a unit conversion from Celsius to Fahrenheit.

expression -> (string)

The mathematical expression that defines the transformation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.

For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the *IoT SiteWise User Guide* .

variables -> (list)

The list of variables used in the expression.

(structure)

Contains expression variable information.

name -> (string)

The friendly name of the variable to be used in the expression.

value -> (structure)

The variable that identifies an asset property from which to use values.

propertyId -> (string)

The ID of the property to use as the variable. You can use the property `name` if itâs from the same asset model. If the property has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

hierarchyId -> (string)

The ID of the hierarchy to query for the property ID. You can use the hierarchyâs name instead of the hierarchyâs ID. If the hierarchy has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same `propertyId` . For example, you might have separately grouped assets that come from the same asset model. For more information, see [Asset hierarchies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html) in the *IoT SiteWise User Guide* .

propertyPath -> (list)

The path of the property.

(structure)

Represents one level between a property and the root of the asset model.

id -> (string)

The ID of the path segment.

name -> (string)

The name of the path segment.

processingConfig -> (structure)

The processing configuration for the given transform property. You can configure transforms to be kept at the edge or forwarded to the Amazon Web Services Cloud. You can also configure transforms to be computed at the edge or in the cloud.

computeLocation -> (string)

The compute location for the given transform property.

forwardingConfig -> (structure)

The forwarding configuration for a given property.

state -> (string)

The forwarding state for the given property.

metric -> (structure)

Specifies an asset metric property. A metric contains a mathematical expression that uses aggregate functions to process all input data points over a time interval and output a single data point, such as to calculate the average hourly temperature.

expression -> (string)

The mathematical expression that defines the metric aggregation function. You can specify up to 10 variables per expression. You can specify up to 10 functions per expression.

For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the *IoT SiteWise User Guide* .

variables -> (list)

The list of variables used in the expression.

(structure)

Contains expression variable information.

name -> (string)

The friendly name of the variable to be used in the expression.

value -> (structure)

The variable that identifies an asset property from which to use values.

propertyId -> (string)

The ID of the property to use as the variable. You can use the property `name` if itâs from the same asset model. If the property has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

hierarchyId -> (string)

The ID of the hierarchy to query for the property ID. You can use the hierarchyâs name instead of the hierarchyâs ID. If the hierarchy has an external ID, you can specify `externalId:` followed by the external ID. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

You use a hierarchy ID instead of a model ID because you can have several hierarchies using the same model and therefore the same `propertyId` . For example, you might have separately grouped assets that come from the same asset model. For more information, see [Asset hierarchies](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/asset-hierarchies.html) in the *IoT SiteWise User Guide* .

propertyPath -> (list)

The path of the property.

(structure)

Represents one level between a property and the root of the asset model.

id -> (string)

The ID of the path segment.

name -> (string)

The name of the path segment.

window -> (structure)

The window (time interval) over which IoT SiteWise computes the metricâs aggregation expression. IoT SiteWise computes one data point per `window` .

tumbling -> (structure)

The tumbling time interval window.

interval -> (string)

The time interval for the tumbling window. The interval time must be between 1 minute and 1 week.

IoT SiteWise computes the `1w` interval the end of Sunday at midnight each week (UTC), the `1d` interval at the end of each day at midnight (UTC), the `1h` interval at the end of each hour, and so on.

When IoT SiteWise aggregates data points for metric computations, the start of each interval is exclusive and the end of each interval is inclusive. IoT SiteWise places the computed data point at the end of the interval.

offset -> (string)

The offset for the tumbling window. The `offset` parameter accepts the following:

- The offset time. For example, if you specify `18h` for `offset` and `1d` for `interval` , IoT SiteWise aggregates data in one of the following ways:
- If you create the metric before or at 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) on the day when you create the metric.
- If you create the metric after 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) the next day.
- The ISO 8601 format. For example, if you specify `PT18H` for `offset` and `1d` for `interval` , IoT SiteWise aggregates data in one of the following ways:
- If you create the metric before or at 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) on the day when you create the metric.
- If you create the metric after 6 PM (UTC), you get the first aggregation result at 6 PM (UTC) the next day.
- The 24-hour clock. For example, if you specify `00:03:00` for `offset` , `5m` for `interval` , and you create the metric at 2 PM (UTC), you get the first aggregation result at 2:03 PM (UTC). You get the second aggregation result at 2:08 PM (UTC).
- The offset time zone. For example, if you specify `2021-07-23T18:00-08` for `offset` and `1d` for `interval` , IoT SiteWise aggregates data in one of the following ways:
- If you create the metric before or at 6 PM (PST), you get the first aggregation result at 6 PM (PST) on the day when you create the metric.
- If you create the metric after 6 PM (PST), you get the first aggregation result at 6 PM (PST) the next day.

processingConfig -> (structure)

The processing configuration for the given metric property. You can configure metrics to be computed at the edge or in the Amazon Web Services Cloud. By default, metrics are forwarded to the cloud.

computeLocation -> (string)

The compute location for the given metric property.

path -> (list)

The structured path to the property from the root of the asset model.

(structure)

Represents one level between a property and the root of the asset model.

id -> (string)

The ID of the path segment.

name -> (string)

The name of the path segment.

id -> (string)

The ID of the asset model composite model.

externalId -> (string)

The external ID of the asset model composite model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

assetModelCompositeModelSummaries -> (list)

The list of the immediate child custom composite model summaries for the asset model.

(structure)

Contains a summary of the composite model.

id -> (string)

The ID of the composite model that this summary describes..

externalId -> (string)

The external ID of a composite model on this asset model. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

name -> (string)

The name of the composite model that this summary describes..

type -> (string)

The composite model type. Valid values are `AWS/ALARM` , `CUSTOM` , or `AWS/L4E_ANOMALY` .

description -> (string)

The description of the composite model that this summary describes..

path -> (list)

The path that includes all the pieces that make up the composite model.

(structure)

Represents one level between a composite model and the root of the asset model.

id -> (string)

The ID of the path segment.

name -> (string)

The name of the path segment.

assetModelCreationDate -> (timestamp)

The date the asset model was created, in Unix epoch time.

assetModelLastUpdateDate -> (timestamp)

The date the asset model was last updated, in Unix epoch time.

assetModelStatus -> (structure)

The current status of the asset model, which contains a state and any error message.

state -> (string)

The current state of the asset model.

error -> (structure)

Contains associated error information, if any.

code -> (string)

The error code.

message -> (string)

The error message.

details -> (list)

A list of detailed errors.

(structure)

Contains detailed error information.

code -> (string)

The error code.

message -> (string)

The error message.

assetModelVersion -> (string)

The version of the asset model. See [Asset model versions](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/model-active-version.html) in the *IoT SiteWise User Guide* .

eTag -> (string)

The entity tag (ETag) is a hash of the retrieved version of the asset model. Itâs used to make concurrent updates safely to the resource. See [Optimistic locking for asset model writes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html) in the *IoT SiteWise User Guide* .

See [Optimistic locking for asset model writes](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/opt-locking-for-model.html) in the *IoT SiteWise User Guide* .