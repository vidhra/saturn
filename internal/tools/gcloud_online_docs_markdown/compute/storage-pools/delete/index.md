# gcloud compute storage-pools delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/delete](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/delete)*

**NAME**

: **gcloud compute storage-pools delete - delete a storage pool**

**SYNOPSIS**

: **`gcloud compute storage-pools delete` (`[STORAGE_POOL](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/delete#STORAGE_POOL)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/delete#--zone)`=`ZONE`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pools/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Deleta a storage pool.

**EXAMPLES**

: To delete a single storage pool named `my-storage-pool`, run the
following command:

```
gcloud compute storage-pools delete my-storage-pool
```

**POSITIONAL ARGUMENTS**

: **Storage pool resource - Name of the storage pool you want to delete. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `storage_pool` on the command line with a fully
specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`STORAGE_POOL`**:
ID of the storage pool or fully qualified identifier for the storage pool.
To set the `storage_pool` attribute:

- provide the argument `storage_pool` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The name of the Google Compute Engine zone.
To set the `zone` attribute:

- provide the argument `storage_pool` on the command line with a fully
specified name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.**

**FLAGS**

: **--async**:
Return immediately, without waiting for the operation in progress to complete.

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
gcloud alpha compute storage-pools delete
```

```
gcloud beta compute storage-pools delete
```