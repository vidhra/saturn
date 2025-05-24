# get-sampled-requestsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-sampled-requests.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/get-sampled-requests.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [wafv2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/wafv2/index.html#cli-aws-wafv2) ]

# get-sampled-requests

## Description

Gets detailed information about a specified number of requestsâa sampleâthat WAF randomly selects from among the first 5,000 requests that your Amazon Web Services resource received during a time range that you choose. You can specify a sample size of up to 500 requests, and you can specify any time range in the previous three hours.

`GetSampledRequests` returns a time range, which is usually the time range that you specified. However, if your resource (such as a CloudFront distribution) received 5,000 requests before the specified time range elapsed, `GetSampledRequests` returns an updated time range. This new time range indicates the actual period during which WAF selected the requests in the sample.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/wafv2-2019-07-29/GetSampledRequests)

## Synopsis

```
get-sampled-requests
--web-acl-arn <value>
--rule-metric-name <value>
--scope <value>
--time-window <value>
--max-items <value>
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

`--web-acl-arn` (string)

The Amazon resource name (ARN) of the `WebACL` for which you want a sample of requests.

`--rule-metric-name` (string)

The metric name assigned to the `Rule` or `RuleGroup` dimension for which you want a sample of requests.

`--scope` (string)

Specifies whether this is for a global resource type, such as a Amazon CloudFront distribution. For an Amplify application, use `CLOUDFRONT` .

To work with CloudFront, you must also specify the Region US East (N. Virginia) as follows:

- CLI - Specify the Region when you use the CloudFront scope: `--scope=CLOUDFRONT --region=us-east-1` .
- API and SDKs - For all calls, use the Region endpoint us-east-1.

Possible values:

- `CLOUDFRONT`
- `REGIONAL`

`--time-window` (structure)

The start date and time and the end date and time of the range for which you want `GetSampledRequests` to return a sample of requests. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z` . For example, `"2016-09-27T14:50Z"` . You can specify any time range in the previous three hours. If you specify a start time thatâs earlier than three hours ago, WAF sets it to three hours ago.

StartTime -> (timestamp)

The beginning of the time range from which you want `GetSampledRequests` to return a sample of the requests that your Amazon Web Services resource received. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z` . For example, `"2016-09-27T14:50Z"` . You can specify any time range in the previous three hours.

EndTime -> (timestamp)

The end of the time range from which you want `GetSampledRequests` to return a sample of the requests that your Amazon Web Services resource received. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z` . For example, `"2016-09-27T14:50Z"` . You can specify any time range in the previous three hours.

Shorthand Syntax:

```
StartTime=timestamp,EndTime=timestamp
```

JSON Syntax:

```
{
  "StartTime": timestamp,
  "EndTime": timestamp
}
```

`--max-items` (long)

The number of requests that you want WAF to return from among the first 5,000 requests that your Amazon Web Services resource received during the time range. If your resource received fewer requests than the value of `MaxItems` , `GetSampledRequests` returns information about all of them.

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

**To retrieve a sample of web requests for a web ACL**

The following `get-sampled-requests` retrieves the sampled web requests for the specified web ACL, rule metric, and time frame.

```
aws wafv2 get-sampled-requests \
    --web-acl-arn arn:aws:wafv2:us-west-2:123456789012:regional/webacl/test-cli/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111 \
    --rule-metric-name AWS-AWSManagedRulesSQLiRuleSet \
    --scope=REGIONAL \
    --time-window StartTime=2020-02-12T20:00Z,EndTime=2020-02-12T21:10Z \
    --max-items 100
```

Output:

```
{
    "TimeWindow": {
    "EndTime": 1581541800.0,
    "StartTime": 1581537600.0
    },
    "SampledRequests": [
        {
            "Action": "BLOCK",
            "Timestamp": 1581541799.564,
            "RuleNameWithinRuleGroup": "AWS#AWSManagedRulesSQLiRuleSet#SQLi_BODY",
            "Request": {
                "Country": "US",
                "URI": "/",
                "Headers": [
                    {
                        "Name": "Host",
                        "Value": "alb-test-1EXAMPLE1.us-east-1.elb.amazonaws.com"
                    },
                    {
                        "Name": "Content-Length",
                        "Value": "7456"
                    },
                    {
                        "Name": "User-Agent",
                        "Value": "curl/7.53.1"
                    },
                    {
                        "Name": "Accept",
                        "Value": "/"
                    },
                    {
                        "Name": "Content-Type",
                        "Value": "application/x-www-form-urlencoded"
                    }
                ],
                "ClientIP": "198.51.100.08",
                "Method": "POST",
                "HTTPVersion": "HTTP/1.1"
            },
            "Weight": 1
        },
        {
            "Action": "BLOCK",
            "Timestamp": 1581541799.988,
            "RuleNameWithinRuleGroup": "AWS#AWSManagedRulesSQLiRuleSet#SQLi_BODY",
            "Request": {
                "Country": "US",
                "URI": "/",
                "Headers": [
                    {
                        "Name": "Host",
                        "Value": "alb-test-1EXAMPLE1.us-east-1.elb.amazonaws.com"
                    },
                    {
                        "Name": "Content-Length",
                        "Value": "7456"
                    },
                    {
                        "Name": "User-Agent",
                        "Value": "curl/7.53.1"
                    },
                    {
                        "Name": "Accept",
                        "Value": "/"
                    },
                    {
                        "Name": "Content-Type",
                        "Value": "application/x-www-form-urlencoded"
                    }
                ],
                "ClientIP": "198.51.100.08",
                "Method": "POST",
                "HTTPVersion": "HTTP/1.1"
            },
            "Weight": 3
        },
        {
            "Action": "BLOCK",
            "Timestamp": 1581541799.846,
            "RuleNameWithinRuleGroup": "AWS#AWSManagedRulesSQLiRuleSet#SQLi_BODY",
            "Request": {
                "Country": "US",
                "URI": "/",
                "Headers": [
                    {
                        "Name": "Host",
                        "Value": "alb-test-1EXAMPLE1.us-east-1.elb.amazonaws.com"
                    },
                    {
                        "Name": "Content-Length",
                        "Value": "7456"
                    },
                    {
                        "Name": "User-Agent",
                        "Value": "curl/7.53.1"
                    },
                    {
                        "Name": "Accept",
                        "Value": "/"
                    },
                    {
                        "Name": "Content-Type",
                        "Value": "application/x-www-form-urlencoded"
                    }
                ],
                "ClientIP": "198.51.100.08",
                "Method": "POST",
                "HTTPVersion": "HTTP/1.1"
            },
            "Weight": 1
        },
        {
            "Action": "BLOCK",
            "Timestamp": 1581541799.4,
            "RuleNameWithinRuleGroup": "AWS#AWSManagedRulesSQLiRuleSet#SQLi_BODY",
            "Request": {
                "Country": "US",
                "URI": "/",
                "Headers": [
                    {
                        "Name": "Host",
                        "Value": "alb-test-1EXAMPLE1.us-east-1.elb.amazonaws.com"
                    },
                    {
                        "Name": "Content-Length",
                        "Value": "7456"
                    },
                    {
                        "Name": "User-Agent",
                        "Value": "curl/7.53.1"
                    },
                    {
                        "Name": "Accept",
                        "Value": "/"
                    },
                    {
                        "Name": "Content-Type",
                        "Value": "application/x-www-form-urlencoded"
                    }
                ],
                "ClientIP": "198.51.100.08",
                "Method": "POST",
                "HTTPVersion": "HTTP/1.1"
            },
            "Weight": 1
        }
    ],
    "PopulationSize": 4
}
```

For more information, see [Viewing a Sample of Web Requests](https://docs.aws.amazon.com/waf/latest/developerguide/web-acl-testing.html#web-acl-testing-view-sample) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.

## Output

SampledRequests -> (list)

A complex type that contains detailed information about each of the requests in the sample.

(structure)

Represents a single sampled web request. The response from  GetSampledRequests includes a `SampledHTTPRequests` complex type that appears as `SampledRequests` in the response syntax. `SampledHTTPRequests` contains an array of `SampledHTTPRequest` objects.

Request -> (structure)

A complex type that contains detailed information about the request.

ClientIP -> (string)

The IP address that the request originated from. If the web ACL is associated with a CloudFront distribution, this is the value of one of the following fields in CloudFront access logs:

- `c-ip` , if the viewer did not use an HTTP proxy or a load balancer to send the request
- `x-forwarded-for` , if the viewer did use an HTTP proxy or a load balancer to send the request

Country -> (string)

The two-letter country code for the country that the request originated from. For a current list of country codes, see the Wikipedia entry [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) .

URI -> (string)

The URI path of the request, which identifies the resource, for example, `/images/daily-ad.jpg` .

Method -> (string)

The HTTP method specified in the sampled web request.

HTTPVersion -> (string)

The HTTP version specified in the sampled web request, for example, `HTTP/1.1` .

Headers -> (list)

A complex type that contains the name and value for each header in the sampled web request.

(structure)

Part of the response from  GetSampledRequests . This is a complex type that appears as `Headers` in the response syntax. `HTTPHeader` contains the names and values of all of the headers that appear in one of the web requests.

Name -> (string)

The name of the HTTP header.

Value -> (string)

The value of the HTTP header.

Weight -> (long)

A value that indicates how one result in the response relates proportionally to other results in the response. For example, a result that has a weight of `2` represents roughly twice as many web requests as a result that has a weight of `1` .

Timestamp -> (timestamp)

The time at which WAF received the request from your Amazon Web Services resource, in Unix time format (in seconds).

Action -> (string)

The action that WAF applied to the request.

RuleNameWithinRuleGroup -> (string)

The name of the `Rule` that the request matched. For managed rule groups, the format for this name is `<vendor name>#<managed rule group name>#<rule name>` . For your own rule groups, the format for this name is `<rule group name>#<rule name>` . If the rule is not in a rule group, this field is absent.

RequestHeadersInserted -> (list)

Custom request headers inserted by WAF into the request, according to the custom request configuration for the matching rule action.

(structure)

Part of the response from  GetSampledRequests . This is a complex type that appears as `Headers` in the response syntax. `HTTPHeader` contains the names and values of all of the headers that appear in one of the web requests.

Name -> (string)

The name of the HTTP header.

Value -> (string)

The value of the HTTP header.

ResponseCodeSent -> (integer)

The response code that was sent for the request.

Labels -> (list)

Labels applied to the web request by matching rules. WAF applies fully qualified labels to matching web requests. A fully qualified label is the concatenation of a label namespace and a rule label. The ruleâs rule group or web ACL defines the label namespace.

For example, `awswaf:111122223333:myRuleGroup:testRules:testNS1:testNS2:labelNameA` or `awswaf:managed:aws:managed-rule-set:header:encoding:utf8` .

(structure)

A single label container. This is used as an element of a label array in multiple contexts, for example, in `RuleLabels` inside a  Rule and in `Labels` inside a  SampledHTTPRequest .

Name -> (string)

The label string.

CaptchaResponse -> (structure)

The `CAPTCHA` response for the request.

ResponseCode -> (integer)

The HTTP response code indicating the status of the `CAPTCHA` token in the web request. If the token is missing, invalid, or expired, this code is `405 Method Not Allowed` .

SolveTimestamp -> (long)

The time that the `CAPTCHA` was last solved for the supplied token.

FailureReason -> (string)

The reason for failure, populated when the evaluation of the token fails.

ChallengeResponse -> (structure)

The `Challenge` response for the request.

ResponseCode -> (integer)

The HTTP response code indicating the status of the challenge token in the web request. If the token is missing, invalid, or expired, this code is `202 Request Accepted` .

SolveTimestamp -> (long)

The time that the challenge was last solved for the supplied token.

FailureReason -> (string)

The reason for failure, populated when the evaluation of the token fails.

OverriddenAction -> (string)

Used only for rule group rules that have a rule action override in place in the web ACL. This is the action that the rule group rule is configured for, and not the action that was applied to the request. The action that WAF applied is the `Action` value.

PopulationSize -> (long)

The total number of requests from which `GetSampledRequests` got a sample of `MaxItems` requests. If `PopulationSize` is less than `MaxItems` , the sample includes every request that your Amazon Web Services resource received during the specified time range.

TimeWindow -> (structure)

Usually, `TimeWindow` is the time range that you specified in the `GetSampledRequests` request. However, if your Amazon Web Services resource received more than 5,000 requests during the time range that you specified in the request, `GetSampledRequests` returns the time range for the first 5,000 requests. Times are in Coordinated Universal Time (UTC) format.

StartTime -> (timestamp)

The beginning of the time range from which you want `GetSampledRequests` to return a sample of the requests that your Amazon Web Services resource received. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z` . For example, `"2016-09-27T14:50Z"` . You can specify any time range in the previous three hours.

EndTime -> (timestamp)

The end of the time range from which you want `GetSampledRequests` to return a sample of the requests that your Amazon Web Services resource received. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z` . For example, `"2016-09-27T14:50Z"` . You can specify any time range in the previous three hours.