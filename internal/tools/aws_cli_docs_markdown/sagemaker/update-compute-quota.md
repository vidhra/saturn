# update-compute-quotaÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-compute-quota.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/update-compute-quota.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [sagemaker](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sagemaker/index.html#cli-aws-sagemaker) ]

# update-compute-quota

## Description

Update the compute allocation definition.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/sagemaker-2017-07-24/UpdateComputeQuota)

## Synopsis

```
update-compute-quota
--compute-quota-id <value>
--target-version <value>
[--compute-quota-config <value>]
[--compute-quota-target <value>]
[--activation-state <value>]
[--description <value>]
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

`--compute-quota-id` (string)

ID of the compute allocation definition.

`--target-version` (integer)

Target version.

`--compute-quota-config` (structure)

Configuration of the compute allocation definition. This includes the resource sharing option, and the setting to preempt low priority tasks.

ComputeQuotaResources -> (list)

Allocate compute resources by instance types.

(structure)

Configuration of the resources used for the compute allocation definition.

InstanceType -> (string)

The instance type of the instance group for the cluster.

Count -> (integer)

The number of instances to add to the instance group of a SageMaker HyperPod cluster.

ResourceSharingConfig -> (structure)

Resource sharing configuration. This defines how an entity can lend and borrow idle compute with other entities within the cluster.

Strategy -> (string)

The strategy of how idle compute is shared within the cluster. The following are the options of strategies.

- `DontLend` : entities do not lend idle compute.
- `Lend` : entities can lend idle compute to entities that can borrow.
- `LendandBorrow` : entities can lend idle compute and borrow idle compute from other entities.

Default is `LendandBorrow` .

BorrowLimit -> (integer)

The limit on how much idle compute can be borrowed.The values can be 1 - 500 percent of idle compute that the team is allowed to borrow.

Default is `50` .

PreemptTeamTasks -> (string)

Allows workloads from within an entity to preempt same-team workloads. When set to `LowerPriority` , the entityâs lower priority tasks are preempted by their own higher priority tasks.

Default is `LowerPriority` .

Shorthand Syntax:

```
ComputeQuotaResources=[{InstanceType=string,Count=integer},{InstanceType=string,Count=integer}],ResourceSharingConfig={Strategy=string,BorrowLimit=integer},PreemptTeamTasks=string
```

JSON Syntax:

```
{
  "ComputeQuotaResources": [
    {
      "InstanceType": "ml.p4d.24xlarge"|"ml.p4de.24xlarge"|"ml.p5.48xlarge"|"ml.trn1.32xlarge"|"ml.trn1n.32xlarge"|"ml.g5.xlarge"|"ml.g5.2xlarge"|"ml.g5.4xlarge"|"ml.g5.8xlarge"|"ml.g5.12xlarge"|"ml.g5.16xlarge"|"ml.g5.24xlarge"|"ml.g5.48xlarge"|"ml.c5.large"|"ml.c5.xlarge"|"ml.c5.2xlarge"|"ml.c5.4xlarge"|"ml.c5.9xlarge"|"ml.c5.12xlarge"|"ml.c5.18xlarge"|"ml.c5.24xlarge"|"ml.c5n.large"|"ml.c5n.2xlarge"|"ml.c5n.4xlarge"|"ml.c5n.9xlarge"|"ml.c5n.18xlarge"|"ml.m5.large"|"ml.m5.xlarge"|"ml.m5.2xlarge"|"ml.m5.4xlarge"|"ml.m5.8xlarge"|"ml.m5.12xlarge"|"ml.m5.16xlarge"|"ml.m5.24xlarge"|"ml.t3.medium"|"ml.t3.large"|"ml.t3.xlarge"|"ml.t3.2xlarge"|"ml.g6.xlarge"|"ml.g6.2xlarge"|"ml.g6.4xlarge"|"ml.g6.8xlarge"|"ml.g6.16xlarge"|"ml.g6.12xlarge"|"ml.g6.24xlarge"|"ml.g6.48xlarge"|"ml.gr6.4xlarge"|"ml.gr6.8xlarge"|"ml.g6e.xlarge"|"ml.g6e.2xlarge"|"ml.g6e.4xlarge"|"ml.g6e.8xlarge"|"ml.g6e.16xlarge"|"ml.g6e.12xlarge"|"ml.g6e.24xlarge"|"ml.g6e.48xlarge"|"ml.p5e.48xlarge"|"ml.p5en.48xlarge"|"ml.trn2.48xlarge"|"ml.c6i.large"|"ml.c6i.xlarge"|"ml.c6i.2xlarge"|"ml.c6i.4xlarge"|"ml.c6i.8xlarge"|"ml.c6i.12xlarge"|"ml.c6i.16xlarge"|"ml.c6i.24xlarge"|"ml.c6i.32xlarge"|"ml.m6i.large"|"ml.m6i.xlarge"|"ml.m6i.2xlarge"|"ml.m6i.4xlarge"|"ml.m6i.8xlarge"|"ml.m6i.12xlarge"|"ml.m6i.16xlarge"|"ml.m6i.24xlarge"|"ml.m6i.32xlarge"|"ml.r6i.large"|"ml.r6i.xlarge"|"ml.r6i.2xlarge"|"ml.r6i.4xlarge"|"ml.r6i.8xlarge"|"ml.r6i.12xlarge"|"ml.r6i.16xlarge"|"ml.r6i.24xlarge"|"ml.r6i.32xlarge"|"ml.i3en.large"|"ml.i3en.xlarge"|"ml.i3en.2xlarge"|"ml.i3en.3xlarge"|"ml.i3en.6xlarge"|"ml.i3en.12xlarge"|"ml.i3en.24xlarge"|"ml.m7i.large"|"ml.m7i.xlarge"|"ml.m7i.2xlarge"|"ml.m7i.4xlarge"|"ml.m7i.8xlarge"|"ml.m7i.12xlarge"|"ml.m7i.16xlarge"|"ml.m7i.24xlarge"|"ml.m7i.48xlarge"|"ml.r7i.large"|"ml.r7i.xlarge"|"ml.r7i.2xlarge"|"ml.r7i.4xlarge"|"ml.r7i.8xlarge"|"ml.r7i.12xlarge"|"ml.r7i.16xlarge"|"ml.r7i.24xlarge"|"ml.r7i.48xlarge",
      "Count": integer
    }
    ...
  ],
  "ResourceSharingConfig": {
    "Strategy": "Lend"|"DontLend"|"LendAndBorrow",
    "BorrowLimit": integer
  },
  "PreemptTeamTasks": "Never"|"LowerPriority"
}
```

`--compute-quota-target` (structure)

The target entity to allocate compute resources to.

TeamName -> (string)

Name of the team to allocate compute resources to.

FairShareWeight -> (integer)

Assigned entity fair-share weight. Idle compute will be shared across entities based on these assigned weights. This weight is only used when `FairShare` is enabled.

A weight of 0 is the lowest priority and 100 is the highest. Weight 0 is the default.

Shorthand Syntax:

```
TeamName=string,FairShareWeight=integer
```

JSON Syntax:

```
{
  "TeamName": "string",
  "FairShareWeight": integer
}
```

`--activation-state` (string)

The state of the compute allocation being described. Use to enable or disable compute allocation.

Default is `Enabled` .

Possible values:

- `Enabled`
- `Disabled`

`--description` (string)

Description of the compute allocation definition.

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

ComputeQuotaArn -> (string)

ARN of the compute allocation definition.

ComputeQuotaVersion -> (integer)

Version of the compute allocation definition.