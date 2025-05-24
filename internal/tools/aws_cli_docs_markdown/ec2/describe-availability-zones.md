# describe-availability-zonesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-availability-zones.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/describe-availability-zones.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [ec2](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html#cli-aws-ec2) ]

# describe-availability-zones

## Description

Describes the Availability Zones, Local Zones, and Wavelength Zones that are available to you.

For more information about Availability Zones, Local Zones, and Wavelength Zones, see [Regions and zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) in the *Amazon EC2 User Guide* .

### Note

The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/ec2-2016-11-15/DescribeAvailabilityZones)

## Synopsis

```
describe-availability-zones
[--zone-names <value>]
[--zone-ids <value>]
[--all-availability-zones | --no-all-availability-zones]
[--dry-run | --no-dry-run]
[--filters <value>]
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

`--zone-names` (list)

The names of the Availability Zones, Local Zones, and Wavelength Zones.

(string)

Syntax:

```
"string" "string" ...
```

`--zone-ids` (list)

The IDs of the Availability Zones, Local Zones, and Wavelength Zones.

(string)

Syntax:

```
"string" "string" ...
```

`--all-availability-zones` | `--no-all-availability-zones` (boolean)

Include all Availability Zones, Local Zones, and Wavelength Zones regardless of your opt-in status.

If you do not use this parameter, the results include only the zones for the Regions where you have chosen the option to opt in.

`--dry-run` | `--no-dry-run` (boolean)

Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation` . Otherwise, it is `UnauthorizedOperation` .

`--filters` (list)

The filters.

- `group-long-name` - The long name of the zone group for the Availability Zone (for example, `US West (Oregon) 1` ), the Local Zone (for example, for Zone group `us-west-2-lax-1` , it is `US West (Los Angeles)` , or the Wavelength Zone (for example, for Zone group `us-east-1-wl1` , it is `US East (Verizon)` .
- `group-name` - The name of the zone group for the Availability Zone (for example, `us-east-1-zg-1` ), the Local Zone (for example, `us-west-2-lax-1` ), or the Wavelength Zone (for example, `us-east-1-wl1` ).
- `message` - The Zone message.
- `opt-in-status` - The opt-in status (`opted-in` | `not-opted-in` | `opt-in-not-required` ).
- `parent-zone-id` - The ID of the zone that handles some of the Local Zone and Wavelength Zone control plane operations, such as API calls.
- `parent-zone-name` - The ID of the zone that handles some of the Local Zone and Wavelength Zone control plane operations, such as API calls.
- `region-name` - The name of the Region for the Zone (for example, `us-east-1` ).
- `state` - The state of the Availability Zone, the Local Zone, or the Wavelength Zone (`available` | `unavailable` | `constrained` ).
- `zone-id` - The ID of the Availability Zone (for example, `use1-az1` ), the Local Zone (for example, `usw2-lax1-az1` ), or the Wavelength Zone (for example, `us-east-1-wl1-bos-wlz-1` ).
- `zone-name` - The name of the Availability Zone (for example, `us-east-1a` ), the Local Zone (for example, `us-west-2-lax-1a` ), or the Wavelength Zone (for example, `us-east-1-wl1-bos-wlz-1` ).
- `zone-type` - The type of zone (`availability-zone` | `local-zone` | `wavelength-zone` ).

(structure)

A filter name and value pair that is used to return a more specific list of results from a describe operation. Filters can be used to match a set of resources by specific criteria, such as tags, attributes, or IDs.

If you specify multiple filters, the filters are joined with an `AND` , and the request returns only results that match all of the specified filters.

For more information, see [List and filter using the CLI and API](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Using_Filtering.html#Filtering_Resources_CLI) in the *Amazon EC2 User Guide* .

Name -> (string)

The name of the filter. Filter names are case-sensitive.

Values -> (list)

The filter values. Filter values are case-sensitive. If you specify multiple values for a filter, the values are joined with an `OR` , and the request returns all results that match any of the specified values.

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

**To describe your Availability Zones**

The following example `describe-availability-zones` displays details for the Availability Zones that are available to you. The response includes Availability Zones only for the current Region. In this example, it uses the profiles default `us-west-2` (Oregon) Region.

```
aws ec2 describe-availability-zones
```

Output:

```
{
    "AvailabilityZones": [
        {
            "State": "available",
            "OptInStatus": "opt-in-not-required",
            "Messages": [],
            "RegionName": "us-west-2",
            "ZoneName": "us-west-2a",
            "ZoneId": "usw2-az1",
            "GroupName": "us-west-2",
            "NetworkBorderGroup": "us-west-2"
        },
        {
            "State": "available",
            "OptInStatus": "opt-in-not-required",
            "Messages": [],
            "RegionName": "us-west-2",
            "ZoneName": "us-west-2b",
            "ZoneId": "usw2-az2",
            "GroupName": "us-west-2",
            "NetworkBorderGroup": "us-west-2"
        },
        {
            "State": "available",
            "OptInStatus": "opt-in-not-required",
            "Messages": [],
            "RegionName": "us-west-2",
            "ZoneName": "us-west-2c",
            "ZoneId": "usw2-az3",
            "GroupName": "us-west-2",
            "NetworkBorderGroup": "us-west-2"
        },
        {
            "State": "available",
            "OptInStatus": "opt-in-not-required",
            "Messages": [],
            "RegionName": "us-west-2",
            "ZoneName": "us-west-2d",
            "ZoneId": "usw2-az4",
            "GroupName": "us-west-2",
            "NetworkBorderGroup": "us-west-2"
        },
        {
            "State": "available",
            "OptInStatus": "opted-in",
            "Messages": [],
            "RegionName": "us-west-2",
            "ZoneName": "us-west-2-lax-1a",
            "ZoneId": "usw2-lax1-az1",
            "GroupName": "us-west-2-lax-1",
            "NetworkBorderGroup": "us-west-2-lax-1"
        }
    ]
}
```

## Output

AvailabilityZones -> (list)

Information about the Availability Zones, Local Zones, and Wavelength Zones.

(structure)

Describes Availability Zones, Local Zones, and Wavelength Zones.

OptInStatus -> (string)

For Availability Zones, this parameter always has the value of `opt-in-not-required` .

For Local Zones and Wavelength Zones, this parameter is the opt-in status. The possible values are `opted-in` and `not-opted-in` .

Messages -> (list)

Any messages about the Availability Zone, Local Zone, or Wavelength Zone.

(structure)

Describes a message about an Availability Zone, Local Zone, or Wavelength Zone.

Message -> (string)

The message about the Availability Zone, Local Zone, or Wavelength Zone.

RegionName -> (string)

The name of the Region.

ZoneName -> (string)

The name of the Availability Zone, Local Zone, or Wavelength Zone.

ZoneId -> (string)

The ID of the Availability Zone, Local Zone, or Wavelength Zone.

GroupName -> (string)

The name of the zone group. For example:

- Availability Zones - `us-east-1-zg-1`
- Local Zones - `us-west-2-lax-1`
- Wavelength Zones - `us-east-1-wl1-bos-wlz-1`

NetworkBorderGroup -> (string)

The name of the network border group.

ZoneType -> (string)

The type of zone.

Valid values: `availability-zone` | `local-zone` | `wavelength-zone`

ParentZoneName -> (string)

The name of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls.

ParentZoneId -> (string)

The ID of the zone that handles some of the Local Zone or Wavelength Zone control plane operations, such as API calls.

GroupLongName -> (string)

The long name of the Availability Zone group, Local Zone group, or Wavelength Zone group.

State -> (string)

The state of the Availability Zone, Local Zone, or Wavelength Zone. The possible values are `available` , `unavailable` , and `constrained` .