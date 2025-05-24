# evaluate-featureÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/evaluate-feature.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/evaluate-feature.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [evidently](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/evidently/index.html#cli-aws-evidently) ]

# evaluate-feature

## Description

This operation assigns a feature variation to one given user session. You pass in an `entityID` that represents the user. Evidently then checks the evaluation rules and assigns the variation.

The first rules that are evaluated are the override rules. If the userâs `entityID` matches an override rule, the user is served the variation specified by that rule.

If there is a current launch with this feature that uses segment overrides, and if the user sessionâs `evaluationContext` matches a segment rule defined in a segment override, the configuration in the segment overrides is used. For more information about segments, see [CreateSegment](https://docs.aws.amazon.com/cloudwatchevidently/latest/APIReference/API_CreateSegment.html) and [Use segments to focus your audience](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html) .

If there is a launch with no segment overrides, the user might be assigned to a variation in the launch. The chance of this depends on the percentage of users that are allocated to that launch. If the user is enrolled in the launch, the variation they are served depends on the allocation of the various feature variations used for the launch.

If the user is not assigned to a launch, and there is an ongoing experiment for this feature, the user might be assigned to a variation in the experiment. The chance of this depends on the percentage of users that are allocated to that experiment.

If the experiment uses a segment, then only user sessions with `evaluationContext` values that match the segment rule are used in the experiment.

If the user is enrolled in the experiment, the variation they are served depends on the allocation of the various feature variations used for the experiment.

If the user is not assigned to a launch or experiment, they are served the default variation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/evidently-2021-02-01/EvaluateFeature)

## Synopsis

```
evaluate-feature
--entity-id <value>
[--evaluation-context <value>]
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

`--entity-id` (string)

An internal ID that represents a unique user of the application. This `entityID` is checked against any override rules assigned for this feature.

`--evaluation-context` (string)

A JSON object of attributes that you can optionally pass in as part of the evaluation event sent to Evidently from the user session. Evidently can use this value to match user sessions with defined audience segments. For more information, see [Use segments to focus your audience](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Evidently-segments.html) .

If you include this parameter, the value must be a JSON object. A JSON array is not supported.

`--feature` (string)

The name of the feature being evaluated.

`--project` (string)

The name or ARN of the project that contains this feature.

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

details -> (string)

If this user was assigned to a launch or experiment, this field lists the launch or experiment name.

reason -> (string)

Specifies the reason that the user session was assigned this variation. Possible values include `DEFAULT` , meaning the user was served the default variation; `LAUNCH_RULE_MATCH` , if the user session was enrolled in a launch; `EXPERIMENT_RULE_MATCH` , if the user session was enrolled in an experiment; or `ENTITY_OVERRIDES_MATCH` , if the userâs `entityId` matches an override rule.

value -> (tagged union structure)

The value assigned to this variation to differentiate it from the other variations of this feature.

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

variation -> (string)

The name of the variation that was served to the user session.