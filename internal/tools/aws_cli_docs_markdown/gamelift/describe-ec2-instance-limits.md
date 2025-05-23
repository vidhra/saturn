# describe-ec2-instance-limitsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-ec2-instance-limits.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/describe-ec2-instance-limits.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# describe-ec2-instance-limits

## Description

Retrieves the instance limits and current utilization for an Amazon Web Services Region or location. Instance limits control the number of instances, per instance type, per location, that your Amazon Web Services account can use. Learn more at [Amazon EC2 Instance Types](http://aws.amazon.com/ec2/instance-types/) . The information returned includes the maximum number of instances allowed and your accountâs current usage across all fleets. This information can affect your ability to scale your Amazon GameLift fleets. You can request a limit increase for your account by using the **Service limits** page in the Amazon GameLift console.

Instance limits differ based on whether the instances are deployed in a fleetâs home Region or in a remote location. For remote locations, limits also differ based on the combination of home Region and remote location. All requests must specify an Amazon Web Services Region (either explicitly or as your default settings). To get the limit for a remote location, you must also specify the location. For example, the following requests all return different results:

- Request specifies the Region `ap-northeast-1` with no location. The result is limits and usage data on all instance types that are deployed in `us-east-2` , by all of the fleets that reside in `ap-northeast-1` .
- Request specifies the Region `us-east-1` with location `ca-central-1` . The result is limits and usage data on all instance types that are deployed in `ca-central-1` , by all of the fleets that reside in `us-east-2` . These limits do not affect fleets in any other Regions that deploy instances to `ca-central-1` .
- Request specifies the Region `eu-west-1` with location `ca-central-1` . The result is limits and usage data on all instance types that are deployed in `ca-central-1` , by all of the fleets that reside in `eu-west-1` .

This operation can be used in the following ways:

- To get limit and usage data for all instance types that are deployed in an Amazon Web Services Region by fleets that reside in the same Region: Specify the Region only. Optionally, specify a single instance type to retrieve information for.
- To get limit and usage data for all instance types that are deployed to a remote location by fleets that reside in different Amazon Web Services Region: Provide both the Amazon Web Services Region and the remote location. Optionally, specify a single instance type to retrieve information for.

If successful, an `EC2InstanceLimits` object is returned with limits and usage data for each requested instance type.

**Learn more**

[Setting up Amazon GameLift fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/DescribeEC2InstanceLimits)

## Synopsis

```
describe-ec2-instance-limits
[--ec2-instance-type <value>]
[--location <value>]
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

`--ec2-instance-type` (string)

Name of an Amazon EC2 instance type that is supported in Amazon GameLift. A fleet instance type determines the computing resources of each instance in the fleet, including CPU, memory, storage, and networking capacity. Do not specify a value for this parameter to retrieve limits for all instance types.

Possible values:

- `t2.micro`
- `t2.small`
- `t2.medium`
- `t2.large`
- `c3.large`
- `c3.xlarge`
- `c3.2xlarge`
- `c3.4xlarge`
- `c3.8xlarge`
- `c4.large`
- `c4.xlarge`
- `c4.2xlarge`
- `c4.4xlarge`
- `c4.8xlarge`
- `c5.large`
- `c5.xlarge`
- `c5.2xlarge`
- `c5.4xlarge`
- `c5.9xlarge`
- `c5.12xlarge`
- `c5.18xlarge`
- `c5.24xlarge`
- `c5a.large`
- `c5a.xlarge`
- `c5a.2xlarge`
- `c5a.4xlarge`
- `c5a.8xlarge`
- `c5a.12xlarge`
- `c5a.16xlarge`
- `c5a.24xlarge`
- `r3.large`
- `r3.xlarge`
- `r3.2xlarge`
- `r3.4xlarge`
- `r3.8xlarge`
- `r4.large`
- `r4.xlarge`
- `r4.2xlarge`
- `r4.4xlarge`
- `r4.8xlarge`
- `r4.16xlarge`
- `r5.large`
- `r5.xlarge`
- `r5.2xlarge`
- `r5.4xlarge`
- `r5.8xlarge`
- `r5.12xlarge`
- `r5.16xlarge`
- `r5.24xlarge`
- `r5a.large`
- `r5a.xlarge`
- `r5a.2xlarge`
- `r5a.4xlarge`
- `r5a.8xlarge`
- `r5a.12xlarge`
- `r5a.16xlarge`
- `r5a.24xlarge`
- `m3.medium`
- `m3.large`
- `m3.xlarge`
- `m3.2xlarge`
- `m4.large`
- `m4.xlarge`
- `m4.2xlarge`
- `m4.4xlarge`
- `m4.10xlarge`
- `m5.large`
- `m5.xlarge`
- `m5.2xlarge`
- `m5.4xlarge`
- `m5.8xlarge`
- `m5.12xlarge`
- `m5.16xlarge`
- `m5.24xlarge`
- `m5a.large`
- `m5a.xlarge`
- `m5a.2xlarge`
- `m5a.4xlarge`
- `m5a.8xlarge`
- `m5a.12xlarge`
- `m5a.16xlarge`
- `m5a.24xlarge`
- `c5d.large`
- `c5d.xlarge`
- `c5d.2xlarge`
- `c5d.4xlarge`
- `c5d.9xlarge`
- `c5d.12xlarge`
- `c5d.18xlarge`
- `c5d.24xlarge`
- `c6a.large`
- `c6a.xlarge`
- `c6a.2xlarge`
- `c6a.4xlarge`
- `c6a.8xlarge`
- `c6a.12xlarge`
- `c6a.16xlarge`
- `c6a.24xlarge`
- `c6i.large`
- `c6i.xlarge`
- `c6i.2xlarge`
- `c6i.4xlarge`
- `c6i.8xlarge`
- `c6i.12xlarge`
- `c6i.16xlarge`
- `c6i.24xlarge`
- `r5d.large`
- `r5d.xlarge`
- `r5d.2xlarge`
- `r5d.4xlarge`
- `r5d.8xlarge`
- `r5d.12xlarge`
- `r5d.16xlarge`
- `r5d.24xlarge`
- `m6g.medium`
- `m6g.large`
- `m6g.xlarge`
- `m6g.2xlarge`
- `m6g.4xlarge`
- `m6g.8xlarge`
- `m6g.12xlarge`
- `m6g.16xlarge`
- `c6g.medium`
- `c6g.large`
- `c6g.xlarge`
- `c6g.2xlarge`
- `c6g.4xlarge`
- `c6g.8xlarge`
- `c6g.12xlarge`
- `c6g.16xlarge`
- `r6g.medium`
- `r6g.large`
- `r6g.xlarge`
- `r6g.2xlarge`
- `r6g.4xlarge`
- `r6g.8xlarge`
- `r6g.12xlarge`
- `r6g.16xlarge`
- `c6gn.medium`
- `c6gn.large`
- `c6gn.xlarge`
- `c6gn.2xlarge`
- `c6gn.4xlarge`
- `c6gn.8xlarge`
- `c6gn.12xlarge`
- `c6gn.16xlarge`
- `c7g.medium`
- `c7g.large`
- `c7g.xlarge`
- `c7g.2xlarge`
- `c7g.4xlarge`
- `c7g.8xlarge`
- `c7g.12xlarge`
- `c7g.16xlarge`
- `r7g.medium`
- `r7g.large`
- `r7g.xlarge`
- `r7g.2xlarge`
- `r7g.4xlarge`
- `r7g.8xlarge`
- `r7g.12xlarge`
- `r7g.16xlarge`
- `m7g.medium`
- `m7g.large`
- `m7g.xlarge`
- `m7g.2xlarge`
- `m7g.4xlarge`
- `m7g.8xlarge`
- `m7g.12xlarge`
- `m7g.16xlarge`
- `g5g.xlarge`
- `g5g.2xlarge`
- `g5g.4xlarge`
- `g5g.8xlarge`
- `g5g.16xlarge`
- `r6i.large`
- `r6i.xlarge`
- `r6i.2xlarge`
- `r6i.4xlarge`
- `r6i.8xlarge`
- `r6i.12xlarge`
- `r6i.16xlarge`
- `c6gd.medium`
- `c6gd.large`
- `c6gd.xlarge`
- `c6gd.2xlarge`
- `c6gd.4xlarge`
- `c6gd.8xlarge`
- `c6gd.12xlarge`
- `c6gd.16xlarge`
- `c6in.large`
- `c6in.xlarge`
- `c6in.2xlarge`
- `c6in.4xlarge`
- `c6in.8xlarge`
- `c6in.12xlarge`
- `c6in.16xlarge`
- `c7a.medium`
- `c7a.large`
- `c7a.xlarge`
- `c7a.2xlarge`
- `c7a.4xlarge`
- `c7a.8xlarge`
- `c7a.12xlarge`
- `c7a.16xlarge`
- `c7gd.medium`
- `c7gd.large`
- `c7gd.xlarge`
- `c7gd.2xlarge`
- `c7gd.4xlarge`
- `c7gd.8xlarge`
- `c7gd.12xlarge`
- `c7gd.16xlarge`
- `c7gn.medium`
- `c7gn.large`
- `c7gn.xlarge`
- `c7gn.2xlarge`
- `c7gn.4xlarge`
- `c7gn.8xlarge`
- `c7gn.12xlarge`
- `c7gn.16xlarge`
- `c7i.large`
- `c7i.xlarge`
- `c7i.2xlarge`
- `c7i.4xlarge`
- `c7i.8xlarge`
- `c7i.12xlarge`
- `c7i.16xlarge`
- `m6a.large`
- `m6a.xlarge`
- `m6a.2xlarge`
- `m6a.4xlarge`
- `m6a.8xlarge`
- `m6a.12xlarge`
- `m6a.16xlarge`
- `m6gd.medium`
- `m6gd.large`
- `m6gd.xlarge`
- `m6gd.2xlarge`
- `m6gd.4xlarge`
- `m6gd.8xlarge`
- `m6gd.12xlarge`
- `m6gd.16xlarge`
- `m6i.large`
- `m6i.xlarge`
- `m6i.2xlarge`
- `m6i.4xlarge`
- `m6i.8xlarge`
- `m6i.12xlarge`
- `m6i.16xlarge`
- `m7a.medium`
- `m7a.large`
- `m7a.xlarge`
- `m7a.2xlarge`
- `m7a.4xlarge`
- `m7a.8xlarge`
- `m7a.12xlarge`
- `m7a.16xlarge`
- `m7gd.medium`
- `m7gd.large`
- `m7gd.xlarge`
- `m7gd.2xlarge`
- `m7gd.4xlarge`
- `m7gd.8xlarge`
- `m7gd.12xlarge`
- `m7gd.16xlarge`
- `m7i.large`
- `m7i.xlarge`
- `m7i.2xlarge`
- `m7i.4xlarge`
- `m7i.8xlarge`
- `m7i.12xlarge`
- `m7i.16xlarge`
- `r6gd.medium`
- `r6gd.large`
- `r6gd.xlarge`
- `r6gd.2xlarge`
- `r6gd.4xlarge`
- `r6gd.8xlarge`
- `r6gd.12xlarge`
- `r6gd.16xlarge`
- `r7a.medium`
- `r7a.large`
- `r7a.xlarge`
- `r7a.2xlarge`
- `r7a.4xlarge`
- `r7a.8xlarge`
- `r7a.12xlarge`
- `r7a.16xlarge`
- `r7gd.medium`
- `r7gd.large`
- `r7gd.xlarge`
- `r7gd.2xlarge`
- `r7gd.4xlarge`
- `r7gd.8xlarge`
- `r7gd.12xlarge`
- `r7gd.16xlarge`
- `r7i.large`
- `r7i.xlarge`
- `r7i.2xlarge`
- `r7i.4xlarge`
- `r7i.8xlarge`
- `r7i.12xlarge`
- `r7i.16xlarge`
- `r7i.24xlarge`
- `r7i.48xlarge`
- `c5ad.large`
- `c5ad.xlarge`
- `c5ad.2xlarge`
- `c5ad.4xlarge`
- `c5ad.8xlarge`
- `c5ad.12xlarge`
- `c5ad.16xlarge`
- `c5ad.24xlarge`
- `c5n.large`
- `c5n.xlarge`
- `c5n.2xlarge`
- `c5n.4xlarge`
- `c5n.9xlarge`
- `c5n.18xlarge`
- `r5ad.large`
- `r5ad.xlarge`
- `r5ad.2xlarge`
- `r5ad.4xlarge`
- `r5ad.8xlarge`
- `r5ad.12xlarge`
- `r5ad.16xlarge`
- `r5ad.24xlarge`
- `c6id.large`
- `c6id.xlarge`
- `c6id.2xlarge`
- `c6id.4xlarge`
- `c6id.8xlarge`
- `c6id.12xlarge`
- `c6id.16xlarge`
- `c6id.24xlarge`
- `c6id.32xlarge`
- `c8g.medium`
- `c8g.large`
- `c8g.xlarge`
- `c8g.2xlarge`
- `c8g.4xlarge`
- `c8g.8xlarge`
- `c8g.12xlarge`
- `c8g.16xlarge`
- `c8g.24xlarge`
- `c8g.48xlarge`
- `m5ad.large`
- `m5ad.xlarge`
- `m5ad.2xlarge`
- `m5ad.4xlarge`
- `m5ad.8xlarge`
- `m5ad.12xlarge`
- `m5ad.16xlarge`
- `m5ad.24xlarge`
- `m5d.large`
- `m5d.xlarge`
- `m5d.2xlarge`
- `m5d.4xlarge`
- `m5d.8xlarge`
- `m5d.12xlarge`
- `m5d.16xlarge`
- `m5d.24xlarge`
- `m5dn.large`
- `m5dn.xlarge`
- `m5dn.2xlarge`
- `m5dn.4xlarge`
- `m5dn.8xlarge`
- `m5dn.12xlarge`
- `m5dn.16xlarge`
- `m5dn.24xlarge`
- `m5n.large`
- `m5n.xlarge`
- `m5n.2xlarge`
- `m5n.4xlarge`
- `m5n.8xlarge`
- `m5n.12xlarge`
- `m5n.16xlarge`
- `m5n.24xlarge`
- `m6id.large`
- `m6id.xlarge`
- `m6id.2xlarge`
- `m6id.4xlarge`
- `m6id.8xlarge`
- `m6id.12xlarge`
- `m6id.16xlarge`
- `m6id.24xlarge`
- `m6id.32xlarge`
- `m6idn.large`
- `m6idn.xlarge`
- `m6idn.2xlarge`
- `m6idn.4xlarge`
- `m6idn.8xlarge`
- `m6idn.12xlarge`
- `m6idn.16xlarge`
- `m6idn.24xlarge`
- `m6idn.32xlarge`
- `m6in.large`
- `m6in.xlarge`
- `m6in.2xlarge`
- `m6in.4xlarge`
- `m6in.8xlarge`
- `m6in.12xlarge`
- `m6in.16xlarge`
- `m6in.24xlarge`
- `m6in.32xlarge`
- `m8g.medium`
- `m8g.large`
- `m8g.xlarge`
- `m8g.2xlarge`
- `m8g.4xlarge`
- `m8g.8xlarge`
- `m8g.12xlarge`
- `m8g.16xlarge`
- `m8g.24xlarge`
- `m8g.48xlarge`
- `r5dn.large`
- `r5dn.xlarge`
- `r5dn.2xlarge`
- `r5dn.4xlarge`
- `r5dn.8xlarge`
- `r5dn.12xlarge`
- `r5dn.16xlarge`
- `r5dn.24xlarge`
- `r5n.large`
- `r5n.xlarge`
- `r5n.2xlarge`
- `r5n.4xlarge`
- `r5n.8xlarge`
- `r5n.12xlarge`
- `r5n.16xlarge`
- `r5n.24xlarge`
- `r6a.large`
- `r6a.xlarge`
- `r6a.2xlarge`
- `r6a.4xlarge`
- `r6a.8xlarge`
- `r6a.12xlarge`
- `r6a.16xlarge`
- `r6a.24xlarge`
- `r6a.32xlarge`
- `r6a.48xlarge`
- `r6id.large`
- `r6id.xlarge`
- `r6id.2xlarge`
- `r6id.4xlarge`
- `r6id.8xlarge`
- `r6id.12xlarge`
- `r6id.16xlarge`
- `r6id.24xlarge`
- `r6id.32xlarge`
- `r6idn.large`
- `r6idn.xlarge`
- `r6idn.2xlarge`
- `r6idn.4xlarge`
- `r6idn.8xlarge`
- `r6idn.12xlarge`
- `r6idn.16xlarge`
- `r6idn.24xlarge`
- `r6idn.32xlarge`
- `r6in.large`
- `r6in.xlarge`
- `r6in.2xlarge`
- `r6in.4xlarge`
- `r6in.8xlarge`
- `r6in.12xlarge`
- `r6in.16xlarge`
- `r6in.24xlarge`
- `r6in.32xlarge`
- `r8g.medium`
- `r8g.large`
- `r8g.xlarge`
- `r8g.2xlarge`
- `r8g.4xlarge`
- `r8g.8xlarge`
- `r8g.12xlarge`
- `r8g.16xlarge`
- `r8g.24xlarge`
- `r8g.48xlarge`
- `m4.16xlarge`
- `c6a.32xlarge`
- `c6a.48xlarge`
- `c6i.32xlarge`
- `r6i.24xlarge`
- `r6i.32xlarge`
- `c6in.24xlarge`
- `c6in.32xlarge`
- `c7a.24xlarge`
- `c7a.32xlarge`
- `c7a.48xlarge`
- `c7i.24xlarge`
- `c7i.48xlarge`
- `m6a.24xlarge`
- `m6a.32xlarge`
- `m6a.48xlarge`
- `m6i.24xlarge`
- `m6i.32xlarge`
- `m7a.24xlarge`
- `m7a.32xlarge`
- `m7a.48xlarge`
- `m7i.24xlarge`
- `m7i.48xlarge`
- `r7a.24xlarge`
- `r7a.32xlarge`
- `r7a.48xlarge`

`--location` (string)

The name of a remote location to request instance limits for, in the form of an Amazon Web Services Region code such as `us-west-2` .

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

**To retrieve service limits for an EC2 instance type**

The following `describe-ec2-instance-limits` example displays the maximum allowed instances and current instances in use for the specified EC2 instance type in the current Region. The result indicates that only five of the allowed twenty instances are being used.

```
aws gamelift describe-ec2-instance-limits \
    --ec2-instance-type m5.large
```

Output:

```
{
    "EC2InstanceLimits": [
        {
            "EC2InstanceType": ""m5.large",
            "CurrentInstances": 5,
            "InstanceLimit": 20
        }
    ]
}
```

For more information, see [Choose Computing Resources](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-ec2-instances.html) in the *Amazon GameLift Developer Guide*.

## Output

EC2InstanceLimits -> (list)

The maximum number of instances for the specified instance type.

(structure)

The Amazon GameLift service limits for an Amazon EC2 instance type and current utilization. Amazon GameLift allows Amazon Web Services accounts a maximum number of instances, per instance type, per Amazon Web Services Region or location, for use with Amazon GameLift. You can request an limit increase for your account by using the **Service limits** page in the Amazon GameLift console.

EC2InstanceType -> (string)

The name of an Amazon EC2 instance type. See [Amazon Elastic Compute Cloud Instance Types](http://aws.amazon.com/ec2/instance-types/) for detailed descriptions.

CurrentInstances -> (integer)

The number of instances for the specified type and location that are currently being used by the Amazon Web Services account.

InstanceLimit -> (integer)

The number of instances that is allowed for the specified instance type and location.

Location -> (string)

An Amazon Web Services Region code, such as `us-west-2` .