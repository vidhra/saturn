# create-kx-clusterÂ¶

*Source: [https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/create-kx-cluster.html](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/create-kx-cluster.html)*

[ [aws](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html#cli-aws) . [finspace](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/finspace/index.html#cli-aws-finspace) ]

# create-kx-cluster

## Description

Creates a new kdb cluster.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/finspace-2021-03-12/CreateKxCluster)

## Synopsis

```
create-kx-cluster
[--client-token <value>]
--environment-id <value>
--cluster-name <value>
--cluster-type <value>
[--tickerplant-log-configuration <value>]
[--databases <value>]
[--cache-storage-configurations <value>]
[--auto-scaling-configuration <value>]
[--cluster-description <value>]
[--capacity-configuration <value>]
--release-label <value>
--vpc-configuration <value>
[--initialization-script <value>]
[--command-line-arguments <value>]
[--code <value>]
[--execution-role <value>]
[--savedown-storage-configuration <value>]
--az-mode <value>
[--availability-zone-id <value>]
[--tags <value>]
[--scaling-group-configuration <value>]
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

A unique identifier for the kdb environment.

`--cluster-name` (string)

A unique name for the cluster that you want to create.

`--cluster-type` (string)

Specifies the type of KDB database that is being created. The following types are available:

- HDB â A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.
- RDB â A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the `savedownStorageConfiguration` parameter.
- GATEWAY â A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.
- GP â A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only `SINGLE` AZ mode.
- Tickerplant â A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.

Possible values:

- `HDB`
- `RDB`
- `GATEWAY`
- `GP`
- `TICKERPLANT`

`--tickerplant-log-configuration` (structure)

A configuration to store Tickerplant logs. It consists of a list of volumes that will be mounted to your cluster. For the cluster type `Tickerplant` , the location of the TP volume on the cluster will be available by using the global variable `.aws.tp_log_path` .

tickerplantLogVolumes -> (list)

The name of the volumes for tickerplant logs.

(string)

Shorthand Syntax:

```
tickerplantLogVolumes=string,string
```

JSON Syntax:

```
{
  "tickerplantLogVolumes": ["string", ...]
}
```

`--databases` (list)

A list of databases that will be available for querying.

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

`--cache-storage-configurations` (list)

The configurations for a read only cache storage associated with a cluster. This cache will be stored as an FSx Lustre that reads from the S3 store.

(structure)

The configuration for read only disk cache associated with a cluster.

type -> (string)

The type of cache storage. The valid values are:

- CACHE_1000 â This type provides at least 1000 MB/s disk access throughput.
- CACHE_250 â This type provides at least 250 MB/s disk access throughput.
- CACHE_12 â This type provides at least 12 MB/s disk access throughput.

For cache type `CACHE_1000` and `CACHE_250` you can select cache size as 1200 GB or increments of 2400 GB. For cache type `CACHE_12` you can select the cache size in increments of 6000 GB.

size -> (integer)

The size of cache in Gigabytes.

Shorthand Syntax:

```
type=string,size=integer ...
```

JSON Syntax:

```
[
  {
    "type": "string",
    "size": integer
  }
  ...
]
```

`--auto-scaling-configuration` (structure)

The configuration based on which FinSpace will scale in or scale out nodes in your cluster.

minNodeCount -> (integer)

The lowest number of nodes to scale. This value must be at least 1 and less than the `maxNodeCount` . If the nodes in a cluster belong to multiple availability zones, then `minNodeCount` must be at least 3.

maxNodeCount -> (integer)

The highest number of nodes to scale. This value cannot be greater than 5.

autoScalingMetric -> (string)

The metric your cluster will track in order to scale in and out. For example, `CPU_UTILIZATION_PERCENTAGE` is the average CPU usage across all the nodes in a cluster.

metricTarget -> (double)

The desired value of the chosen `autoScalingMetric` . When the metric drops below this value, the cluster will scale in. When the metric goes above this value, the cluster will scale out. You can set the target value between 1 and 100 percent.

scaleInCooldownSeconds -> (double)

The duration in seconds that FinSpace will wait after a scale in event before initiating another scaling event.

scaleOutCooldownSeconds -> (double)

The duration in seconds that FinSpace will wait after a scale out event before initiating another scaling event.

Shorthand Syntax:

```
minNodeCount=integer,maxNodeCount=integer,autoScalingMetric=string,metricTarget=double,scaleInCooldownSeconds=double,scaleOutCooldownSeconds=double
```

JSON Syntax:

```
{
  "minNodeCount": integer,
  "maxNodeCount": integer,
  "autoScalingMetric": "CPU_UTILIZATION_PERCENTAGE",
  "metricTarget": double,
  "scaleInCooldownSeconds": double,
  "scaleOutCooldownSeconds": double
}
```

`--cluster-description` (string)

A description of the cluster.

`--capacity-configuration` (structure)

A structure for the metadata of a cluster. It includes information like the CPUs needed, memory of instances, and number of instances.

nodeType -> (string)

The type that determines the hardware of the host computer used for your cluster instance. Each node type offers different memory and storage capabilities. Choose a node type based on the requirements of the application or software that you plan to run on your instance.

You can only specify one of the following values:

- `kx.s.large` â The node type with a configuration of 12 GiB memory and 2 vCPUs.
- `kx.s.xlarge` â The node type with a configuration of 27 GiB memory and 4 vCPUs.
- `kx.s.2xlarge` â The node type with a configuration of 54 GiB memory and 8 vCPUs.
- `kx.s.4xlarge` â The node type with a configuration of 108 GiB memory and 16 vCPUs.
- `kx.s.8xlarge` â The node type with a configuration of 216 GiB memory and 32 vCPUs.
- `kx.s.16xlarge` â The node type with a configuration of 432 GiB memory and 64 vCPUs.
- `kx.s.32xlarge` â The node type with a configuration of 864 GiB memory and 128 vCPUs.

nodeCount -> (integer)

The number of instances running in a cluster.

Shorthand Syntax:

```
nodeType=string,nodeCount=integer
```

JSON Syntax:

```
{
  "nodeType": "string",
  "nodeCount": integer
}
```

`--release-label` (string)

The version of FinSpace managed kdb to run.

`--vpc-configuration` (structure)

Configuration details about the network where the Privatelink endpoint of the cluster resides.

vpcId -> (string)

The identifier of the VPC endpoint.

securityGroupIds -> (list)

The unique identifier of the VPC security group applied to the VPC endpoint ENI for the cluster.

(string)

subnetIds -> (list)

The identifier of the subnet that the Privatelink VPC endpoint uses to connect to the cluster.

(string)

ipAddressType -> (string)

The IP address type for cluster network configuration parameters. The following type is available:

- IP_V4 â IP address version 4

Shorthand Syntax:

```
vpcId=string,securityGroupIds=string,string,subnetIds=string,string,ipAddressType=string
```

JSON Syntax:

```
{
  "vpcId": "string",
  "securityGroupIds": ["string", ...],
  "subnetIds": ["string", ...],
  "ipAddressType": "IP_V4"
}
```

`--initialization-script` (string)

Specifies a Q program that will be run at launch of a cluster. It is a relative path within *.zip* file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, `somedir/init.q` .

`--command-line-arguments` (list)

Defines the key-value pairs to make them available inside the cluster.

(structure)

Defines the key-value pairs to make them available inside the cluster.

key -> (string)

The name of the key.

value -> (string)

The value of the key.

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

`--code` (structure)

The details of the custom code that you want to use inside a cluster when analyzing a data. It consists of the S3 source bucket, location, S3 object version, and the relative path from where the custom code is loaded into the cluster.

s3Bucket -> (string)

A unique name for the S3 bucket.

s3Key -> (string)

The full S3 path (excluding bucket) to the .zip file. This file contains the code that is loaded onto the cluster when itâs started.

s3ObjectVersion -> (string)

The version of an S3 object.

Shorthand Syntax:

```
s3Bucket=string,s3Key=string,s3ObjectVersion=string
```

JSON Syntax:

```
{
  "s3Bucket": "string",
  "s3Key": "string",
  "s3ObjectVersion": "string"
}
```

`--execution-role` (string)

An IAM role that defines a set of permissions associated with a cluster. These permissions are assumed when a cluster attempts to access another cluster.

`--savedown-storage-configuration` (structure)

The size and type of the temporary storage that is used to hold data during the savedown process. This parameter is required when you choose `clusterType` as RDB. All the data written to this storage space is lost when the cluster node is restarted.

type -> (string)

The type of writeable storage space for temporarily storing your savedown data. The valid values are:

- SDS01 â This type represents 3000 IOPS and io2 ebs volume type.

size -> (integer)

The size of temporary storage in gibibytes.

volumeName -> (string)

The name of the kdb volume that you want to use as writeable save-down storage for clusters.

Shorthand Syntax:

```
type=string,size=integer,volumeName=string
```

JSON Syntax:

```
{
  "type": "SDS01",
  "size": integer,
  "volumeName": "string"
}
```

`--az-mode` (string)

The number of availability zones you want to assign per cluster. This can be one of the following

- `SINGLE` â Assigns one availability zone per cluster.
- `MULTI` â Assigns all the availability zones per cluster.

Possible values:

- `SINGLE`
- `MULTI`

`--availability-zone-id` (string)

The availability zone identifiers for the requested regions.

`--tags` (map)

A list of key-value pairs to label the cluster. You can add up to 50 tags to a cluster.

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

`--scaling-group-configuration` (structure)

The structure that stores the configuration details of a scaling group.

scalingGroupName -> (string)

A unique identifier for the kdb scaling group.

memoryLimit -> (integer)

An optional hard limit on the amount of memory a kdb cluster can use.

memoryReservation -> (integer)

A reservation of the minimum amount of memory that should be available on the scaling group for a kdb cluster to be successfully placed in a scaling group.

nodeCount -> (integer)

The number of kdb cluster nodes.

cpu -> (double)

The number of vCPUs that you want to reserve for each node of this kdb cluster on the scaling group host.

Shorthand Syntax:

```
scalingGroupName=string,memoryLimit=integer,memoryReservation=integer,nodeCount=integer,cpu=double
```

JSON Syntax:

```
{
  "scalingGroupName": "string",
  "memoryLimit": integer,
  "memoryReservation": integer,
  "nodeCount": integer,
  "cpu": double
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

environmentId -> (string)

A unique identifier for the kdb environment.

status -> (string)

The status of cluster creation.

- PENDING â The cluster is pending creation.
- CREATING â The cluster creation process is in progress.
- CREATE_FAILED â The cluster creation process has failed.
- RUNNING â The cluster creation process is running.
- UPDATING â The cluster is in the process of being updated.
- DELETING â The cluster is in the process of being deleted.
- DELETED â The cluster has been deleted.
- DELETE_FAILED â The cluster failed to delete.

statusReason -> (string)

The error message when a failed state occurs.

clusterName -> (string)

A unique name for the cluster.

clusterType -> (string)

Specifies the type of KDB database that is being created. The following types are available:

- HDB â A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.
- RDB â A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the `savedownStorageConfiguration` parameter.
- GATEWAY â A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.
- GP â A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only `SINGLE` AZ mode.
- Tickerplant â A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.

tickerplantLogConfiguration -> (structure)

A configuration to store the Tickerplant logs. It consists of a list of volumes that will be mounted to your cluster. For the cluster type `Tickerplant` , the location of the TP volume on the cluster will be available by using the global variable `.aws.tp_log_path` .

tickerplantLogVolumes -> (list)

The name of the volumes for tickerplant logs.

(string)

volumes -> (list)

A list of volumes mounted on the cluster.

(structure)

The structure that consists of name and type of volume.

volumeName -> (string)

A unique identifier for the volume.

volumeType -> (string)

The type of file system volume. Currently, FinSpace only supports `NAS_1` volume type.

databases -> (list)

A list of databases that will be available for querying.

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

cacheStorageConfigurations -> (list)

The configurations for a read only cache storage associated with a cluster. This cache will be stored as an FSx Lustre that reads from the S3 store.

(structure)

The configuration for read only disk cache associated with a cluster.

type -> (string)

The type of cache storage. The valid values are:

- CACHE_1000 â This type provides at least 1000 MB/s disk access throughput.
- CACHE_250 â This type provides at least 250 MB/s disk access throughput.
- CACHE_12 â This type provides at least 12 MB/s disk access throughput.

For cache type `CACHE_1000` and `CACHE_250` you can select cache size as 1200 GB or increments of 2400 GB. For cache type `CACHE_12` you can select the cache size in increments of 6000 GB.

size -> (integer)

The size of cache in Gigabytes.

autoScalingConfiguration -> (structure)

The configuration based on which FinSpace will scale in or scale out nodes in your cluster.

minNodeCount -> (integer)

The lowest number of nodes to scale. This value must be at least 1 and less than the `maxNodeCount` . If the nodes in a cluster belong to multiple availability zones, then `minNodeCount` must be at least 3.

maxNodeCount -> (integer)

The highest number of nodes to scale. This value cannot be greater than 5.

autoScalingMetric -> (string)

The metric your cluster will track in order to scale in and out. For example, `CPU_UTILIZATION_PERCENTAGE` is the average CPU usage across all the nodes in a cluster.

metricTarget -> (double)

The desired value of the chosen `autoScalingMetric` . When the metric drops below this value, the cluster will scale in. When the metric goes above this value, the cluster will scale out. You can set the target value between 1 and 100 percent.

scaleInCooldownSeconds -> (double)

The duration in seconds that FinSpace will wait after a scale in event before initiating another scaling event.

scaleOutCooldownSeconds -> (double)

The duration in seconds that FinSpace will wait after a scale out event before initiating another scaling event.

clusterDescription -> (string)

A description of the cluster.

capacityConfiguration -> (structure)

A structure for the metadata of a cluster. It includes information like the CPUs needed, memory of instances, and number of instances.

nodeType -> (string)

The type that determines the hardware of the host computer used for your cluster instance. Each node type offers different memory and storage capabilities. Choose a node type based on the requirements of the application or software that you plan to run on your instance.

You can only specify one of the following values:

- `kx.s.large` â The node type with a configuration of 12 GiB memory and 2 vCPUs.
- `kx.s.xlarge` â The node type with a configuration of 27 GiB memory and 4 vCPUs.
- `kx.s.2xlarge` â The node type with a configuration of 54 GiB memory and 8 vCPUs.
- `kx.s.4xlarge` â The node type with a configuration of 108 GiB memory and 16 vCPUs.
- `kx.s.8xlarge` â The node type with a configuration of 216 GiB memory and 32 vCPUs.
- `kx.s.16xlarge` â The node type with a configuration of 432 GiB memory and 64 vCPUs.
- `kx.s.32xlarge` â The node type with a configuration of 864 GiB memory and 128 vCPUs.

nodeCount -> (integer)

The number of instances running in a cluster.

releaseLabel -> (string)

A version of the FinSpace managed kdb to run.

vpcConfiguration -> (structure)

Configuration details about the network where the Privatelink endpoint of the cluster resides.

vpcId -> (string)

The identifier of the VPC endpoint.

securityGroupIds -> (list)

The unique identifier of the VPC security group applied to the VPC endpoint ENI for the cluster.

(string)

subnetIds -> (list)

The identifier of the subnet that the Privatelink VPC endpoint uses to connect to the cluster.

(string)

ipAddressType -> (string)

The IP address type for cluster network configuration parameters. The following type is available:

- IP_V4 â IP address version 4

initializationScript -> (string)

Specifies a Q program that will be run at launch of a cluster. It is a relative path within *.zip* file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, `somedir/init.q` .

commandLineArguments -> (list)

Defines the key-value pairs to make them available inside the cluster.

(structure)

Defines the key-value pairs to make them available inside the cluster.

key -> (string)

The name of the key.

value -> (string)

The value of the key.

code -> (structure)

The details of the custom code that you want to use inside a cluster when analyzing a data. It consists of the S3 source bucket, location, S3 object version, and the relative path from where the custom code is loaded into the cluster.

s3Bucket -> (string)

A unique name for the S3 bucket.

s3Key -> (string)

The full S3 path (excluding bucket) to the .zip file. This file contains the code that is loaded onto the cluster when itâs started.

s3ObjectVersion -> (string)

The version of an S3 object.

executionRole -> (string)

An IAM role that defines a set of permissions associated with a cluster. These permissions are assumed when a cluster attempts to access another cluster.

lastModifiedTimestamp -> (timestamp)

The last time that the cluster was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.

savedownStorageConfiguration -> (structure)

The size and type of the temporary storage that is used to hold data during the savedown process. This parameter is required when you choose `clusterType` as RDB. All the data written to this storage space is lost when the cluster node is restarted.

type -> (string)

The type of writeable storage space for temporarily storing your savedown data. The valid values are:

- SDS01 â This type represents 3000 IOPS and io2 ebs volume type.

size -> (integer)

The size of temporary storage in gibibytes.

volumeName -> (string)

The name of the kdb volume that you want to use as writeable save-down storage for clusters.

azMode -> (string)

The number of availability zones you want to assign per cluster. This can be one of the following

- `SINGLE` â Assigns one availability zone per cluster.
- `MULTI` â Assigns all the availability zones per cluster.

availabilityZoneId -> (string)

The availability zone identifiers for the requested regions.

createdTimestamp -> (timestamp)

The timestamp at which the cluster was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.

scalingGroupConfiguration -> (structure)

The structure that stores the configuration details of a scaling group.

scalingGroupName -> (string)

A unique identifier for the kdb scaling group.

memoryLimit -> (integer)

An optional hard limit on the amount of memory a kdb cluster can use.

memoryReservation -> (integer)

A reservation of the minimum amount of memory that should be available on the scaling group for a kdb cluster to be successfully placed in a scaling group.

nodeCount -> (integer)

The number of kdb cluster nodes.

cpu -> (double)

The number of vCPUs that you want to reserve for each node of this kdb cluster on the scaling group host.