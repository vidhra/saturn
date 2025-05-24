# get-spot-placement-scoresÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-spot-placement-scores.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/get-spot-placement-scores.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# get-spot-placement-scores

## Description

Calculates the Spot placement score for a Region or Availability Zone based on the specified target capacity and compute requirements.

You can specify your compute requirements either by using `InstanceRequirementsWithMetadata` and letting Amazon EC2 choose the optimal instance types to fulfill your Spot request, or you can specify the instance types by using `InstanceTypes` .

For more information, see [Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html) in the *Amazon EC2 User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/GetSpotPlacementScores)

`get-spot-placement-scores` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `SpotPlacementScores`

## Synopsis

```
get-spot-placement-scores
[--instance-types <value>]
--target-capacity <value>
[--target-capacity-unit-type <value>]
[--single-availability-zone | --no-single-availability-zone]
[--region-names <value>]
[--instance-requirements-with-metadata <value>]
[--dry-run | --no-dry-run]
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

`--instance-types` (list)

The instance types. We recommend that you specify at least three instance types. If you specify one or two instance types, or specify variations of a single instance type (for example, an `m3.xlarge` with and without instance storage), the returned placement score will always be low.

If you specify `InstanceTypes` , you canât specify `InstanceRequirementsWithMetadata` .

(string)

Syntax:

```
"string" "string" ...
```

`--target-capacity` (integer)

The target capacity.

`--target-capacity-unit-type` (string)

The unit for the target capacity.

Possible values:

- `vcpu`
- `memory-mib`
- `units`

`--single-availability-zone` | `--no-single-availability-zone` (boolean)

Specify `true` so that the response returns a list of scored Availability Zones. Otherwise, the response returns a list of scored Regions.

A list of scored Availability Zones is useful if you want to launch all of your Spot capacity into a single Availability Zone.

`--region-names` (list)

The Regions used to narrow down the list of Regions to be scored. Enter the Region code, for example, `us-east-1` .

(string)

Syntax:

```
"string" "string" ...
```

`--instance-requirements-with-metadata` (structure)

The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.

If you specify `InstanceRequirementsWithMetadata` , you canât specify `InstanceTypes` .

ArchitectureTypes -> (list)

The architecture type.

(string)

VirtualizationTypes -> (list)

The virtualization type.

(string)

InstanceRequirements -> (structure)

The attributes for the instance types. When you specify instance attributes, Amazon EC2 will identify instance types with those attributes.

VCpuCount -> (structure)

The minimum and maximum number of vCPUs.

Min -> (integer)

The minimum number of vCPUs. To specify no minimum limit, specify `0` .

Max -> (integer)

The maximum number of vCPUs. To specify no maximum limit, omit this parameter.

MemoryMiB -> (structure)

The minimum and maximum amount of memory, in MiB.

Min -> (integer)

The minimum amount of memory, in MiB. To specify no minimum limit, specify `0` .

Max -> (integer)

The maximum amount of memory, in MiB. To specify no maximum limit, omit this parameter.

CpuManufacturers -> (list)

The CPU manufacturers to include.

- For instance types with Intel CPUs, specify `intel` .
- For instance types with AMD CPUs, specify `amd` .
- For instance types with Amazon Web Services CPUs, specify `amazon-web-services` .
- For instance types with Apple CPUs, specify `apple` .

### Note

Donât confuse the CPU manufacturer with the CPU architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.

Default: Any manufacturer

(string)

MemoryGiBPerVCpu -> (structure)

The minimum and maximum amount of memory per vCPU, in GiB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of memory per vCPU, in GiB. To specify no minimum limit, omit this parameter.

Max -> (double)

The maximum amount of memory per vCPU, in GiB. To specify no maximum limit, omit this parameter.

ExcludedInstanceTypes -> (list)

The instance types to exclude.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to exclude an instance family, type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will exclude the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will exclude all the M5a instance types, but not the M5n instance types.

### Note

If you specify `ExcludedInstanceTypes` , you canât specify `AllowedInstanceTypes` .

Default: No excluded instance types

(string)

InstanceGenerations -> (list)

Indicates whether current or previous generation instance types are included. The current generation instance types are recommended for use. Current generation instance types are typically the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide* .

For current generation instance types, specify `current` .

For previous generation instance types, specify `previous` .

Default: Current and previous generation instance types

(string)

SpotMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the Spot price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified Spot price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose Spot price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

Default: `100`

OnDemandMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

To indicate no price protection threshold, specify a high value, such as `999999` .

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) and [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements.html) .

### Note

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per-instance price.

Default: `20`

BareMetal -> (string)

Indicates whether bare metal instance types must be included, excluded, or required.

- To include bare metal instance types, specify `included` .
- To require only bare metal instance types, specify `required` .
- To exclude bare metal instance types, specify `excluded` .

Default: `excluded`

BurstablePerformance -> (string)

Indicates whether burstable performance T instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) .

- To include burstable performance instance types, specify `included` .
- To require only burstable performance instance types, specify `required` .
- To exclude burstable performance instance types, specify `excluded` .

Default: `excluded`

RequireHibernateSupport -> (boolean)

Indicates whether instance types must support hibernation for On-Demand Instances.

This parameter is not supported for [GetSpotPlacementScores](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetSpotPlacementScores.html) .

Default: `false`

NetworkInterfaceCount -> (structure)

The minimum and maximum number of network interfaces.

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of network interfaces. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum number of network interfaces. To specify no maximum limit, omit this parameter.

LocalStorage -> (string)

Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide* .

- To include instance types with instance store volumes, specify `included` .
- To require only instance types with instance store volumes, specify `required` .
- To exclude instance types with instance store volumes, specify `excluded` .

Default: `included`

LocalStorageTypes -> (list)

The type of local storage that is required.

- For instance types with hard disk drive (HDD) storage, specify `hdd` .
- For instance types with solid state drive (SSD) storage, specify `ssd` .

Default: `hdd` and `ssd`

(string)

TotalLocalStorageGB -> (structure)

The minimum and maximum amount of total local storage, in GB.

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of total local storage, in GB. To specify no minimum limit, omit this parameter.

Max -> (double)

The maximum amount of total local storage, in GB. To specify no maximum limit, omit this parameter.

BaselineEbsBandwidthMbps -> (structure)

The minimum and maximum baseline bandwidth to Amazon EBS, in Mbps. For more information, see [Amazon EBSâoptimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide* .

Default: No minimum or maximum limits

Min -> (integer)

The minimum baseline bandwidth, in Mbps. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum baseline bandwidth, in Mbps. To specify no maximum limit, omit this parameter.

AcceleratorTypes -> (list)

The accelerator types that must be on the instance type.

- For instance types with FPGA accelerators, specify `fpga` .
- For instance types with GPU accelerators, specify `gpu` .
- For instance types with Inference accelerators, specify `inference` .

Default: Any accelerator type

(string)

AcceleratorCount -> (structure)

The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) on an instance.

To exclude accelerator-enabled instance types, set `Max` to `0` .

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of accelerators. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum number of accelerators. To specify no maximum limit, omit this parameter. To exclude accelerator-enabled instance types, set `Max` to `0` .

AcceleratorManufacturers -> (list)

Indicates whether instance types must have accelerators by specific manufacturers.

- For instance types with Amazon Web Services devices, specify `amazon-web-services` .
- For instance types with AMD devices, specify `amd` .
- For instance types with Habana devices, specify `habana` .
- For instance types with NVIDIA devices, specify `nvidia` .
- For instance types with Xilinx devices, specify `xilinx` .

Default: Any manufacturer

(string)

AcceleratorNames -> (list)

The accelerators that must be on the instance type.

- For instance types with NVIDIA A10G GPUs, specify `a10g` .
- For instance types with NVIDIA A100 GPUs, specify `a100` .
- For instance types with NVIDIA H100 GPUs, specify `h100` .
- For instance types with Amazon Web Services Inferentia chips, specify `inferentia` .
- For instance types with NVIDIA GRID K520 GPUs, specify `k520` .
- For instance types with NVIDIA K80 GPUs, specify `k80` .
- For instance types with NVIDIA M60 GPUs, specify `m60` .
- For instance types with AMD Radeon Pro V520 GPUs, specify `radeon-pro-v520` .
- For instance types with NVIDIA T4 GPUs, specify `t4` .
- For instance types with NVIDIA T4G GPUs, specify `t4g` .
- For instance types with Xilinx VU9P FPGAs, specify `vu9p` .
- For instance types with NVIDIA V100 GPUs, specify `v100` .

Default: Any accelerator

(string)

AcceleratorTotalMemoryMiB -> (structure)

The minimum and maximum amount of total accelerator memory, in MiB.

Default: No minimum or maximum limits

Min -> (integer)

The minimum amount of accelerator memory, in MiB. To specify no minimum limit, omit this parameter.

Max -> (integer)

The maximum amount of accelerator memory, in MiB. To specify no maximum limit, omit this parameter.

NetworkBandwidthGbps -> (structure)

The minimum and maximum amount of baseline network bandwidth, in gigabits per second (Gbps). For more information, see [Amazon EC2 instance network bandwidth](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instance-network-bandwidth.html) in the *Amazon EC2 User Guide* .

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of network bandwidth, in Gbps. To specify no minimum limit, omit this parameter.

Max -> (double)

The maximum amount of network bandwidth, in Gbps. To specify no maximum limit, omit this parameter.

AllowedInstanceTypes -> (list)

The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` ,Amazon EC2 will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 will allow all the M5a instance types, but not the M5n instance types.

### Note

If you specify `AllowedInstanceTypes` , you canât specify `ExcludedInstanceTypes` .

Default: All instance types

(string)

MaxSpotPriceAsPercentageOfOptimalOnDemandPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from the lowest priced current generation instance types, and failing that, from the lowest priced previous generation instance types that match your attributes. When Amazon EC2 selects instance types with your attributes, it will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 interprets as a percentage.

If you set `TargetCapacityUnitType` to `vcpu` or `memory-mib` , the price protection threshold is based on the per vCPU or per memory price instead of the per instance price.

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

BaselinePerformanceFactors -> (structure)

The baseline performance to consider, using an instance family as a baseline reference. The instance family establishes the lowest acceptable level of performance. Amazon EC2 uses this baseline to guide instance type selection, but there is no guarantee that the selected instance types will always exceed the baseline for every application. Currently, this parameter only supports CPU performance as a baseline performance factor. For more information, see [Performance protection](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-fleet-attribute-based-instance-type-selection.html#ec2fleet-abis-performance-protection) in the *Amazon EC2 User Guide* .

Cpu -> (structure)

The CPU performance to consider, using an instance family as the baseline reference.

References -> (list)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.

### Note

Currently, only one instance family can be specified in the list.

(structure)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture.

### Note

Currently, only one instance family can be specified in the list.

InstanceFamily -> (string)

The instance family to use as a baseline reference.

### Note

Ensure that you specify the correct value for the instance family. The instance family is everything before the period (`.` ) in the instance type name. For example, in the instance type `c6i.large` , the instance family is `c6i` , not `c6` . For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html) in *Amazon EC2 Instance Types* .

The following instance families are *not supported* for performance protection:

- `c1`
- `g3` | `g3s`
- `hpc7g`
- `m1` | `m2`
- `mac1` | `mac2` | `mac2-m1ultra` | `mac2-m2` | `mac2-m2pro`
- `p3dn` | `p4d` | `p5`
- `t1`
- `u-12tb1` | `u-18tb1` | `u-24tb1` | `u-3tb1` | `u-6tb1` | `u-9tb1` | `u7i-12tb` | `u7in-16tb` | `u7in-24tb` | `u7in-32tb`

If you enable performance protection by specifying a supported instance family, the returned instance types will exclude the above unsupported instance families.

If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response for [GetInstanceTypesFromInstanceRequirements](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetInstanceTypesFromInstanceRequirements) and an exception for [CreateFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateFleet) , [RequestSpotFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RequestSpotFleet) , [ModifyFleet](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyFleet) , and [ModifySpotFleetRequest](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifySpotFleetRequest) .

JSON Syntax:

```
{
  "ArchitectureTypes": ["i386"|"x86_64"|"arm64"|"x86_64_mac"|"arm64_mac", ...],
  "VirtualizationTypes": ["hvm"|"paravirtual", ...],
  "InstanceRequirements": {
    "VCpuCount": {
      "Min": integer,
      "Max": integer
    },
    "MemoryMiB": {
      "Min": integer,
      "Max": integer
    },
    "CpuManufacturers": ["intel"|"amd"|"amazon-web-services"|"apple", ...],
    "MemoryGiBPerVCpu": {
      "Min": double,
      "Max": double
    },
    "ExcludedInstanceTypes": ["string", ...],
    "InstanceGenerations": ["current"|"previous", ...],
    "SpotMaxPricePercentageOverLowestPrice": integer,
    "OnDemandMaxPricePercentageOverLowestPrice": integer,
    "BareMetal": "included"|"required"|"excluded",
    "BurstablePerformance": "included"|"required"|"excluded",
    "RequireHibernateSupport": true|false,
    "NetworkInterfaceCount": {
      "Min": integer,
      "Max": integer
    },
    "LocalStorage": "included"|"required"|"excluded",
    "LocalStorageTypes": ["hdd"|"ssd", ...],
    "TotalLocalStorageGB": {
      "Min": double,
      "Max": double
    },
    "BaselineEbsBandwidthMbps": {
      "Min": integer,
      "Max": integer
    },
    "AcceleratorTypes": ["gpu"|"fpga"|"inference", ...],
    "AcceleratorCount": {
      "Min": integer,
      "Max": integer
    },
    "AcceleratorManufacturers": ["amazon-web-services"|"amd"|"nvidia"|"xilinx"|"habana", ...],
    "AcceleratorNames": ["a100"|"inferentia"|"k520"|"k80"|"m60"|"radeon-pro-v520"|"t4"|"vu9p"|"v100"|"a10g"|"h100"|"t4g", ...],
    "AcceleratorTotalMemoryMiB": {
      "Min": integer,
      "Max": integer
    },
    "NetworkBandwidthGbps": {
      "Min": double,
      "Max": double
    },
    "AllowedInstanceTypes": ["string", ...],
    "MaxSpotPriceAsPercentageOfOptimalOnDemandPrice": integer,
    "BaselinePerformanceFactors": {
      "Cpu": {
        "References": [
          {
            "InstanceFamily": "string"
          }
          ...
        ]
      }
    }
  }
}
```

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

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

**To calculate the Spot placement score for specified requirements**

The following `get-spot-placement-scores` example first generates a list of all of the possible parameters that can be specified for the Spot placement score configuration using the `--generate-cli-skeleton` parameter, and saves the list to a JSON file. Then, the JSON file is used to configure the requirements to use to calculate the Spot placement score.

To generate all possible parameters that can be specified for the Spot placement score configuration, and save the output directly to a JSON file.

```
aws ec2 get-spot-placement-scores \
    --region us-east-1 \
    --generate-cli-skeleton input > attributes.json
```

Output:

```
{
    "InstanceTypes": [
        ""
    ],
    "TargetCapacity": 0,
    "TargetCapacityUnitType": "vcpu",
    "SingleAvailabilityZone": true,
    "RegionNames": [
        ""
    ],
    "InstanceRequirementsWithMetadata": {
        "ArchitectureTypes": [
            "x86_64_mac"
        ],
        "VirtualizationTypes": [
            "hvm"
        ],
        "InstanceRequirements": {
            "VCpuCount": {
                "Min": 0,
                "Max": 0
            },
            "MemoryMiB": {
                "Min": 0,
                "Max": 0
            },
            "CpuManufacturers": [
                "amd"
            ],
            "MemoryGiBPerVCpu": {
                "Min": 0.0,
                "Max": 0.0
            },
            "ExcludedInstanceTypes": [
                ""
            ],
            "InstanceGenerations": [
                "previous"
            ],
            "SpotMaxPricePercentageOverLowestPrice": 0,
            "OnDemandMaxPricePercentageOverLowestPrice": 0,
            "BareMetal": "excluded",
            "BurstablePerformance": "excluded",
            "RequireHibernateSupport": true,
            "NetworkInterfaceCount": {
                "Min": 0,
                "Max": 0
            },
            "LocalStorage": "included",
            "LocalStorageTypes": [
                "hdd"
            ],
            "TotalLocalStorageGB": {
                "Min": 0.0,
                "Max": 0.0
            },
            "BaselineEbsBandwidthMbps": {
                "Min": 0,
                "Max": 0
            },
            "AcceleratorTypes": [
                "fpga"
            ],
            "AcceleratorCount": {
                "Min": 0,
                "Max": 0
            },
            "AcceleratorManufacturers": [
                "amd"
            ],
            "AcceleratorNames": [
                "vu9p"
            ],
            "AcceleratorTotalMemoryMiB": {
                "Min": 0,
                "Max": 0
            }
        }
    },
    "DryRun": true,
    "MaxResults": 0,
    "NextToken": ""
}
```

Configure the JSON file. You must provide a value for `TargetCapacity`. For a description of each parameter and their default values, see Calculate the Spot placement score (AWS CLI) <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html#calculate-sps-cli>.

Calculate the Spot placement score for the requirements specified in `attributes.json`. Specify the name and path to your JSON file by using the `--cli-input-json` parameter.

```
aws ec2 get-spot-placement-scores \
    --region us-east-1 \
    --cli-input-json file://attributes.json
```

Output if `SingleAvailabilityZone` is set to `false` or omitted (if omitted, it defaults to `false`). A scored list of Regions is returned.

```
"Recommendation": [
    {
        "Region": "us-east-1",
        "Score": 7
    },
    {
        "Region": "us-west-1",
        "Score": 5
    },
   ...
```

Output if `SingleAvailabilityZone` is set to `true`. A scored list of SingleAvailability Zones is returned.

```
"Recommendation": [
    {
        "Region": "us-east-1",
        "AvailabilityZoneId": "use1-az1"
        "Score": 8
    },
    {
        "Region": "us-east-1",
        "AvailabilityZoneId": "usw2-az3"
        "Score": 6
    },
   ...
```

For more information about calculating a Spot placement score, and for example configurations, see [Calculate a Spot placement score](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-placement-score.html#work-with-spot-placement-score) in the *Amazon EC2 User Guide*.

## Output

SpotPlacementScores -> (list)

The Spot placement score for the top 10 Regions or Availability Zones, scored on a scale from 1 to 10. Each score reflects how likely it is that each Region or Availability Zone will succeed at fulfilling the specified target capacity *at the time of the Spot placement score request* . A score of `10` means that your Spot capacity request is highly likely to succeed in that Region or Availability Zone.

If you request a Spot placement score for Regions, a high score assumes that your fleet request will be configured to use all Availability Zones and the `capacity-optimized` allocation strategy. If you request a Spot placement score for Availability Zones, a high score assumes that your fleet request will be configured to use a single Availability Zone and the `capacity-optimized` allocation strategy.

Different Regions or Availability Zones might return the same score.

### Note

The Spot placement score serves as a recommendation only. No score guarantees that your Spot request will be fully or partially fulfilled.

(structure)

The Spot placement score for this Region or Availability Zone. The score is calculated based on the assumption that the `capacity-optimized` allocation strategy is used and that all of the Availability Zones in the Region can be used.

Region -> (string)

The Region.

AvailabilityZoneId -> (string)

The Availability Zone.

Score -> (integer)

The placement score, on a scale from `1` to `10` . A score of `10` indicates that your Spot request is highly likely to succeed in this Region or Availability Zone. A score of `1` indicates that your Spot request is not likely to succeed.

NextToken -> (string)

The token to include in another request to get the next page of items. This value is `null` when there are no more items to return.