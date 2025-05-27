# gcloud dataproc workflow-templates set-managed-cluster  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster)*

**NAME**

: **gcloud dataproc workflow-templates set-managed-cluster - set a managed cluster for the workflow template**

**SYNOPSIS**

: **`gcloud dataproc workflow-templates set-managed-cluster` (`[TEMPLATE](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#TEMPLATE)` : `[--region](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--region)`=`REGION`) [`[--autoscaling-policy](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--autoscaling-policy)`=`AUTOSCALING_POLICY`] [`[--bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--bucket)`=`BUCKET`] [`[--cluster-name](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--cluster-name)`=`CLUSTER_NAME`] [`[--cluster-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--cluster-type)`=`TYPE`] [`[--confidential-compute](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--confidential-compute)`] [`[--dataproc-metastore](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--dataproc-metastore)`=`DATAPROC_METASTORE`] [`[--enable-component-gateway](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--enable-component-gateway)`] [`[--initialization-action-timeout](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--initialization-action-timeout)`=`TIMEOUT`; default="10m"] [`[--initialization-actions](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--initialization-actions)`=`CLOUD_STORAGE_URI`,[…]] [`[--labels](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--labels)`=[`KEY`=`VALUE`,…]] [`[--master-accelerator](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--master-accelerator)`=[`type`=`TYPE`,[`count`=`COUNT`],…]] [`[--master-boot-disk-provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--master-boot-disk-provisioned-iops)`=`MASTER_BOOT_DISK_PROVISIONED_IOPS`] [`[--master-boot-disk-provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--master-boot-disk-provisioned-throughput)`=`MASTER_BOOT_DISK_PROVISIONED_THROUGHPUT`] [`[--master-boot-disk-size](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--master-boot-disk-size)`=`MASTER_BOOT_DISK_SIZE`] [`[--master-boot-disk-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--master-boot-disk-type)`=`MASTER_BOOT_DISK_TYPE`] [`[--master-local-ssd-interface](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--master-local-ssd-interface)`=`MASTER_LOCAL_SSD_INTERFACE`] [`[--master-machine-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--master-machine-type)`=`MASTER_MACHINE_TYPE`] [`[--master-min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--master-min-cpu-platform)`=`PLATFORM`] [`[--min-secondary-worker-fraction](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--min-secondary-worker-fraction)`=`MIN_SECONDARY_WORKER_FRACTION`] [`[--node-group](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--node-group)`=`NODE_GROUP`] [`[--num-master-local-ssds](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--num-master-local-ssds)`=`NUM_MASTER_LOCAL_SSDS`] [`[--num-masters](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--num-masters)`=`NUM_MASTERS`] [`[--num-secondary-worker-local-ssds](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--num-secondary-worker-local-ssds)`=`NUM_SECONDARY_WORKER_LOCAL_SSDS`] [`[--num-worker-local-ssds](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--num-worker-local-ssds)`=`NUM_WORKER_LOCAL_SSDS`] [`[--optional-components](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--optional-components)`=[`COMPONENT`,…]] [`[--private-ipv6-google-access-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--private-ipv6-google-access-type)`=`PRIVATE_IPV6_GOOGLE_ACCESS_TYPE`] [`[--properties](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--properties)`=[`PREFIX`:`[PROPERTY](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#PROPERTY)`=`VALUE`,…]] [`[--secondary-worker-accelerator](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--secondary-worker-accelerator)`=[`type`=`TYPE`,[`count`=`COUNT`],…]] [`[--secondary-worker-boot-disk-size](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--secondary-worker-boot-disk-size)`=`SECONDARY_WORKER_BOOT_DISK_SIZE`] [`[--secondary-worker-boot-disk-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--secondary-worker-boot-disk-type)`=`SECONDARY_WORKER_BOOT_DISK_TYPE`] [`[--secondary-worker-local-ssd-interface](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--secondary-worker-local-ssd-interface)`=`SECONDARY_WORKER_LOCAL_SSD_INTERFACE`] [`[--secondary-worker-machine-types](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--secondary-worker-machine-types)`=`type`=`MACHINE_TYPE`[,`type`=`MACHINE_TYPE`…][,`rank`=`RANK`]] [`[--secondary-worker-standard-capacity-base](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--secondary-worker-standard-capacity-base)`=`SECONDARY_WORKER_STANDARD_CAPACITY_BASE`] [`[--secondary-worker-standard-capacity-percent-above-base](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--secondary-worker-standard-capacity-percent-above-base)`=`SECONDARY_WORKER_STANDARD_CAPACITY_PERCENT_ABOVE_BASE`] [`[--shielded-integrity-monitoring](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--shielded-integrity-monitoring)`] [`[--shielded-secure-boot](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--shielded-secure-boot)`] [`[--shielded-vtpm](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--shielded-vtpm)`] [`[--temp-bucket](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--temp-bucket)`=`TEMP_BUCKET`] [`[--worker-accelerator](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--worker-accelerator)`=[`type`=`TYPE`,[`count`=`COUNT`],…]] [`[--worker-boot-disk-provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--worker-boot-disk-provisioned-iops)`=`WORKER_BOOT_DISK_PROVISIONED_IOPS`] [`[--worker-boot-disk-provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--worker-boot-disk-provisioned-throughput)`=`WORKER_BOOT_DISK_PROVISIONED_THROUGHPUT`] [`[--worker-boot-disk-size](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--worker-boot-disk-size)`=`WORKER_BOOT_DISK_SIZE`] [`[--worker-boot-disk-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--worker-boot-disk-type)`=`WORKER_BOOT_DISK_TYPE`] [`[--worker-local-ssd-interface](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--worker-local-ssd-interface)`=`WORKER_LOCAL_SSD_INTERFACE`] [`[--worker-min-cpu-platform](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--worker-min-cpu-platform)`=`PLATFORM`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--zone)`=`ZONE`] [`[--identity-config-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--identity-config-file)`=`IDENTITY_CONFIG_FILE`     | `[--secure-multi-tenancy-user-mapping](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--secure-multi-tenancy-user-mapping)`=`SECURE_MULTI_TENANCY_USER_MAPPING`] [`[--image](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--image)`=`IMAGE`     | `[--image-version](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--image-version)`=`VERSION`] [`[--kerberos-config-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--kerberos-config-file)`=`KERBEROS_CONFIG_FILE`     | `[--enable-kerberos](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--enable-kerberos)` `[--kerberos-root-principal-password-uri](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--kerberos-root-principal-password-uri)`=`KERBEROS_ROOT_PRINCIPAL_PASSWORD_URI` [`[--kerberos-kms-key](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--kerberos-kms-key)`=`KERBEROS_KMS_KEY` : `[--kerberos-kms-key-keyring](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--kerberos-kms-key-keyring)`=`KERBEROS_KMS_KEY_KEYRING` `[--kerberos-kms-key-location](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--kerberos-kms-key-location)`=`KERBEROS_KMS_KEY_LOCATION` `[--kerberos-kms-key-project](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--kerberos-kms-key-project)`=`KERBEROS_KMS_KEY_PROJECT`]] [`[--kms-key](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--kms-key)`=`KMS_KEY` : `[--kms-keyring](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--kms-keyring)`=`KMS_KEYRING` `[--kms-location](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--kms-location)`=`KMS_LOCATION` `[--kms-project](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--kms-project)`=`KMS_PROJECT`] [`[--metadata](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--metadata)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#KEY)`=`VALUE`,…] `[--resource-manager-tags](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--resource-manager-tags)`=`KEY`=`VALUE`,[`[KEY](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#KEY)`=`VALUE`,…] `[--scopes](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--scopes)`=`SCOPE`,[`[SCOPE](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#SCOPE)`,…] `[--service-account](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--service-account)`=`SERVICE_ACCOUNT` `[--tags](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--tags)`=`TAG`,[`[TAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#TAG)`,…] `[--network](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--network)`=`NETWORK`     | `[--subnet](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--subnet)`=`SUBNET` `[--reservation](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--reservation)`=`RESERVATION` `[--reservation-affinity](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--reservation-affinity)`=`RESERVATION_AFFINITY`; default="any"] [[`[--metric-sources](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--metric-sources)`=[`METRIC_SOURCE`,…] : `[--metric-overrides](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--metric-overrides)`=[`METRIC_SOURCE`:`[INSTANCE](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#INSTANCE)`:`[GROUP](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#GROUP)`:`[METRIC](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#METRIC)`,…] | `[--metric-overrides-file](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--metric-overrides-file)`=`METRIC_OVERRIDES_FILE`]] [`[--no-address](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--address)`     | `[--public-ip-address](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--public-ip-address)`] [`[--single-node](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--single-node)`     | `[--min-num-workers](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--min-num-workers)`=`MIN_NUM_WORKERS` `[--num-secondary-workers](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--num-secondary-workers)`=`NUM_SECONDARY_WORKERS` `[--num-workers](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--num-workers)`=`NUM_WORKERS` `[--secondary-worker-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--secondary-worker-type)`=`TYPE`; default="preemptible"] [`[--worker-machine-type](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--worker-machine-type)`=`WORKER_MACHINE_TYPE`     | `[--worker-machine-types](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#--worker-machine-types)`=`type`=`MACHINE_TYPE`[,`type`=`MACHINE_TYPE`…][,`rank`=`RANK`]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/dataproc/workflow-templates/set-managed-cluster#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Set a managed cluster for the workflow template.

**EXAMPLES**

: To update managed cluster in a workflow template, run:

```
gcloud dataproc workflow-templates set-managed-cluster my_template --region=us-central1 --no-address --num-workers=10 --worker-machine-type=custom-6-23040
```

**POSITIONAL ARGUMENTS**

: **Template resource - The name of the workflow template to set managed cluster.
The arguments in this group can be used to specify the attributes of this
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `template` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`TEMPLATE`**:
ID of the template or fully qualified identifier for the template.
To set the `template` attribute:

- provide the argument `template` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--region**:
Dataproc region for the template. Each Dataproc region constitutes an
independent resource namespace constrained to deploying instances into Compute
Engine zones inside the region. Overrides the default
`dataproc/region` property value for this command invocation.
To set the `region` attribute:

- provide the argument `template` on the command line with a fully
specified name;
- provide the argument `--region` on the command line;
- set the property `dataproc/region`.**

**FLAGS**

: **--autoscaling-policy**:
ID of the autoscaling policy or fully qualified identifier for the autoscaling
policy.
To set the `autoscaling_policy` attribute:

- provide the argument `--autoscaling-policy` on the command line.

**--bucket**:
The Google Cloud Storage bucket to use by default to stage job dependencies,
miscellaneous config files, and job driver console output when using this
cluster.

**--cluster-name**:
The name of the managed dataproc cluster. If unspecified, the workflow template
ID will be used.

**--cluster-type**:
The type of cluster. `TYPE` must be one of:
`standard`, `single-node`, `zero-scale`.

**--confidential-compute**:
Enables Confidential VM. See [https://cloud.google.com/compute/confidential-vm/docs](https://cloud.google.com/compute/confidential-vm/docs)
for more information. Note that Confidential VM can only be enabled when the
machine types are N2D
(https://cloud.google.com/compute/docs/machine-types#n2d_machine_types) and the
image is SEV Compatible.

**--dataproc-metastore**:
Specify the name of a Dataproc Metastore service to be used as an external
metastore in the format:
"projects/{project-id}/locations/{region}/services/{service-name}".

**--enable-component-gateway**:
Enable access to the web UIs of selected components on the cluster through the
component gateway.

**--initialization-action-timeout**:
The maximum duration of each initialization action. See $ [gcloud topic datetimes](https://cloud.google.com/sdk/gcloud/reference/topic/datetimes) for
information on duration formats.

**--initialization-actions**:
A list of Google Cloud Storage URIs of executables to run on each node in the
cluster.

**--labels**:
List of label KEY=VALUE pairs to add.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--master-accelerator**:
Attaches accelerators, such as GPUs, to the master instance(s).

**`type`**:
The specific type of accelerator to attach to the instances, such as
`nvidia-tesla-t4` for NVIDIA T4. Use `gcloud compute
accelerator-types list` to display available accelerator types.

**`count`**:
The number of accelerators to attach to each instance. The default value is 1.

**--master-boot-disk-provisioned-iops**:
Indicates the [IOPS](https://cloud.google.com/compute/docs/disks/hyperdisks#iops) to
provision for the disk. This sets the limit for disk I/O operations per second.
This is only supported if the bootdisk type is [hyperdisk-balanced](https://cloud.google.com/compute/docs/disks/hyperdisks).

**--master-boot-disk-provisioned-throughput**:
Indicates the [throughput](https://cloud.google.com/compute/docs/disks/hyperdisks#throughput)
to provision for the disk. This sets the limit for throughput in MiB per second.
This is only supported if the bootdisk type is [hyperdisk-balanced](https://cloud.google.com/compute/docs/disks/hyperdisks).

**--master-boot-disk-size**:
The size of the boot disk. The value must be a whole number followed by a size
unit of ``KB`` for kilobyte,
``MB`` for megabyte,
``GB`` for gigabyte, or
``TB`` for terabyte. For example,
`10GB` will produce a 10 gigabyte disk. The minimum boot disk size is
10 GB. Boot disk size must be a multiple of 1 GB.

**--master-boot-disk-type**:
The type of the boot disk. The value must be `pd-balanced`,
`pd-ssd`, or `pd-standard`.

**--master-local-ssd-interface**:
Interface to use to attach local SSDs to master node(s) in a cluster.

**--master-machine-type**:
The type of machine to use for the master. Defaults to server-specified.

**--master-min-cpu-platform**:
When specified, the VM is scheduled on the host with a specified CPU
architecture or a more recent CPU platform that's available in that zone. To
list available CPU platforms in a zone, run:

```
gcloud compute zones describe ZONE
```

CPU platform selection may not be available in a zone. Zones that support CPU
platform selection provide an `availableCpuPlatforms` field, which
contains the list of available CPU platforms in the zone (see [Availability
of CPU platforms](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform#availablezones) for more information).

**--min-secondary-worker-fraction**:
Minimum fraction of secondary worker nodes required to create the cluster. If it
is not met, cluster creation will fail. Must be a decimal value between 0 and 1.
The number of required secondary workers is calculated by
ceil(min-secondary-worker-fraction * num_secondary_workers). Defaults to 0.0001.

**--node-group**:
The name of the sole-tenant node group to create the cluster on. Can be a short
name ("node-group-name") or in the format
"projects/{project-id}/zones/{zone}/nodeGroups/{node-group-name}".

**--num-master-local-ssds**:
The number of local SSDs to attach to the master in a cluster.

**--num-masters**:
The number of master nodes in the cluster.

| Number of Masters | Cluster Mode |
| --- | --- |
| 1 | Standard |
| 3 | High Availability |

**--num-secondary-worker-local-ssds**:
The number of local SSDs to attach to each preemptible worker in a cluster.

**--num-worker-local-ssds**:
The number of local SSDs to attach to each worker in a cluster.

**--optional-components**:
List of optional components to be installed on cluster machines.
The following page documents the optional components that can be installed: [https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/optional-components](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/optional-components).

**--private-ipv6-google-access-type**:
The private IPv6 Google access type for the cluster.
`PRIVATE_IPV6_GOOGLE_ACCESS_TYPE` must be one of:
`inherit-subnetwork`, `outbound`,
`bidirectional`.

**--properties**:
Specifies configuration properties for installed packages, such as Hadoop and
Spark.
Properties are mapped to configuration files by specifying a prefix, such as
"core:io.serializations". The following are supported prefixes and their
mappings:

| Prefix | File | Purpose of file |
| --- | --- | --- |
| capacity-scheduler | capacity-scheduler.xml | Hadoop YARN Capacity Scheduler configuration |
| core | core-site.xml | Hadoop general configuration |
| distcp | distcp-default.xml | Hadoop Distributed Copy configuration |
| hadoop-env | hadoop-env.sh | Hadoop specific environment variables |
| hdfs | hdfs-site.xml | Hadoop HDFS configuration |
| hive | hive-site.xml | Hive configuration |
| mapred | mapred-site.xml | Hadoop MapReduce configuration |
| mapred-env | mapred-env.sh | Hadoop MapReduce specific environment variables |
| pig | pig.properties | Pig configuration |
| spark | spark-defaults.conf | Spark configuration |
| spark-env | spark-env.sh | Spark specific environment variables |
| yarn | yarn-site.xml | Hadoop YARN configuration |
| yarn-env | yarn-env.sh | Hadoop YARN specific environment variables |

See [https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties](https://cloud.google.com/dataproc/docs/concepts/configuring-clusters/cluster-properties)
for more information.

**--secondary-worker-accelerator**:
Attaches accelerators, such as GPUs, to the secondary-worker instance(s).

**`type`**:
The specific type of accelerator to attach to the instances, such as
`nvidia-tesla-t4` for NVIDIA T4. Use `gcloud compute
accelerator-types list` to display available accelerator types.

**`count`**:
The number of accelerators to attach to each instance. The default value is 1.

**--secondary-worker-boot-disk-size**:
The size of the boot disk. The value must be a whole number followed by a size
unit of ``KB`` for kilobyte,
``MB`` for megabyte,
``GB`` for gigabyte, or
``TB`` for terabyte. For example,
`10GB` will produce a 10 gigabyte disk. The minimum boot disk size is
10 GB. Boot disk size must be a multiple of 1 GB.

**--secondary-worker-boot-disk-type**:
The type of the boot disk. The value must be `pd-balanced`,
`pd-ssd`, or `pd-standard`.

**--secondary-worker-local-ssd-interface**:
Interface to use to attach local SSDs to each secondary worker in a cluster.

**--secondary-worker-machine-types**:
Types of machines with optional rank for secondary workers to use. Defaults to
server-specified.eg.
--secondary-worker-machine-types="type=e2-standard-8,type=t2d-standard-8,rank=0"

**--secondary-worker-standard-capacity-base**:
This flag sets the base number of Standard VMs to use for [secondary
workers](https://cloud.google.com/dataproc/docs/concepts/compute/secondary-vms#preemptible_and_non-preemptible_secondary_workers). Dataproc will create only standard VMs until it reaches this
number, then it will mix Spot and Standard VMs according to
``SECONDARY_WORKER_STANDARD_CAPACITY_PERCENT_ABOVE_BASE``.

**--secondary-worker-standard-capacity-percent-above-base**:
When combining Standard and Spot VMs for [secondary-workers](https://cloud.google.com/dataproc/docs/concepts/compute/secondary-vms#preemptible_and_non-preemptible_secondary_workers)
once the number of Standard VMs specified by
``SECONDARY_WORKER_STANDARD_CAPACITY_BASE`` has
been used, this flag specifies the percentage of the total number of additional
Standard VMs secondary workers will use. Spot VMs will be used for the remaining
percentage.

**--shielded-integrity-monitoring**:
Enables monitoring and attestation of the boot integrity of the cluster's VMs.
vTPM (virtual Trusted Platform Module) must also be enabled. A TPM is a hardware
module that can be used for different security operations, such as remote
attestation, encryption, and sealing of keys.

**--shielded-secure-boot**:
The cluster's VMs will boot with secure boot enabled.

**--shielded-vtpm**:
The cluster's VMs will boot with the TPM (Trusted Platform Module) enabled. A
TPM is a hardware module that can be used for different security operations,
such as remote attestation, encryption, and sealing of keys.

**--temp-bucket**:
The Google Cloud Storage bucket to use by default to store ephemeral cluster and
jobs data, such as Spark and MapReduce history files.

**--worker-accelerator**:
Attaches accelerators, such as GPUs, to the worker instance(s).

**`type`**:
The specific type of accelerator to attach to the instances, such as
`nvidia-tesla-t4` for NVIDIA T4. Use `gcloud compute
accelerator-types list` to display available accelerator types.

**`count`**:
The number of accelerators to attach to each instance. The default value is 1.

**--worker-boot-disk-provisioned-iops**:
Indicates the [IOPS](https://cloud.google.com/compute/docs/disks/hyperdisks#iops) to
provision for the disk. This sets the limit for disk I/O operations per second.
This is only supported if the bootdisk type is [hyperdisk-balanced](https://cloud.google.com/compute/docs/disks/hyperdisks).

**--worker-boot-disk-provisioned-throughput**:
Indicates the [throughput](https://cloud.google.com/compute/docs/disks/hyperdisks#throughput)
to provision for the disk. This sets the limit for throughput in MiB per second.
This is only supported if the bootdisk type is [hyperdisk-balanced](https://cloud.google.com/compute/docs/disks/hyperdisks).

**--worker-boot-disk-size**:
The size of the boot disk. The value must be a whole number followed by a size
unit of ``KB`` for kilobyte,
``MB`` for megabyte,
``GB`` for gigabyte, or
``TB`` for terabyte. For example,
`10GB` will produce a 10 gigabyte disk. The minimum boot disk size is
10 GB. Boot disk size must be a multiple of 1 GB.

**--worker-boot-disk-type**:
The type of the boot disk. The value must be `pd-balanced`,
`pd-ssd`, or `pd-standard`.

**--worker-local-ssd-interface**:
Interface to use to attach local SSDs to each worker in a cluster.

**--worker-min-cpu-platform**:
When specified, the VM is scheduled on the host with a specified CPU
architecture or a more recent CPU platform that's available in that zone. To
list available CPU platforms in a zone, run:

```
gcloud compute zones describe ZONE
```

CPU platform selection may not be available in a zone. Zones that support CPU
platform selection provide an `availableCpuPlatforms` field, which
contains the list of available CPU platforms in the zone (see [Availability
of CPU platforms](https://cloud.google.com/compute/docs/instances/specify-min-cpu-platform#availablezones) for more information).

**--zone**:
The compute zone (e.g. us-central1-a) for the cluster. If empty and --region is
set to a value other than `global`, the server will pick a zone in
the region. Overrides the default `compute/zone` property value for
this command invocation.

**--identity-config-file**

**--image**

**--kerberos-config-file**

**--kms-key**

**--metadata**

**--metric-sources**:
Specifies a list of cluster [Metric
Sources](https://cloud.google.com/dataproc/docs/guides/monitoring#available_oss_metrics) to collect custom metrics. `METRIC_SOURCE`
must be one of: `FLINK`, `HDFS`,
`HIVEMETASTORE`, `HIVESERVER2`,
`MONITORING_AGENT_DEFAULTS`, `SPARK`,
`SPARK_HISTORY_SERVER`, `YARN`.

**--metric-overrides**

**--no-address**

**--single-node**

**--worker-machine-type**

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

**NOTES**

: These variants are also available:

```
gcloud alpha dataproc workflow-templates set-managed-cluster
```

```
gcloud beta dataproc workflow-templates set-managed-cluster
```