# create-rate-based-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rate-based-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/create-rate-based-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [waf](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/index.html#cli-aws-waf) ]

# create-rate-based-rule

## Description

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Creates a  RateBasedRule . The `RateBasedRule` contains a `RateLimit` , which specifies the maximum number of requests that AWS WAF allows from a specified IP address in a five-minute period. The `RateBasedRule` also contains the `IPSet` objects, `ByteMatchSet` objects, and other predicates that identify the requests that you want to count or block if these requests exceed the `RateLimit` .

If you add more than one predicate to a `RateBasedRule` , a request not only must exceed the `RateLimit` , but it also must match all the conditions to be counted or blocked. For example, suppose you add the following to a `RateBasedRule` :

- An `IPSet` that matches the IP address `192.0.2.44/32`
- A `ByteMatchSet` that matches `BadBot` in the `User-Agent` header

Further, you specify a `RateLimit` of 1,000.

You then add the `RateBasedRule` to a `WebACL` and specify that you want to block requests that meet the conditions in the rule. For a request to be blocked, it must come from the IP address 192.0.2.44 *and* the `User-Agent` header in the request must contain the value `BadBot` . Further, requests that match these two conditions must be received at a rate of more than 1,000 requests every five minutes. If both conditions are met and the rate is exceeded, AWS WAF blocks the requests. If the rate drops below 1,000 for a five-minute period, AWS WAF no longer blocks the requests.

As a second example, suppose you want to limit requests to a particular page on your site. To do this, you could add the following to a `RateBasedRule` :

- A `ByteMatchSet` with `FieldToMatch` of `URI`
- A `PositionalConstraint` of `STARTS_WITH`
- A `TargetString` of `login`

Further, you specify a `RateLimit` of 1,000.

By adding this `RateBasedRule` to a `WebACL` , you could limit requests to your login page without affecting the rest of your site.

To create and configure a `RateBasedRule` , perform the following steps:

- Create and update the predicates that you want to include in the rule. For more information, see  CreateByteMatchSet ,  CreateIPSet , and  CreateSqlInjectionMatchSet .
- Use  GetChangeToken to get the change token that you provide in the `ChangeToken` parameter of a `CreateRule` request.
- Submit a `CreateRateBasedRule` request.
- Use `GetChangeToken` to get the change token that you provide in the `ChangeToken` parameter of an  UpdateRule request.
- Submit an `UpdateRateBasedRule` request to specify the predicates that you want to include in the rule.
- Create and update a `WebACL` that contains the `RateBasedRule` . For more information, see  CreateWebACL .

For more information about how to use the AWS WAF API to allow or block HTTP requests, see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/waf-2015-08-24/CreateRateBasedRule)

## Synopsis

```
create-rate-based-rule
--name <value>
--metric-name <value>
--rate-key <value>
--rate-limit <value>
--change-token <value>
[--tags <value>]
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

`--name` (string)

A friendly name or description of the  RateBasedRule . You canât change the name of a `RateBasedRule` after you create it.

`--metric-name` (string)

A friendly name or description for the metrics for this `RateBasedRule` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It canât contain whitespace or metric names reserved for AWS WAF, including âAllâ and âDefault_Action.â You canât change the name of the metric after you create the `RateBasedRule` .

`--rate-key` (string)

The field that AWS WAF uses to determine if requests are likely arriving from a single source and thus subject to rate monitoring. The only valid value for `RateKey` is `IP` . `IP` indicates that requests that arrive from the same IP address are subject to the `RateLimit` that is specified in the `RateBasedRule` .

Possible values:

- `IP`

`--rate-limit` (long)

The maximum number of requests, which have an identical value in the field that is specified by `RateKey` , allowed in a five-minute period. If the number of requests exceeds the `RateLimit` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.

`--change-token` (string)

The `ChangeToken` that you used to submit the `CreateRateBasedRule` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .

`--tags` (list)

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

A tag associated with an AWS resource. Tags are key:value pairs that you can use to categorize and manage your resources, for purposes like billing. For example, you might set the tag key to âcustomerâ and the value to the customer name or ID. You can specify one or more tags to add to each AWS resource, up to 50 tags for a resource.

Tagging is only available through the API, SDKs, and CLI. You canât manage or view tags through the AWS WAF Classic console. You can tag the AWS resources that you manage through AWS WAF Classic: web ACLs, rule groups, and rules.

Key -> (string)

Value -> (string)

Shorthand Syntax:

```
Key=string,Value=string ...
```

JSON Syntax:

```
[
  {
    "Key": "string",
    "Value": "string"
  }
  ...
]
```

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

Rule -> (structure)

The  RateBasedRule that is returned in the `CreateRateBasedRule` response.

RuleId -> (string)

A unique identifier for a `RateBasedRule` . You use `RuleId` to get more information about a `RateBasedRule` (see  GetRateBasedRule ), update a `RateBasedRule` (see  UpdateRateBasedRule ), insert a `RateBasedRule` into a `WebACL` or delete one from a `WebACL` (see  UpdateWebACL ), or delete a `RateBasedRule` from AWS WAF (see  DeleteRateBasedRule ).

Name -> (string)

A friendly name or description for a `RateBasedRule` . You canât change the name of a `RateBasedRule` after you create it.

MetricName -> (string)

A friendly name or description for the metrics for a `RateBasedRule` . The name can contain only alphanumeric characters (A-Z, a-z, 0-9), with maximum length 128 and minimum length one. It canât contain whitespace or metric names reserved for AWS WAF, including âAllâ and âDefault_Action.â You canât change the name of the metric after you create the `RateBasedRule` .

MatchPredicates -> (list)

The `Predicates` object contains one `Predicate` element for each  ByteMatchSet ,  IPSet , or  SqlInjectionMatchSet object that you want to include in a `RateBasedRule` .

(structure)

### Note

This is **AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.

**For the latest version of AWS WAF** , use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) . With the latest version, AWS WAF has a single set of endpoints for regional and global use.

Specifies the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , and  SizeConstraintSet objects that you want to add to a `Rule` and, for each object, indicates whether you want to negate the settings, for example, requests that do NOT originate from the IP address 192.0.2.44.

Negated -> (boolean)

Set `Negated` to `False` if you want AWS WAF to allow, block, or count requests based on the settings in the specified  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an `IPSet` includes the IP address `192.0.2.44` , AWS WAF will allow or block requests based on that IP address.

Set `Negated` to `True` if you want AWS WAF to allow or block a request based on the negation of the settings in the  ByteMatchSet ,  IPSet ,  SqlInjectionMatchSet ,  XssMatchSet ,  RegexMatchSet ,  GeoMatchSet , or  SizeConstraintSet . For example, if an `IPSet` includes the IP address `192.0.2.44` , AWS WAF will allow, block, or count requests based on all IP addresses *except* `192.0.2.44` .

Type -> (string)

The type of predicate in a `Rule` , such as `ByteMatch` or `IPSet` .

DataId -> (string)

A unique identifier for a predicate in a `Rule` , such as `ByteMatchSetId` or `IPSetId` . The ID is returned by the corresponding `Create` or `List` command.

RateKey -> (string)

The field that AWS WAF uses to determine if requests are likely arriving from single source and thus subject to rate monitoring. The only valid value for `RateKey` is `IP` . `IP` indicates that requests arriving from the same IP address are subject to the `RateLimit` that is specified in the `RateBasedRule` .

RateLimit -> (long)

The maximum number of requests, which have an identical value in the field specified by the `RateKey` , allowed in a five-minute period. If the number of requests exceeds the `RateLimit` and the other predicates specified in the rule are also met, AWS WAF triggers the action that is specified for this rule.

ChangeToken -> (string)

The `ChangeToken` that you used to submit the `CreateRateBasedRule` request. You can also use this value to query the status of the request. For more information, see  GetChangeTokenStatus .