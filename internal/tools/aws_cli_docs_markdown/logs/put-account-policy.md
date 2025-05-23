# put-account-policyÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-account-policy.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/put-account-policy.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [logs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/index.html#cli-aws-logs) ]

# put-account-policy

## Description

Creates an account-level data protection policy, subscription filter policy, or field index policy that applies to all log groups or a subset of log groups in the account.

To use this operation, you must be signed on with the correct permissions depending on the type of policy that you are creating.

- To create a data protection policy, you must have the `logs:PutDataProtectionPolicy` and `logs:PutAccountPolicy` permissions.
- To create a subscription filter policy, you must have the `logs:PutSubscriptionFilter` and `logs:PutccountPolicy` permissions.
- To create a transformer policy, you must have the `logs:PutTransformer` and `logs:PutAccountPolicy` permissions.
- To create a field index policy, you must have the `logs:PutIndexPolicy` and `logs:PutAccountPolicy` permissions.

**Data protection policy**

A data protection policy can help safeguard sensitive data thatâs ingested by your log groups by auditing and masking the sensitive log data. Each account can have only one account-level data protection policy.

### Warning

Sensitive data is detected and masked when it is ingested into a log group. When you set a data protection policy, log events ingested into the log groups before that time are not masked.

If you use `PutAccountPolicy` to create a data protection policy for your whole account, it applies to both existing log groups and all log groups that are created later in this account. The account-level policy is applied to existing log groups with eventual consistency. It might take up to 5 minutes before sensitive data in existing log groups begins to be masked.

By default, when a user views a log event that includes masked data, the sensitive data is replaced by asterisks. A user who has the `logs:Unmask` permission can use a [GetLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogEvents.html) or [FilterLogEvents](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_FilterLogEvents.html) operation with the `unmask` parameter set to `true` to view the unmasked log events. Users with the `logs:Unmask` can also view unmasked data in the CloudWatch Logs console by running a CloudWatch Logs Insights query with the `unmask` query command.

For more information, including a list of types of data that can be audited and masked, see [Protect sensitive log data with masking](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data.html) .

To use the `PutAccountPolicy` operation for a data protection policy, you must be signed on with the `logs:PutDataProtectionPolicy` and `logs:PutAccountPolicy` permissions.

The `PutAccountPolicy` operation applies to all log groups in the account. You can use [PutDataProtectionPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDataProtectionPolicy.html) to create a data protection policy that applies to just one log group. If a log group has its own data protection policy and the account also has an account-level data protection policy, then the two policies are cumulative. Any sensitive term specified in either policy is masked.

**Subscription filter policy**

A subscription filter policy sets up a real-time feed of log events from CloudWatch Logs to other Amazon Web Services services. Account-level subscription filter policies apply to both existing log groups and log groups that are created later in this account. Supported destinations are Kinesis Data Streams, Firehose, and Lambda. When log events are sent to the receiving service, they are Base64 encoded and compressed with the GZIP format.

The following destinations are supported for subscription filters:

- An Kinesis Data Streams data stream in the same account as the subscription policy, for same-account delivery.
- An Firehose data stream in the same account as the subscription policy, for same-account delivery.
- A Lambda function in the same account as the subscription policy, for same-account delivery.
- A logical destination in a different account created with [PutDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html) , for cross-account delivery. Kinesis Data Streams and Firehose are supported as logical destinations.

Each account can have one account-level subscription filter policy per Region. If you are updating an existing filter, you must specify the correct name in `PolicyName` . To perform a `PutAccountPolicy` subscription filter operation for any destination except a Lambda function, you must also have the `iam:PassRole` permission.

**Transformer policy**

Creates or updates a *log transformer policy* for your account. You use log transformers to transform log events into a different format, making them easier for you to process and analyze. You can also transform logs from different sources into standardized formats that contain relevant, source-specific information. After you have created a transformer, CloudWatch Logs performs this transformation at the time of log ingestion. You can then refer to the transformed versions of the logs during operations such as querying with CloudWatch Logs Insights or creating metric filters or subscription filters.

You can also use a transformer to copy metadata from metadata keys into the log events themselves. This metadata can include log group name, log stream name, account ID and Region.

A transformer for a log group is a series of processors, where each processor applies one type of transformation to the log events ingested into this log group. For more information about the available processors to use in a transformer, see [Processors that you can use](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors) .

Having log events in standardized format enables visibility across your applications for your log analysis, reporting, and alarming needs. CloudWatch Logs provides transformation for common log types with out-of-the-box transformation templates for major Amazon Web Services log sources such as VPC flow logs, Lambda, and Amazon RDS. You can use pre-built transformation templates or create custom transformation policies.

You can create transformers only for the log groups in the Standard log class.

You can have one account-level transformer policy that applies to all log groups in the account. Or you can create as many as 20 account-level transformer policies that are each scoped to a subset of log groups with the `selectionCriteria` parameter. If you have multiple account-level transformer policies with selection criteria, no two of them can use the same or overlapping log group name prefixes. For example, if you have one policy filtered to log groups that start with `my-log` , you canât have another field index policy filtered to `my-logpprod` or `my-logging` .

You can also set up a transformer at the log-group level. For more information, see [PutTransformer](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutTransformer.html) . If there is both a log-group level transformer created with `PutTransformer` and an account-level transformer that could apply to the same log group, the log group uses only the log-group level transformer. It ignores the account-level transformer.

**Field index policy**

You can use field index policies to create indexes on fields found in log events in the log group. Creating field indexes can help lower the scan volume for CloudWatch Logs Insights queries that reference those fields, because these queries attempt to skip the processing of log events that are known to not match the indexed field. Good fields to index are fields that you often need to query for and fields or values that match only a small fraction of the total log events. Common examples of indexes include request ID, session ID, user IDs, or instance IDs. For more information, see [Create field indexes to improve query performance and reduce costs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs-Field-Indexing.html)

To find the fields that are in your log group events, use the [GetLogGroupFields](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_GetLogGroupFields.html) operation.

For example, suppose you have created a field index for `requestId` . Then, any CloudWatch Logs Insights query on that log group that includes `requestId = *value* `` or ``requestId in [*value* , *value* , ...]` will attempt to process only the log events where the indexed field matches the specified value.

Matches of log events to the names of indexed fields are case-sensitive. For example, an indexed field of `RequestId` wonât match a log event containing `requestId` .

You can have one account-level field index policy that applies to all log groups in the account. Or you can create as many as 20 account-level field index policies that are each scoped to a subset of log groups with the `selectionCriteria` parameter. If you have multiple account-level index policies with selection criteria, no two of them can use the same or overlapping log group name prefixes. For example, if you have one policy filtered to log groups that start with `my-log` , you canât have another field index policy filtered to `my-logpprod` or `my-logging` .

If you create an account-level field index policy in a monitoring account in cross-account observability, the policy is applied only to the monitoring account and not to any source accounts.

If you want to create a field index policy for a single log group, you can use [PutIndexPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutIndexPolicy.html) instead of `PutAccountPolicy` . If you do so, that log group will use only that log-group level policy, and will ignore the account-level policy that you create with [PutAccountPolicy](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutAccountPolicy.html) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/logs-2014-03-28/PutAccountPolicy)

## Synopsis

```
put-account-policy
--policy-name <value>
--policy-document <value>
--policy-type <value>
[--scope <value>]
[--selection-criteria <value>]
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

`--policy-name` (string)

A name for the policy. This must be unique within the account.

`--policy-document` (string)

Specify the policy, in JSON.

**Data protection policy**

A data protection policy must include two JSON blocks:

- The first block must include both a `DataIdentifer` array and an `Operation` property with an `Audit` action. The `DataIdentifer` array lists the types of sensitive data that you want to mask. For more information about the available options, see [Types of data that you can mask](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/mask-sensitive-log-data-types.html) . The `Operation` property with an `Audit` action is required to find the sensitive data terms. This `Audit` action must contain a `FindingsDestination` object. You can optionally use that `FindingsDestination` object to list one or more destinations to send audit findings to. If you specify destinations such as log groups, Firehose streams, and S3 buckets, they must already exist.
- The second block must include both a `DataIdentifer` array and an `Operation` property with an `Deidentify` action. The `DataIdentifer` array must exactly match the `DataIdentifer` array in the first block of the policy. The `Operation` property with the `Deidentify` action is what actually masks the data, and it must contain the `"MaskConfig": {}` object. The `"MaskConfig": {}` object must be empty.

For an example data protection policy, see the **Examples** section on this page.

### Warning

The contents of the two `DataIdentifer` arrays must match exactly.

In addition to the two JSON blocks, the `policyDocument` can also include `Name` , `Description` , and `Version` fields. The `Name` is different than the operationâs `policyName` parameter, and is used as a dimension when CloudWatch Logs reports audit findings metrics to CloudWatch.

The JSON specified in `policyDocument` can be up to 30,720 characters long.

**Subscription filter policy**

A subscription filter policy can include the following attributes in a JSON block:

- **DestinationArn** The ARN of the destination to deliver log events to. Supported destinations are:
- An Kinesis Data Streams data stream in the same account as the subscription policy, for same-account delivery.
- An Firehose data stream in the same account as the subscription policy, for same-account delivery.
- A Lambda function in the same account as the subscription policy, for same-account delivery.
- A logical destination in a different account created with [PutDestination](https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.html) , for cross-account delivery. Kinesis Data Streams and Firehose are supported as logical destinations.
- **RoleArn** The ARN of an IAM role that grants CloudWatch Logs permissions to deliver ingested log events to the destination stream. You donât need to provide the ARN when you are working with a logical destination for cross-account delivery.
- **FilterPattern** A filter pattern for subscribing to a filtered stream of log events.
- **Distribution** The method used to distribute log data to the destination. By default, log data is grouped by log stream, but the grouping can be set to `Random` for a more even distribution. This property is only applicable when the destination is an Kinesis Data Streams data stream.

**Transformer policy**

A transformer policy must include one JSON block with the array of processors and their configurations. For more information about available processors, see [Processors that you can use](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatch-Logs-Transformation.html#CloudWatch-Logs-Transformation-Processors) .

**Field index policy**

A field index filter policy can include the following attribute in a JSON block:

- **Fields** The array of field indexes to create.

It must contain at least one field index.

The following is an example of an index policy document that creates two indexes, `RequestId` and `TransactionId` .

`"policyDocument": "{ \"Fields\": [ \"RequestId\", \"TransactionId\" ] }"`

`--policy-type` (string)

The type of policy that youâre creating or updating.

Possible values:

- `DATA_PROTECTION_POLICY`
- `SUBSCRIPTION_FILTER_POLICY`
- `FIELD_INDEX_POLICY`
- `TRANSFORMER_POLICY`

`--scope` (string)

Currently the only valid value for this parameter is `ALL` , which specifies that the data protection policy applies to all log groups in the account. If you omit this parameter, the default of `ALL` is used.

Possible values:

- `ALL`

`--selection-criteria` (string)

Use this parameter to apply the new policy to a subset of log groups in the account.

Specifing `selectionCriteria` is valid only when you specify `SUBSCRIPTION_FILTER_POLICY` , `FIELD_INDEX_POLICY` or `TRANSFORMER_POLICY` for `policyType` .

If `policyType` is `SUBSCRIPTION_FILTER_POLICY` , the only supported `selectionCriteria` filter is `LogGroupName NOT IN []`

If `policyType` is `FIELD_INDEX_POLICY` or `TRANSFORMER_POLICY` , the only supported `selectionCriteria` filter is `LogGroupNamePrefix`

The `selectionCriteria` string can be up to 25KB in length. The length is determined by using its UTF-8 bytes.

Using the `selectionCriteria` parameter with `SUBSCRIPTION_FILTER_POLICY` is useful to help prevent infinite loops. For more information, see [Log recursion prevention](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Subscriptions-recursion-prevention.html) .

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

accountPolicy -> (structure)

The account policy that you created.

policyName -> (string)

The name of the account policy.

policyDocument -> (string)

The policy document for this account policy.

The JSON specified in `policyDocument` can be up to 30,720 characters.

lastUpdatedTime -> (long)

The date and time that this policy was most recently updated.

policyType -> (string)

The type of policy for this account policy.

scope -> (string)

The scope of the account policy.

selectionCriteria -> (string)

The log group selection criteria that is used for this policy.

accountId -> (string)

The Amazon Web Services account ID that the policy applies to.