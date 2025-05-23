# get-conformance-pack-compliance-detailsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-conformance-pack-compliance-details.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/get-conformance-pack-compliance-details.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [configservice](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/configservice/index.html#cli-aws-configservice) ]

# get-conformance-pack-compliance-details

## Description

Returns compliance details of a conformance pack for all Amazon Web Services resources that are monitered by conformance pack.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/config-2014-11-12/GetConformancePackComplianceDetails)

## Synopsis

```
get-conformance-pack-compliance-details
--conformance-pack-name <value>
[--filters <value>]
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

`--conformance-pack-name` (string)

Name of the conformance pack.

`--filters` (structure)

A `ConformancePackEvaluationFilters` object.

ConfigRuleNames -> (list)

Filters the results by Config rule names.

(string)

ComplianceType -> (string)

Filters the results by compliance.

The allowed values are `COMPLIANT` and `NON_COMPLIANT` . `INSUFFICIENT_DATA` is not supported.

ResourceType -> (string)

Filters the results by the resource type (for example, `"AWS::EC2::Instance"` ).

ResourceIds -> (list)

Filters the results by resource IDs.

### Note

This is valid only when you provide resource type. If there is no resource type, you will see an error.

(string)

Shorthand Syntax:

```
ConfigRuleNames=string,string,ComplianceType=string,ResourceType=string,ResourceIds=string,string
```

JSON Syntax:

```
{
  "ConfigRuleNames": ["string", ...],
  "ComplianceType": "COMPLIANT"|"NON_COMPLIANT"|"INSUFFICIENT_DATA",
  "ResourceType": "string",
  "ResourceIds": ["string", ...]
}
```

`--limit` (integer)

The maximum number of evaluation results returned on each page. If you do no specify a number, Config uses the default. The default is 100.

`--next-token` (string)

The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.

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

ConformancePackName -> (string)

Name of the conformance pack.

ConformancePackRuleEvaluationResults -> (list)

Returns a list of `ConformancePackEvaluationResult` objects.

(structure)

The details of a conformance pack evaluation. Provides Config rule and Amazon Web Services resource type that was evaluated, the compliance of the conformance pack, related time stamps, and supplementary information.

ComplianceType -> (string)

The compliance type. The allowed values are `COMPLIANT` and `NON_COMPLIANT` . `INSUFFICIENT_DATA` is not supported.

EvaluationResultIdentifier -> (structure)

Uniquely identifies an evaluation result.

EvaluationResultQualifier -> (structure)

Identifies an Config rule used to evaluate an Amazon Web Services resource, and provides the type and ID of the evaluated resource.

ConfigRuleName -> (string)

The name of the Config rule that was used in the evaluation.

ResourceType -> (string)

The type of Amazon Web Services resource that was evaluated.

ResourceId -> (string)

The ID of the evaluated Amazon Web Services resource.

EvaluationMode -> (string)

The mode of an evaluation. The valid values are Detective or Proactive.

OrderingTimestamp -> (timestamp)

The time of the event that triggered the evaluation of your Amazon Web Services resources. The time can indicate when Config delivered a configuration item change notification, or it can indicate when Config delivered the configuration snapshot, depending on which event triggered the evaluation.

ResourceEvaluationId -> (string)

A Unique ID for an evaluation result.

ConfigRuleInvokedTime -> (timestamp)

The time when Config rule evaluated Amazon Web Services resource.

ResultRecordedTime -> (timestamp)

The time when Config recorded the evaluation result.

Annotation -> (string)

Supplementary information about how the evaluation determined the compliance.

NextToken -> (string)

The `nextToken` string returned in a previous request that you use to request the next page of results in a paginated response.