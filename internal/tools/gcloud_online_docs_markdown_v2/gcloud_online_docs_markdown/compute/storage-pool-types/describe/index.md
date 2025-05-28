# gcloud compute storage-pool-types describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/compute/storage-pool-types/describe](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pool-types/describe)*

**NAME**

: **gcloud compute storage-pool-types describe - describe a storage pool type**

**SYNOPSIS**

: **`gcloud compute storage-pool-types describe` (`[STORAGE_POOL_TYPE](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pool-types/describe#STORAGE_POOL_TYPE)` : `[--zone](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pool-types/describe#--zone)`=`ZONE`) [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/compute/storage-pool-types/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Describe a storage pool.

**EXAMPLES**

: To retrieve a single storage pool type and print its properties, run the
following command:

```
gcloud compute storage-pool-types describe my-storage-pool
```

**POSITIONAL ARGUMENTS**

: **Storage pool type resource - Name of the storage pool you want to inspect. The
arguments in this group can be used to specify the attributes of this resource.
(NOTE) Some attributes are not given arguments in this group but can be set in
other ways.
To set the `project` attribute:

- provide the argument `storage_pool_type` on the command line with a
fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

This must be specified.

**`STORAGE_POOL_TYPE`**:
ID of the storage pool type or fully qualified identifier for the storage pool
type.
To set the `storage_pool_type` attribute:

- provide the argument `storage_pool_type` on the command line.

This positional argument must be specified if any of the other arguments in this
group are specified.

**--zone**:
The name of the Google Compute Engine zone.
To set the `zone` attribute:

- provide the argument `storage_pool_type` on the command line with a
fully specified name;
- provide the argument `--zone` on the command line;
- set the property `compute/zone`.**

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
gcloud alpha compute storage-pool-types describe
```

```
gcloud beta compute storage-pool-types describe
```