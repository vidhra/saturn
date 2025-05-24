# update-fleet-port-settingsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-fleet-port-settings.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-fleet-port-settings.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# update-fleet-port-settings

## Description

Updates permissions that allow inbound traffic to connect to game sessions in the fleet.

To update settings, specify the fleet ID to be updated and specify the changes to be made. List the permissions you want to add in `InboundPermissionAuthorizations` , and permissions you want to remove in `InboundPermissionRevocations` . Permissions to be removed must match existing fleet permissions.

If successful, the fleet ID for the updated fleet is returned. For fleets with remote locations, port setting updates can take time to propagate across all locations. You can check the status of updates in each location by calling `DescribeFleetPortSettings` with a location name.

**Learn more**

[Setting up Amazon GameLift fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateFleetPortSettings)

## Synopsis

```
update-fleet-port-settings
--fleet-id <value>
[--inbound-permission-authorizations <value>]
[--inbound-permission-revocations <value>]
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

A unique identifier for the fleet to update port settings for. You can use either the fleet ID or ARN value.

`--inbound-permission-authorizations` (list)

A collection of port settings to be added to the fleet resource.

(structure)

A range of IP addresses and port settings that allow inbound traffic to connect to processes on an instance in a fleet. Processes are assigned an IP address/port number combination, which must fall into the fleetâs allowed ranges.

For Amazon GameLift Realtime fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP.

FromPort -> (integer)

A starting value for a range of allowed port numbers.

For fleets using Linux builds, only ports `22` and `1026-60000` are valid.

For fleets using Windows builds, only ports `1026-60000` are valid.

ToPort -> (integer)

An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort` .

For fleets using Linux builds, only ports `22` and `1026-60000` are valid.

For fleets using Windows builds, only ports `1026-60000` are valid.

IpRange -> (string)

A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: â`000.000.000.000/[subnet mask]` â or optionally the shortened version â`0.0.0.0/[subnet mask]` â.

Protocol -> (string)

The network communication protocol used by the fleet.

Shorthand Syntax:

```
FromPort=integer,ToPort=integer,IpRange=string,Protocol=string ...
```

JSON Syntax:

```
[
  {
    "FromPort": integer,
    "ToPort": integer,
    "IpRange": "string",
    "Protocol": "TCP"|"UDP"
  }
  ...
]
```

`--inbound-permission-revocations` (list)

A collection of port settings to be removed from the fleet resource.

(structure)

A range of IP addresses and port settings that allow inbound traffic to connect to processes on an instance in a fleet. Processes are assigned an IP address/port number combination, which must fall into the fleetâs allowed ranges.

For Amazon GameLift Realtime fleets, Amazon GameLift automatically opens two port ranges, one for TCP messaging and one for UDP.

FromPort -> (integer)

A starting value for a range of allowed port numbers.

For fleets using Linux builds, only ports `22` and `1026-60000` are valid.

For fleets using Windows builds, only ports `1026-60000` are valid.

ToPort -> (integer)

An ending value for a range of allowed port numbers. Port numbers are end-inclusive. This value must be equal to or greater than `FromPort` .

For fleets using Linux builds, only ports `22` and `1026-60000` are valid.

For fleets using Windows builds, only ports `1026-60000` are valid.

IpRange -> (string)

A range of allowed IP addresses. This value must be expressed in CIDR notation. Example: â`000.000.000.000/[subnet mask]` â or optionally the shortened version â`0.0.0.0/[subnet mask]` â.

Protocol -> (string)

The network communication protocol used by the fleet.

Shorthand Syntax:

```
FromPort=integer,ToPort=integer,IpRange=string,Protocol=string ...
```

JSON Syntax:

```
[
  {
    "FromPort": integer,
    "ToPort": integer,
    "IpRange": "string",
    "Protocol": "TCP"|"UDP"
  }
  ...
]
```

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