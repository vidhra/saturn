# list-instance-fleetsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-instance-fleets.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/list-instance-fleets.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [emr](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/emr/index.html#cli-aws-emr) ]

# list-instance-fleets

## Description

Lists all available details about the instance fleets in a cluster.

### Note

The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/elasticmapreduce-2009-03-31/ListInstanceFleets)

`list-instance-fleets` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `InstanceFleets`

## Synopsis

```
list-instance-fleets
--cluster-id <value>
[--cli-input-json | --cli-input-yaml]
[--starting-token <value>]
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

`--cluster-id` (string)

The unique identifier of the cluster.

`--cli-input-json` | `--cli-input-yaml` (string)
Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--starting-token` (string)

A token to specify where to start paginating. This is the `NextToken` from a previously truncated response.

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

**To get configuration details of instance fleets in a cluster**

This example lists the details of instance fleets in the cluster specified.

Command:

```
list-instance-fleets --cluster-id 'j-12ABCDEFGHI34JK'
```

Output:

```
{
  "InstanceFleets": [
      {
          "Status": {
              "Timeline": {
                  "ReadyDateTime": 1488759094.637,
                  "CreationDateTime": 1488758719.817
              },
              "State": "RUNNING",
              "StateChangeReason": {
                  "Message": ""
              }
          },
          "ProvisionedSpotCapacity": 6,
          "Name": "CORE",
          "InstanceFleetType": "CORE",
          "LaunchSpecifications": {
              "SpotSpecification": {
                  "TimeoutDurationMinutes": 60,
                  "TimeoutAction": "TERMINATE_CLUSTER"
              }
          },
          "ProvisionedOnDemandCapacity": 2,
          "InstanceTypeSpecifications": [
              {
                  "BidPrice": "0.5",
                  "InstanceType": "m3.xlarge",
                  "WeightedCapacity": 2
              }
          ],
          "Id": "if-1ABC2DEFGHIJ3"
      },
      {
          "Status": {
              "Timeline": {
                  "ReadyDateTime": 1488759058.598,
                  "CreationDateTime": 1488758719.811
              },
              "State": "RUNNING",
              "StateChangeReason": {
                  "Message": ""
              }
          },
          "ProvisionedSpotCapacity": 0,
          "Name": "MASTER",
          "InstanceFleetType": "MASTER",
          "ProvisionedOnDemandCapacity": 1,
          "InstanceTypeSpecifications": [
              {
                  "BidPriceAsPercentageOfOnDemandPrice": 100.0,
                  "InstanceType": "m3.xlarge",
                  "WeightedCapacity": 1
              }
          ],
         "Id": "if-2ABC4DEFGHIJ4"
      }
  ]
}
```

## Output

InstanceFleets -> (list)

The list of instance fleets for the cluster and given filters.

(structure)

Describes an instance fleet, which is a group of Amazon EC2 instances that host a particular node type (master, core, or task) in an Amazon EMR cluster. Instance fleets can consist of a mix of instance types and On-Demand and Spot Instances, which are provisioned to meet a defined target capacity.

### Note

The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

Id -> (string)

The unique identifier of the instance fleet.

Name -> (string)

A friendly name for the instance fleet.

Status -> (structure)

The current status of the instance fleet.

State -> (string)

A code representing the instance fleet status.

- `PROVISIONING` âThe instance fleet is provisioning Amazon EC2 resources and is not yet ready to run jobs.
- `BOOTSTRAPPING` âAmazon EC2 instances and other resources have been provisioned and the bootstrap actions specified for the instances are underway.
- `RUNNING` âAmazon EC2 instances and other resources are running. They are either executing jobs or waiting to execute jobs.
- `RESIZING` âA resize operation is underway. Amazon EC2 instances are either being added or removed.
- `SUSPENDED` âA resize operation could not complete. Existing Amazon EC2 instances are running, but instances canât be added or removed.
- `TERMINATING` âThe instance fleet is terminating Amazon EC2 instances.
- `TERMINATED` âThe instance fleet is no longer active, and all Amazon EC2 instances have been terminated.

StateChangeReason -> (structure)

Provides status change reason details for the instance fleet.

Code -> (string)

A code corresponding to the reason the state change occurred.

Message -> (string)

An explanatory message.

Timeline -> (structure)

Provides historical timestamps for the instance fleet, including the time of creation, the time it became ready to run jobs, and the time of termination.

CreationDateTime -> (timestamp)

The time and date the instance fleet was created.

ReadyDateTime -> (timestamp)

The time and date the instance fleet was ready to run jobs.

EndDateTime -> (timestamp)

The time and date the instance fleet terminated.

InstanceFleetType -> (string)

The node type that the instance fleet hosts. Valid values are MASTER, CORE, or TASK.

TargetOnDemandCapacity -> (integer)

The target capacity of On-Demand units for the instance fleet, which determines how many On-Demand Instances to provision. When the instance fleet launches, Amazon EMR tries to provision On-Demand Instances as specified by  InstanceTypeConfig . Each instance configuration has a specified `WeightedCapacity` . When an On-Demand Instance is provisioned, the `WeightedCapacity` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a `WeightedCapacity` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. You can use  InstanceFleet$ProvisionedOnDemandCapacity to determine the Spot capacity units that have been provisioned for the instance fleet.

### Note

If not specified or set to 0, only Spot Instances are provisioned for the instance fleet using `TargetSpotCapacity` . At least one of `TargetSpotCapacity` and `TargetOnDemandCapacity` should be greater than 0. For a master instance fleet, only one of `TargetSpotCapacity` and `TargetOnDemandCapacity` can be specified, and its value must be 1.

TargetSpotCapacity -> (integer)

The target capacity of Spot units for the instance fleet, which determines how many Spot Instances to provision. When the instance fleet launches, Amazon EMR tries to provision Spot Instances as specified by  InstanceTypeConfig . Each instance configuration has a specified `WeightedCapacity` . When a Spot instance is provisioned, the `WeightedCapacity` units count toward the target capacity. Amazon EMR provisions instances until the target capacity is totally fulfilled, even if this results in an overage. For example, if there are 2 units remaining to fulfill capacity, and Amazon EMR can only provision an instance with a `WeightedCapacity` of 5 units, the instance is provisioned, and the target capacity is exceeded by 3 units. You can use  InstanceFleet$ProvisionedSpotCapacity to determine the Spot capacity units that have been provisioned for the instance fleet.

### Note

If not specified or set to 0, only On-Demand Instances are provisioned for the instance fleet. At least one of `TargetSpotCapacity` and `TargetOnDemandCapacity` should be greater than 0. For a master instance fleet, only one of `TargetSpotCapacity` and `TargetOnDemandCapacity` can be specified, and its value must be 1.

ProvisionedOnDemandCapacity -> (integer)

The number of On-Demand units that have been provisioned for the instance fleet to fulfill `TargetOnDemandCapacity` . This provisioned capacity might be less than or greater than `TargetOnDemandCapacity` .

ProvisionedSpotCapacity -> (integer)

The number of Spot units that have been provisioned for this instance fleet to fulfill `TargetSpotCapacity` . This provisioned capacity might be less than or greater than `TargetSpotCapacity` .

InstanceTypeSpecifications -> (list)

An array of specifications for the instance types that comprise an instance fleet.

(structure)

The configuration specification for each instance type in an instance fleet.

### Note

The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

InstanceType -> (string)

The Amazon EC2 instance type, for example `m3.xlarge` .

WeightedCapacity -> (integer)

The number of units that a provisioned instance of this type provides toward fulfilling the target capacities defined in  InstanceFleetConfig . Capacity values represent performance characteristics such as vCPUs, memory, or I/O. If not specified, the default value is 1.

BidPrice -> (string)

The bid price for each Amazon EC2 Spot Instance type as defined by `InstanceType` . Expressed in USD.

BidPriceAsPercentageOfOnDemandPrice -> (double)

The bid price, as a percentage of On-Demand price, for each Amazon EC2 Spot Instance as defined by `InstanceType` . Expressed as a number (for example, 20 specifies 20%).

Configurations -> (list)

A configuration classification that applies when provisioning cluster instances, which can include configurations for applications and software bundled with Amazon EMR.

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

EbsBlockDevices -> (list)

The configuration of Amazon Elastic Block Store (Amazon EBS) attached to each instance as defined by `InstanceType` .

(structure)

Configuration of requested EBS block device associated with the instance group.

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

Device -> (string)

The device name that is exposed to the instance, such as /dev/sdh.

EbsOptimized -> (boolean)

Evaluates to `TRUE` when the specified `InstanceType` is EBS-optimized.

CustomAmiId -> (string)

The custom AMI ID to use for the instance type.

Priority -> (double)

The priority at which Amazon EMR launches the Amazon EC2 instances with this instance type. Priority starts at 0, which is the highest priority. Amazon EMR considers the highest priority first.

LaunchSpecifications -> (structure)

Describes the launch specification for an instance fleet.

SpotSpecification -> (structure)

The launch specification for Spot instances in the fleet, which determines the allocation strategy, defined duration, and provisioning timeout behavior.

TimeoutDurationMinutes -> (integer)

The Spot provisioning timeout period in minutes. If Spot Instances are not provisioned within this time period, the `TimeOutAction` is taken. Minimum value is 5 and maximum value is 1440. The timeout applies only during initial provisioning, when the cluster is first created.

TimeoutAction -> (string)

The action to take when `TargetSpotCapacity` has not been fulfilled when the `TimeoutDurationMinutes` has expired; that is, when all Spot Instances could not be provisioned within the Spot provisioning timeout. Valid values are `TERMINATE_CLUSTER` and `SWITCH_TO_ON_DEMAND` . SWITCH_TO_ON_DEMAND specifies that if no Spot Instances are available, On-Demand Instances should be provisioned to fulfill any remaining Spot capacity.

BlockDurationMinutes -> (integer)

The defined duration for Spot Instances (also known as Spot blocks) in minutes. When specified, the Spot Instance does not terminate before the defined duration expires, and defined duration pricing for Spot Instances applies. Valid values are 60, 120, 180, 240, 300, or 360. The duration period starts as soon as a Spot Instance receives its instance ID. At the end of the duration, Amazon EC2 marks the Spot Instance for termination and provides a Spot Instance termination notice, which gives the instance a two-minute warning before it terminates.

### Note

Spot Instances with a defined duration (also known as Spot blocks) are no longer available to new customers from July 1, 2021. For customers who have previously used the feature, we will continue to support Spot Instances with a defined duration until December 31, 2022.

AllocationStrategy -> (string)

Specifies one of the following strategies to launch Spot Instance fleets: `capacity-optimized` , `price-capacity-optimized` , `lowest-price` , or `diversified` , and `capacity-optimized-prioritized` . For more information on the provisioning strategies, see [Allocation strategies for Spot Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-allocation-strategy.html) in the *Amazon EC2 User Guide for Linux Instances* .

### Note

When you launch a Spot Instance fleet with the old console, it automatically launches with the `capacity-optimized` strategy. You canât change the allocation strategy from the old console.

OnDemandSpecification -> (structure)

The launch specification for On-Demand Instances in the instance fleet, which determines the allocation strategy and capacity reservation options.

### Note

The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions. On-Demand Instances allocation strategy is available in Amazon EMR releases 5.12.1 and later.

AllocationStrategy -> (string)

Specifies the strategy to use in launching On-Demand instance fleets. Available options are `lowest-price` and `prioritized` . `lowest-price` specifies to launch the instances with the lowest price first, and `prioritized` specifies that Amazon EMR should launch the instances with the highest priority first. The default is `lowest-price` .

CapacityReservationOptions -> (structure)

The launch specification for On-Demand instances in the instance fleet, which determines the allocation strategy.

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

Context -> (string)

Reserved.

Marker -> (string)

The pagination token that indicates the next set of results to retrieve.