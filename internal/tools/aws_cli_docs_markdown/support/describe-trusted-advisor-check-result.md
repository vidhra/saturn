# describe-trusted-advisor-check-resultÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-result.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/describe-trusted-advisor-check-result.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [support](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/support/index.html#cli-aws-support) ]

# describe-trusted-advisor-check-result

## Description

Returns the results of the Trusted Advisor check that has the specified check ID. You can get the check IDs by calling the  DescribeTrustedAdvisorChecks operation.

The response contains a  TrustedAdvisorCheckResult object, which contains these three objects:

- TrustedAdvisorCategorySpecificSummary
- TrustedAdvisorResourceDetail
- TrustedAdvisorResourcesSummary

In addition, the response contains these fields:

- **status** - The alert status of the check can be `ok` (green), `warning` (yellow), `error` (red), or `not_available` .
- **timestamp** - The time of the last refresh of the check.
- **checkId** - The unique identifier for the check.

### Note

- You must have a Business, Enterprise On-Ramp, or Enterprise Support plan to use the Amazon Web Services Support API.
- If you call the Amazon Web Services Support API from an account that doesnât have a Business, Enterprise On-Ramp, or Enterprise Support plan, the `SubscriptionRequiredException` error message appears. For information about changing your support plan, see [Amazon Web Services Support](http://aws.amazon.com/premiumsupport/) .

To call the Trusted Advisor operations in the Amazon Web Services Support API, you must use the US East (N. Virginia) endpoint. Currently, the US West (Oregon) and Europe (Ireland) endpoints donât support the Trusted Advisor operations. For more information, see [About the Amazon Web Services Support API](https://docs.aws.amazon.com/awssupport/latest/user/about-support-api.html#endpoint) in the *Amazon Web Services Support User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/support-2013-04-15/DescribeTrustedAdvisorCheckResult)

## Synopsis

```
describe-trusted-advisor-check-result
--check-id <value>
[--language <value>]
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

`--check-id` (string)

The unique identifier for the Trusted Advisor check.

`--language` (string)

The ISO 639-1 code for the language that you want your check results to appear in.

The Amazon Web Services Support API currently supports the following languages for Trusted Advisor:

- Chinese, Simplified - `zh`
- Chinese, Traditional - `zh_TW`
- English - `en`
- French - `fr`
- German - `de`
- Indonesian - `id`
- Italian - `it`
- Japanese - `ja`
- Korean - `ko`
- Portuguese, Brazilian - `pt_BR`
- Spanish - `es`

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

**To list the results of an AWS Trusted Advisor check**

The following `describe-trusted-advisor-check-result` example lists the results of the IAM Use check.

```
aws support describe-trusted-advisor-check-result \
    --check-id "zXCkfM1nI3"
```

Output:

```
{
    "result": {
        "checkId": "zXCkfM1nI3",
        "timestamp": "2020-05-13T21:38:05Z",
        "status": "ok",
        "resourcesSummary": {
            "resourcesProcessed": 1,
            "resourcesFlagged": 0,
            "resourcesIgnored": 0,
            "resourcesSuppressed": 0
        },
        "categorySpecificSummary": {
            "costOptimizing": {
                "estimatedMonthlySavings": 0.0,
                "estimatedPercentMonthlySavings": 0.0
            }
        },
        "flaggedResources": [
            {
                "status": "ok",
                "resourceId": "47DEQpj8HBSa-_TImW-5JCeuQeRkm5NMpJWZEXAMPLE",
                "isSuppressed": false
            }
        ]
    }
}
```

For more information, see [AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) in the *AWS Support User Guide*.

## Output

result -> (structure)

The detailed results of the Trusted Advisor check.

checkId -> (string)

The unique identifier for the Trusted Advisor check.

timestamp -> (string)

The time of the last refresh of the check.

status -> (string)

The alert status of the check: âokâ (green), âwarningâ (yellow), âerrorâ (red), or ânot_availableâ.

resourcesSummary -> (structure)

Details about Amazon Web Services resources that were analyzed in a call to Trusted Advisor  DescribeTrustedAdvisorCheckSummaries .

resourcesProcessed -> (long)

The number of Amazon Web Services resources that were analyzed by the Trusted Advisor check.

resourcesFlagged -> (long)

The number of Amazon Web Services resources that were flagged (listed) by the Trusted Advisor check.

resourcesIgnored -> (long)

The number of Amazon Web Services resources ignored by Trusted Advisor because information was unavailable.

resourcesSuppressed -> (long)

The number of Amazon Web Services resources ignored by Trusted Advisor because they were marked as suppressed by the user.

categorySpecificSummary -> (structure)

Summary information that relates to the category of the check. Cost Optimizing is the only category that is currently supported.

costOptimizing -> (structure)

The summary information about cost savings for a Trusted Advisor check that is in the Cost Optimizing category.

estimatedMonthlySavings -> (double)

The estimated monthly savings that might be realized if the recommended operations are taken.

estimatedPercentMonthlySavings -> (double)

The estimated percentage of savings that might be realized if the recommended operations are taken.

flaggedResources -> (list)

The details about each resource listed in the check result.

(structure)

Contains information about a resource identified by a Trusted Advisor check.

status -> (string)

The status code for the resource identified in the Trusted Advisor check.

region -> (string)

The Amazon Web Services Region in which the identified resource is located.

resourceId -> (string)

The unique identifier for the identified resource.

isSuppressed -> (boolean)

Specifies whether the Amazon Web Services resource was ignored by Trusted Advisor because it was marked as suppressed by the user.

metadata -> (list)

Additional information about the identified resource. The exact metadata and its order can be obtained by inspecting the  TrustedAdvisorCheckDescription object returned by the call to  DescribeTrustedAdvisorChecks . **Metadata** contains all the data that is shown in the Excel download, even in those cases where the UI shows just summary data.

(string)