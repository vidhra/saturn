# modify-instance-placementÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-placement.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/modify-instance-placement.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# modify-instance-placement

## Description

Modifies the placement attributes for a specified instance. You can do the following:

- Modify the affinity between an instance and a [Dedicated Host](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-overview.html) . When affinity is set to `host` and the instance is not associated with a specific Dedicated Host, the next time the instance is started, it is automatically associated with the host on which it lands. If the instance is restarted or rebooted, this relationship persists.
- Change the Dedicated Host with which an instance is associated.
- Change the instance tenancy of an instance.
- Move an instance to or from a [placement group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html) .

At least one attribute for affinity, host ID, tenancy, or placement group name must be specified in the request. Affinity and tenancy can be modified in the same request.

To modify the host ID, tenancy, placement group, or partition for an instance, the instance must be in the `stopped` state.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/ModifyInstancePlacement)

## Synopsis

```
modify-instance-placement
[--group-name <value>]
[--partition-number <value>]
[--host-resource-group-arn <value>]
[--group-id <value>]
--instance-id <value>
[--tenancy <value>]
[--affinity <value>]
[--host-id <value>]
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

`--group-name` (string)

The name of the placement group in which to place the instance. For spread placement groups, the instance must have a tenancy of `default` . For cluster and partition placement groups, the instance must have a tenancy of `default` or `dedicated` .

To remove an instance from a placement group, specify an empty string (ââ).

`--partition-number` (integer)

The number of the partition in which to place the instance. Valid only if the placement group strategy is set to `partition` .

`--host-resource-group-arn` (string)

The ARN of the host resource group in which to place the instance. The instance must have a tenancy of `host` to specify this parameter.

`--group-id` (string)

The Group Id of a placement group. You must specify the Placement Group **Group Id** to launch an instance in a shared placement group.

`--instance-id` (string)

The ID of the instance that you are modifying.

`--tenancy` (string)

The tenancy for the instance.

### Note

For T3 instances, you must launch the instance on a Dedicated Host to use a tenancy of `host` . You canât change the tenancy from `host` to `dedicated` or `default` . Attempting to make one of these unsupported tenancy changes results in an `InvalidRequest` error code.

Possible values:

- `default`
- `dedicated`
- `host`

`--affinity` (string)

The affinity setting for the instance. For more information, see [Host affinity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/how-dedicated-hosts-work.html#dedicated-hosts-affinity) in the *Amazon EC2 User Guide* .

Possible values:

- `default`
- `host`

`--host-id` (string)

The ID of the Dedicated Host with which to associate the instance.

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

**Example 1: To remove an instanceâs affinity with a Dedicated Host**

The following `modify-instance-placement` example removes an instanceâs affinity with a Dedicated Host and enables it to launch on any available Dedicated Host in your account that supports its instance type.

```
aws ec2 modify-instance-placement \
    --instance-id i-0e6ddf6187EXAMPLE \
    --affinity default
```

Output:

```
{
    "Return": true
}
```

**Example 2: To establish affinity between an instance and the specified Dedicated Host**

The following `modify-instance-placement` example establishes a launch relationship between an instance and a Dedicated Host. The instance is only able to run on the specified Dedicated Host.

```
aws ec2 modify-instance-placement \
    --instance-id i-0e6ddf6187EXAMPLE \
    --affinity host \
    --host-id i-0e6ddf6187EXAMPLE
```

Output:

```
{
    "Return": true
}
```

**Example 3: To move an instance to a placement group**

The following `modify-instance-placement` example moves an instance to a placement group, stop the instance, modify the instance placement, and then restart the instance.

```
aws ec2 stop-instances \
    --instance-ids i-0123a456700123456

aws ec2 modify-instance-placement \
    --instance-id i-0123a456700123456 \
    --group-name MySpreadGroup

aws ec2 start-instances \
    --instance-ids i-0123a456700123456
```

**Example 4: To remove an instance from a placement group**

The following `modify-instance-placement` example removes an instance from a placement group by stopping the instance, modifying the instance placement, and then restarting the instance. The following example specifies an empty string (ââ) for the placement group name to indicate that the instance is not to be located in a placement group.

Stop the instance:

```
aws ec2 stop-instances \
    --instance-ids i-0123a456700123456
```

Modify the placement (Windows Command Prompt):

```
aws ec2 modify-instance-placement \
    --instance-id i-0123a456700123456 \
    --group-name ""
```

Modify the placement (Windows PowerShell, Linux, and macOS):

```
aws ec2 modify-instance-placement `
    --instance-id i-0123a456700123456 `
    --group-name ''
```

Restart the instance:

```
aws ec2 start-instances \
    --instance-ids i-0123a456700123456
```

Output:

```
{
    "Return": true
}
```

For more information, see [Modify Dedicated Host tenancy and affinity](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/moving-instances-dedicated-hosts.html) in the *Amazon EC2 User Guide*.

## Output

Return -> (boolean)

Is `true` if the request succeeds, and an error otherwise.