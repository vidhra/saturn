# describe-simulationÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/describe-simulation.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/describe-simulation.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [simspaceweaver](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/simspaceweaver/index.html#cli-aws-simspaceweaver) ]

# describe-simulation

## Description

Returns the current state of the given simulation.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/simspaceweaver-2022-10-28/DescribeSimulation)

## Synopsis

```
describe-simulation
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

Arn -> (string)

The Amazon Resource Name (ARN) of the simulation. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* .

CreationTime -> (timestamp)

The time when the simulation was created, expressed as the number of seconds and milliseconds in UTC since the Unix epoch (0:0:0.000, January 1, 1970).

Description -> (string)

The description of the simulation.

ExecutionId -> (string)

A universally unique identifier (UUID) for this simulation.

LiveSimulationState -> (structure)

A collection of additional state information, such as domain and clock configuration.

Clocks -> (list)

A list of simulation clocks.

### Note

At this time, a simulation has only one clock.

(structure)

Status information about the simulation clock.

Status -> (string)

The current status of the simulation clock.

TargetStatus -> (string)

The desired status of the simulation clock.

Domains -> (list)

A list of domains for the simulation. For more information about domains, see [Key concepts: Domains](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is_key-concepts.html#what-is_key-concepts_domains) in the *SimSpace Weaver User Guide* .

(structure)

A collection of app instances that run the same executable app code and have the same launch options and commands.

For more information about domains, see [Key concepts: Domains](https://docs.aws.amazon.com/simspaceweaver/latest/userguide/what-is_key-concepts.html#what-is_key-concepts_domains) in the *SimSpace Weaver User Guide* .

Lifecycle -> (string)

The type of lifecycle management for apps in the domain. Indicates whether apps in this domain are *managed* (SimSpace Weaver starts and stops the apps) or *unmanaged* (you must start and stop the apps).

**Lifecycle types**

- `PerWorker` â Managed: SimSpace Weaver starts one app on each worker.
- `BySpatialSubdivision` â Managed: SimSpace Weaver starts one app for each spatial partition.
- `ByRequest` â Unmanaged: You use the `StartApp` API to start the apps and use the `StopApp` API to stop the apps.

Name -> (string)

The name of the domain.

LoggingConfiguration -> (structure)

Settings that control how SimSpace Weaver handles your simulation log data.

Destinations -> (list)

A list of the locations where SimSpace Weaver sends simulation log data.

(structure)

The location where SimSpace Weaver sends simulation log data.

CloudWatchLogsLogGroup -> (structure)

An Amazon CloudWatch Logs log group that stores simulation log data. For more information about log groups, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide* .

LogGroupArn -> (string)

The Amazon Resource Name (ARN) of the Amazon CloudWatch Logs log group for the simulation. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* . For more information about log groups, see [Working with log groups and log streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html) in the *Amazon CloudWatch Logs User Guide* .

MaximumDuration -> (string)

The maximum running time of the simulation, specified as a number of minutes (m or M), hours (h or H), or days (d or D). The simulation stops when it reaches this limit. The maximum value is `14D` , or its equivalent in the other units. The default value is `14D` . A value equivalent to `0` makes the simulation immediately transition to `Stopping` as soon as it reaches `Started` .

Name -> (string)

The name of the simulation.

RoleArn -> (string)

The Amazon Resource Name (ARN) of the Identity and Access Management (IAM) role that the simulation assumes to perform actions. For more information about ARNs, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *Amazon Web Services General Reference* . For more information about IAM roles, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the *Identity and Access Management User Guide* .

SchemaError -> (string)

An error message that SimSpace Weaver returns only if there is a problem with the simulation schema.

SchemaS3Location -> (structure)

The location of the simulation schema in Amazon Simple Storage Service (Amazon S3). For more information about Amazon S3, see the ` *Amazon Simple Storage Service User Guide* [https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome).html`__ .

BucketName -> (string)

The name of an Amazon S3 bucket. For more information about buckets, see [Creating, configuring, and working with Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) in the *Amazon Simple Storage Service User Guide* .

ObjectKey -> (string)

The key name of an object in Amazon S3. For more information about Amazon S3 objects and object keys, see [Uploading, downloading, and working with objects in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html) in the *Amazon Simple Storage Service User Guide* .

SnapshotS3Location -> (structure)

A location in Amazon Simple Storage Service (Amazon S3) where SimSpace Weaver stores simulation data, such as your app .zip files and schema file. For more information about Amazon S3, see the ` *Amazon Simple Storage Service User Guide* [https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome).html`__ .

BucketName -> (string)

The name of an Amazon S3 bucket. For more information about buckets, see [Creating, configuring, and working with Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) in the *Amazon Simple Storage Service User Guide* .

ObjectKey -> (string)

The key name of an object in Amazon S3. For more information about Amazon S3 objects and object keys, see [Uploading, downloading, and working with objects in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/uploading-downloading-objects.html) in the *Amazon Simple Storage Service User Guide* .

StartError -> (string)

An error message that SimSpace Weaver returns only if a problem occurs when the simulation is in the `STARTING` state.

Status -> (string)

The current lifecycle state of the simulation.

TargetStatus -> (string)

The desired lifecycle state of the simulation.