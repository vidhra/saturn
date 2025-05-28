# gcloud compute storage-pools create  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create)*

**NAME**

: **gcloud compute storage-pools create - create a storage pool**

**SYNOPSIS**

: **`gcloud compute storage-pools create` `[STORAGE_POOL](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#STORAGE_POOL)` `[--provisioned-capacity](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#--provisioned-capacity)`=`PROVISIONED_CAPACITY` `[--storage-pool-type](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#--storage-pool-type)`=`STORAGE_POOL_TYPE` [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#--async)`] [`[--capacity-provisioning-type](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#--capacity-provisioning-type)`=`CAPACITY_PROVISIONING_TYPE`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#--description)`=`DESCRIPTION`] [`[--performance-provisioning-type](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#--performance-provisioning-type)`=`PERFORMANCE_PROVISIONING_TYPE`] [`[--provisioned-iops](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#--provisioned-iops)`=`PROVISIONED_IOPS`] [`[--provisioned-throughput](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#--provisioned-throughput)`=`PROVISIONED_THROUGHPUT`] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#--zone)`=`ZONE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/create#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Create a storage pool.

**EXAMPLES**

: To create a new storage pool named `my-storage-pool`, run the
following command:

```
gcloud compute storage-pools create my-storage-pool --storage-pool-type=hyperdisk-throughput --provisioned-capacity=10TB --provisioned-throughput=200
```

**POSITIONAL ARGUMENTS**

: **Storage pool resource - The name of the storage pool you want to create. This
represents a Cloud resource. (NOTE) Some attributes are not given arguments in
this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `storage_pool` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `zone` attribute:

- provide the argument `storage_pool` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.

This must be specified.

**`STORAGE_POOL`**:
ID of the storage pool or fully qualified identifier for the storage pool.
To set the `storage_pool` attribute:

- provide the argument `storage_pool` on the command line.**

**REQUIRED FLAGS**

: **--provisioned-capacity**:
Provisioned capacity of the storage pool.

**Storage pool type resource - Type of the storage pool. This represents a Cloud
resource. (NOTE) Some attributes are not given arguments in this group but can
be set in other ways.
To set the `project` attribute:

- provide the argument `--storage-pool-type` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `zone` attribute:

- provide the argument `--storage-pool-type` on the command line with a
fully specified name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.

This must be specified.

**--storage-pool-type**:
ID of the storage pool type or fully qualified identifier for the storage pool
type.
To set the `storage-pool-type` attribute:

- provide the argument `--storage-pool-type` on the command line.**

**OPTIONAL FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

**--capacity-provisioning-type**:
Capacity provisioning type. `CAPACITY_PROVISIONING_TYPE`
must be one of: `advanced`, `standard`.

**--description**:
Description of the storage pool.

**--performance-provisioning-type**:
Performance provisioning type.
`PERFORMANCE_PROVISIONING_TYPE` must be one of:
`advanced`, `standard`.

**--provisioned-iops**:
IOPS with which to provision the pool.

**--provisioned-throughput**:
Throughput in MB/s with which to provision the pool.

**--zone**:
For resources [storage pool, storage pool type], provides fallback value for
resource zone attribute. When the resource's full URI path is not provided, zone
will fallback to this flag value.

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

: This command uses the `compute/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/compute/](https://cloud.google.com/compute/)

**NOTES**

: These variants are also available:

```
gcloud alpha compute storage-pools create
```

```
gcloud beta compute storage-pools create
```