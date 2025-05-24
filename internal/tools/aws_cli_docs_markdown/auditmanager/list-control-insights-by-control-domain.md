# list-control-insights-by-control-domainÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-control-insights-by-control-domain.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/list-control-insights-by-control-domain.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [auditmanager](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/auditmanager/index.html#cli-aws-auditmanager) ]

# list-control-insights-by-control-domain

## Description

Lists the latest analytics data for controls within a specific control domain across all active assessments.

### Note

Control insights are listed only if the control belongs to the control domain that was specified and the control collected evidence on the `lastUpdated` date of `controlInsightsMetadata` . If neither of these conditions are met, no data is listed for that control.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/auditmanager-2017-07-25/ListControlInsightsByControlDomain)

## Synopsis

```
list-control-insights-by-control-domain
--control-domain-id <value>
[--next-token <value>]
[--max-results <value>]
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

`--control-domain-id` (string)

The unique identifier for the control domain.

Audit Manager supports the control domains that are provided by Amazon Web Services Control Catalog. For information about how to find a list of available control domains, see ` `ListDomains` [https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains](https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_ListDomains).html`__ in the Amazon Web Services Control Catalog API Reference.

`--next-token` (string)

The pagination token thatâs used to fetch the next set of results.

`--max-results` (integer)

Represents the maximum number of results on a page or for an API request call.

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

controlInsightsMetadata -> (list)

The control analytics data that the `ListControlInsightsByControlDomain` API returned.

(structure)

A summary of the latest analytics data for a specific control.

This data reflects the total counts for the specified control across all active assessments. Control insights are grouped by control domain, and ranked by the highest total count of non-compliant evidence.

name -> (string)

The name of the control.

id -> (string)

The unique identifier for the control.

evidenceInsights -> (structure)

A breakdown of the compliance check status for the evidence thatâs associated with the control.

noncompliantEvidenceCount -> (integer)

The number of compliance check evidence that Audit Manager classified as non-compliant. This includes evidence that was collected from Security Hub with a *Fail* ruling, or collected from Config with a *Non-compliant* ruling.

compliantEvidenceCount -> (integer)

The number of compliance check evidence that Audit Manager classified as compliant. This includes evidence that was collected from Security Hub with a *Pass* ruling, or collected from Config with a *Compliant* ruling.

inconclusiveEvidenceCount -> (integer)

The number of evidence that a compliance check ruling isnât available for. Evidence is inconclusive when the associated control uses Security Hub or Config as a data source but you didnât enable those services. This is also the case when a control uses a data source that doesnât support compliance checks (for example, manual evidence, API calls, or CloudTrail).

### Note

If evidence has a compliance check status of *not applicable* in the console, itâs classified as *inconclusive* in `EvidenceInsights` data.

lastUpdated -> (timestamp)

The time when the control insights were last updated.

nextToken -> (string)

The pagination token thatâs used to fetch the next set of results.