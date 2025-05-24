# get-compute-node-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/get-compute-node-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/get-compute-node-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [pcs](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/pcs/index.html#cli-aws-pcs) ]

# get-compute-node-group

## Description

Returns detailed information about a compute node group. This API action provides networking information, EC2 instance type, compute node group status, and scheduler (such as Slurm) configuration.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/pcs-2023-02-10/GetComputeNodeGroup)

## Synopsis

```
get-compute-node-group
--cluster-identifier <value>
--compute-node-group-identifier <value>
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

The name or ID of the cluster.

`--compute-node-group-identifier` (string)

The name or ID of the compute node group.

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

computeNodeGroup -> (structure)

A compute node group associated with a cluster.

name -> (string)

The name that identifies the compute node group.

id -> (string)

The generated unique ID of the compute node group.

arn -> (string)

The unique Amazon Resource Name (ARN) of the compute node group.

clusterId -> (string)

The ID of the cluster of the compute node group.

createdAt -> (timestamp)

The date and time the resource was created.

modifiedAt -> (timestamp)

The date and time the resource was modified.

status -> (string)

The provisioning status of the compute node group.

### Note

The provisioning status doesnât indicate the overall health of the compute node group.

amiId -> (string)

The ID of the Amazon Machine Image (AMI) that Amazon Web Services PCS uses to launch instances. If not provided, Amazon Web Services PCS uses the AMI ID specified in the custom launch template.

subnetIds -> (list)

The list of subnet IDs where instances are provisioned by the compute node group. The subnets must be in the same VPC as the cluster.

(string)

purchaseOption -> (string)

Specifies how EC2 instances are purchased on your behalf. Amazon Web Services PCS supports On-Demand and Spot instances. For more information, see [Instance purchasing options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-purchasing-options.html) in the *Amazon Elastic Compute Cloud User Guide* . If you donât provide this option, it defaults to On-Demand.

customLaunchTemplate -> (structure)

An Amazon EC2 launch template Amazon Web Services PCS uses to launch compute nodes.

id -> (string)

The ID of the EC2 launch template to use to provision instances.

Example: `lt-xxxx`

version -> (string)

The version of the EC2 launch template to use to provision instances.

iamInstanceProfileArn -> (string)

The Amazon Resource Name (ARN) of the IAM instance profile used to pass an IAM role when launching EC2 instances. The role contained in your instance profile must have the `pcs:RegisterComputeNodeGroupInstance` permission. The resource identifier of the ARN must start with `AWSPCS` or it must have `/aws-pcs/` in its path.

**Examples**

- `arn:aws:iam::111122223333:instance-profile/AWSPCS-example-role-1`
- `arn:aws:iam::111122223333:instance-profile/aws-pcs/example-role-2`

scalingConfiguration -> (structure)

Specifies the boundaries of the compute node group auto scaling.

minInstanceCount -> (integer)

The lower bound of the number of instances allowed in the compute fleet.

maxInstanceCount -> (integer)

The upper bound of the number of instances allowed in the compute fleet.

instanceConfigs -> (list)

A list of EC2 instance configurations that Amazon Web Services PCS can provision in the compute node group.

(structure)

An EC2 instance configuration Amazon Web Services PCS uses to launch compute nodes.

instanceType -> (string)

The EC2 instance type that Amazon Web Services PCS can provision in the compute node group.

Example: `t2.xlarge`

spotOptions -> (structure)

Additional configuration when you specify `SPOT` as the `purchaseOption` for the `CreateComputeNodeGroup` API action.

allocationStrategy -> (string)

The Amazon EC2 allocation strategy Amazon Web Services PCS uses to provision EC2 instances. Amazon Web Services PCS supports **lowest price** , **capacity optimized** , and **price capacity optimized** . For more information, see [Use allocation strategies to determine how EC2 Fleet or Spot Fleet fulfills Spot and On-Demand capacity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-fleet-allocation-strategy.html) in the *Amazon Elastic Compute Cloud User Guide* . If you donât provide this option, it defaults to **price capacity optimized** .

slurmConfiguration -> (structure)

Additional options related to the Slurm scheduler.

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

errorInfo -> (list)

The list of errors that occurred during compute node group provisioning.

(structure)

An error that occurred during resource creation.

code -> (string)

The short-form error code.

message -> (string)

The detailed error information.