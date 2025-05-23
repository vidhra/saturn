# describe-managed-rule-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/describe-managed-rule-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/describe-managed-rule-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wafv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/index.html#cli-aws-wafv2) ]

# describe-managed-rule-group

## Description

Provides high-level information for a managed rule group, including descriptions of the rules.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wafv2-2019-07-29/DescribeManagedRuleGroup)

## Synopsis

```
describe-managed-rule-group
--vendor-name <value>
--name <value>
--scope <value>
[--version-name <value>]
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

`--vendor-name` (string)

The name of the managed rule group vendor. You use this, along with the rule group name, to identify a rule group.

`--name` (string)

The name of the managed rule group. You use this, along with the vendor name, to identify the rule group.

`--scope` (string)

Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use `CLOUDFRONT` .

To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:

- CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1` .
- API and SDKs - For all calls, use the Region endpoint us-east-1.

Possible values:

- `CLOUDFRONT`
- `REGIONAL`

`--version-name` (string)

The version of the rule group. You can only use a version that is not scheduled for expiration. If you donât provide this, WAF uses the vendorâs default version.

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

**To retrieve the description for a managed rule group**

The following `describe-managed-rule-group` retrieves the description for an AWS managed rule group.

```
aws wafv2 describe-managed-rule-group \
    --vendor-name AWS \
    --name AWSManagedRulesCommonRuleSet \
    --scope REGIONAL
```

Output:

```
{
    "Capacity": 700,
    "Rules": [
        {
            "Name": "NoUserAgent_HEADER",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "UserAgent_BadBots_HEADER",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "SizeRestrictions_QUERYSTRING",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "SizeRestrictions_Cookie_HEADER",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "SizeRestrictions_BODY",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "SizeRestrictions_URIPATH",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "EC2MetaDataSSRF_BODY",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "EC2MetaDataSSRF_COOKIE",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "EC2MetaDataSSRF_URIPATH",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "EC2MetaDataSSRF_QUERYARGUMENTS",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "GenericLFI_QUERYARGUMENTS",
            "Action": {
                "Block": {}
            }
        },
        {
            }
            "Name": "GenericLFI_URIPATH",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "GenericLFI_BODY",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "RestrictedExtensions_URIPATH",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "RestrictedExtensions_QUERYARGUMENTS",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "GenericRFI_QUERYARGUMENTS",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "GenericRFI_BODY",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "GenericRFI_URIPATH",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "CrossSiteScripting_COOKIE",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "CrossSiteScripting_QUERYARGUMENTS",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "CrossSiteScripting_BODY",
            "Action": {
                "Block": {}
            }
        },
        {
            "Name": "CrossSiteScripting_URIPATH",
            "Action": {
                "Block": {}
            }
        }
    ]
}
```

For more information, see [Managed Rule Groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-rule-groups.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

## Output

VersionName -> (string)

The managed rule groupâs version.

SnsTopicArn -> (string)

The Amazon resource name (ARN) of the Amazon Simple Notification Service SNS topic thatâs used to provide notification of changes to the managed rule group. You can subscribe to the SNS topic to receive notifications when the managed rule group is modified, such as for new versions and for version expiration. For more information, see the [Amazon Simple Notification Service Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) .

Capacity -> (long)

The web ACL capacity units (WCUs) required for this rule group.

WAF uses WCUs to calculate and control the operating resources that are used to run your rules, rule groups, and web ACLs. WAF calculates capacity differently for each rule type, to reflect the relative cost of each rule. Simple rules that cost little to run use fewer WCUs than more complex rules that use more processing power. Rule group capacity is fixed at creation, which helps users plan their web ACL WCU usage when they use a rule group. For more information, see [WAF web ACL capacity units (WCU)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-waf-capacity-units.html) in the *WAF Developer Guide* .

Rules -> (list)

(structure)

High-level information about a  Rule , returned by operations like  DescribeManagedRuleGroup . This provides information like the ID, that you can use to retrieve and manage a `RuleGroup` , and the ARN, that you provide to the  RuleGroupReferenceStatement to use the rule group in a  Rule .

Name -> (string)

The name of the rule.

Action -> (structure)

The action that WAF should take on a web request when it matches a ruleâs statement. Settings at the web ACL level can override the rule action setting.

Block -> (structure)

Instructs WAF to block the web request.

CustomResponse -> (structure)

Defines a custom response for the web request.

For information about customizing web requests and responses, see [Customizing web requests and responses in WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the *WAF Developer Guide* .

ResponseCode -> (integer)

The HTTP status code to return to the client.

For a list of status codes that you can use in your custom responses, see [Supported status codes for custom response](https://docs.aws.amazon.com/waf/latest/developerguide/customizing-the-response-status-codes.html) in the *WAF Developer Guide* .

CustomResponseBodyKey -> (string)

References the response body that you want WAF to return to the web request client. You can define a custom response for a rule action or a default web ACL action that is set to block. To do this, you first define the response body key and value in the `CustomResponseBodies` setting for the  WebACL or  RuleGroup where you want to use it. Then, in the rule action or web ACL default action `BlockAction` setting, you reference the response body using this key.

ResponseHeaders -> (list)

The HTTP headers to use in the response. You can specify any header name except for `content-type` . Duplicate header names are not allowed.

For information about the limits on count and size for custom request and response settings, see [WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the *WAF Developer Guide* .

(structure)

A custom header for custom request and response handling. This is used in  CustomResponse and  CustomRequestHandling .

Name -> (string)

The name of the custom header.

For custom request header insertion, when WAF inserts the header into the request, it prefixes this name `x-amzn-waf-` , to avoid confusion with the headers that are already in the request. For example, for the header name `sample` , WAF inserts the header `x-amzn-waf-sample` .

Value -> (string)

The value of the custom header.

Allow -> (structure)

Instructs WAF to allow the web request.

CustomRequestHandling -> (structure)

Defines custom handling for the web request.

For information about customizing web requests and responses, see [Customizing web requests and responses in WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the *WAF Developer Guide* .

InsertHeaders -> (list)

The HTTP headers to insert into the request. Duplicate header names are not allowed.

For information about the limits on count and size for custom request and response settings, see [WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the *WAF Developer Guide* .

(structure)

A custom header for custom request and response handling. This is used in  CustomResponse and  CustomRequestHandling .

Name -> (string)

The name of the custom header.

For custom request header insertion, when WAF inserts the header into the request, it prefixes this name `x-amzn-waf-` , to avoid confusion with the headers that are already in the request. For example, for the header name `sample` , WAF inserts the header `x-amzn-waf-sample` .

Value -> (string)

The value of the custom header.

Count -> (structure)

Instructs WAF to count the web request and then continue evaluating the request using the remaining rules in the web ACL.

CustomRequestHandling -> (structure)

Defines custom handling for the web request.

For information about customizing web requests and responses, see [Customizing web requests and responses in WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the *WAF Developer Guide* .

InsertHeaders -> (list)

The HTTP headers to insert into the request. Duplicate header names are not allowed.

For information about the limits on count and size for custom request and response settings, see [WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the *WAF Developer Guide* .

(structure)

A custom header for custom request and response handling. This is used in  CustomResponse and  CustomRequestHandling .

Name -> (string)

The name of the custom header.

For custom request header insertion, when WAF inserts the header into the request, it prefixes this name `x-amzn-waf-` , to avoid confusion with the headers that are already in the request. For example, for the header name `sample` , WAF inserts the header `x-amzn-waf-sample` .

Value -> (string)

The value of the custom header.

Captcha -> (structure)

Instructs WAF to run a `CAPTCHA` check against the web request.

CustomRequestHandling -> (structure)

Defines custom handling for the web request, used when the `CAPTCHA` inspection determines that the requestâs token is valid and unexpired.

For information about customizing web requests and responses, see [Customizing web requests and responses in WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the *WAF Developer Guide* .

InsertHeaders -> (list)

The HTTP headers to insert into the request. Duplicate header names are not allowed.

For information about the limits on count and size for custom request and response settings, see [WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the *WAF Developer Guide* .

(structure)

A custom header for custom request and response handling. This is used in  CustomResponse and  CustomRequestHandling .

Name -> (string)

The name of the custom header.

For custom request header insertion, when WAF inserts the header into the request, it prefixes this name `x-amzn-waf-` , to avoid confusion with the headers that are already in the request. For example, for the header name `sample` , WAF inserts the header `x-amzn-waf-sample` .

Value -> (string)

The value of the custom header.

Challenge -> (structure)

Instructs WAF to run a `Challenge` check against the web request.

CustomRequestHandling -> (structure)

Defines custom handling for the web request, used when the challenge inspection determines that the requestâs token is valid and unexpired.

For information about customizing web requests and responses, see [Customizing web requests and responses in WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-custom-request-response.html) in the *WAF Developer Guide* .

InsertHeaders -> (list)

The HTTP headers to insert into the request. Duplicate header names are not allowed.

For information about the limits on count and size for custom request and response settings, see [WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) in the *WAF Developer Guide* .

(structure)

A custom header for custom request and response handling. This is used in  CustomResponse and  CustomRequestHandling .

Name -> (string)

The name of the custom header.

For custom request header insertion, when WAF inserts the header into the request, it prefixes this name `x-amzn-waf-` , to avoid confusion with the headers that are already in the request. For example, for the header name `sample` , WAF inserts the header `x-amzn-waf-sample` .

Value -> (string)

The value of the custom header.

LabelNamespace -> (string)

The label namespace prefix for this rule group. All labels added by rules in this rule group have this prefix.

- The syntax for the label namespace prefix for a managed rule group is the following:   `awswaf:managed:<vendor>:<rule group name>` :
- When a rule with a label matches a web request, WAF adds the fully qualified label to the request. A fully qualified label is made up of the label namespace from the rule group or web ACL where the rule is defined and the label from the rule, separated by a colon:   `<label namespace>:<label from rule>`

AvailableLabels -> (list)

The labels that one or more rules in this rule group add to matching web requests. These labels are defined in the `RuleLabels` for a  Rule .

(structure)

List of labels used by one or more of the rules of a  RuleGroup . This summary object is used for the following rule group lists:

- `AvailableLabels` - Labels that rules add to matching requests. These labels are defined in the `RuleLabels` for a  Rule .
- `ConsumedLabels` - Labels that rules match against. These labels are defined in a `LabelMatchStatement` specification, in the  Statement definition of a rule.

Name -> (string)

An individual label specification.

ConsumedLabels -> (list)

The labels that one or more rules in this rule group match against in label match statements. These labels are defined in a `LabelMatchStatement` specification, in the  Statement definition of a rule.

(structure)

List of labels used by one or more of the rules of a  RuleGroup . This summary object is used for the following rule group lists:

- `AvailableLabels` - Labels that rules add to matching requests. These labels are defined in the `RuleLabels` for a  Rule .
- `ConsumedLabels` - Labels that rules match against. These labels are defined in a `LabelMatchStatement` specification, in the  Statement definition of a rule.

Name -> (string)

An individual label specification.