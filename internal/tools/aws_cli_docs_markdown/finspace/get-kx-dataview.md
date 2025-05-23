# get-kx-dataviewÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/get-kx-dataview.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/get-kx-dataview.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [finspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/index.html#cli-aws-finspace) ]

# get-kx-dataview

## Description

Retrieves details of the dataview.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/finspace-2021-03-12/GetKxDataview)

## Synopsis

```
get-kx-dataview
--environment-id <value>
--database-name <value>
--dataview-name <value>
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

`--environment-id` (string)

A unique identifier for the kdb environment, from where you want to retrieve the dataview details.

`--database-name` (string)

The name of the database where you created the dataview.

`--dataview-name` (string)

A unique identifier for the dataview.

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

databaseName -> (string)

The name of the database where you created the dataview.

dataviewName -> (string)

A unique identifier for the dataview.

azMode -> (string)

The number of availability zones you want to assign per volume. Currently, FinSpace only supports `SINGLE` for volumes. This places dataview in a single AZ.

availabilityZoneId -> (string)

The identifier of the availability zones.

changesetId -> (string)

A unique identifier of the changeset that you want to use to ingest data.

segmentConfigurations -> (list)

The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.

(structure)

The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.

dbPaths -> (list)

The database path of the data that you want to place on each selected volume for the segment. Each segment must have a unique database path for each volume.

(string)

volumeName -> (string)

The name of the volume where you want to add data.

onDemand -> (boolean)

Enables on-demand caching on the selected database path when a particular file or a column of the database is accessed. When on demand caching is **True** , dataviews perform minimal loading of files on the filesystem as needed. When it is set to **False** , everything is cached. The default value is **False** .

activeVersions -> (list)

The current active changeset versions of the database on the given dataview.

(structure)

The active version of the dataview that is currently in use by this cluster.

changesetId -> (string)

A unique identifier for the changeset.

segmentConfigurations -> (list)

The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.

(structure)

The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.

dbPaths -> (list)

The database path of the data that you want to place on each selected volume for the segment. Each segment must have a unique database path for each volume.

(string)

volumeName -> (string)

The name of the volume where you want to add data.

onDemand -> (boolean)

Enables on-demand caching on the selected database path when a particular file or a column of the database is accessed. When on demand caching is **True** , dataviews perform minimal loading of files on the filesystem as needed. When it is set to **False** , everything is cached. The default value is **False** .

attachedClusters -> (list)

The list of clusters that are currently using this dataview.

(string)

createdTimestamp -> (timestamp)

The timestamp at which the dataview version was active. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.

versionId -> (string)

A unique identifier of the active version.

description -> (string)

A description of the dataview.

autoUpdate -> (boolean)

The option to specify whether you want to apply all the future additions and corrections automatically to the dataview when new changesets are ingested. The default value is false.

readWrite -> (boolean)

Returns True if the dataview is created as writeable and False otherwise.

environmentId -> (string)

A unique identifier for the kdb environment, from where you want to retrieve the dataview details.

createdTimestamp -> (timestamp)

The timestamp at which the dataview was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.

lastModifiedTimestamp -> (timestamp)

The last time that the dataview was updated in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.

status -> (string)

The status of dataview creation.

- `CREATING` â The dataview creation is in progress.
- `UPDATING` â The dataview is in the process of being updated.
- `ACTIVE` â The dataview is active.

statusReason -> (string)

The error message when a failed state occurs.