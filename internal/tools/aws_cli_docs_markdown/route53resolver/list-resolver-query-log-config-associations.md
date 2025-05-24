# list-resolver-query-log-config-associationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-query-log-config-associations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/list-resolver-query-log-config-associations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [route53resolver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/route53resolver/index.html#cli-aws-route53resolver) ]

# list-resolver-query-log-config-associations

## Description

Lists information about associations between Amazon VPCs and query logging configurations.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/route53resolver-2018-04-01/ListResolverQueryLogConfigAssociations)

`list-resolver-query-log-config-associations` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `ResolverQueryLogConfigAssociations`

## Synopsis

```
list-resolver-query-log-config-associations
[--filters <value>]
[--sort-by <value>]
[--sort-order <value>]
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

An optional specification to return a subset of query logging associations.

### Note

If you submit a second or subsequent `ListResolverQueryLogConfigAssociations` request and specify the `NextToken` parameter, you must use the same values for `Filters` , if any, as in the previous request.

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

`--sort-by` (string)

The element that you want Resolver to sort query logging associations by.

### Note

If you submit a second or subsequent `ListResolverQueryLogConfigAssociations` request and specify the `NextToken` parameter, you must use the same value for `SortBy` , if any, as in the previous request.

Valid values include the following elements:

- `CreationTime` : The ID of the query logging association.
- `Error` : If the value of `Status` is `FAILED` , the value of `Error` indicates the cause:
- `DESTINATION_NOT_FOUND` : The specified destination (for example, an Amazon S3 bucket) was deleted.
- `ACCESS_DENIED` : Permissions donât allow sending logs to the destination.

If `Status` is a value other than `FAILED` , `ERROR` is null.

- `Id` : The ID of the query logging association
- `ResolverQueryLogConfigId` : The ID of the query logging configuration
- `ResourceId` : The ID of the VPC that is associated with the query logging configuration
- `Status` : The current status of the configuration. Valid values include the following:
- `CREATING` : Resolver is creating an association between an Amazon VPC and a query logging configuration.
- `CREATED` : The association between an Amazon VPC and a query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.
- `DELETING` : Resolver is deleting this query logging association.
- `FAILED` : Resolver either couldnât create or couldnât delete the query logging association. Here are two common causes:
- The specified destination (for example, an Amazon S3 bucket) was deleted.
- Permissions donât allow sending logs to the destination.

`--sort-order` (string)

If you specified a value for `SortBy` , the order that you want query logging associations to be listed in, `ASCENDING` or `DESCENDING` .

### Note

If you submit a second or subsequent `ListResolverQueryLogConfigAssociations` request and specify the `NextToken` parameter, you must use the same value for `SortOrder` , if any, as in the previous request.

Possible values:

- `ASCENDING`
- `DESCENDING`

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

## Output

NextToken -> (string)

If there are more than `MaxResults` query logging associations, you can submit another `ListResolverQueryLogConfigAssociations` request to get the next group of associations. In the next request, specify the value of `NextToken` from the previous response.

TotalCount -> (integer)

The total number of query logging associations that were created by the current account in the specified Region. This count can differ from the number of associations that are returned in a `ListResolverQueryLogConfigAssociations` response, depending on the values that you specify in the request.

TotalFilteredCount -> (integer)

The total number of query logging associations that were created by the current account in the specified Region and that match the filters that were specified in the `ListResolverQueryLogConfigAssociations` request. For the total number of associations that were created by the current account in the specified Region, see `TotalCount` .

ResolverQueryLogConfigAssociations -> (list)

A list that contains one `ResolverQueryLogConfigAssociations` element for each query logging association that matches the values that you specified for `Filter` .

(structure)

In the response to an [AssociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_AssociateResolverQueryLogConfig.html) , [DisassociateResolverQueryLogConfig](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_DisassociateResolverQueryLogConfig.html) , [GetResolverQueryLogConfigAssociation](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_GetResolverQueryLogConfigAssociation.html) , or [ListResolverQueryLogConfigAssociations](https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53resolver_ListResolverQueryLogConfigAssociations.html) , request, a complex type that contains settings for a specified association between an Amazon VPC and a query logging configuration.

Id -> (string)

The ID of the query logging association.

ResolverQueryLogConfigId -> (string)

The ID of the query logging configuration that a VPC is associated with.

ResourceId -> (string)

The ID of the Amazon VPC that is associated with the query logging configuration.

Status -> (string)

The status of the specified query logging association. Valid values include the following:

- `CREATING` : Resolver is creating an association between an Amazon VPC and a query logging configuration.
- `ACTIVE` : The association between an Amazon VPC and a query logging configuration was successfully created. Resolver is logging queries that originate in the specified VPC.
- `DELETING` : Resolver is deleting this query logging association.
- `FAILED` : Resolver either couldnât create or couldnât delete the query logging association.

Error -> (string)

If the value of `Status` is `FAILED` , the value of `Error` indicates the cause:

- `DESTINATION_NOT_FOUND` : The specified destination (for example, an Amazon S3 bucket) was deleted.
- `ACCESS_DENIED` : Permissions donât allow sending logs to the destination.

If the value of `Status` is a value other than `FAILED` , `Error` is null.

ErrorMessage -> (string)

Contains additional information about the error. If the value or `Error` is null, the value of `ErrorMessage` also is null.

CreationTime -> (string)

The date and time that the VPC was associated with the query logging configuration, in Unix time format and Coordinated Universal Time (UTC).