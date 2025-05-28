# gcloud netapp storage-pools delete  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/delete](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/delete)*

**NAME**

: **gcloud netapp storage-pools delete - delete a Cloud NetApp Storage Pool**

**SYNOPSIS**

: **`gcloud netapp storage-pools delete` (`[STORAGE_POOL](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/delete#STORAGE_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/delete#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/delete#--async)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/delete#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Delete a Storage Pool

**EXAMPLES**

: The following command deletes a Storage Pool named NAME in the given location

```
gcloud netapp storage-pools delete NAME --location=us-central1
```

To delete a Storage Pool asynchronously, run the following command:

```
gcloud netapp storage-pools delete NAME --location=us-central1 --async
```

**POSITIONAL ARGUMENTS**

: **Storage pool resource - The Storage Pool to delete. The arguments in this group
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

**NOTES**

: These variants are also available:

```
gcloud alpha netapp storage-pools delete
```

```
gcloud beta netapp storage-pools delete
```