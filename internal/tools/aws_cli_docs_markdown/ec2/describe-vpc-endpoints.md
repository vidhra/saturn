# describe-vpc-endpointsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoints.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-vpc-endpoints.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-vpc-endpoints

## Description

Describes your VPC endpoints. The default is to describe all your VPC endpoints. Alternatively, you can specify specific VPC endpoint IDs or filter the results to include only the VPC endpoints that match specific criteria.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeVpcEndpoints)

`describe-vpc-endpoints` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `VpcEndpoints`

## Synopsis

```
describe-vpc-endpoints
[--dry-run | --no-dry-run]
[--vpc-endpoint-ids <value>]
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--vpc-endpoint-ids` (list)

The IDs of the VPC endpoints.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

The filters.

- `ip-address-type` - The IP address type (`ipv4` | `ipv6` ).
- `service-name` - The name of the service.
- `service-region` - The Region of the service.
- `tag` :<key> - The key/value combination of a tag assigned to the resource. Use the tag key in the filter name and the tag value as the filter value. For example, to find all resources that have a tag with the key `Owner` and the value `TeamA` , specify `tag:Owner` for the filter name and `TeamA` for the filter value.
- `tag-key` - The key of a tag assigned to the resource. Use this filter to find all resources assigned a tag with a specific key, regardless of the tag value.
- `vpc-id` - The ID of the VPC in which the endpoint resides.
- `vpc-endpoint-id` - The ID of the endpoint.
- `vpc-endpoint-state` - The state of the endpoint (`pendingAcceptance` | `pending` | `available` | `deleting` | `deleted` | `rejected` | `failed` ).
- `vpc-endpoint-type` - The type of VPC endpoint (`Interface` | `Gateway` | `GatewayLoadBalancer` | `Resource` | `ServiceNetwork` ).

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

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

**To describe your VPC endpoints**

The following `describe-vpc-endpoints` example displays details for all of your VPC endpoints.

```
aws ec2 describe-vpc-endpoints
```

Output:

```
{
    "VpcEndpoints": [
        {
            "PolicyDocument": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":\"*\",\"Action\":\"*\",\"Resource\":\"*\"}]}",
            "VpcId": "vpc-aabb1122",
            "NetworkInterfaceIds": [],
            "SubnetIds": [],
            "PrivateDnsEnabled": true,
            "State": "available",
            "ServiceName": "com.amazonaws.us-east-1.dynamodb",
            "RouteTableIds": [
                "rtb-3d560345"
            ],
            "Groups": [],
            "VpcEndpointId": "vpce-032a826a",
            "VpcEndpointType": "Gateway",
            "CreationTimestamp": "2017-09-05T20:41:28Z",
            "DnsEntries": [],
            "OwnerId": "123456789012"
        },
        {
            "PolicyDocument": "{\n  \"Statement\": [\n    {\n      \"Action\": \"*\", \n      \"Effect\": \"Allow\", \n      \"Principal\": \"*\", \n      \"Resource\": \"*\"\n    }\n  ]\n}",
            "VpcId": "vpc-1a2b3c4d",
            "NetworkInterfaceIds": [
                "eni-2ec2b084",
                "eni-1b4a65cf"
            ],
            "SubnetIds": [
                "subnet-d6fcaa8d",
                "subnet-7b16de0c"
            ],
            "PrivateDnsEnabled": false,
            "State": "available",
            "ServiceName": "com.amazonaws.us-east-1.elasticloadbalancing",
            "RouteTableIds": [],
            "Groups": [
                {
                    "GroupName": "default",
                    "GroupId": "sg-54e8bf31"
                }
            ],
            "VpcEndpointId": "vpce-0f89a33420c1931d7",
            "VpcEndpointType": "Interface",
            "CreationTimestamp": "2017-09-05T17:55:27.583Z",
            "DnsEntries": [
                {
                    "HostedZoneId": "Z7HUB22UULQXV",
                    "DnsName": "vpce-0f89a33420c1931d7-bluzidnv.elasticloadbalancing.us-east-1.vpce.amazonaws.com"
                },
                {
                    "HostedZoneId": "Z7HUB22UULQXV",
                    "DnsName": "vpce-0f89a33420c1931d7-bluzidnv-us-east-1b.elasticloadbalancing.us-east-1.vpce.amazonaws.com"
                },
                {
                    "HostedZoneId": "Z7HUB22UULQXV",
                    "DnsName": "vpce-0f89a33420c1931d7-bluzidnv-us-east-1a.elasticloadbalancing.us-east-1.vpce.amazonaws.com"
                }
            ],
            "OwnerId": "123456789012"
        },
        {
            "VpcEndpointId": "vpce-aabbaabbaabbaabba",
            "VpcEndpointType": "GatewayLoadBalancer",
            "VpcId": "vpc-111122223333aabbc",
            "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-123123a1c43abc123",
            "State": "available",
            "SubnetIds": [
                "subnet-0011aabbcc2233445"
            ],
            "RequesterManaged": false,
            "NetworkInterfaceIds": [
                "eni-01010120203030405"
            ],
            "CreationTimestamp": "2020-11-11T08:06:03.522Z",
            "Tags": [],
            "OwnerId": "123456789012"
        }
    ]
}
```

For more information, see [Concepts](https://docs.aws.amazon.com/vpc/latest/privatelink/concepts.html) in the *AWS PrivateLink User Guide*.

## Output

VpcEndpoints -> (list)

Information about the VPC endpoints.

(structure)

Describes a VPC endpoint.

VpcEndpointId -> (string)

The ID of the endpoint.

VpcEndpointType -> (string)

The type of endpoint.

VpcId -> (string)

The ID of the VPC to which the endpoint is associated.

ServiceName -> (string)

The name of the service to which the endpoint is associated.

State -> (string)

The state of the endpoint.

PolicyDocument -> (string)

The policy document associated with the endpoint, if applicable.

RouteTableIds -> (list)

(Gateway endpoint) The IDs of the route tables associated with the endpoint.

(string)

SubnetIds -> (list)

(Interface endpoint) The subnets for the endpoint.

(string)

Groups -> (list)

(Interface endpoint) Information about the security groups that are associated with the network interface.

(structure)

Describes a security group.

GroupId -> (string)

The ID of the security group.

GroupName -> (string)

The name of the security group.

IpAddressType -> (string)

The IP address type for the endpoint.

DnsOptions -> (structure)

The DNS options for the endpoint.

DnsRecordIpType -> (string)

The DNS records created for the endpoint.

PrivateDnsOnlyForInboundResolverEndpoint -> (boolean)

Indicates whether to enable private DNS only for inbound endpoints.

PrivateDnsEnabled -> (boolean)

(Interface endpoint) Indicates whether the VPC is associated with a private hosted zone.

RequesterManaged -> (boolean)

Indicates whether the endpoint is being managed by its service.

NetworkInterfaceIds -> (list)

(Interface endpoint) The network interfaces for the endpoint.

(string)

DnsEntries -> (list)

(Interface endpoint) The DNS entries for the endpoint.

(structure)

Describes a DNS entry.

DnsName -> (string)

The DNS name.

HostedZoneId -> (string)

The ID of the private hosted zone.

CreationTimestamp -> (timestamp)

The date and time that the endpoint was created.

Tags -> (list)

The tags assigned to the endpoint.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the endpoint.

LastError -> (structure)

The last error that occurred for endpoint.

Message -> (string)

The error message for the VPC endpoint error.

Code -> (string)

The error code for the VPC endpoint error.

Ipv4Prefixes -> (list)

Array of IPv4 prefixes.

(structure)

Prefixes of the subnet IP.

SubnetId -> (string)

ID of the subnet.

IpPrefixes -> (list)

Array of SubnetIpPrefixes objects.

(string)

Ipv6Prefixes -> (list)

Array of IPv6 prefixes.

(structure)

Prefixes of the subnet IP.

SubnetId -> (string)

ID of the subnet.

IpPrefixes -> (list)

Array of SubnetIpPrefixes objects.

(string)

FailureReason -> (string)

Reason for the failure.

ServiceNetworkArn -> (string)

The Amazon Resource Name (ARN) of the service network.

ResourceConfigurationArn -> (string)

The Amazon Resource Name (ARN) of the resource configuration.

ServiceRegion -> (string)

The Region where the service is hosted.

NextToken -> (string)

The token to use when requesting the next set of items. If there are no additional items to return, the string is empty.