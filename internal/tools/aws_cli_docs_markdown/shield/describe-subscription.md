# describe-subscriptionÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-subscription.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/describe-subscription.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [shield](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/shield/index.html#cli-aws-shield) ]

# describe-subscription

## Description

Provides details about the Shield Advanced subscription for an account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/shield-2016-06-02/DescribeSubscription)

## Synopsis

```
describe-subscription
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

**To retrieve the details of the AWS Shield Advanced protection for the account**

The following `describe-subscription` example displays details about the Shield Advanced protection provided for the account.:

```
aws shield describe-subscription
```

Output:

```
{
    "Subscription": {
        "StartTime": 1534368978.0,
        "EndTime": 1597613778.0,
        "TimeCommitmentInSeconds": 63244800,
        "AutoRenew": "ENABLED",
        "Limits": [
            {
                "Type": "GLOBAL_ACCELERATOR",
                "Max": 1000
            },
            {
                "Type": "ROUTE53_HOSTED_ZONE",
                "Max": 1000
            },
            {
                "Type": "CF_DISTRIBUTION",
                "Max": 1000
            },
            {
                "Type": "ELB_LOAD_BALANCER",
                "Max": 1000
            },
            {
                "Type": "EC2_ELASTIC_IP_ALLOCATION",
                "Max": 1000
            }
        ]
    }
}
```

For more information, see [How AWS Shield Works](https://docs.aws.amazon.com/waf/latest/developerguide/ddos-overview.html) in the *AWS Shield Advanced Developer Guide*.

## Output

Subscription -> (structure)

The Shield Advanced subscription details for an account.

StartTime -> (timestamp)

The start time of the subscription, in Unix time in seconds.

EndTime -> (timestamp)

The date and time your subscription will end.

TimeCommitmentInSeconds -> (long)

The length, in seconds, of the Shield Advanced subscription for the account.

AutoRenew -> (string)

If `ENABLED` , the subscription will be automatically renewed at the end of the existing subscription period.

When you initally create a subscription, `AutoRenew` is set to `ENABLED` . You can change this by submitting an `UpdateSubscription` request. If the `UpdateSubscription` request does not included a value for `AutoRenew` , the existing value for `AutoRenew` remains unchanged.

Limits -> (list)

Specifies how many protections of a given type you can create.

(structure)

Specifies how many protections of a given type you can create.

Type -> (string)

The type of protection.

Max -> (long)

The maximum number of protections that can be created for the specified `Type` .

ProactiveEngagementStatus -> (string)

If `ENABLED` , the Shield Response Team (SRT) will use email and phone to notify contacts about escalations to the SRT and to initiate proactive customer support.

If `PENDING` , you have requested proactive engagement and the request is pending. The status changes to `ENABLED` when your request is fully processed.

If `DISABLED` , the SRT will not proactively notify contacts about escalations or to initiate proactive customer support.

SubscriptionLimits -> (structure)

Limits settings for your subscription.

ProtectionLimits -> (structure)

Limits settings on protections for your subscription.

ProtectedResourceTypeLimits -> (list)

The maximum number of resource types that you can specify in a protection.

(structure)

Specifies how many protections of a given type you can create.

Type -> (string)

The type of protection.

Max -> (long)

The maximum number of protections that can be created for the specified `Type` .

ProtectionGroupLimits -> (structure)

Limits settings on protection groups for your subscription.

MaxProtectionGroups -> (long)

The maximum number of protection groups that you can have at one time.

PatternTypeLimits -> (structure)

Limits settings by pattern type in the protection groups for your subscription.

ArbitraryPatternLimits -> (structure)

Limits settings on protection groups with arbitrary pattern type.

MaxMembers -> (long)

The maximum number of resources you can specify for a single arbitrary pattern in a protection group.

SubscriptionArn -> (string)

The ARN (Amazon Resource Name) of the subscription.