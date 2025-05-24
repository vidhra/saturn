# list-resolver-rulesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rules.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-rules.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/index.html#cli-aws-route53resolver) ]

# list-resolver-rules

## Description

Lists the Resolver rules that were created using the current Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53resolver-2018-04-01/ListResolverRules)

`list-resolver-rules` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ResolverRules`

## Synopsis

```
list-resolver-rules
[--filters <value>]
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
[--page-size <value>]
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

`--filters` (list)

An optional specification to return a subset of Resolver rules, such as all Resolver rules that are associated with the same Resolver endpoint.

### Note

If you submit a second or subsequent `ListResolverRules` request and specify the `NextToken` parameter, you must use the same values for `Filters` , if any, as in the previous request.

(structure)

For Resolver list operations ([ListResolverEndpoints](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverEndpoints.html) , [ListResolverRules](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html) , [ListResolverRuleAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html) , [ListResolverQueryLogConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigs.html) , [ListResolverQueryLogConfigAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigAssociations.html) ), and [ListResolverDnssecConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverDnssecConfigs.html) ), an optional specification to return a subset of objects.

To filter objects, such as Resolver endpoints or Resolver rules, you specify `Name` and `Values` . For example, to list only inbound Resolver endpoints, specify `Direction` for `Name` and specify `INBOUND` for `Values` .

Name -> (string)

The name of the parameter that you want to use to filter objects.

The valid values for `Name` depend on the action that youâre including the filter in, [ListResolverEndpoints](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverEndpoints.html) , [ListResolverRules](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html) , [ListResolverRuleAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRuleAssociations.html) , [ListResolverQueryLogConfigs](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigs.html) , or [ListResolverQueryLogConfigAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigAssociations.html) .

### Note

In early versions of Resolver, values for `Name` were listed as uppercase, with underscore (_) delimiters. For example, `CreatorRequestId` was originally listed as `CREATOR_REQUEST_ID` . Uppercase values for `Name` are still supported.

**ListResolverEndpoints**

Valid values for `Name` include the following:

- `CreatorRequestId` : The value that you specified when you created the Resolver endpoint.
- `Direction` : Whether you want to return inbound or outbound Resolver endpoints. If you specify `DIRECTION` for `Name` , specify `INBOUND` or `OUTBOUND` for `Values` .
- `HostVPCId` : The ID of the VPC that inbound DNS queries pass through on the way from your network to your VPCs in a region, or the VPC that outbound queries pass through on the way from your VPCs to your network. In a [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html) request, `SubnetId` indirectly identifies the VPC. In a [GetResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html) request, the VPC ID for a Resolver endpoint is returned in the `HostVPCId` element.
- `IpAddressCount` : The number of IP addresses that you have associated with the Resolver endpoint.
- `Name` : The name of the Resolver endpoint.
- `SecurityGroupIds` : The IDs of the VPC security groups that you specified when you created the Resolver endpoint.
- `Status` : The status of the Resolver endpoint. If you specify `Status` for `Name` , specify one of the following status codes for `Values` : `CREATING` , `OPERATIONAL` , `UPDATING` , `AUTO_RECOVERING` , `ACTION_NEEDED` , or `DELETING` . For more information, see `Status` in [ResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverEndpoint.html) .

**ListResolverRules**

Valid values for `Name` include the following:

- `CreatorRequestId` : The value that you specified when you created the Resolver rule.
- `DomainName` : The domain name for which Resolver is forwarding DNS queries to your network. In the value that you specify for `Values` , include a trailing dot (.) after the domain name. For example, if the domain name is example.com, specify the following value. Note the â.â after `com` :  `example.com.`
- `Name` : The name of the Resolver rule.
- `ResolverEndpointId` : The ID of the Resolver endpoint that the Resolver rule is associated with.

### Note

You can filter on the Resolver endpoint only for rules that have a value of `FORWARD` for `RuleType` .

- `Status` : The status of the Resolver rule. If you specify `Status` for `Name` , specify one of the following status codes for `Values` : `COMPLETE` , `DELETING` , `UPDATING` , or `FAILED` .
- `Type` : The type of the Resolver rule. If you specify `TYPE` for `Name` , specify `FORWARD` or `SYSTEM` for `Values` .

**ListResolverRuleAssociations**

Valid values for `Name` include the following:

- `Name` : The name of the Resolver rule association.
- `ResolverRuleId` : The ID of the Resolver rule that is associated with one or more VPCs.
- `Status` : The status of the Resolver rule association. If you specify `Status` for `Name` , specify one of the following status codes for `Values` : `CREATING` , `COMPLETE` , `DELETING` , or `FAILED` .
- `VPCId` : The ID of the VPC that the Resolver rule is associated with.

**ListResolverQueryLogConfigs**

Valid values for `Name` include the following:

- `Arn` : The ARN for the query logging configuration.
- `AssociationCount` : The number of VPCs that are associated with the query logging configuration.
- `CreationTime` : The date and time that the query logging configuration was created, in Unix time format and Coordinated Universal Time (UTC).
- `CreatorRequestId` : A unique string that identifies the request that created the query logging configuration.
- `Destination` : The Amazon Web Services service that you want to forward query logs to. Valid values include the following:
- `S3`
- `CloudWatchLogs`
- `KinesisFirehose`
- `DestinationArn` : The ARN of the location that Resolver is sending query logs to. This value can be the ARN for an S3 bucket, a CloudWatch Logs log group, or a Kinesis Data Firehose delivery stream.
- `Id` : The ID of the query logging configuration
- `Name` : The name of the query logging configuration
- `OwnerId` : The Amazon Web Services account ID for the account that created the query logging configuration.
- `ShareStatus` : An indication of whether the query logging configuration is shared with other Amazon Web Services accounts, or was shared with the current account by another Amazon Web Services account. Valid values include: `NOT_SHARED` , `SHARED_WITH_ME` , or `SHARED_BY_ME` .
- `Status` : The status of the query logging configuration. If you specify `Status` for `Name` , specify the applicable status code for `Values` : `CREATING` , `CREATED` , `DELETING` , or `FAILED` . For more information, see [Status](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverQueryLogConfig.html#Route53Resolver-Type-route53resolver_ResolverQueryLogConfig-Status) .

**ListResolverQueryLogConfigAssociations**

Valid values for `Name` include the following:

- `CreationTime` : The date and time that the VPC was associated with the query logging configuration, in Unix time format and Coordinated Universal Time (UTC).
- `Error` : If the value of `Status` is `FAILED` , specify the cause: `DESTINATION_NOT_FOUND` or `ACCESS_DENIED` .
- `Id` : The ID of the query logging association.
- `ResolverQueryLogConfigId` : The ID of the query logging configuration that a VPC is associated with.
- `ResourceId` : The ID of the Amazon VPC that is associated with the query logging configuration.
- `Status` : The status of the query logging association. If you specify `Status` for `Name` , specify the applicable status code for `Values` : `CREATING` , `CREATED` , `DELETING` , or `FAILED` . For more information, see [Status](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ResolverQueryLogConfigAssociation.html#Route53Resolver-Type-route53resolver_ResolverQueryLogConfigAssociation-Status) .

Values -> (list)

When youâre using a `List` operation and you want the operation to return a subset of objects, such as Resolver endpoints or Resolver rules, the value of the parameter that you want to use to filter objects. For example, to list only inbound Resolver endpoints, specify `Direction` for `Name` and specify `INBOUND` for `Values` .

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

For usage examples, see [Pagination](https://docs.aws.amazon.com/cli/latest/userguide/pagination.html) in the *AWS Command Line Interface User Guide* .

`--page-size` (integer)

The size of each page to get in the AWS service call. This does not affect the number of items returned in the commandâs output. Setting a smaller page size results in more calls to the AWS service, retrieving fewer items in each call. This can help prevent the AWS service calls from timing out.

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

**To list Resolver rules**

The following `list-resolver-rules` example lists all the Resolver rules in the current AWS account.

```
aws route53resolver list-resolver-rules
```

Output:

```
{
    "MaxResults": 30,
    "ResolverRules": [
        {
            "Id": "rslvr-autodefined-rr-internet-resolver",
            "CreatorRequestId": "",
            "Arn": "arn:aws:route53resolver:us-west-2::autodefined-rule/rslvr-autodefined-rr-internet-resolver",
            "DomainName": ".",
            "Status": "COMPLETE",
            "RuleType": "RECURSIVE",
            "Name": "Internet Resolver",
            "OwnerId": "Route 53 Resolver",
            "ShareStatus": "NOT_SHARED"
        },
        {
            "Id": "rslvr-rr-42b60677c0example",
            "CreatorRequestId": "2020-01-01-18:47",
            "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-rule/rslvr-rr-42b60677c0bc4e299",
            "DomainName": "example.com.",
            "Status": "COMPLETE",
            "StatusMessage": "[Trace id: 1-5dc4b177-ff1d9d001a0f80005example] Successfully created Resolver Rule.",
            "RuleType": "FORWARD",
            "Name": "my-rule",
            "TargetIps": [
                {
                    "Ip": "192.0.2.45",
                    "Port": 53
                }
            ],
            "ResolverEndpointId": "rslvr-out-d5e5920e37example",
            "OwnerId": "111122223333",
            "ShareStatus": "NOT_SHARED"
        }
    ]
}
```

For more information, see [How Route 53 Resolver Forwards DNS Queries from Your VPCs to Your Network](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/resolver.html#resolver-overview-forward-vpc-to-network) in the *Amazon Route 53 Developer Guide*.

## Output

NextToken -> (string)

If more than `MaxResults` Resolver rules match the specified criteria, you can submit another `ListResolverRules` request to get the next group of results. In the next request, specify the value of `NextToken` from the previous response.

MaxResults -> (integer)

The value that you specified for `MaxResults` in the request.

ResolverRules -> (list)

The Resolver rules that were created using the current Amazon Web Services account and that match the specified filters, if any.

(structure)

For queries that originate in your VPC, detailed information about a Resolver rule, which specifies how to route DNS queries out of the VPC. The `ResolverRule` parameter appears in the response to a [CreateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverRule.html) , [DeleteResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverRule.html) , [GetResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverRule.html) , [ListResolverRules](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverRules.html) , or [UpdateResolverRule](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverRule.html) request.

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