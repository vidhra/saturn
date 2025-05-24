# get-ops-summaryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-ops-summary.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/get-ops-summary.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ssm](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/index.html#cli-aws-ssm) ]

# get-ops-summary

## Description

View a summary of operations metadata (OpsData) based on specified filters and aggregators. OpsData can include information about Amazon Web Services Systems Manager OpsCenter operational workitems (OpsItems) as well as information about any Amazon Web Services resource or service configured to report OpsData to Amazon Web Services Systems Manager Explorer.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ssm-2014-11-06/GetOpsSummary)

`get-ops-summary` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Entities`

## Synopsis

```
get-ops-summary
[--sync-name <value>]
[--filters <value>]
[--aggregators <value>]
[--result-attributes <value>]
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

`--sync-name` (string)

Specify the name of a resource data sync to get.

`--filters` (list)

Optional filters used to scope down the returned OpsData.

(structure)

A filter for viewing OpsData summaries.

Key -> (string)

The name of the filter.

Values -> (list)

The filter value.

(string)

Type -> (string)

The type of filter.

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
    "Type": "Equal"|"NotEqual"|"BeginWith"|"LessThan"|"GreaterThan"|"Exists"
  }
  ...
]
```

`--aggregators` (list)

Optional aggregators that return counts of OpsData based on one or more expressions.

(structure)

One or more aggregators for viewing counts of OpsData using different dimensions such as `Source` , `CreatedTime` , or `Source and CreatedTime` , to name a few.

AggregatorType -> (string)

Either a `Range` or `Count` aggregator for limiting an OpsData summary.

TypeName -> (string)

The data type name to use for viewing counts of OpsData.

AttributeName -> (string)

The name of an OpsData attribute on which to limit the count of OpsData.

Values -> (map)

The aggregator value.

key -> (string)

value -> (string)

Filters -> (list)

The aggregator filters.

(structure)

A filter for viewing OpsData summaries.

Key -> (string)

The name of the filter.

Values -> (list)

The filter value.

(string)

Type -> (string)

The type of filter.

Aggregators -> (list)

A nested aggregator for viewing counts of OpsData.

(structure)

One or more aggregators for viewing counts of OpsData using different dimensions such as `Source` , `CreatedTime` , or `Source and CreatedTime` , to name a few.

AggregatorType -> (string)

Either a `Range` or `Count` aggregator for limiting an OpsData summary.

TypeName -> (string)

The data type name to use for viewing counts of OpsData.

AttributeName -> (string)

The name of an OpsData attribute on which to limit the count of OpsData.

Values -> (map)

The aggregator value.

key -> (string)

value -> (string)

Filters -> (list)

The aggregator filters.

(structure)

A filter for viewing OpsData summaries.

Key -> (string)

The name of the filter.

Values -> (list)

The filter value.

(string)

Type -> (string)

The type of filter.

JSON Syntax:

```
[
  {
    "AggregatorType": "string",
    "TypeName": "string",
    "AttributeName": "string",
    "Values": {"string": "string"
      ...},
    "Filters": [
      {
        "Key": "string",
        "Values": ["string", ...],
        "Type": "Equal"|"NotEqual"|"BeginWith"|"LessThan"|"GreaterThan"|"Exists"
      }
      ...
    ],
    "Aggregators": [
      {
        "AggregatorType": "string",
        "TypeName": "string",
        "AttributeName": "string",
        "Values": {"string": "string"
          ...},
        "Filters": [
          {
            "Key": "string",
            "Values": ["string", ...],
            "Type": "Equal"|"NotEqual"|"BeginWith"|"LessThan"|"GreaterThan"|"Exists"
          }
          ...
        ],
        "Aggregators":
      }
      ...
    ]
  }
  ...
]
```

`--result-attributes` (list)

The OpsData data type to return.

(structure)

The OpsItem data type to return.

TypeName -> (string)

Name of the data type. Valid value: `AWS:OpsItem` , `AWS:EC2InstanceInformation` , `AWS:OpsItemTrendline` , or `AWS:ComplianceSummary` .

Shorthand Syntax:

```
TypeName=string ...
```

JSON Syntax:

```
[
  {
    "TypeName": "string"
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

**To view a summary of all OpsItems**

The following `get-ops-summary` example displays a summary of all OpsItems in your AWS account.

```
aws ssm get-ops-summary
```

Output:

```
{
    "Entities": [
        {
            "Id": "oi-4309fEXAMPLE",
            "Data": {
                "AWS:OpsItem": {
                    "CaptureTime": "2020-02-26T18:58:32.918Z",
                    "Content": [
                        {
                            "AccountId": "111222333444",
                            "Category": "Availability",
                            "CreatedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE",
                            "CreatedTime": "2020-02-26T19:10:44.149Z",
                            "Description": "CloudWatch Event Rule SSMOpsItems-EC2-instance-terminated was triggered. Your EC2 instance has terminated. See below for more details.",
                            "LastModifiedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE",
                            "LastModifiedTime": "2020-02-26T19:10:44.149Z",
                            "Notifications": "",
                            "OperationalData": "{\"/aws/automations\":{\"type\":\"SearchableString\",\"value\":\"[ { \\\"automationType\\\": \\\"AWS:SSM:Automation\\\", \\\"automationId\\\": \\\"AWS-CreateManagedWindowsInstance\\\" }, { \\\"automationType\\\": \\\"AWS:SSM:Automation\\\", \\\"automationId\\\": \\\"AWS-CreateManagedLinuxInstance\\\" } ]\"},\"/aws/resources\":{\"type\":\"SearchableString\",\"value\":\"[{\\\"arn\\\":\\\"arn:aws:ec2:us-east-2:111222333444:instance/i-0acbd0800fEXAMPLE\\\"}]\"},\"/aws/dedup\":{\"type\":\"SearchableString\",\"value\":\"{\\\"dedupString\\\":\\\"SSMOpsItems-EC2-instance-terminated\\\"}\"}}",
                            "OpsItemId": "oi-4309fEXAMPLE",
                            "RelatedItems": "",
                            "Severity": "3",
                            "Source": "EC2",
                            "Status": "Open",
                            "Title": "EC2 instance terminated"
                        }
                    ]
                }
            }
        },
        {
            "Id": "oi-bb2a0e6a4541",
            "Data": {
                "AWS:OpsItem": {
                    "CaptureTime": "2019-11-26T19:20:06.161Z",
                    "Content": [
                        {
                            "AccountId": "111222333444",
                            "Category": "Availability",
                            "CreatedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE",
                            "CreatedTime": "2019-11-26T20:00:07.237Z",
                            "Description": "CloudWatch Event Rule SSMOpsItems-SSM-maintenance-window-execution-failed was triggered. Your SSM Maintenance Window execution has failed. See below for more details.",
                            "LastModifiedBy": "arn:aws:sts::111222333444:assumed-role/OpsItem-CWE-Role/fbf77cbe264a33509569f23e4EXAMPLE",
                            "LastModifiedTime": "2019-11-26T20:00:07.237Z",
                            "Notifications": "",
                            "OperationalData": "{\"/aws/resources\":{\"type\":\"SearchableString\",\"value\":\"[{\\\"arn\\\":\\\"arn:aws:ssm:us-east-2:111222333444:maintenancewindow/mw-0e83ba440dEXAMPLE\\\"}]\"},\"/aws/dedup\":{\"type\":\"SearchableString\",\"value\":\"{\\\"dedupString\\\":\\\"SSMOpsItems-SSM-maintenance-window-execution-failed\\\"}\"}}",
                            "OpsItemId": "oi-bb2a0EXAMPLE",
                            "RelatedItems": "",
                            "Severity": "3",
                            "Source": "SSM",
                            "Status": "Open",
                            "Title": "SSM Maintenance Window execution failed"
                        }
                    ]
                }
            }
        }
    ]
}
```

For more information, see [Working with OpsItems](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter-working-with-OpsItems.html) in the *AWS Systems Manager User Guide*.

## Output

Entities -> (list)

The list of aggregated details and filtered OpsData.

(structure)

The result of the query.

Id -> (string)

The query ID.

Data -> (map)

The data returned by the query.

key -> (string)

value -> (structure)

The OpsData summary.

CaptureTime -> (string)

The time the OpsData was captured.

Content -> (list)

The details of an OpsData summary.

(map)

key -> (string)

value -> (string)

NextToken -> (string)

The token for the next set of items to return. Use this token to get the next set of results.