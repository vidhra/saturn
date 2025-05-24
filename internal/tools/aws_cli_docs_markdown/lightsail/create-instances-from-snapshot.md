# create-instances-from-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instances-from-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instances-from-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# create-instances-from-snapshot

## Description

Creates one or more new instances from a manual or automatic snapshot of an instance.

The `create instances from snapshot` operation supports tag-based access control via request tags and resource tags applied to the resource identified by `instance snapshot name` . For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateInstancesFromSnapshot)

## Synopsis

```
create-instances-from-snapshot
--instance-names <value>
[--attached-disk-mapping <value>]
--availability-zone <value>
[--instance-snapshot-name <value>]
--bundle-id <value>
[--user-data <value>]
[--key-pair-name <value>]
[--tags <value>]
[--add-ons <value>]
[--ip-address-type <value>]
[--source-instance-name <value>]
[--restore-date <value>]
[--use-latest-restorable-auto-snapshot | --no-use-latest-restorable-auto-snapshot]
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

`--instance-names` (list)

The names for your new instances.

(string)

Syntax:

```
"string" "string" ...
```

`--attached-disk-mapping` (map)

An object containing information about one or more disk mappings.

key -> (string)

value -> (list)

(structure)

Describes a block storage disk mapping.

originalDiskPath -> (string)

The original disk path exposed to the instance (for example, `/dev/sdh` ).

newDiskName -> (string)

The new disk name (`my-new-disk` ).

Shorthand Syntax:

```
KeyName1=[{originalDiskPath=string,newDiskName=string},{originalDiskPath=string,newDiskName=string}],KeyName2=[{originalDiskPath=string,newDiskName=string},{originalDiskPath=string,newDiskName=string}]
```

JSON Syntax:

```
{"string": [
      {
        "originalDiskPath": "string",
        "newDiskName": "string"
      }
      ...
    ]
  ...}
```

`--availability-zone` (string)

The Availability Zone where you want to create your instances. Use the following formatting: `us-east-2a` (case sensitive). You can get a list of Availability Zones by using the [get regions](http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html) operation. Be sure to add the `include Availability Zones` parameter to your request.

`--instance-snapshot-name` (string)

The name of the instance snapshot on which you are basing your new instances. Use the get instance snapshots operation to return information about your existing snapshots.

Constraint:

- This parameter cannot be defined together with the `source instance name` parameter. The `instance snapshot name` and `source instance name` parameters are mutually exclusive.

`--bundle-id` (string)

The bundle of specification information for your virtual private server (or *instance* ), including the pricing plan (`micro_x_x` ).

`--user-data` (string)

You can create a launch script that configures a server with additional user data. For example, `apt-get -y update` .

### Note

Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use `yum` , Debian and Ubuntu use `apt-get` , and FreeBSD uses `pkg` . For a complete list, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/compare-options-choose-lightsail-instance-image) .

`--key-pair-name` (string)

The name for your key pair.

`--tags` (list)

The tag keys and optional values to add to the resource during create.

Use the `TagResource` action to tag a resource after itâs created.

(structure)

Describes a tag key and optional value assigned to an Amazon Lightsail resource.

For more information about tags in Lightsail, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-tags) .

key -> (string)

The key of the tag.

Constraints: Tag keys accept a maximum of 128 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

value -> (string)

The value of the tag.

Constraints: Tag values accept a maximum of 256 letters, numbers, spaces in UTF-8, or the following characters: + - = . _ : / @

Shorthand Syntax:

```
key=string,value=string ...
```

JSON Syntax:

```
[
  {
    "key": "string",
    "value": "string"
  }
  ...
]
```

`--add-ons` (list)

An array of objects representing the add-ons to enable for the new instance.

(structure)

Describes a request to enable, modify, or disable an add-on for an Amazon Lightsail resource.

### Note

An additional cost may be associated with enabling add-ons. For more information, see the [Lightsail pricing page](https://aws.amazon.com/lightsail/pricing/) .

addOnType -> (string)

The add-on type.

autoSnapshotAddOnRequest -> (structure)

An object that represents additional parameters when enabling or modifying the automatic snapshot add-on.

snapshotTimeOfDay -> (string)

The daily time when an automatic snapshot will be created.

Constraints:

- Must be in `HH:00` format, and in an hourly increment.
- Specified in Coordinated Universal Time (UTC).
- The snapshot will be automatically created between the time specified and up to 45 minutes after.

stopInstanceOnIdleRequest -> (structure)

An object that represents additional parameters when enabling or modifying the `StopInstanceOnIdle` add-on.

### Warning

This object only applies to Lightsail for Research resources.

threshold -> (string)

The value to compare with the duration.

duration -> (string)

The amount of idle time in minutes after which your virtual computer will automatically stop.

Shorthand Syntax:

```
addOnType=string,autoSnapshotAddOnRequest={snapshotTimeOfDay=string},stopInstanceOnIdleRequest={threshold=string,duration=string} ...
```

JSON Syntax:

```
[
  {
    "addOnType": "AutoSnapshot"|"StopInstanceOnIdle",
    "autoSnapshotAddOnRequest": {
      "snapshotTimeOfDay": "string"
    },
    "stopInstanceOnIdleRequest": {
      "threshold": "string",
      "duration": "string"
    }
  }
  ...
]
```

`--ip-address-type` (string)

The IP address type for the instance.

The possible values are `ipv4` for IPv4 only, `ipv6` for IPv6 only, and `dualstack` for IPv4 and IPv6.

The default value is `dualstack` .

Possible values:

- `dualstack`
- `ipv4`
- `ipv6`

`--source-instance-name` (string)

The name of the source instance from which the source automatic snapshot was created.

Constraints:

- This parameter cannot be defined together with the `instance snapshot name` parameter. The `source instance name` and `instance snapshot name` parameters are mutually exclusive.
- Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots) .

`--restore-date` (string)

The date of the automatic snapshot to use for the new instance. Use the `get auto snapshots` operation to identify the dates of the available automatic snapshots.

Constraints:

- Must be specified in `YYYY-MM-DD` format.
- This parameter cannot be defined together with the `use latest restorable auto snapshot` parameter. The `restore date` and `use latest restorable auto snapshot` parameters are mutually exclusive.
- Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots) .

`--use-latest-restorable-auto-snapshot` | `--no-use-latest-restorable-auto-snapshot` (boolean)

A Boolean value to indicate whether to use the latest available automatic snapshot.

Constraints:

- This parameter cannot be defined together with the `restore date` parameter. The `use latest restorable auto snapshot` and `restore date` parameters are mutually exclusive.
- Define this parameter only when creating a new instance from an automatic snapshot. For more information, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-configuring-automatic-snapshots) .

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

**To create an instance from a snapshot**

The following `create-instances-from-snapshot` example creates an instance from the specified instance snapshot, in the specified AWS Region and Availability Zone, using the $12 USD bundle.

**Note:** The bundle that you specify must be equal to or greater in specifications than the bundle of the original source instance used to create the snapshot.

```
aws lightsail create-instances-from-snapshot \
    --instance-snapshot-name WordPress-1-1569866208 \
    --instance-names WordPress-2 \
    --availability-zone us-west-2a \
    --bundle-id small_3_0
```

Output:

```
{
    "operations": [
        {
            "id": "003f8271-b711-464d-b9b8-7f3806cb496e",
            "resourceName": "WordPress-2",
            "resourceType": "Instance",
            "createdAt": 1569865914.908,
            "location": {
                "availabilityZone": "us-west-2a",
                "regionName": "us-west-2"
            },
            "isTerminal": false,
            "operationType": "CreateInstancesFromSnapshot",
            "status": "Started",
            "statusChangedAt": 1569865914.908
        }
    ]
}
```

## Output

operations -> (list)

An array of objects that describe the result of the action, such as the status of the request, the timestamp of the request, and the resources affected by the request.

(structure)

Describes the API operation.

id -> (string)

The ID of the operation.

resourceName -> (string)

The resource name.

resourceType -> (string)

The resource type.

createdAt -> (timestamp)

The timestamp when the operation was initialized (`1479816991.349` ).

location -> (structure)

The Amazon Web Services Region and Availability Zone.

availabilityZone -> (string)

The Availability Zone. Follows the format `us-east-2a` (case-sensitive).

regionName -> (string)

The Amazon Web Services Region name.

isTerminal -> (boolean)

A Boolean value indicating whether the operation is terminal.

operationDetails -> (string)

Details about the operation (`Debian-1GB-Ohio-1` ).

operationType -> (string)

The type of operation.

status -> (string)

The status of the operation.

statusChangedAt -> (timestamp)

The timestamp when the status was changed (`1479816991.349` ).

errorCode -> (string)

The error code.

errorDetails -> (string)

The error details.