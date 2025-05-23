# create-fleet-locationsÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet-locations.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/create-fleet-locations.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [gamelift](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/gamelift/index.html#cli-aws-gamelift) ]

# create-fleet-locations

## Description

Adds remote locations to an EC2 and begins populating the new locations with instances. The new instances conform to the fleetâs instance type, auto-scaling, and other configuration settings.

### Note

You canât add remote locations to a fleet that resides in an Amazon Web Services Region that doesnât support multiple locations. Fleets created prior to March 2021 canât support multiple locations.

To add fleet locations, specify the fleet to be updated and provide a list of one or more locations.

If successful, this operation returns the list of added locations with their status set to `NEW` . Amazon GameLift initiates the process of starting an instance in each added location. You can track the status of each new location by monitoring location creation events using [DescribeFleetEvents](https://docs.aws.amazon.com/gamelift/latest/apireference/API_DescribeFleetEvents.html) .

**Learn more**

[Setting up fleets](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-intro.html)

[Update fleet locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/fleets-editing.html#fleets-update-locations)

[Amazon GameLift service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/gamelift-2015-10-01/CreateFleetLocations)

## Synopsis

```
create-fleet-locations
--fleet-id <value>
--locations <value>
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

A unique identifier for the fleet to add locations to. You can use either the fleet ID or ARN value.

`--locations` (list)

A list of locations to deploy additional instances to and manage as part of the fleet. You can add any Amazon GameLift-supported Amazon Web Services Region as a remote location, in the form of an Amazon Web Services Region code such as `us-west-2` .

(structure)

A remote location where a multi-location fleet can deploy game servers for game hosting.

Location -> (string)

An Amazon Web Services Region code, such as `us-west-2` . For a list of supported Regions and Local Zones, see [Amazon GameLift service locations](https://docs.aws.amazon.com/gamelift/latest/developerguide/gamelift-regions.html) for managed hosting.

Shorthand Syntax:

```
Location=string ...
```

JSON Syntax:

```
[
  {
    "Location": "string"
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

A unique identifier for the fleet that was updated with new locations.

FleetArn -> (string)

The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html) ) that is assigned to a Amazon GameLift fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912` .

LocationStates -> (list)

The remote locations that are being added to the fleet, and the life-cycle status of each location. For new locations, the status is set to `NEW` . During location creation, Amazon GameLift updates each locationâs status as instances are deployed there and prepared for game hosting. This list does not include the fleet home Region or any remote locations that were already added to the fleet.

(structure)

A fleet location and its life-cycle state. A location state object might be used to describe a fleetâs remote location or home Region. Life-cycle state tracks the progress of launching the first instance in a new location and preparing it for game hosting, and then removing all instances and deleting the location from the fleet.

- **NEW** â A new fleet location has been defined and desired instances is set to 1.
- **DOWNLOADING/VALIDATING/BUILDING/ACTIVATING** â Amazon GameLift is setting up the new fleet location, creating new instances with the game build or Realtime script and starting server processes.
- **ACTIVE** â Hosts can now accept game sessions.
- **ERROR** â An error occurred when downloading, validating, building, or activating the fleet location.
- **DELETING** â Hosts are responding to a delete fleet location request.
- **TERMINATED** â The fleet location no longer exists.
- **NOT_FOUND** â The fleet location was not found. This could be because the custom location was removed or not created.

Location -> (string)

The fleet location, expressed as an Amazon Web Services Region code such as `us-west-2` .

Status -> (string)

The life-cycle status of a fleet location.