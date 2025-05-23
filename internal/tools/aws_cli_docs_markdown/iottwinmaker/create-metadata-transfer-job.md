# create-metadata-transfer-jobÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/create-metadata-transfer-job.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/create-metadata-transfer-job.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [iottwinmaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iottwinmaker/index.html#cli-aws-iottwinmaker) ]

# create-metadata-transfer-job

## Description

Creates a new metadata transfer job.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/iottwinmaker-2021-11-29/CreateMetadataTransferJob)

## Synopsis

```
create-metadata-transfer-job
[--metadata-transfer-job-id <value>]
[--description <value>]
--sources <value>
--destination <value>
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

`--metadata-transfer-job-id` (string)

The metadata transfer job Id.

`--description` (string)

The metadata transfer job description.

`--sources` (list)

The metadata transfer job sources.

(structure)

The source configuration.

type -> (string)

The source configuration type.

s3Configuration -> (structure)

The source configuration S3 configuration.

location -> (string)

The S3 destination source configuration location.

iotSiteWiseConfiguration -> (structure)

The source configuration IoT SiteWise configuration.

filters -> (list)

The AWS IoT SiteWise soucre configuration filters.

(tagged union structure)

The AWS IoT SiteWise soucre configuration filter.[need held with desc here]

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `filterByAssetModel`, `filterByAsset`.

filterByAssetModel -> (structure)

Filter by asset model.

assetModelId -> (string)

The asset model Id.

assetModelExternalId -> (string)

The external-Id property of an asset model.

includeOffspring -> (boolean)

Include asset offspring. [need desc.]

includeAssets -> (boolean)

Bolean to include assets.

filterByAsset -> (structure)

Filter by asset.

assetId -> (string)

Filter by asset Id.

assetExternalId -> (string)

The external-Id property of an asset.

includeOffspring -> (boolean)

Includes sub-assets.[need description hekp for this]

includeAssetModel -> (boolean)

Boolean to include the asset model.

iotTwinMakerConfiguration -> (structure)

The source configuration IoT TwinMaker configuration.

workspace -> (string)

The IoT TwinMaker workspace.

filters -> (list)

The metadata transfer job AWS IoT TwinMaker source configuration filters.

(tagged union structure)

The metadata transfer job AWS IoT TwinMaker source configuration filter.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `filterByComponentType`, `filterByEntity`.

filterByComponentType -> (structure)

Filter by component type.

componentTypeId -> (string)

The component type Id.

filterByEntity -> (structure)

Filter by entity.

entityId -> (string)

The entity Id.

JSON Syntax:

```
[
  {
    "type": "s3"|"iotsitewise"|"iottwinmaker",
    "s3Configuration": {
      "location": "string"
    },
    "iotSiteWiseConfiguration": {
      "filters": [
        {
          "filterByAssetModel": {
            "assetModelId": "string",
            "assetModelExternalId": "string",
            "includeOffspring": true|false,
            "includeAssets": true|false
          },
          "filterByAsset": {
            "assetId": "string",
            "assetExternalId": "string",
            "includeOffspring": true|false,
            "includeAssetModel": true|false
          }
        }
        ...
      ]
    },
    "iotTwinMakerConfiguration": {
      "workspace": "string",
      "filters": [
        {
          "filterByComponentType": {
            "componentTypeId": "string"
          },
          "filterByEntity": {
            "entityId": "string"
          }
        }
        ...
      ]
    }
  }
  ...
]
```

`--destination` (structure)

The metadata transfer job destination.

type -> (string)

The destination type.

s3Configuration -> (structure)

The metadata transfer job S3 configuration. [need to add S3 entity]

location -> (string)

The S3 destination configuration location.

iotTwinMakerConfiguration -> (structure)

The metadata transfer job Amazon Web Services IoT TwinMaker configuration.

workspace -> (string)

The IoT TwinMaker workspace.

Shorthand Syntax:

```
type=string,s3Configuration={location=string},iotTwinMakerConfiguration={workspace=string}
```

JSON Syntax:

```
{
  "type": "s3"|"iotsitewise"|"iottwinmaker",
  "s3Configuration": {
    "location": "string"
  },
  "iotTwinMakerConfiguration": {
    "workspace": "string"
  }
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

metadataTransferJobId -> (string)

The metadata transfer job Id.

arn -> (string)

The metadata transfer job ARN.

creationDateTime -> (timestamp)

The The metadata transfer job creation DateTime property.

status -> (structure)

The metadata transfer job response status.

state -> (string)

The metadata transfer job state.

error -> (structure)

The metadata transfer job error.

code -> (string)

The error code.

message -> (string)

The error message.

queuedPosition -> (integer)

The queued position.