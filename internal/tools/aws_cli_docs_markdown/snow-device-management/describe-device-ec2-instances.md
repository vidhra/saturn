# describe-device-ec2-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snow-device-management/describe-device-ec2-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snow-device-management/describe-device-ec2-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [snow-device-management](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/snow-device-management/index.html#cli-aws-snow-device-management) ]

# describe-device-ec2-instances

## Description

Checks the current state of the Amazon EC2 instances. The output is similar to `describeDevice` , but the results are sourced from the device cache in the Amazon Web Services Cloud and include a subset of the available fields.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/snow-device-management-2021-08-04/DescribeDeviceEc2Instances)

## Synopsis

```
describe-device-ec2-instances
--instance-ids <value>
--managed-device-id <value>
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

`--instance-ids` (list)

A list of instance IDs associated with the managed device.

(string)

Syntax:

```
"string" "string" ...
```

`--managed-device-id` (string)

The ID of the managed device.

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

instances -> (list)

A list of structures containing information about each instance.

(structure)

The details about the instance.

instance -> (structure)

A structure containing details about the instance.

amiLaunchIndex -> (integer)

The Amazon Machine Image (AMI) launch index, which you can use to find this instance in the launch group.

blockDeviceMappings -> (list)

Any block device mapping entries for the instance.

(structure)

The description of a block device mapping.

deviceName -> (string)

The block device name.

ebs -> (structure)

The parameters used to automatically set up Amazon Elastic Block Store (Amazon EBS) volumes when the instance is launched.

attachTime -> (timestamp)

When the attachment was initiated.

deleteOnTermination -> (boolean)

A value that indicates whether the volume is deleted on instance termination.

status -> (string)

The attachment state.

volumeId -> (string)

The ID of the Amazon EBS volume.

cpuOptions -> (structure)

The CPU options for the instance.

coreCount -> (integer)

The number of cores that the CPU can use.

threadsPerCore -> (integer)

The number of threads per core in the CPU.

createdAt -> (timestamp)

When the instance was created.

imageId -> (string)

The ID of the AMI used to launch the instance.

instanceId -> (string)

The ID of the instance.

instanceType -> (string)

The instance type.

privateIpAddress -> (string)

The private IPv4 address assigned to the instance.

publicIpAddress -> (string)

The public IPv4 address assigned to the instance.

rootDeviceName -> (string)

The device name of the root device volume (for example, `/dev/sda1` ).

securityGroups -> (list)

The security groups for the instance.

(structure)

Information about the deviceâs security group.

groupId -> (string)

The security group ID.

groupName -> (string)

The security group name.

state -> (structure)

The description of the current state of an instance.

code -> (integer)

The state of the instance as a 16-bit unsigned integer.

The high byte is all of the bits between 2^8 and (2^16)-1, which equals decimal values between 256 and 65,535. These numerical values are used for internal purposes and should be ignored.

The low byte is all of the bits between 2^0 and (2^8)-1, which equals decimal values between 0 and 255.

The valid values for the instance state code are all in the range of the low byte. These values are:

- `0` : `pending`
- `16` : `running`
- `32` : `shutting-down`
- `48` : `terminated`
- `64` : `stopping`
- `80` : `stopped`

You can ignore the high byte value by zeroing out all of the bits above 2^8 or 256 in decimal.

name -> (string)

The current state of the instance.

updatedAt -> (timestamp)

When the instance was last updated.

lastUpdatedAt -> (timestamp)

When the instance summary was last updated.