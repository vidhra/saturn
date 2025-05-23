# start-commitment-purchase-analysisÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/start-commitment-purchase-analysis.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/start-commitment-purchase-analysis.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ce](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ce/index.html#cli-aws-ce) ]

# start-commitment-purchase-analysis

## Description

Specifies the parameters of a planned commitment purchase and starts the generation of the analysis. This enables you to estimate the cost, coverage, and utilization impact of your planned commitment purchases.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ce-2017-10-25/StartCommitmentPurchaseAnalysis)

## Synopsis

```
start-commitment-purchase-analysis
--commitment-purchase-analysis-configuration <value>
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

`--commitment-purchase-analysis-configuration` (structure)

The configuration for the commitment purchase analysis.

SavingsPlansPurchaseAnalysisConfiguration -> (structure)

The configuration for the Savings Plans purchase analysis.

AccountScope -> (string)

The account scope that you want your analysis for.

AccountId -> (string)

The account that the analysis is for.

AnalysisType -> (string)

The type of analysis.

SavingsPlansToAdd -> (list)

Savings Plans to include in the analysis.

(structure)

The Savings Plans commitment details.

PaymentOption -> (string)

The payment option for the Savings Plans commitment.

SavingsPlansType -> (string)

The Savings Plans type.

Region -> (string)

The Region associated with the Savings Plans commitment.

InstanceFamily -> (string)

The instance family of the Savings Plans commitment.

TermInYears -> (string)

The term that you want the Savings Plans commitment for.

SavingsPlansCommitment -> (double)

The Savings Plans commitment.

OfferingId -> (string)

The unique ID thatâs used to distinguish Savings Plans commitments from one another.

SavingsPlansToExclude -> (list)

Savings Plans to exclude from the analysis.

(string)

LookBackTimePeriod -> (structure)

The time period associated with the analysis.

Start -> (string)

The beginning of the time period. The start date is inclusive. For example, if `start` is `2017-01-01` , Amazon Web Services retrieves cost and usage data starting at `2017-01-01` up to the end date. The start date must be equal to or no later than the current date to avoid a validation error.

End -> (string)

The end of the time period. The end date is exclusive. For example, if `end` is `2017-05-01` , Amazon Web Services retrieves cost and usage data from the start date up to, but not including, `2017-05-01` .

JSON Syntax:

```
{
  "SavingsPlansPurchaseAnalysisConfiguration": {
    "AccountScope": "PAYER"|"LINKED",
    "AccountId": "string",
    "AnalysisType": "MAX_SAVINGS"|"CUSTOM_COMMITMENT",
    "SavingsPlansToAdd": [
      {
        "PaymentOption": "NO_UPFRONT"|"PARTIAL_UPFRONT"|"ALL_UPFRONT"|"LIGHT_UTILIZATION"|"MEDIUM_UTILIZATION"|"HEAVY_UTILIZATION",
        "SavingsPlansType": "COMPUTE_SP"|"EC2_INSTANCE_SP"|"SAGEMAKER_SP",
        "Region": "string",
        "InstanceFamily": "string",
        "TermInYears": "ONE_YEAR"|"THREE_YEARS",
        "SavingsPlansCommitment": double,
        "OfferingId": "string"
      }
      ...
    ],
    "SavingsPlansToExclude": ["string", ...],
    "LookBackTimePeriod": {
      "Start": "string",
      "End": "string"
    }
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

AnalysisId -> (string)

The analysis ID thatâs associated with the commitment purchase analysis.

AnalysisStartedTime -> (string)

The start time of the analysis.

EstimatedCompletionTime -> (string)

The estimated time for when the analysis will complete.