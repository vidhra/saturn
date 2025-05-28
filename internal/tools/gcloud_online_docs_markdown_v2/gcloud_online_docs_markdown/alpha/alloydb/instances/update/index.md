# gcloud alpha alloydb instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update)*

**NAME**

: **gcloud alpha alloydb instances update - updates an AlloyDB instance within a given cluster**

**SYNOPSIS**

: **`gcloud alpha alloydb instances update` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#INSTANCE)` `[--cluster](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--region)`=`REGION` [`[--activation-policy](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--activation-policy)`=`ACTIVATION_POLICY`] [`[--allowed-psc-projects](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--allowed-psc-projects)`=[`ALLOWED_PSC_PROJECTS`,…]] [`[--assign-inbound-public-ip](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--assign-inbound-public-ip)`=`ASSIGN_INBOUND_PUBLIC_IP`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--async)`] [`[--authorized-external-networks](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--authorized-external-networks)`=[`AUTHORIZED_NETWORK`,…]] [`[--availability-type](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--availability-type)`=`AVAILABILITY_TYPE`] [`[--clear-psc-network-attachment-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--clear-psc-network-attachment-uri)`] [`[--connection-pooling-ignore-startup-parameters](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--connection-pooling-ignore-startup-parameters)`=[`STARTUP_PARAMETERS`,…]] [`[--connection-pooling-max-client-connections](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--connection-pooling-max-client-connections)`=`CONNECTION_POOLING_MAX_CLIENT_CONNECTIONS`] [`[--connection-pooling-max-pool-size](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--connection-pooling-max-pool-size)`=`CONNECTION_POOLING_MAX_POOL_SIZE`] [`[--connection-pooling-min-pool-size](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--connection-pooling-min-pool-size)`=`CONNECTION_POOLING_MIN_POOL_SIZE`] [`[--connection-pooling-pool-mode](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--connection-pooling-pool-mode)`=`CONNECTION_POOLING_POOL_MODE`] [`[--connection-pooling-query-wait-timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--connection-pooling-query-wait-timeout)`=`CONNECTION_POOLING_QUERY_WAIT_TIMEOUT`] [`[--connection-pooling-server-idle-timeout](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--connection-pooling-server-idle-timeout)`=`CONNECTION_POOLING_SERVER_IDLE_TIMEOUT`] [`[--connection-pooling-stats-users](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--connection-pooling-stats-users)`=[`STATS_USERS`,…]] [`[--cpu-count](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--cpu-count)`=`CPU_COUNT`] [`[--database-flags](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--database-flags)`=`FLAG`=`VALUE`,[`[FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#FLAG)`=`VALUE`,…]] [`[--[no-]enable-connection-pooling](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--[no-]enable-connection-pooling)`] [`[--insights-config-query-plans-per-minute](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--insights-config-query-plans-per-minute)`=`INSIGHTS_CONFIG_QUERY_PLANS_PER_MINUTE`] [`[--insights-config-query-string-length](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--insights-config-query-string-length)`=`INSIGHTS_CONFIG_QUERY_STRING_LENGTH`] [`[--[no-]insights-config-record-application-tags](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--[no-]insights-config-record-application-tags)`] [`[--[no-]insights-config-record-client-address](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--[no-]insights-config-record-client-address)`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--machine-type)`=`MACHINE_TYPE`] [`[--[no-]observability-config-enabled](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--[no-]observability-config-enabled)`] [`[--observability-config-max-query-string-length](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--observability-config-max-query-string-length)`=`OBSERVABILITY_CONFIG_MAX_QUERY_STRING_LENGTH`] [`[--[no-]observability-config-preserve-comments](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--[no-]observability-config-preserve-comments)`] [`[--observability-config-query-plans-per-minute](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--observability-config-query-plans-per-minute)`=`OBSERVABILITY_CONFIG_QUERY_PLANS_PER_MINUTE`] [`[--[no-]observability-config-record-application-tags](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--[no-]observability-config-record-application-tags)`] [`[--[no-]observability-config-track-active-queries](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--[no-]observability-config-track-active-queries)`] [`[--observability-config-track-wait-events](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--observability-config-track-wait-events)`] [`[--[no-]outbound-public-ip](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--[no-]outbound-public-ip)`] [`[--psc-network-attachment-uri](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--psc-network-attachment-uri)`=`PSC_NETWORK_ATTACHMENT_URI`] [`[--read-pool-node-count](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--read-pool-node-count)`=`READ_POOL_NODE_COUNT`] [`[--[no-]require-connectors](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--[no-]require-connectors)`] [`[--ssl-mode](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--ssl-mode)`=`SSL_MODE`] [`[--update-mode](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--update-mode)`=`UPDATE_MODE`] [`[--clear-psc-auto-connections](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--clear-psc-auto-connections)`     | `[--psc-auto-connections](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#--psc-auto-connections)`=[`network`=`NETWORK`],[`project`=`PROJECT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alpha/alloydb/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: `(ALPHA)` Updates an AlloyDB instance within a given cluster.

**EXAMPLES**

: To update the number of nodes in the read pool, run:

```
gcloud alpha alloydb instances update my-read-instance --cluster=my-cluster --region=us-central1 --read-pool-node-count=3
```

**POSITIONAL ARGUMENTS**

: **`INSTANCE`**:
AlloyDB instance ID

**REQUIRED FLAGS**

: **--cluster**:
AlloyDB cluster ID

**--region**:
Regional location (e.g. `asia-east1`, `us-east1`). See the
full list of regions at [https://cloud.google.com/sql/docs/instance-locations](https://cloud.google.com/sql/docs/instance-locations).

**OPTIONAL FLAGS**

: **--activation-policy**:
Activation Policy for the instance.Required to START or STOP an instance.ALWAYS
- The instance is up and running.NEVER - The instance is stopped.
`ACTIVATION_POLICY` must be one of: `ALWAYS`,
`NEVER`.

**--allowed-psc-projects**:
Comma-separated list of allowed consumer projects to create endpoints for
Private Service Connect (PSC) connectivity for the instance. Only instances in
PSC-enabled clusters are allowed to set this field.(e.g.,
`--allowed-psc-projects=project1,12345678,project2)`

**--assign-inbound-public-ip**:
Specify to enable or disable public IP on an instance. ASSIGN_INBOUND_PUBLIC_IP
must be one of:

- `NO_PUBLIC_IP`

- This disables public IP on the instance. Updating an instance to disable public
IP will clear the list of authorized networks.
- `ASSIGN_IPV4`

- Assign an inbound public IPv4 address for the instance. Public IP is enabled.

**--async**:
Return immediately, without waiting for the operation in progress to complete.
The default is `True`. Enabled by default, use
`--no-async` to disable.

**--authorized-external-networks**:
Comma-separated list of authorized external networks to set on the instance.
Authorized networks should use CIDR notation (e.g. 1.2.3.4/30). This flag is
only allowed to be set for instances with public IP enabled.

**--availability-type**:
Specifies level of availability. `AVAILABILITY_TYPE` must
be one of:

**`REGIONAL`**:
Provide high availability instances. Recommended for production instances;
instances automatically fail over to another zone within your selected region.

**`ZONAL`**:
Provide zonal availability instances. Not recommended for production instances;
instance does not automatically fail over to another zone.

**--clear-psc-network-attachment-uri**:
Disable outbound connectivity from an AlloyDB instance which uses Private
Service Connect (PSC).

**--connection-pooling-ignore-startup-parameters**:
Comma-separated list of startup parameters that should be ignored by the
connection pool.

**--connection-pooling-max-client-connections**:
The max client connections for managed connection pooling.

**--connection-pooling-max-pool-size**:
The max pool size for managed connection pooling.

**--connection-pooling-min-pool-size**:
The min pool size for managed connection pooling.

**--connection-pooling-pool-mode**:
The pool mode for managed connection pooling.
`CONNECTION_POOLING_POOL_MODE` must be one of:

**`SESSION`**:
Session mode for managed connection pooling.

**`TRANSACTION`**:
Transaction mode for managed connection pooling.

**--connection-pooling-query-wait-timeout**:
The query wait timeout for managed connection pooling.

**--connection-pooling-server-idle-timeout**:
The server idle timeout for managed connection pooling.

**--connection-pooling-stats-users**:
Comma-separated list of database users to access connection pooling stats.

**--cpu-count**:
Whole number value indicating how many vCPUs the machine should contain. If the
instance does not have a machine-type, the vCPU count will be used to determine
the machine type where each vCPU corresponds to an N2 high-mem machine:
(https://cloud.google.com/compute/docs/general-purpose-machines#n2_machine_types).
where CPU_COUNT can be one of: 2, 4, 8, 16, 32, 64, 96, 128. If the instance has
a machine-type, cpu-count must have the same value as the vCPU count in the
machine-type. Eg: if machine-type is c4a-highmem-4-lssd, cpu-count must be 4.
`CPU_COUNT` must be one of: `1`,
`2`, `4`, `8`, `16`,
`32`, `48`, `64`, `72`,
`96`, `128`.

**--database-flags**:
Comma-separated list of database flags to set on the instance. Use an equals
sign to separate flag name and value. Flags without values, like
skip_grant_tables, can be written out without a value after, e.g.,
skip_grant_tables=`. Use on/off for booleans. View the Instance
Resource API for allowed flags. (e.g.,`--database-flags
max_allowed_packet=55555,skip_grant_tables=,log_output=1`)`

**--[no-]enable-connection-pooling**:
Enable connection pooling for the instance. Use
`--enable-connection-pooling` to enable and
`--no-enable-connection-pooling` to disable.

**--insights-config-query-plans-per-minute**:
Number of query plans to sample every minute. Default value is 5. Allowed range:
0 to 20.

**--insights-config-query-string-length**:
Query string length in bytes to be stored by the query insights feature. Default
length is 1024 bytes. Allowed range: 256 to 4500 bytes.

**--[no-]insights-config-record-application-tags**:
Allow application tags to be recorded by the query insights feature.
Use `--insights-config-record-application-tags` to enable and
`--no-insights-config-record-application-tags` to disable.

**--[no-]insights-config-record-client-address**:
Allow the client address to be recorded by the query insights feature.
Use `--insights-config-record-client-address` to enable and
`--no-insights-config-record-client-address` to disable.

**--machine-type**:
Specifies machine type for the instance. `MACHINE_TYPE`
must be one of: `n2-highmem-2`, `n2-highmem-4`,
`n2-highmem-8`, `n2-highmem-16`,
`n2-highmem-32`, `n2-highmem-64`,
`n2-highmem-96`, `n2-highmem-128`,
`c4a-highmem-1`, `c4a-highmem-4-lssd`,
`c4a-highmem-8-lssd`, `c4a-highmem-16-lssd`,
`c4a-highmem-32-lssd`, `c4a-highmem-48-lssd`,
`c4a-highmem-64-lssd`, `c4a-highmem-72-lssd`.

**--[no-]observability-config-enabled**:
Enable enhanced query insights feature. Use
`--observability-config-enabled` to enable and
`--no-observability-config-enabled` to disable.

**--observability-config-max-query-string-length**:
Query string length in bytes to be stored by the enhanced query insights
feature. Default length is 10k bytes.

**--[no-]observability-config-preserve-comments**:
Allow preservation of comments in query string recorded by the enhanced query
insights feature.
Use `--observability-config-preserve-comments` to enable and
`--no-observability-config-preserve-comments` to disable.

**--observability-config-query-plans-per-minute**:
Number of query plans to sample every minute. Default value is 200. Allowed
range: 0 to 200.

**--[no-]observability-config-record-application-tags**:
Allow application tags to be recorded by the enhanced query insights feature.
Use `--observability-config-record-application-tags` to enable and
`--no-observability-config-record-application-tags` to disable.

**--[no-]observability-config-track-active-queries**:
Track actively running queries. Use
`--observability-config-track-active-queries` to enable and
`--no-observability-config-track-active-queries` to disable.

**--observability-config-track-wait-events**:
Track wait events during query execution.

**--[no-]outbound-public-ip**:
Add outbound Public IP connectivity to an AlloyDB instance. Use
`--outbound-public-ip` to enable and
`--no-outbound-public-ip` to disable.

**--psc-network-attachment-uri**:
Full URI of the network attachment that is configured to support outbound
connectivity from an AlloyDB instance which uses Private Service Connect (PSC).
For example, this would be of the
form:psc-network-attachment-uri=projects/test-project/regions/us-central1/networkAttachments/my-na``

**--read-pool-node-count**:
Read capacity, i.e. number of nodes in a read pool instance.

**--[no-]require-connectors**:
Enable or disable enforcing connectors only (ex: AuthProxy) connections to the
database. Use `--require-connectors` to enable and
`--no-require-connectors` to disable.

**--ssl-mode**:
Specify the SSL mode to use when the instance connects to the database.
`SSL_MODE` must be one of:

**`ALLOW_UNENCRYPTED_AND_ENCRYPTED`**:
SSL connections are optional. CA verification is not enforced.

**`ENCRYPTED_ONLY`**:
SSL connections are required. CA verification is not enforced.

**--update-mode**:
Specify the mode for updating the instance. If unspecified, the update would
follow a least disruptive approach. `UPDATE_MODE` must be
(only one value is supported):

**`FORCE_APPLY`**:
Performs a forced update when applicable. This will be fast but may incur a
downtime.

**--clear-psc-auto-connections**