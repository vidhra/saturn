# gcloud redis clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create)*

**NAME**

: **gcloud redis clusters create - create a new Memorystore for Redis Cluster instance**

**SYNOPSIS**

: **`gcloud redis clusters create` (`[CLUSTER](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#CLUSTER)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--region)`=`REGION`) [`[--aof-append-fsync](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--aof-append-fsync)`=`AOF_APPEND_FSYNC`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--async)`] [`[--auth-mode](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--auth-mode)`=`AUTH_MODE`] [`[--automated-backup-mode](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--automated-backup-mode)`=`AUTOMATED_BACKUP_MODE`] [`[--automated-backup-start-time](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--automated-backup-start-time)`=`AUTOMATED_BACKUP_START_TIME`] [`[--automated-backup-ttl](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--automated-backup-ttl)`=`AUTOMATED_BACKUP_TTL`] [`[--cross-cluster-replication-role](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--cross-cluster-replication-role)`=`CROSS_CLUSTER_REPLICATION_ROLE`] [`[--deletion-protection](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--deletion-protection)`] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY`] [`[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--network)`=`NETWORK`] [`[--node-type](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--node-type)`=`NODE_TYPE`] [`[--persistence-mode](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--persistence-mode)`=`PERSISTENCE_MODE`] [`[--primary-cluster](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--primary-cluster)`=`PRIMARY_CLUSTER`] [`[--rdb-snapshot-period](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--rdb-snapshot-period)`=`RDB_SNAPSHOT_PERIOD`] [`[--rdb-snapshot-start-time](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--rdb-snapshot-start-time)`=`RDB_SNAPSHOT_START_TIME`] [`[--redis-config](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--redis-config)`=[`KEY`=`VALUE`,…]] [`[--replica-count](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--replica-count)`=`REPLICA_COUNT`] [`[--shard-count](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--shard-count)`=`SHARD_COUNT`] [`[--transit-encryption-mode](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--transit-encryption-mode)`=`TRANSIT_ENCRYPTION_MODE`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--zone)`=`ZONE`] [`[--zone-distribution-mode](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--zone-distribution-mode)`=`ZONE_DISTRIBUTION_MODE`] [`[--import-gcs-object-uris](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--import-gcs-object-uris)`=[`IMPORT_GCS_OBJECT_URIS`,…]     | `[--import-managed-backup](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#--import-managed-backup)`=`IMPORT_MANAGED_BACKUP`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Memorystore for Redis Cluster instance, and uses Private Service
Connect service connectivity automation to automate connectivity for instances.
This command can fail for the following reasons:

- A cluster with the same name already exists.
- The active account does not have permission to create clusters.
- Some required APIs not enabled yet.
- No connection policy defined yet on the network and in the region a cluster will
be created.
- Miss the steps for creating and configuring a service account (to grant
permissions) in both host project and service project, if a shared VPC network
is used.

Refer to [https://cloud.google.com/memorystore/docs/cluster/networking#prerequisites_required_before_creating_a_cluster](https://cloud.google.com/memorystore/docs/cluster/networking#prerequisites_required_before_creating_a_cluster)
for prerequisites.

**EXAMPLES**

: To create a cluster with name `my-redis-cluster` in region
`us-central1` with 3 shards and with a discovery endpoint created on
network "default", run:

```
gcloud redis clusters create my-redis-cluster --region=us-central1 --shard-count=3 --network=projects/NETWORK_PROJECT_ID/global/networks/default
```

**POSITIONAL ARGUMENTS**

: **Cluster resource - Arguments and flags that specify the cluster you want to
create. Your cluster ID must be 1 to 63 characters and use only lowercase
letters, numbers, or hyphens. It must start with a lowercase letter and end with
a lowercase letter or number. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`CLUSTER`**:
ID of the cluster or fully qualified identifier for the cluster.
To set the `cluster` attribute:

- provide the argument `cluster` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the Redis region of the cluster. Overrides the default redis/region
property value for this command invocation.
To set the `region` attribute:

- provide the argument `cluster` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `redis/region`.**

**FLAGS**

: **--aof-append-fsync**:
Fsync configuration. `AOF_APPEND_FSYNC` must be one of:

**`always`**:
Redis explicitly calls fsync for every write command.

**`everysec`**:
(default) Redis explicitly calls fsync every second.

**`no`**:
Redis will not explicitly call fsync.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--auth-mode**:
Available authorization mode of a Redis cluster.
`AUTH_MODE` must be one of:

**`disabled`**:
Authorization is disabled for the cluster.

**`iam-auth`**:
IAM basic authorization is enabled for the cluster.

**--automated-backup-mode**:
Automated backup mode. `AUTOMATED_BACKUP_MODE` must be one
of:

**`disabled`**:
(default) Automated backup is disabled.

**`enabled`**:
Automated backup is enabled.

**--automated-backup-start-time**:
One-hour window when you want automated-backup operations to start. Specify the
time in the format HH:00 on a 24-hour cycle in UTC time.

**--automated-backup-ttl**:
Time to live for automated backups. A backup will be deleted automatically after
the TTL is reached. It ranges from 1 day to 365 days. For example, "10d" for 10
days. If not specified, the default value is 35 days.

**--cross-cluster-replication-role**:
The role of the cluster in cross cluster replication.
`CROSS_CLUSTER_REPLICATION_ROLE` must be (only one value
is supported):

**`secondary`**:
Create a secondary cluster.

**--deletion-protection**:
Enable deletion protection for the Redis Cluster. Use
`--deletion-protection`/`--no-deletion-protection` to
enable/disable it.

**--maintenance-window-day**:
Day of week when the window starts, e.g. `sunday`.
`MAINTENANCE_WINDOW_DAY` must be one of:
`friday`, `monday`, `saturday`,
`sunday`, `thursday`, `tuesday`,
`wednesday`.

**--maintenance-window-hour**:
Hour of day (`0` to `23`) for the start of maintenance
window, in UTC time zone.

**--network**:
The network used to create your instance. It must use the format:
projects/NETWORK_PROJECT_ID/global/networks/NETWORK_ID. The network ID used here
must match the network ID used by the service connection policy. Otherwise, the
create operation fails

**--node-type**:
Node Type of the redis cluster Node. `NODE_TYPE` must be
one of: `redis-highmem-medium`, `redis-highmem-xlarge`,
`redis-shared-core-nano`, `redis-standard-small`.

**--persistence-mode**:
Operation mode for persistence. `PERSISTENCE_MODE` must be
one of:

**`aof`**:
AOF-based persistence

**`disabled`**:
Persistence mode is disabled

**`rdb`**:
RDB-based persistence

**--primary-cluster**:
The primary cluster that the secondary cluster will replicate from. It must use
the format: projects/PROJECT_ID/locations/REGION/clusters/CLUSTER_ID. It must
refer to an existing cluster. Otherwise, the create operation fails.

**--rdb-snapshot-period**:
Attempted period between RDB snapshots.
`RDB_SNAPSHOT_PERIOD` must be one of:

**`12h`**:
12 hours

**`1h`**:
1 hour

**`24h`**:
(default) 24 hours

**`6h`**:
6 hours

**--rdb-snapshot-start-time**:
Date and time of the first snapshot in the ISO 1801 format, and alignment time
for future snapshots. For example, 2024-01-01T01:00:00Z. If not specified, the
current time will be used.

**--redis-config**:
A list of Redis config KEY=VALUE pairs to set on the Redis Cluster according to
[http://redis.io/topics/config](http://redis.io/topics/config).
Currently the supported Redis configs are:

```
maxmemory-clients, maxmemory, maxmemory-policy, notify-keyspace-events,
slowlog-log-slower-than, maxclients.
```

**--replica-count**:
The replica count of each shard.

**--shard-count**:
The shard count of the cluster.

**--transit-encryption-mode**:
Transit encryption mode used for the Redis cluster. If not provided, encryption
is disabled for the cluster. `TRANSIT_ENCRYPTION_MODE`
must be one of:

**`disabled`**:
In-transit encryption is disabled for the cluster.

**`server-authentication`**:
The cluster uses server managed encryption for in-transit encryption.

**--zone**:
The zone used to allocate the cluster nodes. Applicable only if the
zone-distribution-mode is set to single-zone.

**--zone-distribution-mode**:
Determines how the cluster nodes are distributed across zones.
`ZONE_DISTRIBUTION_MODE` must be one of:

**`multi-zone`**:
Allocate cluster nodes across multiple zones.

**`single-zone`**:
Allocate cluster nodes in a single zone.

**--import-gcs-object-uris**

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

: This command uses the `redis/v1` API. The full documentation for this
API can be found at: [https://cloud.google.com/memorystore/docs/redis/](https://cloud.google.com/memorystore/docs/redis/)

**NOTES**

: These variants are also available:

```
gcloud alpha redis clusters create
```

```
gcloud beta redis clusters create
```