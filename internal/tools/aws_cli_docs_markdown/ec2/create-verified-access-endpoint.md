# create-verified-access-endpointÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-verified-access-endpoint.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/create-verified-access-endpoint.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# create-verified-access-endpoint

## Description

An Amazon Web Services Verified Access endpoint is where you define your application along with an optional endpoint-level access policy.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/CreateVerifiedAccessEndpoint)

## Synopsis

```
create-verified-access-endpoint
--verified-access-group-id <value>
--endpoint-type <value>
--attachment-type <value>
[--domain-certificate-arn <value>]
[--application-domain <value>]
[--endpoint-domain-prefix <value>]
[--security-group-ids <value>]
[--load-balancer-options <value>]
[--network-interface-options <value>]
[--description <value>]
[--policy-document <value>]
[--tag-specifications <value>]
[--client-token <value>]
[--dry-run | --no-dry-run]
[--sse-specification <value>]
[--rds-options <value>]
[--cidr-options <value>]
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

`--verified-access-group-id` (string)

The ID of the Verified Access group to associate the endpoint with.

`--endpoint-type` (string)

The type of Verified Access endpoint to create.

Possible values:

- `load-balancer`
- `network-interface`
- `rds`
- `cidr`

`--attachment-type` (string)

The type of attachment.

Possible values:

- `vpc`

`--domain-certificate-arn` (string)

The ARN of the public TLS/SSL certificate in Amazon Web Services Certificate Manager to associate with the endpoint. The CN in the certificate must match the DNS name your end users will use to reach your application.

`--application-domain` (string)

The DNS name for users to reach your application.

`--endpoint-domain-prefix` (string)

A custom identifier that is prepended to the DNS name that is generated for the endpoint.

`--security-group-ids` (list)

The IDs of the security groups to associate with the Verified Access endpoint. Required if `AttachmentType` is set to `vpc` .

(string)

Syntax:

```
"string" "string" ...
```

`--load-balancer-options` (structure)

The load balancer details. This parameter is required if the endpoint type is `load-balancer` .

Protocol -> (string)

The IP protocol.

Port -> (integer)

The IP port number.

LoadBalancerArn -> (string)

The ARN of the load balancer.

SubnetIds -> (list)

The IDs of the subnets. You can specify only one subnet per Availability Zone.

(string)

PortRanges -> (list)

The port ranges.

(structure)

Describes the port range for a Verified Access endpoint.

FromPort -> (integer)

The start of the port range.

ToPort -> (integer)

The end of the port range.

Shorthand Syntax:

```
Protocol=string,Port=integer,LoadBalancerArn=string,SubnetIds=string,string,PortRanges=[{FromPort=integer,ToPort=integer},{FromPort=integer,ToPort=integer}]
```

JSON Syntax:

```
{
  "Protocol": "http"|"https"|"tcp",
  "Port": integer,
  "LoadBalancerArn": "string",
  "SubnetIds": ["string", ...],
  "PortRanges": [
    {
      "FromPort": integer,
      "ToPort": integer
    }
    ...
  ]
}
```

`--network-interface-options` (structure)

The network interface details. This parameter is required if the endpoint type is `network-interface` .

NetworkInterfaceId -> (string)

The ID of the network interface.

Protocol -> (string)

The IP protocol.

Port -> (integer)

The IP port number.

PortRanges -> (list)

The port ranges.

(structure)

Describes the port range for a Verified Access endpoint.

FromPort -> (integer)

The start of the port range.

ToPort -> (integer)

The end of the port range.

Shorthand Syntax:

```
NetworkInterfaceId=string,Protocol=string,Port=integer,PortRanges=[{FromPort=integer,ToPort=integer},{FromPort=integer,ToPort=integer}]
```

JSON Syntax:

```
{
  "NetworkInterfaceId": "string",
  "Protocol": "http"|"https"|"tcp",
  "Port": integer,
  "PortRanges": [
    {
      "FromPort": integer,
      "ToPort": integer
    }
    ...
  ]
}
```

`--description` (string)

A description for the Verified Access endpoint.

`--policy-document` (string)

The Verified Access policy document.

`--tag-specifications` (list)

The tags to assign to the Verified Access endpoint.

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

`--client-token` (string)

A unique, case-sensitive token that you provide to ensure idempotency of your modification request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html) .

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--sse-specification` (structure)

The options for server side encryption.

CustomerManagedKeyEnabled -> (boolean)

Enable or disable the use of customer managed KMS keys for server side encryption.

Valid values: `True` | `False`

KmsKeyArn -> (string)

The ARN of the KMS key.

Shorthand Syntax:

```
CustomerManagedKeyEnabled=boolean,KmsKeyArn=string
```

JSON Syntax:

```
{
  "CustomerManagedKeyEnabled": true|false,
  "KmsKeyArn": "string"
}
```

`--rds-options` (structure)

The RDS details. This parameter is required if the endpoint type is `rds` .

Protocol -> (string)

The protocol.

Port -> (integer)

The port.

RdsDbInstanceArn -> (string)

The ARN of the RDS instance.

RdsDbClusterArn -> (string)

The ARN of the DB cluster.

RdsDbProxyArn -> (string)

The ARN of the RDS proxy.

RdsEndpoint -> (string)

The RDS endpoint.

SubnetIds -> (list)

The IDs of the subnets. You can specify only one subnet per Availability Zone.

(string)

Shorthand Syntax:

```
Protocol=string,Port=integer,RdsDbInstanceArn=string,RdsDbClusterArn=string,RdsDbProxyArn=string,RdsEndpoint=string,SubnetIds=string,string
```

JSON Syntax:

```
{
  "Protocol": "http"|"https"|"tcp",
  "Port": integer,
  "RdsDbInstanceArn": "string",
  "RdsDbClusterArn": "string",
  "RdsDbProxyArn": "string",
  "RdsEndpoint": "string",
  "SubnetIds": ["string", ...]
}
```

`--cidr-options` (structure)

The CIDR options. This parameter is required if the endpoint type is `cidr` .

Protocol -> (string)

The protocol.

SubnetIds -> (list)

The IDs of the subnets.

(string)

Cidr -> (string)

The CIDR.

PortRanges -> (list)

The port ranges.

(structure)

Describes the port range for a Verified Access endpoint.

FromPort -> (integer)

The start of the port range.

ToPort -> (integer)

The end of the port range.

Shorthand Syntax:

```
Protocol=string,SubnetIds=string,string,Cidr=string,PortRanges=[{FromPort=integer,ToPort=integer},{FromPort=integer,ToPort=integer}]
```

JSON Syntax:

```
{
  "Protocol": "http"|"https"|"tcp",
  "SubnetIds": ["string", ...],
  "Cidr": "string",
  "PortRanges": [
    {
      "FromPort": integer,
      "ToPort": integer
    }
    ...
  ]
}
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

**To create a Verified Access endpoint**

The following `create-verified-access-endpoint` example creates a Verified Access endpoint for the speciied Verified Access group. The specified network interface and security group must belong to the same VPC.

```
aws ec2 create-verified-access-endpoint \
    --verified-access-group-id vagr-0dbe967baf14b7235 \
    --endpoint-type network-interface \
    --attachment-type vpc \
    --domain-certificate-arn arn:aws:acm:us-east-2:123456789012:certificate/eb065ea0-26f9-4e75-a6ce-0a1a7EXAMPLE \
    --application-domain example.com \
    --endpoint-domain-prefix my-ava-app \
    --security-group-ids sg-004915970c4c8f13a \
    --network-interface-options NetworkInterfaceId=eni-0aec70418c8d87a0f,Protocol=https,Port=443 \
    --tag-specifications ResourceType=verified-access-endpoint,Tags=[{Key=Name,Value=my-va-endpoint}]
```

Output:

```
{
    "VerifiedAccessEndpoint": {
        "VerifiedAccessInstanceId": "vai-0ce000c0b7643abea",
        "VerifiedAccessGroupId": "vagr-0dbe967baf14b7235",
        "VerifiedAccessEndpointId": "vae-066fac616d4d546f2",
        "ApplicationDomain": "example.com",
        "EndpointType": "network-interface",
        "AttachmentType": "vpc",
        "DomainCertificateArn": "arn:aws:acm:us-east-2:123456789012:certificate/eb065ea0-26f9-4e75-a6ce-0a1a7EXAMPLE",
        "EndpointDomain": "my-ava-app.edge-00c3372d53b1540bb.vai-0ce000c0b7643abea.prod.verified-access.us-east-2.amazonaws.com",
        "SecurityGroupIds": [
            "sg-004915970c4c8f13a"
        ],
        "NetworkInterfaceOptions": {
            "NetworkInterfaceId": "eni-0aec70418c8d87a0f",
            "Protocol": "https",
            "Port": 443
        },
        "Status": {
            "Code": "pending"
        },
        "Description": "",
        "CreationTime": "2023-08-25T20:54:43",
        "LastUpdatedTime": "2023-08-25T20:54:43",
        "Tags": [
            {
                "Key": "Name",
                "Value": "my-va-endpoint"
            }
        ]
    }
}
```

For more information, see [Verified Access endpoints](https://docs.aws.amazon.com/verified-access/latest/ug/verified-access-endpoints.html) in the *AWS Verified Access User Guide*.

## Output

VerifiedAccessEndpoint -> (structure)

Details about the Verified Access endpoint.

VerifiedAccessInstanceId -> (string)

The ID of the Amazon Web Services Verified Access instance.

VerifiedAccessGroupId -> (string)

The ID of the Amazon Web Services Verified Access group.

VerifiedAccessEndpointId -> (string)

The ID of the Amazon Web Services Verified Access endpoint.

ApplicationDomain -> (string)

The DNS name for users to reach your application.

EndpointType -> (string)

The type of Amazon Web Services Verified Access endpoint. Incoming application requests will be sent to an IP address, load balancer or a network interface depending on the endpoint type specified.

AttachmentType -> (string)

The type of attachment used to provide connectivity between the Amazon Web Services Verified Access endpoint and the application.

DomainCertificateArn -> (string)

The ARN of a public TLS/SSL certificate imported into or created with ACM.

EndpointDomain -> (string)

A DNS name that is generated for the endpoint.

DeviceValidationDomain -> (string)

Returned if endpoint has a device trust provider attached.

SecurityGroupIds -> (list)

The IDs of the security groups for the endpoint.

(string)

LoadBalancerOptions -> (structure)

The load balancer details if creating the Amazon Web Services Verified Access endpoint as `load-balancer` type.

Protocol -> (string)

The IP protocol.

Port -> (integer)

The IP port number.

LoadBalancerArn -> (string)

The ARN of the load balancer.

SubnetIds -> (list)

The IDs of the subnets.

(string)

PortRanges -> (list)

The port ranges.

(structure)

Describes a port range.

FromPort -> (integer)

The start of the port range.

ToPort -> (integer)

The end of the port range.

NetworkInterfaceOptions -> (structure)

The options for network-interface type endpoint.

NetworkInterfaceId -> (string)

The ID of the network interface.

Protocol -> (string)

The IP protocol.

Port -> (integer)

The IP port number.

PortRanges -> (list)

The port ranges.

(structure)

Describes a port range.

FromPort -> (integer)

The start of the port range.

ToPort -> (integer)

The end of the port range.

Status -> (structure)

The endpoint status.

Code -> (string)

The status code of the Verified Access endpoint.

Message -> (string)

The status message of the Verified Access endpoint.

Description -> (string)

A description for the Amazon Web Services Verified Access endpoint.

CreationTime -> (string)

The creation time.

LastUpdatedTime -> (string)

The last updated time.

DeletionTime -> (string)

The deletion time.

Tags -> (list)

The tags.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

SseSpecification -> (structure)

The options in use for server side encryption.

CustomerManagedKeyEnabled -> (boolean)

Indicates whether customer managed KMS keys are in use for server side encryption.

Valid values: `True` | `False`

KmsKeyArn -> (string)

The ARN of the KMS key.

RdsOptions -> (structure)

The options for an RDS endpoint.

Protocol -> (string)

The protocol.

Port -> (integer)

The port.

RdsDbInstanceArn -> (string)

The ARN of the RDS instance.

RdsDbClusterArn -> (string)

The ARN of the DB cluster.

RdsDbProxyArn -> (string)

The ARN of the RDS proxy.

RdsEndpoint -> (string)

The RDS endpoint.

SubnetIds -> (list)

The IDs of the subnets.

(string)

CidrOptions -> (structure)

The options for a CIDR endpoint.

Cidr -> (string)

The CIDR.

PortRanges -> (list)

The port ranges.

(structure)

Describes a port range.

FromPort -> (integer)

The start of the port range.

ToPort -> (integer)

The end of the port range.

Protocol -> (string)

The protocol.

SubnetIds -> (list)

The IDs of the subnets.

(string)