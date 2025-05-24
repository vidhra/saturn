# create-vpc-endpoint-service-configurationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint-service-configuration.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-vpc-endpoint-service-configuration.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# create-vpc-endpoint-service-configuration

## Description

Creates a VPC endpoint service to which service consumers (Amazon Web Services accounts, users, and IAM roles) can connect.

Before you create an endpoint service, you must create one of the following for your service:

- A [Network Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/) . Service consumers connect to your service using an interface endpoint.
- A [Gateway Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/gateway/) . Service consumers connect to your service using a Gateway Load Balancer endpoint.

If you set the private DNS name, you must prove that you own the private DNS domain name.

For more information, see the [Amazon Web Services PrivateLink Guide](https://docs.aws.amazon.com/vpc/latest/privatelink/) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateVpcEndpointServiceConfiguration)

## Synopsis

```
create-vpc-endpoint-service-configuration
[--dry-run | --no-dry-run]
[--acceptance-required | --no-acceptance-required]
[--private-dns-name <value>]
[--network-load-balancer-arns <value>]
[--gateway-load-balancer-arns <value>]
[--supported-ip-address-types <value>]
[--supported-regions <value>]
[--client-token <value>]
[--tag-specifications <value>]
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

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--acceptance-required` | `--no-acceptance-required` (boolean)

Indicates whether requests from service consumers to create an endpoint to your service must be accepted manually.

`--private-dns-name` (string)

(Interface endpoint configuration) The private DNS name to assign to the VPC endpoint service.

`--network-load-balancer-arns` (list)

The Amazon Resource Names (ARNs) of the Network Load Balancers.

(string)

Syntax:

```
"string" "string" ...
```

`--gateway-load-balancer-arns` (list)

The Amazon Resource Names (ARNs) of the Gateway Load Balancers.

(string)

Syntax:

```
"string" "string" ...
```

`--supported-ip-address-types` (list)

The supported IP address types. The possible values are `ipv4` and `ipv6` .

(string)

Syntax:

```
"string" "string" ...
```

`--supported-regions` (list)

The Regions from which service consumers can access the service.

(string)

Syntax:

```
"string" "string" ...
```

`--client-token` (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [How to ensure idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

`--tag-specifications` (list)

The tags to associate with the service.

(structure)

The tags to apply to a resource when the resource is being created. When you specify a tag, you must specify the resource type to tag, otherwise the request will fail.

### Note

The `Valid Values` lists all the resource types that can be tagged. However, the action youâre using might not support tagging all of these resource types. If you try to tag a resource type that is unsupported for the action youâre using, youâll get an error.

ResourceType -> (string)

The type of resource to tag on creation.

Tags -> (list)

The tags to apply to the resource.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

Shorthand Syntax:

```
ResourceType=string,Tags=[{Key=string,Value=string},{Key=string,Value=string}] ...
```

JSON Syntax:

```
[
  {
    "ResourceType": "capacity-reservation"|"client-vpn-endpoint"|"customer-gateway"|"carrier-gateway"|"coip-pool"|"declarative-policies-report"|"dedicated-host"|"dhcp-options"|"egress-only-internet-gateway"|"elastic-ip"|"elastic-gpu"|"export-image-task"|"export-instance-task"|"fleet"|"fpga-image"|"host-reservation"|"image"|"import-image-task"|"import-snapshot-task"|"instance"|"instance-event-window"|"internet-gateway"|"ipam"|"ipam-pool"|"ipam-scope"|"ipv4pool-ec2"|"ipv6pool-ec2"|"key-pair"|"launch-template"|"local-gateway"|"local-gateway-route-table"|"local-gateway-virtual-interface"|"local-gateway-virtual-interface-group"|"local-gateway-route-table-vpc-association"|"local-gateway-route-table-virtual-interface-group-association"|"natgateway"|"network-acl"|"network-interface"|"network-insights-analysis"|"network-insights-path"|"network-insights-access-scope"|"network-insights-access-scope-analysis"|"outpost-lag"|"placement-group"|"prefix-list"|"replace-root-volume-task"|"reserved-instances"|"route-table"|"security-group"|"security-group-rule"|"service-link-virtual-interface"|"snapshot"|"spot-fleet-request"|"spot-instances-request"|"subnet"|"subnet-cidr-reservation"|"traffic-mirror-filter"|"traffic-mirror-session"|"traffic-mirror-target"|"transit-gateway"|"transit-gateway-attachment"|"transit-gateway-connect-peer"|"transit-gateway-multicast-domain"|"transit-gateway-policy-table"|"transit-gateway-route-table"|"transit-gateway-route-table-announcement"|"volume"|"vpc"|"vpc-endpoint"|"vpc-endpoint-connection"|"vpc-endpoint-service"|"vpc-endpoint-service-permission"|"vpc-peering-connection"|"vpn-connection"|"vpn-gateway"|"vpc-flow-log"|"capacity-reservation-fleet"|"traffic-mirror-filter-rule"|"vpc-endpoint-connection-device-type"|"verified-access-instance"|"verified-access-group"|"verified-access-endpoint"|"verified-access-policy"|"verified-access-trust-provider"|"vpn-connection-device-type"|"vpc-block-public-access-exclusion"|"route-server"|"route-server-endpoint"|"route-server-peer"|"ipam-resource-discovery"|"ipam-resource-discovery-association"|"instance-connect-endpoint"|"verified-access-endpoint-target"|"ipam-external-resource-verification-token"|"mac-modification-task",
    "Tags": [
      {
        "Key": "string",
        "Value": "string"
      }
      ...
    ]
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

**Example 1: To create an endpoint service configuration for an interface endpoint**

The following `create-vpc-endpoint-service-configuration` example creates a VPC endpoint service configuration using the Network Load Balancer `nlb-vpce`. This example also specifies that requests to connect to the service through an interface endpoint must be accepted.

```
aws ec2 create-vpc-endpoint-service-configuration \
    --network-load-balancer-arns arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/nlb-vpce/e94221227f1ba532 \
    --acceptance-required
```

Output:

```
{
   "ServiceConfiguration": {
       "ServiceType": [
           {
               "ServiceType": "Interface"
           }
       ],
       "NetworkLoadBalancerArns": [
           "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/net/nlb-vpce/e94221227f1ba532"
       ],
       "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-03d5ebb7d9579a2b3",
       "ServiceState": "Available",
       "ServiceId": "vpce-svc-03d5ebb7d9579a2b3",
       "AcceptanceRequired": true,
       "AvailabilityZones": [
           "us-east-1d"
       ],
       "BaseEndpointDnsNames": [
           "vpce-svc-03d5ebb7d9579a2b3.us-east-1.vpce.amazonaws.com"
       ]
   }
}
```

For more information, see [Create an endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-endpoint-service.html) in the *AWS PrivateLink User Guide*.

**Example 2: To create an endpoint service configuration for a Gateway Load Balancer endpoint**

The following `create-vpc-endpoint-service-configuration` example creates a VPC endpoint service configuration using the Gateway Load Balancer `GWLBService`. Requests to connect to the service through a Gateway Load Balancer endpoint are automatically accepted.

```
aws ec2 create-vpc-endpoint-service-configuration \
    --gateway-load-balancer-arns arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/gwy/GWLBService/123123123123abcc \
    --no-acceptance-required
```

Output:

```
{
    "ServiceConfiguration": {
        "ServiceType": [
            {
                "ServiceType": "GatewayLoadBalancer"
            }
        ],
        "ServiceId": "vpce-svc-123123a1c43abc123",
        "ServiceName": "com.amazonaws.vpce.us-east-1.vpce-svc-123123a1c43abc123",
        "ServiceState": "Available",
        "AvailabilityZones": [
            "us-east-1d"
        ],
        "AcceptanceRequired": false,
        "ManagesVpcEndpoints": false,
        "GatewayLoadBalancerArns": [
            "arn:aws:elasticloadbalancing:us-east-1:123456789012:loadbalancer/gwy/GWLBService/123123123123abcc"
        ]
    }
}
```

For more information, see [Create a Gateway Load Balancer endpoint service](https://docs.aws.amazon.com/vpc/latest/privatelink/create-gateway-load-balancer-endpoint-service.html) in the *AWS PrivateLink User Guide*.

## Output

ServiceConfiguration -> (structure)

Information about the service configuration.

ServiceType -> (list)

The type of service.

(structure)

Describes the type of service for a VPC endpoint.

ServiceType -> (string)

The type of service.

ServiceId -> (string)

The ID of the service.

ServiceName -> (string)

The name of the service.

ServiceState -> (string)

The service state.

AvailabilityZones -> (list)

The Availability Zones in which the service is available.

(string)

AcceptanceRequired -> (boolean)

Indicates whether requests from other Amazon Web Services accounts to create an endpoint to the service must first be accepted.

ManagesVpcEndpoints -> (boolean)

Indicates whether the service manages its VPC endpoints. Management of the service VPC endpoints using the VPC endpoint API is restricted.

NetworkLoadBalancerArns -> (list)

The Amazon Resource Names (ARNs) of the Network Load Balancers for the service.

(string)

GatewayLoadBalancerArns -> (list)

The Amazon Resource Names (ARNs) of the Gateway Load Balancers for the service.

(string)

SupportedIpAddressTypes -> (list)

The supported IP address types.

(string)

BaseEndpointDnsNames -> (list)

The DNS names for the service.

(string)

PrivateDnsName -> (string)

The private DNS name for the service.

PrivateDnsNameConfiguration -> (structure)

Information about the endpoint service private DNS name configuration.

State -> (string)

The verification state of the VPC endpoint service.

>Consumers of the endpoint service can use the private name only when the state is `verified` .

Type -> (string)

The endpoint service verification type, for example TXT.

Value -> (string)

The value the service provider adds to the private DNS name domain record before verification.

Name -> (string)

The name of the record subdomain the service provider needs to create. The service provider adds the `value` text to the `name` .

PayerResponsibility -> (string)

The payer responsibility.

Tags -> (list)

The tags assigned to the service.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

SupportedRegions -> (list)

The supported Regions.

(structure)

Describes a supported Region.

Region -> (string)

The Region code.

ServiceState -> (string)

The service state. The possible values are `Pending` , `Available` , `Deleting` , `Deleted` , `Failed` , and `Closed` .

RemoteAccessEnabled -> (boolean)

Indicates whether consumers can access the service from a Region other than the Region where the service is hosted.

ClientToken -> (string)

Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.