# get-logging-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-logging-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-logging-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wafv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/index.html#cli-aws-wafv2) ]

# get-logging-configuration

## Description

Returns the  LoggingConfiguration for the specified web ACL.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wafv2-2019-07-29/GetLoggingConfiguration)

## Synopsis

```
get-logging-configuration
--resource-arn <value>
[--log-type <value>]
[--log-scope <value>]
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

`--resource-arn` (string)

The Amazon Resource Name (ARN) of the web ACL for which you want to get the  LoggingConfiguration .

`--log-type` (string)

Used to distinguish between various logging options. Currently, there is one option.

Default: `WAF_LOGS`

Possible values:

- `WAF_LOGS`

`--log-scope` (string)

The owner of the logging configuration, which must be set to `CUSTOMER` for the configurations that you manage.

The log scope `SECURITY_LAKE` indicates a configuration that is managed through Amazon Security Lake. You can use Security Lake to collect log and event data from various sources for normalization, analysis, and management. For information, see [Collecting data from Amazon Web Services services](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html) in the *Amazon Security Lake user guide* .

Default: `CUSTOMER`

Possible values:

- `CUSTOMER`
- `SECURITY_LAKE`

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

**To retrieve the logging configurations for a web ACL**

The following `get-logging-configuration` retrieves the logging configuration for the specified web ACL.

```
aws wafv2 get-logging-configuration \
    --resource-arn arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222 \
    --region us-west-2
```

Output:

```
{
    "LoggingConfiguration":{
        "ResourceArn":"arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test/a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
        "RedactedFields":[
            {
                "Method":{

                }
            }
        ],
        "LogDestinationConfigs":[
            "arn:aws:firehose:us-west-2:123456789012:deliverystream/aws-waf-logs-custom-transformation"
        ]
    }
}
```

For more information, see [Logging Web ACL Traffic Information](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

## Output

LoggingConfiguration -> (structure)

The  LoggingConfiguration for the specified web ACL.

ResourceArn -> (string)

The Amazon Resource Name (ARN) of the web ACL that you want to associate with `LogDestinationConfigs` .

LogDestinationConfigs -> (list)

The logging destination configuration that you want to associate with the web ACL.

### Note

You can associate one logging destination to a web ACL.

(string)

RedactedFields -> (list)

The parts of the request that you want to keep out of the logs.

For example, if you redact the `SingleHeader` field, the `HEADER` field in the logs will be `REDACTED` for all rules that use the `SingleHeader` `FieldToMatch` setting.

If you configure data protection for the web ACL, the protection applies to the data that WAF sends to the logs.

Redaction applies only to the component thatâs specified in the ruleâs `FieldToMatch` setting, so the `SingleHeader` redaction doesnât apply to rules that use the `Headers` `FieldToMatch` .

### Note

You can specify only the following fields for redaction: `UriPath` , `QueryString` , `SingleHeader` , and `Method` .

### Note

This setting has no impact on request sampling. You can only exclude fields from request sampling by disabling sampling in the web ACL visibility configuration or by configuring data protection for the web ACL.

(structure)

Specifies a web request component to be used in a rule match statement or in a logging configuration.

- In a rule statement, this is the part of the web request that you want WAF to inspect. Include the single `FieldToMatch` type that you want to inspect, with additional specifications as needed, according to the type. You specify a single request component in `FieldToMatch` for each rule statement that requires it. To inspect more than one component of the web request, create a separate rule statement for each component. Example JSON for a `QueryString` field to match:   `"FieldToMatch": { "QueryString": {} }`   Example JSON for a `Method` field to match specification:  `"FieldToMatch": { "Method": { "Name": "DELETE" } }`
- In a logging configuration, this is used in the `RedactedFields` property to specify a field to redact from the logging records. For this use case, note the following:
- Even though all `FieldToMatch` settings are available, the only valid settings for field redaction are `UriPath` , `QueryString` , `SingleHeader` , and `Method` .
- In this documentation, the descriptions of the individual fields talk about specifying the web request component to inspect, but for field redaction, you are specifying the component type to redact from the logs.
- If you have request sampling enabled, the redacted fields configuration for logging has no impact on sampling. You can only exclude fields from request sampling by disabling sampling in the web ACL visibility configuration or by configuring data protection for the web ACL.

SingleHeader -> (structure)

Inspect a single header. Provide the name of the header to inspect, for example, `User-Agent` or `Referer` . This setting isnât case sensitive.

Example JSON: `"SingleHeader": { "Name": "haystack" }`

Alternately, you can filter and inspect all headers with the `Headers` `FieldToMatch` setting.

Name -> (string)

The name of the query header to inspect.

SingleQueryArgument -> (structure)

Inspect a single query argument. Provide the name of the query argument to inspect, such as *UserName* or *SalesRegion* . The name can be up to 30 characters long and isnât case sensitive.

Example JSON: `"SingleQueryArgument": { "Name": "myArgument" }`

Name -> (string)

The name of the query argument to inspect.

AllQueryArguments -> (structure)

Inspect all query arguments.

UriPath -> (structure)

Inspect the request URI path. This is the part of the web request that identifies a resource, for example, `/images/daily-ad.jpg` .

QueryString -> (structure)

Inspect the query string. This is the part of a URL that appears after a `?` character, if any.

Body -> (structure)

Inspect the request body as plain text. The request body immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.

WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to WAF for inspection.

- For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).
- For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig` , for additional processing fees.
- For Amplify, use the CloudFront limit.

For information about how to handle oversized request bodies, see the `Body` object configuration.

OversizeHandling -> (string)

What WAF should do if the body is larger than WAF can inspect.

WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to WAF for inspection.

- For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).
- For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig` , for additional processing fees.
- For Amplify, use the CloudFront limit.

The options for oversize handling are the following:

- `CONTINUE` - Inspect the available body contents normally, according to the rule inspection criteria.
- `MATCH` - Treat the web request as matching the rule statement. WAF applies the rule action to the request.
- `NO_MATCH` - Treat the web request as not matching the rule statement.

You can combine the `MATCH` or `NO_MATCH` settings for oversize handling with your rule and web ACL action settings, so that you block any request whose body is over the limit.

Default: `CONTINUE`

Method -> (structure)

Inspect the HTTP method. The method indicates the type of operation that the request is asking the origin to perform.

JsonBody -> (structure)

Inspect the request body as JSON. The request body immediately follows the request headers. This is the part of a request that contains any additional data that you want to send to your web server as the HTTP request body, such as data from a form.

WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to WAF for inspection.

- For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).
- For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig` , for additional processing fees.
- For Amplify, use the CloudFront limit.

For information about how to handle oversized request bodies, see the `JsonBody` object configuration.

MatchPattern -> (structure)

The patterns to look for in the JSON body. WAF inspects the results of these pattern matches against the rule inspection criteria.

All -> (structure)

Match all of the elements. See also `MatchScope` in  JsonBody .

You must specify either this setting or the `IncludedPaths` setting, but not both.

IncludedPaths -> (list)

Match only the specified include paths. See also `MatchScope` in  JsonBody .

Provide the include paths using JSON Pointer syntax. For example, `"IncludedPaths": ["/dogs/0/name", "/dogs/1/name"]` . For information about this syntax, see the Internet Engineering Task Force (IETF) documentation [JavaScript Object Notation (JSON) Pointer](https://tools.ietf.org/html/rfc6901) .

You must specify either this setting or the `All` setting, but not both.

### Note

Donât use this option to include all paths. Instead, use the `All` setting.

(string)

MatchScope -> (string)

The parts of the JSON to match against using the `MatchPattern` . If you specify `ALL` , WAF matches against keys and values.

`All` does not require a match to be found in the keys and a match to be found in the values. It requires a match to be found in the keys or the values or both. To require a match in the keys and in the values, use a logical `AND` statement to combine two match rules, one that inspects the keys and another that inspects the values.

InvalidFallbackBehavior -> (string)

What WAF should do if it fails to completely parse the JSON body. The options are the following:

- `EVALUATE_AS_STRING` - Inspect the body as plain text. WAF applies the text transformations and inspection criteria that you defined for the JSON inspection to the body text string.
- `MATCH` - Treat the web request as matching the rule statement. WAF applies the rule action to the request.
- `NO_MATCH` - Treat the web request as not matching the rule statement.

If you donât provide this setting, WAF parses and evaluates the content only up to the first parsing failure that it encounters.

### Note

WAF parsing doesnât fully validate the input JSON string, so parsing can succeed even for invalid JSON. When parsing succeeds, WAF doesnât apply the fallback behavior. For more information, see [JSON body](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body) in the *WAF Developer Guide* .

OversizeHandling -> (string)

What WAF should do if the body is larger than WAF can inspect.

WAF does not support inspecting the entire contents of the web request body if the body exceeds the limit for the resource type. When a web request body is larger than the limit, the underlying host service only forwards the contents that are within the limit to WAF for inspection.

- For Application Load Balancer and AppSync, the limit is fixed at 8 KB (8,192 bytes).
- For CloudFront, API Gateway, Amazon Cognito, App Runner, and Verified Access, the default limit is 16 KB (16,384 bytes), and you can increase the limit for each resource type in the web ACL `AssociationConfig` , for additional processing fees.
- For Amplify, use the CloudFront limit.

The options for oversize handling are the following:

- `CONTINUE` - Inspect the available body contents normally, according to the rule inspection criteria.
- `MATCH` - Treat the web request as matching the rule statement. WAF applies the rule action to the request.
- `NO_MATCH` - Treat the web request as not matching the rule statement.

You can combine the `MATCH` or `NO_MATCH` settings for oversize handling with your rule and web ACL action settings, so that you block any request whose body is over the limit.

Default: `CONTINUE`

Headers -> (structure)

Inspect the request headers. You must configure scope and pattern matching filters in the `Headers` object, to define the set of headers to and the parts of the headers that WAF inspects.

Only the first 8 KB (8192 bytes) of a requestâs headers and only the first 200 headers are forwarded to WAF for inspection by the underlying host service. You must configure how to handle any oversize header content in the `Headers` object. WAF applies the pattern matching filters to the headers that it receives from the underlying host service.

MatchPattern -> (structure)

The filter to use to identify the subset of headers to inspect in a web request.

You must specify exactly one setting: either `All` , `IncludedHeaders` , or `ExcludedHeaders` .

Example JSON: `"MatchPattern": { "ExcludedHeaders": [ "KeyToExclude1", "KeyToExclude2" ] }`

All -> (structure)

Inspect all headers.

IncludedHeaders -> (list)

Inspect only the headers that have a key that matches one of the strings specified here.

(string)

ExcludedHeaders -> (list)

Inspect only the headers whose keys donât match any of the strings specified here.

(string)

MatchScope -> (string)

The parts of the headers to match with the rule inspection criteria. If you specify `ALL` , WAF inspects both keys and values.

`All` does not require a match to be found in the keys and a match to be found in the values. It requires a match to be found in the keys or the values or both. To require a match in the keys and in the values, use a logical `AND` statement to combine two match rules, one that inspects the keys and another that inspects the values.

OversizeHandling -> (string)

What WAF should do if the headers of the request are more numerous or larger than WAF can inspect. WAF does not support inspecting the entire contents of request headers when they exceed 8 KB (8192 bytes) or 200 total headers. The underlying host service forwards a maximum of 200 headers and at most 8 KB of header contents to WAF.

The options for oversize handling are the following:

- `CONTINUE` - Inspect the available headers normally, according to the rule inspection criteria.
- `MATCH` - Treat the web request as matching the rule statement. WAF applies the rule action to the request.
- `NO_MATCH` - Treat the web request as not matching the rule statement.

Cookies -> (structure)

Inspect the request cookies. You must configure scope and pattern matching filters in the `Cookies` object, to define the set of cookies and the parts of the cookies that WAF inspects.

Only the first 8 KB (8192 bytes) of a requestâs cookies and only the first 200 cookies are forwarded to WAF for inspection by the underlying host service. You must configure how to handle any oversize cookie content in the `Cookies` object. WAF applies the pattern matching filters to the cookies that it receives from the underlying host service.

MatchPattern -> (structure)

The filter to use to identify the subset of cookies to inspect in a web request.

You must specify exactly one setting: either `All` , `IncludedCookies` , or `ExcludedCookies` .

Example JSON: `"MatchPattern": { "IncludedCookies": [ "session-id-time", "session-id" ] }`

All -> (structure)

Inspect all cookies.

IncludedCookies -> (list)

Inspect only the cookies that have a key that matches one of the strings specified here.

(string)

ExcludedCookies -> (list)

Inspect only the cookies whose keys donât match any of the strings specified here.

(string)

MatchScope -> (string)

The parts of the cookies to inspect with the rule inspection criteria. If you specify `ALL` , WAF inspects both keys and values.

`All` does not require a match to be found in the keys and a match to be found in the values. It requires a match to be found in the keys or the values or both. To require a match in the keys and in the values, use a logical `AND` statement to combine two match rules, one that inspects the keys and another that inspects the values.

OversizeHandling -> (string)

What WAF should do if the cookies of the request are more numerous or larger than WAF can inspect. WAF does not support inspecting the entire contents of request cookies when they exceed 8 KB (8192 bytes) or 200 total cookies. The underlying host service forwards a maximum of 200 cookies and at most 8 KB of cookie contents to WAF.

The options for oversize handling are the following:

- `CONTINUE` - Inspect the available cookies normally, according to the rule inspection criteria.
- `MATCH` - Treat the web request as matching the rule statement. WAF applies the rule action to the request.
- `NO_MATCH` - Treat the web request as not matching the rule statement.

HeaderOrder -> (structure)

Inspect a string containing the list of the requestâs header names, ordered as they appear in the web request that WAF receives for inspection. WAF generates the string and then uses that as the field to match component in its inspection. WAF separates the header names in the string using colons and no added spaces, for example `host:user-agent:accept:authorization:referer` .

OversizeHandling -> (string)

What WAF should do if the headers of the request are more numerous or larger than WAF can inspect. WAF does not support inspecting the entire contents of request headers when they exceed 8 KB (8192 bytes) or 200 total headers. The underlying host service forwards a maximum of 200 headers and at most 8 KB of header contents to WAF.

The options for oversize handling are the following:

- `CONTINUE` - Inspect the available headers normally, according to the rule inspection criteria.
- `MATCH` - Treat the web request as matching the rule statement. WAF applies the rule action to the request.
- `NO_MATCH` - Treat the web request as not matching the rule statement.

JA3Fingerprint -> (structure)

Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the requestâs JA3 fingerprint. The JA3 fingerprint is a 32-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the clientâs TLS configuration. WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation. Almost all web requests include this information.

### Note

You can use this choice only with a string match `ByteMatchStatement` with the `PositionalConstraint` set to `EXACTLY` .

You can obtain the JA3 fingerprint for client requests from the web ACL logs. If WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see [Log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the *WAF Developer Guide* .

Provide the JA3 fingerprint string from the logs in your string match statement specification, to match with any future requests that have the same TLS configuration.

FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a JA3 fingerprint.

You can specify the following fallback behaviors:

- `MATCH` - Treat the web request as matching the rule statement. WAF applies the rule action to the request.
- `NO_MATCH` - Treat the web request as not matching the rule statement.

JA4Fingerprint -> (structure)

Available for use with Amazon CloudFront distributions and Application Load Balancers. Match against the requestâs JA4 fingerprint. The JA4 fingerprint is a 36-character hash derived from the TLS Client Hello of an incoming request. This fingerprint serves as a unique identifier for the clientâs TLS configuration. WAF calculates and logs this fingerprint for each request that has enough TLS Client Hello information for the calculation. Almost all web requests include this information.

### Note

You can use this choice only with a string match `ByteMatchStatement` with the `PositionalConstraint` set to `EXACTLY` .

You can obtain the JA4 fingerprint for client requests from the web ACL logs. If WAF is able to calculate the fingerprint, it includes it in the logs. For information about the logging fields, see [Log fields](https://docs.aws.amazon.com/waf/latest/developerguide/logging-fields.html) in the *WAF Developer Guide* .

Provide the JA4 fingerprint string from the logs in your string match statement specification, to match with any future requests that have the same TLS configuration.

FallbackBehavior -> (string)

The match status to assign to the web request if the request doesnât have a JA4 fingerprint.

You can specify the following fallback behaviors:

- `MATCH` - Treat the web request as matching the rule statement. WAF applies the rule action to the request.
- `NO_MATCH` - Treat the web request as not matching the rule statement.

UriFragment -> (structure)

Inspect fragments of the request URI. You must configure scope and pattern matching filters in the `UriFragment` object, to define the fragment of a URI that WAF inspects.

Only the first 8 KB (8192 bytes) of a requestâs URI fragments and only the first 200 URI fragments are forwarded to WAF for inspection by the underlying host service. You must configure how to handle any oversize URI fragment content in the `UriFragment` object. WAF applies the pattern matching filters to the cookies that it receives from the underlying host service.

FallbackBehavior -> (string)

What WAF should do if it fails to completely parse the JSON body. The options are the following:

- `EVALUATE_AS_STRING` - Inspect the body as plain text. WAF applies the text transformations and inspection criteria that you defined for the JSON inspection to the body text string.
- `MATCH` - Treat the web request as matching the rule statement. WAF applies the rule action to the request.
- `NO_MATCH` - Treat the web request as not matching the rule statement.

If you donât provide this setting, WAF parses and evaluates the content only up to the first parsing failure that it encounters.

Example JSON: `{ "UriFragment": { "FallbackBehavior": "MATCH"} }`

### Note

WAF parsing doesnât fully validate the input JSON string, so parsing can succeed even for invalid JSON. When parsing succeeds, WAF doesnât apply the fallback behavior. For more information, see [JSON body](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-fields-list.html#waf-rule-statement-request-component-json-body) in the *WAF Developer Guide* .

ManagedByFirewallManager -> (boolean)

Indicates whether the logging configuration was created by Firewall Manager, as part of an WAF policy configuration. If true, only Firewall Manager can modify or delete the configuration.

The logging configuration can be created by Firewall Manager for use with any web ACL that Firewall Manager is using for an WAF policy. Web ACLs that Firewall Manager creates and uses have their `ManagedByFirewallManager` property set to true. Web ACLs that were created by a customer account and then retrofitted by Firewall Manager for use by a policy have their `RetrofittedByFirewallManager` property set to true. For either case, any corresponding logging configuration will indicate `ManagedByFirewallManager` .

LoggingFilter -> (structure)

Filtering that specifies which web requests are kept in the logs and which are dropped. You can filter on the rule action and on the web request labels that were applied by matching rules during web ACL evaluation.

Filters -> (list)

The filters that you want to apply to the logs.

(structure)

A single logging filter, used in  LoggingFilter .

Behavior -> (string)

How to handle logs that satisfy the filterâs conditions and requirement.

Requirement -> (string)

Logic to apply to the filtering conditions. You can specify that, in order to satisfy the filter, a log must match all conditions or must match at least one condition.

Conditions -> (list)

Match conditions for the filter.

(structure)

A single match condition for a  Filter .

ActionCondition -> (structure)

A single action condition. This is the action setting that a log record must contain in order to meet the condition.

Action -> (string)

The action setting that a log record must contain in order to meet the condition. This is the action that WAF applied to the web request.

For rule groups, this is either the configured rule action setting, or if youâve applied a rule action override to the rule, itâs the override action. The value `EXCLUDED_AS_COUNT` matches on excluded rules and also on rules that have a rule action override of Count.

LabelNameCondition -> (structure)

A single label name condition. This is the fully qualified label name that a log record must contain in order to meet the condition. Fully qualified labels have a prefix, optional namespaces, and label name. The prefix identifies the rule group or web ACL context of the rule that added the label.

LabelName -> (string)

The label name that a log record must contain in order to meet the condition. This must be a fully qualified label name. Fully qualified labels have a prefix, optional namespaces, and label name. The prefix identifies the rule group or web ACL context of the rule that added the label.

DefaultBehavior -> (string)

Default handling for logs that donât match any of the specified filtering conditions.

LogType -> (string)

Used to distinguish between various logging options. Currently, there is one option.

Default: `WAF_LOGS`

LogScope -> (string)

The owner of the logging configuration, which must be set to `CUSTOMER` for the configurations that you manage.

The log scope `SECURITY_LAKE` indicates a configuration that is managed through Amazon Security Lake. You can use Security Lake to collect log and event data from various sources for normalization, analysis, and management. For information, see [Collecting data from Amazon Web Services services](https://docs.aws.amazon.com/security-lake/latest/userguide/internal-sources.html) in the *Amazon Security Lake user guide* .

Default: `CUSTOMER`