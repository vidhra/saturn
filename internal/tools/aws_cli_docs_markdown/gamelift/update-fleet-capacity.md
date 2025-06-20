# update-fleet-capacityÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-fleet-capacity.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-fleet-capacity.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# update-fleet-capacity

## Description

Updates capacity settings for a managed EC2 fleet or managed container fleet. For these fleets, you adjust capacity by changing the number of instances in the fleet. Fleet capacity determines the number of game sessions and players that the fleet can host based on its configuration. For fleets with multiple locations, use this operation to manage capacity settings in each location individually.

Use this operation to set these fleet capacity properties:

- Minimum/maximum size: Set hard limits on the number of Amazon EC2 instances allowed. If Amazon GameLift receives a requestâeither through manual update or automatic scalingâit wonât change the capacity to a value outside of this range.
- Desired capacity: As an alternative to automatic scaling, manually set the number of Amazon EC2 instances to be maintained. Before changing a fleetâs desired capacity, check the maximum capacity of the fleetâs Amazon EC2 instance type by calling [DescribeEC2InstanceLimits](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeEC2InstanceLimits.html) .

To update capacity for a fleetâs home Region, or if the fleet has no remote locations, omit the `Location` parameter. The fleet must be in `ACTIVE` status.

To update capacity for a fleetâs remote location, set the `Location` parameter to the location to update. The location must be in `ACTIVE` status.

If successful, Amazon GameLift updates the capacity settings and returns the identifiers for the updated fleet and/or location. If a requested change to desired capacity exceeds the instance typeâs limit, the `LimitExceeded` exception occurs.

Updates often prompt an immediate change in fleet capacity, such as when current capacity is different than the new desired capacity or outside the new limits. In this scenario, Amazon GameLift automatically initiates steps to add or remove instances in the fleet location. You can track a fleetâs current capacity by calling [DescribeFleetCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetCapacity.html) or [DescribeFleetLocationCapacity](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetLocationCapacity.html) .

**Learn more**

[Scaling fleet capacity](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-manage-capacity.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateFleetCapacity)

## Synopsis

```
update-fleet-capacity
--fleet-id <value>
[--desired-instances <value>]
[--min-size <value>]
[--max-size <value>]
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

`--fleet-id` (string)

A unique identifier for the fleet to update capacity settings for. You can use either the fleet ID or ARN value.

`--desired-instances` (integer)

The number of Amazon EC2 instances you want to maintain in the specified fleet location. This value must fall between the minimum and maximum size limits. Changes in desired instance value can take up to 1 minute to be reflected when viewing the fleetâs capacity settings.

`--min-size` (integer)

The minimum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 0.

`--max-size` (integer)

The maximum number of instances that are allowed in the specified fleet location. If this parameter is not set, the default is 1.

`--location` (string)

The name of a remote location to update fleet capacity settings for, in the form of an Amazon Web Services Region code such as `us-west-2` .

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

FleetId -> (string)

A unique identifier for the fleet that was updated.

FleetArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to a Amazon GameLift fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912` .

Location -> (string)

The remote location being updated, expressed as an Amazon Web Services Region code, such as `us-west-2` .