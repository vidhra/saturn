# describe-algorithmÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-algorithm.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/describe-algorithm.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [personalize](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/personalize/index.html#cli-aws-personalize) ]

# describe-algorithm

## Description

Describes the given algorithm.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/personalize-2018-05-22/DescribeAlgorithm)

## Synopsis

```
describe-algorithm
--algorithm-arn <value>
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

`--algorithm-arn` (string)

The Amazon Resource Name (ARN) of the algorithm to describe.

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

algorithm -> (structure)

A listing of the properties of the algorithm.

name -> (string)

The name of the algorithm.

algorithmArn -> (string)

The Amazon Resource Name (ARN) of the algorithm.

algorithmImage -> (structure)

The URI of the Docker container for the algorithm image.

name -> (string)

The name of the algorithm image.

dockerURI -> (string)

The URI of the Docker container for the algorithm image.

defaultHyperParameters -> (map)

Specifies the default hyperparameters.

key -> (string)

value -> (string)

defaultHyperParameterRanges -> (structure)

Specifies the default hyperparameters, their ranges, and whether they are tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).

integerHyperParameterRanges -> (list)

The integer-valued hyperparameters and their default ranges.

(structure)

Provides the name and default range of a integer-valued hyperparameter and whether the hyperparameter is tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).

name -> (string)

The name of the hyperparameter.

minValue -> (integer)

The minimum allowable value for the hyperparameter.

maxValue -> (integer)

The maximum allowable value for the hyperparameter.

isTunable -> (boolean)

Indicates whether the hyperparameter is tunable.

continuousHyperParameterRanges -> (list)

The continuous hyperparameters and their default ranges.

(structure)

Provides the name and default range of a continuous hyperparameter and whether the hyperparameter is tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).

name -> (string)

The name of the hyperparameter.

minValue -> (double)

The minimum allowable value for the hyperparameter.

maxValue -> (double)

The maximum allowable value for the hyperparameter.

isTunable -> (boolean)

Whether the hyperparameter is tunable.

categoricalHyperParameterRanges -> (list)

The categorical hyperparameters and their default ranges.

(structure)

Provides the name and default range of a categorical hyperparameter and whether the hyperparameter is tunable. A tunable hyperparameter can have its value determined during hyperparameter optimization (HPO).

name -> (string)

The name of the hyperparameter.

values -> (list)

A list of the categories for the hyperparameter.

(string)

isTunable -> (boolean)

Whether the hyperparameter is tunable.

defaultResourceConfig -> (map)

Specifies the default maximum number of training jobs and parallel training jobs.

key -> (string)

value -> (string)

trainingInputMode -> (string)

The training input mode.

roleArn -> (string)

The Amazon Resource Name (ARN) of the role.

creationDateTime -> (timestamp)

The date and time (in Unix time) that the algorithm was created.

lastUpdatedDateTime -> (timestamp)

The date and time (in Unix time) that the algorithm was last updated.