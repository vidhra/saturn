# list-resolver-endpointsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-endpoints.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-endpoints.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/index.html#cli-aws-route53resolver) ]

# list-resolver-endpoints

## Description

Lists all the Resolver endpoints that were created using the current Amazon Web Services account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53resolver-2018-04-01/ListResolverEndpoints)

`list-resolver-endpoints` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ResolverEndpoints`

## Synopsis

```
list-resolver-endpoints
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

An optional specification to return a subset of Resolver endpoints, such as all inbound Resolver endpoints.

### Note

If you submit a second or subsequent `ListResolverEndpoints` request and specify the `NextToken` parameter, you must use the same values for `Filters` , if any, as in the previous request.

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

**To list Resolver endpoints in an AWS Region**

The following `list-resolver-endpoints` example lists the inbound and outbound Resolver endpoints that exist in the current account.

```
aws route53resolver list-resolver-endpoints
```

Output:

```
{
    "MaxResults": 10,
    "ResolverEndpoints": [
        {
            "Id": "rslvr-in-497098ad59example",
            "CreatorRequestId": "2020-01-01-18:47",
            "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-in-497098ad59example",
            "Name": "my-inbound-endpoint",
            "SecurityGroupIds": [
                "sg-05cd7b25d6example"
            ],
            "Direction": "INBOUND",
            "IpAddressCount": 2,
            "HostVPCId": "vpc-304bexam",
            "Status": "OPERATIONAL",
            "StatusMessage": "This Resolver Endpoint is operational.",
            "CreationTime": "2020-01-01T23:25:45.538Z",
            "ModificationTime": "2020-01-01T23:25:45.538Z"
        },
        {
            "Id": "rslvr-out-d5e5920e37example",
            "CreatorRequestId": "2020-01-01-18:48",
            "Arn": "arn:aws:route53resolver:us-west-2:111122223333:resolver-endpoint/rslvr-out-d5e5920e37example",
            "Name": "my-outbound-endpoint",
            "SecurityGroupIds": [
                "sg-05cd7b25d6example"
            ],
            "Direction": "OUTBOUND",
            "IpAddressCount": 2,
            "HostVPCId": "vpc-304bexam",
            "Status": "OPERATIONAL",
            "StatusMessage": "This Resolver Endpoint is operational.",
            "CreationTime": "2020-01-01T23:50:50.979Z",
            "ModificationTime": "2020-01-01T23:50:50.979Z"
        }
    ]
}
```

## Output

NextToken -> (string)

If more than `MaxResults` IP addresses match the specified criteria, you can submit another `ListResolverEndpoint` request to get the next group of results. In the next request, specify the value of `NextToken` from the previous response.

MaxResults -> (integer)

The value that you specified for `MaxResults` in the request.

ResolverEndpoints -> (list)

The Resolver endpoints that were created by using the current Amazon Web Services account, and that match the specified filters, if any.

(structure)

In the response to a [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html) , [DeleteResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DeleteResolverEndpoint.html) , [GetResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverEndpoint.html) , Updates the name, or ResolverEndpointType for an endpoint, or [UpdateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_UpdateResolverEndpoint.html) request, a complex type that contains settings for an existing inbound or outbound Resolver endpoint.

Id -> (string)

The ID of the Resolver endpoint.

CreatorRequestId -> (string)

A unique string that identifies the request that created the Resolver endpoint. The `CreatorRequestId` allows failed requests to be retried without the risk of running the operation twice.

Arn -> (string)

The ARN (Amazon Resource Name) for the Resolver endpoint.

Name -> (string)

The name that you assigned to the Resolver endpoint when you submitted a [CreateResolverEndpoint](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_CreateResolverEndpoint.html) request.

SecurityGroupIds -> (list)

The ID of one or more security groups that control access to this VPC. The security group must include one or more inbound rules (for inbound endpoints) or outbound rules (for outbound endpoints). Inbound and outbound rules must allow TCP and UDP access. For inbound access, open port 53. For outbound access, open the port that youâre using for DNS queries on your network.

(string)

Direction -> (string)

Indicates whether the Resolver endpoint allows inbound or outbound DNS queries:

- `INBOUND` : allows DNS queries to your VPC from your network
- `OUTBOUND` : allows DNS queries from your VPC to your network

IpAddressCount -> (integer)

The number of IP addresses that the Resolver endpoint can use for DNS queries.

HostVPCId -> (string)

The ID of the VPC that you want to create the Resolver endpoint in.

Status -> (string)

A code that specifies the current status of the Resolver endpoint. Valid values include the following:

- `CREATING` : Resolver is creating and configuring one or more Amazon VPC network interfaces for this endpoint.
- `OPERATIONAL` : The Amazon VPC network interfaces for this endpoint are correctly configured and able to pass inbound or outbound DNS queries between your network and Resolver.
- `UPDATING` : Resolver is associating or disassociating one or more network interfaces with this endpoint.
- `AUTO_RECOVERING` : Resolver is trying to recover one or more of the network interfaces that are associated with this endpoint. During the recovery process, the endpoint functions with limited capacity because of the limit on the number of DNS queries per IP address (per network interface). For the current limit, see [Limits on Route 53 Resolver](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/DNSLimitations.html#limits-api-entities-resolver) .
- `ACTION_NEEDED` : This endpoint is unhealthy, and Resolver canât automatically recover it. To resolve the problem, we recommend that you check each IP address that you associated with the endpoint. For each IP address that isnât available, add another IP address and then delete the IP address that isnât available. (An endpoint must always include at least two IP addresses.) A status of `ACTION_NEEDED` can have a variety of causes. Here are two common causes:
- One or more of the network interfaces that are associated with the endpoint were deleted using Amazon VPC.
- The network interface couldnât be created for some reason thatâs outside the control of Resolver.
- `DELETING` : Resolver is deleting this endpoint and the associated network interfaces.

StatusMessage -> (string)

A detailed description of the status of the Resolver endpoint.

CreationTime -> (string)

The date and time that the endpoint was created, in Unix time format and Coordinated Universal Time (UTC).

ModificationTime -> (string)

The date and time that the endpoint was last modified, in Unix time format and Coordinated Universal Time (UTC).

OutpostArn -> (string)

The ARN (Amazon Resource Name) for the Outpost.

PreferredInstanceType -> (string)

The Amazon EC2 instance type.

ResolverEndpointType -> (string)

The Resolver endpoint IP address type.

Protocols -> (list)

Protocols used for the endpoint. DoH-FIPS is applicable for inbound endpoints only.

For an inbound endpoint you can apply the protocols as follows:

- Do53 and DoH in combination.
- Do53 and DoH-FIPS in combination.
- Do53 alone.
- DoH alone.
- DoH-FIPS alone.
- None, which is treated as Do53.

For an outbound endpoint you can apply the protocols as follows:

- Do53 and DoH in combination.
- Do53 alone.
- DoH alone.
- None, which is treated as Do53.

(string)