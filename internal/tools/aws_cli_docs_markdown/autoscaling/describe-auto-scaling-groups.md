# describe-auto-scaling-groupsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-auto-scaling-groups.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [autoscaling](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/index.html#cli-aws-autoscaling) ]

# describe-auto-scaling-groups

## Description

Gets information about the Auto Scaling groups in the account and Region.

If you specify Auto Scaling group names, the output includes information for only the specified Auto Scaling groups. If you specify filters, the output includes information for only those Auto Scaling groups that meet the filter criteria. If you do not specify group names or filters, the output includes information for all Auto Scaling groups.

This operation also returns information about instances in Auto Scaling groups. To retrieve information about the instances in a warm pool, you must call the [DescribeWarmPool](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeWarmPool.html) API.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/autoscaling-2011-01-01/DescribeAutoScalingGroups)

`describe-auto-scaling-groups` is a paginated operation. Multiple API calls may be issued in order to retrieve the entire data set of results. You can disable pagination by providing the `--no-paginate` argument.
When using `--output text` and the `--query` argument on a paginated response, the `--query` argument must extract data from the results of the following query expressions: `AutoScalingGroups`

## Synopsis

```
describe-auto-scaling-groups
[--auto-scaling-group-names <value>]
[--filters <value>]
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

`--auto-scaling-group-names` (list)

The names of the Auto Scaling groups. By default, you can only specify up to 50 names. You can optionally increase this limit using the `MaxRecords` property.

If you omit this property, all Auto Scaling groups are described.

(string)

Syntax:

```
"string" "string" ...
```

`--filters` (list)

One or more filters to limit the results based on specific tags.

(structure)

Describes a filter that is used to return a more specific list of results from a describe operation.

If you specify multiple filters, the filters are automatically logically joined with an `AND` , and the request returns only the results that match all of the specified filters.

For more information, see [Tag Auto Scaling groups and instances](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-tagging.html) in the *Amazon EC2 Auto Scaling User Guide* .

Name -> (string)

The name of the filter.

The valid values for `Name` depend on which API operation youâre using with the filter ([DescribeAutoScalingGroups](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeAutoScalingGroups.html) or [DescribeTags](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DescribeTags.html) ).

**DescribeAutoScalingGroups**

Valid values for `Name` include the following:

- `tag-key` - Accepts tag keys. The results only include information about the Auto Scaling groups associated with these tag keys.
- `tag-value` - Accepts tag values. The results only include information about the Auto Scaling groups associated with these tag values.
- `tag:<key>` - Accepts the key/value combination of the tag. Use the tag key in the filter name and the tag value as the filter value. The results only include information about the Auto Scaling groups associated with the specified key/value combination.

**DescribeTags**

Valid values for `Name` include the following:

- `auto-scaling-group` - Accepts the names of Auto Scaling groups. The results only include information about the tags associated with these Auto Scaling groups.
- `key` - Accepts tag keys. The results only include information about the tags associated with these tag keys.
- `value` - Accepts tag values. The results only include information about the tags associated with these tag values.
- `propagate-at-launch` - Accepts a Boolean value, which specifies whether tags propagate to instances at launch. The results only include information about the tags associated with the specified Boolean value.

Values -> (list)

One or more filter values. Filter values are case-sensitive.

If you specify multiple values for a filter, the values are automatically logically joined with an `OR` , and the request returns all results that match any of the specified values. For example, specify â[tag:environment](tag:environment)â for the filter name and âproduction,developmentâ for the filter values to find Auto Scaling groups with the tag âenvironment=productionâ or âenvironment=developmentâ.

(string)

Shorthand Syntax:

```
Name=string,Values=string,string ...
```

JSON Syntax:

```
[
  {
    "Name": "string",
    "Values": ["string", ...]
  }
  ...
]
```

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

**Example 1: To describe the specified Auto Scaling group**

This example describes the specified Auto Scaling group.

```
aws autoscaling describe-auto-scaling-groups \
    --auto-scaling-group-names my-asg
```

Output:

```
{
    "AutoScalingGroups": [
        {
            "AutoScalingGroupName": "my-asg",
            "AutoScalingGroupARN": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:930d940e-891e-4781-a11a-7b0acd480f03:autoScalingGroupName/my-asg",
            "LaunchTemplate": {
                "LaunchTemplateName": "my-launch-template",
                "Version": "1",
                "LaunchTemplateId": "lt-1234567890abcde12"
            },
            "MinSize": 0,
            "MaxSize": 1,
            "DesiredCapacity": 1,
            "DefaultCooldown": 300,
            "AvailabilityZones": [
                "us-west-2a",
                "us-west-2b",
                "us-west-2c"
            ],
            "LoadBalancerNames": [],
            "TargetGroupARNs": [],
            "HealthCheckType": "EC2",
            "HealthCheckGracePeriod": 0,
            "Instances": [
                {
                    "InstanceId": "i-06905f55584de02da",
                    "InstanceType": "t2.micro",
                    "AvailabilityZone": "us-west-2a",
                    "HealthStatus": "Healthy",
                    "LifecycleState": "InService",
                    "ProtectedFromScaleIn": false,
                    "LaunchTemplate": {
                        "LaunchTemplateName": "my-launch-template",
                        "Version": "1",
                        "LaunchTemplateId": "lt-1234567890abcde12"
                    }
                }
            ],
            "CreatedTime": "2023-10-28T02:39:22.152Z",
            "SuspendedProcesses": [],
            "VPCZoneIdentifier": "subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782",
            "EnabledMetrics": [],
            "Tags": [],
            "TerminationPolicies": [
                "Default"
            ],
            "NewInstancesProtectedFromScaleIn": false,
            "ServiceLinkedRoleARN":"arn",
            "TrafficSources": []
        }
    ]
}
```

**Example 2: To describe the first 100 specified Auto Scaling group**

This example describes the specified Auto Scaling groups. It allows you to specify up to 100 group names.

```
aws autoscaling describe-auto-scaling-groups \
    --max-items 100 \
    --auto-scaling-group-names "group1" "group2" "group3" "group4"
```

See example 1 for sample output.

**Example 3: To describe an Auto Scaling group in the specified region**

This example describes the Auto Scaling groups in the specified region, up to a maximum of 75 groups.

```
aws autoscaling describe-auto-scaling-groups \
    --max-items 75 \
    --region us-east-1
```

See example 1 for sample output.

**Example 4: To describe the specified number of Auto Scaling group**

To return a specific number of Auto Scaling groups, use the `--max-items` option.

```
aws autoscaling describe-auto-scaling-groups \
    --max-items 1
```

See example 1 for sample output.

If the output includes a `NextToken` field, there are more groups. To get the additional groups, use the value of this field with the `--starting-token` option in a subsequent call as follows.

```
aws autoscaling describe-auto-scaling-groups \
    --starting-token Z3M3LMPEXAMPLE
```

See example 1 for sample output.

**Example 5: To describe Auto Scaling groups that use launch configurations**

This example uses the `--query` option to describe Auto Scaling groups that use launch configurations.

```
aws autoscaling describe-auto-scaling-groups \
    --query 'AutoScalingGroups[?LaunchConfigurationName!=`null`]'
```

Output:

```
[
    {
        "AutoScalingGroupName": "my-asg",
        "AutoScalingGroupARN": "arn:aws:autoscaling:us-west-2:123456789012:autoScalingGroup:930d940e-891e-4781-a11a-7b0acd480f03:autoScalingGroupName/my-asg",
        "LaunchConfigurationName": "my-lc",
        "MinSize": 0,
        "MaxSize": 1,
        "DesiredCapacity": 1,
        "DefaultCooldown": 300,
        "AvailabilityZones": [
            "us-west-2a",
            "us-west-2b",
            "us-west-2c"
        ],
        "LoadBalancerNames": [],
        "TargetGroupARNs": [],
        "HealthCheckType": "EC2",
        "HealthCheckGracePeriod": 0,
        "Instances": [
            {
                "InstanceId": "i-088c57934a6449037",
                "InstanceType": "t2.micro",
                "AvailabilityZone": "us-west-2c",
                "HealthStatus": "Healthy",
                "LifecycleState": "InService",
                "LaunchConfigurationName": "my-lc",
                "ProtectedFromScaleIn": false
            }
        ],
        "CreatedTime": "2023-10-28T02:39:22.152Z",
        "SuspendedProcesses": [],
        "VPCZoneIdentifier": "subnet-5ea0c127,subnet-6194ea3b,subnet-c934b782",
        "EnabledMetrics": [],
        "Tags": [],
        "TerminationPolicies": [
            "Default"
        ],
        "NewInstancesProtectedFromScaleIn": false,
        "ServiceLinkedRoleARN":"arn",
        "TrafficSources": []
    }
]
```

For more information, see [Filter AWS CLI output](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-filter.html) in the *AWS Command Line Interface User Guide*.

## Output

AutoScalingGroups -> (list)

The groups.

(structure)

Describes an Auto Scaling group.

AutoScalingGroupName -> (string)

The name of the Auto Scaling group.

AutoScalingGroupARN -> (string)

The Amazon Resource Name (ARN) of the Auto Scaling group.

LaunchConfigurationName -> (string)

The name of the associated launch configuration.

LaunchTemplate -> (structure)

The launch template for the group.

LaunchTemplateId -> (string)

The ID of the launch template. To get the template ID, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

LaunchTemplateName -> (string)

The name of the launch template. To get the template name, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

Version -> (string)

The version number, `$Latest` , or `$Default` . To get the version number, use the Amazon EC2 [DescribeLaunchTemplateVersions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html) API operation. New launch template versions can be created using the Amazon EC2 [CreateLaunchTemplateVersion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html) API. If the value is `$Latest` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is `$Default` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is `$Default` .

MixedInstancesPolicy -> (structure)

The mixed instances policy for the group.

LaunchTemplate -> (structure)

One or more launch templates and the instance types (overrides) that are used to launch EC2 instances to fulfill On-Demand and Spot capacities.

LaunchTemplateSpecification -> (structure)

The launch template.

LaunchTemplateId -> (string)

The ID of the launch template. To get the template ID, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

LaunchTemplateName -> (string)

The name of the launch template. To get the template name, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

Version -> (string)

The version number, `$Latest` , or `$Default` . To get the version number, use the Amazon EC2 [DescribeLaunchTemplateVersions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html) API operation. New launch template versions can be created using the Amazon EC2 [CreateLaunchTemplateVersion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html) API. If the value is `$Latest` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is `$Default` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is `$Default` .

Overrides -> (list)

Any properties that you specify override the same properties in the launch template.

(structure)

Use this structure to let Amazon EC2 Auto Scaling do the following when the Auto Scaling group has a mixed instances policy:

- Override the instance type that is specified in the launch template.
- Use multiple instance types.

Specify the instance types that you want, or define your instance requirements instead and let Amazon EC2 Auto Scaling provision the available instance types that meet your requirements. This can provide Amazon EC2 Auto Scaling with a larger selection of instance types to choose from when fulfilling Spot and On-Demand capacities. You can view which instance types are matched before you apply the instance requirements to your Auto Scaling group.

After you define your instance requirements, you donât have to keep updating these settings to get new EC2 instance types automatically. Amazon EC2 Auto Scaling uses the instance requirements of the Auto Scaling group to determine whether a new EC2 instance type can be used.

InstanceType -> (string)

The instance type, such as `m3.xlarge` . You must specify an instance type that is supported in your requested Region and Availability Zones. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide for Linux Instances* .

You can specify up to 40 instance types per Auto Scaling group.

WeightedCapacity -> (string)

If you provide a list of instance types to use, you can specify the number of capacity units provided by each instance type in terms of virtual CPUs, memory, storage, throughput, or other relative performance characteristic. When a Spot or On-Demand Instance is launched, the capacity units count toward the desired capacity. Amazon EC2 Auto Scaling launches instances until the desired capacity is totally fulfilled, even if this results in an overage. For example, if there are two units remaining to fulfill capacity, and Amazon EC2 Auto Scaling can only launch an instance with a `WeightedCapacity` of five units, the instance is launched, and the desired capacity is exceeded by three units. For more information, see [Configure an Auto Scaling group to use instance weights](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups-instance-weighting.html) in the *Amazon EC2 Auto Scaling User Guide* . Value must be in the range of 1â999.

If you specify a value for `WeightedCapacity` for one instance type, you must specify a value for `WeightedCapacity` for all of them.

### Warning

Every Auto Scaling group has three size parameters (`DesiredCapacity` , `MaxSize` , and `MinSize` ). Usually, you set these sizes based on a specific number of instances. However, if you configure a mixed instances policy that defines weights for the instance types, you must specify these sizes with the same units that you use for weighting instances.

LaunchTemplateSpecification -> (structure)

Provides a launch template for the specified instance type or set of instance requirements. For example, some instance types might require a launch template with a different AMI. If not provided, Amazon EC2 Auto Scaling uses the launch template thatâs specified in the `LaunchTemplate` definition. For more information, see [Specifying a different launch template for an instance type](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-mixed-instances-groups-launch-template-overrides.html) in the *Amazon EC2 Auto Scaling User Guide* .

You can specify up to 20 launch templates per Auto Scaling group. The launch templates specified in the overrides and in the `LaunchTemplate` definition count towards this limit.

LaunchTemplateId -> (string)

The ID of the launch template. To get the template ID, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

LaunchTemplateName -> (string)

The name of the launch template. To get the template name, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

Version -> (string)

The version number, `$Latest` , or `$Default` . To get the version number, use the Amazon EC2 [DescribeLaunchTemplateVersions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html) API operation. New launch template versions can be created using the Amazon EC2 [CreateLaunchTemplateVersion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html) API. If the value is `$Latest` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is `$Default` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is `$Default` .

InstanceRequirements -> (structure)

The instance requirements. Amazon EC2 Auto Scaling uses your specified requirements to identify instance types. Then, it uses your On-Demand and Spot allocation strategies to launch instances from these instance types.

You can specify up to four separate sets of instance requirements per Auto Scaling group. This is useful for provisioning instances from different Amazon Machine Images (AMIs) in the same Auto Scaling group. To do this, create the AMIs and create a new launch template for each AMI. Then, create a compatible set of instance requirements for each launch template.

### Note

If you specify `InstanceRequirements` , you canât specify `InstanceType` .

VCpuCount -> (structure)

The minimum and maximum number of vCPUs for an instance type.

Min -> (integer)

The minimum number of vCPUs.

Max -> (integer)

The maximum number of vCPUs.

MemoryMiB -> (structure)

The minimum and maximum instance memory size for an instance type, in MiB.

Min -> (integer)

The memory minimum in MiB.

Max -> (integer)

The memory maximum in MiB.

CpuManufacturers -> (list)

Lists which specific CPU manufacturers to include.

- For instance types with Intel CPUs, specify `intel` .
- For instance types with AMD CPUs, specify `amd` .
- For instance types with Amazon Web Services CPUs, specify `amazon-web-services` .

### Note

Donât confuse the CPU hardware manufacturer with the CPU hardware architecture. Instances will be launched with a compatible CPU architecture based on the Amazon Machine Image (AMI) that you specify in your launch template.

Default: Any manufacturer

(string)

MemoryGiBPerVCpu -> (structure)

The minimum and maximum amount of memory per vCPU for an instance type, in GiB.

Default: No minimum or maximum limits

Min -> (double)

The memory minimum in GiB.

Max -> (double)

The memory maximum in GiB.

ExcludedInstanceTypes -> (list)

The instance types to exclude. You can use strings with one or more wild cards, represented by an asterisk (`*` ), to exclude an instance family, type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` , you are excluding the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 Auto Scaling will exclude all the M5a instance types, but not the M5n instance types.

### Note

If you specify `ExcludedInstanceTypes` , you canât specify `AllowedInstanceTypes` .

Default: No excluded instance types

(string)

InstanceGenerations -> (list)

Indicates whether current or previous generation instance types are included.

- For current generation instance types, specify `current` . The current generation includes EC2 instance types currently recommended for use. This typically includes the latest two to three generations in each instance family. For more information, see [Instance types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html) in the *Amazon EC2 User Guide for Linux Instances* .
- For previous generation instance types, specify `previous` .

Default: Any current or previous generation

(string)

SpotMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage higher than an identified Spot price. The identified Spot price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.

If you set `DesiredCapacityType` to `vcpu` or `memory-mib` , the price protection threshold is based on the per-vCPU or per-memory price instead of the per instance price.

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 Auto Scaling will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

MaxSpotPriceAsPercentageOfOptimalOnDemandPrice -> (integer)

[Price protection] The price protection threshold for Spot Instances, as a percentage of an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.

If you set `DesiredCapacityType` to `vcpu` or `memory-mib` , the price protection threshold is based on the per-vCPU or per-memory price instead of the per instance price.

### Note

Only one of `SpotMaxPricePercentageOverLowestPrice` or `MaxSpotPriceAsPercentageOfOptimalOnDemandPrice` can be specified. If you donât specify either, Amazon EC2 Auto Scaling will automatically apply optimal price protection to consistently select from a wide range of instance types. To indicate no price protection threshold for Spot Instances, meaning you want to consider all instance types that match your attributes, include one of these parameters and specify a high value, such as `999999` .

OnDemandMaxPricePercentageOverLowestPrice -> (integer)

[Price protection] The price protection threshold for On-Demand Instances, as a percentage higher than an identified On-Demand price. The identified On-Demand price is the price of the lowest priced current generation C, M, or R instance type with your specified attributes. If no current generation C, M, or R instance type matches your attributes, then the identified price is from either the lowest priced current generation instance types or, failing that, the lowest priced previous generation instance types that match your attributes. When Amazon EC2 Auto Scaling selects instance types with your attributes, we will exclude instance types whose price exceeds your specified threshold.

The parameter accepts an integer, which Amazon EC2 Auto Scaling interprets as a percentage.

To turn off price protection, specify a high value, such as `999999` .

If you set `DesiredCapacityType` to `vcpu` or `memory-mib` , the price protection threshold is applied based on the per-vCPU or per-memory price instead of the per instance price.

Default: `20`

BareMetal -> (string)

Indicates whether bare metal instance types are included, excluded, or required.

Default: `excluded`

BurstablePerformance -> (string)

Indicates whether burstable performance instance types are included, excluded, or required. For more information, see [Burstable performance instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/burstable-performance-instances.html) in the *Amazon EC2 User Guide for Linux Instances* .

Default: `excluded`

RequireHibernateSupport -> (boolean)

Indicates whether instance types must provide On-Demand Instance hibernation support.

Default: `false`

NetworkInterfaceCount -> (structure)

The minimum and maximum number of network interfaces for an instance type.

Default: No minimum or maximum limits

Min -> (integer)

The minimum number of network interfaces.

Max -> (integer)

The maximum number of network interfaces.

LocalStorage -> (string)

Indicates whether instance types with instance store volumes are included, excluded, or required. For more information, see [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) in the *Amazon EC2 User Guide for Linux Instances* .

Default: `included`

LocalStorageTypes -> (list)

Indicates the type of local storage that is required.

- For instance types with hard disk drive (HDD) storage, specify `hdd` .
- For instance types with solid state drive (SSD) storage, specify `ssd` .

Default: Any local storage type

(string)

TotalLocalStorageGB -> (structure)

The minimum and maximum total local storage size for an instance type, in GB.

Default: No minimum or maximum limits

Min -> (double)

The storage minimum in GB.

Max -> (double)

The storage maximum in GB.

BaselineEbsBandwidthMbps -> (structure)

The minimum and maximum baseline bandwidth performance for an instance type, in Mbps. For more information, see [Amazon EBSâoptimized instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-optimized.html) in the *Amazon EC2 User Guide for Linux Instances* .

Default: No minimum or maximum limits

Min -> (integer)

The minimum value in Mbps.

Max -> (integer)

The maximum value in Mbps.

AcceleratorTypes -> (list)

Lists the accelerator types that must be on an instance type.

- For instance types with GPU accelerators, specify `gpu` .
- For instance types with FPGA accelerators, specify `fpga` .
- For instance types with inference accelerators, specify `inference` .

Default: Any accelerator type

(string)

AcceleratorCount -> (structure)

The minimum and maximum number of accelerators (GPUs, FPGAs, or Amazon Web Services Inferentia chips) for an instance type.

To exclude accelerator-enabled instance types, set `Max` to `0` .

Default: No minimum or maximum limits

Min -> (integer)

The minimum value.

Max -> (integer)

The maximum value.

AcceleratorManufacturers -> (list)

Indicates whether instance types must have accelerators by specific manufacturers.

- For instance types with NVIDIA devices, specify `nvidia` .
- For instance types with AMD devices, specify `amd` .
- For instance types with Amazon Web Services devices, specify `amazon-web-services` .
- For instance types with Xilinx devices, specify `xilinx` .

Default: Any manufacturer

(string)

AcceleratorNames -> (list)

Lists the accelerators that must be on an instance type.

- For instance types with NVIDIA A100 GPUs, specify `a100` .
- For instance types with NVIDIA V100 GPUs, specify `v100` .
- For instance types with NVIDIA K80 GPUs, specify `k80` .
- For instance types with NVIDIA T4 GPUs, specify `t4` .
- For instance types with NVIDIA M60 GPUs, specify `m60` .
- For instance types with AMD Radeon Pro V520 GPUs, specify `radeon-pro-v520` .
- For instance types with Xilinx VU9P FPGAs, specify `vu9p` .

Default: Any accelerator

(string)

AcceleratorTotalMemoryMiB -> (structure)

The minimum and maximum total memory size for the accelerators on an instance type, in MiB.

Default: No minimum or maximum limits

Min -> (integer)

The memory minimum in MiB.

Max -> (integer)

The memory maximum in MiB.

NetworkBandwidthGbps -> (structure)

The minimum and maximum amount of network bandwidth, in gigabits per second (Gbps).

Default: No minimum or maximum limits

Min -> (double)

The minimum amount of network bandwidth, in gigabits per second (Gbps).

Max -> (double)

The maximum amount of network bandwidth, in gigabits per second (Gbps).

AllowedInstanceTypes -> (list)

The instance types to apply your specified attributes against. All other instance types are ignored, even if they match your specified attributes.

You can use strings with one or more wild cards, represented by an asterisk (`*` ), to allow an instance type, size, or generation. The following are examples: `m5.8xlarge` , `c5*.*` , `m5a.*` , `r*` , `*3*` .

For example, if you specify `c5*` , Amazon EC2 Auto Scaling will allow the entire C5 instance family, which includes all C5a and C5n instance types. If you specify `m5a.*` , Amazon EC2 Auto Scaling will allow all the M5a instance types, but not the M5n instance types.

### Note

If you specify `AllowedInstanceTypes` , you canât specify `ExcludedInstanceTypes` .

Default: All instance types

(string)

BaselinePerformanceFactors -> (structure)

The baseline performance factors for the instance requirements.

Cpu -> (structure)

The CPU performance to consider, using an instance family as the baseline reference.

References -> (list)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.

### Note

Currently only one instance family can be specified in the list.

(structure)

Specify an instance family to use as the baseline reference for CPU performance. All instance types that All instance types that match your specified attributes will be compared against the CPU performance of the referenced instance family, regardless of CPU manufacturer or architecture differences.

### Note

Currently only one instance family can be specified in the list.

InstanceFamily -> (string)

The instance family to use as a baseline reference.

### Note

Make sure that you specify the correct value for the instance family. The instance family is everything before the period (.) in the instance type name. For example, in the instance `c6i.large` , the instance family is `c6i` , not `c6` . For more information, see [Amazon EC2 instance type naming conventions](https://docs.aws.amazon.com/ec2/latest/instancetypes/instance-type-names.html) in *Amazon EC2 Instance Types* .

The following instance types are *not supported* for performance protection.

- `c1`
- `g3| g3s`
- `hpc7g`
- `m1| m2`
- `mac1 | mac2 | mac2-m1ultra | mac2-m2 | mac2-m2pro`
- `p3dn | p4d | p5`
- `t1`
- `u-12tb1 | u-18tb1 | u-24tb1 | u-3tb1 | u-6tb1 | u-9tb1 | u7i-12tb | u7in-16tb | u7in-24tb | u7in-32tb`

If you performance protection by specifying a supported instance family, the returned instance types will exclude the preceding unsupported instance families.

If you specify an unsupported instance family as a value for baseline performance, the API returns an empty response.

InstancesDistribution -> (structure)

The instances distribution.

OnDemandAllocationStrategy -> (string)

The allocation strategy to apply to your On-Demand Instances when they are launched. Possible instance types are determined by the launch template overrides that you specify.

The following lists the valid values:

lowest-price

Uses price to determine which instance types are the highest priority, launching the lowest priced instance types within an Availability Zone first. This is the default value for Auto Scaling groups that specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) .

prioritized

You set the order of instance types for the launch template overrides from highest to lowest priority (from first to last in the list). Amazon EC2 Auto Scaling launches your highest priority instance types first. If all your On-Demand capacity cannot be fulfilled using your highest priority instance type, then Amazon EC2 Auto Scaling launches the remaining capacity using the second priority instance type, and so on. This is the default value for Auto Scaling groups that donât specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) and cannot be used for groups that do.

OnDemandBaseCapacity -> (integer)

The minimum amount of the Auto Scaling groupâs capacity that must be fulfilled by On-Demand Instances. This base portion is launched first as your group scales.

This number has the same unit of measurement as the groupâs desired capacity. If you change the default unit of measurement (number of instances) by specifying weighted capacity values in your launch template overrides list, or by changing the default desired capacity type setting of the group, you must specify this number using the same unit of measurement.

Default: 0

OnDemandPercentageAboveBaseCapacity -> (integer)

Controls the percentages of On-Demand Instances and Spot Instances for your additional capacity beyond `OnDemandBaseCapacity` . Expressed as a number (for example, 20 specifies 20% On-Demand Instances, 80% Spot Instances). If set to 100, only On-Demand Instances are used.

Default: 100

SpotAllocationStrategy -> (string)

The allocation strategy to apply to your Spot Instances when they are launched. Possible instance types are determined by the launch template overrides that you specify.

The following lists the valid values:

capacity-optimized

Requests Spot Instances using pools that are optimally chosen based on the available Spot capacity. This strategy has the lowest risk of interruption. To give certain instance types a higher chance of launching first, use `capacity-optimized-prioritized` .

capacity-optimized-prioritized

You set the order of instance types for the launch template overrides from highest to lowest priority (from first to last in the list). Amazon EC2 Auto Scaling honors the instance type priorities on a best effort basis but optimizes for capacity first. Note that if the On-Demand allocation strategy is set to `prioritized` , the same priority is applied when fulfilling On-Demand capacity. This is not a valid value for Auto Scaling groups that specify [InstanceRequirements](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstanceRequirements.html) .

lowest-price

Requests Spot Instances using the lowest priced pools within an Availability Zone, across the number of Spot pools that you specify for the `SpotInstancePools` property. To ensure that your desired capacity is met, you might receive Spot Instances from several pools. This is the default value, but it might lead to high interruption rates because this strategy only considers instance price and not available capacity.

price-capacity-optimized (recommended)

The price and capacity optimized allocation strategy looks at both price and capacity to select the Spot Instance pools that are the least likely to be interrupted and have the lowest possible price.

SpotInstancePools -> (integer)

The number of Spot Instance pools across which to allocate your Spot Instances. The Spot pools are determined from the different instance types in the overrides. Valid only when the `SpotAllocationStrategy` is `lowest-price` . Value must be in the range of 1â20.

Default: 2

SpotMaxPrice -> (string)

The maximum price per unit hour that you are willing to pay for a Spot Instance. If your maximum price is lower than the Spot price for the instance types that you selected, your Spot Instances are not launched. We do not recommend specifying a maximum price because it can lead to increased interruptions. When Spot Instances launch, you pay the current Spot price. To remove a maximum price that you previously set, include the property but specify an empty string (ââ) for the value.

### Warning

If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify one.

Valid Range: Minimum value of 0.001

MinSize -> (integer)

The minimum size of the group.

MaxSize -> (integer)

The maximum size of the group.

DesiredCapacity -> (integer)

The desired size of the group.

PredictedCapacity -> (integer)

The predicted capacity of the group when it has a predictive scaling policy.

DefaultCooldown -> (integer)

The duration of the default cooldown period, in seconds.

AvailabilityZones -> (list)

One or more Availability Zones for the group.

(string)

LoadBalancerNames -> (list)

One or more load balancers associated with the group.

(string)

TargetGroupARNs -> (list)

The Amazon Resource Names (ARN) of the target groups for your load balancer.

(string)

HealthCheckType -> (string)

A comma-separated value string of one or more health check types.

HealthCheckGracePeriod -> (integer)

The duration of the health check grace period, in seconds.

Instances -> (list)

The EC2 instances associated with the group.

(structure)

Describes an EC2 instance.

InstanceId -> (string)

The ID of the instance.

InstanceType -> (string)

The instance type of the EC2 instance.

AvailabilityZone -> (string)

The Availability Zone in which the instance is running.

LifecycleState -> (string)

A description of the current lifecycle state. The `Quarantined` state is not used. For more information, see [Amazon EC2 Auto Scaling instance lifecycle](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-lifecycle.html) in the *Amazon EC2 Auto Scaling User Guide* .

HealthStatus -> (string)

The last reported health status of the instance. `Healthy` means that the instance is healthy and should remain in service. `Unhealthy` means that the instance is unhealthy and that Amazon EC2 Auto Scaling should terminate and replace it.

LaunchConfigurationName -> (string)

The launch configuration associated with the instance.

LaunchTemplate -> (structure)

The launch template for the instance.

LaunchTemplateId -> (string)

The ID of the launch template. To get the template ID, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

LaunchTemplateName -> (string)

The name of the launch template. To get the template name, use the Amazon EC2 [DescribeLaunchTemplates](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplates.html) API operation. New launch templates can be created using the Amazon EC2 [CreateLaunchTemplate](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplate.html) API.

Conditional: You must specify either a `LaunchTemplateId` or a `LaunchTemplateName` .

Version -> (string)

The version number, `$Latest` , or `$Default` . To get the version number, use the Amazon EC2 [DescribeLaunchTemplateVersions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeLaunchTemplateVersions.html) API operation. New launch template versions can be created using the Amazon EC2 [CreateLaunchTemplateVersion](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateLaunchTemplateVersion.html) API. If the value is `$Latest` , Amazon EC2 Auto Scaling selects the latest version of the launch template when launching instances. If the value is `$Default` , Amazon EC2 Auto Scaling selects the default version of the launch template when launching instances. The default value is `$Default` .

ProtectedFromScaleIn -> (boolean)

Indicates whether the instance is protected from termination by Amazon EC2 Auto Scaling when scaling in.

WeightedCapacity -> (string)

The number of capacity units contributed by the instance based on its instance type.

Valid Range: Minimum value of 1. Maximum value of 999.

CreatedTime -> (timestamp)

The date and time the group was created.

SuspendedProcesses -> (list)

The suspended processes associated with the group.

(structure)

Describes an auto scaling process that has been suspended.

For more information, see [Types of processes](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-suspend-resume-processes.html#process-types) in the *Amazon EC2 Auto Scaling User Guide* .

ProcessName -> (string)

The name of the suspended process.

SuspensionReason -> (string)

The reason that the process was suspended.

PlacementGroup -> (string)

The name of the placement group into which to launch your instances, if any.

VPCZoneIdentifier -> (string)

One or more subnet IDs, if applicable, separated by commas.

EnabledMetrics -> (list)

The metrics enabled for the group.

(structure)

Describes an enabled Auto Scaling group metric.

Metric -> (string)

One of the following metrics:

- `GroupMinSize`
- `GroupMaxSize`
- `GroupDesiredCapacity`
- `GroupInServiceInstances`
- `GroupPendingInstances`
- `GroupStandbyInstances`
- `GroupTerminatingInstances`
- `GroupTotalInstances`
- `GroupInServiceCapacity`
- `GroupPendingCapacity`
- `GroupStandbyCapacity`
- `GroupTerminatingCapacity`
- `GroupTotalCapacity`
- `WarmPoolDesiredCapacity`
- `WarmPoolWarmedCapacity`
- `WarmPoolPendingCapacity`
- `WarmPoolTerminatingCapacity`
- `WarmPoolTotalCapacity`
- `GroupAndWarmPoolDesiredCapacity`
- `GroupAndWarmPoolTotalCapacity`

For more information, see [Amazon CloudWatch metrics for Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-metrics.html) in the *Amazon EC2 Auto Scaling User Guide* .

Granularity -> (string)

The granularity of the metric. The only valid value is `1Minute` .

Status -> (string)

The current state of the group when the [DeleteAutoScalingGroup](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_DeleteAutoScalingGroup.html) operation is in progress.

Tags -> (list)

The tags for the group.

(structure)

Describes a tag for an Auto Scaling group.

ResourceId -> (string)

The name of the group.

ResourceType -> (string)

The type of resource. The only supported value is `auto-scaling-group` .

Key -> (string)

The tag key.

Value -> (string)

The tag value.

PropagateAtLaunch -> (boolean)

Determines whether the tag is added to new instances as they are launched in the group.

TerminationPolicies -> (list)

The termination policies for the group.

(string)

NewInstancesProtectedFromScaleIn -> (boolean)

Indicates whether newly launched instances are protected from termination by Amazon EC2 Auto Scaling when scaling in. For more information about preventing instances from terminating on scale in, see [Use instance scale-in protection](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-instance-protection.html) in the *Amazon EC2 Auto Scaling User Guide* .

ServiceLinkedRoleARN -> (string)

The Amazon Resource Name (ARN) of the service-linked role that the Auto Scaling group uses to call other Amazon Web Services on your behalf.

MaxInstanceLifetime -> (integer)

The maximum amount of time, in seconds, that an instance can be in service.

Valid Range: Minimum value of 0.

CapacityRebalance -> (boolean)

Indicates whether Capacity Rebalancing is enabled.

WarmPoolConfiguration -> (structure)

The warm pool for the group.

MaxGroupPreparedCapacity -> (integer)

The maximum number of instances that are allowed to be in the warm pool or in any state except `Terminated` for the Auto Scaling group.

MinSize -> (integer)

The minimum number of instances to maintain in the warm pool.

PoolState -> (string)

The instance state to transition to after the lifecycle actions are complete.

Status -> (string)

The status of a warm pool that is marked for deletion.

InstanceReusePolicy -> (structure)

The instance reuse policy.

ReuseOnScaleIn -> (boolean)

Specifies whether instances in the Auto Scaling group can be returned to the warm pool on scale in.

WarmPoolSize -> (integer)

The current size of the warm pool.

Context -> (string)

Reserved.

DesiredCapacityType -> (string)

The unit of measurement for the value specified for desired capacity. Amazon EC2 Auto Scaling supports `DesiredCapacityType` for attribute-based instance type selection only.

DefaultInstanceWarmup -> (integer)

The duration of the default instance warmup, in seconds.

TrafficSources -> (list)

The traffic sources associated with this Auto Scaling group.

(structure)

Identifying information for a traffic source.

Identifier -> (string)

Identifies the traffic source.

For Application Load Balancers, Gateway Load Balancers, Network Load Balancers, and VPC Lattice, this will be the Amazon Resource Name (ARN) for a target group in this account and Region. For Classic Load Balancers, this will be the name of the Classic Load Balancer in this account and Region.

For example:

- Application Load Balancer ARN: `arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/1234567890123456`
- Classic Load Balancer name: `my-classic-load-balancer`
- VPC Lattice ARN: `arn:aws:vpc-lattice:us-west-2:123456789012:targetgroup/tg-1234567890123456`

To get the ARN of a target group for a Application Load Balancer, Gateway Load Balancer, or Network Load Balancer, or the name of a Classic Load Balancer, use the Elastic Load Balancing [DescribeTargetGroups](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeTargetGroups.html) and [DescribeLoadBalancers](https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_DescribeLoadBalancers.html) API operations.

To get the ARN of a target group for VPC Lattice, use the VPC Lattice [GetTargetGroup](https://docs.aws.amazon.com/vpc-lattice/latest/APIReference/API_GetTargetGroup.html) API operation.

Type -> (string)

Provides additional context for the value of `Identifier` .

The following lists the valid values:

- `elb` if `Identifier` is the name of a Classic Load Balancer.
- `elbv2` if `Identifier` is the ARN of an Application Load Balancer, Gateway Load Balancer, or Network Load Balancer target group.
- `vpc-lattice` if `Identifier` is the ARN of a VPC Lattice target group.

Required if the identifier is the name of a Classic Load Balancer.

InstanceMaintenancePolicy -> (structure)

An instance maintenance policy.

MinHealthyPercentage -> (integer)

Specifies the lower threshold as a percentage of the desired capacity of the Auto Scaling group. It represents the minimum percentage of the group to keep in service, healthy, and ready to use to support your workload when replacing instances. Value range is 0 to 100. To clear a previously set value, specify a value of `-1` .

MaxHealthyPercentage -> (integer)

Specifies the upper threshold as a percentage of the desired capacity of the Auto Scaling group. It represents the maximum percentage of the group that can be in service and healthy, or pending, to support your workload when replacing instances. Value range is 100 to 200. To clear a previously set value, specify a value of `-1` .

Both `MinHealthyPercentage` and `MaxHealthyPercentage` must be specified, and the difference between them cannot be greater than 100. A large range increases the number of instances that can be replaced at the same time.

AvailabilityZoneDistribution -> (structure)

The instance capacity distribution across Availability Zones.

CapacityDistributionStrategy -> (string)

If launches fail in an Availability Zone, the following strategies are available. The default is `balanced-best-effort` .

- `balanced-only` - If launches fail in an Availability Zone, Auto Scaling will continue to attempt to launch in the unhealthy zone to preserve a balanced distribution.
- `balanced-best-effort` - If launches fail in an Availability Zone, Auto Scaling will attempt to launch in another healthy Availability Zone instead.

AvailabilityZoneImpairmentPolicy -> (structure)

The Availability Zone impairment policy.

ZonalShiftEnabled -> (boolean)

If `true` , enable zonal shift for your Auto Scaling group.

ImpairedZoneHealthCheckBehavior -> (string)

Specifies the health check behavior for the impaired Availability Zone in an active zonal shift. If you select `Replace unhealthy` , instances that appear unhealthy will be replaced in all Availability Zones. If you select `Ignore unhealthy` , instances will not be replaced in the Availability Zone with the active zonal shift. For more information, see [Auto Scaling group zonal shift](https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-zonal-shift.html) in the *Amazon EC2 Auto Scaling User Guide* .

CapacityReservationSpecification -> (structure)

The capacity reservation specification.

CapacityReservationPreference -> (string)

The capacity reservation preference. The following options are available:

- `capacity-reservations-only` - Auto Scaling will only launch instances into a Capacity Reservation or Capacity Reservation resource group. If capacity isnât available, instances will fail to launch.
- `capacity-reservations-first` - Auto Scaling will try to launch instances into a Capacity Reservation or Capacity Reservation resource group first. If capacity isnât available, instances will run in On-Demand capacity.
- `none` - Auto Scaling will not launch instances into a Capacity Reservation. Instances will run in On-Demand capacity.
- `default` - Auto Scaling uses the Capacity Reservation preference from your launch template or an open Capacity Reservation.

CapacityReservationTarget -> (structure)

Describes a target Capacity Reservation or Capacity Reservation resource group.

CapacityReservationIds -> (list)

The Capacity Reservation IDs to launch instances into.

(string)

CapacityReservationResourceGroupArns -> (list)

The resource group ARNs of the Capacity Reservation to launch instances into.

(string)

NextToken -> (string)

A string that indicates that the response contains more items than can be returned in a single response. To receive additional items, specify this string for the `NextToken` value when requesting the next set of items. This value is null when there are no more items to return.