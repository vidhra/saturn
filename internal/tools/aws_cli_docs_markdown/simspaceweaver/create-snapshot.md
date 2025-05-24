# create-snapshotÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/create-snapshot.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/create-snapshot.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [simspaceweaver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/index.html#cli-aws-simspaceweaver) ]

# create-snapshot

## Description

Creates a snapshot of the specified simulation. A snapshot is a file that contains simulation state data at a specific time. The state data saved in a snapshot includes entity data from the State Fabric, the simulation configuration specified in the schema, and the clock tick number. You can use the snapshot to initialize a new simulation. For more information about snapshots, see [Snapshots](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots.html) in the *SimSpace Weaver User Guide* .

You specify a `Destination` when you create a snapshot. The `Destination` is the name of an Amazon S3 bucket and an optional `ObjectKeyPrefix` . The `ObjectKeyPrefix` is usually the name of a folder in the bucket. SimSpace Weaver creates a `snapshot` folder inside the `Destination` and places the snapshot file there.

The snapshot file is an Amazon S3 object. It has an object key with the form: `` *object-key-prefix* /snapshot/*simulation-name* -*YYMMdd* -*HHmm* -*ss* .zip`` , where:

- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/create-snapshot.html#id1)*YY* `` is the 2-digit year
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/create-snapshot.html#id3)*MM* `` is the 2-digit month
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/create-snapshot.html#id5)*dd* `` is the 2-digit day of the month
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/create-snapshot.html#id7)*HH* `` is the 2-digit hour (24-hour clock)
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/create-snapshot.html#id9)*mm* `` is the 2-digit minutes
- [``](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/create-snapshot.html#id11)*ss* `` is the 2-digit seconds

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/simspaceweaver-2022-10-28/CreateSnapshot)

## Synopsis

```
create-snapshot
--destination <value>
--simulation <value>
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

`--destination` (structure)

The Amazon S3 bucket and optional folder (object key prefix) where SimSpace Weaver creates the snapshot file.

The Amazon S3 bucket must be in the same Amazon Web Services Region as the simulation.

BucketName -> (string)

The name of an Amazon S3 bucket. For more information about buckets, see [Creating, configuring, and working with Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) in the *Amazon Simple Storage Service User Guide* .

ObjectKeyPrefix -> (string)

A string prefix for an Amazon S3 object key. Itâs usually a folder name. For more information about folders in Amazon S3, see [Organizing objects in the Amazon S3 console using folders](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-folders.html) in the *Amazon Simple Storage Service User Guide* .

Shorthand Syntax:

```
BucketName=string,ObjectKeyPrefix=string
```

JSON Syntax:

```
{
  "BucketName": "string",
  "ObjectKeyPrefix": "string"
}
```

`--simulation` (string)

The name of the simulation.

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

None