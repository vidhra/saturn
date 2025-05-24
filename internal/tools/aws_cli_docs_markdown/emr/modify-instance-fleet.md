# modify-instance-fleetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/modify-instance-fleet.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/modify-instance-fleet.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# modify-instance-fleet

## Description

Modifies the target On-Demand and target Spot capacities for the instance fleet with the specified InstanceFleetID within the cluster specified using ClusterID. The call either succeeds or fails atomically.

### Note

The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ModifyInstanceFleet)

## Synopsis

```
modify-instance-fleet
--cluster-id <value>
--instance-fleet <value>
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

`--cluster-id` (string)

The unique identifier of the cluster.

`--instance-fleet` (structure)

The configuration parameters of the instance fleet.

InstanceFleetId -> (string)

A unique identifier for the instance fleet.

TargetOnDemandCapacity -> (integer)

The target capacity of On-Demand units for the instance fleet. For more information see  InstanceFleetConfig$TargetOnDemandCapacity .

TargetSpotCapacity -> (integer)

The target capacity of Spot units for the instance fleet. For more information, see  InstanceFleetConfig$TargetSpotCapacity .

ResizeSpecifications -> (structure)

The resize specification for the instance fleet.

SpotResizeSpecification -> (structure)

The resize specification for Spot Instances in the instance fleet, which contains the allocation strategy and the resize timeout period.

TimeoutDurationMinutes -> (integer)

Spot resize timeout in minutes. If Spot Instances are not provisioned within this time, the resize workflow will stop provisioning of Spot instances. Minimum value is 5 minutes and maximum value is 10,080 minutes (7 days). The timeout applies to all resize workflows on the Instance Fleet. The resize could be triggered by Amazon EMR Managed Scaling or by the customer (via Amazon EMR Console, Amazon EMR CLI modify-instance-fleet or Amazon EMR SDK ModifyInstanceFleet API) or by Amazon EMR due to Amazon EC2 Spot Reclamation.

AllocationStrategy -> (string)

Specifies the allocation strategy to use to launch Spot instances during a resize. If you run Amazon EMR releases 6.9.0 or higher, the default is `price-capacity-optimized` . If you run Amazon EMR releases 6.8.0 or lower, the default is `capacity-optimized` .

OnDemandResizeSpecification -> (structure)

The resize specification for On-Demand Instances in the instance fleet, which contains the allocation strategy, capacity reservation options, and the resize timeout period.

TimeoutDurationMinutes -> (integer)

On-Demand resize timeout in minutes. If On-Demand Instances are not provisioned within this time, the resize workflow stops. The minimum value is 5 minutes, and the maximum value is 10,080 minutes (7 days). The timeout applies to all resize workflows on the Instance Fleet. The resize could be triggered by Amazon EMR Managed Scaling or by the customer (via Amazon EMR Console, Amazon EMR CLI modify-instance-fleet or Amazon EMR SDK ModifyInstanceFleet API) or by Amazon EMR due to Amazon EC2 Spot Reclamation.

AllocationStrategy -> (string)

Specifies the allocation strategy to use to launch On-Demand instances during a resize. The default is `lowest-price` .

CapacityReservationOptions -> (structure)

Describes the strategy for using unused Capacity Reservations for fulfilling On-Demand capacity.

UsageStrategy -> (string)

Indicates whether to use unused Capacity Reservations for fulfilling On-Demand capacity.

If you specify `use-capacity-reservations-first` , the fleet uses unused Capacity Reservations to fulfill On-Demand capacity up to the target On-Demand capacity. If multiple instance pools have unused Capacity Reservations, the On-Demand allocation strategy (`lowest-price` ) is applied. If the number of unused Capacity Reservations is less than the On-Demand target capacity, the remaining On-Demand target capacity is launched according to the On-Demand allocation strategy (`lowest-price` ).

If you do not specify a value, the fleet fulfills the On-Demand capacity according to the chosen On-Demand allocation strategy.

CapacityReservationPreference -> (string)

Indicates the instanceâs Capacity Reservation preferences. Possible preferences include:

- `open` - The instance can run in any open Capacity Reservation that has matching attributes (instance type, platform, Availability Zone).
- `none` - The instance avoids running in a Capacity Reservation even if one is available. The instance runs as an On-Demand Instance.

CapacityReservationResourceGroupArn -> (string)

The ARN of the Capacity Reservation resource group in which to run the instance.

InstanceTypeConfigs -> (list)

An array of InstanceTypeConfig objects that specify how Amazon EMR provisions Amazon EC2 instances when it fulfills On-Demand and Spot capacities. For more information, see [InstanceTypeConfig](https://docs.aws.amazon.com/emr/latest/APIReference/API_InstanceTypeConfig.html) .

(structure)

An instance type configuration for each instance type in an instance fleet, which determines the Amazon EC2 instances Amazon EMR attempts to provision to fulfill On-Demand and Spot target capacities. When you use an allocation strategy, you can include a maximum of 30 instance type configurations for a fleet. For more information about how to use an allocation strategy, see [Configure Instance Fleets](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-instance-fleet.html) . Without an allocation strategy, you may specify a maximum of five instance type configurations for a fleet.

### Note

The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

InstanceType -> (string)

An Amazon EC2 instance type, such as `m3.xlarge` .

WeightedCapacity -> (integer)

The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in  InstanceFleetConfig . This value is 1 for a master instance fleet, and must be 1 or greater for core and task instance fleets. Defaults to 1 if not specified.

BidPrice -> (string)

The bid price for each Amazon EC2 Spot Instance type as defined by `InstanceType` . Expressed in USD. If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.

BidPriceAsPercentageOfOnDemandPrice -> (double)

The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by `InstanceType` . Expressed as a number (for example, 20 specifies 20%). If neither `BidPrice` nor `BidPriceAsPercentageOfOnDemandPrice` is provided, `BidPriceAsPercentageOfOnDemandPrice` defaults to 100%.

EbsConfiguration -> (structure)

The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by `InstanceType` .

EbsBlockDeviceConfigs -> (list)

An array of Amazon EBS volume specifications attached to a cluster instance.

(structure)

Configuration of requested EBS block device associated with the instance group with count of volumes that are associated to every instance.

VolumeSpecification -> (structure)

EBS volume specifications such as volume type, IOPS, size (GiB) and throughput (MiB/s) that are requested for the EBS volume attached to an Amazon EC2 instance in the cluster.

VolumeType -> (string)

The volume type. Volume types supported are gp3, gp2, io1, st1, sc1, and standard.

Iops -> (integer)

The number of I/O operations per second (IOPS) that the volume supports.

SizeInGB -> (integer)

The volume size, in gibibytes (GiB). This can be a number from 1 - 1024. If the volume type is EBS-optimized, the minimum value is 10.

Throughput -> (integer)

The throughput, in mebibyte per second (MiB/s). This optional parameter can be a number from 125 - 1000 and is valid only for gp3 volumes.

VolumesPerInstance -> (integer)

Number of EBS volumes with a specific volume configuration that are associated with every instance in the instance group

EbsOptimized -> (boolean)

Indicates whether an Amazon EBS volume is EBS-optimized. The default is false. You should explicitly set this value to true to enable the Amazon EBS-optimized setting for an EC2 instance.

Configurations -> (list)

A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software that run on the cluster.

(structure)

### Note

Amazon EMR releases 4.x or later.

An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html) .

Classification -> (string)

The classification within a configuration.

Configurations -> (list)

A list of additional configurations to apply within a configuration object.

(structure)

### Note

Amazon EMR releases 4.x or later.

An optional configuration specification to be used when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR. A configuration consists of a classification, properties, and optional nested configurations. A classification refers to an application-specific configuration file. Properties are the settings you want to change in that file. For more information, see [Configuring Applications](https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-configure-apps.html) .

Classification -> (string)

The classification within a configuration.

Properties -> (map)

A set of properties specified within a configuration classification.

key -> (string)

value -> (string)

Properties -> (map)

A set of properties specified within a configuration classification.

key -> (string)

value -> (string)

CustomAmiId -> (string)

The custom AMI ID to use for the instance type.

Priority -> (double)

The priority at which Amazon EMR launches the Amazon EC2 instances with this instance type. Priority starts at 0, which is the highest priority. Amazon EMR considers the highest priority first.

Context -> (string)

Reserved.

JSON Syntax:

```
{
  "InstanceFleetId": "string",
  "TargetOnDemandCapacity": integer,
  "TargetSpotCapacity": integer,
  "ResizeSpecifications": {
    "SpotResizeSpecification": {
      "TimeoutDurationMinutes": integer,
      "AllocationStrategy": "capacity-optimized"|"price-capacity-optimized"|"lowest-price"|"diversified"|"capacity-optimized-prioritized"
    },
    "OnDemandResizeSpecification": {
      "TimeoutDurationMinutes": integer,
      "AllocationStrategy": "lowest-price"|"prioritized",
      "CapacityReservationOptions": {
        "UsageStrategy": "use-capacity-reservations-first",
        "CapacityReservationPreference": "open"|"none",
        "CapacityReservationResourceGroupArn": "string"
      }
    }
  },
  "InstanceTypeConfigs": [
    {
      "InstanceType": "string",
      "WeightedCapacity": integer,
      "BidPrice": "string",
      "BidPriceAsPercentageOfOnDemandPrice": double,
      "EbsConfiguration": {
        "EbsBlockDeviceConfigs": [
          {
            "VolumeSpecification": {
              "VolumeType": "string",
              "Iops": integer,
              "SizeInGB": integer,
              "Throughput": integer
            },
            "VolumesPerInstance": integer
          }
          ...
        ],
        "EbsOptimized": true|false
      },
      "Configurations": [
        {
          "Classification": "string",
          "Configurations": [
            {
              "Classification": "string",
              "Configurations": ,
              "Properties": {"string": "string"
                ...}
            }
            ...
          ],
          "Properties": {"string": "string"
            ...}
        }
        ...
      ],
      "CustomAmiId": "string",
      "Priority": double
    }
    ...
  ],
  "Context": "string"
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

**To change the target capacites of an instance fleet**

This example changes the On-Demand and Spot target capacities to 1 for the instance fleet specified.

Command:

```
aws emr modify-instance-fleet --cluster-id 'j-12ABCDEFGHI34JK' --instance-fleet InstanceFleetId='if-2ABC4DEFGHIJ4',TargetOnDemandCapacity=1,TargetSpotCapacity=1
```

## Output

None