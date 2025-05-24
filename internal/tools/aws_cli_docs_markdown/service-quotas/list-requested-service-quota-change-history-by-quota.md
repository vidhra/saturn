# list-requested-service-quota-change-history-by-quotaÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-requested-service-quota-change-history-by-quota.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-requested-service-quota-change-history-by-quota.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [service-quotas](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/index.html#cli-aws-service-quotas) ]

# list-requested-service-quota-change-history-by-quota

## Description

Retrieves the quota increase requests for the specified quota. Filter responses to return quota requests at either the account level, resource level, or all levels.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/service-quotas-2019-06-24/ListRequestedServiceQuotaChangeHistoryByQuota)

`list-requested-service-quota-change-history-by-quota` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `RequestedQuotas`

## Synopsis

```
list-requested-service-quota-change-history-by-quota
--service-code <value>
--quota-code <value>
[--status <value>]
[--quota-requested-at-level <value>]
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

`--service-code` (string)

Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the  ListServices operation.

`--quota-code` (string)

Specifies the quota identifier. To find the quota code for a specific quota, use the  ListServiceQuotas operation, and look for the `QuotaCode` response in the output for the quota you want.

`--status` (string)

Specifies that you want to filter the results to only the requests with the matching status.

Possible values:

- `PENDING`
- `CASE_OPENED`
- `APPROVED`
- `DENIED`
- `CASE_CLOSED`
- `NOT_APPROVED`
- `INVALID_REQUEST`

`--quota-requested-at-level` (string)

Filters the response to return quota requests for the `ACCOUNT` , `RESOURCE` , or `ALL` levels. `ACCOUNT` is the default.

Possible values:

- `ACCOUNT`
- `RESOURCE`
- `ALL`

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

**To list your quota increase requests**

The following `list-requested-service-quota-change-history-by-quota` example lists the quota increase requests for the specified quota.

```
aws service-quotas list-requested-service-quota-change-history-by-quota \
    --service-code ec2 \
    --quota-code L-20F13EBD
```

Output:

```
{
    "RequestedQuotas": [
        {
            "Id": "d187537d15254312a9609aa51bbf7624u7W49tPO",
            "CaseId": "6780195351",
            "ServiceCode": "ec2",
            "ServiceName": "Amazon Elastic Compute Cloud (Amazon EC2)",
            "QuotaCode": "L-20F13EBD",
            "QuotaName": "Running Dedicated c5n Hosts",
            "DesiredValue": 2.0,
            "Status": "CASE_OPENED",
            "Created": 1580446904.067,
            "LastUpdated": 1580446953.265,
            "Requester": "{\"accountId\":\"123456789012\",\"callerArn\":\"arn:aws:iam::123456789012:root\"}",
            "QuotaArn": "arn:aws:servicequotas:us-east-2:123456789012:ec2/L-20F13EBD",
            "GlobalQuota": false,
            "Unit": "None"
        }
    ]
}
```

## Output

NextToken -> (string)

If present, indicates that more output is available than is included in the current response. Use this value in the `NextToken` request parameter in a subsequent call to the operation to get the next part of the output. You should repeat this until the `NextToken` response element comes back as `null` .

RequestedQuotas -> (list)

Information about the quota increase requests.

(structure)

Information about a quota increase request.

Id -> (string)

The unique identifier.

CaseId -> (string)

The case ID.

ServiceCode -> (string)

Specifies the service identifier. To find the service code value for an Amazon Web Services service, use the  ListServices operation.

ServiceName -> (string)

Specifies the service name.

QuotaCode -> (string)

Specifies the quota identifier. To find the quota code for a specific quota, use the  ListServiceQuotas operation, and look for the `QuotaCode` response in the output for the quota you want.

QuotaName -> (string)

Specifies the quota name.

DesiredValue -> (double)

The new, increased value for the quota.

Status -> (string)

The state of the quota increase request.

- `PENDING` : The quota increase request is under review by Amazon Web Services.
- `CASE_OPENED` : Service Quotas opened a support case to process the quota increase request. Follow-up on the support case for more information.
- `APPROVED` : The quota increase request is approved.
- `DENIED` : The quota increase request canât be approved by Service Quotas. Contact Amazon Web Services Support for more details.
- `NOT APPROVED` : The quota increase request canât be approved by Service Quotas. Contact Amazon Web Services Support for more details.
- `CASE_CLOSED` : The support case associated with this quota increase request was closed. Check the support case correspondence for the outcome of your quota request.
- `INVALID_REQUEST` : Service Quotas couldnât process your resource-level quota increase request because the Amazon Resource Name (ARN) specified as part of the `ContextId` is invalid.

Created -> (timestamp)

The date and time when the quota increase request was received and the case ID was created.

LastUpdated -> (timestamp)

The date and time of the most recent change.

Requester -> (string)

The IAM identity of the requester.

QuotaArn -> (string)

The Amazon Resource Name (ARN) of the quota.

GlobalQuota -> (boolean)

Indicates whether the quota is global.

Unit -> (string)

The unit of measurement.

QuotaRequestedAtLevel -> (string)

Filters the response to return quota requests for the `ACCOUNT` , `RESOURCE` , or `ALL` levels. `ACCOUNT` is the default.

QuotaContext -> (structure)

The context for this service quota.

ContextScope -> (string)

Specifies the scope to which the quota value is applied. If the scope is `RESOURCE` , the quota value is applied to each resource in the Amazon Web Services account. If the scope is `ACCOUNT` , the quota value is applied to the Amazon Web Services account.

ContextScopeType -> (string)

Specifies the resource type to which the quota can be applied.

ContextId -> (string)

Specifies the resource, or resources, to which the quota applies. The value for this field is either an Amazon Resource Name (ARN) or [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-requested-service-quota-change-history-by-quota.html#id1). If the value is an ARN, the quota value applies to that resource. If the value is [*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/service-quotas/list-requested-service-quota-change-history-by-quota.html#id3), then the quota value applies to all resources listed in the `ContextScopeType` field. The quota value applies to all resources for which you havenât previously applied a quota value, and any new resources you create in your Amazon Web Services account.