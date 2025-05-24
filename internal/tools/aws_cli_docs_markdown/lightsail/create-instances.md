# create-instancesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instances.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/create-instances.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [lightsail](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lightsail/index.html#cli-aws-lightsail) ]

# create-instances

## Description

Creates one or more Amazon Lightsail instances.

The `create instances` operation supports tag-based access control via request tags. For more information, see the [Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/amazon-lightsail-controlling-access-using-tags) .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/lightsail-2016-11-28/CreateInstances)

## Synopsis

```
create-instances
--instance-names <value>
--availability-zone <value>
[--custom-image-name <value>]
--blueprint-id <value>
--bundle-id <value>
[--user-data <value>]
[--key-pair-name <value>]
[--tags <value>]
[--add-ons <value>]
[--ip-address-type <value>]
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

The names to use for your new Lightsail instances. Separate multiple values using quotation marks and commas, for example: `["MyFirstInstance","MySecondInstance"]`

(string)

Syntax:

```
"string" "string" ...
```

`--availability-zone` (string)

The Availability Zone in which to create your instance. Use the following format: `us-east-2a` (case sensitive). You can get a list of Availability Zones by using the [get regions](http://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_GetRegions.html) operation. Be sure to add the `include Availability Zones` parameter to your request.

`--custom-image-name` (string)

(Discontinued) The name for your custom image.

### Note

In releases prior to June 12, 2017, this parameter was ignored by the API. It is now discontinued.

`--blueprint-id` (string)

The ID for a virtual private server image (`app_wordpress_x_x` or `app_lamp_x_x` ). Use the `get blueprints` operation to return a list of available images (or *blueprints* ).

### Note

Use active blueprints when creating new instances. Inactive blueprints are listed to support customers with existing instances and are not necessarily available to create new instances. Blueprints are marked inactive when they become outdated due to operating system updates or new application releases.

`--bundle-id` (string)

The bundle of specification information for your virtual private server (or *instance* ), including the pricing plan (`medium_x_x` ).

`--user-data` (string)

A launch script you can create that configures a server with additional user data. For example, you might want to run `apt-get -y update` .

### Note

Depending on the machine image you choose, the command to get software on your instance varies. Amazon Linux and CentOS use `yum` , Debian and Ubuntu use `apt-get` , and FreeBSD uses `pkg` . For a complete list, see the [Amazon Lightsail Developer Guide](https://docs.aws.amazon.com/lightsail/latest/userguide/compare-options-choose-lightsail-instance-image) .

`--key-pair-name` (string)

The name of your key pair.

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

**Example 1: To create a single instance**

The following `create-instances` example creates an instance in the specified AWS Region and Availability Zone, using the WordPress blueprint, and the $5.00 USD bundle.

```
aws lightsail create-instances \
    --instance-names Instance-1 \
    --availability-zone us-west-2a \
    --blueprint-id wordpress \
    --bundle-id nano_3_0
```

Output:

```
{
    "operations": [
        {
            "id": "9a77158f-7be3-4d6d-8054-cf5ae2b720cc",
            "resourceName": "Instance-1",
            "resourceType": "Instance",
            "createdAt": 1569447986.061,
            "location": {
                "availabilityZone": "us-west-2a",
                "regionName": "us-west-2"
            },
            "isTerminal": false,
            "operationType": "CreateInstance",
            "status": "Started",
            "statusChangedAt": 1569447986.061
        }
    ]
}
```

**Example 2: To create multiple instances at one time**

The following `create-instances` example creates three instances in the specified AWS Region and Availability Zone, using the WordPress blueprint, and the $5.00 USD bundle.

```
aws lightsail create-instances \
    --instance-names {"Instance1","Instance2","Instance3"} \
    --availability-zone us-west-2a \
    --blueprint-id wordpress \
    --bundle-id nano_3_0
```

Output:

```
{
    "operations": [
        {
            "id": "5492f015-9d2e-48c6-8eea-b516840e6903",
            "resourceName": "Instance1",
            "resourceType": "Instance",
            "createdAt": 1569448780.054,
            "location": {
                "availabilityZone": "us-west-2a",
                "regionName": "us-west-2"
            },
            "isTerminal": false,
            "operationType": "CreateInstance",
            "status": "Started",
            "statusChangedAt": 1569448780.054
        },
        {
            "id": "c58b5f46-2676-44c8-b95c-3ad375898515",
            "resourceName": "Instance2",
            "resourceType": "Instance",
            "createdAt": 1569448780.054,
            "location": {
                "availabilityZone": "us-west-2a",
                "regionName": "us-west-2"
            },
            "isTerminal": false,
            "operationType": "CreateInstance",
            "status": "Started",
            "statusChangedAt": 1569448780.054
        },
        {
            "id": "a5ad8006-9bee-4499-9eb7-75e42e6f5882",
            "resourceName": "Instance3",
            "resourceType": "Instance",
            "createdAt": 1569448780.054,
            "location": {
                "availabilityZone": "us-west-2a",
                "regionName": "us-west-2"
            },
            "isTerminal": false,
            "operationType": "CreateInstance",
            "status": "Started",
            "statusChangedAt": 1569448780.054
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