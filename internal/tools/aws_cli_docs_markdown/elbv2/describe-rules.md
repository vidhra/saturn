# describe-rulesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-rules.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-rules.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [elbv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/index.html#cli-aws-elbv2) ]

# describe-rules

## Description

Describes the specified rules or the rules for the specified listener. You must specify either a listener or one or more rules.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticloadbalancingv2-2015-12-01/DescribeRules)

`describe-rules` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `Rules`

## Synopsis

```
describe-rules
[--listener-arn <value>]
[--rule-arns <value>]
[--page-size <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--listener-arn` (string)

The Amazon Resource Name (ARN) of the listener.

`--rule-arns` (list)

The Amazon Resource Names (ARN) of the rules.

(string)

Syntax:

```
"string" "string" ...
```

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

**Example 1: To describe a rule**

The following `describe-rules` example displays details for the specified rule.

```
aws elbv2 describe-rules \
    --rule-arns arn:aws:elasticloadbalancing:us-west-2:123456789012:listener-rule/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2/9683b2d02a6cabee
```

**Example 2: To describe the rules for a listener**

The following `describe-rules` example displays details for the rules for the specified listener. The output includes the default rule and any other rules that youâve added.

```
aws elbv2 describe-rules \
    --listener-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:listener/app/my-load-balancer/50dc6c495c0c9188/f2f7dc8efc522ab2
```

## Output

Rules -> (list)

Information about the rules.

(structure)

Information about a rule.

RuleArn -> (string)

The Amazon Resource Name (ARN) of the rule.

Priority -> (string)

The priority.

Conditions -> (list)

The conditions. Each rule can include zero or one of the following conditions: `http-request-method` , `host-header` , `path-pattern` , and `source-ip` , and zero or more of the following conditions: `http-header` and `query-string` .

(structure)

Information about a condition for a rule.

Each rule can optionally include up to one of each of the following conditions: `http-request-method` , `host-header` , `path-pattern` , and `source-ip` . Each rule can also optionally include one or more of each of the following conditions: `http-header` and `query-string` . Note that the value for a condition canât be empty.

For more information, see [Quotas for your Application Load Balancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-limits.html) .

Field -> (string)

The field in the HTTP request. The following are the possible values:

- `http-header`
- `http-request-method`
- `host-header`
- `path-pattern`
- `query-string`
- `source-ip`

Values -> (list)

The condition value. Specify only when `Field` is `host-header` or `path-pattern` . Alternatively, to specify multiple host names or multiple path patterns, use `HostHeaderConfig` or `PathPatternConfig` .

If `Field` is `host-header` and you are not using `HostHeaderConfig` , you can specify a single host name (for example, my.example.com) in `Values` . A host name is case insensitive, can be up to 128 characters in length, and can contain any of the following characters.

- A-Z, a-z, 0-9
- - .
- - (matches 0 or more characters)
- ? (matches exactly 1 character)

If `Field` is `path-pattern` and you are not using `PathPatternConfig` , you can specify a single path pattern (for example, /img/[*](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/elbv2/describe-rules.html#id1)) in `Values` . A path pattern is case-sensitive, can be up to 128 characters in length, and can contain any of the following characters.

- A-Z, a-z, 0-9
- _ - . $ / ~ â â @ : +
- & (using &amp;)
- - (matches 0 or more characters)
- ? (matches exactly 1 character)

(string)

HostHeaderConfig -> (structure)

Information for a host header condition. Specify only when `Field` is `host-header` .

Values -> (list)

The host names. The maximum size of each name is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).

If you specify multiple strings, the condition is satisfied if one of the strings matches the host name.

(string)

PathPatternConfig -> (structure)

Information for a path pattern condition. Specify only when `Field` is `path-pattern` .

Values -> (list)

The path patterns to compare against the request URL. The maximum size of each string is 128 characters. The comparison is case sensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).

If you specify multiple strings, the condition is satisfied if one of them matches the request URL. The path pattern is compared only to the path of the URL, not to its query string. To compare against the query string, use  QueryStringConditionConfig .

(string)

HttpHeaderConfig -> (structure)

Information for an HTTP header condition. Specify only when `Field` is `http-header` .

HttpHeaderName -> (string)

The name of the HTTP header field. The maximum size is 40 characters. The header name is case insensitive. The allowed characters are specified by RFC 7230. Wildcards are not supported.

You canât use an HTTP header condition to specify the host header. Use  HostHeaderConditionConfig to specify a host header condition.

Values -> (list)

The strings to compare against the value of the HTTP header. The maximum size of each string is 128 characters. The comparison strings are case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character).

If the same header appears multiple times in the request, we search them in order until a match is found.

If you specify multiple strings, the condition is satisfied if one of the strings matches the value of the HTTP header. To require that all of the strings are a match, create one condition per string.

(string)

QueryStringConfig -> (structure)

Information for a query string condition. Specify only when `Field` is `query-string` .

Values -> (list)

The key/value pairs or values to find in the query string. The maximum size of each string is 128 characters. The comparison is case insensitive. The following wildcard characters are supported: * (matches 0 or more characters) and ? (matches exactly 1 character). To search for a literal â*â or â?â character in a query string, you must escape these characters in `Values` using a â' character.

If you specify multiple key/value pairs or values, the condition is satisfied if one of them is found in the query string.

(structure)

Information about a key/value pair.

Key -> (string)

The key. You can omit the key.

Value -> (string)

The value.

HttpRequestMethodConfig -> (structure)

Information for an HTTP method condition. Specify only when `Field` is `http-request-method` .

Values -> (list)

The name of the request method. The maximum size is 40 characters. The allowed characters are A-Z, hyphen (-), and underscore (_). The comparison is case sensitive. Wildcards are not supported; therefore, the method name must be an exact match.

If you specify multiple strings, the condition is satisfied if one of the strings matches the HTTP request method. We recommend that you route GET and HEAD requests in the same way, because the response to a HEAD request may be cached.

(string)

SourceIpConfig -> (structure)

Information for a source IP condition. Specify only when `Field` is `source-ip` .

Values -> (list)

The source IP addresses, in CIDR format. You can use both IPv4 and IPv6 addresses. Wildcards are not supported.

If you specify multiple addresses, the condition is satisfied if the source IP address of the request matches one of the CIDR blocks. This condition is not satisfied by the addresses in the X-Forwarded-For header. To search for addresses in the X-Forwarded-For header, use  HttpHeaderConditionConfig .

The total number of values must be less than, or equal to five.

(string)

Actions -> (list)

The actions. Each rule must include exactly one of the following types of actions: `forward` , `redirect` , or `fixed-response` , and it must be the last action to be performed.

(structure)

Information about an action.

Each rule must include exactly one of the following types of actions: `forward` , `fixed-response` , or `redirect` , and it must be the last action to be performed.

Type -> (string)

The type of action.

TargetGroupArn -> (string)

The Amazon Resource Name (ARN) of the target group. Specify only when `Type` is `forward` and you want to route to a single target group. To route to one or more target groups, use `ForwardConfig` instead.

AuthenticateOidcConfig -> (structure)

[HTTPS listeners] Information about an identity provider that is compliant with OpenID Connect (OIDC). Specify only when `Type` is `authenticate-oidc` .

Issuer -> (string)

The OIDC issuer identifier of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

AuthorizationEndpoint -> (string)

The authorization endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

TokenEndpoint -> (string)

The token endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

UserInfoEndpoint -> (string)

The user info endpoint of the IdP. This must be a full URL, including the HTTPS protocol, the domain, and the path.

ClientId -> (string)

The OAuth 2.0 client identifier.

ClientSecret -> (string)

The OAuth 2.0 client secret. This parameter is required if you are creating a rule. If you are modifying a rule, you can omit this parameter if you set `UseExistingClientSecret` to true.

SessionCookieName -> (string)

The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope -> (string)

The set of user claims to be requested from the IdP. The default is `openid` .

To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout -> (long)

The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams -> (map)

The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

key -> (string)

value -> (string)

OnUnauthenticatedRequest -> (string)

The behavior if the user is not authenticated. The following are possible values:

- deny- Return an HTTP 401 Unauthorized error.
- allow- Allow the request to be forwarded to the target.
- authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.

UseExistingClientSecret -> (boolean)

Indicates whether to use the existing client secret when modifying a rule. If you are creating a rule, you can omit this parameter or set it to false.

AuthenticateCognitoConfig -> (structure)

[HTTPS listeners] Information for using Amazon Cognito to authenticate users. Specify only when `Type` is `authenticate-cognito` .

UserPoolArn -> (string)

The Amazon Resource Name (ARN) of the Amazon Cognito user pool.

UserPoolClientId -> (string)

The ID of the Amazon Cognito user pool client.

UserPoolDomain -> (string)

The domain prefix or fully-qualified domain name of the Amazon Cognito user pool.

SessionCookieName -> (string)

The name of the cookie used to maintain session information. The default is AWSELBAuthSessionCookie.

Scope -> (string)

The set of user claims to be requested from the IdP. The default is `openid` .

To verify which scope values your IdP supports and how to separate multiple values, see the documentation for your IdP.

SessionTimeout -> (long)

The maximum duration of the authentication session, in seconds. The default is 604800 seconds (7 days).

AuthenticationRequestExtraParams -> (map)

The query parameters (up to 10) to include in the redirect request to the authorization endpoint.

key -> (string)

value -> (string)

OnUnauthenticatedRequest -> (string)

The behavior if the user is not authenticated. The following are possible values:

- deny- Return an HTTP 401 Unauthorized error.
- allow- Allow the request to be forwarded to the target.
- authenticate- Redirect the request to the IdP authorization endpoint. This is the default value.

Order -> (integer)

The order for the action. This value is required for rules with multiple actions. The action with the lowest value for order is performed first.

RedirectConfig -> (structure)

[Application Load Balancer] Information for creating a redirect action. Specify only when `Type` is `redirect` .

Protocol -> (string)

The protocol. You can specify HTTP, HTTPS, or #{protocol}. You can redirect HTTP to HTTP, HTTP to HTTPS, and HTTPS to HTTPS. You canât redirect HTTPS to HTTP.

Port -> (string)

The port. You can specify a value from 1 to 65535 or #{port}.

Host -> (string)

The hostname. This component is not percent-encoded. The hostname can contain #{host}.

Path -> (string)

The absolute path, starting with the leading â/â. This component is not percent-encoded. The path can contain #{host}, #{path}, and #{port}.

Query -> (string)

The query parameters, URL-encoded when necessary, but not percent-encoded. Do not include the leading â?â, as it is automatically added. You can specify any of the reserved keywords.

StatusCode -> (string)

The HTTP redirect code. The redirect is either permanent (HTTP 301) or temporary (HTTP 302).

FixedResponseConfig -> (structure)

[Application Load Balancer] Information for creating an action that returns a custom HTTP response. Specify only when `Type` is `fixed-response` .

MessageBody -> (string)

The message.

StatusCode -> (string)

The HTTP response code (2XX, 4XX, or 5XX).

ContentType -> (string)

The content type.

Valid Values: text/plain | text/css | text/html | application/javascript | application/json

ForwardConfig -> (structure)

Information for creating an action that distributes requests among one or more target groups. For Network Load Balancers, you can specify a single target group. Specify only when `Type` is `forward` . If you specify both `ForwardConfig` and `TargetGroupArn` , you can specify only one target group using `ForwardConfig` and it must be the same target group specified in `TargetGroupArn` .

TargetGroups -> (list)

The target groups. For Network Load Balancers, you can specify a single target group.

(structure)

Information about how traffic will be distributed between multiple target groups in a forward rule.

TargetGroupArn -> (string)

The Amazon Resource Name (ARN) of the target group.

Weight -> (integer)

The weight. The range is 0 to 999.

TargetGroupStickinessConfig -> (structure)

The target group stickiness for the rule.

Enabled -> (boolean)

Indicates whether target group stickiness is enabled.

DurationSeconds -> (integer)

The time period, in seconds, during which requests from a client should be routed to the same target group. The range is 1-604800 seconds (7 days).

IsDefault -> (boolean)

Indicates whether this is the default rule.

NextMarker -> (string)

If there are additional results, this is the marker for the next set of results. Otherwise, this is null.