# create-linkÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/create-link.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/create-link.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [oam](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/oam/index.html#cli-aws-oam) ]

# create-link

## Description

Creates a link between a source account and a sink that you have created in a monitoring account. After the link is created, data is sent from the source account to the monitoring account. When you create a link, you can optionally specify filters that specify which metric namespaces and which log groups are shared from the source account to the monitoring account.

Before you create a link, you must create a sink in the monitoring account and create a sink policy in that account. The sink policy must permit the source account to link to it. You can grant permission to source accounts by granting permission to an entire organization or to individual accounts.

For more information, see [CreateSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html) and [PutSinkPolicy](https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html) .

Each monitoring account can be linked to as many as 100,000 source accounts.

Each source account can be linked to as many as five monitoring accounts.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/oam-2022-06-10/CreateLink)

## Synopsis

```
create-link
--label-template <value>
[--link-configuration <value>]
--resource-types <value>
--sink-identifier <value>
[--tags <value>]
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

`--label-template` (string)

Specify a friendly human-readable name to use to identify this source account when you are viewing data from it in the monitoring account.

You can use a custom label or use the following variables:

- `$AccountName` is the name of the account
- `$AccountEmail` is the globally unique email address of the account
- `$AccountEmailNoDomain` is the email address of the account without the domain name

### Note

In the Amazon Web Services GovCloud (US-East) and Amazon Web Services GovCloud (US-West) Regions, the only supported option is to use custom labels, and the `$AccountName` , `$AccountEmail` , and `$AccountEmailNoDomain` variables all resolve as *account-id* instead of the specified variable.

`--link-configuration` (structure)

Use this structure to optionally create filters that specify that only some metric namespaces or log groups are to be shared from the source account to the monitoring account.

LogGroupConfiguration -> (structure)

Use this structure to filter which log groups are to send log events from the source account to the monitoring account.

Filter -> (string)

Use this field to specify which log groups are to share their log events with the monitoring account. Use the term `LogGroupName` and one or more of the following operands. Use single quotation marks (â) around log group names. The matching of log group names is case sensitive. Each filter has a limit of five conditional operands. Conditional operands are `AND` and `OR` .

- `=` and `!=`
- `AND`
- `OR`
- `LIKE` and `NOT LIKE` . These can be used only as prefix searches. Include a `%` at the end of the string that you want to search for and include.
- `IN` and `NOT IN` , using parentheses `( )`

Examples:

- `LogGroupName IN ('This-Log-Group', 'Other-Log-Group')` includes only the log groups with names `This-Log-Group` and `Other-Log-Group` .
- `LogGroupName NOT IN ('Private-Log-Group', 'Private-Log-Group-2')` includes all log groups except the log groups with names `Private-Log-Group` and `Private-Log-Group-2` .
- `LogGroupName LIKE 'aws/lambda/%' OR LogGroupName LIKE 'AWSLogs%'` includes all log groups that have names that start with `aws/lambda/` or `AWSLogs` .

### Note

If you are updating a link that uses filters, you can specify `*` as the only value for the `filter` parameter to delete the filter and share all log groups with the monitoring account.

MetricConfiguration -> (structure)

Use this structure to filter which metric namespaces are to be shared from the source account to the monitoring account.

Filter -> (string)

Use this field to specify which metrics are to be shared with the monitoring account. Use the term `Namespace` and one or more of the following operands. Use single quotation marks (â) around namespace names. The matching of namespace names is case sensitive. Each filter has a limit of five conditional operands. Conditional operands are `AND` and `OR` .

- `=` and `!=`
- `AND`
- `OR`
- `LIKE` and `NOT LIKE` . These can be used only as prefix searches. Include a `%` at the end of the string that you want to search for and include.
- `IN` and `NOT IN` , using parentheses `( )`

Examples:

- `Namespace NOT LIKE 'AWS/%'` includes only namespaces that donât start with `AWS/` , such as custom namespaces.
- `Namespace IN ('AWS/EC2', 'AWS/ELB', 'AWS/S3')` includes only the metrics in the EC2, Elastic Load Balancing, and Amazon S3 namespaces.
- `Namespace = 'AWS/EC2' OR Namespace NOT LIKE 'AWS/%'` includes only the EC2 namespace and your custom namespaces.

### Note

If you are updating a link that uses filters, you can specify `*` as the only value for the `filter` parameter to delete the filter and share all metric namespaces with the monitoring account.

Shorthand Syntax:

```
LogGroupConfiguration={Filter=string},MetricConfiguration={Filter=string}
```

JSON Syntax:

```
{
  "LogGroupConfiguration": {
    "Filter": "string"
  },
  "MetricConfiguration": {
    "Filter": "string"
  }
}
```

`--resource-types` (list)

An array of strings that define which types of data that the source account shares with the monitoring account.

(string)

Syntax:

```
"string" "string" ...

Where valid values are:
  AWS::CloudWatch::Metric
  AWS::Logs::LogGroup
  AWS::XRay::Trace
  AWS::ApplicationInsights::Application
  AWS::InternetMonitor::Monitor
  AWS::ApplicationSignals::Service
  AWS::ApplicationSignals::ServiceLevelObjective
```

`--sink-identifier` (string)

The ARN of the sink to use to create this link. You can use [ListSinks](https://docs.aws.amazon.com/OAM/latest/APIReference/API_ListSinks.html) to find the ARNs of sinks.

For more information about sinks, see [CreateSink](https://docs.aws.amazon.com/OAM/latest/APIReference/API_CreateSink.html) .

`--tags` (map)

Assigns one or more tags (key-value pairs) to the link.

Tags can help you organize and categorize your resources. You can also use them to scope user permissions by granting a user permission to access or change only resources with certain tag values.

For more information about using tags to control access, see [Controlling access to Amazon Web Services resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) .

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

**To create a link**

The following `create-link` example creates a link between a source account and a sink that you have created in a monitoring account.

```
aws oam create-link \
    --label-template sourceAccount \
    --resource-types AWS::CloudWatch::Metric \
    --sink-identifier arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345
```

Output:

```
{
    "Arn": "arn:aws:oam:us-east-2:123456789111:link/a1b2c3d4-5678-90ab-cdef-example11111",
    "Id": "a1b2c3d4-5678-90ab-cdef-example11111",
    "Label": "sourceAccount",
    "LabelTemplate": "sourceAccount",
    "ResourceTypes": [
        "AWS::CloudWatch::Metric"
    ],
    "SinkArn": "arn:aws:oam:us-east-2:123456789012:sink/a1b2c3d4-5678-90ab-cdef-example12345",
    "Tags": {}
}
```

For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) in the *Amazon CloudWatch User Guide*.

## Output

Arn -> (string)

The ARN of the link that is newly created.

Id -> (string)

The random ID string that Amazon Web Services generated as part of the link ARN.

Label -> (string)

The label that you assigned to this link. If the `labelTemplate` includes variables, this field displays the variables resolved to their actual values.

LabelTemplate -> (string)

The exact label template that you specified, with the variables not resolved.

LinkConfiguration -> (structure)

This structure includes filters that specify which metric namespaces and which log groups are shared from the source account to the monitoring account.

LogGroupConfiguration -> (structure)

Use this structure to filter which log groups are to send log events from the source account to the monitoring account.

Filter -> (string)

Use this field to specify which log groups are to share their log events with the monitoring account. Use the term `LogGroupName` and one or more of the following operands. Use single quotation marks (â) around log group names. The matching of log group names is case sensitive. Each filter has a limit of five conditional operands. Conditional operands are `AND` and `OR` .

- `=` and `!=`
- `AND`
- `OR`
- `LIKE` and `NOT LIKE` . These can be used only as prefix searches. Include a `%` at the end of the string that you want to search for and include.
- `IN` and `NOT IN` , using parentheses `( )`

Examples:

- `LogGroupName IN ('This-Log-Group', 'Other-Log-Group')` includes only the log groups with names `This-Log-Group` and `Other-Log-Group` .
- `LogGroupName NOT IN ('Private-Log-Group', 'Private-Log-Group-2')` includes all log groups except the log groups with names `Private-Log-Group` and `Private-Log-Group-2` .
- `LogGroupName LIKE 'aws/lambda/%' OR LogGroupName LIKE 'AWSLogs%'` includes all log groups that have names that start with `aws/lambda/` or `AWSLogs` .

### Note

If you are updating a link that uses filters, you can specify `*` as the only value for the `filter` parameter to delete the filter and share all log groups with the monitoring account.

MetricConfiguration -> (structure)

Use this structure to filter which metric namespaces are to be shared from the source account to the monitoring account.

Filter -> (string)

Use this field to specify which metrics are to be shared with the monitoring account. Use the term `Namespace` and one or more of the following operands. Use single quotation marks (â) around namespace names. The matching of namespace names is case sensitive. Each filter has a limit of five conditional operands. Conditional operands are `AND` and `OR` .

- `=` and `!=`
- `AND`
- `OR`
- `LIKE` and `NOT LIKE` . These can be used only as prefix searches. Include a `%` at the end of the string that you want to search for and include.
- `IN` and `NOT IN` , using parentheses `( )`

Examples:

- `Namespace NOT LIKE 'AWS/%'` includes only namespaces that donât start with `AWS/` , such as custom namespaces.
- `Namespace IN ('AWS/EC2', 'AWS/ELB', 'AWS/S3')` includes only the metrics in the EC2, Elastic Load Balancing, and Amazon S3 namespaces.
- `Namespace = 'AWS/EC2' OR Namespace NOT LIKE 'AWS/%'` includes only the EC2 namespace and your custom namespaces.

### Note

If you are updating a link that uses filters, you can specify `*` as the only value for the `filter` parameter to delete the filter and share all metric namespaces with the monitoring account.

ResourceTypes -> (list)

The resource types supported by this link.

(string)

SinkArn -> (string)

The ARN of the sink that is used for this link.

Tags -> (map)

The tags assigned to the link.

key -> (string)

value -> (string)