# get-featureÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/get-feature.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/get-feature.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [evidently](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/index.html#cli-aws-evidently) ]

# get-feature

## Description

Returns the details about one feature. You must already know the feature name. To retrieve a list of features in your account, use [ListFeatures](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_ListFeatures.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/evidently-2021-02-01/GetFeature)

## Synopsis

```
get-feature
--feature <value>
--project <value>
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

`--feature` (string)

The name of the feature that you want to retrieve information for.

`--project` (string)

The name or ARN of the project that contains the feature.

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

feature -> (structure)

A structure containing the configuration details of the feature.

arn -> (string)

The ARN of the feature.

createdTime -> (timestamp)

The date and time that the feature is created.

defaultVariation -> (string)

The name of the variation that is used as the default variation. The default variation is served to users who are not allocated to any ongoing launches or experiments of this feature.

This variation must also be listed in the `variations` structure.

If you omit `defaultVariation` , the first variation listed in the `variations` structure is used as the default variation.

description -> (string)

The description of the feature.

entityOverrides -> (map)

A set of key-value pairs that specify users who should always be served a specific variation of a feature. Each key specifies a user using their user ID, account ID, or some other identifier. The value specifies the name of the variation that the user is to be served.

For the override to be successful, the value of the key must match the `entityId` used in the [EvaluateFeature](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_EvaluateFeature.html) operation.

key -> (string)

value -> (string)

evaluationRules -> (list)

An array of structures that define the evaluation rules for the feature.

(structure)

A structure that contains the information about an evaluation rule for this feature, if it is used in a launch or experiment.

name -> (string)

The name of the experiment or launch.

type -> (string)

This value is `aws.evidently.splits` if this is an evaluation rule for a launch, and it is `aws.evidently.onlineab` if this is an evaluation rule for an experiment.

evaluationStrategy -> (string)

If this value is `ALL_RULES` , the traffic allocation specified by any ongoing launches or experiments is being used. If this is `DEFAULT_VARIATION` , the default variation is being served to all users.

lastUpdatedTime -> (timestamp)

The date and time that the feature was most recently updated.

name -> (string)

The name of the feature.

project -> (string)

The name or ARN of the project that contains the feature.

status -> (string)

The current state of the feature.

tags -> (map)

The list of tag keys and values associated with this feature.

key -> (string)

value -> (string)

valueType -> (string)

Defines the type of value used to define the different feature variations. For more information, see [Variation types](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-variationtypes.html)

variations -> (list)

An array of structures that contain the configuration of the featureâs different variations.

(structure)

This structure contains the name and variation value of one variation of a feature.

name -> (string)

The name of the variation.

value -> (tagged union structure)

The value assigned to this variation.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `boolValue`, `doubleValue`, `longValue`, `stringValue`.

boolValue -> (boolean)

If this feature uses the Boolean variation type, this field contains the Boolean value of this variation.

doubleValue -> (double)

If this feature uses the double integer variation type, this field contains the double integer value of this variation.

longValue -> (long)

If this feature uses the long variation type, this field contains the long value of this variation.

stringValue -> (string)

If this feature uses the string variation type, this field contains the string value of this variation.