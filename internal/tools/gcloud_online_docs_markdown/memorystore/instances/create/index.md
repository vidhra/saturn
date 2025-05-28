# gcloud memorystore instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create)*

**NAME**

: **gcloud memorystore instances create - create a Memorystore instance**

**SYNOPSIS**

: **`gcloud memorystore instances create` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#INSTANCE)` [`[--async](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--async)`] [`[--async-instance-endpoints-deletion-enabled](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--async-instance-endpoints-deletion-enabled)`] [`[--authorization-mode](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--authorization-mode)`=`AUTHORIZATION_MODE`] [`[--deletion-protection-enabled](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--deletion-protection-enabled)`] [`[--endpoints](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--endpoints)`=[`connections`=`CONNECTIONS`]] [`[--engine-configs](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--engine-configs)`=[`ENGINE_CONFIGS`,…]] [`[--engine-version](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--engine-version)`=`ENGINE_VERSION`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--labels)`=[`LABELS`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--location)`=`LOCATION`] [`[--maintenance-policy-weekly-window](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--maintenance-policy-weekly-window)`=[`day`=`DAY`],[`startTime`=`STARTTIME`]] [`[--mode](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--mode)`=`MODE`] [`[--node-type](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--node-type)`=`NODE_TYPE`] [`[--ondemand-maintenance](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--ondemand-maintenance)`] [`[--psc-auto-connections](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--psc-auto-connections)`=[`network`=`NETWORK`],[`port`=`PORT`],[`projectId`=`PROJECTID`]] [`[--replica-count](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--replica-count)`=`REPLICA_COUNT`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--request-id)`=`REQUEST_ID`] [`[--shard-count](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--shard-count)`=`SHARD_COUNT`] [`[--transit-encryption-mode](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--transit-encryption-mode)`=`TRANSIT_ENCRYPTION_MODE`] [`[--aof-config-append-fsync](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--aof-config-append-fsync)`=`AOF_CONFIG_APPEND_FSYNC` `[--persistence-config-mode](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--persistence-config-mode)`=`PERSISTENCE_CONFIG_MODE` `[--rdb-config-snapshot-period](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--rdb-config-snapshot-period)`=`RDB_CONFIG_SNAPSHOT_PERIOD` `[--rdb-config-snapshot-start-time](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--rdb-config-snapshot-start-time)`=`RDB_CONFIG_SNAPSHOT_START_TIME`] [`[--automated-backup-config-mode](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--automated-backup-config-mode)`=`AUTOMATED_BACKUP_CONFIG_MODE` `[--automated-backup-config-retention](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--automated-backup-config-retention)`=`AUTOMATED_BACKUP_CONFIG_RETENTION` (`[--fixed-frequency-schedule-start-time-hours](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--fixed-frequency-schedule-start-time-hours)`=`FIXED_FREQUENCY_SCHEDULE_START_TIME_HOURS` `[--fixed-frequency-schedule-start-time-minutes](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--fixed-frequency-schedule-start-time-minutes)`=`FIXED_FREQUENCY_SCHEDULE_START_TIME_MINUTES` `[--fixed-frequency-schedule-start-time-nanos](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--fixed-frequency-schedule-start-time-nanos)`=`FIXED_FREQUENCY_SCHEDULE_START_TIME_NANOS` `[--fixed-frequency-schedule-start-time-seconds](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--fixed-frequency-schedule-start-time-seconds)`=`FIXED_FREQUENCY_SCHEDULE_START_TIME_SECONDS`)] [`[--cross-instance-replication-config-role](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--cross-instance-replication-config-role)`=`CROSS_INSTANCE_REPLICATION_CONFIG_ROLE` : `[--cross-instance-replication-config-secondary-instances](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--cross-instance-replication-config-secondary-instances)`=[`instance`=`INSTANCE`] `[--primary-instance](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--primary-instance)`=`PRIMARY_INSTANCE`] [`[--gcs-source-uris](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--gcs-source-uris)`=[`GCS_SOURCE_URIS`,…]     | `[--managed-backup-source](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--managed-backup-source)`=`MANAGED_BACKUP_SOURCE`] [`[--zone-distribution-config](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--zone-distribution-config)`=`ZONE_DISTRIBUTION_CONFIG` `[--zone-distribution-config-mode](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#--zone-distribution-config-mode)`=`ZONE_DISTRIBUTION_CONFIG_MODE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/memorystore/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a Memorystore instance.
A service connection policy for service class `gcp-memorystore` must
already exist for the location and network. Refer to [creation
prerequisites](https://cloud.google.com/memorystore/docs/valkey/networking#prerequisites_required_before_creating_an_instance) for more details.

**EXAMPLES**

: To create a three shard Memorystore instance `my-instance` in project
`my-project` and location `us-central1`, run:

```
gcloud memorystore instances create my-instance --project=my-project --location=us-central1 --shard-count=3 --psc-auto-connections="network=NETWORK,projectId=PROJECT_ID"
```

To create a three shard Memorystore instance `my-instance` in project
`my-project`, location `us-central1`, with one replica per
shard, and TLS enabled, run:

```
gcloud memorystore instances create my-instance --project=my-project --location=us-central1 --shard-count=3 --psc-auto-connections="network=NETWORK,projectId=PROJECT_ID" --transit-encryption-mode=server-authentication --replica-count=1
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Identifier. Unique name of the instance. Format:
projects/{project}/locations/{location}/instances/{instance} This represents a
Cloud resource. (NOTE) Some attributes are not given arguments in this group but
can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--location` on the command line.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--async-instance-endpoints-deletion-enabled**

**--authorization-mode**:
Authorization mode of the instance. `AUTHORIZATION_MODE`
must be one of:

**`auth-disabled`**:
Authorization disabled.

**`iam-auth`**:
IAM basic authorization.

**--deletion-protection-enabled**

**--endpoints**:
Endpoints for the instance.

**`connections`**:
A group of PSC connections. They are created in the same VPC network, one for
each service attachment in the cluster.

**`pscAutoConnection`**:
Detailed information of a PSC connection that is created through service
connectivity automation.

**`network`**:
The network where the PSC endpoints are created, in the form of
projects/{project_id}/global/networks/{network_id}.

**`port`**:
port will only be set for Primary/Reader or Discovery endpoint.

**`projectId`**:
The consumer project_id where PSC connections are established. This should be
the same project_id that the instance is being created in.

`Shorthand Example:`

```
--endpoints=connections=[{pscAutoConnection={network=string,port=int,projectId=string}}] --endpoints=connections=[{pscAutoConnection={network=string,port=int,projectId=string}}]
```

`JSON Example:`

```
--endpoints='[{"connections": [{"pscAutoConnection": {"network": "string", "port": int, "projectId": "string"}}]}]'
```

`File Example:`

```
--endpoints=path_to_file.(yaml|json)
```

**--engine-configs**:
User-provided engine configurations for the instance.

**`KEY`**:
Sets `KEY` value.

**`VALUE`**:
Sets `VALUE` value.

`Shorthand Example:`

```
--engine-configs=string=string
```

`JSON Example:`

```
--engine-configs='{"string": "string"}'
```

`File Example:`

```
--engine-configs=path_to_file.(yaml|json)
```

**--engine-version**:
Engine version of the instance.

**--labels**:
Labels to represent user-provided metadata.

**`KEY`**:
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers.

**`VALUE`**:
Values must contain only hyphens (`-`), underscores (`_`),
lowercase characters, and numbers.

`Shorthand Example:`

```
--labels=string=string
```

`JSON Example:`

```
--labels='{"string": "string"}'
```

`File Example:`

```
--labels=path_to_file.(yaml|json)
```

**--location**:
For resources [instance], provides fallback value for resource location
attribute. When the resource's full URI path is not provided, location will
fallback to this flag value.

**--maintenance-policy-weekly-window**

**--mode**:
The mode config for the instance. `MODE` must be one of:

**`cluster`**:
Instance is in cluster mode.

**`cluster-disabled`**:
Cluster mode is disabled for the instance.

**`standalone`**:
Deprecated: Use CLUSTER_DISABLED instead.

**--node-type**:
Machine type for individual nodes of the instance.
`NODE_TYPE` must be one of:

**`highmem-medium`**:
High memory medium.

**`highmem-xlarge`**:
High memory extra large.

**`shared-core-nano`**:
Shared core nano.

**`standard-small`**:
Standard small.

**--ondemand-maintenance**

**--psc-auto-connections**:
Deprecated: Use the endpoints.connections.psc_auto_connection value instead.

**`network`**:
The network where the PSC endpoints are created, in the form of
projects/{project_id}/global/networks/{network_id}.

**`port`**:
port will only be set for Primary/Reader or Discovery endpoint.

**`projectId`**:
The consumer project_id where PSC connections are established. This should be
the same project_id that the instance is being created in.

`Shorthand Example:`

```
--psc-auto-connections=network=string,port=int,projectId=string --psc-auto-connections=network=string,port=int,projectId=string
```

`JSON Example:`

```
--psc-auto-connections='[{"network": "string", "port": int, "projectId": "string"}]'
```

`File Example:`

```
--psc-auto-connections=path_to_file.(yaml|json)
```

**--replica-count**

**--request-id**:
An optional request ID to identify requests. Specify a unique request ID so that
if you must retry your request, the server will know to ignore the request if it
has already been completed. The server will guarantee that for at least 60
minutes since the first request.
For example, consider a situation where you make an initial request and the
request times out. If you make the request again with the same request ID, the
server can check if original operation with the same request ID was received,
and if so, will ignore the second request. This prevents clients from
accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--shard-count**:
Number of shards for the instance.

**--transit-encryption-mode**:
In-transit encryption mode of the instance.
`TRANSIT_ENCRYPTION_MODE` must be one of:

**`server-authentication`**:
Server-managed encryption is used for in-transit encryption.

**`transit-encryption-disabled`**:
In-transit encryption is disabled.

**--aof-config-append-fsync**

**--automated-backup-config-mode**

**--cross-instance-replication-config-role**

**--gcs-source-uris**

**--zone-distribution-config**

**GCLOUD WIDE FLAGS**

: These flags are available to all commands: `[--access-token-file](https://cloud.google.com/sdk/gcloud/reference#--access-token-file)`,
`[--account](https://cloud.google.com/sdk/gcloud/reference#--account)`, `[--billing-project](https://cloud.google.com/sdk/gcloud/reference#--billing-project)`,
`[--configuration](https://cloud.google.com/sdk/gcloud/reference#--configuration)`,
`[--flags-file](https://cloud.google.com/sdk/gcloud/reference#--flags-file)`,
`[--flatten](https://cloud.google.com/sdk/gcloud/reference#--flatten)`, `[--format](https://cloud.google.com/sdk/gcloud/reference#--format)`, `[--help](https://cloud.google.com/sdk/gcloud/reference#--help)`, `[--impersonate-service-account](https://cloud.google.com/sdk/gcloud/reference#--impersonate-service-account)`,
`[--log-http](https://cloud.google.com/sdk/gcloud/reference#--log-http)`,
`[--project](https://cloud.google.com/sdk/gcloud/reference#--project)`, `[--quiet](https://cloud.google.com/sdk/gcloud/reference#--quiet)`, `[--trace-token](https://cloud.google.com/sdk/gcloud/reference#--trace-token)`, `[--user-output-enabled](https://cloud.google.com/sdk/gcloud/reference#--user-output-enabled)`,
`[--verbosity](https://cloud.google.com/sdk/gcloud/reference#--verbosity)`.
Run `$ [gcloud help](https://cloud.google.com/sdk/gcloud/reference)` for details.

**API REFERENCE**

: This command uses the `memorystore/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/memorystore/](https://cloud.google.com/memorystore/)

**NOTES**

: These variants are also available:

```
gcloud alpha memorystore instances create
```

```
gcloud beta memorystore instances create
```