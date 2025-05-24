# create-kx-volumeÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/create-kx-volume.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/create-kx-volume.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [finspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/index.html#cli-aws-finspace) ]

# create-kx-volume

## Description

Creates a new volume with a specific amount of throughput and storage capacity.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/finspace-2021-03-12/CreateKxVolume)

## Synopsis

```
create-kx-volume
[--client-token <value>]
--environment-id <value>
--volume-type <value>
--volume-name <value>
[--description <value>]
[--nas1-configuration <value>]
--az-mode <value>
--availability-zone-ids <value>
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

A unique identifier for the kdb environment, whose clusters can attach to the volume.

`--volume-type` (string)

The type of file system volume. Currently, FinSpace only supports `NAS_1` volume type. When you select `NAS_1` volume type, you must also provide `nas1Configuration` .

Possible values:

- `NAS_1`

`--volume-name` (string)

A unique identifier for the volume.

`--description` (string)

A description of the volume.

`--nas1-configuration` (structure)

Specifies the configuration for the Network attached storage (NAS_1) file system volume. This parameter is required when you choose `volumeType` as *NAS_1* .

type -> (string)

The type of the network attached storage.

size -> (integer)

The size of the network attached storage. For storage type `SSD_1000` and `SSD_250` you can select the minimum size as 1200 GB or increments of 2400 GB. For storage type `HDD_12` you can select the minimum size as 6000 GB or increments of 6000 GB.

Shorthand Syntax:

```
type=string,size=integer
```

JSON Syntax:

```
{
  "type": "SSD_1000"|"SSD_250"|"HDD_12",
  "size": integer
}
```

`--az-mode` (string)

The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.

Possible values:

- `SINGLE`
- `MULTI`

`--availability-zone-ids` (list)

The identifier of the availability zones.

(string)

Syntax:

```
"string" "string" ...
```

`--tags` (map)

A list of key-value pairs to label the volume. You can add up to 50 tags to a volume.

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

A unique identifier for the kdb environment, whose clusters can attach to the volume.

volumeName -> (string)

A unique identifier for the volume.

volumeType -> (string)

The type of file system volume. Currently, FinSpace only supports `NAS_1` volume type.

volumeArn -> (string)

The ARN identifier of the volume.

nas1Configuration -> (structure)

Specifies the configuration for the Network attached storage (NAS_1) file system volume.

type -> (string)

The type of the network attached storage.

size -> (integer)

The size of the network attached storage. For storage type `SSD_1000` and `SSD_250` you can select the minimum size as 1200 GB or increments of 2400 GB. For storage type `HDD_12` you can select the minimum size as 6000 GB or increments of 6000 GB.

status -> (string)

The status of volume creation.

- CREATING â The volume creation is in progress.
- CREATE_FAILED â The volume creation has failed.
- ACTIVE â The volume is active.
- UPDATING â The volume is in the process of being updated.
- UPDATE_FAILED â The update action failed.
- UPDATED â The volume is successfully updated.
- DELETING â The volume is in the process of being deleted.
- DELETE_FAILED â The system failed to delete the volume.
- DELETED â The volume is successfully deleted.

statusReason -> (string)

The error message when a failed state occurs.

azMode -> (string)

The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.

description -> (string)

A description of the volume.

availabilityZoneIds -> (list)

The identifier of the availability zones.

(string)

createdTimestamp -> (timestamp)

The timestamp at which the volume was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.