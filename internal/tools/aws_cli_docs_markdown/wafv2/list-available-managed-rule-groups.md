# list-available-managed-rule-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-available-managed-rule-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/list-available-managed-rule-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wafv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/index.html#cli-aws-wafv2) ]

# list-available-managed-rule-groups

## Description

Retrieves an array of managed rule groups that are available for you to use. This list includes all Amazon Web Services Managed Rules rule groups and all of the Amazon Web Services Marketplace managed rule groups that youâre subscribed to.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wafv2-2019-07-29/ListAvailableManagedRuleGroups)

## Synopsis

```
list-available-managed-rule-groups
--scope <value>
[--next-marker <value>]
[--limit <value>]
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

`--next-marker` (string)

When you request a list of objects with a `Limit` setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a `NextMarker` value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

`--limit` (integer)

The maximum number of objects that you want WAF to return for this request. If more objects are available, in the response, WAF provides a `NextMarker` value that you can use in a subsequent call to get the next batch of objects.

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

**To retrieve the managed rule groups**

The following `list-available-managed-rule-groups` returns the list of all managed rule groups that are currently available for use in your web ACLs.

```
aws wafv2 list-available-managed-rule-groups \
    --scope REGIONAL
```

Output:

```
{
    "ManagedRuleGroups": [
        {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesCommonRuleSet",
            "Description": "Contains rules that are generally applicable to web applications. This provides protection against exploitation of a wide range of vulnerabilities, including those described in OWASP publications and common Common Vulnerabilities and Exposures (CVE)."
        },
        {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesAdminProtectionRuleSet",
            "Description": "Contains rules that allow you to block external access to exposed admin pages. This may be useful if you are running third-party software or would like to reduce the risk of a malicious actor gaining administrative access to your application."
        },
        {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesKnownBadInputsRuleSet",
            "Description": "Contains rules that allow you to block request patterns that are known to be invalid and are associated with exploitation or discovery of vulnerabilities. This can help reduce the risk of a malicious actor discovering a vulnerable application."
        },
        {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesSQLiRuleSet",
            "Description": "Contains rules that allow you to block request patterns associated with exploitation of SQL databases, like SQL injection attacks. This can help prevent remote injection of unauthorized queries."
        },
        {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesLinuxRuleSet",
            "Description": "Contains rules that block request patterns associated with exploitation of vulnerabilities specific to Linux, including LFI attacks. This can help prevent attacks that expose file contents or execute code for which the attacker should not have had access."
        },
        {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesUnixRuleSet",
            "Description": "Contains rules that block request patterns associated with exploiting vulnerabilities specific to POSIX/POSIX-like OS, including LFI attacks. This can help prevent attacks that expose file contents or execute code for which access should not been allowed."
        },
        {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesWindowsRuleSet",
            "Description": "Contains rules that block request patterns associated with exploiting vulnerabilities specific to Windows, (e.g., PowerShell commands). This can help prevent exploits that allow attacker to run unauthorized commands or execute malicious code."
        },
        {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesPHPRuleSet",
            "Description": "Contains rules that block request patterns associated with exploiting vulnerabilities specific to the use of the PHP, including injection of unsafe PHP functions. This can help prevent exploits that allow an attacker to remotely execute code or commands."
        },
        {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesWordPressRuleSet",
            "Description": "The WordPress Applications group contains rules that block request patterns associated with the exploitation of vulnerabilities specific to WordPress sites."
        },
        {
            "VendorName": "AWS",
            "Name": "AWSManagedRulesAmazonIpReputationList",
            "Description": "This group contains rules that are based on Amazon threat intelligence. This is useful if you would like to block sources associated with bots or other threats."
        }
    ]
}
```

For more information, see [Managed Rule Groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

## Output

NextMarker -> (string)

When you request a list of objects with a `Limit` setting, if the number of objects that are still available for retrieval exceeds the limit, WAF returns a `NextMarker` value in the response. To retrieve the next batch of objects, provide the marker from the prior call in your next request.

ManagedRuleGroups -> (list)

Array of managed rule groups that you can use. If you specified a `Limit` in your request, this might not be the full list.

(structure)

High-level information about a managed rule group, returned by  ListAvailableManagedRuleGroups . This provides information like the name and vendor name, that you provide when you add a  ManagedRuleGroupStatement to a web ACL. Managed rule groups include Amazon Web Services Managed Rules rule groups and Amazon Web Services Marketplace managed rule groups. To use any Amazon Web Services Marketplace managed rule group, first subscribe to the rule group through Amazon Web Services Marketplace.

VendorName -> (string)

The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.

Name -> (string)

The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

VersioningSupported -> (boolean)

Indicates whether the managed rule group is versioned. If it is, you can retrieve the versions list by calling  ListAvailableManagedRuleGroupVersions .

Description -> (string)

The description of the managed rule group, provided by Amazon Web Services Managed Rules or the Amazon Web Services Marketplace seller who manages it.