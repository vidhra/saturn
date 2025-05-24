# update-kx-cluster-databasesÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/update-kx-cluster-databases.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/update-kx-cluster-databases.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [finspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/index.html#cli-aws-finspace) ]

# update-kx-cluster-databases

## Description

Updates the databases mounted on a kdb cluster, which includes the `changesetId` and all the dbPaths to be cached. This API does not allow you to change a database name or add a database if you created a cluster without one.

Using this API you can point a cluster to a different changeset and modify a list of partitions being cached.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/finspace-2021-03-12/UpdateKxClusterDatabases)

## Synopsis

```
update-kx-cluster-databases
--environment-id <value>
--cluster-name <value>
[--client-token <value>]
--databases <value>
[--deployment-configuration <value>]
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

The unique identifier of a kdb environment.

`--cluster-name` (string)

A unique name for the cluster that you want to modify.

`--client-token` (string)

A token that ensures idempotency. This token expires in 10 minutes.

`--databases` (list)

The structure of databases mounted on the cluster.

(structure)

The configuration of data that is available for querying from this database.

databaseName -> (string)

The name of the kdb database. When this parameter is specified in the structure, S3 with the whole database is included by default.

cacheConfigurations -> (list)

Configuration details for the disk cache used to increase performance reading from a kdb database mounted to the cluster.

(structure)

The structure of database cache configuration that is used for mapping database paths to cache types in clusters.

cacheType -> (string)

The type of disk cache. This parameter is used to map the database path to cache storage. The valid values are:

- CACHE_1000 â This type provides at least 1000 MB/s disk access throughput.

dbPaths -> (list)

Specifies the portions of database that will be loaded into the cache for access.

(string)

dataviewName -> (string)

The name of the dataview to be used for caching historical data on disk.

changesetId -> (string)

A unique identifier of the changeset that is associated with the cluster.

dataviewName -> (string)

The name of the dataview to be used for caching historical data on disk.

dataviewConfiguration -> (structure)

The configuration of the dataview to be used with specified cluster.

dataviewName -> (string)

The unique identifier of the dataview.

dataviewVersionId -> (string)

The version of the dataview corresponding to a given changeset.

changesetId -> (string)

A unique identifier for the changeset.

segmentConfigurations -> (list)

The db path and volume configuration for the segmented database.

(structure)

The configuration that contains the database path of the data that you want to place on each selected volume. Each segment must have a unique database path for each volume. If you do not explicitly specify any database path for a volume, they are accessible from the cluster through the default S3/object store segment.

dbPaths -> (list)

The database path of the data that you want to place on each selected volume for the segment. Each segment must have a unique database path for each volume.

(string)

volumeName -> (string)

The name of the volume where you want to add data.

onDemand -> (boolean)

Enables on-demand caching on the selected database path when a particular file or a column of the database is accessed. When on demand caching is **True** , dataviews perform minimal loading of files on the filesystem as needed. When it is set to **False** , everything is cached. The default value is **False** .

JSON Syntax:

```
[
  {
    "databaseName": "string",
    "cacheConfigurations": [
      {
        "cacheType": "string",
        "dbPaths": ["string", ...],
        "dataviewName": "string"
      }
      ...
    ],
    "changesetId": "string",
    "dataviewName": "string",
    "dataviewConfiguration": {
      "dataviewName": "string",
      "dataviewVersionId": "string",
      "changesetId": "string",
      "segmentConfigurations": [
        {
          "dbPaths": ["string", ...],
          "volumeName": "string",
          "onDemand": true|false
        }
        ...
      ]
    }
  }
  ...
]
```

`--deployment-configuration` (structure)

The configuration that allows you to choose how you want to update the databases on a cluster.

deploymentStrategy -> (string)

The type of deployment that you want on a cluster.

- ROLLING â This options updates the cluster by stopping the exiting q process and starting a new q process with updated configuration.
- NO_RESTART â This option updates the cluster without stopping the running q process. It is only available for `HDB` type cluster. This option is quicker as it reduces the turn around time to update configuration on a cluster.  With this deployment mode, you cannot update the `initializationScript` and `commandLineArguments` parameters.

Shorthand Syntax:

```
deploymentStrategy=string
```

JSON Syntax:

```
{
  "deploymentStrategy": "NO_RESTART"|"ROLLING"
}
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

None