# gcloud oracle-database cloud-vm-clusters create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create)*

**NAME**

: **gcloud oracle-database cloud-vm-clusters create - create a new CloudVmCluster**

**SYNOPSIS**

: **`gcloud oracle-database cloud-vm-clusters create` `[CLOUD_VM_CLUSTER](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#CLOUD_VM_CLUSTER)` `[--exadata-infrastructure](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--exadata-infrastructure)`=`EXADATA_INFRASTRUCTURE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--async)`] [`[--backup-subnet-cidr](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--backup-subnet-cidr)`=`BACKUP_SUBNET_CIDR`] [`[--cidr](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--cidr)`=`CIDR`] [`[--display-name](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--display-name)`=`DISPLAY_NAME`] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--labels)`=[`LABELS`,…]] [`[--location](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--location)`=`LOCATION`] [`[--network](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--network)`=`NETWORK`] [`[--request-id](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--request-id)`=`REQUEST_ID`] [[`[--properties-cpu-core-count](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-cpu-core-count)`=`PROPERTIES_CPU_CORE_COUNT` `[--properties-license-type](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-license-type)`=`PROPERTIES_LICENSE_TYPE` : `[--properties-cluster-name](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-cluster-name)`=`PROPERTIES_CLUSTER_NAME` `[--properties-data-storage-size-tb](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-data-storage-size-tb)`=`PROPERTIES_DATA_STORAGE_SIZE_TB` `[--properties-db-node-storage-size-gb](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-db-node-storage-size-gb)`=`PROPERTIES_DB_NODE_STORAGE_SIZE_GB` `[--properties-db-server-ocids](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-db-server-ocids)`=[`PROPERTIES_DB_SERVER_OCIDS`,…] `[--properties-disk-redundancy](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-disk-redundancy)`=`PROPERTIES_DISK_REDUNDANCY` `[--properties-gi-version](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-gi-version)`=`PROPERTIES_GI_VERSION` `[--properties-hostname-prefix](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-hostname-prefix)`=`PROPERTIES_HOSTNAME_PREFIX` `[--properties-local-backup-enabled](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-local-backup-enabled)` `[--properties-memory-size-gb](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-memory-size-gb)`=`PROPERTIES_MEMORY_SIZE_GB` `[--properties-node-count](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-node-count)`=`PROPERTIES_NODE_COUNT` `[--properties-ocpu-count](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-ocpu-count)`=`PROPERTIES_OCPU_COUNT` `[--properties-sparse-diskgroup-enabled](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-sparse-diskgroup-enabled)` `[--properties-ssh-public-keys](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-ssh-public-keys)`=[`PROPERTIES_SSH_PUBLIC_KEYS`,…] `[--properties-system-version](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--properties-system-version)`=`PROPERTIES_SYSTEM_VERSION` `[--diagnostics-data-collection-options-events-enabled](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--diagnostics-data-collection-options-events-enabled)` `[--diagnostics-data-collection-options-health-monitoring-enabled](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--diagnostics-data-collection-options-health-monitoring-enabled)` `[--diagnostics-data-collection-options-incident-logs-enabled](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--diagnostics-data-collection-options-incident-logs-enabled)` `[--time-zone-id](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--time-zone-id)`=`TIME_ZONE_ID` `[--time-zone-version](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#--time-zone-version)`=`TIME_ZONE_VERSION`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/oracle-database/cloud-vm-clusters/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a new CloudVmCluster.

**EXAMPLES**

: Choose an available gi-versions in your location by running `gcloud
oracle-database db-system-shapes list --location=us-east4`. To create
CloudVmCluster instance with id `my-instance` in the location
`us-east4` with display-name `my instance`, cidr
`10.1.0.0/24`, network
`projects/my-project/locations/global/networks/default`,
backup-subnet-cidr `10.2.0.0/24`, license-type
`LICENSE_INCLUDED`, ssh-public-keys
`VtTxzlPJtIivthmLOmWdRDFy5l27pKUTwLp02`, hostname-prefix
`hostname1`, cpu-core-count `4` and choosen gi-version
`xx.0.0.0`, run:

```
gcloud oracle-database cloud-vm-clusters create my-instance --location=us-east4 --display-name="my instance" --cidr=10.1.0.0/24 --network=projects/my-project/locations/global/networks/default --backup-subnet-cidr=10.2.0.0/24 --properties-license-type=LICENSE_INCLUDED --properties-ssh-public-keys="VtTxzlPJtIivthmLOmWdRDFy5l27pKUTwLp02" --properties-gi-version=xx.0.0.0 --properties-hostname-prefix=hostname1 --properties-cpu-core-count=4
```

**POSITIONAL ARGUMENTS**

: **CloudVmCluster resource - Identifier. The name of the VM Cluster resource with
the format:
projects/{project}/locations/{region}/cloudVmClusters/{cloud_vm_cluster} This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `cloud_vm_cluster` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `cloud_vm_cluster` on the command line with a
fully specified name;
- provide the argument `--location` on the command line.

This must be specified.

**`CLOUD_VM_CLUSTER`**:
ID of the cloudVmCluster or fully qualified identifier for the cloudVmCluster.
To set the `cloud_vm_cluster` attribute:

- provide the argument `cloud_vm_cluster` on the command line.**

**REQUIRED FLAGS**

: **CloudExadataInfrastructure resource - The name of the Exadata Infrastructure
resource on which VM cluster resource is created, in the following format:
projects/{project}/locations/{region}/cloudExadataInfrastuctures/{cloud_extradata_infrastructure}
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--exadata-infrastructure` on the command line
with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--exadata-infrastructure` on the command line
with a fully specified name;
- provide the argument `--location` on the command line.

This must be specified.

**--exadata-infrastructure**:
ID of the cloudExadataInfrastructure or fully qualified identifier for the
cloudExadataInfrastructure.
To set the `cloud-exadata-infrastructure` attribute:

- provide the argument `--exadata-infrastructure` on the command line.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--backup-subnet-cidr**:
CIDR range of the backup subnet.

**--cidr**:
Network settings. CIDR to use for cluster IP allocation.

**--display-name**:
User friendly name for this resource.

**--labels**:
Labels or tags associated with the VM Cluster.

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
For resources [cloudVmCluster, cloudExadataInfrastructure], provides fallback
value for resource location attribute. When the resource's full URI path is not
provided, location will fallback to this flag value.

**Network resource - The name of the VPC network. Format:
projects/{project}/global/networks/{network} This represents a Cloud resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `--network` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**--network**:
ID of the network or fully qualified identifier for the network.
To set the `network` attribute:

- provide the argument `--network` on the command line.**

**--request-id**:
An optional ID to identify the request. This value is used to identify duplicate
requests. If you make a request with the same request ID and the original
request is still in progress or completed, the server ignores the second
request. This prevents clients from accidentally creating duplicate commitments.
The request ID must be a valid UUID with the exception that zero UUID is not
supported (00000000-0000-0000-0000-000000000000).

**--properties-cpu-core-count**

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

: This command uses the `oracledatabase/v1` API. The full documentation
for this API can be found at: [https://cloud.google.com/oracle/database/docs](https://cloud.google.com/oracle/database/docs)