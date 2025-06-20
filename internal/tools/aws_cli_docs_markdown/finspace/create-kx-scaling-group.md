# create-kx-scaling-groupÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/create-kx-scaling-group.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/create-kx-scaling-group.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [finspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/index.html#cli-aws-finspace) ]

# create-kx-scaling-group

## Description

Creates a new scaling group.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/finspace-2021-03-12/CreateKxScalingGroup)

## Synopsis

```
create-kx-scaling-group
[--client-token <value>]
--environment-id <value>
--scaling-group-name <value>
--host-type <value>
--availability-zone-id <value>
[--tags <value>]
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

`--client-token` (string)

A token that ensures idempotency. This token expires in 10 minutes.

`--environment-id` (string)

A unique identifier for the kdb environment, where you want to create the scaling group.

`--scaling-group-name` (string)

A unique identifier for the kdb scaling group.

`--host-type` (string)

The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.

You can add one of the following values:

- `kx.sg.large` â The host type with a configuration of 16 GiB memory and 2 vCPUs.
- `kx.sg.xlarge` â The host type with a configuration of 32 GiB memory and 4 vCPUs.
- `kx.sg.2xlarge` â The host type with a configuration of 64 GiB memory and 8 vCPUs.
- `kx.sg.4xlarge` â The host type with a configuration of 108 GiB memory and 16 vCPUs.
- `kx.sg.8xlarge` â The host type with a configuration of 216 GiB memory and 32 vCPUs.
- `kx.sg.16xlarge` â The host type with a configuration of 432 GiB memory and 64 vCPUs.
- `kx.sg.32xlarge` â The host type with a configuration of 864 GiB memory and 128 vCPUs.
- `kx.sg1.16xlarge` â The host type with a configuration of 1949 GiB memory and 64 vCPUs.
- `kx.sg1.24xlarge` â The host type with a configuration of 2948 GiB memory and 96 vCPUs.

`--availability-zone-id` (string)

The identifier of the availability zones.

`--tags` (map)

A list of key-value pairs to label the scaling group. You can add up to 50 tags to a scaling group.

key -> (string)

value -> (string)

Shorthand Syntax:

```
KeyName1=string,KeyName2=string
```

JSON Syntax:

```
{"string": "string"
  ...}
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

environmentId -> (string)

A unique identifier for the kdb environment, where you create the scaling group.

scalingGroupName -> (string)

A unique identifier for the kdb scaling group.

hostType -> (string)

The memory and CPU capabilities of the scaling group host on which FinSpace Managed kdb clusters will be placed.

availabilityZoneId -> (string)

The identifier of the availability zones.

status -> (string)

The status of scaling group.

- CREATING â The scaling group creation is in progress.
- CREATE_FAILED â The scaling group creation has failed.
- ACTIVE â The scaling group is active.
- UPDATING â The scaling group is in the process of being updated.
- UPDATE_FAILED â The update action failed.
- DELETING â The scaling group is in the process of being deleted.
- DELETE_FAILED â The system failed to delete the scaling group.
- DELETED â The scaling group is successfully deleted.

lastModifiedTimestamp -> (timestamp)

The last time that the scaling group was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.

createdTimestamp -> (timestamp)

The timestamp at which the scaling group was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.