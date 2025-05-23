# delete-firewallÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-firewall.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/delete-firewall.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [network-firewall](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/network-firewall/index.html#cli-aws-network-firewall) ]

# delete-firewall

## Description

Deletes the specified  Firewall and its  FirewallStatus . This operation requires the firewallâs `DeleteProtection` flag to be `FALSE` . You canât revert this operation.

You can check whether a firewall is in use by reviewing the route tables for the Availability Zones where you have firewall subnet mappings. Retrieve the subnet mappings by calling  DescribeFirewall . You define and update the route tables through Amazon VPC. As needed, update the route tables for the zones to remove the firewall endpoints. When the route tables no longer use the firewall endpoints, you can remove the firewall safely.

To delete a firewall, remove the delete protection if you need to using  UpdateFirewallDeleteProtection , then delete the firewall by calling  DeleteFirewall .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/network-firewall-2020-11-12/DeleteFirewall)

## Synopsis

```
delete-firewall
[--firewall-name <value>]
[--firewall-arn <value>]
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

`--firewall-name` (string)

The descriptive name of the firewall. You canât change the name of a firewall after you create it.

You must specify the ARN or the name, and you can specify both.

`--firewall-arn` (string)

The Amazon Resource Name (ARN) of the firewall.

You must specify the ARN or the name, and you can specify both.

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

Firewall -> (structure)

The firewall defines the configuration settings for an Network Firewall firewall. These settings include the firewall policy, the subnets in your VPC to use for the firewall endpoints, and any tags that are attached to the firewall Amazon Web Services resource.

The status of the firewall, for example whether itâs ready to filter network traffic, is provided in the corresponding  FirewallStatus . You can retrieve both objects by calling  DescribeFirewall .

FirewallName -> (string)

The descriptive name of the firewall. You canât change the name of a firewall after you create it.

FirewallArn -> (string)

The Amazon Resource Name (ARN) of the firewall.

FirewallPolicyArn -> (string)

The Amazon Resource Name (ARN) of the firewall policy.

The relationship of firewall to firewall policy is many to one. Each firewall requires one firewall policy association, and you can use the same firewall policy for multiple firewalls.

VpcId -> (string)

The unique identifier of the VPC where the firewall is in use.

SubnetMappings -> (list)

The public subnets that Network Firewall is using for the firewall. Each subnet must belong to a different Availability Zone.

(structure)

The ID for a subnet that you want to associate with the firewall. This is used with  CreateFirewall and  AssociateSubnets . Network Firewall creates an instance of the associated firewall in each subnet that you specify, to filter traffic in the subnetâs Availability Zone.

SubnetId -> (string)

The unique identifier for the subnet.

IPAddressType -> (string)

The subnetâs IP address type. You canât change the IP address type after you create the subnet.

DeleteProtection -> (boolean)

A flag indicating whether it is possible to delete the firewall. A setting of `TRUE` indicates that the firewall is protected against deletion. Use this setting to protect against accidentally deleting a firewall that is in use. When you create a firewall, the operation initializes this flag to `TRUE` .

SubnetChangeProtection -> (boolean)

A setting indicating whether the firewall is protected against changes to the subnet associations. Use this setting to protect against accidentally modifying the subnet associations for a firewall that is in use. When you create a firewall, the operation initializes this setting to `TRUE` .

FirewallPolicyChangeProtection -> (boolean)

A setting indicating whether the firewall is protected against a change to the firewall policy association. Use this setting to protect against accidentally modifying the firewall policy for a firewall that is in use. When you create a firewall, the operation initializes this setting to `TRUE` .

Description -> (string)

A description of the firewall.

FirewallId -> (string)

The unique identifier for the firewall.

Tags -> (list)

(structure)

A key:value pair associated with an Amazon Web Services resource. The key:value pair can be anything you define. Typically, the tag key represents a category (such as âenvironmentâ) and the tag value represents a specific value within that category (such as âtest,â âdevelopment,â or âproductionâ). You can add up to 50 tags to each Amazon Web Services resource.

Key -> (string)

The part of the key:value pair that defines a tag. You can use a tag key to describe a category of information, such as âcustomer.â Tag keys are case-sensitive.

Value -> (string)

The part of the key:value pair that defines a tag. You can use a tag value to describe a specific value within a category, such as âcompanyAâ or âcompanyB.â Tag values are case-sensitive.

EncryptionConfiguration -> (structure)

A complex type that contains the Amazon Web Services KMS encryption configuration settings for your firewall.

KeyId -> (string)

The ID of the Amazon Web Services Key Management Service (KMS) customer managed key. You can use any of the key identifiers that KMS supports, unless youâre using a key thatâs managed by another account. If youâre using a key managed by another account, then specify the key ARN. For more information, see [Key ID](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#key-id) in the *Amazon Web Services KMS Developer Guide* .

Type -> (string)

The type of Amazon Web Services KMS key to use for encryption of your Network Firewall resources.

EnabledAnalysisTypes -> (list)

An optional setting indicating the specific traffic analysis types to enable on the firewall.

(string)

FirewallStatus -> (structure)

Detailed information about the current status of a  Firewall . You can retrieve this for a firewall by calling  DescribeFirewall and providing the firewall name and ARN.

Status -> (string)

The readiness of the configured firewall to handle network traffic across all of the Availability Zones where youâve configured it. This setting is `READY` only when the `ConfigurationSyncStateSummary` value is `IN_SYNC` and the `Attachment` `Status` values for all of the configured subnets are `READY` .

ConfigurationSyncStateSummary -> (string)

The configuration sync state for the firewall. This summarizes the sync states reported in the `Config` settings for all of the Availability Zones where you have configured the firewall.

When you create a firewall or update its configuration, for example by adding a rule group to its firewall policy, Network Firewall distributes the configuration changes to all zones where the firewall is in use. This summary indicates whether the configuration changes have been applied everywhere.

This status must be `IN_SYNC` for the firewall to be ready for use, but it doesnât indicate that the firewall is ready. The `Status` setting indicates firewall readiness.

SyncStates -> (map)

The subnets that youâve configured for use by the Network Firewall firewall. This contains one array element per Availability Zone where youâve configured a subnet. These objects provide details of the information that is summarized in the `ConfigurationSyncStateSummary` and `Status` , broken down by zone and configuration object.

key -> (string)

value -> (structure)

The status of the firewall endpoint and firewall policy configuration for a single VPC subnet.

For each VPC subnet that you associate with a firewall, Network Firewall does the following:

- Instantiates a firewall endpoint in the subnet, ready to take traffic.
- Configures the endpoint with the current firewall policy settings, to provide the filtering behavior for the endpoint.

When you update a firewall, for example to add a subnet association or change a rule group in the firewall policy, the affected sync states reflect out-of-sync or not ready status until the changes are complete.

Attachment -> (structure)

The attachment status of the firewallâs association with a single VPC subnet. For each configured subnet, Network Firewall creates the attachment by instantiating the firewall endpoint in the subnet so that itâs ready to take traffic. This is part of the  FirewallStatus .

SubnetId -> (string)

The unique identifier of the subnet that youâve specified to be used for a firewall endpoint.

EndpointId -> (string)

The identifier of the firewall endpoint that Network Firewall has instantiated in the subnet. You use this to identify the firewall endpoint in the VPC route tables, when you redirect the VPC traffic through the endpoint.

Status -> (string)

The current status of the firewall endpoint in the subnet. This value reflects both the instantiation of the endpoint in the VPC subnet and the sync states that are reported in the `Config` settings. When this value is `READY` , the endpoint is available and configured properly to handle network traffic. When the endpoint isnât available for traffic, this value will reflect its state, for example `CREATING` or `DELETING` .

StatusMessage -> (string)

If Network Firewall fails to create or delete the firewall endpoint in the subnet, it populates this with the reason for the error or failure and how to resolve it. A `FAILED` status indicates a non-recoverable state, and a `ERROR` status indicates an issue that you can fix. Depending on the error, it can take as many as 15 minutes to populate this field. For more information about the causes for failiure or errors and solutions available for this field, see [Troubleshooting firewall endpoint failures](https://docs.aws.amazon.com/network-firewall/latest/developerguide/firewall-troubleshooting-endpoint-failures.html) in the *Network Firewall Developer Guide* .

Config -> (map)

The configuration status of the firewall endpoint in a single VPC subnet. Network Firewall provides each endpoint with the rules that are configured in the firewall policy. Each time you add a subnet or modify the associated firewall policy, Network Firewall synchronizes the rules in the endpoint, so it can properly filter network traffic. This is part of the  FirewallStatus .

key -> (string)

value -> (structure)

Provides configuration status for a single policy or rule group that is used for a firewall endpoint. Network Firewall provides each endpoint with the rules that are configured in the firewall policy. Each time you add a subnet or modify the associated firewall policy, Network Firewall synchronizes the rules in the endpoint, so it can properly filter network traffic. This is part of a  SyncState for a firewall.

SyncStatus -> (string)

Indicates whether this object is in sync with the version indicated in the update token.

UpdateToken -> (string)

The current version of the object that is either in sync or pending synchronization.

CapacityUsageSummary -> (structure)

Describes the capacity usage of the resources contained in a firewallâs reference sets. Network Firewall calclulates the capacity usage by taking an aggregated count of all of the resources used by all of the reference sets in a firewall.

CIDRs -> (structure)

Describes the capacity usage of the CIDR blocks used by the IP set references in a firewall.

AvailableCIDRCount -> (integer)

The number of CIDR blocks available for use by the IP set references in a firewall.

UtilizedCIDRCount -> (integer)

The number of CIDR blocks used by the IP set references in a firewall.

IPSetReferences -> (map)

The list of the IP set references used by a firewall.

key -> (string)

value -> (structure)

General information about the IP set.

ResolvedCIDRCount -> (integer)

Describes the total number of CIDR blocks currently in use by the IP set references in a firewall. To determine how many CIDR blocks are available for you to use in a firewall, you can call `AvailableCIDRCount` .