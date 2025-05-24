# copy-image-setÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/copy-image-set.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/copy-image-set.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [medical-imaging](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/medical-imaging/index.html#cli-aws-medical-imaging) ]

# copy-image-set

## Description

Copy an image set.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/medical-imaging-2023-07-19/CopyImageSet)

## Synopsis

```
copy-image-set
--datastore-id <value>
--source-image-set-id <value>
--copy-image-set-information <value>
[--force | --no-force]
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

`--datastore-id` (string)

The data store identifier.

`--source-image-set-id` (string)

The source image set identifier.

`--copy-image-set-information` (structure)

Copy image set information.

sourceImageSet -> (structure)

The source image set.

latestVersionId -> (string)

The latest version identifier for the source image set.

DICOMCopies -> (structure)

Contains `MetadataCopies` structure and wraps information related to specific copy use cases. For example, when copying subsets.

copiableAttributes -> (string)

The JSON string used to specify a subset of SOP Instances to copy from source to destination image set.

destinationImageSet -> (structure)

The destination image set.

imageSetId -> (string)

The image set identifier for the destination image set.

latestVersionId -> (string)

The latest version identifier for the destination image set.

Shorthand Syntax:

```
sourceImageSet={latestVersionId=string,DICOMCopies={copiableAttributes=string}},destinationImageSet={imageSetId=string,latestVersionId=string}
```

JSON Syntax:

```
{
  "sourceImageSet": {
    "latestVersionId": "string",
    "DICOMCopies": {
      "copiableAttributes": "string"
    }
  },
  "destinationImageSet": {
    "imageSetId": "string",
    "latestVersionId": "string"
  }
}
```

`--force` | `--no-force` (boolean)

Setting this flag will force the `CopyImageSet` operation, even if Patient, Study, or Series level metadata are mismatched across the `sourceImageSet` and `destinationImageSet` .

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

**Example 1: To copy an image set without a destination.**

The following `copy-image-set` example makes a duplicate copy of an image set without a destination.

```
aws medical-imaging copy-image-set \
    --datastore-id 12345678901234567890123456789012 \
    --source-image-set-id ea92b0d8838c72a3f25d00d13616f87e \
    --copy-image-set-information '{"sourceImageSet": {"latestVersionId": "1" } }'
```

Output:

```
{
    "destinationImageSetProperties": {
        "latestVersionId": "2",
        "imageSetWorkflowStatus": "COPYING",
        "updatedAt": 1680042357.432,
        "imageSetId": "b9a06fef182a5f992842f77f8e0868e5",
        "imageSetState": "LOCKED",
        "createdAt": 1680042357.432
    },
    "sourceImageSetProperties": {
        "latestVersionId": "1",
        "imageSetWorkflowStatus": "COPYING_WITH_READ_ONLY_ACCESS",
        "updatedAt": 1680042357.432,
        "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e",
        "imageSetState": "LOCKED",
        "createdAt": 1680027126.436
    },
    "datastoreId": "12345678901234567890123456789012"
}
```

**Example 2: To copy an image set with a destination.**

The following `copy-image-set` example makes a duplicate copy of an image set with a destination.

```
aws medical-imaging copy-image-set \
    --datastore-id 12345678901234567890123456789012 \
    --source-image-set-id ea92b0d8838c72a3f25d00d13616f87e \
    --copy-image-set-information '{"sourceImageSet": {"latestVersionId": "1" }, "destinationImageSet": { "imageSetId": "b9a06fef182a5f992842f77f8e0868e5", "latestVersionId": "1"} }'
```

Output:

```
{
    "destinationImageSetProperties": {
        "latestVersionId": "2",
        "imageSetWorkflowStatus": "COPYING",
        "updatedAt": 1680042505.135,
        "imageSetId": "b9a06fef182a5f992842f77f8e0868e5",
        "imageSetState": "LOCKED",
        "createdAt": 1680042357.432
    },
    "sourceImageSetProperties": {
        "latestVersionId": "1",
        "imageSetWorkflowStatus": "COPYING_WITH_READ_ONLY_ACCESS",
        "updatedAt": 1680042505.135,
        "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e",
        "imageSetState": "LOCKED",
        "createdAt": 1680027126.436
    },
    "datastoreId": "12345678901234567890123456789012"
}
```

**Example 3: To copy a subset of instances from a source image set to a destination image set.**

The following `copy-image-set` example copies one DICOM instance from the source image set to the destination image set.
The force parameter is provided to override inconsistencies in the Patient, Study, and Series level attributes.

```
aws medical-imaging copy-image-set \
    --datastore-id 12345678901234567890123456789012 \
    --source-image-set-id ea92b0d8838c72a3f25d00d13616f87e \
    --copy-image-set-information '{"sourceImageSet": {"latestVersionId": "1","DICOMCopies": {"copiableAttributes": "{\"SchemaVersion\":\"1.1\",\"Study\":{\"Series\":{\"1.3.6.1.4.1.5962.99.1.3673257865.2104868982.1369432891697.3666.0\":{\"Instances\":{\"1.3.6.1.4.1.5962.99.1.3673257865.2104868982.1369432891697.3669.0\":{}}}}}}"}},"destinationImageSet": {"imageSetId": "b9eb50d8ee682eb9fcf4acbf92f62bb7","latestVersionId": "1"}}' \
    --force
```

Output:

```
{
    "destinationImageSetProperties": {
        "latestVersionId": "2",
        "imageSetWorkflowStatus": "COPYING",
        "updatedAt": 1680042505.135,
        "imageSetId": "b9eb50d8ee682eb9fcf4acbf92f62bb7",
        "imageSetState": "LOCKED",
        "createdAt": 1680042357.432
    },
    "sourceImageSetProperties": {
        "latestVersionId": "1",
        "imageSetWorkflowStatus": "COPYING_WITH_READ_ONLY_ACCESS",
        "updatedAt": 1680042505.135,
        "imageSetId": "ea92b0d8838c72a3f25d00d13616f87e",
        "imageSetState": "LOCKED",
        "createdAt": 1680027126.436
    },
    "datastoreId": "12345678901234567890123456789012"
}
```

For more information, see [Copying an image set](https://docs.aws.amazon.com/healthimaging/latest/devguide/copy-image-set.html) in the *AWS HealthImaging Developer Guide*.

## Output

datastoreId -> (string)

The data store identifier.

sourceImageSetProperties -> (structure)

The properties of the source image set.

imageSetId -> (string)

The image set identifier for the copied source image set.

latestVersionId -> (string)

The latest version identifier for the copied source image set.

imageSetState -> (string)

The image set state of the copied source image set.

imageSetWorkflowStatus -> (string)

The workflow status of the copied source image set.

createdAt -> (timestamp)

The timestamp when the source image set properties were created.

updatedAt -> (timestamp)

The timestamp when the source image set properties were updated.

imageSetArn -> (string)

The Amazon Resource Name (ARN) assigned to the source image set.

destinationImageSetProperties -> (structure)

The properties of the destination image set.

imageSetId -> (string)

The image set identifier of the copied image set properties.

latestVersionId -> (string)

The latest version identifier for the destination image set properties.

imageSetState -> (string)

The image set state of the destination image set properties.

imageSetWorkflowStatus -> (string)

The image set workflow status of the destination image set properties.

createdAt -> (timestamp)

The timestamp when the destination image set properties were created.

updatedAt -> (timestamp)

The timestamp when the destination image set properties were last updated.

imageSetArn -> (string)

The Amazon Resource Name (ARN) assigned to the destination image set.