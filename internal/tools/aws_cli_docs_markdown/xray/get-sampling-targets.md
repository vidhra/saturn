# get-sampling-targetsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-sampling-targets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/get-sampling-targets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [xray](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/xray/index.html#cli-aws-xray) ]

# get-sampling-targets

## Description

Requests a sampling quota for rules that the service is using to sample requests.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/xray-2016-04-12/GetSamplingTargets)

## Synopsis

```
get-sampling-targets
--sampling-statistics-documents <value>
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

`--sampling-statistics-documents` (list)

Information about rules that the service is using to sample requests.

(structure)

Request sampling results for a single rule from a service. Results are for the last 10 seconds unless the service has been assigned a longer reporting interval after a previous call to [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html) .

RuleName -> (string)

The name of the sampling rule.

ClientID -> (string)

A unique identifier for the service in hexadecimal.

Timestamp -> (timestamp)

The current time.

RequestCount -> (integer)

The number of requests that matched the rule.

SampledCount -> (integer)

The number of requests recorded.

BorrowCount -> (integer)

The number of requests recorded with borrowed reservoir quota.

Shorthand Syntax:

```
RuleName=string,ClientID=string,Timestamp=timestamp,RequestCount=integer,SampledCount=integer,BorrowCount=integer ...
```

JSON Syntax:

```
[
  {
    "RuleName": "string",
    "ClientID": "string",
    "Timestamp": timestamp,
    "RequestCount": integer,
    "SampledCount": integer,
    "BorrowCount": integer
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To request a sampling quota**

The following `get-sampling-targets` example requests a sampling quota for rules that the service is using to sample requests. The response from AWS X-Ray includes a quota that can be used instead of borrowing from the reservoir.

```
aws xray get-sampling-targets \
    --sampling-statistics-documents '[ { "RuleName": "base-scorekeep", "ClientID": "ABCDEF1234567890ABCDEF10", "Timestamp": "2018-07-07T00:20:06, "RequestCount": 110, "SampledCount": 20, "BorrowCount": 10 }, { "RuleName": "polling-scorekeep", 31, "BorrowCount": 0 } ]'
```

Output:

```
{
    "SamplingTargetDocuments": [
        {
            "RuleName": "base-scorekeep",
            "FixedRate": 0.1,
            "ReservoirQuota": 2,
            "ReservoirQuotaTTL": 1530923107.0,
            "Interval": 10
        },
        {
            "RuleName": "polling-scorekeep",
            "FixedRate": 0.003,
            "ReservoirQuota": 0,
            "ReservoirQuotaTTL": 1530923107.0,
            "Interval": 10
        }
    ],
    "LastRuleModification": 1530920505.0,
    "UnprocessedStatistics": []
}
```

For more information, see [Using Sampling Rules with the X-Ray API](https://docs.aws.amazon.com/en_pv/xray/latest/devguide/xray-api-sampling.html) in the *AWS X-Ray Developer Guide*.

## Output

SamplingTargetDocuments -> (list)

Updated rules that the service should use to sample requests.

(structure)

Temporary changes to a sampling rule configuration. To meet the global sampling target for a rule, X-Ray calculates a new reservoir for each service based on the recent sampling results of all services that called [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html) .

RuleName -> (string)

The name of the sampling rule.

FixedRate -> (double)

The percentage of matching requests to instrument, after the reservoir is exhausted.

ReservoirQuota -> (integer)

The number of requests per second that X-Ray allocated for this service.

ReservoirQuotaTTL -> (timestamp)

When the reservoir quota expires.

Interval -> (integer)

The number of seconds for the service to wait before getting sampling targets again.

LastRuleModification -> (timestamp)

The last time a user changed the sampling rule configuration. If the sampling rule configuration changed since the service last retrieved it, the service should call [GetSamplingRules](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingRules.html) to get the latest version.

UnprocessedStatistics -> (list)

Information about [SamplingStatisticsDocument](https://docs.aws.amazon.com/xray/latest/api/API_SamplingStatisticsDocument.html) that X-Ray could not process.

(structure)

Sampling statistics from a call to [GetSamplingTargets](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html) that X-Ray could not process.

RuleName -> (string)

The name of the sampling rule.

ErrorCode -> (string)

The error code.

Message -> (string)

The error message.