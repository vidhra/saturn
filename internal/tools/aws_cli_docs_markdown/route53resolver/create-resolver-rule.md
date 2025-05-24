# create-resolver-ruleÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-rule.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/create-resolver-rule.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/index.html#cli-aws-route53resolver) ]

# create-resolver-rule

## Description

For DNS queries that originate in your VPCs, specifies which Resolver endpoint the queries pass through, one domain name that you want to forward to your network, and the IP addresses of the DNS resolvers in your network.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53resolver-2018-04-01/CreateResolverRule)

## Synopsis

```
create-resolver-rule
--creator-request-id <value>
[--name <value>]
--rule-type <value>
[--domain-name <value>]
[--target-ips <value>]
[--resolver-endpoint-id <value>]
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

`--creator-request-id` (string)

A unique string that identifies the request and that allows failed requests to be retried without the risk of running the operation twice. `CreatorRequestId` can be any unique string, for example, a date/time stamp.

`--name` (string)

A friendly name that lets you easily find a rule in the Resolver dashboard in the Route 53 console.

`--rule-type` (string)

When you want to forward DNS queries for specified domain name to resolvers on your network, specify `FORWARD` .

When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify `SYSTEM` .

For example, to forward DNS queries for example.com to resolvers on your network, you create a rule and specify `FORWARD` for `RuleType` . To then have Resolver process queries for apex.example.com, you create a rule and specify `SYSTEM` for `RuleType` .

Currently, only Resolver can create rules that have a value of `RECURSIVE` for `RuleType` .

Possible values:

- `FORWARD`
- `SYSTEM`
- `RECURSIVE`

`--domain-name` (string)

DNS queries for this domain name are forwarded to the IP addresses that you specify in `TargetIps` . If a query matches multiple Resolver rules (example.com and www.example.com), outbound DNS queries are routed using the Resolver rule that contains the most specific domain name (www.example.com).

`--target-ips` (list)

The IPs that you want Resolver to forward DNS queries to. You can specify either Ipv4 or Ipv6 addresses but not both in the same rule. Separate IP addresses with a space.

`TargetIps` is available only when the value of `Rule type` is `FORWARD` .

(structure)

In a [CreateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html) request, an array of the IPs that you want to forward DNS queries to.

Ip -> (string)

One IPv4 address that you want to forward DNS queries to.

Port -> (integer)

The port at `Ip` that you want to forward DNS queries to.

Ipv6 -> (string)

One IPv6 address that you want to forward DNS queries to.

Protocol -> (string)

The protocols for the target address. The protocol you choose needs to be supported by the outbound endpoint of the Resolver rule.

ServerNameIndication -> (string)

The Server Name Indication of the DoH server that you want to forward queries to. This is only used if the Protocol of the `TargetAddress` is `DoH` .

Shorthand Syntax:

```
Ip=string,Port=integer,Ipv6=string,Protocol=string,ServerNameIndication=string ...
```

JSON Syntax:

```
[
  {
    "Ip": "string",
    "Port": integer,
    "Ipv6": "string",
    "Protocol": "DoH"|"Do53"|"DoH-FIPS",
    "ServerNameIndication": "string"
  }
  ...
]
```

`--resolver-endpoint-id` (string)

The ID of the outbound Resolver endpoint that you want to use to route DNS queries to the IP addresses that you specify in `TargetIps` .

`--tags` (list)

A list of the tag keys and values that you want to associate with the endpoint.

(structure)

One tag that you want to add to the specified resource. A tag consists of a `Key` (a name for the tag) and a `Value` .

Key -> (string)

The name for the tag. For example, if you want to associate Resolver resources with the account IDs of your customers for billing purposes, the value of `Key` might be `account-id` .

Value -> (string)

The value for the tag. For example, if `Key` is `account-id` , then `Value` might be the ID of the customer account that youâre creating the resource for.

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

## Examples

### Note

To use the following examples, you must have the AWS CLI installed and configured. See the [Getting started guide](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) in the *AWS CLI User Guide* for more information.

Unless otherwise stated, all examples have unix-like quotation rules. These examples will need to be adapted to your terminalâs quoting rules. See [Using quotation marks with strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the *AWS CLI User Guide* .

**To create a Resolver rule**

The following `create-resolver-rule` example creates a Resolver forwarding rule. The rule uses the outbound endpoint rslvr-out-d5e5920e37example to forward DNS queries for `example.com` to the IP addresses 10.24.8.75 and 10.24.8.156.

```
aws route53resolver create-resolver-rule \
    --creator-request-id 2020-01-02-18:47 \
    --domain-name example.com \
    --name my-rule \
    --resolver-endpoint-id rslvr-out-d5e5920e37example \
    --rule-type FORWARD \
    --target-ips "Ip=10.24.8.75" "Ip=10.24.8.156"
```

Output:

```
{
    "ResolverRule": {
        "Status": "COMPLETE",
        "RuleType": "FORWARD",
        "ResolverEndpointId": "rslvr-out-d5e5920e37example",
        "Name": "my-rule",
        "DomainName": "example.com.",
        "CreationTime": "2022-05-10T21:35:30.923187Z",
        "TargetIps": [
            {
                "Ip": "10.24.8.75",
                "Port": 53
            },
            {
                "Ip": "10.24.8.156",
                "Port": 53
            }
        ],
        "CreatorRequestId": "2022-05-10-16:33",
        "ModificationTime": "2022-05-10T21:35:30.923187Z",
        "ShareStatus": "NOT_SHARED",
        "Arn": "arn:aws:route53resolver:us-east-1:111117012054:resolver-rule/rslvr-rr-b1e0b905e93611111",
        "OwnerId": "111111111111",
        "Id": "rslvr-rr-rslvr-rr-b1e0b905e93611111",
        "StatusMessage": "[Trace id: 1-22222222-3e56afcc71a3724664f22e24] Successfully created Resolver Rule."
    }
}
```

## Output

ResolverRule -> (structure)

Information about the `CreateResolverRule` request, including the status of the request.

Id -> (string)

The ID that Resolver assigned to the Resolver rule when you created it.

CreatorRequestId -> (string)

A unique string that you specified when you created the Resolver rule. `CreatorRequestId` identifies the request and allows failed requests to be retried without the risk of running the operation twice.

Arn -> (string)

The ARN (Amazon Resource Name) for the Resolver rule specified by `Id` .

DomainName -> (string)

DNS queries for this domain name are forwarded to the IP addresses that are specified in `TargetIps` . If a query matches multiple Resolver rules (example.com and www.example.com), the query is routed using the Resolver rule that contains the most specific domain name (www.example.com).

Status -> (string)

A code that specifies the current status of the Resolver rule.

StatusMessage -> (string)

A detailed description of the status of a Resolver rule.

RuleType -> (string)

When you want to forward DNS queries for specified domain name to resolvers on your network, specify `FORWARD` .

When you have a forwarding rule to forward DNS queries for a domain to your network and you want Resolver to process queries for a subdomain of that domain, specify `SYSTEM` .

For example, to forward DNS queries for example.com to resolvers on your network, you create a rule and specify `FORWARD` for `RuleType` . To then have Resolver process queries for apex.example.com, you create a rule and specify `SYSTEM` for `RuleType` .

Currently, only Resolver can create rules that have a value of `RECURSIVE` for `RuleType` .

Name -> (string)

The name for the Resolver rule, which you specified when you created the Resolver rule.

TargetIps -> (list)

An array that contains the IP addresses and ports that an outbound endpoint forwards DNS queries to. Typically, these are the IP addresses of DNS resolvers on your network.

(structure)

In a [CreateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html) request, an array of the IPs that you want to forward DNS queries to.

Ip -> (string)

One IPv4 address that you want to forward DNS queries to.

Port -> (integer)

The port at `Ip` that you want to forward DNS queries to.

Ipv6 -> (string)

One IPv6 address that you want to forward DNS queries to.

Protocol -> (string)

The protocols for the target address. The protocol you choose needs to be supported by the outbound endpoint of the Resolver rule.

ServerNameIndication -> (string)

The Server Name Indication of the DoH server that you want to forward queries to. This is only used if the Protocol of the `TargetAddress` is `DoH` .

ResolverEndpointId -> (string)

The ID of the endpoint that the rule is associated with.

OwnerId -> (string)

When a rule is shared with another Amazon Web Services account, the account ID of the account that the rule is shared with.

ShareStatus -> (string)

Whether the rule is shared and, if so, whether the current account is sharing the rule with another account, or another account is sharing the rule with the current account.

CreationTime -> (string)

The date and time that the Resolver rule was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime -> (string)

The date and time that the Resolver rule was last updated, in Unix time format and Coordinated Universal Time (UTC).