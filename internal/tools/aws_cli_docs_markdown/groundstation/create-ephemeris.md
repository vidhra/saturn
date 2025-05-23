# create-ephemerisÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-ephemeris.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/create-ephemeris.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [groundstation](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/groundstation/index.html#cli-aws-groundstation) ]

# create-ephemeris

## Description

Creates an Ephemeris with the specified `EphemerisData` .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/groundstation-2019-05-23/CreateEphemeris)

## Synopsis

```
create-ephemeris
[--enabled | --no-enabled]
[--ephemeris <value>]
[--expiration-time <value>]
[--kms-key-arn <value>]
--name <value>
[--priority <value>]
--satellite-id <value>
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

`--enabled` | `--no-enabled` (boolean)

Whether to set the ephemeris status to `ENABLED` after validation.

Setting this to false will set the ephemeris status to `DISABLED` after validation.

`--ephemeris` (tagged union structure)

Ephemeris data.

### Note

This is a Tagged Union structure. Only one of the following top level keys can be set: `oem`, `tle`.

oem -> (structure)

Ephemeris data in Orbit Ephemeris Message (OEM) format.

AWS Ground Station processes OEM Customer Provided Ephemerides according to the [CCSDS standard](https://public.ccsds.org/Pubs/502x0b3e1.pdf) with some extra restrictions. OEM files should be in KVN format. For more detail about the OEM format that AWS Ground Station supports, see [OEM ephemeris format](https://docs.aws.amazon.com/ground-station/latest/ug/providing-custom-ephemeris-data.html#oem-ephemeris-format) in the AWS Ground Station user guide.

oemData -> (string)

The data for an OEM ephemeris, supplied directly in the request rather than through an S3 object.

s3Object -> (structure)

Identifies the S3 object to be used as the ephemeris.

bucket -> (string)

An Amazon S3 Bucket name.

key -> (string)

An Amazon S3 key for the ephemeris.

version -> (string)

For versioned S3 objects, the version to use for the ephemeris.

tle -> (structure)

Two-line element set (TLE) ephemeris.

s3Object -> (structure)

Identifies the S3 object to be used as the ephemeris.

bucket -> (string)

An Amazon S3 Bucket name.

key -> (string)

An Amazon S3 key for the ephemeris.

version -> (string)

For versioned S3 objects, the version to use for the ephemeris.

tleData -> (list)

The data for a TLE ephemeris, supplied directly in the request rather than through an S3 object.

(structure)

Two-line element set (TLE) data.

tleLine1 -> (string)

First line of two-line element set (TLE) data.

tleLine2 -> (string)

Second line of two-line element set (TLE) data.

validTimeRange -> (structure)

The valid time range for the TLE. Gaps or overlap are not permitted.

endTime -> (timestamp)

Time in UTC at which the time range ends.

startTime -> (timestamp)

Time in UTC at which the time range starts.

JSON Syntax:

```
{
  "oem": {
    "oemData": "string",
    "s3Object": {
      "bucket": "string",
      "key": "string",
      "version": "string"
    }
  },
  "tle": {
    "s3Object": {
      "bucket": "string",
      "key": "string",
      "version": "string"
    },
    "tleData": [
      {
        "tleLine1": "string",
        "tleLine2": "string",
        "validTimeRange": {
          "endTime": timestamp,
          "startTime": timestamp
        }
      }
      ...
    ]
  }
}
```

`--expiration-time` (timestamp)

An overall expiration time for the ephemeris in UTC, after which it will become `EXPIRED` .

`--kms-key-arn` (string)

The ARN of a KMS key used to encrypt the ephemeris in Ground Station.

`--name` (string)

A name string associated with the ephemeris. Used as a human-readable identifier for the ephemeris.

`--priority` (integer)

Customer-provided priority score to establish the order in which overlapping ephemerides should be used.

The default for customer-provided ephemeris priority is 1, and higher numbers take precedence.

Priority must be 1 or greater

`--satellite-id` (string)

AWS Ground Station satellite ID for this ephemeris.

`--tags` (map)

Tags assigned to an ephemeris.

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

ephemerisId -> (string)

The AWS Ground Station ephemeris ID.