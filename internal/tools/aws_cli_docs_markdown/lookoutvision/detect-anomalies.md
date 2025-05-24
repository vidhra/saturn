# detect-anomaliesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/detect-anomalies.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/detect-anomalies.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutvision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutvision/index.html#cli-aws-lookoutvision) ]

# detect-anomalies

## Description

Detects anomalies in an image that you supply.

The response from `DetectAnomalies` includes a boolean prediction that the image contains one or more anomalies and a confidence value for the prediction. If the model is an image segmentation model, the response also includes segmentation information for each type of anomaly found in the image.

### Note

Before calling `DetectAnomalies` , you must first start your model with the  StartModel operation. You are charged for the amount of time, in minutes, that a model runs and for the number of anomaly detection units that your model uses. If you are not using a model, use the  StopModel operation to stop your model.

For more information, see *Detecting anomalies in an image* in the Amazon Lookout for Vision developer guide.

This operation requires permissions to perform the `lookoutvision:DetectAnomalies` operation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutvision-2020-11-20/DetectAnomalies)

## Synopsis

```
detect-anomalies
--project-name <value>
--model-version <value>
--body <value>
--content-type <value>
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

`--project-name` (string)

The name of the project that contains the model version that you want to use.

`--model-version` (string)

The version of the model that you want to use.

`--body` (streaming blob)

The unencrypted image bytes that you want to analyze.

### Note

This argument is of type: streaming blob. Its value must be the path to a file (e.g. `path/to/file`) and must **not** be prefixed with `file://` or `fileb://`

`--content-type` (string)

The type of the image passed in `Body` . Valid values are `image/png` (PNG format images) and `image/jpeg` (JPG format images).

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

DetectAnomalyResult -> (structure)

The results of the `DetectAnomalies` operation.

Source -> (structure)

The source of the image that was analyzed. `direct` means that the images was supplied from the local computer. No other values are supported.

Type -> (string)

The type of the image.

IsAnomalous -> (boolean)

True if Amazon Lookout for Vision classifies the image as containing an anomaly, otherwise false.

Confidence -> (float)

The confidence that Lookout for Vision has in the accuracy of the classification in `IsAnomalous` .

Anomalies -> (list)

If the model is an image segmentation model, `Anomalies` contains a list of anomaly types found in the image. There is one entry for each type of anomaly found (even if multiple instances of an anomaly type exist on the image). The first element in the list is always an anomaly type representing the image background (âbackgroundâ) and shouldnât be considered an anomaly. Amazon Lookout for Vision automatically add the background anomaly type to the response, and you donât need to declare a background anomaly type in your dataset.

If the list has one entry (âbackgroundâ), no anomalies were found on the image.

An image classification model doesnât return an `Anomalies` list.

(structure)

Information about an anomaly type found on an image by an image segmentation model. For more information, see  DetectAnomalies .

Name -> (string)

The name of an anomaly type found in an image. `Name` maps to an anomaly type in the training dataset, apart from the anomaly type `background` . The service automatically inserts the `background` anomaly type into the response from `DetectAnomalies` .

PixelAnomaly -> (structure)

Information about the pixel mask that covers an anomaly type.

TotalPercentageArea -> (float)

The percentage area of the image that the anomaly type covers.

Color -> (string)

A hex color value for the mask that covers an anomaly type. Each anomaly type has a different mask color. The color maps to the color of the anomaly type used in the training dataset.

AnomalyMask -> (blob)

If the model is an image segmentation model, `AnomalyMask` contains pixel masks that covers all anomaly types found on the image. Each anomaly type has a different mask color. To map a color to an anomaly type, see the `color` field of the  PixelAnomaly object.

An image classification model doesnât return an `Anomalies` list.