# purchase-capacity-blockÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/purchase-capacity-block.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/purchase-capacity-block.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# purchase-capacity-block

## Description

Purchase the Capacity Block for use with your account. With Capacity Blocks you ensure GPU capacity is available for machine learning (ML) workloads. You must specify the ID of the Capacity Block offering you are purchasing.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/PurchaseCapacityBlock)

## Synopsis

```
purchase-capacity-block
[--dry-run | --no-dry-run]
[--tag-specifications <value>]
--capacity-block-offering-id <value>
--instance-platform <value>
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

`--tag-specifications` (list)

The tags to apply to the Capacity Block during launch.

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

`--capacity-block-offering-id` (string)

The ID of the Capacity Block offering.

`--instance-platform` (string)

The type of operating system for which to reserve capacity.

Possible values:

- `Linux/UNIX`
- `Red Hat Enterprise Linux`
- `SUSE Linux`
- `Windows`
- `Windows with SQL Server`
- `Windows with SQL Server Enterprise`
- `Windows with SQL Server Standard`
- `Windows with SQL Server Web`
- `Linux with SQL Server Standard`
- `Linux with SQL Server Web`
- `Linux with SQL Server Enterprise`
- `RHEL with SQL Server Standard`
- `RHEL with SQL Server Enterprise`
- `RHEL with SQL Server Web`
- `RHEL with HA`
- `RHEL with HA and SQL Server Standard`
- `RHEL with HA and SQL Server Enterprise`
- `Ubuntu Pro`

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

CapacityReservation -> (structure)

The Capacity Reservation.

CapacityReservationId -> (string)

The ID of the Capacity Reservation.

OwnerId -> (string)

The ID of the Amazon Web Services account that owns the Capacity Reservation.

CapacityReservationArn -> (string)

The Amazon Resource Name (ARN) of the Capacity Reservation.

AvailabilityZoneId -> (string)

The Availability Zone ID of the Capacity Reservation.

InstanceType -> (string)

The type of instance for which the Capacity Reservation reserves capacity.

InstancePlatform -> (string)

The type of operating system for which the Capacity Reservation reserves capacity.

AvailabilityZone -> (string)

The Availability Zone in which the capacity is reserved.

Tenancy -> (string)

Indicates the tenancy of the Capacity Reservation. A Capacity Reservation can have one of the following tenancy settings:

- `default` - The Capacity Reservation is created on hardware that is shared with other Amazon Web Services accounts.
- `dedicated` - The Capacity Reservation is created on single-tenant hardware that is dedicated to a single Amazon Web Services account.

TotalInstanceCount -> (integer)

The total number of instances for which the Capacity Reservation reserves capacity.

AvailableInstanceCount -> (integer)

The remaining capacity. Indicates the number of instances that can be launched in the Capacity Reservation.

EbsOptimized -> (boolean)

Indicates whether the Capacity Reservation supports EBS-optimized instances. This optimization provides dedicated throughput to Amazon EBS and an optimized configuration stack to provide optimal I/O performance. This optimization isnât available with all instance types. Additional usage charges apply when using an EBS- optimized instance.

EphemeralStorage -> (boolean)

*Deprecated.*

State -> (string)

The current state of the Capacity Reservation. A Capacity Reservation can be in one of the following states:

- `active` - The capacity is available for use.
- `expired` - The Capacity Reservation expired automatically at the date and time specified in your reservation request. The reserved capacity is no longer available for your use.
- `cancelled` - The Capacity Reservation was canceled. The reserved capacity is no longer available for your use.
- `pending` - The Capacity Reservation request was successful but the capacity provisioning is still pending.
- `failed` - The Capacity Reservation request has failed. A request can fail due to request parameters that are not valid, capacity constraints, or instance limit constraints. You can view a failed request for 60 minutes.
- `scheduled` - (*Future-dated Capacity Reservations* ) The future-dated Capacity Reservation request was approved and the Capacity Reservation is scheduled for delivery on the requested start date.
- `payment-pending` - (*Capacity Blocks* ) The upfront payment has not been processed yet.
- `payment-failed` - (*Capacity Blocks* ) The upfront payment was not processed in the 12-hour time frame. Your Capacity Block was released.
- `assessing` - (*Future-dated Capacity Reservations* ) Amazon EC2 is assessing your request for a future-dated Capacity Reservation.
- `delayed` - (*Future-dated Capacity Reservations* ) Amazon EC2 encountered a delay in provisioning the requested future-dated Capacity Reservation. Amazon EC2 is unable to deliver the requested capacity by the requested start date and time.
- `unsupported` - (*Future-dated Capacity Reservations* ) Amazon EC2 canât support the future-dated Capacity Reservation request due to capacity constraints. You can view unsupported requests for 30 days. The Capacity Reservation will not be delivered.

StartDate -> (timestamp)

The date and time at which the Capacity Reservation was started.

EndDate -> (timestamp)

The date and time at which the Capacity Reservation expires. When a Capacity Reservation expires, the reserved capacity is released and you can no longer launch instances into it. The Capacity Reservationâs state changes to `expired` when it reaches its end date and time.

EndDateType -> (string)

Indicates the way in which the Capacity Reservation ends. A Capacity Reservation can have one of the following end types:

- `unlimited` - The Capacity Reservation remains active until you explicitly cancel it.
- `limited` - The Capacity Reservation expires automatically at a specified date and time.

InstanceMatchCriteria -> (string)

Indicates the type of instance launches that the Capacity Reservation accepts. The options include:

- `open` - The Capacity Reservation accepts all instances that have matching attributes (instance type, platform, and Availability Zone). Instances that have matching attributes launch into the Capacity Reservation automatically without specifying any additional parameters.
- `targeted` - The Capacity Reservation only accepts instances that have matching attributes (instance type, platform, and Availability Zone), and explicitly target the Capacity Reservation. This ensures that only permitted instances can use the reserved capacity.

CreateDate -> (timestamp)

The date and time at which the Capacity Reservation was created.

Tags -> (list)

Any tags assigned to the Capacity Reservation.

(structure)

Describes a tag.

Key -> (string)

The key of the tag.

Constraints: Tag keys are case-sensitive and accept a maximum of 127 Unicode characters. May not begin with `aws:` .

Value -> (string)

The value of the tag.

Constraints: Tag values are case-sensitive and accept a maximum of 256 Unicode characters.

OutpostArn -> (string)

The Amazon Resource Name (ARN) of the Outpost on which the Capacity Reservation was created.

CapacityReservationFleetId -> (string)

The ID of the Capacity Reservation Fleet to which the Capacity Reservation belongs. Only valid for Capacity Reservations that were created by a Capacity Reservation Fleet.

PlacementGroupArn -> (string)

The Amazon Resource Name (ARN) of the cluster placement group in which the Capacity Reservation was created. For more information, see [Capacity Reservations for cluster placement groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/cr-cpg.html) in the *Amazon EC2 User Guide* .

CapacityAllocations -> (list)

Information about instance capacity usage.

(structure)

Information about instance capacity usage for a Capacity Reservation.

AllocationType -> (string)

The usage type. `used` indicates that the instance capacity is in use by instances that are running in the Capacity Reservation.

Count -> (integer)

The amount of instance capacity associated with the usage. For example a value of `4` indicates that instance capacity for 4 instances is currently in use.

ReservationType -> (string)

The type of Capacity Reservation.

UnusedReservationBillingOwnerId -> (string)

The ID of the Amazon Web Services account to which billing of the unused capacity of the Capacity Reservation is assigned.

CommitmentInfo -> (structure)

Information about your commitment for a future-dated Capacity Reservation.

CommittedInstanceCount -> (integer)

The instance capacity that you committed to when you requested the future-dated Capacity Reservation.

CommitmentEndDate -> (timestamp)

The date and time at which the commitment duration expires, in the ISO8601 format in the UTC time zone (`YYYY-MM-DDThh:mm:ss.sssZ` ). You canât decrease the instance count or cancel the Capacity Reservation before this date and time.

DeliveryPreference -> (string)

The delivery method for a future-dated Capacity Reservation. `incremental` indicates that the requested capacity is delivered in addition to any running instances and reserved capacity that you have in your account at the requested date and time.