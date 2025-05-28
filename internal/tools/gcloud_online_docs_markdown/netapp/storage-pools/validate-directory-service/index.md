# gcloud netapp storage-pools validate-directory-service  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/validate-directory-service](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/validate-directory-service)*

**NAME**

: **gcloud netapp storage-pools validate-directory-service - validate directory service for a Cloud Netapp storage pool**

**SYNOPSIS**

: **`gcloud netapp storage-pools validate-directory-service` (`[STORAGE_POOL](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/validate-directory-service#STORAGE_POOL)` : `[--location](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/validate-directory-service#--location)`=`LOCATION`) [`[--async](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/validate-directory-service#--async)`] [`[--directory-service-type](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/validate-directory-service#--directory-service-type)`=`DIRECTORY_SERVICE_TYPE`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/netapp/storage-pools/validate-directory-service#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Validate the directory service for a Cloud Netapp storage pool.

**EXAMPLES**

: The following command validates the directory service of type ACTIVE_DIRECTORY
for a storage pool named NAME:

```
gcloud netapp storage-pools validate-directory-service NAME --location=us-central1 --directory-service-type=ACTIVE_DIRECTORY
```

**POSITIONAL ARGUMENTS**

: **Storage pool resource - The Storage Pool to validate. The arguments in this
group can be used to specify the attributes of this resource. (NOTE) Some
attributes are not given arguments in this group but can be set in other ways.
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

**--directory-service-type**:
String indicating directory service type for the Storage Pool

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

: This variant is also available:

```
gcloud beta netapp storage-pools validate-directory-service
```