# describe-log-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-log-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-log-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# describe-log-groups

## Description

Returns information about log groups. You can return all your log groups or filter the results by prefix. The results are ASCII-sorted by log group name.

CloudWatch Logs doesnât support IAM policies that control access to the `DescribeLogGroups` action by using the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-log-groups.html#id1)aws:ResourceTag/*key-name* `` condition key. Other CloudWatch Logs actions do support the use of the [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/describe-log-groups.html#id3)aws:ResourceTag/*key-name* `` condition key to control access. For more information about using tags to control access, see [Controlling access to Amazon Web Services resources using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_tags.html) .

If you are using CloudWatch cross-account observability, you can use this operation in a monitoring account and view data from the linked source accounts. For more information, see [CloudWatch cross-account observability](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Unified-Cross-Account.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/DescribeLogGroups)

`describe-log-groups` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `logGroups`

## Synopsis

```
describe-log-groups
[--account-identifiers <value>]
[--log-group-name-prefix <value>]
[--log-group-name-pattern <value>]
[--include-linked-accounts | --no-include-linked-accounts]
[--log-group-class <value>]
[--log-group-identifiers <value>]
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

`--account-identifiers` (list)

When `includeLinkedAccounts` is set to `true` , use this parameter to specify the list of accounts to search. You can specify as many as 20 account IDs in the array.

(string)

Syntax:

```
"string" "string" ...
```

`--log-group-name-prefix` (string)

The prefix to match.

### Note

`logGroupNamePrefix` and `logGroupNamePattern` are mutually exclusive. Only one of these parameters can be passed.

`--log-group-name-pattern` (string)

If you specify a string for this parameter, the operation returns only log groups that have names that match the string based on a case-sensitive substring search. For example, if you specify `Foo` , log groups named `FooBar` , `aws/Foo` , and `GroupFoo` would match, but `foo` , `F/o/o` and `Froo` would not match.

If you specify `logGroupNamePattern` in your request, then only `arn` , `creationTime` , and `logGroupName` are included in the response.

### Note

`logGroupNamePattern` and `logGroupNamePrefix` are mutually exclusive. Only one of these parameters can be passed.

`--include-linked-accounts` | `--no-include-linked-accounts` (boolean)

If you are using a monitoring account, set this to `true` to have the operation return log groups in the accounts listed in `accountIdentifiers` .

If this parameter is set to `true` and `accountIdentifiers` contains a null value, the operation returns all log groups in the monitoring account and all log groups in all source accounts that are linked to the monitoring account.

The default for this parameter is `false` .

`--log-group-class` (string)

Use this parameter to limit the results to only those log groups in the specified log group class. If you omit this parameter, log groups of all classes can be returned.

Specifies the log group class for this log group. There are three classes:

- The `Standard` log class supports all CloudWatch Logs features.
- The `Infrequent Access` log class supports a subset of CloudWatch Logs features and incurs lower costs.
- Use the `Delivery` log class only for delivering Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for only one day. This log class doesnât offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries.

For details about the features supported by each class, see [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)

Possible values:

- `STANDARD`
- `INFREQUENT_ACCESS`
- `DELIVERY`

`--log-group-identifiers` (list)

Use this array to filter the list of log groups returned. If you specify this parameter, the only other filter that you can choose to specify is `includeLinkedAccounts` .

If you are using this operation in a monitoring account, you can specify the ARNs of log groups in source accounts and in the monitoring account itself. If you are using this operation in an account that is not a cross-account monitoring account, you can specify only log group names in the same account as the operation.

(string)

Syntax:

```
"string" "string" ...
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

The following command describes a log group named `my-logs`:

```
aws logs describe-log-groups --log-group-name-prefix my-logs
```

Output:

```
{
    "logGroups": [
        {
            "storedBytes": 0,
            "metricFilterCount": 0,
            "creationTime": 1433189500783,
            "logGroupName": "my-logs",
            "retentionInDays": 5,
            "arn": "arn:aws:logs:us-west-2:0123456789012:log-group:my-logs:*"
        }
    ]
}
```

## Output

logGroups -> (list)

An array of structures, where each structure contains the information about one log group.

(structure)

Represents a log group.

logGroupName -> (string)

The name of the log group.

creationTime -> (long)

The creation time of the log group, expressed as the number of milliseconds after Jan 1, 1970 00:00:00 UTC.

retentionInDays -> (integer)

The number of days to retain the log events in the specified log group. Possible values are: 1, 3, 5, 7, 14, 30, 60, 90, 120, 150, 180, 365, 400, 545, 731, 1096, 1827, 2192, 2557, 2922, 3288, and 3653.

To set a log group so that its log events do not expire, use [DeleteRetentionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_DeleteRetentionPolicy.html) .

metricFilterCount -> (integer)

The number of metric filters.

arn -> (string)

The Amazon Resource Name (ARN) of the log group. This version of the ARN includes a trailing `:*` after the log group name.

Use this version to refer to the ARN in IAM policies when specifying permissions for most API actions. The exception is when specifying permissions for [TagResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html) , [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html) , and [ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html) . The permissions for those three actions require the ARN version that doesnât include a trailing `:*` .

storedBytes -> (long)

The number of bytes stored.

kmsKeyId -> (string)

The Amazon Resource Name (ARN) of the KMS key to use when encrypting log data.

dataProtectionStatus -> (string)

Displays whether this log group has a protection policy, or whether it had one in the past. For more information, see [PutDataProtectionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html) .

inheritedProperties -> (list)

Displays all the properties that this log group has inherited from account-level settings.

(string)

logGroupClass -> (string)

This specifies the log group class for this log group. There are three classes:

- The `Standard` log class supports all CloudWatch Logs features.
- The `Infrequent Access` log class supports a subset of CloudWatch Logs features and incurs lower costs.
- Use the `Delivery` log class only for delivering Lambda logs to store in Amazon S3 or Amazon Data Firehose. Log events in log groups in the Delivery class are kept in CloudWatch Logs for only one day. This log class doesnât offer rich CloudWatch Logs capabilities such as CloudWatch Logs Insights queries.

For details about the features supported by the Standard and Infrequent Access classes, see [Log classes](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch_Logs_Log_Classes.html)

logGroupArn -> (string)

The Amazon Resource Name (ARN) of the log group. This version of the ARN doesnât include a trailing `:*` after the log group name.

Use this version to refer to the ARN in the following situations:

- In the `logGroupIdentifier` input field in many CloudWatch Logs APIs.
- In the `resourceArn` field in tagging APIs
- In IAM policies, when specifying permissions for [TagResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_TagResource.html) , [UntagResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.html) , and [ListTagsForResource](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.html) .

nextToken -> (string)

The token for the next set of items to return. The token expires after 24 hours.