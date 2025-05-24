# describe-asset-composite-modelÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-composite-model.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/describe-asset-composite-model.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iotsitewise](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsitewise/index.html#cli-aws-iotsitewise) ]

# describe-asset-composite-model

## Description

Retrieves information about an asset composite model (also known as an asset component). An `AssetCompositeModel` is an instance of an `AssetModelCompositeModel` . If you want to see information about the model this is based on, call [DescribeAssetModelCompositeModel](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DescribeAssetModelCompositeModel.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iotsitewise-2019-12-02/DescribeAssetCompositeModel)

## Synopsis

```
describe-asset-composite-model
--asset-id <value>
--asset-composite-model-id <value>
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

`--asset-id` (string)

The ID of the asset. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the *IoT SiteWise User Guide* .

`--asset-composite-model-id` (string)

The ID of a composite model on this asset. This can be either the actual ID in UUID format, or else `externalId:` followed by the external ID, if it has one. For more information, see [Referencing objects with external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-id-references) in the *IoT SiteWise User Guide* .

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

assetId -> (string)

The ID of the asset, in UUID format. This ID uniquely identifies the asset within IoT SiteWise and can be used with other IoT SiteWise APIs.

assetCompositeModelId -> (string)

The ID of a composite model on this asset.

assetCompositeModelExternalId -> (string)

An external ID to assign to the asset model.

If the composite model is a component-based composite model, or one nested inside a component model, you can only set the external ID using `UpdateAssetModelCompositeModel` and specifying the derived ID of the model or property from the created model itâs a part of.

assetCompositeModelPath -> (list)

The path to the composite model listing the parent composite models.

(structure)

Represents one level between a composite model and the root of the asset.

id -> (string)

The ID of the path segment.

name -> (string)

The name of the path segment.

assetCompositeModelName -> (string)

The unique, friendly name for the composite model.

assetCompositeModelDescription -> (string)

A description for the composite model.

assetCompositeModelType -> (string)

The composite model type. Valid values are `AWS/ALARM` , `CUSTOM` , or `AWS/L4E_ANOMALY` .

assetCompositeModelProperties -> (list)

The property definitions of the composite model that was used to create the asset.

(structure)

Contains asset property information.

id -> (string)

The ID of the asset property.

name -> (string)

The name of the property.

alias -> (string)

The alias that identifies the property, such as an OPC-UA server data stream path (for example, `/company/windfarm/3/turbine/7/temperature` ). For more information, see [Mapping industrial data streams to asset properties](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/connect-data-streams.html) in the *IoT SiteWise User Guide* .

notification -> (structure)

The asset propertyâs notification topic and state. For more information, see [UpdateAssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_UpdateAssetProperty.html) .

topic -> (string)

The MQTT topic to which IoT SiteWise publishes property value update notifications.

state -> (string)

The current notification state.

dataType -> (string)

The data type of the asset property.

dataTypeSpec -> (string)

The data type of the structure for this property. This parameter exists on properties that have the `STRUCT` data type.

unit -> (string)

The unit (such as `Newtons` or `RPM` ) of the asset property.

path -> (list)

The structured path to the property from the root of the asset.

(structure)

Represents one level between a property and the root of the asset.

id -> (string)

The ID of the path segment.

name -> (string)

The name of the path segment.

externalId -> (string)

The external ID of the asset property. For more information, see [Using external IDs](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/object-ids.html#external-ids) in the *IoT SiteWise User Guide* .

assetCompositeModelSummaries -> (list)

The list of composite model summaries.

(structure)

Contains a summary of the composite model for a specific asset.

id -> (string)

The ID of the composite model that this summary describes.

externalId -> (string)

An external ID to assign to the asset model.

If the composite model is a derived composite model, or one nested inside a component model, you can only set the external ID using `UpdateAssetModelCompositeModel` and specifying the derived ID of the model or property from the created model itâs a part of.

name -> (string)

The name of the composite model that this summary describes.

type -> (string)

The type of asset model.

- **ASSET_MODEL** â (default) An asset model that you can use to create assets. Canât be included as a component in another asset model.
- **COMPONENT_MODEL** â A reusable component that you can include in the composite models of other asset models. You canât create assets directly from this type of asset model.

description -> (string)

A description of the composite model that this summary describes.

path -> (list)

The path that includes all the components of the asset model for the asset.

(structure)

Represents one level between a composite model and the root of the asset.

id -> (string)

The ID of the path segment.

name -> (string)

The name of the path segment.

actionDefinitions -> (list)

The available actions for a composite model on this asset.

(structure)

Contains a definition for an action.

actionDefinitionId -> (string)

The ID of the action definition.

actionName -> (string)

The name of the action definition.

actionType -> (string)

The type of the action definition.