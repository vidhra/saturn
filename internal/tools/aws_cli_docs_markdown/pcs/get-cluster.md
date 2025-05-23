# get-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/get-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/get-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pcs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/index.html#cli-aws-pcs) ]

# get-cluster

## Description

Returns detailed information about a running cluster in your account. This API action provides networking information, endpoint information for communication with the scheduler, and provisioning status.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pcs-2023-02-10/GetCluster)

## Synopsis

```
get-cluster
--cluster-identifier <value>
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

`--cluster-identifier` (string)

The name or ID of the cluster of the queue.

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

cluster -> (structure)

The cluster resource.

name -> (string)

The name that identifies the cluster.

id -> (string)

The generated unique ID of the cluster.

arn -> (string)

The unique Amazon Resource Name (ARN) of the cluster.

status -> (string)

The provisioning status of the cluster.

### Note

The provisioning status doesnât indicate the overall health of the cluster.

createdAt -> (timestamp)

The date and time the resource was created.

modifiedAt -> (timestamp)

The date and time the resource was modified.

scheduler -> (structure)

The cluster management and job scheduling software associated with the cluster.

type -> (string)

The software Amazon Web Services PCS uses to manage cluster scaling and job scheduling.

version -> (string)

The version of the specified scheduling software that Amazon Web Services PCS uses to manage cluster scaling and job scheduling. For more information, see [Slurm versions in Amazon Web Services PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions.html) in the *Amazon Web Services PCS User Guide* .

Valid Values: `23.11 | 24.05 | 24.11`

size -> (string)

The size of the cluster.

- `SMALL` : 32 compute nodes and 256 jobs
- `MEDIUM` : 512 compute nodes and 8192 jobs
- `LARGE` : 2048 compute nodes and 16,384 jobs

slurmConfiguration -> (structure)

Additional options related to the Slurm scheduler.

scaleDownIdleTimeInSeconds -> (integer)

The time (in seconds) before an idle node is scaled down.

Default: `600`

slurmCustomSettings -> (list)

Additional Slurm-specific configuration that directly maps to Slurm settings.

(structure)

Additional settings that directly map to Slurm settings.

parameterName -> (string)

Amazon Web Services PCS supports configuration of the following Slurm parameters:

- For **clusters**
- ``Prolog` [https://slurm.schedmd.com/slurm.conf](https://slurm.schedmd.com/slurm.conf).html#OPT_Prolog_1`__
- ``Epilog` [https://slurm.schedmd.com/slurm.conf](https://slurm.schedmd.com/slurm.conf).html#OPT_Epilog_1`__
- ``SelectTypeParameters` [https://slurm.schedmd.com/slurm.conf](https://slurm.schedmd.com/slurm.conf).html#OPT_SelectTypeParameters`__
- For **compute node groups**
- ``Weight` [https://slurm.schedmd.com/slurm.conf](https://slurm.schedmd.com/slurm.conf).html#OPT_Weight`__
- ``RealMemory` [https://slurm.schedmd.com/slurm.conf](https://slurm.schedmd.com/slurm.conf).html#OPT_Weight`__

parameterValue -> (string)

The values for the configured Slurm settings.

authKey -> (structure)

The shared Slurm key for authentication, also known as the **cluster secret** .

secretArn -> (string)

The Amazon Resource Name (ARN) of the the shared Slurm key.

secretVersion -> (string)

The version of the shared Slurm key.

accounting -> (structure)

The accounting configuration includes configurable settings for Slurm accounting.

mode -> (string)

The default value for `mode` is `STANDARD` . A value of `STANDARD` means Slurm accounting is enabled.

defaultPurgeTimeInDays -> (integer)

The default value for all purge settings for `slurmdbd.conf` . For more information, see the [slurmdbd.conf documentation at SchedMD](https://slurm.schedmd.com/slurmdbd.conf.html) .

The default value for `defaultPurgeTimeInDays` is `-1` .

A value of `-1` means there is no purge time and records persist as long as the cluster exists.

### Warning

`0` isnât a valid value.

networking -> (structure)

The networking configuration for the clusterâs control plane.

subnetIds -> (list)

The ID of the subnet where Amazon Web Services PCS creates an Elastic Network Interface (ENI) to enable communication between managed controllers and Amazon Web Services PCS resources. The subnet must have an available IP address, cannot reside in AWS Outposts, AWS Wavelength, or an AWS Local Zone.

Example: `subnet-abcd1234`

(string)

securityGroupIds -> (list)

The list of security group IDs associated with the Elastic Network Interface (ENI) created in subnets.

The following rules are required:

- Inbound rule 1
- Protocol: All
- Ports: All
- Source: Self
- Outbound rule 1
- Protocol: All
- Ports: All
- Destination: 0.0.0.0/0 (IPv4)
- Outbound rule 2
- Protocol: All
- Ports: All
- Destination: Self

(string)

endpoints -> (list)

The list of endpoints available for interaction with the scheduler.

(structure)

An endpoint available for interaction with the scheduler.

type -> (string)

Indicates the type of endpoint running at the specific IP address.

privateIpAddress -> (string)

The endpointâs private IP address.

Example: `2.2.2.2`

publicIpAddress -> (string)

The endpointâs public IP address.

Example: `1.1.1.1`

port -> (string)

The endpointâs connection port number.

Example: `1234`

errorInfo -> (list)

The list of errors that occurred during cluster provisioning.

(structure)

An error that occurred during resource creation.

code -> (string)

The short-form error code.

message -> (string)

The detailed error information.