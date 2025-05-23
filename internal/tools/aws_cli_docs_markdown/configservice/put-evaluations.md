# put-evaluationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-evaluations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/put-evaluations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# put-evaluations

## Description

Used by an Lambda function to deliver evaluation results to Config. This operation is required in every Lambda function that is invoked by an Config rule.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/PutEvaluations)

## Synopsis

```
put-evaluations
[--evaluations <value>]
--result-token <value>
[--test-mode | --no-test-mode]
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

`--evaluations` (list)

The assessments that the Lambda function performs. Each evaluation identifies an Amazon Web Services resource and indicates whether it complies with the Config rule that invokes the Lambda function.

(structure)

Identifies an Amazon Web Services resource and indicates whether it complies with the Config rule that it was evaluated against.

ComplianceResourceType -> (string)

The type of Amazon Web Services resource that was evaluated.

ComplianceResourceId -> (string)

The ID of the Amazon Web Services resource that was evaluated.

ComplianceType -> (string)

Indicates whether the Amazon Web Services resource complies with the Config rule that it was evaluated against.

For the `Evaluation` data type, Config supports only the `COMPLIANT` , `NON_COMPLIANT` , and `NOT_APPLICABLE` values. Config does not support the `INSUFFICIENT_DATA` value for this data type.

Similarly, Config does not accept `INSUFFICIENT_DATA` as the value for `ComplianceType` from a `PutEvaluations` request. For example, an Lambda function for a custom Config rule cannot pass an `INSUFFICIENT_DATA` value to Config.

Annotation -> (string)

Supplementary information about how the evaluation determined the compliance.

OrderingTimestamp -> (timestamp)

The time of the event in Config that triggered the evaluation. For event-based evaluations, the time indicates when Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).

Shorthand Syntax:

```
ComplianceResourceType=string,ComplianceResourceId=string,ComplianceType=string,Annotation=string,OrderingTimestamp=timestamp ...
```

JSON Syntax:

```
[
  {
    "ComplianceResourceType": "string",
    "ComplianceResourceId": "string",
    "ComplianceType": "COMPLIANT"|"NON_COMPLIANT"|"NOT_APPLICABLE"|"INSUFFICIENT_DATA",
    "Annotation": "string",
    "OrderingTimestamp": timestamp
  }
  ...
]
```

`--result-token` (string)

An encrypted token that associates an evaluation with an Config rule. Identifies the rule and the event that triggered the evaluation.

`--test-mode` | `--no-test-mode` (boolean)

Use this parameter to specify a test run for `PutEvaluations` . You can verify whether your Lambda function will deliver evaluation results to Config. No updates occur to your existing evaluations, and evaluation results are not sent to Config.

### Note

When `TestMode` is `true` , `PutEvaluations` doesnât require a valid value for the `ResultToken` parameter, but the value cannot be null.

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

FailedEvaluations -> (list)

Requests that failed because of a client or server error.

(structure)

Identifies an Amazon Web Services resource and indicates whether it complies with the Config rule that it was evaluated against.

ComplianceResourceType -> (string)

The type of Amazon Web Services resource that was evaluated.

ComplianceResourceId -> (string)

The ID of the Amazon Web Services resource that was evaluated.

ComplianceType -> (string)

Indicates whether the Amazon Web Services resource complies with the Config rule that it was evaluated against.

For the `Evaluation` data type, Config supports only the `COMPLIANT` , `NON_COMPLIANT` , and `NOT_APPLICABLE` values. Config does not support the `INSUFFICIENT_DATA` value for this data type.

Similarly, Config does not accept `INSUFFICIENT_DATA` as the value for `ComplianceType` from a `PutEvaluations` request. For example, an Lambda function for a custom Config rule cannot pass an `INSUFFICIENT_DATA` value to Config.

Annotation -> (string)

Supplementary information about how the evaluation determined the compliance.

OrderingTimestamp -> (timestamp)

The time of the event in Config that triggered the evaluation. For event-based evaluations, the time indicates when Config created the configuration item that triggered the evaluation. For periodic evaluations, the time indicates when Config triggered the evaluation at the frequency that you specified (for example, every 24 hours).