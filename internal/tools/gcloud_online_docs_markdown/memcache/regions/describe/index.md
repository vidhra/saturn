# gcloud memcache regions describe  |  Google Cloud CLI Documentation

*Source: [https://cloud.google.com/sdk/gcloud/reference/memcache/regions/describe](https://cloud.google.com/sdk/gcloud/reference/memcache/regions/describe)*

**NAME**

: **gcloud memcache regions describe - display metadata for a Memorystore Memcached region**

**SYNOPSIS**

: **`gcloud memcache regions describe` [`[REGION](https://cloud.google.com/sdk/gcloud/reference/memcache/regions/describe#REGION)`] [`[GCLOUD_WIDE_FLAG](https://cloud.google.com/sdk/gcloud/reference/memcache/regions/describe#GCLOUD-WIDE-FLAGS) …`]**

**DESCRIPTION**

: Display all metadata associated with a Memorystore Memcached region given a
valid region name.
This command can fail for the following reasons:

- The region specified does not exist.
- The active account does not have permission to access the given region.

**EXAMPLES**

: To display the metadata for the region `us-central1`, run:

```
gcloud memcache regions describe us-central1
```

**POSITIONAL ARGUMENTS**

: **Region resource - Arguments and flags that specify the Memorystore Memcached
region to describe. This represents a Cloud resource. (NOTE) Some attributes are
not given arguments in this group but can be set in other ways.
To set the `project` attribute:

- provide the argument `region` on the command line with a fully
specified name;
- set the property `memcache/region` with a fully specified name;
- provide the argument `--project` on the command line;
- set the property `core/project`.

**[`REGION`]**:
ID of the region or fully qualified identifier for the region.
To set the `region` attribute:

- provide the argument `region` on the command line;
- set the property `memcache/region`.**

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

: This command uses the `memcache/v1` API. The full documentation for
this API can be found at: [https://cloud.google.com/memorystore/](https://cloud.google.com/memorystore/)

**NOTES**

: These variants are also available:

```
gcloud alpha memcache regions describe
```

```
gcloud beta memcache regions describe
```