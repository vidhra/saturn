# get-aggregate-conformance-pack-compliance-summaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-aggregate-conformance-pack-compliance-summary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-aggregate-conformance-pack-compliance-summary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# get-aggregate-conformance-pack-compliance-summary

## Description

Returns the count of compliant and noncompliant conformance packs across all Amazon Web Services accounts and Amazon Web Services Regions in an aggregator. You can filter based on Amazon Web Services account ID or Amazon Web Services Region.

### Note

The results can return an empty result page, but if you have a nextToken, the results are displayed on the next page.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetAggregateConformancePackComplianceSummary)

## Synopsis

```
get-aggregate-conformance-pack-compliance-summary
--configuration-aggregator-name <value>
[--filters <value>]
[--group-by-key <value>]
[--limit <value>]
[--next-token <value>]
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

`--configuration-aggregator-name` (string)

The name of the configuration aggregator.

`--filters` (structure)

Filters the results based on the `AggregateConformancePackComplianceSummaryFilters` object.

AccountId -> (string)

The 12-digit Amazon Web Services account ID of the source account.

AwsRegion -> (string)

The source Amazon Web Services Region from where the data is aggregated.

Shorthand Syntax:

```
AccountId=string,AwsRegion=string
```

JSON Syntax:

```
{
  "AccountId": "string",
  "AwsRegion": "string"
}
```

`--group-by-key` (string)

Groups the result based on Amazon Web Services account ID or Amazon Web Services Region.

Possible values:

- `ACCOUNT_ID`
- `AWS_REGION`

`--limit` (integer)

The maximum number of results returned on each page. The default is maximum. If you specify 0, Config uses the default.

`--next-token` (string)

The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.

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

AggregateConformancePackComplianceSummaries -> (list)

Returns a list of `AggregateConformancePackComplianceSummary` object.

(structure)

Provides a summary of compliance based on either account ID or region.

ComplianceSummary -> (structure)

Returns an `AggregateConformancePackComplianceCount` object.

CompliantConformancePackCount -> (integer)

Number of compliant conformance packs.

NonCompliantConformancePackCount -> (integer)

Number of noncompliant conformance packs.

GroupName -> (string)

Groups the result based on Amazon Web Services account ID or Amazon Web Services Region.

GroupByKey -> (string)

Groups the result based on Amazon Web Services account ID or Amazon Web Services Region.

NextToken -> (string)

The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.