# get-fleetÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/get-fleet.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/get-fleet.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [deadline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deadline/index.html#cli-aws-deadline) ]

# get-fleet

## Description

Get a fleet.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/deadline-2023-10-12/GetFleet)

## Synopsis

```
get-fleet
--farm-id <value>
--fleet-id <value>
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

`--farm-id` (string)

The farm ID of the farm in the fleet.

`--fleet-id` (string)

The fleet ID of the fleet to get.

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

fleetId -> (string)

The fleet ID.

farmId -> (string)

The farm ID of the farm in the fleet.

displayName -> (string)

The display name of the fleet.

### Warning

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.

description -> (string)

The description of the fleet.

### Warning

This field can store any content. Escape or encode this content before displaying it on a webpage or any other system that might interpret the content of this field.

status -> (string)

The Auto Scaling status of the fleet.

autoScalingStatus -> (string)

The Auto Scaling status of the fleet. Either `GROWING` , `STEADY` , or `SHRINKING` .

targetWorkerCount -> (integer)

The number of target workers in the fleet.

workerCount -> (integer)

The number of workers in the fleet.

minWorkerCount -> (integer)

The minimum number of workers specified in the fleet.

maxWorkerCount -> (integer)

The maximum number of workers specified in the fleet.

configuration -> (tagged union structure)

The configuration setting for the fleet.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `customerManaged`, `serviceManagedEc2`.

customerManaged -> (structure)

The customer managed fleets within a fleet configuration.

mode -> (string)

The Auto Scaling mode for the customer managed fleet configuration.

workerCapabilities -> (structure)

The worker capabilities for a customer managed fleet configuration.

vCpuCount -> (structure)

The vCPU count for the customer manged worker capabilities.

min -> (integer)

The minimum amount of vCPU.

max -> (integer)

The maximum amount of vCPU.

memoryMiB -> (structure)

The memory (MiB).

min -> (integer)

The minimum amount of memory (in MiB).

max -> (integer)

The maximum amount of memory (in MiB).

acceleratorTypes -> (list)

The accelerator types for the customer managed worker capabilities.

(string)

acceleratorCount -> (structure)

The range of the accelerator.

min -> (integer)

The minimum number of GPU accelerators in the worker host.

max -> (integer)

The maximum number of GPU accelerators in the worker host.

acceleratorTotalMemoryMiB -> (structure)

The total memory (MiB) for the customer managed worker capabilities.

min -> (integer)

The minimum amount of memory to use for the accelerator, measured in MiB.

max -> (integer)

The maximum amount of memory to use for the accelerator, measured in MiB.

osFamily -> (string)

The operating system (OS) family.

cpuArchitectureType -> (string)

The CPU architecture type for the customer managed worker capabilities.

customAmounts -> (list)

Custom requirement ranges for customer managed worker capabilities.

(structure)

The fleet amount and attribute capabilities.

name -> (string)

The name of the fleet capability.

min -> (float)

The minimum amount of fleet worker capability.

max -> (float)

The maximum amount of the fleet worker capability.

customAttributes -> (list)

Custom attributes for the customer manged worker capabilities.

(structure)

Defines the fleetâs capability name, minimum, and maximum.

name -> (string)

The name of the fleet attribute capability for the worker.

values -> (list)

The number of fleet attribute capabilities.

(string)

storageProfileId -> (string)

The storage profile ID.

tagPropagationMode -> (string)

Specifies whether tags associated with a fleet are attached to workers when the worker is launched.

When the `tagPropagationMode` is set to `PROPAGATE_TAGS_TO_WORKERS_AT_LAUNCH` any tag associated with a fleet is attached to workers when they launch. If the tags for a fleet change, the tags associated with running workers **do not** change.

If you donât specify `tagPropagationMode` , the default is `NO_PROPAGATION` .

serviceManagedEc2 -> (structure)

The service managed Amazon EC2 instances for a fleet configuration.

instanceCapabilities -> (structure)

The Amazon EC2 instance capabilities.

vCpuCount -> (structure)

The amount of vCPU to require for instances in this fleet.

min -> (integer)

The minimum amount of vCPU.

max -> (integer)

The maximum amount of vCPU.

memoryMiB -> (structure)

The memory, as MiB, for the Amazon EC2 instance type.

min -> (integer)

The minimum amount of memory (in MiB).

max -> (integer)

The maximum amount of memory (in MiB).

osFamily -> (string)

The operating system (OS) family.

cpuArchitectureType -> (string)

The CPU architecture type.

rootEbsVolume -> (structure)

The root EBS volume.

sizeGiB -> (integer)

The EBS volume size in GiB.

iops -> (integer)

The IOPS per volume.

throughputMiB -> (integer)

The throughput per volume in MiB.

acceleratorCapabilities -> (structure)

Describes the GPU accelerator capabilities required for worker host instances in this fleet.

selections -> (list)

A list of accelerator capabilities requested for this fleet. Only Amazon Elastic Compute Cloud instances that provide these capabilities will be used. For example, if you specify both L4 and T4 chips, Deadline Cloud will use Amazon EC2 instances that have either the L4 or the T4 chip installed.

(structure)

Describes a specific GPU accelerator required for an Amazon Elastic Compute Cloud worker host.

name -> (string)

The name of the chip used by the GPU accelerator.

If you specify `l4` as the name of the accelerator, you must specify `latest` or `grid:r550` as the runtime.

The available GPU accelerators are:

- `t4` - NVIDIA T4 Tensor Core GPU
- `a10g` - NVIDIA A10G Tensor Core GPU
- `l4` - NVIDIA L4 Tensor Core GPU
- `l40s` - NVIDIA L40S Tensor Core GPU

runtime -> (string)

Specifies the runtime driver to use for the GPU accelerator. You must use the same runtime for all GPUs.

You can choose from the following runtimes:

- `latest` - Use the latest runtime available for the chip. If you specify `latest` and a new version of the runtime is released, the new version of the runtime is used.
- `grid:r550` - [NVIDIA vGPU software 17](https://docs.nvidia.com/vgpu/17.0/index.html)
- `grid:r535` - [NVIDIA vGPU software 16](https://docs.nvidia.com/vgpu/16.0/index.html)

If you donât specify a runtime, Deadline Cloud uses `latest` as the default. However, if you have multiple accelerators and specify `latest` for some and leave others blank, Deadline Cloud raises an exception.

count -> (structure)

The number of GPU accelerators specified for worker hosts in this fleet.

min -> (integer)

The minimum number of GPU accelerators in the worker host.

max -> (integer)

The maximum number of GPU accelerators in the worker host.

allowedInstanceTypes -> (list)

The allowable Amazon EC2 instance types.

(string)

excludedInstanceTypes -> (list)

The instance types to exclude from the fleet.

(string)

customAmounts -> (list)

The custom capability amounts to require for instances in this fleet.

(structure)

The fleet amount and attribute capabilities.

name -> (string)

The name of the fleet capability.

min -> (float)

The minimum amount of fleet worker capability.

max -> (float)

The maximum amount of the fleet worker capability.

customAttributes -> (list)

The custom capability attributes to require for instances in this fleet.

(structure)

Defines the fleetâs capability name, minimum, and maximum.

name -> (string)

The name of the fleet attribute capability for the worker.

values -> (list)

The number of fleet attribute capabilities.

(string)

instanceMarketOptions -> (structure)

The Amazon EC2 market type.

type -> (string)

The Amazon EC2 instance type.

hostConfiguration -> (structure)

The script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet.

scriptBody -> (string)

The text of the script that runs as a worker is starting up that you can use to provide additional configuration for workers in your fleet. The script runs after a worker enters the `STARTING` state and before the worker processes tasks.

For more information about using the script, see [Run scripts as an administrator to configure workers](https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/smf-admin.html) in the *Deadline Cloud Developer Guide* .

### Warning

The script runs as an administrative user (`sudo root` on Linux, as an Administrator on Windows).

scriptTimeoutSeconds -> (integer)

The maximum time that the host configuration can run. If the timeout expires, the worker enters the `NOT RESPONDING` state and shuts down. You are charged for the time that the worker is running the host configuration script.

### Note

You should configure your fleet for a maximum of one worker while testing your host configuration script to avoid starting additional workers.

The default is 300 seconds (5 minutes).

capabilities -> (structure)

Outlines what the fleet is capable of for minimums, maximums, and naming, in addition to attribute names and values.

amounts -> (list)

Amount capabilities of the fleet.

(structure)

The fleet amount and attribute capabilities.

name -> (string)

The name of the fleet capability.

min -> (float)

The minimum amount of fleet worker capability.

max -> (float)

The maximum amount of the fleet worker capability.

attributes -> (list)

Attribute capabilities of the fleet.

(structure)

Defines the fleetâs capability name, minimum, and maximum.

name -> (string)

The name of the fleet attribute capability for the worker.

values -> (list)

The number of fleet attribute capabilities.

(string)

roleArn -> (string)

The IAM role ARN.

createdAt -> (timestamp)

The date and time the resource was created.

createdBy -> (string)

The user or system that created this resource.

updatedAt -> (timestamp)

The date and time the resource was updated.

updatedBy -> (string)

The user or system that updated this resource.