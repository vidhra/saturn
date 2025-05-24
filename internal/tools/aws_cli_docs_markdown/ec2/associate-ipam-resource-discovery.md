# associate-ipam-resource-discoveryÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-ipam-resource-discovery.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/associate-ipam-resource-discovery.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# associate-ipam-resource-discovery

## Description

Associates an IPAM resource discovery with an Amazon VPC IPAM. A resource discovery is an IPAM component that enables IPAM to manage and monitor resources that belong to the owning account.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/AssociateIpamResourceDiscovery)

## Synopsis

```
associate-ipam-resource-discovery
[--dry-run | --no-dry-run]
--ipam-id <value>
--ipam-resource-discovery-id <value>
[--tag-specifications <value>]
[--client-token <value>]
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

A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--ipam-id` (string)

An IPAM ID.

`--ipam-resource-discovery-id` (string)

A resource discovery ID.

`--tag-specifications` (list)

Tag specifications.

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

A client token.

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

**To associate a resource discovery with an IPAM**

In this example, you are an IPAM delegated admin and a resource discovery has been created and shared with you by another AWS account so that you can use IPAM to manage and monitor resource CIDRs owned by the other account.

Note

- To complete this request, youâll need the resource discovery ID which you can get with [describe-ipam-resource-discoveries](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipam-resource-discoveries.html) and the IPAM ID which you can get with [describe-ipams](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-ipams.html).
- The resource discovery that you are associating must have first been shared with your account using AWS RAM.
- The `--region` you enter must match the home Region of the IPAM you are associating it with.

The following `associate-ipam-resource-discovery` example associates a resource discovery with an IPAM.

```
aws ec2 associate-ipam-resource-discovery \
    --ipam-id ipam-005f921c17ebd5107 \
    --ipam-resource-discovery-id ipam-res-disco-03e0406de76a044ee \
    --tag-specifications 'ResourceType=ipam-resource-discovery,Tags=[{Key=cost-center,Value=cc123}]' \
    --region us-east-1
```

Output:

```
{
    {
        "IpamResourceDiscoveryAssociation": {
            "OwnerId": "320805250157",
            "IpamResourceDiscoveryAssociationId": "ipam-res-disco-assoc-04382a6346357cf82",
            "IpamResourceDiscoveryAssociationArn": "arn:aws:ec2::320805250157:ipam-resource-discovery-association/ipam-res-disco-assoc-04382a6346357cf82",
            "IpamResourceDiscoveryId": "ipam-res-disco-0365d2977fc1672fe",
            "IpamId": "ipam-005f921c17ebd5107",
            "IpamArn": "arn:aws:ec2::320805250157:ipam/ipam-005f921c17ebd5107",
            "IpamRegion": "us-east-1",
            "IsDefault": false,
            "ResourceDiscoveryStatus": "active",
            "State": "associate-in-progress",
            "Tags": []
        }
    }
}
```

Once you associate a resource discovery, you can monitor and/or manage the IP addresses of resources created by the other accounts. For more information, see [Integrate IPAM with accounts outside of your organization](https://docs.aws.amazon.com/vpc/latest/ipam/enable-integ-ipam-outside-org.html) in the *Amazon VPC IPAM User Guide*.

## Output

IpamResourceDiscoveryAssociation -> (structure)

A resource discovery association. An associated resource discovery is a resource discovery that has been associated with an IPAM.

OwnerId -> (string)

The Amazon Web Services account ID of the resource discovery owner.

IpamResourceDiscoveryAssociationId -> (string)

The resource discovery association ID.

IpamResourceDiscoveryAssociationArn -> (string)

The resource discovery association Amazon Resource Name (ARN).

IpamResourceDiscoveryId -> (string)

The resource discovery ID.

IpamId -> (string)

The IPAM ID.

IpamArn -> (string)

The IPAM ARN.

IpamRegion -> (string)

The IPAM home Region.

IsDefault -> (boolean)

Defines if the resource discovery is the default. When you create an IPAM, a default resource discovery is created for your IPAM and itâs associated with your IPAM.

ResourceDiscoveryStatus -> (string)

The resource discovery status.

- `active` - Connection or permissions required to read the results of the resource discovery are intact.
- `not-found` - Connection or permissions required to read the results of the resource discovery are broken. This may happen if the owner of the resource discovery stopped sharing it or deleted the resource discovery. Verify the resource discovery still exists and the Amazon Web Services RAM resource share is still intact.

State -> (string)

The lifecycle state of the association when you associate or disassociate a resource discovery.

- `associate-in-progress` - Resource discovery is being associated.
- `associate-complete` - Resource discovery association is complete.
- `associate-failed` - Resource discovery association has failed.
- `disassociate-in-progress` - Resource discovery is being disassociated.
- `disassociate-complete` - Resource discovery disassociation is complete.
- `disassociate-failed` - Resource discovery disassociation has failed.
- `isolate-in-progress` - Amazon Web Services account that created the resource discovery association has been removed and the resource discovery associatation is being isolated.
- `isolate-complete` - Resource discovery isolation is complete..
- `restore-in-progress` - Resource discovery is being restored.

Tags -> (list)

A tag is a label that you assign to an Amazon Web Services resource. Each tag consists of a key and an optional value. You can use tags to search and filter your resources or track your Amazon Web Services costs.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.