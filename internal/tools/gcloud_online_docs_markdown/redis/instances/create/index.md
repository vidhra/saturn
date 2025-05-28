# gcloud redis instances create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/redis/instances/create](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create)*

**NAME**

: **gcloud redis instances create - create a Memorystore Redis instance**

**SYNOPSIS**

: **`gcloud redis instances create` (`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#INSTANCE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--region)`=`REGION`) [`[--alternative-zone](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--alternative-zone)`=`ALTERNATIVE_ZONE`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--async)`] [`[--connect-mode](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--connect-mode)`=`CONNECT_MODE`] [`[--customer-managed-key](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--customer-managed-key)`=`CUSTOMER_MANAGED_KEY`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--display-name)`=`DISPLAY_NAME`] [`[--enable-auth](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--enable-auth)`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--labels)`=[`KEY`=`VALUE`,…]] [`[--maintenance-window-day](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--maintenance-window-day)`=`MAINTENANCE_WINDOW_DAY`] [`[--maintenance-window-hour](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--maintenance-window-hour)`=`MAINTENANCE_WINDOW_HOUR`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--network)`=`NETWORK`; default="default"] [`[--persistence-mode](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--persistence-mode)`=`PERSISTENCE_MODE`] [`[--rdb-snapshot-period](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--rdb-snapshot-period)`=`RDB_SNAPSHOT_PERIOD`] [`[--rdb-snapshot-start-time](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--rdb-snapshot-start-time)`=`RDB_SNAPSHOT_START_TIME`] [`[--read-replicas-mode](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--read-replicas-mode)`=`READ_REPLICAS_MODE`] [`[--redis-config](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--redis-config)`=[`KEY`=`VALUE`,…]] [`[--redis-version](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--redis-version)`=`VERSION`] [`[--replica-count](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--replica-count)`=`REPLICA_COUNT`] [`[--reserved-ip-range](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--reserved-ip-range)`=`RESERVED_IP_RANGE`] [`[--size](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--size)`=`SIZE`; default=1] [`[--tier](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--tier)`=`TIER`; default="basic"] [`[--transit-encryption-mode](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--transit-encryption-mode)`=`TRANSIT_ENCRYPTION_MODE`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/redis/instances/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new Redis instance.
This command can fail for the following reasons:

- An instance with the same name already exists.
- The active account does not have permission to create instances.

**EXAMPLES**

: To create a basic tier instance with the name `my-redis-instance` in
region `us-central-1` with memory size of 5 GiB, run:

```
gcloud redis instances create my-redis-instance --region=us-central1 --size=5
```

**POSITIONAL ARGUMENTS**

: **Instance resource - Arguments and flags that specify the Memorystore Redis
instance you want to create. The arguments in this group can be used to specify
the attributes of this resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`INSTANCE`**:
ID of the instance or fully qualified identifier for the instance.
To set the `instance` attribute:

- provide the argument `instance` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
The name of the Redis region of the instance. Overrides the default redis/region
property value for this command invocation.
To set the `region` attribute:

- provide the argument `instance` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `redis/region`.**

**FLAGS**

: **--alternative-zone**:
A secondary zone for the Redis instance. Only applicable to the standard tier.
This protects the instance against zonal failures by provisioning it across two
zones. If provided, alternative zone must be a different zone from the one
provided through `--zone`.

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--connect-mode**:
Network connection mode used by instances. `CONNECT_MODE`
must be one of: `connect-mode-unspecified`,
`direct-peering`, `private-service-access`.

**--customer-managed-key**:
The KMS key reference that you want to use to encrypt the data at rest for this
Redis instance. If this is provided, CMEK is enabled.

**--display-name**:
A human-readable name for the instance.

**--enable-auth**:
Enables Redis AUTH for the instance. If omitted AUTH is disabled.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--maintenance-window-day**:
Day of week for maintenance window, in UTC time zone. MAINTENANCE_WINDOW_DAY
must be one of: SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY.
`MAINTENANCE_WINDOW_DAY` must be one of:
`day-of-week-unspecified`, `friday`, `monday`,
`saturday`, `sunday`, `thursday`,
`tuesday`, `wednesday`.

**--maintenance-window-hour**:
Hour of day (0 to 23) for maintenance window, in UTC time zone.

**--network**:
The name of the Google Compute Engine network to which the instance will be
connected. If left unspecified, the default network will be used.

**--persistence-mode**:
Operation mode for automated persistence.
`PERSISTENCE_MODE` must be one of:

**`disabled`**:
RDB mode is disabled

**`rdb`**:
Automatic RDB persistence

**--rdb-snapshot-period**:
Attempted period between RDB snapshots.
`RDB_SNAPSHOT_PERIOD` must be one of:

**`12h`**:
12 hours

**`1h`**:
1 hour

**`24h`**:
24 hours

**`6h`**:
6 hours

**--rdb-snapshot-start-time**:
Date and time of the first snapshot in the ISO 1801 format, and alignment time
for future snapshots. For example, 2022-11-02T03:00:00Z.

**--read-replicas-mode**:
Read replicas mode used by the instance. Only works against standard tier
instances with 5GB and above provisioned capacity.
`READ_REPLICAS_MODE` must be one of:

**`read-replicas-disabled`**:
Read replica is disabled for the instance. Read endpoint will not be provided
and the instance cannot scale up or down the number of replicas.

**`read-replicas-enabled`**:
Read replica is enabled for the instance. Read endpoint will be provided and the
instance can scale up and down the number of replicas.

**--redis-config**:
A list of Redis config KEY=VALUE pairs to set on the instance according to [http://redis.io/topics/config](http://redis.io/topics/config).
Currently, the only supported parameters are:
Redis version 3.2 and newer: maxmemory-policy, notify-keyspace-events, timeout,
databases.
Redis version 4.0 and newer: activedefrag, lfu-decay-time, lfu-log-factor,
maxmemory-gb.
Redis version 5.0 and newer: stream-node-max-bytes, stream-node-max-entries.

**--redis-version**:
The version of Redis software. `VERSION` must be one of:

**`redis_3_2`**:
Redis 3.2 compatibility

**`redis_4_0`**:
Redis 4.0 compatibility

**`redis_5_0`**:
Redis 5.0 compatibility

**`redis_6_x`**:
Redis 6.x compatibility

**`redis_7_0`**:
Redis 7.0 compatibility

**`redis_7_2`**:
Redis 7.2 compatibility

**--replica-count**:
The replica count of the instance.

**--reserved-ip-range**:
For DIRECT_PEERING mode, the CIDR range of internal addresses that are reserved
for this instance. Range must be unique and non-overlapping with existing
subnets in an authorized network. For PRIVATE_SERVICE_ACCESS mode, the name of
an IP address range allocated for the private service access connection. If not
provided, the service will choose an unused /29 block, for example, 10.0.0.0/29
or 192.168.0.0/29. If READ_REPLICAS_ENABLED is used for the --read-replicas-mode
flag, then the block size required for this flag is /28.

**--size**:
The memory size of the instance in GiB. If not provided, size of 1 GiB will be
used.

**--tier**:
The service tier of the instance. `TIER` must be one of:

**`basic`**:
Basic Redis instance with no replication

**`standard`**:
Standard high-availability Redis instance with replication

**--transit-encryption-mode**:
Transit encryption mode used by the instance.
`TRANSIT_ENCRYPTION_MODE` must be one of:

**`disabled`**:
Transit encryption is disabled for the instance.

**`server-authentication`**:
Client to Server traffic encryption enabled with server authentication.

**--zone**:
The zone of the Redis instance. If not provided the service will pick a random
zone in the region. For the standard tier, instances will be created across two
zones for protection against zonal failures. So if --alternative-zone is also
provided, it must be different from --zone.

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
gcloud alpha redis instances create
```

```
gcloud beta redis instances create
```