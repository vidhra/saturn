# create-alertÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutmetrics/create-alert.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutmetrics/create-alert.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lookoutmetrics](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lookoutmetrics/index.html#cli-aws-lookoutmetrics) ]

# create-alert

## Description

Creates an alert for an anomaly detector.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lookoutmetrics-2017-07-25/CreateAlert)

## Synopsis

```
create-alert
--alert-name <value>
[--alert-sensitivity-threshold <value>]
[--alert-description <value>]
--anomaly-detector-arn <value>
--action <value>
[--tags <value>]
[--alert-filters <value>]
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

`--alert-name` (string)

The name of the alert.

`--alert-sensitivity-threshold` (integer)

An integer from 0 to 100 specifying the alert sensitivity threshold.

`--alert-description` (string)

A description of the alert.

`--anomaly-detector-arn` (string)

The ARN of the detector to which the alert is attached.

`--action` (structure)

Action that will be triggered when there is an alert.

SNSConfiguration -> (structure)

A configuration for an Amazon SNS channel.

RoleArn -> (string)

The ARN of the IAM role that has access to the target SNS topic.

SnsTopicArn -> (string)

The ARN of the target SNS topic.

SnsFormat -> (string)

The format of the SNS topic.

- `JSON` â Send JSON alerts with an anomaly ID and a link to the anomaly detail page. This is the default.
- `LONG_TEXT` â Send human-readable alerts with information about the impacted timeseries and a link to the anomaly detail page. We recommend this for email.
- `SHORT_TEXT` â Send human-readable alerts with a link to the anomaly detail page. We recommend this for SMS.

LambdaConfiguration -> (structure)

A configuration for an AWS Lambda channel.

RoleArn -> (string)

The ARN of an IAM role that has permission to invoke the Lambda function.

LambdaArn -> (string)

The ARN of the Lambda function.

Shorthand Syntax:

```
SNSConfiguration={RoleArn=string,SnsTopicArn=string,SnsFormat=string},LambdaConfiguration={RoleArn=string,LambdaArn=string}
```

JSON Syntax:

```
{
  "SNSConfiguration": {
    "RoleArn": "string",
    "SnsTopicArn": "string",
    "SnsFormat": "LONG_TEXT"|"SHORT_TEXT"|"JSON"
  },
  "LambdaConfiguration": {
    "RoleArn": "string",
    "LambdaArn": "string"
  }
}
```

`--tags` (map)

A list of [tags](https://docs.aws.amazon.com/lookoutmetrics/latest/dev/detectors-tags.html) to apply to the alert.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
```

`--alert-filters` (structure)

The configuration of the alert filters, containing MetricList and DimensionFilterList.

MetricList -> (list)

The list of measures that you want to get alerts for.

(string)

DimensionFilterList -> (list)

The list of DimensionFilter objects that are used for dimension-based filtering.

(structure)

The dimension filter, containing DimensionName and DimensionValueList.

DimensionName -> (string)

The name of the dimension to filter on.

DimensionValueList -> (list)

The list of values for the dimension specified in DimensionName that you want to filter on.

(string)

JSON Syntax:

```
{
  "MetricList": ["string", ...],
  "DimensionFilterList": [
    {
      "DimensionName": "string",
      "DimensionValueList": ["string", ...]
    }
    ...
  ]
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

AlertArn -> (string)

The ARN of the alert.