# describe-aggregate-compliance-by-config-rulesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-aggregate-compliance-by-config-rules.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/describe-aggregate-compliance-by-config-rules.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# describe-aggregate-compliance-by-config-rules

## Description

Returns a list of compliant and noncompliant rules with the number of resources for compliant and noncompliant rules. Does not display rules that do not have compliance results.

### Note

The results can return an empty result page, but if you have a `nextToken` , the results are displayed on the next page.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/DescribeAggregateComplianceByConfigRules)

`describe-aggregate-compliance-by-config-rules` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `AggregateComplianceByConfigRules`

## Synopsis

```
describe-aggregate-compliance-by-config-rules
--configuration-aggregator-name <value>
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
[--max-items <value>]
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

`--configuration-aggregator-name` (string)

The name of the configuration aggregator.

`--filters` (structure)

Filters the results by ConfigRuleComplianceFilters object.

ConfigRuleName -> (string)

The name of the Config rule.

ComplianceType -> (string)

The rule compliance status.

For the `ConfigRuleComplianceFilters` data type, Config supports only `COMPLIANT` and `NON_COMPLIANT` . Config does not support the `NOT_APPLICABLE` and the `INSUFFICIENT_DATA` values.

AccountId -> (string)

The 12-digit account ID of the source account.

AwsRegion -> (string)

The source region where the data is aggregated.

Shorthand Syntax:

```
ConfigRuleName=string,ComplianceType=string,AccountId=string,AwsRegion=string
```

JSON Syntax:

```
{
  "ConfigRuleName": "string",
  "ComplianceType": "COMPLIANT"|"NON_COMPLIANT"|"NOT_APPLICABLE"|"INSUFFICIENT_DATA",
  "AccountId": "string",
  "AwsRegion": "string"
}
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--max-items` (integer)

The total number of items to return in the commandâs output. If the total number of items available is more than the value specified, a `NextToken` is provided in the commandâs output. To resume pagination, provide the `NextToken` value in the `starting-token` argument of a subsequent command. **Do not** use the `NextToken` response element directly outside of the AWS CLI.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

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

AggregateComplianceByConfigRules -> (list)

Returns a list of AggregateComplianceByConfigRule object.

(structure)

Indicates whether an Config rule is compliant based on account ID, region, compliance, and rule name.

A rule is compliant if all of the resources that the rule evaluated comply with it. It is noncompliant if any of these resources do not comply.

ConfigRuleName -> (string)

The name of the Config rule.

Compliance -> (structure)

Indicates whether an Amazon Web Services resource or Config rule is compliant and provides the number of contributors that affect the compliance.

ComplianceType -> (string)

Indicates whether an Amazon Web Services resource or Config rule is compliant.

A resource is compliant if it complies with all of the Config rules that evaluate it. A resource is noncompliant if it does not comply with one or more of these rules.

A rule is compliant if all of the resources that the rule evaluates comply with it. A rule is noncompliant if any of these resources do not comply.

Config returns the `INSUFFICIENT_DATA` value when no evaluation results are available for the Amazon Web Services resource or Config rule.

For the `Compliance` data type, Config supports only `COMPLIANT` , `NON_COMPLIANT` , and `INSUFFICIENT_DATA` values. Config does not support the `NOT_APPLICABLE` value for the `Compliance` data type.

ComplianceContributorCount -> (structure)

The number of Amazon Web Services resources or Config rules that cause a result of `NON_COMPLIANT` , up to a maximum number.

CappedCount -> (integer)

The number of Amazon Web Services resources or Config rules responsible for the current compliance of the item.

CapExceeded -> (boolean)

Indicates whether the maximum count is reached.

AccountId -> (string)

The 12-digit account ID of the source account.

AwsRegion -> (string)

The source region from where the data is aggregated.

NextToken -> (string)

The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.