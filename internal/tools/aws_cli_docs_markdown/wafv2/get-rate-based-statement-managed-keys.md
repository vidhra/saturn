# get-rate-based-statement-managed-keysÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-rate-based-statement-managed-keys.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-rate-based-statement-managed-keys.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wafv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/index.html#cli-aws-wafv2) ]

# get-rate-based-statement-managed-keys

## Description

Retrieves the IP addresses that are currently blocked by a rate-based rule instance. This is only available for rate-based rules that aggregate solely on the IP address or on the forwarded IP address.

The maximum number of addresses that can be blocked for a single rate-based rule instance is 10,000. If more than 10,000 addresses exceed the rate limit, those with the highest rates are blocked.

For a rate-based rule that youâve defined inside a rule group, provide the name of the rule group reference statement in your request, in addition to the rate-based rule name and the web ACL name.

WAF monitors web requests and manages keys independently for each unique combination of web ACL, optional rule group, and rate-based rule. For example, if you define a rate-based rule inside a rule group, and then use the rule group in a web ACL, WAF monitors web requests and manages keys for that web ACL, rule group reference statement, and rate-based rule instance. If you use the same rule group in a second web ACL, WAF monitors web requests and manages keys for this second usage completely independent of your first.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wafv2-2019-07-29/GetRateBasedStatementManagedKeys)

## Synopsis

```
get-rate-based-statement-managed-keys
--scope <value>
--web-acl-name <value>
--web-acl-id <value>
[--rule-group-rule-name <value>]
--rule-name <value>
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

`--scope` (string)

Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use `CLOUDFRONT` .

To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:

- CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1` .
- API and SDKs - For all calls, use the Region endpoint us-east-1.

Possible values:

- `CLOUDFRONT`
- `REGIONAL`

`--web-acl-name` (string)

The name of the web ACL. You cannot change the name of a web ACL after you create it.

`--web-acl-id` (string)

The unique identifier for the web ACL. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

`--rule-group-rule-name` (string)

The name of the rule group reference statement in your web ACL. This is required only when you have the rate-based rule nested inside a rule group.

`--rule-name` (string)

The name of the rate-based rule to get the keys for. If you have the rule defined inside a rule group that youâre using in your web ACL, also provide the name of the rule group reference statement in the request parameter `RuleGroupRuleName` .

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

**To retrieve a list of IP addresses that are blocked by a rate-based rule**

The following `get-rate-based-statement-managed-keys` retrieves the IP addresses currently blocked by a rate-based rule thatâs being used for a regional application.

```
aws wafv2 get-rate-based-statement-managed-keys \
    --scope REGIONAL \
    --web-acl-name testwebacl2 \
    --web-acl-id a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --rule-name ratebasedtest
```

Output:

```
{
    "ManagedKeysIPV4":{
        "IPAddressVersion":"IPV4",
        "Addresses":[
            "198.51.100.0/32"
        ]
    },
    "ManagedKeysIPV6":{
        "IPAddressVersion":"IPV6",
        "Addresses":[

        ]
    }
}
```

For more information, see [Rate-Based Rule Statement](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-type-rate-based.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

## Output

ManagedKeysIPV4 -> (structure)

The keys that are of Internet Protocol version 4 (IPv4).

IPAddressVersion -> (string)

The version of the IP addresses, either `IPV4` or `IPV6` .

Addresses -> (list)

The IP addresses that are currently blocked.

(string)

ManagedKeysIPV6 -> (structure)

The keys that are of Internet Protocol version 6 (IPv6).

IPAddressVersion -> (string)

The version of the IP addresses, either `IPV4` or `IPV6` .

Addresses -> (list)

The IP addresses that are currently blocked.

(string)