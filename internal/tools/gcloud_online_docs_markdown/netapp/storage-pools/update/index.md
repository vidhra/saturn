# gcloud netapp storage-pools update  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update)*

**NAME**

: **gcloud netapp storage-pools update - update a Cloud NetApp Storage Pool**

**SYNOPSIS**

: **`gcloud netapp storage-pools update` (`[STORAGE_POOL](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#STORAGE_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--location)`=`LOCATION`) [`[--active-directory](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--active-directory)`=`ACTIVE_DIRECTORY`] [`[--allow-auto-tiering](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--allow-auto-tiering)`=`ALLOW_AUTO_TIERING`] [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--async)`] [`[--capacity](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--capacity)`=`CAPACITY`] [`[--description](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--description)`=`DESCRIPTION`] [`[--replica-zone](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--replica-zone)`=`REPLICA_ZONE`] [`[--total-iops](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--total-iops)`=`TOTAL_IOPS`] [`[--total-throughput](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--total-throughput)`=`TOTAL_THROUGHPUT`] [`[--update-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--update-labels)`=[`KEY`=`VALUE`,…]] [`[--zone](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--zone)`=`ZONE`] [`[--clear-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--clear-labels)`     | `[--remove-labels](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#--remove-labels)`=[`KEY`,…]] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/update#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Updates a Storage Pool with given arguments

**EXAMPLES**

: The following command updates a Storage Pool named NAME in the given location

```
gcloud netapp storage-pools update NAME --location=us-central1 --capacity=4096 --active-directory=ad-2 --description="new description" --update-labels=key1=val1
```

**POSITIONAL ARGUMENTS**

: **Storage pool resource - The Storage Pool to update. The arguments in this group
can be used to specify the attributes of this resource. (NOTE) Some attributes
are not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `storage_pool` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`STORAGE_POOL`**:
ID of the storage_pool or fully qualified identifier for the storage_pool.
To set the `storage_pool` attribute:

- provide the argument `storage_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--location**:
The location of the storage_pool.
To set the `location` attribute:

- provide the argument `storage_pool` on the command line with a fully
specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.**

**FLAGS**

: **Active directory resource - The Active Directory to attach to the Storage Pool.
This represents a Cloud resource. (NOTE) Some attributes are not given arguments
in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `--active-directory` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

To set the `location` attribute:

- provide the argument `--active-directory` on the command line with a
fully specified name;
- provide the argument `--location` on the command line;
- set the property `netapp/location`.

**--active-directory**:
ID of the active_directory or fully qualified identifier for the
active_directory.
To set the `active_directory` attribute:

- provide the argument `--active-directory` on the command line.**

**--allow-auto-tiering**:
Boolean flag indicating whether Storage Pool is allowed to use auto-tiering

**--async**:
Return immediately, without waiting for the operation in progress to complete.

**--capacity**:
The desired capacity of the Storage Pool in GiB or TiB units.If no capacity unit
is specified, GiB is assumed.

**--description**:
A description of the Cloud NetApp Storage Pool

**--replica-zone**:
String indicating replica zone for the Storage Pool

**--total-iops**:
Integer indicating total IOPS of the Storage Pool

**--total-throughput**:
The total throughput of the Storage Pool in MiB/s or GiB/s units. If no
throughput unit is specified, MiB/s is assumed.

**--update-labels**:
List of label KEY=VALUE pairs to update. If a label exists, its value is
modified. Otherwise, a new label is created.
Keys must start with a lowercase character and contain only hyphens
(`-`), underscores (`_`), lowercase characters, and
numbers. Values must contain only hyphens (`-`), underscores
(`_`), lowercase characters, and numbers.

**--zone**:
String indicating active zone of the Storage Pool

**--clear-labels**

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
gcloud alpha netapp storage-pools update
```

```
gcloud beta netapp storage-pools update
```