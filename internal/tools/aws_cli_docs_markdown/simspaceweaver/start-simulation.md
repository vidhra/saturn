# start-simulationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/start-simulation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/start-simulation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [simspaceweaver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/index.html#cli-aws-simspaceweaver) ]

# start-simulation

## Description

Starts a simulation with the given name. You must choose to start your simulation from a schema or from a snapshot. For more information about the schema, see the [schema reference](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/schema-reference.html) in the *SimSpace Weaver User Guide* . For more information about snapshots, see [Snapshots](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/working-with_snapshots.html) in the *SimSpace Weaver User Guide* .

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/simspaceweaver-2022-10-28/StartSimulation)

## Synopsis

```
start-simulation
[--client-token <value>]
[--description <value>]
[--maximum-duration <value>]
--name <value>
--role-arn <value>
[--schema-s3-location <value>]
[--snapshot-s3-location <value>]
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

A value that you provide to ensure that repeated calls to this API operation using the same parameters complete only once. A `ClientToken` is also known as an *idempotency token* . A `ClientToken` expires after 24 hours.

`--description` (string)

The description of the simulation.

`--maximum-duration` (string)

The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is `14D` , or its equivalent in the other units. The default value is `14D` . A value equivalent to `0` makes the simulation immediately transition to `Stopping` as soon as it reaches `Started` .

`--name` (string)

The name of the simulation.

`--role-arn` (string)

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the simulation assumes to perform actions. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* . For more information about IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *Identity and Access Management User Guide* .

`--schema-s3-location` (structure)

The location of the simulation schema in Amazon Simple Storage Service (Amazon S3). For more information about Amazon S3, see the ` *Amazon Simple Storage Service User Guide* [https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome).html`__ .

Provide a `SchemaS3Location` to start your simulation from a schema.

If you provide a `SchemaS3Location` then you canât provide a `SnapshotS3Location` .

BucketName -> (string)

The name of an Amazon S3 bucket. For more information about buckets, see [Creating, configuring, and working with Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) in the *Amazon Simple Storage Service User Guide* .

ObjectKey -> (string)

The key name of an object in Amazon S3. For more information about Amazon S3 objects and object keys, see [Uploading, downloading, and working with objects in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html) in the *Amazon Simple Storage Service User Guide* .

Shorthand Syntax:

```
BucketName=string,ObjectKey=string
```

JSON Syntax:

```
{
  "BucketName": "string",
  "ObjectKey": "string"
}
```

`--snapshot-s3-location` (structure)

The location of the snapshot .zip file in Amazon Simple Storage Service (Amazon S3). For more information about Amazon S3, see the ` *Amazon Simple Storage Service User Guide* [https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome).html`__ .

Provide a `SnapshotS3Location` to start your simulation from a snapshot.

The Amazon S3 bucket must be in the same Amazon Web Services Region as the simulation.

If you provide a `SnapshotS3Location` then you canât provide a `SchemaS3Location` .

BucketName -> (string)

The name of an Amazon S3 bucket. For more information about buckets, see [Creating, configuring, and working with Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) in the *Amazon Simple Storage Service User Guide* .

ObjectKey -> (string)

The key name of an object in Amazon S3. For more information about Amazon S3 objects and object keys, see [Uploading, downloading, and working with objects in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html) in the *Amazon Simple Storage Service User Guide* .

Shorthand Syntax:

```
BucketName=string,ObjectKey=string
```

JSON Syntax:

```
{
  "BucketName": "string",
  "ObjectKey": "string"
}
```

`--tags` (map)

A list of tags for the simulation. For more information about tags, see [Tagging Amazon Web Services resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *Amazon Web Services General Reference* .

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

Arn -> (string)

The Amazon Resource Name (ARN) of the simulation. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

CreationTime -> (timestamp)

The time when the simulation was created, expressed as the number of seconds and milliseconds in UTC since the Unix epoch (0:0:0.000, January 1, 1970).

ExecutionId -> (string)

A universally unique identifier (UUID) for this simulation.