# get-sampled-requestsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-sampled-requests.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/get-sampled-requests.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [waf-regional](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf-regional/index.html#cli-aws-waf-regional) ]

# get-sampled-requests

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Gets detailed information about a specified number of requestsâa sampleâthat AWS WAF randomly selects from among the first 5,000 requests that your AWS resource received during a time range that you choose. You can specify a sample size of up to 500 requests, and you can specify any time range in the previous three hours.

`GetSampledRequests` returns a time range, which is usually the time range that you specified. However, if your resource (such as a CloudFront distribution) received 5,000 requests before the specified time range elapsed, `GetSampledRequests` returns an updated time range. This new time range indicates the actual period during which AWS WAF selected the requests in the sample.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/waf-regional-2016-11-28/GetSampledRequests)

## Synopsis

```
get-sampled-requests
--web-acl-id <value>
--rule-id <value>
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

`--web-acl-id` (string)

The `WebACLId` of the `WebACL` for which you want `GetSampledRequests` to return a sample of requests.

`--rule-id` (string)

`RuleId` is one of three values:

- The `RuleId` of the `Rule` or the `RuleGroupId` of the `RuleGroup` for which you want `GetSampledRequests` to return a sample of requests.
- `Default_Action` , which causes `GetSampledRequests` to return a sample of the requests that didnât match any of the rules in the specified `WebACL` .

`--time-window` (structure)

The start date and time and the end date and time of the range for which you want `GetSampledRequests` to return a sample of requests. You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z` . For example, `"2016-09-27T14:50Z"` . You can specify any time range in the previous three hours.

StartTime -> (timestamp)

The beginning of the time range from which you want `GetSampledRequests` to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z` . For example, `"2016-09-27T14:50Z"` . You can specify any time range in the previous three hours.

EndTime -> (timestamp)

The end of the time range from which you want `GetSampledRequests` to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z` . For example, `"2016-09-27T14:50Z"` . You can specify any time range in the previous three hours.

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

The number of requests that you want AWS WAF to return from among the first 5,000 requests that your AWS resource received during the time range. If your resource received fewer requests than the value of `MaxItems` , `GetSampledRequests` returns information about all of them.

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

SampledRequests -> (list)

A complex type that contains detailed information about each of the requests in the sample.

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The response from a  GetSampledRequests request includes a `SampledHTTPRequests` complex type that appears as `SampledRequests` in the response syntax. `SampledHTTPRequests` contains one `SampledHTTPRequest` object for each web request that is returned by `GetSampledRequests` .

Request -> (structure)

A complex type that contains detailed information about the request.

ClientIP -> (string)

The IP address that the request originated from. If the `WebACL` is associated with a CloudFront distribution, this is the value of one of the following fields in CloudFront access logs:

- `c-ip` , if the viewer did not use an HTTP proxy or a load balancer to send the request
- `x-forwarded-for` , if the viewer did use an HTTP proxy or a load balancer to send the request

Country -> (string)

The two-letter country code for the country that the request originated from. For a current list of country codes, see the Wikipedia entry [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) .

URI -> (string)

The part of a web request that identifies the resource, for example, `/images/daily-ad.jpg` .

Method -> (string)

The HTTP method specified in the sampled web request. CloudFront supports the following methods: `DELETE` , `GET` , `HEAD` , `OPTIONS` , `PATCH` , `POST` , and `PUT` .

HTTPVersion -> (string)

The HTTP version specified in the sampled web request, for example, `HTTP/1.1` .

Headers -> (list)

A complex type that contains two values for each header in the sampled web request: the name of the header and the value of the header.

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

The response from a  GetSampledRequests request includes an `HTTPHeader` complex type that appears as `Headers` in the response syntax. `HTTPHeader` contains the names and values of all of the headers that appear in one of the web requests that were returned by `GetSampledRequests` .

Name -> (string)

The name of one of the headers in the sampled web request.

Value -> (string)

The value of one of the headers in the sampled web request.

Weight -> (long)

A value that indicates how one result in the response relates proportionally to other results in the response. A result that has a weight of `2` represents roughly twice as many CloudFront web requests as a result that has a weight of `1` .

Timestamp -> (timestamp)

The time at which AWS WAF received the request from your AWS resource, in Unix time format (in seconds).

Action -> (string)

The action for the `Rule` that the request matched: `ALLOW` , `BLOCK` , or `COUNT` .

RuleWithinRuleGroup -> (string)

This value is returned if the `GetSampledRequests` request specifies the ID of a `RuleGroup` rather than the ID of an individual rule. `RuleWithinRuleGroup` is the rule within the specified `RuleGroup` that matched the request listed in the response.

PopulationSize -> (long)

The total number of requests from which `GetSampledRequests` got a sample of `MaxItems` requests. If `PopulationSize` is less than `MaxItems` , the sample includes every request that your AWS resource received during the specified time range.

TimeWindow -> (structure)

Usually, `TimeWindow` is the time range that you specified in the `GetSampledRequests` request. However, if your AWS resource received more than 5,000 requests during the time range that you specified in the request, `GetSampledRequests` returns the time range for the first 5,000 requests. Times are in Coordinated Universal Time (UTC) format.

StartTime -> (timestamp)

The beginning of the time range from which you want `GetSampledRequests` to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z` . For example, `"2016-09-27T14:50Z"` . You can specify any time range in the previous three hours.

EndTime -> (timestamp)

The end of the time range from which you want `GetSampledRequests` to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z` . For example, `"2016-09-27T14:50Z"` . You can specify any time range in the previous three hours.