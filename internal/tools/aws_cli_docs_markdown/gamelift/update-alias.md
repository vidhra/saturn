# update-aliasÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-alias.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/update-alias.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# update-alias

## Description

Updates properties for an alias. Specify the unique identifier of the alias to be updated and the new property values. When reassigning an alias to a new fleet, provide an updated routing strategy. If successful, the updated alias record is returned.

**Related actions**

[All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/UpdateAlias)

## Synopsis

```
update-alias
--alias-id <value>
[--name <value>]
[--description <value>]
[--routing-strategy <value>]
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

`--alias-id` (string)

A unique identifier for the alias that you want to update. You can use either the alias ID or ARN value.

`--name` (string)

A descriptive label that is associated with an alias. Alias names do not need to be unique.

`--description` (string)

A human-readable description of the alias.

`--routing-strategy` (structure)

The routing configuration, including routing type and fleet target, for the alias.

Type -> (string)

The type of routing strategy for the alias.

Possible routing types include the following:

- **SIMPLE** - The alias resolves to one specific fleet. Use this type when routing to active fleets.
- **TERMINAL** - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the message embedded.

FleetId -> (string)

A unique identifier for the fleet that the alias points to. This value is the fleet ID, not the fleet ARN.

Message -> (string)

The message text to be used with a terminal routing strategy.

Shorthand Syntax:

```
Type=string,FleetId=string,Message=string
```

JSON Syntax:

```
{
  "Type": "SIMPLE"|"TERMINAL",
  "FleetId": "string",
  "Message": "string"
}
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

Alias -> (structure)

The updated alias resource.

AliasId -> (string)

A unique identifier for the alias. Alias IDs are unique within a Region.

Name -> (string)

A descriptive label that is associated with an alias. Alias names do not need to be unique.

AliasArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to a Amazon GameLift alias resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::alias/alias-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912` . In a GameLift alias ARN, the resource ID matches the alias ID value.

Description -> (string)

A human-readable description of an alias.

RoutingStrategy -> (structure)

The routing configuration, including routing type and fleet target, for the alias.

Type -> (string)

The type of routing strategy for the alias.

Possible routing types include the following:

- **SIMPLE** - The alias resolves to one specific fleet. Use this type when routing to active fleets.
- **TERMINAL** - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the message embedded.

FleetId -> (string)

A unique identifier for the fleet that the alias points to. This value is the fleet ID, not the fleet ARN.

Message -> (string)

The message text to be used with a terminal routing strategy.

CreationTime -> (timestamp)

A time stamp indicating when this data object was created. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).

LastUpdatedTime -> (timestamp)

The time that this data object was last modified. Format is a number expressed in Unix time as milliseconds (for example `"1469498468.057"` ).