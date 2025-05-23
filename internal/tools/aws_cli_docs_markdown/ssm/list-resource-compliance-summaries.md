# list-resource-compliance-summariesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-resource-compliance-summaries.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/list-resource-compliance-summaries.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# list-resource-compliance-summaries

## Description

Returns a resource-level summary count. The summary includes information about compliant and non-compliant statuses and detailed compliance-item severity counts, according to the filter criteria you specify.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/ListResourceComplianceSummaries)

`list-resource-compliance-summaries` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ResourceComplianceSummaryItems`

## Synopsis

```
list-resource-compliance-summaries
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

`--filters` (list)

One or more filters. Use a filter to return a more specific list of results.

(structure)

One or more filters. Use a filter to return a more specific list of results.

Key -> (string)

The name of the filter.

Values -> (list)

The value for which to search.

(string)

Type -> (string)

The type of comparison that should be performed for the value: Equal, NotEqual, BeginWith, LessThan, or GreaterThan.

Shorthand Syntax:

```
Key=string,Values=string,string,Type=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Values": ["string", ...],
    "Type": "EQUAL"|"NOT_EQUAL"|"BEGIN_WITH"|"LESS_THAN"|"GREATER_THAN"
  }
  ...
]
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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To list resource-level compliance summary counts**

This example lists resource-level compliance summary counts.

Command:

```
aws ssm list-resource-compliance-summaries
```

Output:

```
{
  "ResourceComplianceSummaryItems": [
      {
          "ComplianceType": "Association",
          "ResourceType": "ManagedInstance",
          "ResourceId": "i-1234567890abcdef0",
          "Status": "COMPLIANT",
          "OverallSeverity": "UNSPECIFIED",
          "ExecutionSummary": {
              "ExecutionTime": 1550509273.0
          },
          "CompliantSummary": {
              "CompliantCount": 2,
              "SeveritySummary": {
                  "CriticalCount": 0,
                  "HighCount": 0,
                  "MediumCount": 0,
                  "LowCount": 0,
                  "InformationalCount": 0,
                  "UnspecifiedCount": 2
              }
          },
          "NonCompliantSummary": {
              "NonCompliantCount": 0,
              "SeveritySummary": {
                  "CriticalCount": 0,
                  "HighCount": 0,
                  "MediumCount": 0,
                  "LowCount": 0,
                  "InformationalCount": 0,
                  "UnspecifiedCount": 0
              }
          }
      },
      {
          "ComplianceType": "Patch",
          "ResourceType": "ManagedInstance",
          "ResourceId": "i-9876543210abcdef0",
          "Status": "COMPLIANT",
          "OverallSeverity": "UNSPECIFIED",
          "ExecutionSummary": {
              "ExecutionTime": 1550248550.0,
              "ExecutionId": "7abb6378-a4a5-4f10-8312-0123456789ab",
              "ExecutionType": "Command"
          },
          "CompliantSummary": {
              "CompliantCount": 397,
              "SeveritySummary": {
                  "CriticalCount": 0,
                  "HighCount": 0,
                  "MediumCount": 0,
                  "LowCount": 0,
                  "InformationalCount": 0,
                  "UnspecifiedCount": 397
              }
          },
          "NonCompliantSummary": {
              "NonCompliantCount": 0,
              "SeveritySummary": {
                  "CriticalCount": 0,
                  "HighCount": 0,
                  "MediumCount": 0,
                  "LowCount": 0,
                  "InformationalCount": 0,
                  "UnspecifiedCount": 0
              }
          }
      }
  ],
  "NextToken": "--token string truncated--"
}
```

**To list resource-level compliance summaries for a specific compliance type**

This example lists resource-level compliance summaries for the Patch compliance type.

Command:

```
aws ssm list-resource-compliance-summaries --filters "Key=ComplianceType,Values=Patch,Type=EQUAL"
```

## Output

ResourceComplianceSummaryItems -> (list)

A summary count for specified or targeted managed nodes. Summary count includes information about compliant and non-compliant State Manager associations, patch status, or custom items according to the filter criteria that you specify.

(structure)

Compliance summary information for a specific resource.

ComplianceType -> (string)

The compliance type.

ResourceType -> (string)

The resource type.

ResourceId -> (string)

The resource ID.

Status -> (string)

The compliance status for the resource.

OverallSeverity -> (string)

The highest severity item found for the resource. The resource is compliant for this item.

ExecutionSummary -> (structure)

Information about the execution.

ExecutionTime -> (timestamp)

The time the execution ran as a datetime object that is saved in the following format: `yyyy-MM-dd'T'HH:mm:ss'Z'`

ExecutionId -> (string)

An ID created by the system when `PutComplianceItems` was called. For example, `CommandID` is a valid execution ID. You can use this ID in subsequent calls.

ExecutionType -> (string)

The type of execution. For example, `Command` is a valid execution type.

CompliantSummary -> (structure)

A list of items that are compliant for the resource.

CompliantCount -> (integer)

The total number of resources that are compliant.

SeveritySummary -> (structure)

A summary of the compliance severity by compliance type.

CriticalCount -> (integer)

The total number of resources or compliance items that have a severity level of `Critical` . Critical severity is determined by the organization that published the compliance items.

HighCount -> (integer)

The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.

MediumCount -> (integer)

The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.

LowCount -> (integer)

The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.

InformationalCount -> (integer)

The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.

UnspecifiedCount -> (integer)

The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.

NonCompliantSummary -> (structure)

A list of items that arenât compliant for the resource.

NonCompliantCount -> (integer)

The total number of compliance items that arenât compliant.

SeveritySummary -> (structure)

A summary of the non-compliance severity by compliance type

CriticalCount -> (integer)

The total number of resources or compliance items that have a severity level of `Critical` . Critical severity is determined by the organization that published the compliance items.

HighCount -> (integer)

The total number of resources or compliance items that have a severity level of high. High severity is determined by the organization that published the compliance items.

MediumCount -> (integer)

The total number of resources or compliance items that have a severity level of medium. Medium severity is determined by the organization that published the compliance items.

LowCount -> (integer)

The total number of resources or compliance items that have a severity level of low. Low severity is determined by the organization that published the compliance items.

InformationalCount -> (integer)

The total number of resources or compliance items that have a severity level of informational. Informational severity is determined by the organization that published the compliance items.

UnspecifiedCount -> (integer)

The total number of resources or compliance items that have a severity level of unspecified. Unspecified severity is determined by the organization that published the compliance items.

NextToken -> (string)

The token for the next set of items to return. Use this token to get the next set of results.