# gcloud alloydb instances update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update)*

**NAME**

: **gcloud alloydb instances update - updates an AlloyDB instance within a given cluster**

**SYNOPSIS**

: **`gcloud alloydb instances update` `[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#INSTANCE)` `[--cluster](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--cluster)`=`CLUSTER` `[--region](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--region)`=`REGION` [`[--activation-policy](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--activation-policy)`=`ACTIVATION_POLICY`] [`[--allowed-psc-projects](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--allowed-psc-projects)`=[`ALLOWED_PSC_PROJECTS`,…]] [`[--assign-inbound-public-ip](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--assign-inbound-public-ip)`=`ASSIGN_INBOUND_PUBLIC_IP`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--async)`] [`[--authorized-external-networks](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--authorized-external-networks)`=[`AUTHORIZED_NETWORK`,…]] [`[--availability-type](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--availability-type)`=`AVAILABILITY_TYPE`] [`[--clear-psc-network-attachment-uri](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--clear-psc-network-attachment-uri)`] [`[--cpu-count](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--cpu-count)`=`CPU_COUNT`] [`[--database-flags](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--database-flags)`=`FLAG`=`VALUE`,[`[FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#FLAG)`=`VALUE`,…]] [`[--insights-config-query-plans-per-minute](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--insights-config-query-plans-per-minute)`=`INSIGHTS_CONFIG_QUERY_PLANS_PER_MINUTE`] [`[--insights-config-query-string-length](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--insights-config-query-string-length)`=`INSIGHTS_CONFIG_QUERY_STRING_LENGTH`] [`[--[no-]insights-config-record-application-tags](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--[no-]insights-config-record-application-tags)`] [`[--[no-]insights-config-record-client-address](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--[no-]insights-config-record-client-address)`] [`[--machine-type](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--machine-type)`=`MACHINE_TYPE`] [`[--[no-]outbound-public-ip](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--[no-]outbound-public-ip)`] [`[--psc-network-attachment-uri](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--psc-network-attachment-uri)`=`PSC_NETWORK_ATTACHMENT_URI`] [`[--read-pool-node-count](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--read-pool-node-count)`=`READ_POOL_NODE_COUNT`] [`[--[no-]require-connectors](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--[no-]require-connectors)`] [`[--ssl-mode](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--ssl-mode)`=`SSL_MODE`] [`[--clear-psc-auto-connections](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--clear-psc-auto-connections)`     | `[--psc-auto-connections](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#--psc-auto-connections)`=[`network`=`NETWORK`],[`project`=`PROJECT`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/alloydb/instances/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates an AlloyDB instance within a given cluster.

**EXAMPLES**

: To update the number of nodes in the read pool, run:

```
gcloud alloydb instances update my-read-instance --cluster=my-cluster --region=us-central1 --read-pool-node-count=3
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
Activation Policy for the instance. Required to START or STOP an instance.
ALWAYS - The instance is up and running. NEVER - The instance is stopped.
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

**--clear-psc-auto-connections**